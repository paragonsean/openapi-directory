# ApisGuru.APIsApi

All URIs are relative to *https://api.apis.guru/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAPI**](APIsApi.md#getAPI) | **GET** /specs/{provider}/{api}.json | Retrieve one version of a particular API
[**getMetrics**](APIsApi.md#getMetrics) | **GET** /metrics.json | Get basic metrics
[**getProvider**](APIsApi.md#getProvider) | **GET** /{provider}.json | List all APIs for a particular provider
[**getProviders**](APIsApi.md#getProviders) | **GET** /providers.json | List all providers
[**getServiceAPI**](APIsApi.md#getServiceAPI) | **GET** /specs/{provider}/{service}/{api}.json | Retrieve one version of a particular API with a serviceName.
[**getServices**](APIsApi.md#getServices) | **GET** /{provider}/services.json | List all serviceNames for a particular provider
[**listAPIs**](APIsApi.md#listAPIs) | **GET** /list.json | List all APIs



## getAPI

> API getAPI(provider, api)

Retrieve one version of a particular API

Returns the API entry for one specific version of an API where there is no serviceName.

### Example

```javascript
import ApisGuru from 'apis_guru';

let apiInstance = new ApisGuru.APIsApi();
let provider = "apis.guru"; // String | 
let api = "2.1.0"; // String | 
apiInstance.getAPI(provider, api, (error, data, response) => {
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
 **provider** | **String**|  | 
 **api** | **String**|  | 

### Return type

[**API**](API.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMetrics

> Metrics getMetrics()

Get basic metrics

Some basic metrics for the entire directory. Just stunning numbers to put on a front page and are intended purely for WoW effect :) 

### Example

```javascript
import ApisGuru from 'apis_guru';

let apiInstance = new ApisGuru.APIsApi();
apiInstance.getMetrics((error, data, response) => {
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

[**Metrics**](Metrics.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProvider

> {String: API} getProvider(provider)

List all APIs for a particular provider

List all APIs in the directory for a particular providerName Returns links to the individual API entry for each API. 

### Example

```javascript
import ApisGuru from 'apis_guru';

let apiInstance = new ApisGuru.APIsApi();
let provider = "apis.guru"; // String | 
apiInstance.getProvider(provider, (error, data, response) => {
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
 **provider** | **String**|  | 

### Return type

[**{String: API}**](API.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProviders

> GetProviders200Response getProviders()

List all providers

List all the providers in the directory 

### Example

```javascript
import ApisGuru from 'apis_guru';

let apiInstance = new ApisGuru.APIsApi();
apiInstance.getProviders((error, data, response) => {
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

[**GetProviders200Response**](GetProviders200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServiceAPI

> API getServiceAPI(provider, service, api)

Retrieve one version of a particular API with a serviceName.

Returns the API entry for one specific version of an API where there is a serviceName.

### Example

```javascript
import ApisGuru from 'apis_guru';

let apiInstance = new ApisGuru.APIsApi();
let provider = "apis.guru"; // String | 
let service = "graph"; // String | 
let api = "2.1.0"; // String | 
apiInstance.getServiceAPI(provider, service, api, (error, data, response) => {
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
 **provider** | **String**|  | 
 **service** | **String**|  | 
 **api** | **String**|  | 

### Return type

[**API**](API.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServices

> GetServices200Response getServices(provider)

List all serviceNames for a particular provider

List all serviceNames in the directory for a particular providerName 

### Example

```javascript
import ApisGuru from 'apis_guru';

let apiInstance = new ApisGuru.APIsApi();
let provider = "apis.guru"; // String | 
apiInstance.getServices(provider, (error, data, response) => {
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
 **provider** | **String**|  | 

### Return type

[**GetServices200Response**](GetServices200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAPIs

> {String: API} listAPIs()

List all APIs

List all APIs in the directory. Returns links to the OpenAPI definitions for each API in the directory. If API exist in multiple versions &#x60;preferred&#x60; one is explicitly marked. Some basic info from the OpenAPI definition is cached inside each object. This allows you to generate some simple views without needing to fetch the OpenAPI definition for each API. 

### Example

```javascript
import ApisGuru from 'apis_guru';

let apiInstance = new ApisGuru.APIsApi();
apiInstance.listAPIs((error, data, response) => {
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

[**{String: API}**](API.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

