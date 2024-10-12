# LinodeApi.BackupDisksInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filesystem** | **String** | The Disk filesystem can be one of:    * raw - No filesystem, just a raw binary stream.   * swap - Linux swap area.   * ext3 - The ext3 journaling filesystem for Linux.   * ext4 - The ext4 journaling filesystem for Linux.   * initrd - initrd (uncompressed initrd, ext2, max 32 MB).  | [optional] 
**label** | **String** |  | [optional] 
**size** | **Number** |  | [optional] 



## Enum: FilesystemEnum


* `raw` (value: `"raw"`)

* `swap` (value: `"swap"`)

* `ext3` (value: `"ext3"`)

* `ext4` (value: `"ext4"`)

* `initrd` (value: `"initrd"`)




