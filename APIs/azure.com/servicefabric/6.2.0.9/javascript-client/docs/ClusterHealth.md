# ServiceFabricClientApis.ClusterHealth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregatedHealthState** | [**HealthState**](HealthState.md) |  | [optional] 
**healthEvents** | [**[HealthEvent]**](HealthEvent.md) | The list of health events reported on the entity. | [optional] 
**healthStatistics** | [**HealthStatistics**](HealthStatistics.md) |  | [optional] 
**unhealthyEvaluations** | [**[HealthEvaluationWrapper]**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. | [optional] 
**applicationHealthStates** | [**[ApplicationHealthState]**](ApplicationHealthState.md) | Cluster application health states as found in the health store. | [optional] 
**nodeHealthStates** | [**[NodeHealthState]**](NodeHealthState.md) | Cluster node health states as found in the health store. | [optional] 


