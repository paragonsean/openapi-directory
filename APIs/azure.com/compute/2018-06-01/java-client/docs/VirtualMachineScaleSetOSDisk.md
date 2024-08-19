

# VirtualMachineScaleSetOSDisk

Describes a virtual machine scale set operating system disk.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caching** | **Caching** |  |  [optional] |
|**createOption** | **CreateOption** |  |  |
|**diffDiskSettings** | [**DiffDiskSettings**](DiffDiskSettings.md) |  |  [optional] |
|**diskSizeGB** | **Integer** | Specifies the size of the operating system disk in gigabytes. This element can be used to overwrite the size of the disk in a virtual machine image. &lt;br&gt;&lt;br&gt; This value cannot be larger than 1023 GB |  [optional] |
|**image** | [**VirtualHardDisk**](VirtualHardDisk.md) |  |  [optional] |
|**managedDisk** | [**VirtualMachineScaleSetManagedDiskParameters**](VirtualMachineScaleSetManagedDiskParameters.md) |  |  [optional] |
|**name** | **String** | The disk name. |  [optional] |
|**osType** | [**OsTypeEnum**](#OsTypeEnum) | This property allows you to specify the type of the OS that is included in the disk if creating a VM from user-image or a specialized VHD. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;&lt;br&gt; **Windows** &lt;br&gt;&lt;br&gt; **Linux** |  [optional] |
|**vhdContainers** | **List&lt;String&gt;** | Specifies the container urls that are used to store operating system disks for the scale set. |  [optional] |
|**writeAcceleratorEnabled** | **Boolean** | Specifies whether writeAccelerator should be enabled or disabled on the disk. |  [optional] |



## Enum: OsTypeEnum

| Name | Value |
|---- | -----|
| WINDOWS | &quot;Windows&quot; |
| LINUX | &quot;Linux&quot; |



