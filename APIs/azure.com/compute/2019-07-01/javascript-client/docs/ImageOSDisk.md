# ComputeManagementClient.ImageOSDisk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**osState** | **String** | The OS State. | 
**osType** | **String** | This property allows you to specify the type of the OS that is included in the disk if creating a VM from a custom image. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;&lt;br&gt; **Windows** &lt;br&gt;&lt;br&gt; **Linux** | 
**blobUri** | **String** | The Virtual Hard Disk. | [optional] 
**caching** | **String** | Specifies the caching requirements. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;&lt;br&gt; **None** &lt;br&gt;&lt;br&gt; **ReadOnly** &lt;br&gt;&lt;br&gt; **ReadWrite** &lt;br&gt;&lt;br&gt; Default: **None for Standard storage. ReadOnly for Premium storage** | [optional] 
**diskEncryptionSet** | [**DiskEncryptionSetParameters**](DiskEncryptionSetParameters.md) |  | [optional] 
**diskSizeGB** | **Number** | Specifies the size of empty data disks in gigabytes. This element can be used to overwrite the name of the disk in a virtual machine image. &lt;br&gt;&lt;br&gt; This value cannot be larger than 1023 GB | [optional] 
**managedDisk** | [**SubResource**](SubResource.md) |  | [optional] 
**snapshot** | [**SubResource**](SubResource.md) |  | [optional] 
**storageAccountType** | [**StorageAccountType**](StorageAccountType.md) |  | [optional] 



## Enum: OsStateEnum


* `Generalized` (value: `"Generalized"`)

* `Specialized` (value: `"Specialized"`)





## Enum: OsTypeEnum


* `Windows` (value: `"Windows"`)

* `Linux` (value: `"Linux"`)





## Enum: CachingEnum


* `None` (value: `"None"`)

* `ReadOnly` (value: `"ReadOnly"`)

* `ReadWrite` (value: `"ReadWrite"`)




