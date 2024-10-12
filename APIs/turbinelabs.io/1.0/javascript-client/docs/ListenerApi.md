# TurbineLabsApi.ListenerApi

All URIs are relative to *https://api.turbinelabs.io/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listenerGet**](ListenerApi.md#listenerGet) | **GET** /listener | list listeners
[**listenerListenerKeyDelete**](ListenerApi.md#listenerListenerKeyDelete) | **DELETE** /listener/{listenerKey} | delete listener
[**listenerListenerKeyGet**](ListenerApi.md#listenerListenerKeyGet) | **GET** /listener/{listenerKey} | get listener
[**listenerListenerKeyPut**](ListenerApi.md#listenerListenerKeyPut) | **PUT** /listener/{listenerKey} | modify listener
[**listenerPost**](ListenerApi.md#listenerPost) | **POST** /listener | create listener



## listenerGet

> MultiListenerResult listenerGet(opts)

list listeners

Get a list of listeners

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.ListenerApi();
let opts = {
  'filters': "filters_example" // String | A JSON encoded array of ListenerFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any ListenerFilter will be included. 
};
apiInstance.listenerGet(opts, (error, data, response) => {
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
 **filters** | **String**| A JSON encoded array of ListenerFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any ListenerFilter will be included.  | [optional] 

### Return type

[**MultiListenerResult**](MultiListenerResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listenerListenerKeyDelete

> Listener listenerListenerKeyDelete(listenerKey, checksum)

delete listener

Delete existing listener

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.ListenerApi();
let listenerKey = "72c86057-ee8d-4a2b-a3a7-760fbd1d3b9f"; // String | the listener key
let checksum = "9cd24183-f848-48f8-6f55-0f07240700b9"; // String | the current checksum of the listener to be deleted
apiInstance.listenerListenerKeyDelete(listenerKey, checksum, (error, data, response) => {
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
 **listenerKey** | **String**| the listener key | 
 **checksum** | **String**| the current checksum of the listener to be deleted | 

### Return type

[**Listener**](Listener.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listenerListenerKeyGet

> ListenerResult listenerListenerKeyGet(listenerKey)

get listener

Get details for a single listener

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.ListenerApi();
let listenerKey = "72c86057-ee8d-4a2b-a3a7-760fbd1d3b9f"; // String | the listener key
apiInstance.listenerListenerKeyGet(listenerKey, (error, data, response) => {
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
 **listenerKey** | **String**| the listener key | 

### Return type

[**ListenerResult**](ListenerResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listenerListenerKeyPut

> ListenerResult listenerListenerKeyPut(listenerKey, listener)

modify listener

Modify an existing listener

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.ListenerApi();
let listenerKey = "5074fe62-821e-4034-55bd-b9caa09af2a1"; // String | the listener key
let listener = new TurbineLabsApi.Listener(); // Listener | the listener to modify
apiInstance.listenerListenerKeyPut(listenerKey, listener, (error, data, response) => {
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
 **listenerKey** | **String**| the listener key | 
 **listener** | [**Listener**](Listener.md)| the listener to modify | 

### Return type

[**ListenerResult**](ListenerResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listenerPost

> ListenerResult listenerPost(listener)

create listener

Create a new listener

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.ListenerApi();
let listener = new TurbineLabsApi.ListenerCreate(); // ListenerCreate | the listener to create
apiInstance.listenerPost(listener, (error, data, response) => {
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
 **listener** | [**ListenerCreate**](ListenerCreate.md)| the listener to create | 

### Return type

[**ListenerResult**](ListenerResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

