# MicrosoftNetApp.VolumeProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baremetalTenantId** | **String** | Unique Baremetal Tenant Identifier. | [optional] [readonly] 
**creationToken** | **String** | A unique file path for the volume. Used when creating mount targets | 
**dataProtection** | [**DataProtection**](DataProtection.md) |  | [optional] 
**exportPolicy** | [**ExportPolicy**](ExportPolicy.md) |  | [optional] 
**fileSystemId** | **String** | Unique FileSystem Identifier. | [optional] [readonly] 
**isRestoring** | **Boolean** | Restoring | [optional] 
**mountTargets** | [**[MountTargetList]**](MountTargetList.md) | List of mount targets | [optional] 
**protocolTypes** | **[String]** | Set of protocol types | [optional] 
**provisioningState** | **String** | Azure lifecycle management | [optional] [readonly] 
**serviceLevel** | **String** | The service level of the file system | [optional] [default to &#39;Premium&#39;]
**snapshotId** | **String** | UUID v4 or resource identifier used to identify the Snapshot. | [optional] 
**subnetId** | **String** | The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/volumes | 
**usageThreshold** | **Number** | Maximum storage quota allowed for a file system in bytes. This is a soft quota used for alerting only. Minimum size is 100 GiB. Upper limit is 100TiB. Specified in bytes. | [default to 107374182400]
**volumeType** | **String** | What type of volume is this | [optional] 



## Enum: ServiceLevelEnum


* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)

* `Ultra` (value: `"Ultra"`)




