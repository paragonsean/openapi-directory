

# VolumePatchProperties

Patchable volume properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exportPolicy** | [**ExportPolicy**](ExportPolicy.md) |  |  [optional] |
|**serviceLevel** | [**ServiceLevelEnum**](#ServiceLevelEnum) | The service level of the file system |  [optional] |
|**usageThreshold** | **Long** | Maximum storage quota allowed for a file system in bytes. This is a soft quota used for alerting only. Minimum size is 100 GiB. Upper limit is 100TiB. Specified in bytes. |  [optional] |



## Enum: ServiceLevelEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |
| ULTRA | &quot;Ultra&quot; |



