# SeaBreezeManagementClient.ContainerCodePackageProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commands** | **[String]** | Command array to execute within the container in exec form. | [optional] 
**diagnostics** | [**DiagnosticsRef**](DiagnosticsRef.md) |  | [optional] 
**endpoints** | [**[EndpointProperties]**](EndpointProperties.md) | The endpoints exposed by this container. | [optional] 
**entrypoint** | **String** | Override for the default entry point in the container. | [optional] 
**environmentVariables** | [**[EnvironmentVariable]**](EnvironmentVariable.md) | The environment variables to set in this container | [optional] 
**image** | **String** | The Container image to use. | 
**imageRegistryCredential** | [**ImageRegistryCredential**](ImageRegistryCredential.md) |  | [optional] 
**instanceView** | [**ContainerInstanceView**](ContainerInstanceView.md) |  | [optional] 
**labels** | [**[ContainerLabel]**](ContainerLabel.md) | The labels to set in this container. | [optional] 
**name** | **String** | The name of the code package. | 
**resources** | [**ResourceRequirements**](ResourceRequirements.md) |  | 
**settings** | [**[Setting]**](Setting.md) | The settings to set in this container. The setting file path can be fetched from environment variable \&quot;Fabric_SettingPath\&quot;. The path for Windows container is \&quot;C:\\\\secrets\&quot;. The path for Linux container is \&quot;/var/secrets\&quot;. | [optional] 
**volumeRefs** | [**[ContainerVolume]**](ContainerVolume.md) | The volumes to be attached to the container. | [optional] 


