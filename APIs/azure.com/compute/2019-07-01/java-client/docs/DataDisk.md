

# DataDisk

Describes a data disk.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caching** | **Caching** |  |  [optional] |
|**createOption** | **CreateOption** |  |  |
|**diskIOPSReadWrite** | **Long** | Specifies the Read-Write IOPS for the managed disk when StorageAccountType is UltraSSD_LRS. Returned only for VirtualMachine ScaleSet VM disks. Can be updated only via updates to the VirtualMachine Scale Set. |  [optional] [readonly] |
|**diskMBpsReadWrite** | **Long** | Specifies the bandwidth in MB per second for the managed disk when StorageAccountType is UltraSSD_LRS. Returned only for VirtualMachine ScaleSet VM disks. Can be updated only via updates to the VirtualMachine Scale Set. |  [optional] [readonly] |
|**diskSizeGB** | **Integer** | Specifies the size of an empty data disk in gigabytes. This element can be used to overwrite the size of the disk in a virtual machine image. &lt;br&gt;&lt;br&gt; This value cannot be larger than 1023 GB |  [optional] |
|**image** | [**VirtualHardDisk**](VirtualHardDisk.md) |  |  [optional] |
|**lun** | **Integer** | Specifies the logical unit number of the data disk. This value is used to identify data disks within the VM and therefore must be unique for each data disk attached to a VM. |  |
|**managedDisk** | [**ManagedDiskParameters**](ManagedDiskParameters.md) |  |  [optional] |
|**name** | **String** | The disk name. |  [optional] |
|**toBeDetached** | **Boolean** | Specifies whether the data disk is in process of detachment from the VirtualMachine/VirtualMachineScaleset |  [optional] |
|**vhd** | [**VirtualHardDisk**](VirtualHardDisk.md) |  |  [optional] |
|**writeAcceleratorEnabled** | **Boolean** | Specifies whether writeAccelerator should be enabled or disabled on the disk. |  [optional] |



