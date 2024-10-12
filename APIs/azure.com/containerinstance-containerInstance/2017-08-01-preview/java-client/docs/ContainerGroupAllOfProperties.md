

# ContainerGroupAllOfProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containers** | [**List&lt;Container&gt;**](Container.md) | The containers within the container group. |  |
|**imageRegistryCredentials** | [**List&lt;ImageRegistryCredential&gt;**](ImageRegistryCredential.md) | The image registry credentials by which the container group is created from. |  [optional] |
|**ipAddress** | [**IpAddress**](IpAddress.md) |  |  [optional] |
|**osType** | [**OsTypeEnum**](#OsTypeEnum) | The operating system type required by the containers in the container group. |  |
|**provisioningState** | **String** | The provisioning state of the container group. This only appears in the response. |  [optional] [readonly] |
|**restartPolicy** | [**RestartPolicyEnum**](#RestartPolicyEnum) | Restart policy for all containers within the container group. Currently the only available option is &#x60;always&#x60;. |  [optional] |
|**state** | **String** | The current state of the container group. This is only valid for the response. |  [optional] [readonly] |
|**volumes** | [**List&lt;Volume&gt;**](Volume.md) | The list of volumes that can be mounted by containers in this container group. |  [optional] |



## Enum: OsTypeEnum

| Name | Value |
|---- | -----|
| WINDOWS | &quot;Windows&quot; |
| LINUX | &quot;Linux&quot; |



## Enum: RestartPolicyEnum

| Name | Value |
|---- | -----|
| ALWAYS | &quot;always&quot; |



