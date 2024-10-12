

# VirtualMachineScaleSetUpdateOSDisk

Describes virtual machine scale set operating system disk Update Object. This should be used for Updating VMSS OS Disk.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caching** | **Caching** |  |  [optional] |
|**diskSizeGB** | **Integer** | Specifies the size of the operating system disk in gigabytes. This element can be used to overwrite the size of the disk in a virtual machine image. &lt;br&gt;&lt;br&gt; This value cannot be larger than 1023 GB |  [optional] |
|**image** | [**VirtualHardDisk**](VirtualHardDisk.md) |  |  [optional] |
|**managedDisk** | [**VirtualMachineScaleSetManagedDiskParameters**](VirtualMachineScaleSetManagedDiskParameters.md) |  |  [optional] |
|**vhdContainers** | **List&lt;String&gt;** | The list of virtual hard disk container uris. |  [optional] |
|**writeAcceleratorEnabled** | **Boolean** | Specifies whether writeAccelerator should be enabled or disabled on the disk. |  [optional] |



