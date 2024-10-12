# MerakiDashboardApi.MXStaticRoutesApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkStaticRoute**](MXStaticRoutesApi.md#createNetworkStaticRoute) | **POST** /networks/{networkId}/staticRoutes | Add a static route for an MX or teleworker network
[**deleteNetworkStaticRoute**](MXStaticRoutesApi.md#deleteNetworkStaticRoute) | **DELETE** /networks/{networkId}/staticRoutes/{staticRouteId} | Delete a static route from an MX or teleworker network
[**getNetworkStaticRoute**](MXStaticRoutesApi.md#getNetworkStaticRoute) | **GET** /networks/{networkId}/staticRoutes/{staticRouteId} | Return a static route for an MX or teleworker network
[**getNetworkStaticRoutes**](MXStaticRoutesApi.md#getNetworkStaticRoutes) | **GET** /networks/{networkId}/staticRoutes | List the static routes for an MX or teleworker network
[**updateNetworkStaticRoute**](MXStaticRoutesApi.md#updateNetworkStaticRoute) | **PUT** /networks/{networkId}/staticRoutes/{staticRouteId} | Update a static route for an MX or teleworker network



## createNetworkStaticRoute

> Object createNetworkStaticRoute(networkId, createNetworkStaticRouteRequest)

Add a static route for an MX or teleworker network

Add a static route for an MX or teleworker network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MXStaticRoutesApi();
let networkId = "networkId_example"; // String | 
let createNetworkStaticRouteRequest = new MerakiDashboardApi.CreateNetworkStaticRouteRequest(); // CreateNetworkStaticRouteRequest | 
apiInstance.createNetworkStaticRoute(networkId, createNetworkStaticRouteRequest, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **createNetworkStaticRouteRequest** | [**CreateNetworkStaticRouteRequest**](CreateNetworkStaticRouteRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNetworkStaticRoute

> deleteNetworkStaticRoute(networkId, staticRouteId)

Delete a static route from an MX or teleworker network

Delete a static route from an MX or teleworker network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MXStaticRoutesApi();
let networkId = "networkId_example"; // String | 
let staticRouteId = "staticRouteId_example"; // String | 
apiInstance.deleteNetworkStaticRoute(networkId, staticRouteId, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **staticRouteId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNetworkStaticRoute

> Object getNetworkStaticRoute(networkId, staticRouteId)

Return a static route for an MX or teleworker network

Return a static route for an MX or teleworker network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MXStaticRoutesApi();
let networkId = "networkId_example"; // String | 
let staticRouteId = "staticRouteId_example"; // String | 
apiInstance.getNetworkStaticRoute(networkId, staticRouteId, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **staticRouteId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkStaticRoutes

> [Object] getNetworkStaticRoutes(networkId)

List the static routes for an MX or teleworker network

List the static routes for an MX or teleworker network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MXStaticRoutesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkStaticRoutes(networkId, (error, data, response) => {
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
 **networkId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkStaticRoute

> Object updateNetworkStaticRoute(networkId, staticRouteId, opts)

Update a static route for an MX or teleworker network

Update a static route for an MX or teleworker network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MXStaticRoutesApi();
let networkId = "networkId_example"; // String | 
let staticRouteId = "staticRouteId_example"; // String | 
let opts = {
  'updateNetworkStaticRouteRequest': new MerakiDashboardApi.UpdateNetworkStaticRouteRequest() // UpdateNetworkStaticRouteRequest | 
};
apiInstance.updateNetworkStaticRoute(networkId, staticRouteId, opts, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **staticRouteId** | **String**|  | 
 **updateNetworkStaticRouteRequest** | [**UpdateNetworkStaticRouteRequest**](UpdateNetworkStaticRouteRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

