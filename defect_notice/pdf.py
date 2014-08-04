__author__ = 'anithrao'

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ParagraphAndImage,ParaLines, ParaFrag
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from models import *
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch,cm,mm
from reportlab.pdfgen import canvas

class MyPdf:
    def __init__(self, buffer, pagesize):
        self.buffer = buffer
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
        self.width, self.height = self.pagesize

    @staticmethod
    def _header_footer(canvas, doc):
        # Save the state of our canvas so we can draw on it
        canvas.saveState()
        styles = getSampleStyleSheet()

        # Header
        header = Paragraph('Field Defect Notice', styles['Title'])
        w, h = header.wrap(doc.width, doc.topMargin)
        header.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - h+25)

        # Footer
        footer = Paragraph('Contact Information:<br/> If you have any questions, please contact <a href="mailto:msantori@amazon.com?Subject=FieldDefectNotice"><u>Matthew Santori</u></a> or <a href="mailto:msstark@amazon.com?Subject=FieldDefectNotice"><u>Michael Stark</u></a>.<br />Amazon.com - Confidential - Do not Distribute', styles['Normal'])
        w, h = footer.wrap(doc.width, doc.bottomMargin)
        footer.drawOn(canvas, doc.leftMargin, h)

        # Release the canvas
        canvas.restoreState()

    def pdfgenerate_fdn(self, getid):
            buffer = self.buffer
            doc = SimpleDocTemplate(buffer,
                                    rightMargin=72,
                                    leftMargin=72,
                                    topMargin=72,
                                    bottomMargin=72,
                                    pagesize=self.pagesize)

            # Our container for 'Flowable' objects
            elements = []

            # A large collection of style sheets pre-made for us
            styles = getSampleStyleSheet()
            styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER, ))

            # Draw things on the PDF. Here's where the PDF generation happens.
            # See the ReportLab documentation for the full list of functionality.
            defectdetails = DefectDetails.objects.all().filter(id = getid)
            #elements.append(Paragraph('Field Defect Notice', styles['Title']))
            for i, each in enumerate(defectdetails):
                s = Spacer(1, 0.25*inch)

                # elements.append(Paragraph('Defect Added By: ' + each.username, styles['Heading3']))
                # elements.append(Paragraph(each.username, styles['Normal']))
                # elements.append(s)
                elements.append(Paragraph('Defect Added By: ' + each.username, styles['Heading3']))
                elements.append(Paragraph('Site/s: ' + ''+ each.site, styles['Normal']))

                elements.append(s)

                elements.append(Paragraph('Source of Indication: ' +  each.defectSource_id.defectSource, styles['Normal']))
                # elements.append(Paragraph(each.defectSource_id.defectSource, styles['Normal']))
                elements.append(s)

                elements.append(Paragraph('Incident Date: ' + each.incidentDate.strftime('%m-%d-%Y'), styles['Normal']))
                # elements.append(Paragraph(each.incidentDate.strftime('%m-%d-%Y'), styles['Normal']))
                elements.append(s)

                if each.critical == 0:
                    critical = 'No'
                else:
                    critical  = 'Yes'
                elements.append(Paragraph('Critical load loss: ' + critical, styles['Normal']))
                # elements.append(Paragraph(critical, styles['Normal']))
                elements.append(s)

                if each.largeScale == 0:
                    largeScale = 'No'
                else:
                    largeScale  = 'Yes'
                elements.append(Paragraph('Large Scale Event: ' + largeScale, styles['Normal']))
                # elements.append(Paragraph(largeScale, styles['Normal']))
                elements.append(s)

                elements.append(Paragraph('Infrastructure System: ' + each.infrastructureSystem_id.systemAsset, styles['Normal']))
                # elements.append(Paragraph(each.infrastructureSystem_id.systemAsset, styles['Normal']))
                elements.append(s)

                elements.append(Paragraph('Infrastructure Division: ' + each.infrastructureDivision_id.divisionAsset, styles['Normal']))
                # elements.append(Paragraph(each.infrastructureDivision_id.divisionAsset, styles['Normal']))
                elements.append(s)

                elements.append(Paragraph('Infrastructure Subsystem: ' + each.infrastructureSubsystem, styles['Normal']))
                # elements.append(Paragraph(each.infrastructureSubsystem, styles['Normal']))
                elements.append(s)

                elements.append(Paragraph('Manufacturer: ' + each.assetManufacturer, styles['Normal']))
                # elements.append(Paragraph(each.assetManufacturer, styles['Normal']))
                elements.append(s)

                elements.append(Paragraph('Model Number: ' + each.assetModelNumber, styles['Normal']))
                # elements.append(Paragraph(each.assetModelNumber, styles['Normal']))
                elements.append(s)

                elements.append(Paragraph('Reference file: ' + each.filename, styles['Normal']))
                # elements.append(Paragraph( each.filename, styles['Normal']))
                elements.append(s)

                elements.append(Paragraph('Defect Synopsis: ', styles['Normal']))
                elements.append(Paragraph(each.defectSynopsis, styles['Normal']))
                elements.append(s)

            doc.build(elements, onFirstPage=self._header_footer, onLaterPages=self._header_footer,
                  canvasmaker=NumberedCanvas)
            #doc.build(elements, onFirstPage=self._header_footer, onLaterPages=self._header_footer)
            # doc.build(elements)

            # Get the value of the BytesIO buffer and write it to the response.
            pdf = buffer.getvalue()
            buffer.close()
            return pdf

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        # Change the position of this to wherever you want the page number to be
        self.drawRightString(211 * mm, 15 * mm + (0.2 * inch),
                             "Page %d of %d" % (self._pageNumber, page_count))


