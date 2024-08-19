

# APISchool2Summary

APISchool2Summary: A summary of a school record. For the full school record, call /schools/{id}

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**APILocation**](APILocation.md) |  |  [optional] |
|**county** | [**APICounty**](APICounty.md) |  |  [optional] |
|**distance** | **Double** | Distance from nearLatitude/nearLongitude, boundaryLatitude/boundaryLongitude, or boundaryAddress (if supplied) |  [optional] |
|**district** | [**APIDistrictSum**](APIDistrictSum.md) |  |  [optional] |
|**hasBoundary** | **Boolean** | Indicates that an attendance boundary is available for this school. |  [optional] |
|**highGrade** | **String** | The high grade served by this school |  [optional] |
|**isCharterSchool** | **String** | Indicates if school is a charter school (Yes/No/n-a) |  [optional] |
|**isMagnetSchool** | **String** | Indicates if school is a magnet school (Yes/No/n-a) |  [optional] |
|**isPrivate** | **Boolean** | Indicates if school is a private school (Yes/No) |  [optional] |
|**isTitleISchool** | **String** | Indicates if school is a Title I school (Yes/No/n-a) |  [optional] |
|**isTitleISchoolwideSchool** | **String** | Indicates if a school-wide Title I school (Yes/No/n-a) |  [optional] |
|**isVirtualSchool** | **String** | Indicates if school is a virtual school (Yes/No/n-a) |  [optional] |
|**locale** | **String** | NCES Locale of school (https://nces.ed.gov/ccd/rural_locales.asp) |  [optional] |
|**locationIsWithinBoundary** | **Boolean** | Indicates whether this school&#39;s boundary includes the specified location from boundaryLatitude/boundaryLongitude or boundaryAddress. (School Boundary Add-on Package required) |  [optional] |
|**lowGrade** | **String** | The low grade served by this school (PK &#x3D; Prekindergarten, K &#x3D; Kindergarten) |  [optional] |
|**phone** | **String** | School phone number |  [optional] |
|**privateCoed** | **String** | Coed/Boys/Girls (private schools only) |  [optional] |
|**privateDays** | **Integer** | Days in the school year (private schools only) |  [optional] |
|**privateHasLibrary** | **Boolean** | Indicates if the school has a library (private schools only) |  [optional] |
|**privateHours** | **Double** | Hours in the school day (private schools only) |  [optional] |
|**privateOrientation** | **String** | Affiliation of the school (private schools only) |  [optional] |
|**rankHistory** | [**List&lt;APIRankHistory&gt;**](APIRankHistory.md) | SchoolDigger yearly rank history of the school. To retrieve all years, call /schools/{id}. |  [optional] |
|**rankMovement** | **Integer** | Returns the movement of rank for this school between current and previous year |  [optional] |
|**schoolLevel** | **String** | The level of school (Elementary, Middle, High, Private, Alternative) |  [optional] |
|**schoolName** | **String** | School name |  [optional] |
|**schoolYearlyDetails** | [**List&lt;APIYearlyDemographics&gt;**](APIYearlyDemographics.md) | School Yearly metrics. To retrieve all years, call /schools/{id}. |  [optional] |
|**schoolid** | **String** | SchoolDigger School ID Number (12 digits) |  [optional] |
|**url** | **String** | SchoolDigger URL for this school |  [optional] |
|**urlCompare** | **String** | SchoolDigger URL for comparing this school to nearby schools |  [optional] |



