# ComputeManagementClient.DataDisk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caching** | [**Caching**](Caching.md) |  | [optional] 
**createOption** | [**CreateOption**](CreateOption.md) |  | 
**diskSizeGB** | **Number** | Specifies the size of an empty data disk in gigabytes. This element can be used to overwrite the size of the disk in a virtual machine image. &lt;br&gt;&lt;br&gt; This value cannot be larger than 1023 GB | [optional] 
**image** | [**VirtualHardDisk**](VirtualHardDisk.md) |  | [optional] 
**lun** | **Number** | Specifies the logical unit number of the data disk. This value is used to identify data disks within the VM and therefore must be unique for each data disk attached to a VM. | 
**managedDisk** | [**ManagedDiskParameters**](ManagedDiskParameters.md) |  | [optional] 
**name** | **String** | The disk name. | [optional] 
**vhd** | [**VirtualHardDisk**](VirtualHardDisk.md) |  | [optional] 


