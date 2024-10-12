# CdnManagementClient.EdgenodesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edgeNodesList**](EdgenodesApi.md#edgeNodesList) | **GET** /providers/Microsoft.Cdn/edgenodes | 



## edgeNodesList

> EdgenodeResult edgeNodesList(apiVersion)



Edgenodes are the global Point of Presence (POP) locations used to deliver CDN content to end users.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.EdgenodesApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.edgeNodesList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 

### Return type

[**EdgenodeResult**](EdgenodeResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

