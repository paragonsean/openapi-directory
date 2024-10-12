

# DeployedStatefulServiceReplicaInfo

Information about a stateful service replica deployed on a node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reconfigurationInformation** | [**ReconfigurationInformation**](ReconfigurationInformation.md) |  |  [optional] |
|**replicaId** | **String** | Id of a stateful service replica. ReplicaId is used by Service Fabric to uniquely identify a replica of a partition. It is unique within a partition and does not change for the lifetime of the replica. If a replica gets dropped and another replica gets created on the same node for the same partition, it will get a different value for the id. Sometimes the id of a stateless service instance is also referred as a replica id. |  [optional] |
|**replicaRole** | **ReplicaRole** |  |  [optional] |



