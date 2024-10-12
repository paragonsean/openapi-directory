# AuthorizationManagementClient.ProviderOperationsMetadataApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**providerOperationsMetadataGet**](ProviderOperationsMetadataApi.md#providerOperationsMetadataGet) | **GET** /providers/Microsoft.Authorization/providerOperations/{resourceProviderNamespace} | 
[**providerOperationsMetadataList**](ProviderOperationsMetadataApi.md#providerOperationsMetadataList) | **GET** /providers/Microsoft.Authorization/providerOperations | 



## providerOperationsMetadataGet

> ProviderOperationsMetadata providerOperationsMetadataGet(resourceProviderNamespace, apiVersion, opts)



Gets provider operations metadata for the specified resource provider.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.ProviderOperationsMetadataApi();
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'expand': "'resourceTypes'" // String | Specifies whether to expand the values.
};
apiInstance.providerOperationsMetadataGet(resourceProviderNamespace, apiVersion, opts, (error, data, response) => {
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
 **resourceProviderNamespace** | **String**| The namespace of the resource provider. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **expand** | **String**| Specifies whether to expand the values. | [optional] [default to &#39;resourceTypes&#39;]

### Return type

[**ProviderOperationsMetadata**](ProviderOperationsMetadata.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## providerOperationsMetadataList

> ProviderOperationsMetadataListResult providerOperationsMetadataList(apiVersion, opts)



Gets provider operations metadata for all resource providers.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.ProviderOperationsMetadataApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'expand': "'resourceTypes'" // String | Specifies whether to expand the values.
};
apiInstance.providerOperationsMetadataList(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **expand** | **String**| Specifies whether to expand the values. | [optional] [default to &#39;resourceTypes&#39;]

### Return type

[**ProviderOperationsMetadataListResult**](ProviderOperationsMetadataListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

