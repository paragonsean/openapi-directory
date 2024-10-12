

# ServiceResourceProperties

This type describes properties of a service resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**codePackages** | [**List&lt;ContainerCodePackageProperties&gt;**](ContainerCodePackageProperties.md) | Describes the set of code packages that forms the service. A code package describes the container and the properties for running it. All the code packages are started together on the same host and share the same context (network, process etc.). |  |
|**diagnostics** | [**DiagnosticsRef**](DiagnosticsRef.md) |  |  [optional] |
|**networkRefs** | [**List&lt;NetworkRef&gt;**](NetworkRef.md) | The names of the private networks that this service needs to be part of. |  [optional] |
|**osType** | [**OsTypeEnum**](#OsTypeEnum) | The Operating system type required by the code in service. |  |
|**description** | **String** | User readable description of the service. |  [optional] |
|**healthState** | **HealthState** |  |  [optional] |
|**replicaCount** | **Integer** | The number of replicas of the service to create. Defaults to 1 if not specified. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Represents the status of the service. |  [optional] [readonly] |



## Enum: OsTypeEnum

| Name | Value |
|---- | -----|
| LINUX | &quot;Linux&quot; |
| WINDOWS | &quot;Windows&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| ACTIVE | &quot;Active&quot; |
| UPGRADING | &quot;Upgrading&quot; |
| DELETING | &quot;Deleting&quot; |
| CREATING | &quot;Creating&quot; |
| FAILED | &quot;Failed&quot; |



