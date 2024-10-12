

# PathQueryOptionsFilter

Dimension filter on path events.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filter** | **String** | Dimension the filter is applied to. |  [optional] |
|**match** | [**MatchEnum**](#MatchEnum) | Match logic of the filter. |  [optional] |
|**values** | **List&lt;String&gt;** | Values to filter on. |  [optional] |



## Enum: MatchEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| EXACT | &quot;EXACT&quot; |
| PARTIAL | &quot;PARTIAL&quot; |
| BEGINS_WITH | &quot;BEGINS_WITH&quot; |
| WILDCARD_EXPRESSION | &quot;WILDCARD_EXPRESSION&quot; |



