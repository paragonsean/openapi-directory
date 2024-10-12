# NtropyTransactionApiV1.ClassifierApi

All URIs are relative to *https://api.ntropy.network*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getABatchOfBusinessTransactionClassificationResults**](ClassifierApi.md#getABatchOfBusinessTransactionClassificationResults) | **GET** /classifier/business/batch/{id} | Get a batch of business transaction classification results.
[**getABatchOfConsumerTransactionClassificationResults**](ClassifierApi.md#getABatchOfConsumerTransactionClassificationResults) | **GET** /classifier/consumer/batch/{id} | Get a batch of consumer transaction classification results.



## getABatchOfBusinessTransactionClassificationResults

> GetABatchOfBusinessTransactionClassificationResults200Response getABatchOfBusinessTransactionClassificationResults(id)

Get a batch of business transaction classification results.

Get a batch of business transaction classification results.

### Example

```javascript
import NtropyTransactionApiV1 from 'ntropy_transaction_api_v1';

let apiInstance = new NtropyTransactionApiV1.ClassifierApi();
let id = "247ee045-3d04-4b3c-872b-a9160b810f33"; // String | (Required) Batch id.
apiInstance.getABatchOfBusinessTransactionClassificationResults(id, (error, data, response) => {
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


## getABatchOfConsumerTransactionClassificationResults

> GetABatchOfConsumerTransactionClassificationResults200Response getABatchOfConsumerTransactionClassificationResults(id)

Get a batch of consumer transaction classification results.

Get a batch of consumer transaction classification results.

### Example

```javascript
import NtropyTransactionApiV1 from 'ntropy_transaction_api_v1';

let apiInstance = new NtropyTransactionApiV1.ClassifierApi();
let id = "247ee045-3d04-4b3c-872b-a9160b810f33"; // String | (Required) Batch id.
apiInstance.getABatchOfConsumerTransactionClassificationResults(id, (error, data, response) => {
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

