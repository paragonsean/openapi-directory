# RudderApi.NodeFull

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **[String]** | User accounts declared in the node | [optional] 
**architectureDescription** | **String** | Information about CPU architecture (32/64 bits) | [optional] 
**bios** | [**NodeFullBios**](NodeFullBios.md) |  | [optional] 
**controllers** | [**[NodeFullControllersInner]**](NodeFullControllersInner.md) | Physical controller information | [optional] 
**description** | **String** | A human intended description of the node (not used) | [optional] 
**environmentVariables** | [**[NodeFullEnvironmentVariablesInner]**](NodeFullEnvironmentVariablesInner.md) | Environment variables defined on the node in the context of the agent | [optional] 
**fileSystems** | [**[NodeFullFileSystemsInner]**](NodeFullFileSystemsInner.md) | File system declared on the node | [optional] 
**hostname** | **String** | Fully qualified name of the node | 
**id** | **String** | Unique id of the node | 
**ipAddresses** | **[String]** | IP addresses of the node (IPv4 and IPv6) | 
**lastInventoryDate** | **Date** | Date and time of the latest generated inventory, if one is available (node time). Up to API v11, format was: \&quot;YYYY-MM-dd HH:mm\&quot; | [optional] 
**lastRunDate** | **Date** | Date and time of the latest run, if one is available (node time). Up to API v11, format was: \&quot;YYYY-MM-dd HH:mm\&quot; | [optional] 
**machine** | [**NodeFullMachine**](NodeFullMachine.md) |  | [optional] 
**managementTechnology** | [**[NodeFullManagementTechnologyInner]**](NodeFullManagementTechnologyInner.md) | Management agents running on the node | 
**managementTechnologyDetails** | [**NodeFullManagementTechnologyDetails**](NodeFullManagementTechnologyDetails.md) |  | [optional] 
**memories** | [**[NodeFullMemoriesInner]**](NodeFullMemoriesInner.md) | Memory slots | [optional] 
**networkInterfaces** | [**[NodeFullNetworkInterfacesInner]**](NodeFullNetworkInterfacesInner.md) | Detailed information about registered network interfaces on the node | [optional] 
**os** | [**NodeFullOs**](NodeFullOs.md) |  | [optional] 
**policyMode** | **String** | Rudder policy mode for the node (&#x60;default&#x60; follows the global configuration) | [optional] 
**policyServerId** | **String** | Rudder policy server managing the node | 
**ports** | [**[NodeFullPortsInner]**](NodeFullPortsInner.md) | Physical port information objects | [optional] 
**processes** | [**[NodeFullProcessesInner]**](NodeFullProcessesInner.md) | Process running (at inventory time) | [optional] 
**processors** | [**[NodeFullProcessorsInner]**](NodeFullProcessorsInner.md) | CPU information | [optional] 
**properties** | [**[NodeAddInnerPropertiesInner]**](NodeAddInnerPropertiesInner.md) | Node properties (either set by user or filled by third party sources) | 
**ram** | **Number** | Size of RAM in MB | [optional] 
**slots** | [**[NodeFullSlotsInner]**](NodeFullSlotsInner.md) | Physical extension slot information | [optional] 
**software** | [**[NodeFullSoftwareInner]**](NodeFullSoftwareInner.md) | Software installed on the node (can have thousands items) | [optional] 
**softwareUpdate** | [**[NodeFullSoftwareUpdateInner]**](NodeFullSoftwareUpdateInner.md) | Software that can be updated on that machine | [optional] 
**sound** | [**[NodeFullSoundInner]**](NodeFullSoundInner.md) | Sound card information | [optional] 
**status** | **String** | Status of the node | 
**storage** | [**[NodeFullStorageInner]**](NodeFullStorageInner.md) | Storage (disks) information objects | [optional] 
**timezone** | [**NodeFullTimezone**](NodeFullTimezone.md) |  | [optional] 
**videos** | [**[NodeFullVideosInner]**](NodeFullVideosInner.md) | Video card information | [optional] 
**virtualMachines** | [**[NodeFullVirtualMachinesInner]**](NodeFullVirtualMachinesInner.md) | Hosted virtual machine information | [optional] 



## Enum: PolicyModeEnum


* `enforce` (value: `"enforce"`)

* `audit` (value: `"audit"`)

* `default` (value: `"default"`)





## Enum: StatusEnum


* `pending` (value: `"pending"`)

* `accepted` (value: `"accepted"`)

* `deleted` (value: `"deleted"`)




