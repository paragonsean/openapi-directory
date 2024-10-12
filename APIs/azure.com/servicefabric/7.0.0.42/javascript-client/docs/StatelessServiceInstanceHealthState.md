# ServiceFabricClientApis.StatelessServiceInstanceHealthState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replicaId** | **String** | Id of a stateful service replica. ReplicaId is used by Service Fabric to uniquely identify a replica of a partition. It is unique within a partition and does not change for the lifetime of the replica. If a replica gets dropped and another replica gets created on the same node for the same partition, it will get a different value for the id. Sometimes the id of a stateless service instance is also referred as a replica id. | [optional] 
**partitionId** | **String** | An internal ID used by Service Fabric to uniquely identify a partition. This is a randomly generated GUID when the service was created. The partition ID is unique and does not change for the lifetime of the service. If the same service was deleted and recreated the IDs of its partitions would be different. | [optional] 
**serviceKind** | [**ServiceKind**](ServiceKind.md) |  | 
**aggregatedHealthState** | [**HealthState**](HealthState.md) |  | [optional] 


