

# PathFilter

Represents a DfaReporting path filter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventFilters** | [**List&lt;EventFilter&gt;**](EventFilter.md) | Event filters in path report. |  [optional] |
|**kind** | **String** | The kind of resource this is, in this case dfareporting#pathFilter. |  [optional] |
|**pathMatchPosition** | [**PathMatchPositionEnum**](#PathMatchPositionEnum) | Determines how the &#39;value&#39; field is matched when filtering. If not specified, defaults to EXACT. If set to WILDCARD_EXPRESSION, &#39;*&#39; is allowed as a placeholder for variable length character sequences, and it can be escaped with a backslash. Note, only paid search dimensions (&#39;dfa:paidSearch*&#39;) allow a matchType other than EXACT. |  [optional] |



## Enum: PathMatchPositionEnum

| Name | Value |
|---- | -----|
| PATH_MATCH_POSITION_UNSPECIFIED | &quot;PATH_MATCH_POSITION_UNSPECIFIED&quot; |
| ANY | &quot;ANY&quot; |
| FIRST | &quot;FIRST&quot; |
| LAST | &quot;LAST&quot; |



