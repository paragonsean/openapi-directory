

# PartitionHealthStateChunk

Represents the health state chunk of a partition, which contains the partition id, its aggregated health state and any replicas that respect the filters in the cluster health chunk query description. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**healthState** | **HealthState** |  |  [optional] |
|**partitionId** | **UUID** | An internal ID used by Service Fabric to uniquely identify a partition. This is a randomly generated GUID when the service was created. The partition id is unique and does not change for the lifetime of the service. If the same service was deleted and recreated the ids of its partitions would be different. |  [optional] |
|**replicaHealthStateChunks** | [**ReplicaHealthStateChunkList**](ReplicaHealthStateChunkList.md) |  |  [optional] |



