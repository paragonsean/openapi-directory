# MagentoB2B.BulkBulkUuidStatusApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asynchronousOperationsBulkStatusV1GetBulkShortStatusGet**](BulkBulkUuidStatusApi.md#asynchronousOperationsBulkStatusV1GetBulkShortStatusGet) | **GET** /V1/bulk/{bulkUuid}/status | bulk/{bulkUuid}/status



## asynchronousOperationsBulkStatusV1GetBulkShortStatusGet

> AsynchronousOperationsDataBulkOperationsStatusInterface asynchronousOperationsBulkStatusV1GetBulkShortStatusGet(bulkUuid)

bulk/{bulkUuid}/status

Get Bulk summary data with list of operations items short data.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.BulkBulkUuidStatusApi();
let bulkUuid = "bulkUuid_example"; // String | 
apiInstance.asynchronousOperationsBulkStatusV1GetBulkShortStatusGet(bulkUuid, (error, data, response) => {
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

[**AsynchronousOperationsDataBulkOperationsStatusInterface**](AsynchronousOperationsDataBulkOperationsStatusInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

