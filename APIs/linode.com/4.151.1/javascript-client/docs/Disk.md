# LinodeApi.Disk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Date** | When this Disk was created. | [optional] [readonly] 
**filesystem** | **String** | The Disk filesystem can be one of:    * raw - No filesystem, just a raw binary stream.   * swap - Linux swap area.   * ext3 - The ext3 journaling filesystem for Linux.   * ext4 - The ext4 journaling filesystem for Linux.   * initrd - initrd (uncompressed initrd, ext2, max 32 MB).  | [optional] 
**id** | **Number** | This Disk&#39;s ID which must be provided for all operations impacting this Disk.  | [optional] [readonly] 
**label** | **String** | The Disk&#39;s label is for display purposes only.  | [optional] 
**size** | **Number** | The size of the Disk in MB. | [optional] 
**status** | **String** | A brief description of this Disk&#39;s current state. This field may change without direct action from you, as a result of operations performed to the Disk or the Linode containing the Disk.  | [optional] [readonly] 
**updated** | **Date** | When this Disk was last updated. | [optional] [readonly] 



## Enum: FilesystemEnum


* `raw` (value: `"raw"`)

* `swap` (value: `"swap"`)

* `ext3` (value: `"ext3"`)

* `ext4` (value: `"ext4"`)

* `initrd` (value: `"initrd"`)





## Enum: StatusEnum


* `ready` (value: `"ready"`)

* `not ready` (value: `"not ready"`)

* `deleting` (value: `"deleting"`)




