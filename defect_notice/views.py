# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage
#the below import is needed to load AJAX:
from django.template.loader import get_template
from django.core.context_processors import csrf
from defect_notice.forms import *
from defect_notice.models import *
import json
from django.core import mail
from django.core.mail import send_mail
import datetime
from django.core.exceptions import ObjectDoesNotExist

from pdf import MyPdf

from io import BytesIO

# Create your views here.
def check_user(request):
    #user = request.META.get('REMOTE_USER')
    user = request.META.get('USER')

    try:
        #checkuser = LoginLookup.objects.get(username=user)
        form = DefectForm()
        #
        # Bad form (or form details), no form supplied...
        # Render the form with error messages (if any).
        # return render_to_response('defect_notice/add.html', {'form': form }, context_instance=RequestContext(request))
        return add(request)
    except ObjectDoesNotExist:
        checkuser = None
        # msg='Permission denied'
        form = DefectForm()
        js = 'js'
        variables = RequestContext(request, {'form':form, 'js':js })
    return render_to_response('defect_notice/add.html', variables)

def test(request):
    return HttpResponse("testing defect_notice application: Passed")

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('defect_notice/index.html', context_dict, context)

def about(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'aboutmessage': "About page - defect notice coming"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('defect_notice/about.html', context_dict)
    #return HttpResponse("About page - defect notice coming")

def add(request):
    # Get the context from the request.
    context = RequestContext(request)
    # A HTTP POST?
    if request.method == 'POST':
        if 'referenceFile' in request.FILES:
            form = DefectForm(request.POST, request.FILES)
            if form.is_valid():
                #parse the dict and remove unicode characters
                # get_username = form.cleaned_data['user_name']
                get_username = request.META.get('USER')
                #getuser = LoginLookup.objects.get(username=get_username)

                get_dict = form.cleaned_data['site_multi']
                my_values = get_dict.values()
                #print my_values

                mylist=[]
                for i in my_values:
                    mylist.append(i['siteCode'])
                mystr = ', '.join(mylist)
                print mystr

                #send the righr email address
                #get_username = form.cleaned_data['user_name']
                my_email = str(get_username) + '@amazon.com'
                #print my_email siteCode- {SiteDetailsLookup} IAD1

                save_username = get_username
                save_site = mystr
                save_tt_number = form.cleaned_data['tt_number']
                save_incident_date = form.cleaned_data['incident_date']
                save_defect_source = form.cleaned_data['indicator_source']
                save_critical = form.cleaned_data['critical_load']
                save_large_scale = form.cleaned_data['large_scale']
                save_division_asset = form.cleaned_data['division_asset']
                save_system_asset = form.cleaned_data['system_asset']
                save_subsystem_asset = form.cleaned_data['subsystem_asset']
                save_manufacturer_asset = form.cleaned_data['manufacturer_asset']
                save_model_number = form.cleaned_data['model_number']
                save_file = request.FILES['referenceFile']
                save_filename = request.FILES['referenceFile'].name
                save_defect_synopsis = form.cleaned_data['defect_synopsis']
                save_email = my_email
                save_approved = False
                save_approvalDate = form.cleaned_data['approvalDate']

                bool_critical= parseUnicodetoBool(save_critical)

                bool_largeScale= parseUnicodetoBool(save_large_scale)

                defectnotice = DefectDetails(username=save_username,  site=save_site, ttnumber=save_tt_number,
                                             incidentDate=save_incident_date, defectSource_id=save_defect_source,
                                             critical=bool_critical, largeScale=bool_largeScale,
                                             infrastructureDivision_id=save_division_asset,
                                             infrastructureSystem_id=save_system_asset,
                                             infrastructureSubsystem=save_subsystem_asset,
                                             assetManufacturer=save_manufacturer_asset, assetModelNumber=save_model_number,
                                             referenceFile=save_file, filename=save_filename,
                                             defectSynopsis=save_defect_synopsis,notifierEmail=save_email,
                                             approved=save_approved, approvalDate=save_approvalDate)
                defectnotice.save()

                defectnotice_id = defectnotice._get_pk_val()
                msg1 = "Approval required for Defect Notice ID: " + str(defectnotice_id) + '\n' + "To approve go to:" + '\n' + "https://" + str(request.META['HTTP_HOST']) + "/defect_notice/search" + '\n' + "Search for the ID number provided." + '\n' +  '\n' + '\n' + "DC Quality & Site Reliability team"
                email_from = str(my_email)
                email_to = ['dcq-sr@amazon.com']

                connection = mail.get_connection()
                # Manually open the connection
                connection.open()
                # Construct two more messages
                email1 = mail.EmailMessage('DCQSR - Defect Notice Approval Notification', msg1, email_from, email_to)
                connection.send_messages([email1])
                # The connection was already open so send_messages() doesn't close it.
                # We need to manually close the connection.
                connection.close()
                msg = "Successfully added Defect Notice ID: " + str(defectnotice_id)

                variables = RequestContext(request, {'form': form, 'msg': msg })
                return render_to_response('defect_notice/add.html', variables)
            else:
                #print form.errors
                form.errors
        else:
            form = DefectForm(request.POST)
            if form.is_valid():
                #parse the dict and remove unicode characters
                # get_username = form.cleaned_data['user_name']
                get_username = request.META.get('USER')
                #getuser = LoginLookup.objects.get(username=get_username)

                get_dict = form.cleaned_data['site_multi']
                my_values = get_dict.values()
                #print my_values

                mylist=[]
                for i in my_values:
                    mylist.append(i['siteCode'])
                mystr = ', '.join(mylist)
                print mystr

                #send the righr email address
                #get_username = form.cleaned_data['user_name']
                my_email = str(get_username) + '@amazon.com'
                #print my_email siteCode- {SiteDetailsLookup} IAD1

                save_username = get_username
                save_site = mystr
                save_tt_number = form.cleaned_data['tt_number']
                save_incident_date = form.cleaned_data['incident_date']
                save_defect_source = form.cleaned_data['indicator_source']
                save_critical = form.cleaned_data['critical_load']
                save_large_scale = form.cleaned_data['large_scale']
                save_division_asset = form.cleaned_data['division_asset']
                save_system_asset = form.cleaned_data['system_asset']
                save_subsystem_asset = form.cleaned_data['subsystem_asset']
                save_manufacturer_asset = form.cleaned_data['manufacturer_asset']
                save_model_number = form.cleaned_data['model_number']
                save_file = form.cleaned_data['referenceFile']
                save_filename = form.cleaned_data['filename']
                save_defect_synopsis = form.cleaned_data['defect_synopsis']
                save_email = my_email
                save_approved = False
                save_approvalDate = form.cleaned_data['approvalDate']

                bool_critical= parseUnicodetoBool(save_critical)

                bool_largeScale= parseUnicodetoBool(save_large_scale)

                defectnotice = DefectDetails(username=save_username,  site=save_site, ttnumber=save_tt_number,
                                             incidentDate=save_incident_date, defectSource_id=save_defect_source,
                                             critical=bool_critical, largeScale=bool_largeScale,
                                             infrastructureDivision_id=save_division_asset,
                                             infrastructureSystem_id=save_system_asset,
                                             infrastructureSubsystem=save_subsystem_asset,
                                             assetManufacturer=save_manufacturer_asset, assetModelNumber=save_model_number,
                                             referenceFile=save_file, filename=save_filename,
                                             defectSynopsis=save_defect_synopsis,notifierEmail=save_email,
                                             approved=save_approved, approvalDate=save_approvalDate)
                defectnotice.save()

                defectnotice_id = defectnotice._get_pk_val()
                msg1 = "Approval required for Defect Notice ID: " + str(defectnotice_id) + '\n' + "To approve go to:" + '\n' + "https://" + str(request.META['HTTP_HOST']) + "/defect_notice/search" + '\n' + "Search for the ID number provided." + '\n' +  '\n' + '\n' + "DC Quality & Site Reliability team"
                email_from = str(my_email)
                email_to = ['dcq-sr@amazon.com']

                connection = mail.get_connection()
                # Manually open the connection
                connection.open()
                # Construct two more messages
                email1 = mail.EmailMessage('DCQSR - Defect Notice Approval Notification', msg1, email_from, email_to)
                pdf=pdfserve_fdn(request, defectnotice_id)
                email1.attach('fdn.pdf',pdf,'application/pdf')
                connection.send_messages([email1])
                # The connection was already open so send_messages() doesn't close it.
                # We need to manually close the connection.
                connection.close()
                msg = "Successfully added Defect Notice ID: " + str(defectnotice_id)

                variables = RequestContext(request, {'form': form, 'msg': msg })
                return render_to_response('defect_notice/add.html', variables)
            else:
                #print form.errors
                form.errors

    else:
        form = DefectForm()
    #
    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('defect_notice/add.html', {'form': form }, context_instance=RequestContext(request))

def search(request):
    show_result = False
    if request.method == 'POST':
        form = SearchDefectForm(request.POST)
        if form.is_valid():
            my_defectid = form.cleaned_data['id']
            try:
                my_search = DefectDetails.objects.get(id=my_defectid)
                if my_search.approved:
                    form = SearchDefectForm()
                    msg = "Already approved ID:" + str(my_defectid)
                    variables = RequestContext(request, {'form':form, 'msg': msg})
                    return render_to_response('defect_notice/search.html', variables)
                show_result = True

                my_critical = my_search.critical
                ucode_critical= parseBooltoUnicode(my_critical)

                my_largeScale = my_search.largeScale
                ucode_largeScale= parseBooltoUnicode(my_largeScale)


                my_approved = my_search.approved
                ucode_approved= parseBooltoUnicode(my_approved)

                hiddenfile = '/media/FDN/' +str(my_search.filename)
                mydata={'id': my_search.id, 'username': str(my_search.username), 'site': str(my_search.site), 'ttnumber': str(my_search.ttnumber),'infrastructureDivision_id':str(my_search.infrastructureDivision_id._get_pk_val()),
                                 'infrastructureSystem_id': str(my_search.infrastructureSystem_id._get_pk_val()), 'infrastructureSubsystem': str(my_search.infrastructureSubsystem),
                                 'incidentDate': str(my_search.incidentDate.strftime('%m-%d-%Y')), 'defectSource_id': my_search.defectSource_id._get_pk_val(),
                                 'critical': ucode_critical,'largeScale': ucode_largeScale, 'assetManufacturer': str(my_search.assetManufacturer),
                                 'assetModelNumber': str(my_search.assetModelNumber), 'filename': str(my_search.filename),
                                 'defectSynopsis': str(my_search.defectSynopsis),
                                 'notifierEmail': str(my_search.notifierEmail), 'approved': ucode_approved,
                                 'approvalDate' : str(my_search.approvalDate.strftime('%m-%d-%Y'))}

                show_result = True
                myform = ApproveDefectForm(mydata)
                form = SearchDefectForm()
                variables = RequestContext(request, {'my_search': my_search,
                                                     'hiddenfile': hiddenfile,
                                                     'show_result': show_result,
                                                     'form': form,
                                                     'myform': myform
                                                    })
                return render_to_response('defect_notice/search.html', variables)
            except DefectDetails.DoesNotExist:
                #raise Http404
                form = SearchDefectForm()
                msg = "Check your input, Id does not exist."
                variables = RequestContext(request, {'form':form, 'msg': msg})
            return render_to_response('defect_notice/search.html', variables)
        else:
            form = SearchDefectForm()
            msg = "invalid Input"
            errors = form.errors
            variables = RequestContext(request, {'form': form, 'msg': msg, 'errors': errors})
            return render_to_response('defect_notice/search.html', variables)
    else:
        form = SearchDefectForm()

        variables = RequestContext(request, {'form': form })
        return render_to_response('defect_notice/search.html', variables)

def approve(request):
    if 'id' in request.POST:
        form = ApproveDefectForm(request.POST)
        if form.is_valid():

            my_defectid = form.cleaned_data['id']

            # if form.is_valid():
            #     #parse the dict and remove unicode characters
            #     get_site = form.cleaned_data['site']
            #     my_values = get_site.values()
            #     #print my_values
            #
            #     for i in my_values:
            #         mylist.append(i['siteCode'])
            #     mystr = ', '.join(mylist)
            #     #print mystr

            my_critical = form.cleaned_data['critical']
            bool_critical= parseUnicodetoBool(my_critical)

            my_largeScale = form.cleaned_data['largeScale']
            bool_largeScale= parseUnicodetoBool(my_largeScale)

            my_approved = form.cleaned_data['approved']
            bool_approved= parseUnicodetoBool(my_approved)

            myDefect = DefectDetails.objects.get(id=my_defectid)

            myDefect.approved = bool_approved
            myDefect.username = form.cleaned_data['username']
            myDefect.site = form.cleaned_data['site']
            myDefect.ttnumber = form.cleaned_data['ttnumber']
            myDefect.infrastructureDivision_id = form.cleaned_data['infrastructureDivision_id']
            myDefect.infrastructureSystem_id = form.cleaned_data['infrastructureSystem_id']
            myDefect.infrastructureSubsystem = form.cleaned_data['infrastructureSubsystem']
            myDefect.incidentDate = form.cleaned_data['incidentDate']
            myDefect.defectSource_id = form.cleaned_data['defectSource_id']
            myDefect.critical = bool_critical
            myDefect.largeScale = bool_largeScale
            myDefect.assetManufacturer = form.cleaned_data['assetManufacturer']
            myDefect.assetModelNumber = form.cleaned_data['assetModelNumber']
            myDefect.filename = form.cleaned_data['filename']
            myDefect.defectSynopsis = form.cleaned_data['defectSynopsis']
            myDefect.notifierEmail = form.cleaned_data['notifierEmail']
            myDefect.approvalDate = form.cleaned_data['approvalDate']



            myDefect.save()

            form=SearchDefectForm()

            getDefectApproval = DefectDetails.getapproved(myDefect)
            if getDefectApproval == True:
                defectnotice_id = myDefect._get_pk_val()
                #pdfgenerate_fdn(request,defectnotice_id)

                # msg1 = "Defect Notice ID: " + str(defectnotice_id) + " has been approved." + '\n' + "View Report here: " + str(request.META['HTTP_HOST']) + "/defect_notice/report" + '\n' +  '\n' + '\n' + "DC Quality & Site Reliability team"
                # email_to = ['dcq-sr@amazon.com']

                # #email_to = ['dceo-iad-am@amazon.com', 'iad-dceo-fm@amazon.com']
                # connection = mail.get_connection()
                # # Manually open the connection
                # connection.open()
                # # Construct two more messages
                # email1 = mail.EmailMessage('DCQSR - Defect Notice Approval Notification', msg1, 'dcq-sr@amazon.com', email_to)
                #pdf=pdfserve_fdn(request, defectnotice_id)
                #email1.attach('fdn.pdf',pdf,'application/pdf')
                # connection.send_messages([email1])
                # # The connection was already open so send_messages() doesn't close it.
                # # We need to manually close the connection.
                # connection.close()
                successmsg = "Approved Defect Notice : " + str(my_defectid)
            else:
                successmsg = "Not Approved Defect Notice : " + str(my_defectid)

            #successmsg = "Approved Defect Notice for: " + str(my_defectid)
            variables = RequestContext(request, {'form': form,'successmsg': successmsg})
            return render_to_response('defect_notice/search.html', variables)
        else:
            print form.errors
            #errors = form.errors
            form = SearchDefectForm()
            form1 = ApproveDefectForm()
            msg = "Invalid Approval form. One or more form fields were empty. Start your search again."

            variables = RequestContext(request, {'form': form, 'form1': form1, 'msg': msg})
            return render_to_response('defect_notice/search.html', variables, context_instance=RequestContext(request))

    else:
        form = SearchDefectForm()
        form1 = ApproveDefectForm()
        msg = "Invalid form"
        errors = form.errors
        variables = RequestContext(request, {'form': form, 'form1': form1, 'msg': msg, 'errors': errors})
        return render_to_response('defect_notice/search.html', variables, context_instance=RequestContext(request))



def pdfserve_fdn(request,id):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="fdn.pdf"'

    response['Content-Disposition'] = 'filename="fdn.pdf"'

    buffer = BytesIO()

    report = MyPdf(buffer, 'Letter')
    pdf = report.pdfgenerate_fdn(id)

    response.write(pdf)
    return response



def report_defectnotice(request):
    context = RequestContext(request)
    rptresult = False
    select_all = DefectDetails.objects.all().filter(approved=1)

    result_list=[]
    for each in select_all:
        result_dict = {}
        result_dict['id'] = each.id
        result_dict['username'] = each.username
        result_dict['site'] = each.site
        result_dict['infrastructureDivision_id'] = each.infrastructureDivision_id
        result_dict['infrastructureSystem_id'] = each.infrastructureSystem_id
        result_dict['infrastructureSubsystem'] = each.infrastructureSubsystem
        result_dict['incidentDate'] = each.incidentDate.strftime('%m-%d-%Y')
        result_dict['defectSource_id'] = each.defectSource_id
        result_dict['critical'] = each.critical
        result_dict['largeScale'] = each.largeScale
        result_dict['assetManufacturer'] = each.assetManufacturer
        result_dict['assetModelNumber'] = each.assetModelNumber
        result_dict['filename'] = each.filename
        result_dict['defectSynopsis'] = each.defectSynopsis
        result_dict['notifierEmail'] = each.notifierEmail

        result_list.append(result_dict)

    #sending this as parameter to the function
    json_populate(request, result_list)
    rptresult = True
     # #pagination
    ITEMS_PER_PAGE = 10

    result_set = result_list
    paginator = Paginator(result_set,ITEMS_PER_PAGE)
    try:
        page_number = int(request.GET['page'])
    except (KeyError, ValueError):
        page_number = 1
    try:
        page = paginator.page(page_number)
    except InvalidPage:
        raise Http404
    response = pdfserve_fdn(request, 1)
    result_list = page.object_list
    meta = request.META['HTTP_HOST']
    variables = RequestContext(request, {'result_list': result_list,
                                         'response': response,
                                         'meta': meta,
                                         'rptresult' : rptresult,
                                         'show_paginator': paginator.num_pages > 0,
                                         'has_prev': page.has_previous(),
                                         'has_next': page.has_next(),
                                         'page': page_number,
                                         'pages': paginator.num_pages,
                                         'next_page': page_number + 1,
                                         'prev_page': page_number - 1
                                        })
    if 'page' > 0:
        return render_to_response('defect_notice/report.html', variables)
    else:
        rptresult = False
        rptmsg= 'Report is not available'
        variables = RequestContext(request, {'rptresult': rptresult,
                                             'rptmsg': rptmsg})
        return render_to_response('defect_notice/report.html', variables)
        #return HttpResponse(json.dumps(result_list), mimetype='application/json')


def json_populate(request, result_list):
    return result_list

def parseBooltoUnicode(theBool):
    if theBool == False:
        theBool = u'0'
    else:
        theBool = u'1'
    return theBool

def parseUnicodetoBool(theUnicode):
    if theUnicode == u'0':
        theUnicode = False
    else:
        theUnicode = True
    return theUnicode