# ServiceFabricClientApis.ServiceHealth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The full name of the service with &#39;fabric:&#39; URI scheme. | [optional] 
**partitionHealthStates** | [**[PartitionHealthState]**](PartitionHealthState.md) | The list of partition health states associated with the service. | [optional] 
**aggregatedHealthState** | [**HealthState**](HealthState.md) |  | [optional] 
**healthEvents** | [**[HealthEvent]**](HealthEvent.md) | The list of health events reported on the entity. | [optional] 
**healthStatistics** | [**HealthStatistics**](HealthStatistics.md) |  | [optional] 
**unhealthyEvaluations** | [**[HealthEvaluationWrapper]**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. | [optional] 


