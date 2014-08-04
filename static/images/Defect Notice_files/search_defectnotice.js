/**
 * Created by anithrao on 4/25/14.
 */

 // on search submit
function test_submit() {
    //alert(" in search submit");
    var defectdetails= $("#id_defectdetails").val();
    //alert(defectdetails);
    $("#search-results").load("/defect_notice/search_defectnotice?ajax&defectdetails=" + encodeURIComponent(defectdetails));

    return false;
}


// document ready
$(document).ready(function () {
    //alert("hi");
    $("#SearchDefectForm_form").submit(test_submit);
//    $("#search-results").load("/search?ajax&defectdetails=" + encodeURIComponent(defectdetails));
});
