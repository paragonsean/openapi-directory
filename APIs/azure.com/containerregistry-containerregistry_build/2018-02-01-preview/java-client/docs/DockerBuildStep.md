

# DockerBuildStep

The Docker build step.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseImageDependencies** | [**List&lt;BaseImageDependency&gt;**](BaseImageDependency.md) | List of base image dependencies for a step. |  [optional] [readonly] |
|**baseImageTrigger** | [**BaseImageTriggerEnum**](#BaseImageTriggerEnum) | The type of the auto trigger for base image dependency updates. |  [optional] |
|**branch** | **String** | The repository branch name. |  [optional] |
|**buildArguments** | [**List&lt;BuildArgument&gt;**](BuildArgument.md) | The custom arguments for building this build step. |  [optional] |
|**contextPath** | **String** | The relative context path for a docker build in the source. |  [optional] |
|**dockerFilePath** | **String** | The Docker file path relative to the source control root. |  [optional] |
|**imageNames** | **List&lt;String&gt;** | The fully qualified image names including the repository and tag. |  [optional] |
|**isPushEnabled** | **Boolean** | The value of this property indicates whether the image built should be pushed to the registry or not. |  [optional] |
|**noCache** | **Boolean** | The value of this property indicates whether the image cache is enabled or not. |  [optional] |



## Enum: BaseImageTriggerEnum

| Name | Value |
|---- | -----|
| ALL | &quot;All&quot; |
| RUNTIME | &quot;Runtime&quot; |
| NONE | &quot;None&quot; |



