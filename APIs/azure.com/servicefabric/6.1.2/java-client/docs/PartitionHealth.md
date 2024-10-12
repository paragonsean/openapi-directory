

# PartitionHealth

Information about the health of a Service Fabric partition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregatedHealthState** | **HealthState** |  |  [optional] |
|**healthEvents** | [**List&lt;HealthEvent&gt;**](HealthEvent.md) | The list of health events reported on the entity. |  [optional] |
|**healthStatistics** | [**HealthStatistics**](HealthStatistics.md) |  |  [optional] |
|**unhealthyEvaluations** | [**List&lt;HealthEvaluationWrapper&gt;**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. |  [optional] |
|**partitionId** | **UUID** | An internal ID used by Service Fabric to uniquely identify a partition. This is a randomly generated GUID when the service was created. The partition id is unique and does not change for the lifetime of the service. If the same service was deleted and recreated the ids of its partitions would be different. |  [optional] |
|**replicaHealthStates** | [**List&lt;ReplicaHealthState&gt;**](ReplicaHealthState.md) | The list of replica health states associated with the partition. |  [optional] |



