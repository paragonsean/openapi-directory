# MachineLearningWorkspacesManagementClient.WorkspaceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationTime** | **String** | The creation time for this workspace resource. | [optional] [readonly] 
**keyVaultIdentifierId** | **String** | The key vault identifier used for encrypted workspaces. | [optional] 
**ownerEmail** | **String** | The email id of the owner for this workspace. | 
**studioEndpoint** | **String** | The regional endpoint for the machine learning studio service which hosts this workspace. | [optional] [readonly] 
**userStorageAccountId** | **String** | The fully qualified arm id of the storage account associated with this workspace. | 
**workspaceId** | **String** | The immutable id associated with this workspace. | [optional] [readonly] 
**workspaceState** | **String** | The current state of workspace resource. | [optional] [readonly] 
**workspaceType** | **String** | The type of this workspace. | [optional] [readonly] 



## Enum: WorkspaceStateEnum


* `Deleted` (value: `"Deleted"`)

* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)

* `Migrated` (value: `"Migrated"`)

* `Updated` (value: `"Updated"`)

* `Registered` (value: `"Registered"`)

* `Unregistered` (value: `"Unregistered"`)





## Enum: WorkspaceTypeEnum


* `Production` (value: `"Production"`)

* `Free` (value: `"Free"`)

* `Anonymous` (value: `"Anonymous"`)

* `PaidStandard` (value: `"PaidStandard"`)

* `PaidPremium` (value: `"PaidPremium"`)




