# MlTeamAccountManagementClient.AccountProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The immutable id associated with this team account. | [optional] [readonly] 
**creationDate** | **Date** | The creation date of the machine learning team account in ISO8601 format. | [optional] [readonly] 
**description** | **String** | The description of this workspace. | [optional] 
**discoveryUri** | **String** | The uri for this machine learning team account. | [optional] [readonly] 
**friendlyName** | **String** | The friendly name for this workspace. This will be the workspace name in the arm id when the workspace object gets created | [optional] 
**keyVaultId** | **String** | The fully qualified arm id of the user key vault. | 
**provisioningState** | **String** | The current deployment state of team account resource. The provisioningState is to indicate states for resource provisioning. | [optional] [readonly] 
**seats** | **String** | The no of users/seats who can access this team account. This property defines the charge on the team account. | [optional] 
**storageAccount** | [**StorageAccountProperties**](StorageAccountProperties.md) |  | 
**vsoAccountId** | **String** | The fully qualified arm id of the vso account to be used for this team account. | 



## Enum: ProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




