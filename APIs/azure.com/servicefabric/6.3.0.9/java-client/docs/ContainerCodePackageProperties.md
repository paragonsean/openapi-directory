

# ContainerCodePackageProperties

Describes a container and its runtime properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commands** | **List&lt;String&gt;** | Command array to execute within the container in exec form. |  [optional] |
|**diagnostics** | [**DiagnosticsRef**](DiagnosticsRef.md) |  |  [optional] |
|**endpoints** | [**List&lt;EndpointProperties&gt;**](EndpointProperties.md) | The endpoints exposed by this container. |  [optional] |
|**entrypoint** | **String** | Override for the default entry point in the container. |  [optional] |
|**environmentVariables** | [**List&lt;EnvironmentVariable&gt;**](EnvironmentVariable.md) | The environment variables to set in this container |  [optional] |
|**image** | **String** | The Container image to use. |  |
|**imageRegistryCredential** | [**ImageRegistryCredential**](ImageRegistryCredential.md) |  |  [optional] |
|**instanceView** | [**ContainerInstanceView**](ContainerInstanceView.md) |  |  [optional] |
|**labels** | [**List&lt;ContainerLabel&gt;**](ContainerLabel.md) | The labels to set in this container. |  [optional] |
|**name** | **String** | The name of the code package. |  |
|**resources** | [**ResourceRequirements**](ResourceRequirements.md) |  |  |
|**settings** | [**List&lt;Setting&gt;**](Setting.md) | The settings to set in this container. The setting file path can be fetched from environment variable \&quot;Fabric_SettingPath\&quot;. The path for Windows container is \&quot;C:\\\\secrets\&quot;. The path for Linux container is \&quot;/var/secrets\&quot;. |  [optional] |
|**volumeRefs** | [**List&lt;ContainerVolume&gt;**](ContainerVolume.md) | The volumes to be attached to the container. |  [optional] |



