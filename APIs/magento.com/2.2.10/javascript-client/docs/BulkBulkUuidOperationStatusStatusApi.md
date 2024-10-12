# MagentoB2B.BulkBulkUuidOperationStatusStatusApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asynchronousOperationsBulkStatusV1GetOperationsCountByBulkIdAndStatusGet**](BulkBulkUuidOperationStatusStatusApi.md#asynchronousOperationsBulkStatusV1GetOperationsCountByBulkIdAndStatusGet) | **GET** /V1/bulk/{bulkUuid}/operation-status/{status} | bulk/{bulkUuid}/operation-status/{status}



## asynchronousOperationsBulkStatusV1GetOperationsCountByBulkIdAndStatusGet

> Number asynchronousOperationsBulkStatusV1GetOperationsCountByBulkIdAndStatusGet(bulkUuid, status)

bulk/{bulkUuid}/operation-status/{status}

Get operations count by bulk uuid and status.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.BulkBulkUuidOperationStatusStatusApi();
let bulkUuid = "bulkUuid_example"; // String | 
let status = 56; // Number | 
apiInstance.asynchronousOperationsBulkStatusV1GetOperationsCountByBulkIdAndStatusGet(bulkUuid, status, (error, data, response) => {
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
 **status** | **Number**|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

