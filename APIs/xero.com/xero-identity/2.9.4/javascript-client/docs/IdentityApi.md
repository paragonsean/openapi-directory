# XeroOAuth2IdentityServiceApi.IdentityApi

All URIs are relative to *https://api.xero.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteConnection**](IdentityApi.md#deleteConnection) | **DELETE** /Connections/{id} | Deletes a connection for this user (i.e. disconnect a tenant)
[**getConnections**](IdentityApi.md#getConnections) | **GET** /Connections | Retrieves the connections for this user



## deleteConnection

> deleteConnection(id)

Deletes a connection for this user (i.e. disconnect a tenant)

Override the base server url that include version

### Example

```javascript
import XeroOAuth2IdentityServiceApi from 'xero_o_auth_2_identity_service_api';
let defaultClient = XeroOAuth2IdentityServiceApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroOAuth2IdentityServiceApi.IdentityApi();
let id = "id_example"; // String | Unique identifier for retrieving single object
apiInstance.deleteConnection(id, (error, data, response) => {
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
 **id** | **String**| Unique identifier for retrieving single object | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getConnections

> [Connection] getConnections(opts)

Retrieves the connections for this user

Override the base server url that include version

### Example

```javascript
import XeroOAuth2IdentityServiceApi from 'xero_o_auth_2_identity_service_api';
let defaultClient = XeroOAuth2IdentityServiceApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroOAuth2IdentityServiceApi.IdentityApi();
let opts = {
  'authEventId': "00000000-0000-0000-0000-000000000000" // String | Filter by authEventId
};
apiInstance.getConnections(opts, (error, data, response) => {
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
 **authEventId** | **String**| Filter by authEventId | [optional] 

### Return type

[**[Connection]**](Connection.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

