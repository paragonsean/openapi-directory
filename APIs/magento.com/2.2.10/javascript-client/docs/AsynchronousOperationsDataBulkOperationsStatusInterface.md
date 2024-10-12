# MagentoB2B.AsynchronousOperationsDataBulkOperationsStatusInterface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulkId** | **String** | Bulk uuid | 
**description** | **String** | Bulk description | 
**extensionAttributes** | **Object** | ExtensionInterface class for @see \\Magento\\AsynchronousOperations\\Api\\Data\\BulkSummaryInterface | [optional] 
**operationCount** | **Number** | Total number of operations scheduled in scope of this bulk | 
**operationsList** | [**[AsynchronousOperationsDataSummaryOperationStatusInterface]**](AsynchronousOperationsDataSummaryOperationStatusInterface.md) | List of operation with statuses (short data). | 
**startTime** | **String** | Bulk scheduled time | 
**userId** | **Number** | User id | 


