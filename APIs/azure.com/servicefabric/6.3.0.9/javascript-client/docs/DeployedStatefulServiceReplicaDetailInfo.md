# ServiceFabricClientApis.DeployedStatefulServiceReplicaDetailInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentReplicatorOperation** | [**ReplicatorOperationName**](ReplicatorOperationName.md) |  | [optional] 
**deployedServiceReplicaQueryResult** | [**DeployedStatefulServiceReplicaInfo**](DeployedStatefulServiceReplicaInfo.md) |  | [optional] 
**readStatus** | [**PartitionAccessStatus**](PartitionAccessStatus.md) |  | [optional] 
**replicaId** | **String** | Id of a stateful service replica. ReplicaId is used by Service Fabric to uniquely identify a replica of a partition. It is unique within a partition and does not change for the lifetime of the replica. If a replica gets dropped and another replica gets created on the same node for the same partition, it will get a different value for the id. Sometimes the id of a stateless service instance is also referred as a replica id. | [optional] 
**replicaStatus** | [**KeyValueStoreReplicaStatus**](KeyValueStoreReplicaStatus.md) |  | [optional] 
**replicatorStatus** | [**ReplicatorStatus**](ReplicatorStatus.md) |  | [optional] 
**writeStatus** | [**PartitionAccessStatus**](PartitionAccessStatus.md) |  | [optional] 


