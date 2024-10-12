

# MachineProperties

Properties of a machine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bootType** | [**BootTypeEnum**](#BootTypeEnum) | Boot type of the machine. |  [optional] [readonly] |
|**createdTimestamp** | **OffsetDateTime** | Time when this machine was created. Date-Time represented in ISO-8601 format. |  [optional] [readonly] |
|**datacenterContainer** | **String** | Container defined in the management solution that this machine is part of in the datacenter. |  [optional] [readonly] |
|**datacenterMachineId** | **String** | ID of the machine as tracked by the datacenter management solution. |  [optional] [readonly] |
|**datacenterManagementServer** | **String** | Name of the server hosting the datacenter management solution. |  [optional] [readonly] |
|**datacenterManagementServerId** | **String** | ID of the server hosting the datacenter management solution. |  [optional] [readonly] |
|**description** | **String** | Description of the machine |  [optional] [readonly] |
|**discoveredTimestamp** | **OffsetDateTime** | Time when this machine was discovered by Azure Migrate agent. Date-Time represented in ISO-8601 format. |  [optional] [readonly] |
|**disks** | [**Map&lt;String, Disk&gt;**](Disk.md) | Dictionary of disks attached to the machine. Key is ID of disk. Value is a disk object |  [optional] [readonly] |
|**displayName** | **String** | User readable name of the machine as defined by the user in their private datacenter. |  [optional] [readonly] |
|**groups** | **List&lt;String&gt;** | List of references to the groups that the machine is member of. |  [optional] [readonly] |
|**megabytesOfMemory** | **BigDecimal** | Memory in Megabytes. |  [optional] [readonly] |
|**networkAdapters** | [**Map&lt;String, NetworkAdapter&gt;**](NetworkAdapter.md) | Dictionary of network adapters attached to the machine. Key is ID of network adapter. Value is a network adapter object |  [optional] [readonly] |
|**numberOfCores** | **Integer** | Processor count. |  [optional] [readonly] |
|**operatingSystem** | **String** | Operating System of the machine. |  [optional] [readonly] |
|**updatedTimestamp** | **OffsetDateTime** | Time when this machine was last updated. Date-Time represented in ISO-8601 format. |  [optional] [readonly] |



## Enum: BootTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| EFI | &quot;EFI&quot; |
| BIOS | &quot;BIOS&quot; |



