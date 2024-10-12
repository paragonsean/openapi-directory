

# APISchool20Full


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**APILocation**](APILocation.md) |  |  [optional] |
|**county** | [**APICounty**](APICounty.md) |  |  [optional] |
|**district** | [**APIDistrictSum**](APIDistrictSum.md) |  |  [optional] |
|**finance** | [**List&lt;APISchoolFinance&gt;**](APISchoolFinance.md) | School finance (Pro and Enterprise API level only) |  [optional] |
|**highGrade** | **String** | The high grade served by this school |  [optional] |
|**isCharterSchool** | **String** | Indicates if school is a charter school (Yes/No/n-a) |  [optional] |
|**isMagnetSchool** | **String** | Indicates if school is a magnet school (Yes/No/n-a) |  [optional] |
|**isPrivate** | **Boolean** | Indicates if school is a private school (Yes/No) |  [optional] |
|**isTitleISchool** | **String** | Indicates if school is a Title I school (Yes/No/n-a) |  [optional] |
|**isTitleISchoolwideSchool** | **String** | Indicates if a school-wide Title I school (Yes/No/n-a) |  [optional] |
|**isVirtualSchool** | **String** | Indicates if school is a virtual school (Yes/No/n-a) |  [optional] |
|**locale** | **String** | NCES Locale of school (https://nces.ed.gov/ccd/rural_locales.asp) |  [optional] |
|**lowGrade** | **String** | The low grade served by this school (PK &#x3D; Prekindergarten, K &#x3D; Kindergarten) |  [optional] |
|**phone** | **String** | School phone number |  [optional] |
|**privateCoed** | **String** | Coed/Boys/Girls (private schools only) |  [optional] |
|**privateDays** | **Integer** | Days in the school year (private schools only) |  [optional] |
|**privateHasLibrary** | **Boolean** | Indicates if the school has a library (private schools only) |  [optional] |
|**privateHours** | **Double** | Hours in the school day (private schools only) |  [optional] |
|**privateOrientation** | **String** | Affiliation of the school (private schools only) |  [optional] |
|**rankHistory** | [**List&lt;APIRankHistory&gt;**](APIRankHistory.md) | SchoolDigger yearly rank history of the school |  [optional] |
|**rankMovement** | **Integer** | Returns the movement of rank for this school between current and previous year |  [optional] |
|**reviews** | [**List&lt;APISchoolReview&gt;**](APISchoolReview.md) | List of reviews for this school submitted by SchoolDigger site visitors |  [optional] |
|**schoolLevel** | **String** | The level of school (Elementary, Middle, High, Private, Alternative) |  [optional] |
|**schoolName** | **String** | School name |  [optional] |
|**schoolYearlyDetails** | [**List&lt;APIYearlyDemographics&gt;**](APIYearlyDemographics.md) | School Yearly metrics |  [optional] |
|**schoolid** | **String** | SchoolDigger School ID Number (12 digits) |  [optional] |
|**testScores** | [**List&lt;APITestScoreWrapper&gt;**](APITestScoreWrapper.md) | Test scores (including district and state) -- requires Pro or Enterprise level API subscription |  [optional] |
|**url** | **String** | URL of the school&#39;s public website |  [optional] |
|**urlCompareSchoolDigger** | **String** | SchoolDigger URL for comparing this school to nearby schools |  [optional] |
|**urlSchoolDigger** | **String** | SchoolDigger URL for this school |  [optional] |



