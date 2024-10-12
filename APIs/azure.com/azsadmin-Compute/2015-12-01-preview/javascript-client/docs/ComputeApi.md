# ComputeAdminClient.ComputeApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](ComputeApi.md#operationsList) | **GET** /providers/Microsoft.Compute.Admin/operations | 



## operationsList

> OperationList operationsList(apiVersion)



Returns the list of supported REST operations.

### Example

```javascript
import ComputeAdminClient from 'compute_admin_client';
let defaultClient = ComputeAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeAdminClient.ComputeApi();
let apiVersion = "'2015-12-01-preview'"; // String | Client API Version.
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
 **apiVersion** | **String**| Client API Version. | [default to &#39;2015-12-01-preview&#39;]

### Return type

[**OperationList**](OperationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

