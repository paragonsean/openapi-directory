

# VolumeConfig

Configuration parameters for a new volume.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gcpService** | **String** | The GCP service of the storage volume. Available gcp_service are in https://cloud.google.com/bare-metal/docs/bms-planning. |  [optional] |
|**id** | **String** | A transient unique identifier to identify a volume within an ProvisioningConfig request. |  [optional] |
|**lunRanges** | [**List&lt;LunRange&gt;**](LunRange.md) | LUN ranges to be configured. Set only when protocol is PROTOCOL_FC. |  [optional] |
|**machineIds** | **List&lt;String&gt;** | Machine ids connected to this volume. Set only when protocol is PROTOCOL_FC. |  [optional] |
|**name** | **String** | Output only. The name of the volume config. |  [optional] [readonly] |
|**nfsExports** | [**List&lt;NfsExport&gt;**](NfsExport.md) | NFS exports. Set only when protocol is PROTOCOL_NFS. |  [optional] |
|**performanceTier** | [**PerformanceTierEnum**](#PerformanceTierEnum) | Performance tier of the Volume. Default is SHARED. |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Volume protocol. |  [optional] |
|**sizeGb** | **Integer** | The requested size of this volume, in GB. |  [optional] |
|**snapshotsEnabled** | **Boolean** | Whether snapshots should be enabled. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of this Volume. |  [optional] |
|**userNote** | **String** | User note field, it can be used by customers to add additional information for the BMS Ops team . |  [optional] |



## Enum: PerformanceTierEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;VOLUME_PERFORMANCE_TIER_UNSPECIFIED&quot; |
| SHARED | &quot;VOLUME_PERFORMANCE_TIER_SHARED&quot; |
| ASSIGNED | &quot;VOLUME_PERFORMANCE_TIER_ASSIGNED&quot; |
| HT | &quot;VOLUME_PERFORMANCE_TIER_HT&quot; |
| QOS2_PERFORMANCE | &quot;VOLUME_PERFORMANCE_TIER_QOS2_PERFORMANCE&quot; |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PROTOCOL_UNSPECIFIED&quot; |
| FC | &quot;PROTOCOL_FC&quot; |
| NFS | &quot;PROTOCOL_NFS&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| FLASH | &quot;FLASH&quot; |
| DISK | &quot;DISK&quot; |



