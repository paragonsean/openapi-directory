# ApiManagementClient.ApiManagementOperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiManagementOperationsList**](ApiManagementOperationsApi.md#apiManagementOperationsList) | **GET** /providers/Microsoft.ApiManagement/operations | 



## apiManagementOperationsList

> OperationListResult apiManagementOperationsList(apiVersion)



Lists all of the available REST API operations of the Microsoft.ApiManagement provider.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.ApiManagementOperationsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.apiManagementOperationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**OperationListResult**](OperationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

