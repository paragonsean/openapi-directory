# CloudTpuApi.AttachedDisk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **String** | The mode in which to attach this disk. If not specified, the default is READ_WRITE mode. Only applicable to data_disks. | [optional] 
**sourceDisk** | **String** | Specifies the full path to an existing disk. For example: \&quot;projects/my-project/zones/us-central1-c/disks/my-disk\&quot;. | [optional] 



## Enum: ModeEnum


* `DISK_MODE_UNSPECIFIED` (value: `"DISK_MODE_UNSPECIFIED"`)

* `READ_WRITE` (value: `"READ_WRITE"`)

* `READ_ONLY` (value: `"READ_ONLY"`)




