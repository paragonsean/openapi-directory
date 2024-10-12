

# VirtualDisk

Virtual disk model

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**controllerId** | **String** | Disk&#39;s Controller id |  |
|**independenceMode** | [**IndependenceModeEnum**](#IndependenceModeEnum) | Disk&#39;s independence mode type |  |
|**totalSize** | **Integer** | Disk&#39;s total size |  |
|**virtualDiskId** | **String** | Disk&#39;s id |  [optional] |
|**virtualDiskName** | **String** | Disk&#39;s display name |  [optional] [readonly] |



## Enum: IndependenceModeEnum

| Name | Value |
|---- | -----|
| PERSISTENT | &quot;persistent&quot; |
| INDEPENDENT_PERSISTENT | &quot;independent_persistent&quot; |
| INDEPENDENT_NONPERSISTENT | &quot;independent_nonpersistent&quot; |



