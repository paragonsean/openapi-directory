

# ChildLink

Metadata associated with a parent-child relationship appearing in a PlanNode.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**childIndex** | **Integer** | The node to which the link points. |  [optional] |
|**type** | **String** | The type of the link. For example, in Hash Joins this could be used to distinguish between the build child and the probe child, or in the case of the child being an output variable, to represent the tag associated with the output variable. |  [optional] |
|**variable** | **String** | Only present if the child node is SCALAR and corresponds to an output variable of the parent node. The field carries the name of the output variable. For example, a &#x60;TableScan&#x60; operator that reads rows from a table will have child links to the &#x60;SCALAR&#x60; nodes representing the output variables created for each column that is read by the operator. The corresponding &#x60;variable&#x60; fields will be set to the variable names assigned to the columns. |  [optional] |



