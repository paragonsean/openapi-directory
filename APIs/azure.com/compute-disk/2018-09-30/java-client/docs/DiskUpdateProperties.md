

# DiskUpdateProperties

Disk resource update properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**diskIOPSReadWrite** | **Long** | The number of IOPS allowed for this disk; only settable for UltraSSD disks. One operation can transfer between 4k and 256k bytes. |  [optional] |
|**diskMBpsReadWrite** | **Integer** | The bandwidth allowed for this disk; only settable for UltraSSD disks. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10. |  [optional] |
|**diskSizeGB** | **Integer** | If creationData.createOption is Empty, this field is mandatory and it indicates the size of the VHD to create. If this field is present for updates or creation with other options, it indicates a resize. Resizes are only allowed if the disk is not attached to a running VM, and can only increase the disk&#39;s size. |  [optional] |
|**encryptionSettingsCollection** | [**EncryptionSettingsCollection**](EncryptionSettingsCollection.md) |  |  [optional] |
|**osType** | [**OsTypeEnum**](#OsTypeEnum) | the Operating System type. |  [optional] |



## Enum: OsTypeEnum

| Name | Value |
|---- | -----|
| WINDOWS | &quot;Windows&quot; |
| LINUX | &quot;Linux&quot; |



