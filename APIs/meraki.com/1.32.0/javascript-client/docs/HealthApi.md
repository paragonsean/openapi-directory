# MerakiDashboardApi.HealthApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkHealthAlerts_1**](HealthApi.md#getNetworkHealthAlerts_1) | **GET** /networks/{networkId}/health/alerts | Return all global alerts on this network



## getNetworkHealthAlerts_1

> [GetNetworkHealthAlerts200ResponseInner] getNetworkHealthAlerts_1(networkId)

Return all global alerts on this network

Return all global alerts on this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.HealthApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkHealthAlerts_1(networkId, (error, data, response) => {
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

[**[GetNetworkHealthAlerts200ResponseInner]**](GetNetworkHealthAlerts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

