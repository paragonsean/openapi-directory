# RecoveryServicesBackupClient.AzureStorageJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionsInfo** | **[String]** | Gets or sets the state/actions applicable on this job like cancel/retry. | [optional] 
**duration** | **String** | Time elapsed during the execution of this job. | [optional] 
**errorDetails** | [**[AzureStorageErrorInfo]**](AzureStorageErrorInfo.md) | Error details on execution of this job. | [optional] 
**extendedInfo** | [**AzureStorageJobExtendedInfo**](AzureStorageJobExtendedInfo.md) |  | [optional] 
**storageAccountName** | **String** | Specifies friendly name of the storage account. | [optional] 
**storageAccountVersion** | **String** | Specifies whether the Storage account is a Classic or an Azure Resource Manager Storage account. | [optional] 



## Enum: [ActionsInfoEnum]


* `Invalid` (value: `"Invalid"`)

* `Cancellable` (value: `"Cancellable"`)

* `Retriable` (value: `"Retriable"`)




