# AwsCodeBuild.StartBuildBatchOutputBuildBatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** |  | [optional] 
**arn** | **String** |  | [optional] 
**startTime** | **Date** |  | [optional] 
**endTime** | **Date** |  | [optional] 
**currentPhase** | **String** |  | [optional] 
**buildBatchStatus** | [**StatusType**](StatusType.md) |  | [optional] 
**sourceVersion** | **String** |  | [optional] 
**resolvedSourceVersion** | **String** |  | [optional] 
**projectName** | **String** |  | [optional] 
**phases** | **Array** |  | [optional] 
**source** | [**ProjectSource**](ProjectSource.md) |  | [optional] 
**secondarySources** | **Array** |  | [optional] 
**secondarySourceVersions** | **Array** |  | [optional] 
**artifacts** | [**BuildBatchArtifacts**](BuildBatchArtifacts.md) |  | [optional] 
**secondaryArtifacts** | **Array** |  | [optional] 
**cache** | [**ProjectCache**](ProjectCache.md) |  | [optional] 
**environment** | [**ProjectEnvironment**](ProjectEnvironment.md) |  | [optional] 
**serviceRole** | **String** |  | [optional] 
**logConfig** | [**LogsConfig**](LogsConfig.md) |  | [optional] 
**buildTimeoutInMinutes** | **Number** |  | [optional] 
**queuedTimeoutInMinutes** | **Number** |  | [optional] 
**complete** | **Boolean** |  | [optional] 
**initiator** | **String** |  | [optional] 
**vpcConfig** | [**VpcConfig**](VpcConfig.md) |  | [optional] 
**encryptionKey** | **String** |  | [optional] 
**buildBatchNumber** | **Number** |  | [optional] 
**fileSystemLocations** | **Array** |  | [optional] 
**buildBatchConfig** | [**ProjectBuildBatchConfig**](ProjectBuildBatchConfig.md) |  | [optional] 
**buildGroups** | **Array** |  | [optional] 
**debugSessionEnabled** | **Boolean** |  | [optional] 


