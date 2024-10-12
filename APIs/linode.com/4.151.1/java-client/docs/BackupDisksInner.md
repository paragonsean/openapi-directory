

# BackupDisksInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filesystem** | [**FilesystemEnum**](#FilesystemEnum) | The Disk filesystem can be one of:    * raw - No filesystem, just a raw binary stream.   * swap - Linux swap area.   * ext3 - The ext3 journaling filesystem for Linux.   * ext4 - The ext4 journaling filesystem for Linux.   * initrd - initrd (uncompressed initrd, ext2, max 32 MB).  |  [optional] |
|**label** | **String** |  |  [optional] |
|**size** | **Integer** |  |  [optional] |



## Enum: FilesystemEnum

| Name | Value |
|---- | -----|
| RAW | &quot;raw&quot; |
| SWAP | &quot;swap&quot; |
| EXT3 | &quot;ext3&quot; |
| EXT4 | &quot;ext4&quot; |
| INITRD | &quot;initrd&quot; |



