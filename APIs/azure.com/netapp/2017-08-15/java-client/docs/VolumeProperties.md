

# VolumeProperties

Volume properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationToken** | **String** | A unique file path for the volume. Used when creating mount targets |  |
|**exportPolicy** | [**VolumePatchPropertiesExportPolicy**](VolumePatchPropertiesExportPolicy.md) |  |  [optional] |
|**fileSystemId** | **String** | Unique FileSystem Identifier. |  [optional] [readonly] |
|**provisioningState** | **String** | Azure lifecycle management |  [optional] [readonly] |
|**serviceLevel** | [**ServiceLevelEnum**](#ServiceLevelEnum) | The service level of the file system |  |
|**subnetId** | **String** | The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/volumes |  [optional] |
|**usageThreshold** | **Long** | Maximum storage quota allowed for a file system in bytes. This is a soft quota used for alerting only. Minimum size is 100 GiB. Upper limit is 100TiB. |  [optional] |



## Enum: ServiceLevelEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |
| ULTRA | &quot;Ultra&quot; |



