# AuthorizationManagementClient.ElevateAccessApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**elevateAccessPost**](ElevateAccessApi.md#elevateAccessPost) | **POST** /providers/Microsoft.Authorization/elevateAccess | 



## elevateAccessPost

> elevateAccessPost(apiVersion)



Elevates access for a Global Administrator.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.ElevateAccessApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.elevateAccessPost(apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

