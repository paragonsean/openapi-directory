# CloudSpannerApi.PlanNode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**childLinks** | [**[ChildLink]**](ChildLink.md) | List of child node &#x60;index&#x60;es and their relationship to this parent. | [optional] 
**displayName** | **String** | The display name for the node. | [optional] 
**executionStats** | **{String: Object}** | The execution statistics associated with the node, contained in a group of key-value pairs. Only present if the plan was returned as a result of a profile query. For example, number of executions, number of rows/time per execution etc. | [optional] 
**index** | **Number** | The &#x60;PlanNode&#x60;&#39;s index in node list. | [optional] 
**kind** | **String** | Used to determine the type of node. May be needed for visualizing different kinds of nodes differently. For example, If the node is a SCALAR node, it will have a condensed representation which can be used to directly embed a description of the node in its parent. | [optional] 
**metadata** | **{String: Object}** | Attributes relevant to the node contained in a group of key-value pairs. For example, a Parameter Reference node could have the following information in its metadata: { \&quot;parameter_reference\&quot;: \&quot;param1\&quot;, \&quot;parameter_type\&quot;: \&quot;array\&quot; } | [optional] 
**shortRepresentation** | [**ShortRepresentation**](ShortRepresentation.md) |  | [optional] 



## Enum: KindEnum


* `KIND_UNSPECIFIED` (value: `"KIND_UNSPECIFIED"`)

* `RELATIONAL` (value: `"RELATIONAL"`)

* `SCALAR` (value: `"SCALAR"`)




