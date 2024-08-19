# ContainerInstanceManagementClient.ContainerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **[String]** | The commands to execute within the container instance in exec form. | [optional] 
**environmentVariables** | [**[EnvironmentVariable]**](EnvironmentVariable.md) | The environment variables to set in the container instance. | [optional] 
**image** | **String** | The name of the image used to create the container instance. | 
**instanceView** | [**ContainerPropertiesInstanceView**](ContainerPropertiesInstanceView.md) |  | [optional] 
**ports** | [**[ContainerPort]**](ContainerPort.md) | The exposed ports on the container instance. | [optional] 
**resources** | [**ResourceRequirements**](ResourceRequirements.md) |  | 
**volumeMounts** | [**[VolumeMount]**](VolumeMount.md) | The volume mounts available to the container instance. | [optional] 


