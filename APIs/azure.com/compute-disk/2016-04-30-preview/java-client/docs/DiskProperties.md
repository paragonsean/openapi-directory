

# DiskProperties

Disk resource properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountType** | [**AccountTypeEnum**](#AccountTypeEnum) | the storage account type of the disk. |  [optional] |
|**creationData** | [**CreationData**](CreationData.md) |  |  |
|**diskSizeGB** | **Integer** | If creationData.createOption is Empty, this field is mandatory and it indicates the size of the VHD to create. If this field is present for updates or creation with other options, it indicates a resize. Resizes are only allowed if the disk is not attached to a running VM, and can only increase the disk&#39;s size. |  [optional] |
|**encryptionSettings** | [**EncryptionSettings**](EncryptionSettings.md) |  |  [optional] |
|**osType** | [**OsTypeEnum**](#OsTypeEnum) | The Operating System type. |  [optional] |
|**ownerId** | **String** | A relative URI containing the VM id that has the disk attached. |  [optional] [readonly] |
|**provisioningState** | **String** | The disk provisioning state. |  [optional] [readonly] |
|**timeCreated** | **OffsetDateTime** | The time when the disk was created. |  [optional] [readonly] |



## Enum: AccountTypeEnum

| Name | Value |
|---- | -----|
| STANDARD_LRS | &quot;Standard_LRS&quot; |
| PREMIUM_LRS | &quot;Premium_LRS&quot; |



## Enum: OsTypeEnum

| Name | Value |
|---- | -----|
| WINDOWS | &quot;Windows&quot; |
| LINUX | &quot;Linux&quot; |



