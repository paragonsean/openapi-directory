# QnAMakerClient.OperationsApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsGetDetails**](OperationsApi.md#operationsGetDetails) | **GET** /operations/{operationId} | Gets details of a specific long running operation.



## operationsGetDetails

> Operation operationsGetDetails(operationId)

Gets details of a specific long running operation.

### Example

```javascript
import QnAMakerClient from 'qn_a_maker_client';
let defaultClient = QnAMakerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new QnAMakerClient.OperationsApi();
let operationId = "operationId_example"; // String | Operation id.
apiInstance.operationsGetDetails(operationId, (error, data, response) => {
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
 **operationId** | **String**| Operation id. | 

### Return type

[**Operation**](Operation.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

