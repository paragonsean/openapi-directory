# DataBoxManagementClient.CopyProgress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | Id of the account where the data needs to be uploaded. | [optional] [readonly] 
**bytesSentToCloud** | **Number** | Amount of data uploaded by the job as of now. | [optional] [readonly] 
**dataDestinationType** | **String** | Data Destination Type. | [optional] [readonly] 
**filesErroredOut** | **Number** | Number of files which could not be copied | [optional] [readonly] 
**filesProcessed** | **Number** | Number of files processed by the job as of now. | [optional] [readonly] 
**invalidFileBytesUploaded** | **Number** | Total amount of data not adhering to azure naming conventions which were processed by automatic renaming | [optional] [readonly] 
**invalidFilesProcessed** | **Number** | Number of files not adhering to azure naming conventions which were processed by automatic renaming | [optional] [readonly] 
**renamedContainerCount** | **Number** | Number of folders not adhering to azure naming conventions which were processed by automatic renaming | [optional] [readonly] 
**storageAccountName** | **String** | Name of the storage account where the data needs to be uploaded. | [optional] [readonly] 
**totalBytesToProcess** | **Number** | Total amount of data to be processed by the job. | [optional] [readonly] 
**totalFilesToProcess** | **Number** | Total number of files to be processed by the job. | [optional] [readonly] 



## Enum: DataDestinationTypeEnum


* `StorageAccount` (value: `"StorageAccount"`)

* `ManagedDisk` (value: `"ManagedDisk"`)




