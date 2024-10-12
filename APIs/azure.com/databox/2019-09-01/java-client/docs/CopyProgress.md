

# CopyProgress

Copy progress.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Id of the account where the data needs to be uploaded. |  [optional] [readonly] |
|**bytesSentToCloud** | **Long** | Amount of data uploaded by the job as of now. |  [optional] [readonly] |
|**dataDestinationType** | [**DataDestinationTypeEnum**](#DataDestinationTypeEnum) | Data Destination Type. |  [optional] [readonly] |
|**filesErroredOut** | **Long** | Number of files which could not be copied |  [optional] [readonly] |
|**filesProcessed** | **Long** | Number of files processed by the job as of now. |  [optional] [readonly] |
|**invalidFileBytesUploaded** | **Long** | Total amount of data not adhering to azure naming conventions which were processed by automatic renaming |  [optional] [readonly] |
|**invalidFilesProcessed** | **Long** | Number of files not adhering to azure naming conventions which were processed by automatic renaming |  [optional] [readonly] |
|**renamedContainerCount** | **Long** | Number of folders not adhering to azure naming conventions which were processed by automatic renaming |  [optional] [readonly] |
|**storageAccountName** | **String** | Name of the storage account where the data needs to be uploaded. |  [optional] [readonly] |
|**totalBytesToProcess** | **Long** | Total amount of data to be processed by the job. |  [optional] [readonly] |
|**totalFilesToProcess** | **Long** | Total number of files to be processed by the job. |  [optional] [readonly] |



## Enum: DataDestinationTypeEnum

| Name | Value |
|---- | -----|
| STORAGE_ACCOUNT | &quot;StorageAccount&quot; |
| MANAGED_DISK | &quot;ManagedDisk&quot; |



