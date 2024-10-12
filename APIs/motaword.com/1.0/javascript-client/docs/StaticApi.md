# MotaWordApi.StaticApi

All URIs are relative to *https://api.motaword.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEndpoints**](StaticApi.md#getEndpoints) | **GET** / | Available endpoints
[**getFormats**](StaticApi.md#getFormats) | **GET** /formats | List of supported file formats
[**getLanguages**](StaticApi.md#getLanguages) | **GET** /languages | List of supported languages
[**getSwaggerYaml**](StaticApi.md#getSwaggerYaml) | **GET** /swagger | OpenAPI YAML representation of our API



## getEndpoints

> Object getEndpoints()

Available endpoints

The root endpoint will provide you with an OpenAPI definition of MotaWord API. 

### Example

```javascript
import MotaWordApi from 'mota_word_api';

let apiInstance = new MotaWordApi.StaticApi();
apiInstance.getEndpoints((error, data, response) => {
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/yaml, application/json


## getFormats

> [Formats] getFormats()

List of supported file formats

Get a list of supported formats for documents, style guides and extensions. 

### Example

```javascript
import MotaWordApi from 'mota_word_api';

let apiInstance = new MotaWordApi.StaticApi();
apiInstance.getFormats((error, data, response) => {
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

[**[Formats]**](Formats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLanguages

> [Language] getLanguages()

List of supported languages

Get a list of supported languages

### Example

```javascript
import MotaWordApi from 'mota_word_api';

let apiInstance = new MotaWordApi.StaticApi();
apiInstance.getLanguages((error, data, response) => {
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

[**[Language]**](Language.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSwaggerYaml

> String getSwaggerYaml()

OpenAPI YAML representation of our API

Get Swagger YAML

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StaticApi();
apiInstance.getSwaggerYaml((error, data, response) => {
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

**String**

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/yaml

