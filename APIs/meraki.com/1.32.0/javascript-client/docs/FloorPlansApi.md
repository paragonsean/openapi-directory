# MerakiDashboardApi.FloorPlansApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkFloorPlan_1**](FloorPlansApi.md#createNetworkFloorPlan_1) | **POST** /networks/{networkId}/floorPlans | Upload a floor plan
[**deleteNetworkFloorPlan_1**](FloorPlansApi.md#deleteNetworkFloorPlan_1) | **DELETE** /networks/{networkId}/floorPlans/{floorPlanId} | Destroy a floor plan
[**getNetworkFloorPlan_1**](FloorPlansApi.md#getNetworkFloorPlan_1) | **GET** /networks/{networkId}/floorPlans/{floorPlanId} | Find a floor plan by ID
[**getNetworkFloorPlans_1**](FloorPlansApi.md#getNetworkFloorPlans_1) | **GET** /networks/{networkId}/floorPlans | List the floor plans that belong to your network
[**updateNetworkFloorPlan_1**](FloorPlansApi.md#updateNetworkFloorPlan_1) | **PUT** /networks/{networkId}/floorPlans/{floorPlanId} | Update a floor plan&#39;s geolocation and other meta data



## createNetworkFloorPlan_1

> Object createNetworkFloorPlan_1(networkId, createNetworkFloorPlanRequest)

Upload a floor plan

Upload a floor plan

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FloorPlansApi();
let networkId = "networkId_example"; // String | 
let createNetworkFloorPlanRequest = new MerakiDashboardApi.CreateNetworkFloorPlanRequest(); // CreateNetworkFloorPlanRequest | 
apiInstance.createNetworkFloorPlan_1(networkId, createNetworkFloorPlanRequest, (error, data, response) => {
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
 **createNetworkFloorPlanRequest** | [**CreateNetworkFloorPlanRequest**](CreateNetworkFloorPlanRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNetworkFloorPlan_1

> deleteNetworkFloorPlan_1(networkId, floorPlanId)

Destroy a floor plan

Destroy a floor plan

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FloorPlansApi();
let networkId = "networkId_example"; // String | 
let floorPlanId = "floorPlanId_example"; // String | 
apiInstance.deleteNetworkFloorPlan_1(networkId, floorPlanId, (error, data, response) => {
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
 **floorPlanId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNetworkFloorPlan_1

> Object getNetworkFloorPlan_1(networkId, floorPlanId)

Find a floor plan by ID

Find a floor plan by ID

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FloorPlansApi();
let networkId = "networkId_example"; // String | 
let floorPlanId = "floorPlanId_example"; // String | 
apiInstance.getNetworkFloorPlan_1(networkId, floorPlanId, (error, data, response) => {
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
 **floorPlanId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkFloorPlans_1

> [Object] getNetworkFloorPlans_1(networkId)

List the floor plans that belong to your network

List the floor plans that belong to your network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FloorPlansApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkFloorPlans_1(networkId, (error, data, response) => {
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


## updateNetworkFloorPlan_1

> Object updateNetworkFloorPlan_1(networkId, floorPlanId, opts)

Update a floor plan&#39;s geolocation and other meta data

Update a floor plan&#39;s geolocation and other meta data

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FloorPlansApi();
let networkId = "networkId_example"; // String | 
let floorPlanId = "floorPlanId_example"; // String | 
let opts = {
  'updateNetworkFloorPlanRequest': new MerakiDashboardApi.UpdateNetworkFloorPlanRequest() // UpdateNetworkFloorPlanRequest | 
};
apiInstance.updateNetworkFloorPlan_1(networkId, floorPlanId, opts, (error, data, response) => {
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
 **floorPlanId** | **String**|  | 
 **updateNetworkFloorPlanRequest** | [**UpdateNetworkFloorPlanRequest**](UpdateNetworkFloorPlanRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

