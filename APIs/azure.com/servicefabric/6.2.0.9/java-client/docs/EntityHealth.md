

# EntityHealth

Health information common to all entities in the cluster. It contains the aggregated health state, health events and unhealthy evaluation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregatedHealthState** | **HealthState** |  |  [optional] |
|**healthEvents** | [**List&lt;HealthEvent&gt;**](HealthEvent.md) | The list of health events reported on the entity. |  [optional] |
|**healthStatistics** | [**HealthStatistics**](HealthStatistics.md) |  |  [optional] |
|**unhealthyEvaluations** | [**List&lt;HealthEvaluationWrapper&gt;**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. |  [optional] |



