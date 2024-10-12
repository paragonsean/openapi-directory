# AzureMachineLearningWorkspaces.WorkspaceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationInsights** | **String** | ARM id of the application insights associated with this workspace. This cannot be changed once the workspace has been created | [optional] 
**batchaiWorkspace** | **String** | ARM id of the Batch AI workspace associated with this workspace. This cannot be changed once the workspace has been created | [optional] 
**containerRegistry** | **String** | ARM id of the container registry associated with this workspace. This cannot be changed once the workspace has been created | [optional] 
**creationTime** | **Date** | The creation time of the machine learning workspace in ISO8601 format. | [optional] [readonly] 
**description** | **String** | The description of this workspace. | [optional] 
**discoveryUrl** | **String** | Url for the discovery service to identify regional endpoints for machine learning experimentation services | [optional] 
**friendlyName** | **String** | The friendly name for this workspace. This name in mutable | [optional] 
**keyVault** | **String** | ARM id of the key vault associated with this workspace. This cannot be changed once the workspace has been created | [optional] 
**provisioningState** | **String** | The current deployment state of workspace resource. The provisioningState is to indicate states for resource provisioning. | [optional] [readonly] 
**storageAccount** | **String** | ARM id of the storage account associated with this workspace. This cannot be changed once the workspace has been created | [optional] 
**workspaceId** | **String** | The immutable id associated with this workspace. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Unknown` (value: `"Unknown"`)

* `Updating` (value: `"Updating"`)

* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)




