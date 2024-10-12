

# NodesHealthEvaluation

Represents health evaluation for nodes, containing health evaluations for each unhealthy node that impacted current aggregated health state. Can be returned when evaluating cluster health and the aggregated health state is either Error or Warning.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxPercentUnhealthyNodes** | **Integer** | Maximum allowed percentage of unhealthy nodes from the ClusterHealthPolicy. |  [optional] |
|**totalCount** | **Long** | Total number of nodes found in the health store. |  [optional] |
|**unhealthyEvaluations** | [**List&lt;HealthEvaluationWrapper&gt;**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. |  [optional] |



