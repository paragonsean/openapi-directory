# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1alphaExpandedDataSetFilterStringFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caseSensitive** | **Boolean** | Optional. If true, the match is case-sensitive. If false, the match is case-insensitive. Must be true when match_type is EXACT. Must be false when match_type is CONTAINS. | [optional] 
**matchType** | **String** | Required. The match type for the string filter. | [optional] 
**value** | **String** | Required. The string value to be matched against. | [optional] 



## Enum: MatchTypeEnum


* `MATCH_TYPE_UNSPECIFIED` (value: `"MATCH_TYPE_UNSPECIFIED"`)

* `EXACT` (value: `"EXACT"`)

* `CONTAINS` (value: `"CONTAINS"`)




