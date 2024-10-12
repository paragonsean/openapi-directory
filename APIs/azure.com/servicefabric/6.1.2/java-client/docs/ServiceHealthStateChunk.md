

# ServiceHealthStateChunk

Represents the health state chunk of a service, which contains the service name, its aggregated health state and any partitions that respect the filters in the cluster health chunk query description. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**healthState** | **HealthState** |  |  [optional] |
|**partitionHealthStateChunks** | [**PartitionHealthStateChunkList**](PartitionHealthStateChunkList.md) |  |  [optional] |
|**serviceName** | **String** | The full name of the service with &#39;fabric:&#39; URI scheme. |  [optional] |



