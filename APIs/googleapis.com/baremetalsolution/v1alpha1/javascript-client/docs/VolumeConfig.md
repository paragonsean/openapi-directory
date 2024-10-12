# BareMetalSolutionApi.VolumeConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | A transient unique identifier to identify a volume within an ProvisioningConfig request. | [optional] 
**location** | **String** | Location where to deploy the volume. | [optional] 
**lunRanges** | [**[LunRange]**](LunRange.md) | LUN ranges to be configured. Set only when protocol is PROTOCOL_FC. | [optional] 
**machineIds** | **[String]** | Machine ids connected to this volume. Set only when protocol is PROTOCOL_FC. | [optional] 
**nfsExports** | [**[NfsExport]**](NfsExport.md) | NFS exports. Set only when protocol is PROTOCOL_NFS. | [optional] 
**protocol** | **String** | Volume protocol. | [optional] 
**sizeGb** | **Number** | The requested size of this volume, in GB. This will be updated in a later iteration with a generic size field. | [optional] 
**snapshotsEnabled** | **Boolean** | Whether snapshots should be enabled. | [optional] 
**type** | **String** | The type of this Volume. | [optional] 
**userNote** | **String** | User note field, it can be used by customers to add additional information for the BMS Ops team (b/194021617). | [optional] 



## Enum: ProtocolEnum


* `UNSPECIFIED` (value: `"PROTOCOL_UNSPECIFIED"`)

* `FC` (value: `"PROTOCOL_FC"`)

* `NFS` (value: `"PROTOCOL_NFS"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `FLASH` (value: `"FLASH"`)

* `DISK` (value: `"DISK"`)




