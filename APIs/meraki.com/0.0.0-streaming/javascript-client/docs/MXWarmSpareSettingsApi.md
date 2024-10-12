# MerakiDashboardApi.MXWarmSpareSettingsApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkWarmSpareSettings**](MXWarmSpareSettingsApi.md#getNetworkWarmSpareSettings) | **GET** /networks/{networkId}/warmSpareSettings | Return MX warm spare settings
[**swapNetworkWarmSpare**](MXWarmSpareSettingsApi.md#swapNetworkWarmSpare) | **POST** /networks/{networkId}/swapWarmSpare | Swap MX primary and warm spare appliances
[**updateNetworkWarmSpareSettings**](MXWarmSpareSettingsApi.md#updateNetworkWarmSpareSettings) | **PUT** /networks/{networkId}/warmSpareSettings | Update MX warm spare settings



## getNetworkWarmSpareSettings

> Object getNetworkWarmSpareSettings(networkId)

Return MX warm spare settings

Return MX warm spare settings

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MXWarmSpareSettingsApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkWarmSpareSettings(networkId, (error, data, response) => {
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


## swapNetworkWarmSpare

> Object swapNetworkWarmSpare(networkId)

Swap MX primary and warm spare appliances

Swap MX primary and warm spare appliances

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MXWarmSpareSettingsApi();
let networkId = "networkId_example"; // String | 
apiInstance.swapNetworkWarmSpare(networkId, (error, data, response) => {
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


## updateNetworkWarmSpareSettings

> Object updateNetworkWarmSpareSettings(networkId, updateNetworkWarmSpareSettingsRequest)

Update MX warm spare settings

Update MX warm spare settings

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MXWarmSpareSettingsApi();
let networkId = "networkId_example"; // String | 
let updateNetworkWarmSpareSettingsRequest = new MerakiDashboardApi.UpdateNetworkWarmSpareSettingsRequest(); // UpdateNetworkWarmSpareSettingsRequest | 
apiInstance.updateNetworkWarmSpareSettings(networkId, updateNetworkWarmSpareSettingsRequest, (error, data, response) => {
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
 **updateNetworkWarmSpareSettingsRequest** | [**UpdateNetworkWarmSpareSettingsRequest**](UpdateNetworkWarmSpareSettingsRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

