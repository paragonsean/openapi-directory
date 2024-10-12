

# ReplicasHealthEvaluation

Represents health evaluation for replicas, containing health evaluations for each unhealthy replica that impacted current aggregated health state. Can be returned when evaluating partition health and the aggregated health state is either Error or Warning.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxPercentUnhealthyReplicasPerPartition** | **Integer** | Maximum allowed percentage of unhealthy replicas per partition from the ApplicationHealthPolicy. |  [optional] |
|**totalCount** | **Long** | Total number of replicas in the partition from the health store. |  [optional] |
|**unhealthyEvaluations** | [**List&lt;HealthEvaluationWrapper&gt;**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. |  [optional] |



