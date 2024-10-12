

# ReportGoogleLocationRequest

Request message for reporting a GoogleLocation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**locationGroupName** | **String** | Optional. The resource name of the location group that this Google Location is being reported for, in the format &#x60;accounts/{account_id}&#x60;. |  [optional] |
|**reportReasonBadLocation** | [**ReportReasonBadLocationEnum**](#ReportReasonBadLocationEnum) | The reason for which the user is reporting this location when the issue is with the location itself. |  [optional] |
|**reportReasonBadRecommendation** | [**ReportReasonBadRecommendationEnum**](#ReportReasonBadRecommendationEnum) | The reason for which the user is reporting this location when the issue is with the recommendation. This report is useful if the location has been recommended to the Business Profile account. |  [optional] |
|**reportReasonElaboration** | **String** | Optional. A text entry for elaborating on the reason for which the user is reporting this location. The maximum length is 512 characters. |  [optional] |
|**reportReasonLanguageCode** | **String** | Optional. The BCP 47 code of language used in &#x60;report_reason_elaboration&#x60;. |  [optional] |



## Enum: ReportReasonBadLocationEnum

| Name | Value |
|---- | -----|
| BAD_LOCATION_REASON_UNSPECIFIED | &quot;BAD_LOCATION_REASON_UNSPECIFIED&quot; |
| NOT_A_LOCATION | &quot;NOT_A_LOCATION&quot; |
| PERMANENTLY_CLOSED | &quot;PERMANENTLY_CLOSED&quot; |
| DOES_NOT_EXIST | &quot;DOES_NOT_EXIST&quot; |
| SPAM | &quot;SPAM&quot; |
| NOT_A_BUSINESS | &quot;NOT_A_BUSINESS&quot; |
| MOVED | &quot;MOVED&quot; |
| DUPLICATE | &quot;DUPLICATE&quot; |



## Enum: ReportReasonBadRecommendationEnum

| Name | Value |
|---- | -----|
| BAD_RECOMMENDATION_REASON_UNSPECIFIED | &quot;BAD_RECOMMENDATION_REASON_UNSPECIFIED&quot; |
| NOT_A_STORE_FRONT | &quot;NOT_A_STORE_FRONT&quot; |
| NOT_PART_OF_SUGGESTED_CHAIN | &quot;NOT_PART_OF_SUGGESTED_CHAIN&quot; |
| IRRELEVANT | &quot;IRRELEVANT&quot; |



