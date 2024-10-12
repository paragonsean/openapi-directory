

# DeployedApplicationHealthStateChunk

Represents the health state chunk of a deployed application, which contains the node where the application is deployed, the aggregated health state and any deployed service packages that respect the chunk query description filters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deployedServicePackageHealthStateChunks** | [**DeployedServicePackageHealthStateChunkList**](DeployedServicePackageHealthStateChunkList.md) |  |  [optional] |
|**nodeName** | **String** | The name of node where the application is deployed. |  [optional] |
|**healthState** | **HealthState** |  |  [optional] |



