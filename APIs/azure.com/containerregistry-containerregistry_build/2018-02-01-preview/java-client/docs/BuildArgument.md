

# BuildArgument

Properties of a build argument.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isSecret** | **Boolean** | Flag to indicate whether the argument represents a secret and want to be removed from build logs. |  [optional] |
|**name** | **String** | The name of the argument. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the argument. |  |
|**value** | **String** | The value of the argument. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DOCKER_BUILD_ARGUMENT | &quot;DockerBuildArgument&quot; |



