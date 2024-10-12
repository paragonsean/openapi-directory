

# GoogleAnalyticsAdminV1alphaSubpropertyEventFilterConditionStringFilter

A filter for a string-type dimension that matches a particular pattern.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caseSensitive** | **Boolean** | Optional. If true, the string value is case sensitive. If false, the match is case-insensitive. |  [optional] |
|**matchType** | [**MatchTypeEnum**](#MatchTypeEnum) | Required. The match type for the string filter. |  [optional] |
|**value** | **String** | Required. The string value used for the matching. |  [optional] |



## Enum: MatchTypeEnum

| Name | Value |
|---- | -----|
| MATCH_TYPE_UNSPECIFIED | &quot;MATCH_TYPE_UNSPECIFIED&quot; |
| EXACT | &quot;EXACT&quot; |
| BEGINS_WITH | &quot;BEGINS_WITH&quot; |
| ENDS_WITH | &quot;ENDS_WITH&quot; |
| CONTAINS | &quot;CONTAINS&quot; |
| FULL_REGEXP | &quot;FULL_REGEXP&quot; |
| PARTIAL_REGEXP | &quot;PARTIAL_REGEXP&quot; |



