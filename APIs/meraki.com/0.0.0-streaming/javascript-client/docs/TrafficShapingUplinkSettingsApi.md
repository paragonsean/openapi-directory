# MerakiDashboardApi.TrafficShapingUplinkSettingsApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkUplinkSettings**](TrafficShapingUplinkSettingsApi.md#getNetworkUplinkSettings) | **GET** /networks/{networkId}/uplinkSettings | Returns the uplink settings for your MX network.
[**updateNetworkUplinkSettings**](TrafficShapingUplinkSettingsApi.md#updateNetworkUplinkSettings) | **PUT** /networks/{networkId}/uplinkSettings | Updates the uplink settings for your MX network.



## getNetworkUplinkSettings

> Object getNetworkUplinkSettings(networkId)

Returns the uplink settings for your MX network.

Returns the uplink settings for your MX network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.TrafficShapingUplinkSettingsApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkUplinkSettings(networkId, (error, data, response) => {
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

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkUplinkSettings

> Object updateNetworkUplinkSettings(networkId, opts)

Updates the uplink settings for your MX network.

Updates the uplink settings for your MX network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.TrafficShapingUplinkSettingsApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkUplinkSettingsRequest': new MerakiDashboardApi.UpdateNetworkUplinkSettingsRequest() // UpdateNetworkUplinkSettingsRequest | 
};
apiInstance.updateNetworkUplinkSettings(networkId, opts, (error, data, response) => {
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
 **updateNetworkUplinkSettingsRequest** | [**UpdateNetworkUplinkSettingsRequest**](UpdateNetworkUplinkSettingsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

