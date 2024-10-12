# MerakiDashboardApi.SwitchPortSchedulesApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkSwitchPortSchedule**](SwitchPortSchedulesApi.md#createNetworkSwitchPortSchedule) | **POST** /networks/{networkId}/switch/portSchedules | Add a switch port schedule
[**deleteNetworkSwitchPortSchedule**](SwitchPortSchedulesApi.md#deleteNetworkSwitchPortSchedule) | **DELETE** /networks/{networkId}/switch/portSchedules/{portScheduleId} | Delete a switch port schedule
[**getNetworkSwitchPortSchedules**](SwitchPortSchedulesApi.md#getNetworkSwitchPortSchedules) | **GET** /networks/{networkId}/switch/portSchedules | List switch port schedules
[**updateNetworkSwitchPortSchedule**](SwitchPortSchedulesApi.md#updateNetworkSwitchPortSchedule) | **PUT** /networks/{networkId}/switch/portSchedules/{portScheduleId} | Update a switch port schedule



## createNetworkSwitchPortSchedule

> Object createNetworkSwitchPortSchedule(networkId, createNetworkSwitchPortScheduleRequest)

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

let apiInstance = new MerakiDashboardApi.SwitchPortSchedulesApi();
let networkId = "networkId_example"; // String | 
let createNetworkSwitchPortScheduleRequest = new MerakiDashboardApi.CreateNetworkSwitchPortScheduleRequest(); // CreateNetworkSwitchPortScheduleRequest | 
apiInstance.createNetworkSwitchPortSchedule(networkId, createNetworkSwitchPortScheduleRequest, (error, data, response) => {
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


## deleteNetworkSwitchPortSchedule

> deleteNetworkSwitchPortSchedule(networkId, portScheduleId)

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

let apiInstance = new MerakiDashboardApi.SwitchPortSchedulesApi();
let networkId = "networkId_example"; // String | 
let portScheduleId = "portScheduleId_example"; // String | 
apiInstance.deleteNetworkSwitchPortSchedule(networkId, portScheduleId, (error, data, response) => {
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


## getNetworkSwitchPortSchedules

> [Object] getNetworkSwitchPortSchedules(networkId)

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

let apiInstance = new MerakiDashboardApi.SwitchPortSchedulesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchPortSchedules(networkId, (error, data, response) => {
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


## updateNetworkSwitchPortSchedule

> Object updateNetworkSwitchPortSchedule(networkId, portScheduleId, opts)

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

let apiInstance = new MerakiDashboardApi.SwitchPortSchedulesApi();
let networkId = "networkId_example"; // String | 
let portScheduleId = "portScheduleId_example"; // String | 
let opts = {
  'updateNetworkSwitchPortScheduleRequest': new MerakiDashboardApi.UpdateNetworkSwitchPortScheduleRequest() // UpdateNetworkSwitchPortScheduleRequest | 
};
apiInstance.updateNetworkSwitchPortSchedule(networkId, portScheduleId, opts, (error, data, response) => {
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

