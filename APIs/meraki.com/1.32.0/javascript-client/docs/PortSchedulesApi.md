# MerakiDashboardApi.PortSchedulesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkSwitchPortSchedule_1**](PortSchedulesApi.md#createNetworkSwitchPortSchedule_1) | **POST** /networks/{networkId}/switch/portSchedules | Add a switch port schedule
[**deleteNetworkSwitchPortSchedule_1**](PortSchedulesApi.md#deleteNetworkSwitchPortSchedule_1) | **DELETE** /networks/{networkId}/switch/portSchedules/{portScheduleId} | Delete a switch port schedule
[**getNetworkSwitchPortSchedules_1**](PortSchedulesApi.md#getNetworkSwitchPortSchedules_1) | **GET** /networks/{networkId}/switch/portSchedules | List switch port schedules
[**updateNetworkSwitchPortSchedule_1**](PortSchedulesApi.md#updateNetworkSwitchPortSchedule_1) | **PUT** /networks/{networkId}/switch/portSchedules/{portScheduleId} | Update a switch port schedule



## createNetworkSwitchPortSchedule_1

> Object createNetworkSwitchPortSchedule_1(networkId, createNetworkSwitchPortScheduleRequest)

Add a switch port schedule

Add a switch port schedule

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.PortSchedulesApi();
let networkId = "networkId_example"; // String | 
let createNetworkSwitchPortScheduleRequest = new MerakiDashboardApi.CreateNetworkSwitchPortScheduleRequest(); // CreateNetworkSwitchPortScheduleRequest | 
apiInstance.createNetworkSwitchPortSchedule_1(networkId, createNetworkSwitchPortScheduleRequest, (error, data, response) => {
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
 **createNetworkSwitchPortScheduleRequest** | [**CreateNetworkSwitchPortScheduleRequest**](CreateNetworkSwitchPortScheduleRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNetworkSwitchPortSchedule_1

> deleteNetworkSwitchPortSchedule_1(networkId, portScheduleId)

Delete a switch port schedule

Delete a switch port schedule

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.PortSchedulesApi();
let networkId = "networkId_example"; // String | 
let portScheduleId = "portScheduleId_example"; // String | 
apiInstance.deleteNetworkSwitchPortSchedule_1(networkId, portScheduleId, (error, data, response) => {
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
 **portScheduleId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNetworkSwitchPortSchedules_1

> [Object] getNetworkSwitchPortSchedules_1(networkId)

List switch port schedules

List switch port schedules

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.PortSchedulesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchPortSchedules_1(networkId, (error, data, response) => {
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


## updateNetworkSwitchPortSchedule_1

> Object updateNetworkSwitchPortSchedule_1(networkId, portScheduleId, opts)

Update a switch port schedule

Update a switch port schedule

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.PortSchedulesApi();
let networkId = "networkId_example"; // String | 
let portScheduleId = "portScheduleId_example"; // String | 
let opts = {
  'updateNetworkSwitchPortScheduleRequest': new MerakiDashboardApi.UpdateNetworkSwitchPortScheduleRequest() // UpdateNetworkSwitchPortScheduleRequest | 
};
apiInstance.updateNetworkSwitchPortSchedule_1(networkId, portScheduleId, opts, (error, data, response) => {
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
 **portScheduleId** | **String**|  | 
 **updateNetworkSwitchPortScheduleRequest** | [**UpdateNetworkSwitchPortScheduleRequest**](UpdateNetworkSwitchPortScheduleRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

