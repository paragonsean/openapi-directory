

# VirtualMachineDetails

Details of a VirtualMachine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**coreCount** | **Integer** | Number of CPU cores in the VirtualMachine. Must be non-negative. |  [optional] |
|**createTime** | **String** | VM creation timestamp. |  [optional] |
|**guestOs** | [**GuestOsDetails**](GuestOsDetails.md) |  |  [optional] |
|**memoryMb** | **Integer** | The amount of memory in the VirtualMachine. Must be non-negative. |  [optional] |
|**osFamily** | [**OsFamilyEnum**](#OsFamilyEnum) | What family the OS belong to, if known. |  [optional] |
|**osName** | **String** | The name of the operating system running on the VirtualMachine. |  [optional] |
|**osVersion** | **String** | The version of the operating system running on the virtual machine. |  [optional] |
|**platform** | [**PlatformDetails**](PlatformDetails.md) |  |  [optional] |
|**powerState** | **String** | Power state of VM (poweredOn or poweredOff). |  [optional] |
|**vcenterFolder** | **String** | Folder name in vCenter where asset resides. |  [optional] |
|**vcenterUrl** | **String** | vCenter URL used in collection. |  [optional] |
|**vcenterVmId** | **String** | vCenter VM ID. |  [optional] |
|**vmArchitecture** | [**VirtualMachineArchitectureDetails**](VirtualMachineArchitectureDetails.md) |  |  [optional] |
|**vmDisks** | [**VirtualMachineDiskDetails**](VirtualMachineDiskDetails.md) |  |  [optional] |
|**vmName** | **String** | Virtual Machine display name. |  [optional] |
|**vmNetwork** | [**VirtualMachineNetworkDetails**](VirtualMachineNetworkDetails.md) |  |  [optional] |
|**vmUuid** | **String** | Virtual Machine unique identifier. |  [optional] |



## Enum: OsFamilyEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;OS_FAMILY_UNKNOWN&quot; |
| WINDOWS | &quot;OS_FAMILY_WINDOWS&quot; |
| LINUX | &quot;OS_FAMILY_LINUX&quot; |
| UNIX | &quot;OS_FAMILY_UNIX&quot; |



