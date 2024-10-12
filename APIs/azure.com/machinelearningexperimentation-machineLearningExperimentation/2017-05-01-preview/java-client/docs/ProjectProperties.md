

# ProjectProperties

The properties of a machine learning project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The immutable id of the team account which contains this project. |  [optional] [readonly] |
|**creationDate** | **OffsetDateTime** | The creation date of the project in ISO8601 format. |  [optional] [readonly] |
|**description** | **String** | The description of this project. |  [optional] |
|**friendlyName** | **String** | The friendly name for this project. |  |
|**gitrepo** | **String** | The reference to git repo for this project. |  [optional] |
|**projectId** | **String** | The immutable id of this project. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current deployment state of project resource. The provisioningState is to indicate states for resource provisioning. |  [optional] [readonly] |
|**workspaceId** | **String** | The immutable id of the workspace which contains this project. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



