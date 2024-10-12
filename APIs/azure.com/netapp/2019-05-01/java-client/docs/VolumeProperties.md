

# VolumeProperties

Volume properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baremetalTenantId** | **String** | Unique Baremetal Tenant Identifier. |  [optional] [readonly] |
|**creationToken** | **String** | A unique file path for the volume. Used when creating mount targets |  |
|**exportPolicy** | [**ExportPolicy**](ExportPolicy.md) |  |  [optional] |
|**fileSystemId** | **String** | Unique FileSystem Identifier. |  [optional] [readonly] |
|**mountTargets** | **Object** | List of mount targets |  [optional] |
|**protocolTypes** | **List&lt;String&gt;** | Set of protocol types |  [optional] |
|**provisioningState** | **String** | Azure lifecycle management |  [optional] [readonly] |
|**serviceLevel** | [**ServiceLevelEnum**](#ServiceLevelEnum) | The service level of the file system |  [optional] |
|**snapshotId** | **String** | UUID v4 used to identify the Snapshot |  [optional] |
|**subnetId** | **String** | The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/volumes |  |
|**usageThreshold** | **Long** | Maximum storage quota allowed for a file system in bytes. This is a soft quota used for alerting only. Minimum size is 100 GiB. Upper limit is 100TiB. Specified in bytes. |  |



## Enum: ServiceLevelEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |
| ULTRA | &quot;Ultra&quot; |



