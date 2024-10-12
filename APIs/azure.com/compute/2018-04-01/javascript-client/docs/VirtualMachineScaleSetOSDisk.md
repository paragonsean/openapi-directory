# ComputeManagementClient.VirtualMachineScaleSetOSDisk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caching** | [**Caching**](Caching.md) |  | [optional] 
**createOption** | [**CreateOption**](CreateOption.md) |  | 
**diskSizeGB** | **Number** | Specifies the size of the operating system disk in gigabytes. This element can be used to overwrite the size of the disk in a virtual machine image. &lt;br&gt;&lt;br&gt; This value cannot be larger than 1023 GB | [optional] 
**image** | [**VirtualHardDisk**](VirtualHardDisk.md) |  | [optional] 
**managedDisk** | [**VirtualMachineScaleSetManagedDiskParameters**](VirtualMachineScaleSetManagedDiskParameters.md) |  | [optional] 
**name** | **String** | The disk name. | [optional] 
**osType** | **String** | This property allows you to specify the type of the OS that is included in the disk if creating a VM from user-image or a specialized VHD. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;&lt;br&gt; **Windows** &lt;br&gt;&lt;br&gt; **Linux** | [optional] 
**vhdContainers** | **[String]** | Specifies the container urls that are used to store operating system disks for the scale set. | [optional] 
**writeAcceleratorEnabled** | **Boolean** | Specifies whether writeAccelerator should be enabled or disabled on the disk. | [optional] 



## Enum: OsTypeEnum


* `Windows` (value: `"Windows"`)

* `Linux` (value: `"Linux"`)




