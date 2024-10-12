# MagentoB2B.BulkBulkUuidDetailedStatusApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asynchronousOperationsBulkStatusV1GetBulkDetailedStatusGet**](BulkBulkUuidDetailedStatusApi.md#asynchronousOperationsBulkStatusV1GetBulkDetailedStatusGet) | **GET** /V1/bulk/{bulkUuid}/detailed-status | bulk/{bulkUuid}/detailed-status



## asynchronousOperationsBulkStatusV1GetBulkDetailedStatusGet

> AsynchronousOperationsDataDetailedBulkOperationsStatusInterface asynchronousOperationsBulkStatusV1GetBulkDetailedStatusGet(bulkUuid)

bulk/{bulkUuid}/detailed-status

Get Bulk summary data with list of operations items full data.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.BulkBulkUuidDetailedStatusApi();
let bulkUuid = "bulkUuid_example"; // String | 
apiInstance.asynchronousOperationsBulkStatusV1GetBulkDetailedStatusGet(bulkUuid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulkUuid** | **String**|  | 

### Return type

[**AsynchronousOperationsDataDetailedBulkOperationsStatusInterface**](AsynchronousOperationsDataDetailedBulkOperationsStatusInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

