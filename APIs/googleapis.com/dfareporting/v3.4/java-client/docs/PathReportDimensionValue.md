

# PathReportDimensionValue

Represents a PathReportDimensionValue resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimensionName** | **String** | The name of the dimension. |  [optional] |
|**ids** | **List&lt;String&gt;** | The possible ID&#39;s associated with the value if available. |  [optional] |
|**kind** | **String** | The kind of resource this is, in this case dfareporting#pathReportDimensionValue. |  [optional] |
|**matchType** | [**MatchTypeEnum**](#MatchTypeEnum) | Determines how the &#39;value&#39; field is matched when filtering. If not specified, defaults to EXACT. If set to WILDCARD_EXPRESSION, &#39;*&#39; is allowed as a placeholder for variable length character sequences, and it can be escaped with a backslash. Note, only paid search dimensions (&#39;dfa:paidSearch*&#39;) allow a matchType other than EXACT. |  [optional] |
|**values** | **List&lt;String&gt;** | The possible values of the dimension. |  [optional] |



## Enum: MatchTypeEnum

| Name | Value |
|---- | -----|
| EXACT | &quot;EXACT&quot; |
| BEGINS_WITH | &quot;BEGINS_WITH&quot; |
| CONTAINS | &quot;CONTAINS&quot; |
| WILDCARD_EXPRESSION | &quot;WILDCARD_EXPRESSION&quot; |



