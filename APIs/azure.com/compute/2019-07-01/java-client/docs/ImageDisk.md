

# ImageDisk

Describes a image disk.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blobUri** | **String** | The Virtual Hard Disk. |  [optional] |
|**caching** | [**CachingEnum**](#CachingEnum) | Specifies the caching requirements. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;&lt;br&gt; **None** &lt;br&gt;&lt;br&gt; **ReadOnly** &lt;br&gt;&lt;br&gt; **ReadWrite** &lt;br&gt;&lt;br&gt; Default: **None for Standard storage. ReadOnly for Premium storage** |  [optional] |
|**diskEncryptionSet** | [**DiskEncryptionSetParameters**](DiskEncryptionSetParameters.md) |  |  [optional] |
|**diskSizeGB** | **Integer** | Specifies the size of empty data disks in gigabytes. This element can be used to overwrite the name of the disk in a virtual machine image. &lt;br&gt;&lt;br&gt; This value cannot be larger than 1023 GB |  [optional] |
|**managedDisk** | [**SubResource**](SubResource.md) |  |  [optional] |
|**snapshot** | [**SubResource**](SubResource.md) |  |  [optional] |
|**storageAccountType** | **StorageAccountType** |  |  [optional] |



## Enum: CachingEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| READ_ONLY | &quot;ReadOnly&quot; |
| READ_WRITE | &quot;ReadWrite&quot; |



