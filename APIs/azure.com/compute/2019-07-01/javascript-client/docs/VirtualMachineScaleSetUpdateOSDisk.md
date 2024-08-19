# ComputeManagementClient.VirtualMachineScaleSetUpdateOSDisk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caching** | [**Caching**](Caching.md) |  | [optional] 
**diskSizeGB** | **Number** | Specifies the size of the operating system disk in gigabytes. This element can be used to overwrite the size of the disk in a virtual machine image. &lt;br&gt;&lt;br&gt; This value cannot be larger than 1023 GB | [optional] 
**image** | [**VirtualHardDisk**](VirtualHardDisk.md) |  | [optional] 
**managedDisk** | [**VirtualMachineScaleSetManagedDiskParameters**](VirtualMachineScaleSetManagedDiskParameters.md) |  | [optional] 
**vhdContainers** | **[String]** | The list of virtual hard disk container uris. | [optional] 
**writeAcceleratorEnabled** | **Boolean** | Specifies whether writeAccelerator should be enabled or disabled on the disk. | [optional] 


