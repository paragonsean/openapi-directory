# CampaignManager360Api.PathFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eventFilters** | [**[EventFilter]**](EventFilter.md) | Event filters in path report. | [optional] 
**kind** | **String** | The kind of resource this is, in this case dfareporting#pathFilter. | [optional] 
**pathMatchPosition** | **String** | Determines how the &#39;value&#39; field is matched when filtering. If not specified, defaults to EXACT. If set to WILDCARD_EXPRESSION, &#39;*&#39; is allowed as a placeholder for variable length character sequences, and it can be escaped with a backslash. Note, only paid search dimensions (&#39;dfa:paidSearch*&#39;) allow a matchType other than EXACT. | [optional] 



## Enum: PathMatchPositionEnum


* `PATH_MATCH_POSITION_UNSPECIFIED` (value: `"PATH_MATCH_POSITION_UNSPECIFIED"`)

* `ANY` (value: `"ANY"`)

* `FIRST` (value: `"FIRST"`)

* `LAST` (value: `"LAST"`)




