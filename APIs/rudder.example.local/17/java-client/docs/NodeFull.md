

# NodeFull


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accounts** | **List&lt;String&gt;** | User accounts declared in the node |  [optional] |
|**architectureDescription** | **String** | Information about CPU architecture (32/64 bits) |  [optional] |
|**bios** | [**NodeFullBios**](NodeFullBios.md) |  |  [optional] |
|**controllers** | [**List&lt;NodeFullControllersInner&gt;**](NodeFullControllersInner.md) | Physical controller information |  [optional] |
|**description** | **String** | A human intended description of the node (not used) |  [optional] |
|**environmentVariables** | [**List&lt;NodeFullEnvironmentVariablesInner&gt;**](NodeFullEnvironmentVariablesInner.md) | Environment variables defined on the node in the context of the agent |  [optional] |
|**fileSystems** | [**List&lt;NodeFullFileSystemsInner&gt;**](NodeFullFileSystemsInner.md) | File system declared on the node |  [optional] |
|**hostname** | **String** | Fully qualified name of the node |  |
|**id** | **String** | Unique id of the node |  |
|**ipAddresses** | **List&lt;String&gt;** | IP addresses of the node (IPv4 and IPv6) |  |
|**lastInventoryDate** | **LocalDate** | Date and time of the latest generated inventory, if one is available (node time). Up to API v11, format was: \&quot;YYYY-MM-dd HH:mm\&quot; |  [optional] |
|**lastRunDate** | **LocalDate** | Date and time of the latest run, if one is available (node time). Up to API v11, format was: \&quot;YYYY-MM-dd HH:mm\&quot; |  [optional] |
|**machine** | [**NodeFullMachine**](NodeFullMachine.md) |  |  [optional] |
|**managementTechnology** | [**List&lt;NodeFullManagementTechnologyInner&gt;**](NodeFullManagementTechnologyInner.md) | Management agents running on the node |  |
|**managementTechnologyDetails** | [**NodeFullManagementTechnologyDetails**](NodeFullManagementTechnologyDetails.md) |  |  [optional] |
|**memories** | [**List&lt;NodeFullMemoriesInner&gt;**](NodeFullMemoriesInner.md) | Memory slots |  [optional] |
|**networkInterfaces** | [**List&lt;NodeFullNetworkInterfacesInner&gt;**](NodeFullNetworkInterfacesInner.md) | Detailed information about registered network interfaces on the node |  [optional] |
|**os** | [**NodeFullOs**](NodeFullOs.md) |  |  [optional] |
|**policyMode** | [**PolicyModeEnum**](#PolicyModeEnum) | Rudder policy mode for the node (&#x60;default&#x60; follows the global configuration) |  [optional] |
|**policyServerId** | **String** | Rudder policy server managing the node |  |
|**ports** | [**List&lt;NodeFullPortsInner&gt;**](NodeFullPortsInner.md) | Physical port information objects |  [optional] |
|**processes** | [**List&lt;NodeFullProcessesInner&gt;**](NodeFullProcessesInner.md) | Process running (at inventory time) |  [optional] |
|**processors** | [**List&lt;NodeFullProcessorsInner&gt;**](NodeFullProcessorsInner.md) | CPU information |  [optional] |
|**properties** | [**List&lt;NodeAddInnerPropertiesInner&gt;**](NodeAddInnerPropertiesInner.md) | Node properties (either set by user or filled by third party sources) |  |
|**ram** | **Integer** | Size of RAM in MB |  [optional] |
|**slots** | [**List&lt;NodeFullSlotsInner&gt;**](NodeFullSlotsInner.md) | Physical extension slot information |  [optional] |
|**software** | [**List&lt;NodeFullSoftwareInner&gt;**](NodeFullSoftwareInner.md) | Software installed on the node (can have thousands items) |  [optional] |
|**softwareUpdate** | [**List&lt;NodeFullSoftwareUpdateInner&gt;**](NodeFullSoftwareUpdateInner.md) | Software that can be updated on that machine |  [optional] |
|**sound** | [**List&lt;NodeFullSoundInner&gt;**](NodeFullSoundInner.md) | Sound card information |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the node |  |
|**storage** | [**List&lt;NodeFullStorageInner&gt;**](NodeFullStorageInner.md) | Storage (disks) information objects |  [optional] |
|**timezone** | [**NodeFullTimezone**](NodeFullTimezone.md) |  |  [optional] |
|**videos** | [**List&lt;NodeFullVideosInner&gt;**](NodeFullVideosInner.md) | Video card information |  [optional] |
|**virtualMachines** | [**List&lt;NodeFullVirtualMachinesInner&gt;**](NodeFullVirtualMachinesInner.md) | Hosted virtual machine information |  [optional] |



## Enum: PolicyModeEnum

| Name | Value |
|---- | -----|
| ENFORCE | &quot;enforce&quot; |
| AUDIT | &quot;audit&quot; |
| DEFAULT | &quot;default&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| ACCEPTED | &quot;accepted&quot; |
| DELETED | &quot;deleted&quot; |



