# TurbineLabsApi.ProxyApi

All URIs are relative to *https://api.turbinelabs.io/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**proxyGet**](ProxyApi.md#proxyGet) | **GET** /proxy | list proxies
[**proxyPost**](ProxyApi.md#proxyPost) | **POST** /proxy | create proxy
[**proxyProxyKeyDelete**](ProxyApi.md#proxyProxyKeyDelete) | **DELETE** /proxy/{proxyKey} | delete proxy
[**proxyProxyKeyGet**](ProxyApi.md#proxyProxyKeyGet) | **GET** /proxy/{proxyKey} | get proxy



## proxyGet

> MultiProxyResult proxyGet(opts)

list proxies

Get a list of proxies

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.ProxyApi();
let opts = {
  'filters': "filters_example" // String | A JSON encoded array of ProxyFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any ProxyFilter will be included. 
};
apiInstance.proxyGet(opts, (error, data, response) => {
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
 **filters** | **String**| A JSON encoded array of ProxyFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any ProxyFilter will be included.  | [optional] 

### Return type

[**MultiProxyResult**](MultiProxyResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proxyPost

> ProxyResult proxyPost(proxy)

create proxy

Create a new proxy

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.ProxyApi();
let proxy = new TurbineLabsApi.ProxyCreate(); // ProxyCreate | the proxy to create
apiInstance.proxyPost(proxy, (error, data, response) => {
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
 **proxy** | [**ProxyCreate**](ProxyCreate.md)| the proxy to create | 

### Return type

[**ProxyResult**](ProxyResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## proxyProxyKeyDelete

> Proxy proxyProxyKeyDelete(proxyKey, checksum)

delete proxy

Delete existing proxy

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.ProxyApi();
let proxyKey = "72c86057-ee8d-4a2b-a3a7-760fbd1d3b9f"; // String | the proxy key
let checksum = "9cd24183-f848-48f8-6f55-0f07240700b9"; // String | the current checksum of the proxy to be deleted
apiInstance.proxyProxyKeyDelete(proxyKey, checksum, (error, data, response) => {
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
 **proxyKey** | **String**| the proxy key | 
 **checksum** | **String**| the current checksum of the proxy to be deleted | 

### Return type

[**Proxy**](Proxy.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proxyProxyKeyGet

> ProxyResult proxyProxyKeyGet(proxyKey)

get proxy

Get details for a single proxy

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.ProxyApi();
let proxyKey = "72c86057-ee8d-4a2b-a3a7-760fbd1d3b9f"; // String | the proxy key
apiInstance.proxyProxyKeyGet(proxyKey, (error, data, response) => {
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
 **proxyKey** | **String**| the proxy key | 

### Return type

[**ProxyResult**](ProxyResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

