# HybridDataManagementClient.JobProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytesProcessed** | **Number** | Number of bytes processed by the job as of now. | [optional] 
**dataSinkName** | **String** | Name of the data sink on which the job was triggered. | [optional] 
**dataSourceName** | **String** | Name of the data source on which the job was triggered. | [optional] 
**details** | [**JobDetails**](JobDetails.md) |  | [optional] 
**isCancellable** | **String** | Describes whether the job is cancellable. | 
**itemsProcessed** | **Number** | Number of items processed by the job as of now | [optional] 
**totalBytesToProcess** | **Number** | Number of bytes to be processed by the job in total. | [optional] 
**totalItemsToProcess** | **Number** | Number of items to be processed by the job in total | [optional] 



## Enum: IsCancellableEnum


* `NotCancellable` (value: `"NotCancellable"`)

* `Cancellable` (value: `"Cancellable"`)




