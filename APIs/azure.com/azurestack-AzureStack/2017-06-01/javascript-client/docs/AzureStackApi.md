# AzureStackAzureBridgeClient.AzureStackApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](AzureStackApi.md#operationsList) | **GET** /providers/Microsoft.AzureStack/operations | 



## operationsList

> OperationList operationsList(apiVersion)



Returns the list of supported REST operations.

### Example

```javascript
import AzureStackAzureBridgeClient from 'azure_stack_azure_bridge_client';
let defaultClient = AzureStackAzureBridgeClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureStackAzureBridgeClient.AzureStackApi();
let apiVersion = "'2017-06-01'"; // String | Client API Version.
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
 **apiVersion** | **String**| Client API Version. | [default to &#39;2017-06-01&#39;]

### Return type

[**OperationList**](OperationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

