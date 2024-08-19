

# SnapshotUpdateProperties

Snapshot resource update properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**diskSizeGB** | **Integer** | If creationData.createOption is Empty, this field is mandatory and it indicates the size of the disk to create. If this field is present for updates or creation with other options, it indicates a resize. Resizes are only allowed if the disk is not attached to a running VM, and can only increase the disk&#39;s size. |  [optional] |
|**encryptionSettingsCollection** | [**EncryptionSettingsCollection**](EncryptionSettingsCollection.md) |  |  [optional] |
|**osType** | [**OsTypeEnum**](#OsTypeEnum) | the Operating System type. |  [optional] |



## Enum: OsTypeEnum

| Name | Value |
|---- | -----|
| WINDOWS | &quot;Windows&quot; |
| LINUX | &quot;Linux&quot; |



