

# BuildBatch

Contains information about a batch build.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**String**](String.md) |  |  [optional] |
|**arn** | [**String**](String.md) |  |  [optional] |
|**startTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**endTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**currentPhase** | [**String**](String.md) |  |  [optional] |
|**buildBatchStatus** | [**StatusType**](StatusType.md) |  |  [optional] |
|**sourceVersion** | [**String**](String.md) |  |  [optional] |
|**resolvedSourceVersion** | [**String**](String.md) |  |  [optional] |
|**projectName** | [**String**](String.md) |  |  [optional] |
|**phases** | [**List**](List.md) |  |  [optional] |
|**source** | [**ProjectSource**](ProjectSource.md) |  |  [optional] |
|**secondarySources** | [**List**](List.md) |  |  [optional] |
|**secondarySourceVersions** | [**List**](List.md) |  |  [optional] |
|**artifacts** | [**BuildBatchArtifacts**](BuildBatchArtifacts.md) |  |  [optional] |
|**secondaryArtifacts** | [**List**](List.md) |  |  [optional] |
|**cache** | [**ProjectCache**](ProjectCache.md) |  |  [optional] |
|**environment** | [**ProjectEnvironment**](ProjectEnvironment.md) |  |  [optional] |
|**serviceRole** | [**String**](String.md) |  |  [optional] |
|**logConfig** | [**LogsConfig**](LogsConfig.md) |  |  [optional] |
|**buildTimeoutInMinutes** | [**Integer**](Integer.md) |  |  [optional] |
|**queuedTimeoutInMinutes** | [**Integer**](Integer.md) |  |  [optional] |
|**complete** | [**Boolean**](Boolean.md) |  |  [optional] |
|**initiator** | [**String**](String.md) |  |  [optional] |
|**vpcConfig** | [**VpcConfig**](VpcConfig.md) |  |  [optional] |
|**encryptionKey** | [**String**](String.md) |  |  [optional] |
|**buildBatchNumber** | [**Integer**](Integer.md) |  |  [optional] |
|**fileSystemLocations** | [**List**](List.md) |  |  [optional] |
|**buildBatchConfig** | [**ProjectBuildBatchConfig**](ProjectBuildBatchConfig.md) |  |  [optional] |
|**buildGroups** | [**List**](List.md) |  |  [optional] |
|**debugSessionEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |



