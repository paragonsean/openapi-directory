

# RegisterTaskDefinitionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**family** | [**String**](String.md) |  |  |
|**taskRoleArn** | [**String**](String.md) |  |  [optional] |
|**executionRoleArn** | [**String**](String.md) |  |  [optional] |
|**networkMode** | [**NetworkMode**](NetworkMode.md) |  |  [optional] |
|**containerDefinitions** | [**List**](List.md) |  |  |
|**volumes** | [**List**](List.md) |  |  [optional] |
|**placementConstraints** | [**List**](List.md) |  |  [optional] |
|**requiresCompatibilities** | [**List**](List.md) |  |  [optional] |
|**cpu** | [**String**](String.md) |  |  [optional] |
|**memory** | [**String**](String.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**pidMode** | [**PidMode**](PidMode.md) |  |  [optional] |
|**ipcMode** | [**IpcMode**](IpcMode.md) |  |  [optional] |
|**proxyConfiguration** | [**RegisterTaskDefinitionRequestProxyConfiguration**](RegisterTaskDefinitionRequestProxyConfiguration.md) |  |  [optional] |
|**inferenceAccelerators** | [**List**](List.md) |  |  [optional] |
|**ephemeralStorage** | [**RegisterTaskDefinitionRequestEphemeralStorage**](RegisterTaskDefinitionRequestEphemeralStorage.md) |  |  [optional] |
|**runtimePlatform** | [**RegisterTaskDefinitionRequestRuntimePlatform**](RegisterTaskDefinitionRequestRuntimePlatform.md) |  |  [optional] |



