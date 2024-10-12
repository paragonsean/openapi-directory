# MerakiDashboardApi.MonitoredMediaServersApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrganizationInsightMonitoredMediaServer_1**](MonitoredMediaServersApi.md#createOrganizationInsightMonitoredMediaServer_1) | **POST** /organizations/{organizationId}/insight/monitoredMediaServers | Add a media server to be monitored for this organization
[**deleteOrganizationInsightMonitoredMediaServer_1**](MonitoredMediaServersApi.md#deleteOrganizationInsightMonitoredMediaServer_1) | **DELETE** /organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId} | Delete a monitored media server from this organization
[**getOrganizationInsightMonitoredMediaServer_1**](MonitoredMediaServersApi.md#getOrganizationInsightMonitoredMediaServer_1) | **GET** /organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId} | Return a monitored media server for this organization
[**getOrganizationInsightMonitoredMediaServers_1**](MonitoredMediaServersApi.md#getOrganizationInsightMonitoredMediaServers_1) | **GET** /organizations/{organizationId}/insight/monitoredMediaServers | List the monitored media servers for this organization
[**updateOrganizationInsightMonitoredMediaServer_1**](MonitoredMediaServersApi.md#updateOrganizationInsightMonitoredMediaServer_1) | **PUT** /organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId} | Update a monitored media server for this organization



## createOrganizationInsightMonitoredMediaServer_1

> Object createOrganizationInsightMonitoredMediaServer_1(organizationId, createOrganizationInsightMonitoredMediaServerRequest)

Add a media server to be monitored for this organization

Add a media server to be monitored for this organization. Only valid for organizations with Meraki Insight.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MonitoredMediaServersApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationInsightMonitoredMediaServerRequest = new MerakiDashboardApi.CreateOrganizationInsightMonitoredMediaServerRequest(); // CreateOrganizationInsightMonitoredMediaServerRequest | 
apiInstance.createOrganizationInsightMonitoredMediaServer_1(organizationId, createOrganizationInsightMonitoredMediaServerRequest, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **createOrganizationInsightMonitoredMediaServerRequest** | [**CreateOrganizationInsightMonitoredMediaServerRequest**](CreateOrganizationInsightMonitoredMediaServerRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteOrganizationInsightMonitoredMediaServer_1

> deleteOrganizationInsightMonitoredMediaServer_1(organizationId, monitoredMediaServerId)

Delete a monitored media server from this organization

Delete a monitored media server from this organization. Only valid for organizations with Meraki Insight.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MonitoredMediaServersApi();
let organizationId = "organizationId_example"; // String | 
let monitoredMediaServerId = "monitoredMediaServerId_example"; // String | 
apiInstance.deleteOrganizationInsightMonitoredMediaServer_1(organizationId, monitoredMediaServerId, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **monitoredMediaServerId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationInsightMonitoredMediaServer_1

> Object getOrganizationInsightMonitoredMediaServer_1(organizationId, monitoredMediaServerId)

Return a monitored media server for this organization

Return a monitored media server for this organization. Only valid for organizations with Meraki Insight.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MonitoredMediaServersApi();
let organizationId = "organizationId_example"; // String | 
let monitoredMediaServerId = "monitoredMediaServerId_example"; // String | 
apiInstance.getOrganizationInsightMonitoredMediaServer_1(organizationId, monitoredMediaServerId, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **monitoredMediaServerId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationInsightMonitoredMediaServers_1

> [GetOrganizationInsightMonitoredMediaServers200ResponseInner] getOrganizationInsightMonitoredMediaServers_1(organizationId)

List the monitored media servers for this organization

List the monitored media servers for this organization. Only valid for organizations with Meraki Insight.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MonitoredMediaServersApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationInsightMonitoredMediaServers_1(organizationId, (error, data, response) => {
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
 **organizationId** | **String**|  | 

### Return type

[**[GetOrganizationInsightMonitoredMediaServers200ResponseInner]**](GetOrganizationInsightMonitoredMediaServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateOrganizationInsightMonitoredMediaServer_1

> Object updateOrganizationInsightMonitoredMediaServer_1(organizationId, monitoredMediaServerId, opts)

Update a monitored media server for this organization

Update a monitored media server for this organization. Only valid for organizations with Meraki Insight.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MonitoredMediaServersApi();
let organizationId = "organizationId_example"; // String | 
let monitoredMediaServerId = "monitoredMediaServerId_example"; // String | 
let opts = {
  'updateOrganizationInsightMonitoredMediaServerRequest': new MerakiDashboardApi.UpdateOrganizationInsightMonitoredMediaServerRequest() // UpdateOrganizationInsightMonitoredMediaServerRequest | 
};
apiInstance.updateOrganizationInsightMonitoredMediaServer_1(organizationId, monitoredMediaServerId, opts, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **monitoredMediaServerId** | **String**|  | 
 **updateOrganizationInsightMonitoredMediaServerRequest** | [**UpdateOrganizationInsightMonitoredMediaServerRequest**](UpdateOrganizationInsightMonitoredMediaServerRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

