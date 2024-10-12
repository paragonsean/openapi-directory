

# BuildTaskProperties

The properties of a build task.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alias** | **String** | The alternative updatable name for a build task. |  |
|**creationDate** | **OffsetDateTime** | The creation date of build task. |  [optional] [readonly] |
|**platform** | [**PlatformProperties**](PlatformProperties.md) |  |  |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state of the build task. |  [optional] [readonly] |
|**sourceRepository** | [**SourceRepositoryProperties**](SourceRepositoryProperties.md) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of build task. |  [optional] |
|**timeout** | **Integer** | Build timeout in seconds. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |



