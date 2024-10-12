

# AsynchronousOperationsDataBulkOperationsStatusInterface

Interface BulkStatusInterface Bulk summary data with list of operations items summary data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bulkId** | **String** | Bulk uuid |  |
|**description** | **String** | Bulk description |  |
|**extensionAttributes** | **Object** | ExtensionInterface class for @see \\Magento\\AsynchronousOperations\\Api\\Data\\BulkSummaryInterface |  [optional] |
|**operationCount** | **Integer** | Total number of operations scheduled in scope of this bulk |  |
|**operationsList** | [**List&lt;AsynchronousOperationsDataSummaryOperationStatusInterface&gt;**](AsynchronousOperationsDataSummaryOperationStatusInterface.md) | List of operation with statuses (short data). |  |
|**startTime** | **String** | Bulk scheduled time |  |
|**userId** | **Integer** | User id |  |



