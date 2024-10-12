# MerakiDashboardApi.WirelessSettingsApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkWirelessSettings**](WirelessSettingsApi.md#getNetworkWirelessSettings) | **GET** /networks/{networkId}/wireless/settings | Return the wireless settings for a network
[**updateNetworkWirelessSettings**](WirelessSettingsApi.md#updateNetworkWirelessSettings) | **PUT** /networks/{networkId}/wireless/settings | Update the wireless settings for a network



## getNetworkWirelessSettings

> Object getNetworkWirelessSettings(networkId)

Return the wireless settings for a network

Return the wireless settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessSettingsApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkWirelessSettings(networkId, (error, data, response) => {
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


## updateNetworkWirelessSettings

> Object updateNetworkWirelessSettings(networkId, opts)

Update the wireless settings for a network

Update the wireless settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessSettingsApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkWirelessSettingsRequest': new MerakiDashboardApi.UpdateNetworkWirelessSettingsRequest() // UpdateNetworkWirelessSettingsRequest | 
};
apiInstance.updateNetworkWirelessSettings(networkId, opts, (error, data, response) => {
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
 **updateNetworkWirelessSettingsRequest** | [**UpdateNetworkWirelessSettingsRequest**](UpdateNetworkWirelessSettingsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

