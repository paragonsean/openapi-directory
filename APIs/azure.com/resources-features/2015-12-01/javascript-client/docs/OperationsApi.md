# FeatureClient.OperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listOperations**](OperationsApi.md#listOperations) | **GET** /providers/Microsoft.Features/operations | 



## listOperations

> OperationListResult listOperations(apiVersion)



Lists all of the available Microsoft.Features REST API operations.

### Example

```javascript
import FeatureClient from 'feature_client';
let defaultClient = FeatureClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FeatureClient.OperationsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.listOperations(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**OperationListResult**](OperationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

