

# WorkspacePropertiesUpdateParameters

The parameters for updating the properties of a machine learning workspace.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keyVaultIdentifierId** | **String** | The key vault identifier used for encrypted workspaces. |  [optional] |
|**workspaceState** | [**WorkspaceStateEnum**](#WorkspaceStateEnum) | The current state of workspace resource. |  [optional] |



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



