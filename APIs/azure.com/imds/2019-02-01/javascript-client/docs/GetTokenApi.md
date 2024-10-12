# InstanceMetadataClient.GetTokenApi

All URIs are relative to *https://169.254.169.254/metadata*

Method | HTTP request | Description
------------- | ------------- | -------------
[**identityGetToken**](GetTokenApi.md#identityGetToken) | **GET** /identity/oauth2/token | 



## identityGetToken

> IdentityTokenResponse identityGetToken(metadata, resource, apiVersion, opts)



Get a Token from Azure AD

### Example

```javascript
import InstanceMetadataClient from 'instance_metadata_client';
let defaultClient = InstanceMetadataClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new InstanceMetadataClient.GetTokenApi();
let metadata = "metadata_example"; // String | This must be set to 'true'.
let resource = "resource_example"; // String | This is the urlencoded identifier URI of the sink resource for the requested Azure AD token. The resulting token contains the corresponding aud for this resource.
let apiVersion = "apiVersion_example"; // String | This is the API version to use.
let opts = {
  'clientId': "clientId_example", // String | This identifies, by Azure AD client id, a specific explicit identity to use when authenticating to Azure AD. Mutually exclusive with object_id and msi_res_id.
  'objectId': "objectId_example", // String | This identifies, by Azure AD object id, a specific explicit identity to use when authenticating to Azure AD. Mutually exclusive with client_id and msi_res_id.
  'msiResId': "msiResId_example", // String | This identifies, by urlencoded ARM resource id, a specific explicit identity to use when authenticating to Azure AD. Mutually exclusive with client_id and object_id.
  'authority': "authority_example", // String | This indicates the authority to request AAD tokens from. Defaults to the known authority of the identity to be used.
  'bypassCache': "bypassCache_example" // String | If provided, the value must be 'true'. This indicates to the server that the token must be retrieved from Azure AD and cannot be retrieved from an internal cache.
};
apiInstance.identityGetToken(metadata, resource, apiVersion, opts, (error, data, response) => {
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
 **metadata** | **String**| This must be set to &#39;true&#39;. | 
 **resource** | **String**| This is the urlencoded identifier URI of the sink resource for the requested Azure AD token. The resulting token contains the corresponding aud for this resource. | 
 **apiVersion** | **String**| This is the API version to use. | 
 **clientId** | **String**| This identifies, by Azure AD client id, a specific explicit identity to use when authenticating to Azure AD. Mutually exclusive with object_id and msi_res_id. | [optional] 
 **objectId** | **String**| This identifies, by Azure AD object id, a specific explicit identity to use when authenticating to Azure AD. Mutually exclusive with client_id and msi_res_id. | [optional] 
 **msiResId** | **String**| This identifies, by urlencoded ARM resource id, a specific explicit identity to use when authenticating to Azure AD. Mutually exclusive with client_id and object_id. | [optional] 
 **authority** | **String**| This indicates the authority to request AAD tokens from. Defaults to the known authority of the identity to be used. | [optional] 
 **bypassCache** | **String**| If provided, the value must be &#39;true&#39;. This indicates to the server that the token must be retrieved from Azure AD and cannot be retrieved from an internal cache. | [optional] 

### Return type

[**IdentityTokenResponse**](IdentityTokenResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

