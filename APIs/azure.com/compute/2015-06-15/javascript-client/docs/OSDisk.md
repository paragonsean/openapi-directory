# ComputeManagementClient.OSDisk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caching** | [**Caching**](Caching.md) |  | [optional] 
**createOption** | [**CreateOption**](CreateOption.md) |  | 
**diskSizeGB** | **Number** | Specifies the size of an empty data disk in gigabytes. This element can be used to overwrite the size of the disk in a virtual machine image. &lt;br&gt;&lt;br&gt; This value cannot be larger than 1023 GB | [optional] 
**encryptionSettings** | [**DiskEncryptionSettings**](DiskEncryptionSettings.md) |  | [optional] 
**image** | [**VirtualHardDisk**](VirtualHardDisk.md) |  | [optional] 
**name** | **String** | The disk name. | 
**osType** | **String** | This property allows you to specify the type of the OS that is included in the disk if creating a VM from user-image or a specialized VHD. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;&lt;br&gt; **Windows** &lt;br&gt;&lt;br&gt; **Linux** | [optional] 
**vhd** | [**VirtualHardDisk**](VirtualHardDisk.md) |  | 



## Enum: OsTypeEnum


* `Windows` (value: `"Windows"`)

* `Linux` (value: `"Linux"`)




