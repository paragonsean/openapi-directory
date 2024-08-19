

# GoogleAnalyticsAdminV1alphaChannelGroupFilterStringFilter

Filter where the field value is a String. The match is case insensitive.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**matchType** | [**MatchTypeEnum**](#MatchTypeEnum) | Required. The match type for the string filter. |  [optional] |
|**value** | **String** | Required. The string value to be matched against. |  [optional] |



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



