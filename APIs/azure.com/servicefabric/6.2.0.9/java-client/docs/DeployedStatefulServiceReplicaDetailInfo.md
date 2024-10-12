

# DeployedStatefulServiceReplicaDetailInfo

Information about a stateful replica running in a code package. Please note DeployedServiceReplicaQueryResult will contain duplicate data like ServiceKind, ServiceName, PartitionId and replicaId.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentReplicatorOperation** | **ReplicatorOperationName** |  |  [optional] |
|**deployedServiceReplicaQueryResult** | [**DeployedStatefulServiceReplicaInfo**](DeployedStatefulServiceReplicaInfo.md) |  |  [optional] |
|**readStatus** | **PartitionAccessStatus** |  |  [optional] |
|**replicaId** | **String** | Id of a stateful service replica. ReplicaId is used by Service Fabric to uniquely identify a replica of a partition. It is unique within a partition and does not change for the lifetime of the replica. If a replica gets dropped and another replica gets created on the same node for the same partition, it will get a different value for the id. Sometimes the id of a stateless service instance is also referred as a replica id. |  [optional] |
|**replicaStatus** | [**KeyValueStoreReplicaStatus**](KeyValueStoreReplicaStatus.md) |  |  [optional] |
|**replicatorStatus** | [**ReplicatorStatus**](ReplicatorStatus.md) |  |  [optional] |
|**writeStatus** | **PartitionAccessStatus** |  |  [optional] |



