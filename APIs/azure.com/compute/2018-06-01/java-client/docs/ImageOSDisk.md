

# ImageOSDisk

Describes an Operating System disk.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blobUri** | **String** | The Virtual Hard Disk. |  [optional] |
|**caching** | [**CachingEnum**](#CachingEnum) | Specifies the caching requirements. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;&lt;br&gt; **None** &lt;br&gt;&lt;br&gt; **ReadOnly** &lt;br&gt;&lt;br&gt; **ReadWrite** &lt;br&gt;&lt;br&gt; Default: **None for Standard storage. ReadOnly for Premium storage** |  [optional] |
|**diskSizeGB** | **Integer** | Specifies the size of empty data disks in gigabytes. This element can be used to overwrite the name of the disk in a virtual machine image. &lt;br&gt;&lt;br&gt; This value cannot be larger than 1023 GB |  [optional] |
|**managedDisk** | [**SubResource**](SubResource.md) |  |  [optional] |
|**osState** | [**OsStateEnum**](#OsStateEnum) | The OS State. |  |
|**osType** | [**OsTypeEnum**](#OsTypeEnum) | This property allows you to specify the type of the OS that is included in the disk if creating a VM from a custom image. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;&lt;br&gt; **Windows** &lt;br&gt;&lt;br&gt; **Linux** |  |
|**snapshot** | [**SubResource**](SubResource.md) |  |  [optional] |
|**storageAccountType** | **StorageAccountType** |  |  [optional] |



## Enum: CachingEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| READ_ONLY | &quot;ReadOnly&quot; |
| READ_WRITE | &quot;ReadWrite&quot; |



## Enum: OsStateEnum

| Name | Value |
|---- | -----|
| GENERALIZED | &quot;Generalized&quot; |
| SPECIALIZED | &quot;Specialized&quot; |



## Enum: OsTypeEnum

| Name | Value |
|---- | -----|
| WINDOWS | &quot;Windows&quot; |
| LINUX | &quot;Linux&quot; |



