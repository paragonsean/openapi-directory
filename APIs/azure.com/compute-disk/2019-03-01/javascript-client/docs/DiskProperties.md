# DiskResourceProviderClient.DiskProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationData** | [**CreationData**](CreationData.md) |  | 
**diskIOPSReadWrite** | **Number** | The number of IOPS allowed for this disk; only settable for UltraSSD disks. One operation can transfer between 4k and 256k bytes. | [optional] 
**diskMBpsReadWrite** | **Number** | The bandwidth allowed for this disk; only settable for UltraSSD disks. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10. | [optional] 
**diskSizeBytes** | **Number** | The size of the disk in bytes. This field is read only. | [optional] [readonly] 
**diskSizeGB** | **Number** | If creationData.createOption is Empty, this field is mandatory and it indicates the size of the disk to create. If this field is present for updates or creation with other options, it indicates a resize. Resizes are only allowed if the disk is not attached to a running VM, and can only increase the disk&#39;s size. | [optional] 
**diskState** | **String** | The state of the disk. | [optional] [readonly] 
**encryptionSettingsCollection** | [**EncryptionSettingsCollection**](EncryptionSettingsCollection.md) |  | [optional] 
**hyperVGeneration** | **String** | The hypervisor generation of the Virtual Machine. Applicable to OS disks only. | [optional] 
**osType** | **String** | The Operating System type. | [optional] 
**provisioningState** | **String** | The disk provisioning state. | [optional] [readonly] 
**timeCreated** | **Date** | The time when the disk was created. | [optional] [readonly] 
**uniqueId** | **String** | Unique Guid identifying the resource. | [optional] [readonly] 



## Enum: DiskStateEnum


* `Unattached` (value: `"Unattached"`)

* `Attached` (value: `"Attached"`)

* `Reserved` (value: `"Reserved"`)

* `ActiveSAS` (value: `"ActiveSAS"`)

* `ReadyToUpload` (value: `"ReadyToUpload"`)

* `ActiveUpload` (value: `"ActiveUpload"`)





## Enum: HyperVGenerationEnum


* `V1` (value: `"V1"`)

* `V2` (value: `"V2"`)





## Enum: OsTypeEnum


* `Windows` (value: `"Windows"`)

* `Linux` (value: `"Linux"`)




