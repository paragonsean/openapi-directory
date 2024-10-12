

# DataDiskProperties

Request body for adding a new or existing data disk to a virtual machine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attachNewDataDiskOptions** | [**AttachNewDataDiskOptions**](AttachNewDataDiskOptions.md) |  |  [optional] |
|**existingLabDiskId** | **String** | Specifies the existing lab disk id to attach to virtual machine. |  [optional] |
|**hostCaching** | [**HostCachingEnum**](#HostCachingEnum) | Caching option for a data disk (i.e. None, ReadOnly, ReadWrite). |  [optional] |



## Enum: HostCachingEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| READ_ONLY | &quot;ReadOnly&quot; |
| READ_WRITE | &quot;ReadWrite&quot; |



