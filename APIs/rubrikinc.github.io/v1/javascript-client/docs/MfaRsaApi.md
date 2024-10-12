# RubrikRestApi.MfaRsaApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createRsaMfaServer**](MfaRsaApi.md#createRsaMfaServer) | **POST** /mfa/rsa/server | Register a new RSA server
[**deleteRsaMfaServer**](MfaRsaApi.md#deleteRsaMfaServer) | **DELETE** /mfa/rsa/server/{id} | Delete RSA server
[**getRsaMfaServer**](MfaRsaApi.md#getRsaMfaServer) | **GET** /mfa/rsa/server/{id} | Get RSA server configuration
[**queryRsaMfaServers**](MfaRsaApi.md#queryRsaMfaServers) | **GET** /mfa/rsa/server | Get RSA server configuration
[**updateRsaMfaServer**](MfaRsaApi.md#updateRsaMfaServer) | **PATCH** /mfa/rsa/server/{id} | Update RSA server configuration



## createRsaMfaServer

> RsaMfaServerDetail createRsaMfaServer(rsaMfaServerConfig)

Register a new RSA server

Register a new RSA server using specified configuration.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MfaRsaApi();
let rsaMfaServerConfig = new RubrikRestApi.RsaMfaServerConfig(); // RsaMfaServerConfig | Configuration of RSA server.
apiInstance.createRsaMfaServer(rsaMfaServerConfig, (error, data, response) => {
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
 **rsaMfaServerConfig** | [**RsaMfaServerConfig**](RsaMfaServerConfig.md)| Configuration of RSA server. | 

### Return type

[**RsaMfaServerDetail**](RsaMfaServerDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteRsaMfaServer

> deleteRsaMfaServer(id)

Delete RSA server

Delete RSA server configuration.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MfaRsaApi();
let id = "id_example"; // String | ID of the RSA server.
apiInstance.deleteRsaMfaServer(id, (error, data, response) => {
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
 **id** | **String**| ID of the RSA server. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRsaMfaServer

> RsaMfaServerDetail getRsaMfaServer(id)

Get RSA server configuration

Get RSA server configuration.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MfaRsaApi();
let id = "id_example"; // String | ID of the RSA server.
apiInstance.getRsaMfaServer(id, (error, data, response) => {
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
 **id** | **String**| ID of the RSA server. | 

### Return type

[**RsaMfaServerDetail**](RsaMfaServerDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryRsaMfaServers

> RsaMfaServerDetailListResponse queryRsaMfaServers()

Get RSA server configuration

Get RSA server configuration.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MfaRsaApi();
apiInstance.queryRsaMfaServers((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**RsaMfaServerDetailListResponse**](RsaMfaServerDetailListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateRsaMfaServer

> RsaMfaServerDetail updateRsaMfaServer(id, rsaMfaServerConfigUpdate)

Update RSA server configuration

Update an existing RSA server using specified configuration.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.MfaRsaApi();
let id = "id_example"; // String | ID of the RSA server.
let rsaMfaServerConfigUpdate = new RubrikRestApi.RsaMfaServerConfigUpdate(); // RsaMfaServerConfigUpdate | Configuration of RSA server.
apiInstance.updateRsaMfaServer(id, rsaMfaServerConfigUpdate, (error, data, response) => {
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
 **id** | **String**| ID of the RSA server. | 
 **rsaMfaServerConfigUpdate** | [**RsaMfaServerConfigUpdate**](RsaMfaServerConfigUpdate.md)| Configuration of RSA server. | 

### Return type

[**RsaMfaServerDetail**](RsaMfaServerDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

