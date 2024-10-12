

# APIDistrict12


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**APILocation**](APILocation.md) |  |  [optional] |
|**boundary** | [**APIBoundary12**](APIBoundary12.md) |  |  [optional] |
|**county** | [**APICounty**](APICounty.md) |  |  [optional] |
|**districtID** | **String** | SchoolDigger District ID Number (7 digits) |  [optional] |
|**districtName** | **String** | District name |  [optional] |
|**districtYearlyDetails** | [**List&lt;APILEAYearlyDetail&gt;**](APILEAYearlyDetail.md) | District yearly metrics |  [optional] |
|**highGrade** | **String** | The high grade served by this district |  [optional] |
|**isWithinBoundary** | **Boolean** | Indicates whether this district&#39;s boundary includes the specified location from nearLatitude/nearLongitude |  [optional] |
|**lowGrade** | **String** | The low grade served by this district (PK &#x3D; Prekindergarten, K &#x3D; Kindergarten) |  [optional] |
|**numberAlternativeSchools** | **Integer** |  |  [optional] |
|**numberHighSchools** | **Integer** |  |  [optional] |
|**numberMiddleSchools** | **Integer** |  |  [optional] |
|**numberPrimarySchools** | **Integer** |  |  [optional] |
|**numberTotalSchools** | **Integer** |  |  [optional] |
|**phone** | **String** | District phone number |  [optional] |
|**rankHistory** | [**List&lt;APILEARankHistory&gt;**](APILEARankHistory.md) | SchoolDigger yearly rank history of the district |  [optional] |
|**testScores** | [**List&lt;APITestScoreWrapper&gt;**](APITestScoreWrapper.md) | Test scores (district and state) -- requires Pro or Enterprise level API subscription |  [optional] |
|**url** | **String** | SchoolDigger URL for this district |  [optional] |



