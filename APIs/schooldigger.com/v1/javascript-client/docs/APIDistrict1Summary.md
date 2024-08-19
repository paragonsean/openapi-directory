# SchoolDiggerApiV1.APIDistrict1Summary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**APILocation**](APILocation.md) |  | [optional] 
**county** | [**APICounty**](APICounty.md) |  | [optional] 
**distance** | **Number** | Distance from nearLatitude/nearLongitude (if supplied) | [optional] 
**districtID** | **String** | SchoolDigger District ID Number (7 digits). Use /districts/{districtID} to retrieve the entire district record | [optional] 
**districtName** | **String** | District name | [optional] 
**districtYearlyDetails** | [**[APILEAYearlyDetail]**](APILEAYearlyDetail.md) | District yearly metrics | [optional] 
**hasBoundary** | **Boolean** | Indicates that an attendance boundary is available for this district. (To retrieve, look up district with /districts/{id}) | [optional] 
**highGrade** | **String** | The high grade served by this district | [optional] 
**isWithinBoundary** | **Boolean** | Indicates whether this district&#39;s boundary includes the specified location from nearLatitude/nearLongitude | [optional] 
**locationIsWithinBoundary** | **Boolean** | Indicates whether this school&#39;s boundary includes the specified location from nearLatitude/nearLongitude or boundaryAddress (Enterprise API level) | [optional] 
**lowGrade** | **String** | The low grade served by this district (PK &#x3D; Prekindergarten, K &#x3D; Kindergarten) | [optional] 
**numberAlternativeSchools** | **Number** | Count of schools designated as other/alternative schools | [optional] 
**numberHighSchools** | **Number** | Count of schools designated as high schools | [optional] 
**numberMiddleSchools** | **Number** | Count of schools designated as middle schools | [optional] 
**numberPrimarySchools** | **Number** | Count of schools designated as primary schools | [optional] 
**numberTotalSchools** | **Number** | Count of schools in the district | [optional] 
**phone** | **String** | District phone number | [optional] 
**rankHistory** | [**[APILEARankHistory]**](APILEARankHistory.md) | SchoolDigger yearly rank history of the district | [optional] 
**url** | **String** | SchoolDigger URL for this district | [optional] 


