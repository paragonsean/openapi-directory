# ComputeManagementClient.VirtualMachineScaleSetOSDisk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caching** | [**Caching**](Caching.md) |  | [optional] 
**createOption** | [**CreateOption**](CreateOption.md) |  | 
**image** | [**VirtualHardDisk**](VirtualHardDisk.md) |  | [optional] 
**managedDisk** | [**VirtualMachineScaleSetManagedDiskParameters**](VirtualMachineScaleSetManagedDiskParameters.md) |  | [optional] 
**name** | **String** | The disk name. | [optional] 
**osType** | **String** | This property allows you to specify the type of the OS that is included in the disk if creating a VM from user-image or a specialized VHD. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;&lt;br&gt; **Windows** &lt;br&gt;&lt;br&gt; **Linux** | [optional] 
**vhdContainers** | **[String]** | The list of virtual hard disk container uris. | [optional] 



## Enum: OsTypeEnum


* `Windows` (value: `"Windows"`)

* `Linux` (value: `"Linux"`)




