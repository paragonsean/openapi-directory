# NtropyTransactionApiV1.Batch1Api

All URIs are relative to *https://api.ntropy.network*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getABatchOfBusinessTransactionClassificationResults_1**](Batch1Api.md#getABatchOfBusinessTransactionClassificationResults_1) | **GET** /classifier/business/batch/{id} | Get a batch of business transaction classification results.



## getABatchOfBusinessTransactionClassificationResults_1

> GetABatchOfBusinessTransactionClassificationResults200Response getABatchOfBusinessTransactionClassificationResults_1(id)

Get a batch of business transaction classification results.

Get a batch of business transaction classification results.

### Example

```javascript
import NtropyTransactionApiV1 from 'ntropy_transaction_api_v1';

let apiInstance = new NtropyTransactionApiV1.Batch1Api();
let id = "247ee045-3d04-4b3c-872b-a9160b810f33"; // String | (Required) Batch id.
apiInstance.getABatchOfBusinessTransactionClassificationResults_1(id, (error, data, response) => {
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
 **id** | **String**| (Required) Batch id. | 

### Return type

[**GetABatchOfBusinessTransactionClassificationResults200Response**](GetABatchOfBusinessTransactionClassificationResults200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain

