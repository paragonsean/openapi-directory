

# VolumeConfig

Configuration parameters for a new volume.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | A transient unique identifier to identify a volume within an ProvisioningConfig request. |  [optional] |
|**location** | **String** | Location where to deploy the volume. |  [optional] |
|**lunRanges** | [**List&lt;LunRange&gt;**](LunRange.md) | LUN ranges to be configured. Set only when protocol is PROTOCOL_FC. |  [optional] |
|**machineIds** | **List&lt;String&gt;** | Machine ids connected to this volume. Set only when protocol is PROTOCOL_FC. |  [optional] |
|**nfsExports** | [**List&lt;NfsExport&gt;**](NfsExport.md) | NFS exports. Set only when protocol is PROTOCOL_NFS. |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Volume protocol. |  [optional] |
|**sizeGb** | **Integer** | The requested size of this volume, in GB. This will be updated in a later iteration with a generic size field. |  [optional] |
|**snapshotsEnabled** | **Boolean** | Whether snapshots should be enabled. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of this Volume. |  [optional] |
|**userNote** | **String** | User note field, it can be used by customers to add additional information for the BMS Ops team (b/194021617). |  [optional] |



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



