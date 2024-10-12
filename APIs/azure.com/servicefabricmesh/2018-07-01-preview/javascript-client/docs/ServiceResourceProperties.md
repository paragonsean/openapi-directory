# SeaBreezeManagementClient.ServiceResourceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codePackages** | [**[ContainerCodePackageProperties]**](ContainerCodePackageProperties.md) | Describes the set of code packages that forms the service. A code package describes the container and the properties for running it. All the code packages are started together on the same host and share the same context (network, process etc.).  | 
**diagnostics** | [**DiagnosticsRef**](DiagnosticsRef.md) |  | [optional] 
**networkRefs** | [**[NetworkRef]**](NetworkRef.md) | The names of the private networks that this service needs to be part of. | [optional] 
**osType** | **String** | The Operating system type required by the code in service.  | 
**description** | **String** | User readable description of the service. | [optional] 
**healthState** | [**HealthState**](HealthState.md) |  | [optional] 
**replicaCount** | **Number** | The number of replicas of the service to create. Defaults to 1 if not specified. | [optional] 
**status** | **String** | Represents the status of the service. | [optional] [readonly] 



## Enum: OsTypeEnum


* `Linux` (value: `"Linux"`)

* `Windows` (value: `"Windows"`)





## Enum: StatusEnum


* `Unknown` (value: `"Unknown"`)

* `Active` (value: `"Active"`)

* `Upgrading` (value: `"Upgrading"`)

* `Deleting` (value: `"Deleting"`)

* `Creating` (value: `"Creating"`)

* `Failed` (value: `"Failed"`)




