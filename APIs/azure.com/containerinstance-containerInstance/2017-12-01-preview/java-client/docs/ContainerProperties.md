

# ContainerProperties

The container instance properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**command** | **List&lt;String&gt;** | The commands to execute within the container instance in exec form. |  [optional] |
|**environmentVariables** | [**List&lt;EnvironmentVariable&gt;**](EnvironmentVariable.md) | The environment variables to set in the container instance. |  [optional] |
|**image** | **String** | The name of the image used to create the container instance. |  |
|**instanceView** | [**ContainerPropertiesInstanceView**](ContainerPropertiesInstanceView.md) |  |  [optional] |
|**ports** | [**List&lt;ContainerPort&gt;**](ContainerPort.md) | The exposed ports on the container instance. |  [optional] |
|**resources** | [**ResourceRequirements**](ResourceRequirements.md) |  |  |
|**volumeMounts** | [**List&lt;VolumeMount&gt;**](VolumeMount.md) | The volume mounts available to the container instance. |  [optional] |



