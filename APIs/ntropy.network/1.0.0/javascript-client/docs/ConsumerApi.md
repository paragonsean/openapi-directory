# NtropyTransactionApiV1.ConsumerApi

All URIs are relative to *https://api.ntropy.network*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getABatchOfConsumerTransactionClassificationResults_0**](ConsumerApi.md#getABatchOfConsumerTransactionClassificationResults_0) | **GET** /classifier/consumer/batch/{id} | Get a batch of consumer transaction classification results.



## getABatchOfConsumerTransactionClassificationResults_0

> GetABatchOfConsumerTransactionClassificationResults200Response getABatchOfConsumerTransactionClassificationResults_0(id)

Get a batch of consumer transaction classification results.

Get a batch of consumer transaction classification results.

### Example

```javascript
import NtropyTransactionApiV1 from 'ntropy_transaction_api_v1';

let apiInstance = new NtropyTransactionApiV1.ConsumerApi();
let id = "247ee045-3d04-4b3c-872b-a9160b810f33"; // String | (Required) Batch id.
apiInstance.getABatchOfConsumerTransactionClassificationResults_0(id, (error, data, response) => {
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

[**GetABatchOfConsumerTransactionClassificationResults200Response**](GetABatchOfConsumerTransactionClassificationResults200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain

