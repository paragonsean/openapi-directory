

# SnapshotProperties

Snapshot resource properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationData** | [**CreationData**](CreationData.md) |  |  |
|**diskSizeBytes** | **Long** | The size of the disk in bytes. This field is read only. |  [optional] [readonly] |
|**diskSizeGB** | **Integer** | If creationData.createOption is Empty, this field is mandatory and it indicates the size of the disk to create. If this field is present for updates or creation with other options, it indicates a resize. Resizes are only allowed if the disk is not attached to a running VM, and can only increase the disk&#39;s size. |  [optional] |
|**encryption** | [**Encryption**](Encryption.md) |  |  [optional] |
|**encryptionSettingsCollection** | [**EncryptionSettingsCollection**](EncryptionSettingsCollection.md) |  |  [optional] |
|**hyperVGeneration** | [**HyperVGenerationEnum**](#HyperVGenerationEnum) | The hypervisor generation of the Virtual Machine. Applicable to OS disks only. |  [optional] |
|**incremental** | **Boolean** | Whether a snapshot is incremental. Incremental snapshots on the same disk occupy less space than full snapshots and can be diffed. |  [optional] |
|**osType** | [**OsTypeEnum**](#OsTypeEnum) | The Operating System type. |  [optional] |
|**provisioningState** | **String** | The disk provisioning state. |  [optional] [readonly] |
|**timeCreated** | **OffsetDateTime** | The time when the disk was created. |  [optional] [readonly] |
|**uniqueId** | **String** | Unique Guid identifying the resource. |  [optional] [readonly] |



## Enum: HyperVGenerationEnum

| Name | Value |
|---- | -----|
| V1 | &quot;V1&quot; |
| V2 | &quot;V2&quot; |



## Enum: OsTypeEnum

| Name | Value |
|---- | -----|
| WINDOWS | &quot;Windows&quot; |
| LINUX | &quot;Linux&quot; |



