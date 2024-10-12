

# QueryPlan

Contains an ordered list of nodes appearing in the query plan.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**planNodes** | [**List&lt;PlanNode&gt;**](PlanNode.md) | The nodes in the query plan. Plan nodes are returned in pre-order starting with the plan root. Each PlanNode&#39;s &#x60;id&#x60; corresponds to its index in &#x60;plan_nodes&#x60;. |  [optional] |
|**queryAdvice** | [**QueryAdvisorResult**](QueryAdvisorResult.md) |  |  [optional] |



