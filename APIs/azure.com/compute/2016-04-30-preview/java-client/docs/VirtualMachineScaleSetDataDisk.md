

# VirtualMachineScaleSetDataDisk

Describes a virtual machine scale set data disk.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caching** | **Caching** |  |  [optional] |
|**createOption** | **CreateOption** |  |  |
|**diskSizeGB** | **Integer** | Specifies the size of an empty data disk in gigabytes. This element can be used to overwrite the size of the disk in a virtual machine image. &lt;br&gt;&lt;br&gt; This value cannot be larger than 1023 GB |  [optional] |
|**lun** | **Integer** | Specifies the logical unit number of the data disk. This value is used to identify data disks within the VM and therefore must be unique for each data disk attached to a VM. |  |
|**managedDisk** | [**VirtualMachineScaleSetManagedDiskParameters**](VirtualMachineScaleSetManagedDiskParameters.md) |  |  [optional] |
|**name** | **String** | The disk name. |  [optional] |



