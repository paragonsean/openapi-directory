

# JobProperties

Job Properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bytesProcessed** | **Long** | Number of bytes processed by the job as of now. |  [optional] |
|**dataSinkName** | **String** | Name of the data sink on which the job was triggered. |  [optional] |
|**dataSourceName** | **String** | Name of the data source on which the job was triggered. |  [optional] |
|**details** | [**JobDetails**](JobDetails.md) |  |  [optional] |
|**isCancellable** | [**IsCancellableEnum**](#IsCancellableEnum) | Describes whether the job is cancellable. |  |
|**itemsProcessed** | **Long** | Number of items processed by the job as of now |  [optional] |
|**totalBytesToProcess** | **Long** | Number of bytes to be processed by the job in total. |  [optional] |
|**totalItemsToProcess** | **Long** | Number of items to be processed by the job in total |  [optional] |



## Enum: IsCancellableEnum

| Name | Value |
|---- | -----|
| NOT_CANCELLABLE | &quot;NotCancellable&quot; |
| CANCELLABLE | &quot;Cancellable&quot; |



