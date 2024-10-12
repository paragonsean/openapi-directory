# UpdateAdminClient.UpdatesApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](UpdatesApi.md#operationsList) | **GET** /providers/Microsoft.Update.Admin/operations | 



## operationsList

> OperationList operationsList(apiVersion)



Get the list of support rest operations.

### Example

```javascript
import UpdateAdminClient from 'update_admin_client';
let defaultClient = UpdateAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new UpdateAdminClient.UpdatesApi();
let apiVersion = "'2016-05-01'"; // String | Client API Version.
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
 **apiVersion** | **String**| Client API Version. | [default to &#39;2016-05-01&#39;]

### Return type

[**OperationList**](OperationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

