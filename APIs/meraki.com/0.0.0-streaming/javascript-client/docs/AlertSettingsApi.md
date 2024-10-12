# MerakiDashboardApi.AlertSettingsApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkAlertSettings**](AlertSettingsApi.md#getNetworkAlertSettings) | **GET** /networks/{networkId}/alertSettings | Return the alert configuration for this network
[**updateNetworkAlertSettings**](AlertSettingsApi.md#updateNetworkAlertSettings) | **PUT** /networks/{networkId}/alertSettings | Update the alert configuration for this network



## getNetworkAlertSettings

> Object getNetworkAlertSettings(networkId)

Return the alert configuration for this network

Return the alert configuration for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AlertSettingsApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkAlertSettings(networkId, (error, data, response) => {
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


## updateNetworkAlertSettings

> Object updateNetworkAlertSettings(networkId, opts)

Update the alert configuration for this network

Update the alert configuration for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AlertSettingsApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkAlertSettingsRequest': new MerakiDashboardApi.UpdateNetworkAlertSettingsRequest() // UpdateNetworkAlertSettingsRequest | 
};
apiInstance.updateNetworkAlertSettings(networkId, opts, (error, data, response) => {
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
 **updateNetworkAlertSettingsRequest** | [**UpdateNetworkAlertSettingsRequest**](UpdateNetworkAlertSettingsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

