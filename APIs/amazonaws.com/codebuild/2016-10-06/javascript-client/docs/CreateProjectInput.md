# AwsCodeBuild.CreateProjectInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** |  | 
**description** | **String** |  | [optional] 
**source** | [**CreateProjectInputSource**](CreateProjectInputSource.md) |  | 
**secondarySources** | **Array** |  | [optional] 
**sourceVersion** | **String** |  | [optional] 
**secondarySourceVersions** | **Array** |  | [optional] 
**artifacts** | [**CreateProjectInputArtifacts**](CreateProjectInputArtifacts.md) |  | 
**secondaryArtifacts** | **Array** |  | [optional] 
**cache** | [**CreateProjectInputCache**](CreateProjectInputCache.md) |  | [optional] 
**environment** | [**CreateProjectInputEnvironment**](CreateProjectInputEnvironment.md) |  | 
**serviceRole** | **String** |  | 
**timeoutInMinutes** | **Number** |  | [optional] 
**queuedTimeoutInMinutes** | **Number** |  | [optional] 
**encryptionKey** | **String** |  | [optional] 
**tags** | **Array** |  | [optional] 
**vpcConfig** | [**CreateProjectInputVpcConfig**](CreateProjectInputVpcConfig.md) |  | [optional] 
**badgeEnabled** | **Boolean** |  | [optional] 
**logsConfig** | [**CreateProjectInputLogsConfig**](CreateProjectInputLogsConfig.md) |  | [optional] 
**fileSystemLocations** | **Array** |  | [optional] 
**buildBatchConfig** | [**CreateProjectInputBuildBatchConfig**](CreateProjectInputBuildBatchConfig.md) |  | [optional] 
**concurrentBuildLimit** | **Number** |  | [optional] 


