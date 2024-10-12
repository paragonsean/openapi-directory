# DataShareManagementClient.OperationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](OperationApi.md#operationsList) | **GET** /providers/Microsoft.DataShare/operations | Lists the available operations



## operationsList

> OperationList operationsList(apiVersion)

Lists the available operations

List of available operations

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.OperationApi();
let apiVersion = "apiVersion_example"; // String | The api version to use.
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
 **apiVersion** | **String**| The api version to use. | 

### Return type

[**OperationList**](OperationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

