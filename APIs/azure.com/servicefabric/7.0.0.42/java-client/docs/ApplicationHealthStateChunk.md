

# ApplicationHealthStateChunk

Represents the health state chunk of a application. The application health state chunk contains the application name, its aggregated health state and any children services and deployed applications that respect the filters in cluster health chunk query description.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationName** | **String** | The name of the application, including the &#39;fabric:&#39; URI scheme. |  [optional] |
|**applicationTypeName** | **String** | The application type name as defined in the application manifest. |  [optional] |
|**deployedApplicationHealthStateChunks** | [**DeployedApplicationHealthStateChunkList**](DeployedApplicationHealthStateChunkList.md) |  |  [optional] |
|**serviceHealthStateChunks** | [**ServiceHealthStateChunkList**](ServiceHealthStateChunkList.md) |  |  [optional] |
|**healthState** | **HealthState** |  |  [optional] |



