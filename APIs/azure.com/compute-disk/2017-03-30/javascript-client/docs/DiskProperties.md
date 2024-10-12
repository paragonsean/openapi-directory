# DiskResourceProviderClient.DiskProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationData** | [**CreationData**](CreationData.md) |  | 
**diskSizeGB** | **Number** | If creationData.createOption is Empty, this field is mandatory and it indicates the size of the VHD to create. If this field is present for updates or creation with other options, it indicates a resize. Resizes are only allowed if the disk is not attached to a running VM, and can only increase the disk&#39;s size. | [optional] 
**encryptionSettings** | [**EncryptionSettings**](EncryptionSettings.md) |  | [optional] 
**osType** | **String** | The Operating System type. | [optional] 
**provisioningState** | **String** | The disk provisioning state. | [optional] [readonly] 
**timeCreated** | **Date** | The time when the disk was created. | [optional] [readonly] 



## Enum: OsTypeEnum


* `Windows` (value: `"Windows"`)

* `Linux` (value: `"Linux"`)




