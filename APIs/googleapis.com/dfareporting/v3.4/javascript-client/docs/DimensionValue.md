# CampaignManager360Api.DimensionValue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimensionName** | **String** | The name of the dimension. | [optional] 
**etag** | **String** | The eTag of this response for caching purposes. | [optional] 
**id** | **String** | The ID associated with the value if available. | [optional] 
**kind** | **String** | The kind of resource this is, in this case dfareporting#dimensionValue. | [optional] 
**matchType** | **String** | Determines how the &#39;value&#39; field is matched when filtering. If not specified, defaults to EXACT. If set to WILDCARD_EXPRESSION, &#39;*&#39; is allowed as a placeholder for variable length character sequences, and it can be escaped with a backslash. Note, only paid search dimensions (&#39;dfa:paidSearch*&#39;) allow a matchType other than EXACT. | [optional] 
**value** | **String** | The value of the dimension. | [optional] 



## Enum: MatchTypeEnum


* `EXACT` (value: `"EXACT"`)

* `BEGINS_WITH` (value: `"BEGINS_WITH"`)

* `CONTAINS` (value: `"CONTAINS"`)

* `WILDCARD_EXPRESSION` (value: `"WILDCARD_EXPRESSION"`)




