# AdvisorManagementClient.OperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](OperationsApi.md#operationsList) | **GET** /providers/Microsoft.Advisor/operations | 



## operationsList

> OperationEntityListResult operationsList(apiVersion)



Lists all the available Advisor REST API operations.

### Example

```javascript
import AdvisorManagementClient from 'advisor_management_client';
let defaultClient = AdvisorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdvisorManagementClient.OperationsApi();
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
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
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**OperationEntityListResult**](OperationEntityListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

