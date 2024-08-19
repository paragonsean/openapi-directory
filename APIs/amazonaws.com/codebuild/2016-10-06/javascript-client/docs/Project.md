# AwsCodeBuild.Project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** |  | [optional] 
**arn** | **String** |  | [optional] 
**description** | **String** |  | [optional] 
**source** | [**ProjectSource**](ProjectSource.md) |  | [optional] 
**secondarySources** | **Array** |  | [optional] 
**sourceVersion** | **String** |  | [optional] 
**secondarySourceVersions** | **Array** |  | [optional] 
**artifacts** | [**CreateProjectInputArtifacts**](CreateProjectInputArtifacts.md) |  | [optional] 
**secondaryArtifacts** | **Array** |  | [optional] 
**cache** | [**ProjectCache**](ProjectCache.md) |  | [optional] 
**environment** | [**ProjectEnvironment**](ProjectEnvironment.md) |  | [optional] 
**serviceRole** | **String** |  | [optional] 
**timeoutInMinutes** | **Number** |  | [optional] 
**queuedTimeoutInMinutes** | **Number** |  | [optional] 
**encryptionKey** | **String** |  | [optional] 
**tags** | **Array** |  | [optional] 
**created** | **Date** |  | [optional] 
**lastModified** | **Date** |  | [optional] 
**webhook** | [**CreateWebhookOutputWebhook**](CreateWebhookOutputWebhook.md) |  | [optional] 
**vpcConfig** | [**ProjectVpcConfig**](ProjectVpcConfig.md) |  | [optional] 
**badge** | [**ProjectBadge**](ProjectBadge.md) |  | [optional] 
**logsConfig** | [**ProjectLogsConfig**](ProjectLogsConfig.md) |  | [optional] 
**fileSystemLocations** | **Array** |  | [optional] 
**buildBatchConfig** | [**CreateProjectInputBuildBatchConfig**](CreateProjectInputBuildBatchConfig.md) |  | [optional] 
**concurrentBuildLimit** | **Number** |  | [optional] 
**projectVisibility** | [**ProjectVisibilityType**](ProjectVisibilityType.md) |  | [optional] 
**publicProjectAlias** | **String** |  | [optional] 
**resourceAccessRole** | **String** |  | [optional] 


