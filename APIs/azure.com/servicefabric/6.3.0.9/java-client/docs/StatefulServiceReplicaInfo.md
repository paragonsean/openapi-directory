

# StatefulServiceReplicaInfo

Represents a stateful service replica. This includes information about the identity, role, status, health, node name, uptime, and other details about the replica.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**replicaId** | **String** | Id of a stateful service replica. ReplicaId is used by Service Fabric to uniquely identify a replica of a partition. It is unique within a partition and does not change for the lifetime of the replica. If a replica gets dropped and another replica gets created on the same node for the same partition, it will get a different value for the id. Sometimes the id of a stateless service instance is also referred as a replica id. |  [optional] |
|**replicaRole** | **ReplicaRole** |  |  [optional] |



