

# VirtualMachineScaleSetOSDisk

Describes a virtual machine scale set operating system disk.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caching** | **Caching** |  |  [optional] |
|**createOption** | **CreateOption** |  |  |
|**image** | [**VirtualHardDisk**](VirtualHardDisk.md) |  |  [optional] |
|**managedDisk** | [**VirtualMachineScaleSetManagedDiskParameters**](VirtualMachineScaleSetManagedDiskParameters.md) |  |  [optional] |
|**name** | **String** | The disk name. |  [optional] |
|**osType** | [**OsTypeEnum**](#OsTypeEnum) | This property allows you to specify the type of the OS that is included in the disk if creating a VM from user-image or a specialized VHD. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;&lt;br&gt; **Windows** &lt;br&gt;&lt;br&gt; **Linux** |  [optional] |
|**vhdContainers** | **List&lt;String&gt;** | The list of virtual hard disk container uris. |  [optional] |



## Enum: OsTypeEnum

| Name | Value |
|---- | -----|
| WINDOWS | &quot;Windows&quot; |
| LINUX | &quot;Linux&quot; |



