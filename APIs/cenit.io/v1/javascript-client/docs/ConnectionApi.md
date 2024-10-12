# CenitIoRestApiSpecification.ConnectionApi

All URIs are relative to *https://cenit.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**setupConnectionGet**](ConnectionApi.md#setupConnectionGet) | **GET** /setup/connection | Returns a list of connections
[**setupConnectionIdDelete**](ConnectionApi.md#setupConnectionIdDelete) | **DELETE** /setup/connection/{id} | Delete a connection
[**setupConnectionIdGet**](ConnectionApi.md#setupConnectionIdGet) | **GET** /setup/connection/{id} | Retrieve an existing connection
[**setupConnectionPost**](ConnectionApi.md#setupConnectionPost) | **POST** /setup/connection | Create or update a connection



## setupConnectionGet

> [Connection] setupConnectionGet()

Returns a list of connections

Returns a list of connections you&#39;ve previously created. The connections are returned in sorted order, with the most recent connection appearing first.

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

let apiInstance = new CenitIoRestApiSpecification.ConnectionApi();
apiInstance.setupConnectionGet((error, data, response) => {
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

[**[Connection]**](Connection.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupConnectionIdDelete

> setupConnectionIdDelete(id)

Delete a connection

Permanently deletes a connection. It cannot be undone.

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

let apiInstance = new CenitIoRestApiSpecification.ConnectionApi();
let id = "id_example"; // String | Connection ID
apiInstance.setupConnectionIdDelete(id, (error, data, response) => {
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
 **id** | **String**| Connection ID | 

### Return type

null (empty response body)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setupConnectionIdGet

> Connection setupConnectionIdGet(id)

Retrieve an existing connection

Retrieves the details of an existing connection. You need only supply the unique connection identifier that was returned upon connection creation.

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

let apiInstance = new CenitIoRestApiSpecification.ConnectionApi();
let id = "id_example"; // String | Connection ID
apiInstance.setupConnectionIdGet(id, (error, data, response) => {
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
 **id** | **String**| Connection ID | 

### Return type

[**Connection**](Connection.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupConnectionPost

> Connection setupConnectionPost()

Create or update a connection

Creates or updates the specified connection by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

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

let apiInstance = new CenitIoRestApiSpecification.ConnectionApi();
apiInstance.setupConnectionPost((error, data, response) => {
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

[**Connection**](Connection.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

