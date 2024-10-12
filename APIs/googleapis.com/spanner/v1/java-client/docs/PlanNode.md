

# PlanNode

Node information for nodes appearing in a QueryPlan.plan_nodes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**childLinks** | [**List&lt;ChildLink&gt;**](ChildLink.md) | List of child node &#x60;index&#x60;es and their relationship to this parent. |  [optional] |
|**displayName** | **String** | The display name for the node. |  [optional] |
|**executionStats** | **Map&lt;String, Object&gt;** | The execution statistics associated with the node, contained in a group of key-value pairs. Only present if the plan was returned as a result of a profile query. For example, number of executions, number of rows/time per execution etc. |  [optional] |
|**index** | **Integer** | The &#x60;PlanNode&#x60;&#39;s index in node list. |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | Used to determine the type of node. May be needed for visualizing different kinds of nodes differently. For example, If the node is a SCALAR node, it will have a condensed representation which can be used to directly embed a description of the node in its parent. |  [optional] |
|**metadata** | **Map&lt;String, Object&gt;** | Attributes relevant to the node contained in a group of key-value pairs. For example, a Parameter Reference node could have the following information in its metadata: { \&quot;parameter_reference\&quot;: \&quot;param1\&quot;, \&quot;parameter_type\&quot;: \&quot;array\&quot; } |  [optional] |
|**shortRepresentation** | [**ShortRepresentation**](ShortRepresentation.md) |  |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| KIND_UNSPECIFIED | &quot;KIND_UNSPECIFIED&quot; |
| RELATIONAL | &quot;RELATIONAL&quot; |
| SCALAR | &quot;SCALAR&quot; |



