# ServiceFabricClientApis.PartitionHealth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partitionId** | **String** | An internal ID used by Service Fabric to uniquely identify a partition. This is a randomly generated GUID when the service was created. The partition ID is unique and does not change for the lifetime of the service. If the same service was deleted and recreated the IDs of its partitions would be different. | [optional] 
**replicaHealthStates** | [**[ReplicaHealthState]**](ReplicaHealthState.md) | The list of replica health states associated with the partition. | [optional] 
**aggregatedHealthState** | [**HealthState**](HealthState.md) |  | [optional] 
**healthEvents** | [**[HealthEvent]**](HealthEvent.md) | The list of health events reported on the entity. | [optional] 
**healthStatistics** | [**HealthStatistics**](HealthStatistics.md) |  | [optional] 
**unhealthyEvaluations** | [**[HealthEvaluationWrapper]**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. | [optional] 


