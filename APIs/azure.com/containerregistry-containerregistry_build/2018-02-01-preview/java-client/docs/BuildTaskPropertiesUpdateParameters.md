

# BuildTaskPropertiesUpdateParameters

The properties for updating a build task.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alias** | **String** | The alternative updatable name for a build task. |  [optional] |
|**platform** | [**PlatformProperties**](PlatformProperties.md) |  |  [optional] |
|**sourceRepository** | [**SourceRepositoryUpdateParameters**](SourceRepositoryUpdateParameters.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of build task. |  [optional] |
|**timeout** | **Integer** | Build timeout in seconds. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |



