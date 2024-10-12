

# DiskProperties

Disk resource properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationData** | [**CreationData**](CreationData.md) |  |  |
|**diskIOPSReadWrite** | **Long** | The number of IOPS allowed for this disk; only settable for UltraSSD disks. One operation can transfer between 4k and 256k bytes. For a description of the range of values you can set, see [Ultra SSD Managed Disk Offerings](https://docs.microsoft.com/azure/virtual-machines/windows/disks-ultra-ssd#ultra-ssd-managed-disk-offerings). |  [optional] |
|**diskMBpsReadWrite** | **Integer** | The bandwidth allowed for this disk; only settable for UltraSSD disks. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10. For a description of the range of values you can set, see [Ultra SSD Managed Disk Offerings](https://docs.microsoft.com/azure/virtual-machines/windows/disks-ultra-ssd#ultra-ssd-managed-disk-offerings). |  [optional] |
|**diskSizeGB** | **Integer** | If creationData.createOption is Empty, this field is mandatory and it indicates the size of the VHD to create. If this field is present for updates or creation with other options, it indicates a resize. Resizes are only allowed if the disk is not attached to a running VM, and can only increase the disk&#39;s size. |  [optional] |
|**encryptionSettings** | [**EncryptionSettings**](EncryptionSettings.md) |  |  [optional] |
|**osType** | [**OsTypeEnum**](#OsTypeEnum) | The Operating System type. |  [optional] |
|**provisioningState** | **String** | The disk provisioning state. |  [optional] [readonly] |
|**timeCreated** | **OffsetDateTime** | The time when the disk was created. |  [optional] [readonly] |



## Enum: OsTypeEnum

| Name | Value |
|---- | -----|
| WINDOWS | &quot;Windows&quot; |
| LINUX | &quot;Linux&quot; |



