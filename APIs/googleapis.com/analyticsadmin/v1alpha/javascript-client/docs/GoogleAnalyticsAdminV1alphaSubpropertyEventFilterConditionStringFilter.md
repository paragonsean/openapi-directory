# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1alphaSubpropertyEventFilterConditionStringFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caseSensitive** | **Boolean** | Optional. If true, the string value is case sensitive. If false, the match is case-insensitive. | [optional] 
**matchType** | **String** | Required. The match type for the string filter. | [optional] 
**value** | **String** | Required. The string value used for the matching. | [optional] 



## Enum: MatchTypeEnum


* `MATCH_TYPE_UNSPECIFIED` (value: `"MATCH_TYPE_UNSPECIFIED"`)

* `EXACT` (value: `"EXACT"`)

* `BEGINS_WITH` (value: `"BEGINS_WITH"`)

* `ENDS_WITH` (value: `"ENDS_WITH"`)

* `CONTAINS` (value: `"CONTAINS"`)

* `FULL_REGEXP` (value: `"FULL_REGEXP"`)

* `PARTIAL_REGEXP` (value: `"PARTIAL_REGEXP"`)




