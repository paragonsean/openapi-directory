# AwsCodeBuild.UpdateProjectInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** |  | 
**description** | **String** |  | [optional] 
**source** | [**UpdateProjectInputSource**](UpdateProjectInputSource.md) |  | [optional] 
**secondarySources** | **Array** |  | [optional] 
**sourceVersion** | **String** |  | [optional] 
**secondarySourceVersions** | **Array** |  | [optional] 
**artifacts** | [**UpdateProjectInputArtifacts**](UpdateProjectInputArtifacts.md) |  | [optional] 
**secondaryArtifacts** | **Array** |  | [optional] 
**cache** | [**CreateProjectInputCache**](CreateProjectInputCache.md) |  | [optional] 
**environment** | [**UpdateProjectInputEnvironment**](UpdateProjectInputEnvironment.md) |  | [optional] 
**serviceRole** | **String** |  | [optional] 
**timeoutInMinutes** | **Number** |  | [optional] 
**queuedTimeoutInMinutes** | **Number** |  | [optional] 
**encryptionKey** | **String** |  | [optional] 
**tags** | **Array** |  | [optional] 
**vpcConfig** | [**CreateProjectInputVpcConfig**](CreateProjectInputVpcConfig.md) |  | [optional] 
**badgeEnabled** | **Boolean** |  | [optional] 
**logsConfig** | [**UpdateProjectInputLogsConfig**](UpdateProjectInputLogsConfig.md) |  | [optional] 
**fileSystemLocations** | **Array** |  | [optional] 
**buildBatchConfig** | [**ProjectBuildBatchConfig**](ProjectBuildBatchConfig.md) |  | [optional] 
**concurrentBuildLimit** | **Number** |  | [optional] 


