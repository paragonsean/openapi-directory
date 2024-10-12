# ApplicationClient.OperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listOperations**](OperationsApi.md#listOperations) | **GET** /providers/Microsoft.Solutions/operations | 



## listOperations

> OperationListResult listOperations(apiVersion)



Lists all of the available Microsoft.Solutions REST API operations.

### Example

```javascript
import ApplicationClient from 'application_client';
let defaultClient = ApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationClient.OperationsApi();
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
- **Accept**: application/json

