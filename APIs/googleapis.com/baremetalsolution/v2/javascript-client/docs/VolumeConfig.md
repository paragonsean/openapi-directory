# BareMetalSolutionApi.VolumeConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcpService** | **String** | The GCP service of the storage volume. Available gcp_service are in https://cloud.google.com/bare-metal/docs/bms-planning. | [optional] 
**id** | **String** | A transient unique identifier to identify a volume within an ProvisioningConfig request. | [optional] 
**lunRanges** | [**[LunRange]**](LunRange.md) | LUN ranges to be configured. Set only when protocol is PROTOCOL_FC. | [optional] 
**machineIds** | **[String]** | Machine ids connected to this volume. Set only when protocol is PROTOCOL_FC. | [optional] 
**name** | **String** | Output only. The name of the volume config. | [optional] [readonly] 
**nfsExports** | [**[NfsExport]**](NfsExport.md) | NFS exports. Set only when protocol is PROTOCOL_NFS. | [optional] 
**performanceTier** | **String** | Performance tier of the Volume. Default is SHARED. | [optional] 
**protocol** | **String** | Volume protocol. | [optional] 
**sizeGb** | **Number** | The requested size of this volume, in GB. | [optional] 
**snapshotsEnabled** | **Boolean** | Whether snapshots should be enabled. | [optional] 
**type** | **String** | The type of this Volume. | [optional] 
**userNote** | **String** | User note field, it can be used by customers to add additional information for the BMS Ops team . | [optional] 



## Enum: PerformanceTierEnum


* `UNSPECIFIED` (value: `"VOLUME_PERFORMANCE_TIER_UNSPECIFIED"`)

* `SHARED` (value: `"VOLUME_PERFORMANCE_TIER_SHARED"`)

* `ASSIGNED` (value: `"VOLUME_PERFORMANCE_TIER_ASSIGNED"`)

* `HT` (value: `"VOLUME_PERFORMANCE_TIER_HT"`)

* `QOS2_PERFORMANCE` (value: `"VOLUME_PERFORMANCE_TIER_QOS2_PERFORMANCE"`)





## Enum: ProtocolEnum


* `UNSPECIFIED` (value: `"PROTOCOL_UNSPECIFIED"`)

* `FC` (value: `"PROTOCOL_FC"`)

* `NFS` (value: `"PROTOCOL_NFS"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `FLASH` (value: `"FLASH"`)

* `DISK` (value: `"DISK"`)




