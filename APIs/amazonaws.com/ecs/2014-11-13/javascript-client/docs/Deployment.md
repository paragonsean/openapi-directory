# AmazonEc2ContainerService.Deployment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** |  | [optional] 
**status** | **String** |  | [optional] 
**taskDefinition** | **String** |  | [optional] 
**desiredCount** | **Number** |  | [optional] 
**pendingCount** | **Number** |  | [optional] 
**runningCount** | **Number** |  | [optional] 
**failedTasks** | **Number** |  | [optional] 
**createdAt** | **Date** |  | [optional] 
**updatedAt** | **Date** |  | [optional] 
**capacityProviderStrategy** | **Array** |  | [optional] 
**launchType** | [**LaunchType**](LaunchType.md) |  | [optional] 
**platformVersion** | **String** |  | [optional] 
**platformFamily** | **String** |  | [optional] 
**networkConfiguration** | [**StartTaskRequestNetworkConfiguration**](StartTaskRequestNetworkConfiguration.md) |  | [optional] 
**rolloutState** | [**DeploymentRolloutState**](DeploymentRolloutState.md) |  | [optional] 
**rolloutStateReason** | **String** |  | [optional] 
**serviceConnectConfiguration** | [**DeploymentServiceConnectConfiguration**](DeploymentServiceConnectConfiguration.md) |  | [optional] 
**serviceConnectResources** | **Array** |  | [optional] 


