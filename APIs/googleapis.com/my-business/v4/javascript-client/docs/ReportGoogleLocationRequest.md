# GoogleMyBusinessApi.ReportGoogleLocationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locationGroupName** | **String** | Optional. The resource name of the location group that this Google Location is being reported for, in the format &#x60;accounts/{account_id}&#x60;. | [optional] 
**reportReasonBadLocation** | **String** | The reason for which the user is reporting this location when the issue is with the location itself. | [optional] 
**reportReasonBadRecommendation** | **String** | The reason for which the user is reporting this location when the issue is with the recommendation. This report is useful if the location has been recommended to the Business Profile account. | [optional] 
**reportReasonElaboration** | **String** | Optional. A text entry for elaborating on the reason for which the user is reporting this location. The maximum length is 512 characters. | [optional] 
**reportReasonLanguageCode** | **String** | Optional. The BCP 47 code of language used in &#x60;report_reason_elaboration&#x60;. | [optional] 



## Enum: ReportReasonBadLocationEnum


* `BAD_LOCATION_REASON_UNSPECIFIED` (value: `"BAD_LOCATION_REASON_UNSPECIFIED"`)

* `NOT_A_LOCATION` (value: `"NOT_A_LOCATION"`)

* `PERMANENTLY_CLOSED` (value: `"PERMANENTLY_CLOSED"`)

* `DOES_NOT_EXIST` (value: `"DOES_NOT_EXIST"`)

* `SPAM` (value: `"SPAM"`)

* `NOT_A_BUSINESS` (value: `"NOT_A_BUSINESS"`)

* `MOVED` (value: `"MOVED"`)

* `DUPLICATE` (value: `"DUPLICATE"`)





## Enum: ReportReasonBadRecommendationEnum


* `BAD_RECOMMENDATION_REASON_UNSPECIFIED` (value: `"BAD_RECOMMENDATION_REASON_UNSPECIFIED"`)

* `NOT_A_STORE_FRONT` (value: `"NOT_A_STORE_FRONT"`)

* `NOT_PART_OF_SUGGESTED_CHAIN` (value: `"NOT_PART_OF_SUGGESTED_CHAIN"`)

* `IRRELEVANT` (value: `"IRRELEVANT"`)




