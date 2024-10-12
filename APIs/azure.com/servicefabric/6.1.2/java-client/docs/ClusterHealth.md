

# ClusterHealth

Represents the health of the cluster. Contains the cluster aggregated health state, the cluster application and node health states as well as the health events and the unhealthy evaluations. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregatedHealthState** | **HealthState** |  |  [optional] |
|**healthEvents** | [**List&lt;HealthEvent&gt;**](HealthEvent.md) | The list of health events reported on the entity. |  [optional] |
|**healthStatistics** | [**HealthStatistics**](HealthStatistics.md) |  |  [optional] |
|**unhealthyEvaluations** | [**List&lt;HealthEvaluationWrapper&gt;**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. |  [optional] |
|**applicationHealthStates** | [**List&lt;ApplicationHealthState&gt;**](ApplicationHealthState.md) | Cluster application health states as found in the health store. |  [optional] |
|**nodeHealthStates** | [**List&lt;NodeHealthState&gt;**](NodeHealthState.md) | Cluster node health states as found in the health store. |  [optional] |



