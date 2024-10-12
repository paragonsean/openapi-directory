# DiskResourceProviderClient.DiskUpdateProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountType** | **String** | the storage account type of the disk. | [optional] 
**creationData** | [**CreationData**](CreationData.md) |  | [optional] 
**diskSizeGB** | **Number** | If creationData.createOption is Empty, this field is mandatory and it indicates the size of the VHD to create. If this field is present for updates or creation with other options, it indicates a resize. Resizes are only allowed if the disk is not attached to a running VM, and can only increase the disk&#39;s size. | [optional] 
**encryptionSettings** | [**EncryptionSettings**](EncryptionSettings.md) |  | [optional] 
**osType** | **String** | the Operating System type. | [optional] 



## Enum: AccountTypeEnum


* `Standard_LRS` (value: `"Standard_LRS"`)

* `Premium_LRS` (value: `"Premium_LRS"`)





## Enum: OsTypeEnum


* `Windows` (value: `"Windows"`)

* `Linux` (value: `"Linux"`)




