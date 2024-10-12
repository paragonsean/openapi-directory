

# WorkspaceProperties

The properties of a machine learning workspace.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **String** | The creation time for this workspace resource. |  [optional] [readonly] |
|**keyVaultIdentifierId** | **String** | The key vault identifier used for encrypted workspaces. |  [optional] |
|**ownerEmail** | **String** | The email id of the owner for this workspace. |  |
|**studioEndpoint** | **String** | The regional endpoint for the machine learning studio service which hosts this workspace. |  [optional] [readonly] |
|**userStorageAccountId** | **String** | The fully qualified arm id of the storage account associated with this workspace. |  |
|**workspaceId** | **String** | The immutable id associated with this workspace. |  [optional] [readonly] |
|**workspaceState** | [**WorkspaceStateEnum**](#WorkspaceStateEnum) | The current state of workspace resource. |  [optional] [readonly] |
|**workspaceType** | [**WorkspaceTypeEnum**](#WorkspaceTypeEnum) | The type of this workspace. |  [optional] [readonly] |



## Enum: WorkspaceStateEnum

| Name | Value |
|---- | -----|
| DELETED | &quot;Deleted&quot; |
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |
| MIGRATED | &quot;Migrated&quot; |
| UPDATED | &quot;Updated&quot; |
| REGISTERED | &quot;Registered&quot; |
| UNREGISTERED | &quot;Unregistered&quot; |



## Enum: WorkspaceTypeEnum

| Name | Value |
|---- | -----|
| PRODUCTION | &quot;Production&quot; |
| FREE | &quot;Free&quot; |
| ANONYMOUS | &quot;Anonymous&quot; |
| PAID_STANDARD | &quot;PaidStandard&quot; |
| PAID_PREMIUM | &quot;PaidPremium&quot; |



