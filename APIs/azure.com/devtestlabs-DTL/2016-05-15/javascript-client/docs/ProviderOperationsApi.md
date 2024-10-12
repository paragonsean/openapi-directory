# DevTestLabsClient.ProviderOperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**providerOperationsList**](ProviderOperationsApi.md#providerOperationsList) | **GET** /providers/Microsoft.DevTestLab/operations | 



## providerOperationsList

> ProviderOperationResult providerOperationsList(apiVersion)



Result of the request to list REST API operations

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ProviderOperationsApi();
let apiVersion = "'2016-05-15'"; // String | Client API version.
apiInstance.providerOperationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2016-05-15&#39;]

### Return type

[**ProviderOperationResult**](ProviderOperationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

