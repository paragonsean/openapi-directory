# AzureMigrateV2.MachineProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bootType** | **String** | Boot type of the machine. | [optional] [readonly] 
**createdTimestamp** | **Date** | Time when this machine was created. Date-Time represented in ISO-8601 format. | [optional] [readonly] 
**datacenterManagementServerArmId** | **String** | ARM ID of the data center as tracked by the Microsoft.OffAzure. | [optional] [readonly] 
**datacenterManagementServerName** | **String** | Name of the server hosting the datacenter management solution. | [optional] [readonly] 
**description** | **String** | Description of the machine | [optional] [readonly] 
**discoveryMachineArmId** | **String** | ARM ID of the machine as tracked by the Microsoft.OffAzure. | [optional] [readonly] 
**disks** | [**{String: Disk}**](Disk.md) | Dictionary of disks attached to the machine. Key is ID of disk. Value is a disk object | [optional] [readonly] 
**displayName** | **String** | User readable name of the machine as defined by the user in their private datacenter. | [optional] [readonly] 
**groups** | **[String]** | List of references to the groups that the machine is member of. | [optional] [readonly] 
**megabytesOfMemory** | **Number** | Memory in Megabytes. | [optional] [readonly] 
**networkAdapters** | [**{String: NetworkAdapter}**](NetworkAdapter.md) | Dictionary of network adapters attached to the machine. Key is ID of network adapter. Value is a network adapter object | [optional] [readonly] 
**numberOfCores** | **Number** | Processor count. | [optional] [readonly] 
**operatingSystemName** | **String** | Operating System name of the machine. | [optional] [readonly] 
**operatingSystemType** | **String** | Operating System type of the machine. | [optional] [readonly] 
**operatingSystemVersion** | **String** | Operating System version of the machine. | [optional] [readonly] 
**updatedTimestamp** | **Date** | Time when this machine was last updated. Date-Time represented in ISO-8601 format. | [optional] [readonly] 



## Enum: BootTypeEnum


* `Unknown` (value: `"Unknown"`)

* `EFI` (value: `"EFI"`)

* `BIOS` (value: `"BIOS"`)




