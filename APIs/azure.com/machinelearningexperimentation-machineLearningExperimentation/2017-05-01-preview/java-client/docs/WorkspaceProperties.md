

# WorkspaceProperties

The properties of a machine learning team account workspace.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The immutable id of the team account which contains this workspace. |  [optional] [readonly] |
|**creationDate** | **OffsetDateTime** | The creation date of the machine learning workspace in ISO8601 format. |  [optional] [readonly] |
|**description** | **String** | The description of this workspace. |  [optional] |
|**friendlyName** | **String** | The friendly name for this workspace. This will be the workspace name in the arm id when the workspace object gets created |  |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current deployment state of team account workspace resource. The provisioningState is to indicate states for resource provisioning. |  [optional] [readonly] |
|**workspaceId** | **String** | The immutable id of this workspace. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



