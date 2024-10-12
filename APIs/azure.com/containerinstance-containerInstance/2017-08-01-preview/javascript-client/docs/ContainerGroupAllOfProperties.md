# ContainerInstanceManagementClient.ContainerGroupAllOfProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containers** | [**[Container]**](Container.md) | The containers within the container group. | 
**imageRegistryCredentials** | [**[ImageRegistryCredential]**](ImageRegistryCredential.md) | The image registry credentials by which the container group is created from. | [optional] 
**ipAddress** | [**IpAddress**](IpAddress.md) |  | [optional] 
**osType** | **String** | The operating system type required by the containers in the container group. | 
**provisioningState** | **String** | The provisioning state of the container group. This only appears in the response. | [optional] [readonly] 
**restartPolicy** | **String** | Restart policy for all containers within the container group. Currently the only available option is &#x60;always&#x60;. | [optional] 
**state** | **String** | The current state of the container group. This is only valid for the response. | [optional] [readonly] 
**volumes** | [**[Volume]**](Volume.md) | The list of volumes that can be mounted by containers in this container group. | [optional] 



## Enum: OsTypeEnum


* `Windows` (value: `"Windows"`)

* `Linux` (value: `"Linux"`)





## Enum: RestartPolicyEnum


* `always` (value: `"always"`)




