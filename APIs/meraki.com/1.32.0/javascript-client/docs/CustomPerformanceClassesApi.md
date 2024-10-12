# MerakiDashboardApi.CustomPerformanceClassesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkApplianceTrafficShapingCustomPerformanceClass_2**](CustomPerformanceClassesApi.md#createNetworkApplianceTrafficShapingCustomPerformanceClass_2) | **POST** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses | Add a custom performance class for an MX network
[**deleteNetworkApplianceTrafficShapingCustomPerformanceClass_2**](CustomPerformanceClassesApi.md#deleteNetworkApplianceTrafficShapingCustomPerformanceClass_2) | **DELETE** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId} | Delete a custom performance class from an MX network
[**getNetworkApplianceTrafficShapingCustomPerformanceClass_2**](CustomPerformanceClassesApi.md#getNetworkApplianceTrafficShapingCustomPerformanceClass_2) | **GET** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId} | Return a custom performance class for an MX network
[**getNetworkApplianceTrafficShapingCustomPerformanceClasses_2**](CustomPerformanceClassesApi.md#getNetworkApplianceTrafficShapingCustomPerformanceClasses_2) | **GET** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses | List all custom performance classes for an MX network
[**updateNetworkApplianceTrafficShapingCustomPerformanceClass_2**](CustomPerformanceClassesApi.md#updateNetworkApplianceTrafficShapingCustomPerformanceClass_2) | **PUT** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId} | Update a custom performance class for an MX network



## createNetworkApplianceTrafficShapingCustomPerformanceClass_2

> Object createNetworkApplianceTrafficShapingCustomPerformanceClass_2(networkId, createNetworkApplianceTrafficShapingCustomPerformanceClassRequest)

Add a custom performance class for an MX network

Add a custom performance class for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.CustomPerformanceClassesApi();
let networkId = "networkId_example"; // String | 
let createNetworkApplianceTrafficShapingCustomPerformanceClassRequest = new MerakiDashboardApi.CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest(); // CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest | 
apiInstance.createNetworkApplianceTrafficShapingCustomPerformanceClass_2(networkId, createNetworkApplianceTrafficShapingCustomPerformanceClassRequest, (error, data, response) => {
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
 **createNetworkApplianceTrafficShapingCustomPerformanceClassRequest** | [**CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest**](CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNetworkApplianceTrafficShapingCustomPerformanceClass_2

> deleteNetworkApplianceTrafficShapingCustomPerformanceClass_2(networkId, customPerformanceClassId)

Delete a custom performance class from an MX network

Delete a custom performance class from an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.CustomPerformanceClassesApi();
let networkId = "networkId_example"; // String | 
let customPerformanceClassId = "customPerformanceClassId_example"; // String | 
apiInstance.deleteNetworkApplianceTrafficShapingCustomPerformanceClass_2(networkId, customPerformanceClassId, (error, data, response) => {
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
 **customPerformanceClassId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNetworkApplianceTrafficShapingCustomPerformanceClass_2

> Object getNetworkApplianceTrafficShapingCustomPerformanceClass_2(networkId, customPerformanceClassId)

Return a custom performance class for an MX network

Return a custom performance class for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.CustomPerformanceClassesApi();
let networkId = "networkId_example"; // String | 
let customPerformanceClassId = "customPerformanceClassId_example"; // String | 
apiInstance.getNetworkApplianceTrafficShapingCustomPerformanceClass_2(networkId, customPerformanceClassId, (error, data, response) => {
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
 **customPerformanceClassId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceTrafficShapingCustomPerformanceClasses_2

> [Object] getNetworkApplianceTrafficShapingCustomPerformanceClasses_2(networkId)

List all custom performance classes for an MX network

List all custom performance classes for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.CustomPerformanceClassesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceTrafficShapingCustomPerformanceClasses_2(networkId, (error, data, response) => {
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


## updateNetworkApplianceTrafficShapingCustomPerformanceClass_2

> Object updateNetworkApplianceTrafficShapingCustomPerformanceClass_2(networkId, customPerformanceClassId, opts)

Update a custom performance class for an MX network

Update a custom performance class for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.CustomPerformanceClassesApi();
let networkId = "networkId_example"; // String | 
let customPerformanceClassId = "customPerformanceClassId_example"; // String | 
let opts = {
  'updateNetworkApplianceTrafficShapingCustomPerformanceClassRequest': new MerakiDashboardApi.UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest() // UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest | 
};
apiInstance.updateNetworkApplianceTrafficShapingCustomPerformanceClass_2(networkId, customPerformanceClassId, opts, (error, data, response) => {
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
 **customPerformanceClassId** | **String**|  | 
 **updateNetworkApplianceTrafficShapingCustomPerformanceClassRequest** | [**UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest**](UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

