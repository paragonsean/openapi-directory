

# ShortRepresentation

Condensed representation of a node and its subtree. Only present for `SCALAR` PlanNode(s).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A string representation of the expression subtree rooted at this node. |  [optional] |
|**subqueries** | **Map&lt;String, Integer&gt;** | A mapping of (subquery variable name) -&gt; (subquery node id) for cases where the &#x60;description&#x60; string of this node references a &#x60;SCALAR&#x60; subquery contained in the expression subtree rooted at this node. The referenced &#x60;SCALAR&#x60; subquery may not necessarily be a direct child of this node. |  [optional] |



