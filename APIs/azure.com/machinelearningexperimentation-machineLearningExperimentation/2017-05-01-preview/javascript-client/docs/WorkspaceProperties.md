# MlTeamAccountManagementClient.WorkspaceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The immutable id of the team account which contains this workspace. | [optional] [readonly] 
**creationDate** | **Date** | The creation date of the machine learning workspace in ISO8601 format. | [optional] [readonly] 
**description** | **String** | The description of this workspace. | [optional] 
**friendlyName** | **String** | The friendly name for this workspace. This will be the workspace name in the arm id when the workspace object gets created | 
**provisioningState** | **String** | The current deployment state of team account workspace resource. The provisioningState is to indicate states for resource provisioning. | [optional] [readonly] 
**workspaceId** | **String** | The immutable id of this workspace. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




