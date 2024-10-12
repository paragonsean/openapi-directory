# MigrationCenterApi.MachineDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | [**MachineArchitectureDetails**](MachineArchitectureDetails.md) |  | [optional] 
**coreCount** | **Number** | Number of CPU cores in the machine. Must be non-negative. | [optional] 
**createTime** | **String** | Machine creation time. | [optional] 
**disks** | [**MachineDiskDetails**](MachineDiskDetails.md) |  | [optional] 
**guestOs** | [**GuestOsDetails**](GuestOsDetails.md) |  | [optional] 
**machineName** | **String** | Machine name. | [optional] 
**memoryMb** | **Number** | The amount of memory in the machine. Must be non-negative. | [optional] 
**network** | [**MachineNetworkDetails**](MachineNetworkDetails.md) |  | [optional] 
**platform** | [**PlatformDetails**](PlatformDetails.md) |  | [optional] 
**powerState** | **String** | Power state of the machine. | [optional] 
**uuid** | **String** | Machine unique identifier. | [optional] 



## Enum: PowerStateEnum


* `POWER_STATE_UNSPECIFIED` (value: `"POWER_STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `SUSPENDING` (value: `"SUSPENDING"`)

* `SUSPENDED` (value: `"SUSPENDED"`)

* `DELETING` (value: `"DELETING"`)

* `DELETED` (value: `"DELETED"`)




