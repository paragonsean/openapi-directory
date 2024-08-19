# AmazonEc2ContainerService.RegisterTaskDefinitionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family** | **String** |  | 
**taskRoleArn** | **String** |  | [optional] 
**executionRoleArn** | **String** |  | [optional] 
**networkMode** | [**NetworkMode**](NetworkMode.md) |  | [optional] 
**containerDefinitions** | **Array** |  | 
**volumes** | **Array** |  | [optional] 
**placementConstraints** | **Array** |  | [optional] 
**requiresCompatibilities** | **Array** |  | [optional] 
**cpu** | **String** |  | [optional] 
**memory** | **String** |  | [optional] 
**tags** | **Array** |  | [optional] 
**pidMode** | [**PidMode**](PidMode.md) |  | [optional] 
**ipcMode** | [**IpcMode**](IpcMode.md) |  | [optional] 
**proxyConfiguration** | [**RegisterTaskDefinitionRequestProxyConfiguration**](RegisterTaskDefinitionRequestProxyConfiguration.md) |  | [optional] 
**inferenceAccelerators** | **Array** |  | [optional] 
**ephemeralStorage** | [**RegisterTaskDefinitionRequestEphemeralStorage**](RegisterTaskDefinitionRequestEphemeralStorage.md) |  | [optional] 
**runtimePlatform** | [**RegisterTaskDefinitionRequestRuntimePlatform**](RegisterTaskDefinitionRequestRuntimePlatform.md) |  | [optional] 


