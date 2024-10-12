

# MachineDetails

Details of a machine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**architecture** | [**MachineArchitectureDetails**](MachineArchitectureDetails.md) |  |  [optional] |
|**coreCount** | **Integer** | Number of CPU cores in the machine. Must be non-negative. |  [optional] |
|**createTime** | **String** | Machine creation time. |  [optional] |
|**disks** | [**MachineDiskDetails**](MachineDiskDetails.md) |  |  [optional] |
|**guestOs** | [**GuestOsDetails**](GuestOsDetails.md) |  |  [optional] |
|**machineName** | **String** | Machine name. |  [optional] |
|**memoryMb** | **Integer** | The amount of memory in the machine. Must be non-negative. |  [optional] |
|**network** | [**MachineNetworkDetails**](MachineNetworkDetails.md) |  |  [optional] |
|**platform** | [**PlatformDetails**](PlatformDetails.md) |  |  [optional] |
|**powerState** | [**PowerStateEnum**](#PowerStateEnum) | Power state of the machine. |  [optional] |
|**uuid** | **String** | Machine unique identifier. |  [optional] |



## Enum: PowerStateEnum

| Name | Value |
|---- | -----|
| POWER_STATE_UNSPECIFIED | &quot;POWER_STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| SUSPENDING | &quot;SUSPENDING&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |
| DELETING | &quot;DELETING&quot; |
| DELETED | &quot;DELETED&quot; |



