# SeaBreezeManagementClient.ServiceReplicaProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codePackages** | [**[ContainerCodePackageProperties]**](ContainerCodePackageProperties.md) | Describes the set of code packages that forms the service. A code package describes the container and the properties for running it. All the code packages are started together on the same host and share the same context (network, process etc.).  | 
**diagnostics** | [**DiagnosticsRef**](DiagnosticsRef.md) |  | [optional] 
**networkRefs** | [**[NetworkRef]**](NetworkRef.md) | The names of the private networks that this service needs to be part of. | [optional] 
**osType** | **String** | The Operating system type required by the code in service.  | 



## Enum: OsTypeEnum


* `Linux` (value: `"Linux"`)

* `Windows` (value: `"Windows"`)




