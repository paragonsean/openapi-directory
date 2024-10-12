# MerakiDashboardApi.EventTypesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkEventsEventTypes_2**](EventTypesApi.md#getNetworkEventsEventTypes_2) | **GET** /networks/{networkId}/events/eventTypes | List the event type to human-readable description



## getNetworkEventsEventTypes_2

> [GetNetworkEventsEventTypes200ResponseInner] getNetworkEventsEventTypes_2(networkId)

List the event type to human-readable description

List the event type to human-readable description

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.EventTypesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkEventsEventTypes_2(networkId, (error, data, response) => {
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

[**[GetNetworkEventsEventTypes200ResponseInner]**](GetNetworkEventsEventTypes200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

