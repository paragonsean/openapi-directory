# SchoolDiggerApiV1.APISchool1Summary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**APILocation**](APILocation.md) |  | [optional] 
**county** | [**APICounty**](APICounty.md) |  | [optional] 
**distance** | **Number** | Distance from nearLatitude/nearLongitude (if supplied) | [optional] 
**district** | [**APIDistrictSum**](APIDistrictSum.md) |  | [optional] 
**hasBoundary** | **Boolean** | Indicates that an attendance boundary is available for this school. | [optional] 
**highGrade** | **String** | The high grade served by this school | [optional] 
**isCharterSchool** | **String** | Indicates if school is a charter school (Yes/No/n-a) | [optional] 
**isMagnetSchool** | **String** | Indicates if school is a magnet school (Yes/No/n-a) | [optional] 
**isPrivate** | **Boolean** | Indicates if school is a private school (Yes/No) | [optional] 
**isTitleISchool** | **String** | Indicates if school is a Title I school (Yes/No/n-a) | [optional] 
**isTitleISchoolwideSchool** | **String** | Indicates if a school-wide Title I school (Yes/No/n-a) | [optional] 
**isVirtualSchool** | **String** | Indicates if school is a virtual school (Yes/No/n-a) | [optional] 
**locationIsWithinBoundary** | **Boolean** | Indicates whether this school&#39;s boundary includes the specified location from nearLatitude/nearLongitude or boundaryAddress. (Enterprise API level only) | [optional] 
**lowGrade** | **String** | The low grade served by this school (PK &#x3D; Prekindergarten, K &#x3D; Kindergarten) | [optional] 
**phone** | **String** | School phone number | [optional] 
**privateCoed** | **String** | Coed/Boys/Girls (private schools only) | [optional] 
**privateDays** | **Number** | Days in the school year (private schools only) | [optional] 
**privateHasLibrary** | **Boolean** | Indicates if the school has a library (private schools only) | [optional] 
**privateHours** | **Number** | Hours in the school day (private schools only) | [optional] 
**privateOrientation** | **String** | Affiliation of the school (private schools only) | [optional] 
**rankHistory** | [**[APIRankHistory]**](APIRankHistory.md) | SchoolDigger yearly rank history of the school. To retrieve all years, call /schools/{id}. | [optional] 
**rankMovement** | **Number** | Returns the movement of rank for this school between current and previous year | [optional] 
**schoolLevel** | **String** | The level of school (Elementary, Middle, High, Private, Alternative) | [optional] 
**schoolName** | **String** | School name | [optional] 
**schoolYearlyDetails** | [**[APIYearlyDemographics]**](APIYearlyDemographics.md) | School Yearly metrics. To retrieve all years, call /schools/{id}. | [optional] 
**schoolid** | **String** | SchoolDigger School ID Number (12 digits). Use /schools/{schoolID} to retrieve the full school record | [optional] 
**url** | **String** | SchoolDigger URL for this school | [optional] 
**urlCompare** | **String** | SchoolDigger URL for comparing this school to others | [optional] 


