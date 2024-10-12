

# TaskStepProperties

Base properties for any task step.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseImageDependencies** | [**List&lt;BaseImageDependency&gt;**](BaseImageDependency.md) | List of base image dependencies for a step. |  [optional] [readonly] |
|**contextAccessToken** | **String** | The token (git PAT or SAS token of storage account blob) associated with the context for a step. |  [optional] |
|**contextPath** | **String** | The URL(absolute or relative) of the source context for the task step. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the step. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DOCKER | &quot;Docker&quot; |
| FILE_TASK | &quot;FileTask&quot; |
| ENCODED_TASK | &quot;EncodedTask&quot; |



