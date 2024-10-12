# MesheryApi.ProvidersAPIApi

All URIs are relative to *http://meshery.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**idChoiceProvider**](ProvidersAPIApi.md#idChoiceProvider) | **GET** /api/provider | Handle GET request for the choice of provider
[**idGetProviderCapabilities**](ProvidersAPIApi.md#idGetProviderCapabilities) | **GET** /api/provider/capabilities | Handle GET requests for Provider
[**idGetProvidersList**](ProvidersAPIApi.md#idGetProvidersList) | **GET** /api/providers | Handle GET request for list of providers
[**idProvider**](ProvidersAPIApi.md#idProvider) | **GET** /provider | Handle GET request to provider UI
[**idReactComponents**](ProvidersAPIApi.md#idReactComponents) | **GET** /api/provider/extension | Handle GET request for React Components



## idChoiceProvider

> idChoiceProvider(opts)

Handle GET request for the choice of provider

Update the choice of provider in system

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.ProvidersAPIApi();
let opts = {
  'provider': "provider_example" // String | 
};
apiInstance.idChoiceProvider(opts, (error, data, response) => {
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
 **provider** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## idGetProviderCapabilities

> idGetProviderCapabilities()

Handle GET requests for Provider

Returns the capabilities.json for the provider

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.ProvidersAPIApi();
apiInstance.idGetProviderCapabilities((error, data, response) => {
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

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## idGetProvidersList

> {String: ProviderProperties} idGetProvidersList()

Handle GET request for list of providers

Returns the available list of providers

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.ProvidersAPIApi();
apiInstance.idGetProvidersList((error, data, response) => {
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

[**{String: ProviderProperties}**](ProviderProperties.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idProvider

> idProvider()

Handle GET request to provider UI

Servers providers UI

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.ProvidersAPIApi();
apiInstance.idProvider((error, data, response) => {
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

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## idReactComponents

> idReactComponents()

Handle GET request for React Components

handles the requests to serve react components from the provider package

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.ProvidersAPIApi();
apiInstance.idReactComponents((error, data, response) => {
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

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

