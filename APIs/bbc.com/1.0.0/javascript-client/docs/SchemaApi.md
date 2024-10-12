# BbcNitroApi.SchemaApi

All URIs are relative to *https://programmes.api.bbc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAPI**](SchemaApi.md#getAPI) | **GET** / | Get API definition
[**getXSD**](SchemaApi.md#getXSD) | **GET** /schema | Get Schema definition



## getAPI

> getAPI()

Get API definition

Get API definition

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.SchemaApi();
apiInstance.getAPI((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getXSD

> getXSD()

Get Schema definition

Get Schema definition

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.SchemaApi();
apiInstance.getXSD((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

