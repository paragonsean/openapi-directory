# TurbineLabsApi.RouteApi

All URIs are relative to *https://api.turbinelabs.io/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**routeGet**](RouteApi.md#routeGet) | **GET** /route | get routes
[**routePost**](RouteApi.md#routePost) | **POST** /route | create route
[**routeRouteKeyDelete**](RouteApi.md#routeRouteKeyDelete) | **DELETE** /route/{routeKey} | delete route
[**routeRouteKeyGet**](RouteApi.md#routeRouteKeyGet) | **GET** /route/{routeKey} | get route
[**routeRouteKeyPut**](RouteApi.md#routeRouteKeyPut) | **PUT** /route/{routeKey} | modify route
[**sharedRulesSharedRulesKeyDelete**](RouteApi.md#sharedRulesSharedRulesKeyDelete) | **DELETE** /shared_rules/{sharedRulesKey} | delete shared_rules object



## routeGet

> MultiRouteResult routeGet(opts)

get routes

Get a list of routes

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.RouteApi();
let opts = {
  'filters': "filters_example" // String | A JSON encoded array of RouteFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any RouteFilter will be included. 
};
apiInstance.routeGet(opts, (error, data, response) => {
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
 **filters** | **String**| A JSON encoded array of RouteFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any RouteFilter will be included.  | [optional] 

### Return type

[**MultiRouteResult**](MultiRouteResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## routePost

> RouteResult routePost(route)

create route

Create a new route

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.RouteApi();
let route = new TurbineLabsApi.RouteCreate(); // RouteCreate | the route to create
apiInstance.routePost(route, (error, data, response) => {
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
 **route** | [**RouteCreate**](RouteCreate.md)| the route to create | 

### Return type

[**RouteResult**](RouteResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## routeRouteKeyDelete

> Object routeRouteKeyDelete(routeKey, checksum)

delete route

Delete an existing route

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.RouteApi();
let routeKey = "1c7b1c5e-1a23-4d04-5cb4-eccea4d5994c"; // String | the route key
let checksum = "9cd24183-f848-48f8-6f55-0f07240700b9"; // String | the current checksum of the route to be deleted
apiInstance.routeRouteKeyDelete(routeKey, checksum, (error, data, response) => {
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
 **routeKey** | **String**| the route key | 
 **checksum** | **String**| the current checksum of the route to be deleted | 

### Return type

**Object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## routeRouteKeyGet

> RouteResult routeRouteKeyGet(routeKey)

get route

Get details for an existing route

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.RouteApi();
let routeKey = "1c7b1c5e-1a23-4d04-5cb4-eccea4d5994c"; // String | the route key
apiInstance.routeRouteKeyGet(routeKey, (error, data, response) => {
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
 **routeKey** | **String**| the route key | 

### Return type

[**RouteResult**](RouteResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## routeRouteKeyPut

> RouteResult routeRouteKeyPut(routeKey, route)

modify route

Modify an existing route

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.RouteApi();
let routeKey = "1c7b1c5e-1a23-4d04-5cb4-eccea4d5994c"; // String | the route key
let route = new TurbineLabsApi.Route(); // Route | the route to modify
apiInstance.routeRouteKeyPut(routeKey, route, (error, data, response) => {
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
 **routeKey** | **String**| the route key | 
 **route** | [**Route**](Route.md)| the route to modify | 

### Return type

[**RouteResult**](RouteResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sharedRulesSharedRulesKeyDelete

> Object sharedRulesSharedRulesKeyDelete(sharedRulesKey, checksum)

delete shared_rules object

Delete an existing shared_rules object

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.RouteApi();
let sharedRulesKey = "1c7b1c5e-1a23-4d04-5cb4-eccea4d5994c"; // String | the shared_rules key
let checksum = "9cd24183-f848-48f8-6f55-0f07240700b9"; // String | the current checksum of the shared_rules to be deleted
apiInstance.sharedRulesSharedRulesKeyDelete(sharedRulesKey, checksum, (error, data, response) => {
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
 **sharedRulesKey** | **String**| the shared_rules key | 
 **checksum** | **String**| the current checksum of the shared_rules to be deleted | 

### Return type

**Object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

