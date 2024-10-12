

# ReplicaHealthStateChunk

Represents the health state chunk of a stateful service replica or a stateless service instance. The replica health state contains the replica ID and its aggregated health state. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**healthState** | **HealthState** |  |  [optional] |
|**replicaOrInstanceId** | **String** | Id of a stateful service replica or a stateless service instance. This id is used in the queries that apply to both stateful and stateless services. It is used by Service Fabric to uniquely identify a replica of a partition of a stateful service or an instance of a stateless service partition. It is unique within a partition and does not change for the lifetime of the replica or the instance. If a stateful replica gets dropped and another replica gets created on the same node for the same partition, it will get a different value for the id. If a staless instance is failed over on the same or different node it will get a different value for the id. |  [optional] |



