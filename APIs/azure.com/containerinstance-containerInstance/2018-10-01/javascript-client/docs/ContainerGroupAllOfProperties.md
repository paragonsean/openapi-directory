# ContainerInstanceManagementClient.ContainerGroupAllOfProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containers** | [**[Container]**](Container.md) | The containers within the container group. | 
**diagnostics** | [**ContainerGroupDiagnostics**](ContainerGroupDiagnostics.md) |  | [optional] 
**dnsConfig** | [**DnsConfiguration**](DnsConfiguration.md) |  | [optional] 
**imageRegistryCredentials** | [**[ImageRegistryCredential]**](ImageRegistryCredential.md) | The image registry credentials by which the container group is created from. | [optional] 
**instanceView** | [**ContainerGroupAllOfPropertiesInstanceView**](ContainerGroupAllOfPropertiesInstanceView.md) |  | [optional] 
**ipAddress** | [**IpAddress**](IpAddress.md) |  | [optional] 
**networkProfile** | [**ContainerGroupNetworkProfile**](ContainerGroupNetworkProfile.md) |  | [optional] 
**osType** | **String** | The operating system type required by the containers in the container group. | 
**provisioningState** | **String** | The provisioning state of the container group. This only appears in the response. | [optional] [readonly] 
**restartPolicy** | **String** | Restart policy for all containers within the container group.  - &#x60;Always&#x60; Always restart - &#x60;OnFailure&#x60; Restart on failure - &#x60;Never&#x60; Never restart  | [optional] 
**volumes** | [**[Volume]**](Volume.md) | The list of volumes that can be mounted by containers in this container group. | [optional] 



## Enum: OsTypeEnum


* `Windows` (value: `"Windows"`)

* `Linux` (value: `"Linux"`)





## Enum: RestartPolicyEnum


* `Always` (value: `"Always"`)

* `OnFailure` (value: `"OnFailure"`)

* `Never` (value: `"Never"`)




