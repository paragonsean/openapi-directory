# Customproviders.OperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](OperationsApi.md#operationsList) | **GET** /providers/Microsoft.CustomProviders/operations | 



## operationsList

> ResourceProviderOperationList operationsList(apiVersion)



The list of operations provided by Microsoft CustomProviders.

### Example

```javascript
import Customproviders from 'customproviders';
let defaultClient = Customproviders.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Customproviders.OperationsApi();
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
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
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 

### Return type

[**ResourceProviderOperationList**](ResourceProviderOperationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

