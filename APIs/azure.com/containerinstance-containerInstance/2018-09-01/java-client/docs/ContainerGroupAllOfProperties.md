

# ContainerGroupAllOfProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containers** | [**List&lt;Container&gt;**](Container.md) | The containers within the container group. |  |
|**diagnostics** | [**ContainerGroupDiagnostics**](ContainerGroupDiagnostics.md) |  |  [optional] |
|**imageRegistryCredentials** | [**List&lt;ImageRegistryCredential&gt;**](ImageRegistryCredential.md) | The image registry credentials by which the container group is created from. |  [optional] |
|**instanceView** | [**ContainerGroupAllOfPropertiesInstanceView**](ContainerGroupAllOfPropertiesInstanceView.md) |  |  [optional] |
|**ipAddress** | [**IpAddress**](IpAddress.md) |  |  [optional] |
|**networkProfile** | [**ContainerGroupNetworkProfile**](ContainerGroupNetworkProfile.md) |  |  [optional] |
|**osType** | [**OsTypeEnum**](#OsTypeEnum) | The operating system type required by the containers in the container group. |  |
|**provisioningState** | **String** | The provisioning state of the container group. This only appears in the response. |  [optional] [readonly] |
|**restartPolicy** | [**RestartPolicyEnum**](#RestartPolicyEnum) | Restart policy for all containers within the container group.  - &#x60;Always&#x60; Always restart - &#x60;OnFailure&#x60; Restart on failure - &#x60;Never&#x60; Never restart  |  [optional] |
|**volumes** | [**List&lt;Volume&gt;**](Volume.md) | The list of volumes that can be mounted by containers in this container group. |  [optional] |



## Enum: OsTypeEnum

| Name | Value |
|---- | -----|
| WINDOWS | &quot;Windows&quot; |
| LINUX | &quot;Linux&quot; |



## Enum: RestartPolicyEnum

| Name | Value |
|---- | -----|
| ALWAYS | &quot;Always&quot; |
| ON_FAILURE | &quot;OnFailure&quot; |
| NEVER | &quot;Never&quot; |



