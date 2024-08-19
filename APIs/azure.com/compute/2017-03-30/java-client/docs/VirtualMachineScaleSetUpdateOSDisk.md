

# VirtualMachineScaleSetUpdateOSDisk

Describes virtual machine scale set operating system disk Update Object. This should be used for Updating VMSS OS Disk.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caching** | **Caching** |  |  [optional] |
|**image** | [**VirtualHardDisk**](VirtualHardDisk.md) |  |  [optional] |
|**managedDisk** | [**VirtualMachineScaleSetManagedDiskParameters**](VirtualMachineScaleSetManagedDiskParameters.md) |  |  [optional] |
|**vhdContainers** | **List&lt;String&gt;** | The list of virtual hard disk container uris. |  [optional] |



