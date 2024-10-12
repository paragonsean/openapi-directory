# VisualStudioResourceProviderClient.OperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](OperationsApi.md#operationsList) | **GET** /providers/microsoft.visualstudio/operations | Operations_List



## operationsList

> OperationListResult operationsList()

Operations_List

Gets the details of all operations possible on the Microsoft.VisualStudio resource provider.

### Example

```javascript
import VisualStudioResourceProviderClient from 'visual_studio_resource_provider_client';
let defaultClient = VisualStudioResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VisualStudioResourceProviderClient.OperationsApi();
apiInstance.operationsList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**OperationListResult**](OperationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

