

# AttachedDisk

A node-attached disk resource. Next ID: 8;

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mode** | [**ModeEnum**](#ModeEnum) | The mode in which to attach this disk. If not specified, the default is READ_WRITE mode. Only applicable to data_disks. |  [optional] |
|**sourceDisk** | **String** | Specifies the full path to an existing disk. For example: \&quot;projects/my-project/zones/us-central1-c/disks/my-disk\&quot;. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| DISK_MODE_UNSPECIFIED | &quot;DISK_MODE_UNSPECIFIED&quot; |
| READ_WRITE | &quot;READ_WRITE&quot; |
| READ_ONLY | &quot;READ_ONLY&quot; |



