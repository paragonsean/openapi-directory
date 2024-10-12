# SiteRecoveryManagementClient.VMwareCbtProtectedDiskDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacityInBytes** | **Number** | The disk capacity in bytes. | [optional] [readonly] 
**diskId** | **String** | The disk id. | [optional] [readonly] 
**diskName** | **String** | The disk name. | [optional] [readonly] 
**diskPath** | **String** | The disk path. | [optional] [readonly] 
**diskType** | **String** | The disk type. | [optional] 
**isOSDisk** | **String** | A value indicating whether the disk is the OS disk. | [optional] [readonly] 
**logStorageAccountId** | **String** | The log storage account ARM Id. | [optional] [readonly] 
**logStorageAccountSasSecretName** | **String** | The key vault secret name of the log storage account. | [optional] [readonly] 
**seedManagedDiskId** | **String** | The ARM Id of the seed managed disk. | [optional] [readonly] 
**targetManagedDiskId** | **String** | The ARM Id of the target managed disk. | [optional] [readonly] 



## Enum: DiskTypeEnum


* `Standard_LRS` (value: `"Standard_LRS"`)

* `Premium_LRS` (value: `"Premium_LRS"`)

* `StandardSSD_LRS` (value: `"StandardSSD_LRS"`)




