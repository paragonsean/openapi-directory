# HybridDataManagementClient.OperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](OperationsApi.md#operationsList) | **GET** /providers/Microsoft.HybridData/operations | This method gets all the operations.



## operationsList

> AvailableProviderOperations operationsList(apiVersion)

This method gets all the operations.

### Example

```javascript
import HybridDataManagementClient from 'hybrid_data_management_client';
let defaultClient = HybridDataManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HybridDataManagementClient.OperationsApi();
let apiVersion = "apiVersion_example"; // String | The API Version
apiInstance.operationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The API Version | 

### Return type

[**AvailableProviderOperations**](AvailableProviderOperations.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

