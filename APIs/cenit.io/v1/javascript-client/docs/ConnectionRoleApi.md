# CenitIoRestApiSpecification.ConnectionRoleApi

All URIs are relative to *https://cenit.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**setupConnectionRoleGet**](ConnectionRoleApi.md#setupConnectionRoleGet) | **GET** /setup/connection_role | Returns a list of connection roles
[**setupConnectionRoleIdDelete**](ConnectionRoleApi.md#setupConnectionRoleIdDelete) | **DELETE** /setup/connection_role/{id} | Delete a connection role.
[**setupConnectionRoleIdGet**](ConnectionRoleApi.md#setupConnectionRoleIdGet) | **GET** /setup/connection_role/{id} | Return a connection role
[**setupConnectionRolePost**](ConnectionRoleApi.md#setupConnectionRolePost) | **POST** /setup/connection_role | Create or update a connection role



## setupConnectionRoleGet

> [ConnectionRole] setupConnectionRoleGet()

Returns a list of connection roles

Returns a list of connection roles you&#39;ve previously created. The connection roles are returned in sorted order, with the most recent connection role appearing first.

### Example

```javascript
import CenitIoRestApiSpecification from 'cenit_io_rest_api_specification';
let defaultClient = CenitIoRestApiSpecification.ApiClient.instance;
// Configure API key authorization: X-User-Access-Key
let X-User-Access-Key = defaultClient.authentications['X-User-Access-Key'];
X-User-Access-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-User-Access-Token
let X-User-Access-Token = defaultClient.authentications['X-User-Access-Token'];
X-User-Access-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Token.apiKeyPrefix = 'Token';

let apiInstance = new CenitIoRestApiSpecification.ConnectionRoleApi();
apiInstance.setupConnectionRoleGet((error, data, response) => {
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

[**[ConnectionRole]**](ConnectionRole.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupConnectionRoleIdDelete

> setupConnectionRoleIdDelete(id)

Delete a connection role.

Deletes the specified connection role.

### Example

```javascript
import CenitIoRestApiSpecification from 'cenit_io_rest_api_specification';
let defaultClient = CenitIoRestApiSpecification.ApiClient.instance;
// Configure API key authorization: X-User-Access-Key
let X-User-Access-Key = defaultClient.authentications['X-User-Access-Key'];
X-User-Access-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-User-Access-Token
let X-User-Access-Token = defaultClient.authentications['X-User-Access-Token'];
X-User-Access-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Token.apiKeyPrefix = 'Token';

let apiInstance = new CenitIoRestApiSpecification.ConnectionRoleApi();
let id = "id_example"; // String | Connection role ID
apiInstance.setupConnectionRoleIdDelete(id, (error, data, response) => {
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
 **id** | **String**| Connection role ID | 

### Return type

null (empty response body)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setupConnectionRoleIdGet

> ConnectionRole setupConnectionRoleIdGet(id)

Return a connection role

Returns a connection role

### Example

```javascript
import CenitIoRestApiSpecification from 'cenit_io_rest_api_specification';
let defaultClient = CenitIoRestApiSpecification.ApiClient.instance;
// Configure API key authorization: X-User-Access-Key
let X-User-Access-Key = defaultClient.authentications['X-User-Access-Key'];
X-User-Access-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-User-Access-Token
let X-User-Access-Token = defaultClient.authentications['X-User-Access-Token'];
X-User-Access-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Token.apiKeyPrefix = 'Token';

let apiInstance = new CenitIoRestApiSpecification.ConnectionRoleApi();
let id = "id_example"; // String | Connection role ID
apiInstance.setupConnectionRoleIdGet(id, (error, data, response) => {
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
 **id** | **String**| Connection role ID | 

### Return type

[**ConnectionRole**](ConnectionRole.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupConnectionRolePost

> ConnectionRole setupConnectionRolePost()

Create or update a connection role

Creates or updates the specified connection role by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

### Example

```javascript
import CenitIoRestApiSpecification from 'cenit_io_rest_api_specification';
let defaultClient = CenitIoRestApiSpecification.ApiClient.instance;
// Configure API key authorization: X-User-Access-Key
let X-User-Access-Key = defaultClient.authentications['X-User-Access-Key'];
X-User-Access-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-User-Access-Token
let X-User-Access-Token = defaultClient.authentications['X-User-Access-Token'];
X-User-Access-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Token.apiKeyPrefix = 'Token';

let apiInstance = new CenitIoRestApiSpecification.ConnectionRoleApi();
apiInstance.setupConnectionRolePost((error, data, response) => {
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

[**ConnectionRole**](ConnectionRole.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

