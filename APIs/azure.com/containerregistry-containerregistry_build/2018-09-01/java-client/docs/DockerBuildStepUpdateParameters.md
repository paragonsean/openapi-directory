

# DockerBuildStepUpdateParameters

The properties for updating a docker build step.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arguments** | [**List&lt;Argument&gt;**](Argument.md) | The collection of override arguments to be used when executing this build step. |  [optional] |
|**dockerFilePath** | **String** | The Docker file path relative to the source context. |  [optional] |
|**imageNames** | **List&lt;String&gt;** | The fully qualified image names including the repository and tag. |  [optional] |
|**isPushEnabled** | **Boolean** | The value of this property indicates whether the image built should be pushed to the registry or not. |  [optional] |
|**noCache** | **Boolean** | The value of this property indicates whether the image cache is enabled or not. |  [optional] |
|**target** | **String** | The name of the target build stage for the docker build. |  [optional] |



