# StorSimpleManagementClient.AvailableProviderOperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**availableProviderOperationsList**](AvailableProviderOperationsApi.md#availableProviderOperationsList) | **GET** /providers/Microsoft.StorSimple/operations | 



## availableProviderOperationsList

> AvailableProviderOperations availableProviderOperationsList(apiVersion)



List of AvailableProviderOperations

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.AvailableProviderOperationsApi();
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.availableProviderOperationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The api version | 

### Return type

[**AvailableProviderOperations**](AvailableProviderOperations.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

