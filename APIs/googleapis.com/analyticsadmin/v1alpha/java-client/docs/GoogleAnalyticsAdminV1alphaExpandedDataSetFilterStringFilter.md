

# GoogleAnalyticsAdminV1alphaExpandedDataSetFilterStringFilter

A filter for a string-type dimension that matches a particular pattern.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caseSensitive** | **Boolean** | Optional. If true, the match is case-sensitive. If false, the match is case-insensitive. Must be true when match_type is EXACT. Must be false when match_type is CONTAINS. |  [optional] |
|**matchType** | [**MatchTypeEnum**](#MatchTypeEnum) | Required. The match type for the string filter. |  [optional] |
|**value** | **String** | Required. The string value to be matched against. |  [optional] |



## Enum: MatchTypeEnum

| Name | Value |
|---- | -----|
| MATCH_TYPE_UNSPECIFIED | &quot;MATCH_TYPE_UNSPECIFIED&quot; |
| EXACT | &quot;EXACT&quot; |
| CONTAINS | &quot;CONTAINS&quot; |



