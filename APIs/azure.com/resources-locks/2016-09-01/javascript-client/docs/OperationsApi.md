# ManagementLockClient.OperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorizationOperationsList**](OperationsApi.md#authorizationOperationsList) | **GET** /providers/Microsoft.Authorization/operations | 



## authorizationOperationsList

> OperationListResult authorizationOperationsList(apiVersion)



Lists all of the available Microsoft.Authorization REST API operations.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.OperationsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
apiInstance.authorizationOperationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the operation. | 

### Return type

[**OperationListResult**](OperationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

