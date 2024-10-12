# AzureBridgeAdminClient.AzureBridgeApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](AzureBridgeApi.md#operationsList) | **GET** /providers/Microsoft.AzureBridge.Admin/operations | 



## operationsList

> OperationList operationsList(apiVersion)



Returns the list of support REST operations.

### Example

```javascript
import AzureBridgeAdminClient from 'azure_bridge_admin_client';
let defaultClient = AzureBridgeAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureBridgeAdminClient.AzureBridgeApi();
let apiVersion = "'2016-01-01'"; // String | Client Api Version.
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
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2016-01-01&#39;]

### Return type

[**OperationList**](OperationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

