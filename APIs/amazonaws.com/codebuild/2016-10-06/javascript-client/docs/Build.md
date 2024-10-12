# AwsCodeBuild.Build

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** |  | [optional] 
**arn** | **String** |  | [optional] 
**buildNumber** | **Number** |  | [optional] 
**startTime** | **Date** |  | [optional] 
**endTime** | **Date** |  | [optional] 
**currentPhase** | **String** |  | [optional] 
**buildStatus** | [**StatusType**](StatusType.md) |  | [optional] 
**sourceVersion** | **String** |  | [optional] 
**resolvedSourceVersion** | **String** |  | [optional] 
**projectName** | **String** |  | [optional] 
**phases** | **Array** |  | [optional] 
**source** | [**BuildSource**](BuildSource.md) |  | [optional] 
**secondarySources** | **Array** |  | [optional] 
**secondarySourceVersions** | **Array** |  | [optional] 
**artifacts** | [**BuildArtifacts**](BuildArtifacts.md) |  | [optional] 
**secondaryArtifacts** | **Array** |  | [optional] 
**cache** | [**BuildCache**](BuildCache.md) |  | [optional] 
**environment** | [**BuildEnvironment**](BuildEnvironment.md) |  | [optional] 
**serviceRole** | **String** |  | [optional] 
**logs** | [**BuildLogs**](BuildLogs.md) |  | [optional] 
**timeoutInMinutes** | **Number** |  | [optional] 
**queuedTimeoutInMinutes** | **Number** |  | [optional] 
**buildComplete** | **Boolean** |  | [optional] 
**initiator** | **String** |  | [optional] 
**vpcConfig** | [**BuildVpcConfig**](BuildVpcConfig.md) |  | [optional] 
**networkInterface** | [**BuildNetworkInterface**](BuildNetworkInterface.md) |  | [optional] 
**encryptionKey** | **String** |  | [optional] 
**exportedEnvironmentVariables** | **Array** |  | [optional] 
**reportArns** | **Array** |  | [optional] 
**fileSystemLocations** | **Array** |  | [optional] 
**debugSession** | [**BuildDebugSession**](BuildDebugSession.md) |  | [optional] 
**buildBatchArn** | **String** |  | [optional] 


