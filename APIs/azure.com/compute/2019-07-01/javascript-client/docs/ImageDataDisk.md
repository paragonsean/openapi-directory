# ComputeManagementClient.ImageDataDisk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lun** | **Number** | Specifies the logical unit number of the data disk. This value is used to identify data disks within the VM and therefore must be unique for each data disk attached to a VM. | 
**blobUri** | **String** | The Virtual Hard Disk. | [optional] 
**caching** | **String** | Specifies the caching requirements. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;&lt;br&gt; **None** &lt;br&gt;&lt;br&gt; **ReadOnly** &lt;br&gt;&lt;br&gt; **ReadWrite** &lt;br&gt;&lt;br&gt; Default: **None for Standard storage. ReadOnly for Premium storage** | [optional] 
**diskEncryptionSet** | [**DiskEncryptionSetParameters**](DiskEncryptionSetParameters.md) |  | [optional] 
**diskSizeGB** | **Number** | Specifies the size of empty data disks in gigabytes. This element can be used to overwrite the name of the disk in a virtual machine image. &lt;br&gt;&lt;br&gt; This value cannot be larger than 1023 GB | [optional] 
**managedDisk** | [**SubResource**](SubResource.md) |  | [optional] 
**snapshot** | [**SubResource**](SubResource.md) |  | [optional] 
**storageAccountType** | [**StorageAccountType**](StorageAccountType.md) |  | [optional] 



## Enum: CachingEnum


* `None` (value: `"None"`)

* `ReadOnly` (value: `"ReadOnly"`)

* `ReadWrite` (value: `"ReadWrite"`)




