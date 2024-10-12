# DiskResourceProviderClient.SnapshotUpdateProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diskSizeGB** | **Number** | If creationData.createOption is Empty, this field is mandatory and it indicates the size of the VHD to create. If this field is present for updates or creation with other options, it indicates a resize. Resizes are only allowed if the disk is not attached to a running VM, and can only increase the disk&#39;s size. | [optional] 
**encryptionSettings** | [**EncryptionSettings**](EncryptionSettings.md) |  | [optional] 
**osType** | **String** | the Operating System type. | [optional] 



## Enum: OsTypeEnum


* `Windows` (value: `"Windows"`)

* `Linux` (value: `"Linux"`)




