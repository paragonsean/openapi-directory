

# AccountProperties

The properties of a machine learning team account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The immutable id associated with this team account. |  [optional] [readonly] |
|**creationDate** | **OffsetDateTime** | The creation date of the machine learning team account in ISO8601 format. |  [optional] [readonly] |
|**description** | **String** | The description of this workspace. |  [optional] |
|**discoveryUri** | **String** | The uri for this machine learning team account. |  [optional] [readonly] |
|**friendlyName** | **String** | The friendly name for this workspace. This will be the workspace name in the arm id when the workspace object gets created |  [optional] |
|**keyVaultId** | **String** | The fully qualified arm id of the user key vault. |  |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current deployment state of team account resource. The provisioningState is to indicate states for resource provisioning. |  [optional] [readonly] |
|**seats** | **String** | The no of users/seats who can access this team account. This property defines the charge on the team account. |  [optional] |
|**storageAccount** | [**StorageAccountProperties**](StorageAccountProperties.md) |  |  |
|**vsoAccountId** | **String** | The fully qualified arm id of the vso account to be used for this team account. |  |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



