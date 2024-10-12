# MerakiDashboardApi.HttpServersApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkWebhooksHttpServer_2**](HttpServersApi.md#createNetworkWebhooksHttpServer_2) | **POST** /networks/{networkId}/webhooks/httpServers | Add an HTTP server to a network
[**deleteNetworkWebhooksHttpServer_2**](HttpServersApi.md#deleteNetworkWebhooksHttpServer_2) | **DELETE** /networks/{networkId}/webhooks/httpServers/{httpServerId} | Delete an HTTP server from a network
[**getNetworkWebhooksHttpServer_2**](HttpServersApi.md#getNetworkWebhooksHttpServer_2) | **GET** /networks/{networkId}/webhooks/httpServers/{httpServerId} | Return an HTTP server for a network
[**getNetworkWebhooksHttpServers_2**](HttpServersApi.md#getNetworkWebhooksHttpServers_2) | **GET** /networks/{networkId}/webhooks/httpServers | List the HTTP servers for a network
[**updateNetworkWebhooksHttpServer_2**](HttpServersApi.md#updateNetworkWebhooksHttpServer_2) | **PUT** /networks/{networkId}/webhooks/httpServers/{httpServerId} | Update an HTTP server



## createNetworkWebhooksHttpServer_2

> GetNetworkWebhooksHttpServers200ResponseInner createNetworkWebhooksHttpServer_2(networkId, createNetworkWebhooksHttpServerRequest)

Add an HTTP server to a network

Add an HTTP server to a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.HttpServersApi();
let networkId = "networkId_example"; // String | 
let createNetworkWebhooksHttpServerRequest = new MerakiDashboardApi.CreateNetworkWebhooksHttpServerRequest(); // CreateNetworkWebhooksHttpServerRequest | 
apiInstance.createNetworkWebhooksHttpServer_2(networkId, createNetworkWebhooksHttpServerRequest, (error, data, response) => {
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
 **createNetworkWebhooksHttpServerRequest** | [**CreateNetworkWebhooksHttpServerRequest**](CreateNetworkWebhooksHttpServerRequest.md)|  | 

### Return type

[**GetNetworkWebhooksHttpServers200ResponseInner**](GetNetworkWebhooksHttpServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNetworkWebhooksHttpServer_2

> deleteNetworkWebhooksHttpServer_2(networkId, httpServerId)

Delete an HTTP server from a network

Delete an HTTP server from a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.HttpServersApi();
let networkId = "networkId_example"; // String | 
let httpServerId = "httpServerId_example"; // String | 
apiInstance.deleteNetworkWebhooksHttpServer_2(networkId, httpServerId, (error, data, response) => {
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
 **httpServerId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNetworkWebhooksHttpServer_2

> GetNetworkWebhooksHttpServers200ResponseInner getNetworkWebhooksHttpServer_2(networkId, httpServerId)

Return an HTTP server for a network

Return an HTTP server for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.HttpServersApi();
let networkId = "networkId_example"; // String | 
let httpServerId = "httpServerId_example"; // String | 
apiInstance.getNetworkWebhooksHttpServer_2(networkId, httpServerId, (error, data, response) => {
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
 **httpServerId** | **String**|  | 

### Return type

[**GetNetworkWebhooksHttpServers200ResponseInner**](GetNetworkWebhooksHttpServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWebhooksHttpServers_2

> [GetNetworkWebhooksHttpServers200ResponseInner] getNetworkWebhooksHttpServers_2(networkId)

List the HTTP servers for a network

List the HTTP servers for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.HttpServersApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkWebhooksHttpServers_2(networkId, (error, data, response) => {
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

[**[GetNetworkWebhooksHttpServers200ResponseInner]**](GetNetworkWebhooksHttpServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkWebhooksHttpServer_2

> GetNetworkWebhooksHttpServers200ResponseInner updateNetworkWebhooksHttpServer_2(networkId, httpServerId, opts)

Update an HTTP server

Update an HTTP server. To change a URL, create a new HTTP server.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.HttpServersApi();
let networkId = "networkId_example"; // String | 
let httpServerId = "httpServerId_example"; // String | 
let opts = {
  'updateNetworkWebhooksHttpServerRequest': new MerakiDashboardApi.UpdateNetworkWebhooksHttpServerRequest() // UpdateNetworkWebhooksHttpServerRequest | 
};
apiInstance.updateNetworkWebhooksHttpServer_2(networkId, httpServerId, opts, (error, data, response) => {
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
 **httpServerId** | **String**|  | 
 **updateNetworkWebhooksHttpServerRequest** | [**UpdateNetworkWebhooksHttpServerRequest**](UpdateNetworkWebhooksHttpServerRequest.md)|  | [optional] 

### Return type

[**GetNetworkWebhooksHttpServers200ResponseInner**](GetNetworkWebhooksHttpServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

