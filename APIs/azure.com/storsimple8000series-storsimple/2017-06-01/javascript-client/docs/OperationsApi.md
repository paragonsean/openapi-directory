# StorSimple8000SeriesManagementClient.OperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](OperationsApi.md#operationsList) | **GET** /providers/Microsoft.StorSimple/operations | 



## operationsList

> AvailableProviderOperationList operationsList(apiVersion)



Lists all of the available REST API operations of the Microsoft.StorSimple provider

### Example

```javascript
import StorSimple8000SeriesManagementClient from 'stor_simple8000_series_management_client';
let defaultClient = StorSimple8000SeriesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimple8000SeriesManagementClient.OperationsApi();
let apiVersion = "apiVersion_example"; // String | The api version
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
 **apiVersion** | **String**| The api version | 

### Return type

[**AvailableProviderOperationList**](AvailableProviderOperationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

