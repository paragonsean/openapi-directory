

# Disk


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **OffsetDateTime** | When this Disk was created. |  [optional] [readonly] |
|**filesystem** | [**FilesystemEnum**](#FilesystemEnum) | The Disk filesystem can be one of:    * raw - No filesystem, just a raw binary stream.   * swap - Linux swap area.   * ext3 - The ext3 journaling filesystem for Linux.   * ext4 - The ext4 journaling filesystem for Linux.   * initrd - initrd (uncompressed initrd, ext2, max 32 MB).  |  [optional] |
|**id** | **Integer** | This Disk&#39;s ID which must be provided for all operations impacting this Disk.  |  [optional] [readonly] |
|**label** | **String** | The Disk&#39;s label is for display purposes only.  |  [optional] |
|**size** | **Integer** | The size of the Disk in MB. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | A brief description of this Disk&#39;s current state. This field may change without direct action from you, as a result of operations performed to the Disk or the Linode containing the Disk.  |  [optional] [readonly] |
|**updated** | **OffsetDateTime** | When this Disk was last updated. |  [optional] [readonly] |



## Enum: FilesystemEnum

| Name | Value |
|---- | -----|
| RAW | &quot;raw&quot; |
| SWAP | &quot;swap&quot; |
| EXT3 | &quot;ext3&quot; |
| EXT4 | &quot;ext4&quot; |
| INITRD | &quot;initrd&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| READY | &quot;ready&quot; |
| NOT_READY | &quot;not ready&quot; |
| DELETING | &quot;deleting&quot; |



