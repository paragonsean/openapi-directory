

# GoogleAnalyticsAdminV1betaAccessStringFilter

The filter for strings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caseSensitive** | **Boolean** | If true, the string value is case sensitive. |  [optional] |
|**matchType** | [**MatchTypeEnum**](#MatchTypeEnum) | The match type for this filter. |  [optional] |
|**value** | **String** | The string value used for the matching. |  [optional] |



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



