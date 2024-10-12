

# AttachNewDataDiskOptions

Properties to attach new disk to the Virtual Machine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**diskName** | **String** | The name of the disk to be attached. |  [optional] |
|**diskSizeGiB** | **Integer** | Size of the disk to be attached in GibiBytes. |  [optional] |
|**diskType** | [**DiskTypeEnum**](#DiskTypeEnum) | The storage type for the disk (i.e. Standard, Premium). |  [optional] |



## Enum: DiskTypeEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |
| STANDARD_SSD | &quot;StandardSSD&quot; |



