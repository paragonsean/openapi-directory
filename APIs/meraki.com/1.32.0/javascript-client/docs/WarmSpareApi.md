# MerakiDashboardApi.WarmSpareApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeviceSwitchWarmSpare_1**](WarmSpareApi.md#getDeviceSwitchWarmSpare_1) | **GET** /devices/{serial}/switch/warmSpare | Return warm spare configuration for a switch
[**getNetworkApplianceWarmSpare_1**](WarmSpareApi.md#getNetworkApplianceWarmSpare_1) | **GET** /networks/{networkId}/appliance/warmSpare | Return MX warm spare settings
[**swapNetworkApplianceWarmSpare_1**](WarmSpareApi.md#swapNetworkApplianceWarmSpare_1) | **POST** /networks/{networkId}/appliance/warmSpare/swap | Swap MX primary and warm spare appliances
[**updateDeviceSwitchWarmSpare_1**](WarmSpareApi.md#updateDeviceSwitchWarmSpare_1) | **PUT** /devices/{serial}/switch/warmSpare | Update warm spare configuration for a switch
[**updateNetworkApplianceWarmSpare_1**](WarmSpareApi.md#updateNetworkApplianceWarmSpare_1) | **PUT** /networks/{networkId}/appliance/warmSpare | Update MX warm spare settings



## getDeviceSwitchWarmSpare_1

> Object getDeviceSwitchWarmSpare_1(serial)

Return warm spare configuration for a switch

Return warm spare configuration for a switch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WarmSpareApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceSwitchWarmSpare_1(serial, (error, data, response) => {
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
 **serial** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceWarmSpare_1

> Object getNetworkApplianceWarmSpare_1(networkId)

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

let apiInstance = new MerakiDashboardApi.WarmSpareApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceWarmSpare_1(networkId, (error, data, response) => {
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


## swapNetworkApplianceWarmSpare_1

> Object swapNetworkApplianceWarmSpare_1(networkId)

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

let apiInstance = new MerakiDashboardApi.WarmSpareApi();
let networkId = "networkId_example"; // String | 
apiInstance.swapNetworkApplianceWarmSpare_1(networkId, (error, data, response) => {
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


## updateDeviceSwitchWarmSpare_1

> Object updateDeviceSwitchWarmSpare_1(serial, updateDeviceSwitchWarmSpareRequest)

Update warm spare configuration for a switch

Update warm spare configuration for a switch. The spare will use the same L3 configuration as the primary. Note that this will irreversibly destroy any existing L3 configuration on the spare.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WarmSpareApi();
let serial = "serial_example"; // String | 
let updateDeviceSwitchWarmSpareRequest = new MerakiDashboardApi.UpdateDeviceSwitchWarmSpareRequest(); // UpdateDeviceSwitchWarmSpareRequest | 
apiInstance.updateDeviceSwitchWarmSpare_1(serial, updateDeviceSwitchWarmSpareRequest, (error, data, response) => {
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
 **serial** | **String**|  | 
 **updateDeviceSwitchWarmSpareRequest** | [**UpdateDeviceSwitchWarmSpareRequest**](UpdateDeviceSwitchWarmSpareRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceWarmSpare_1

> Object updateNetworkApplianceWarmSpare_1(networkId, updateNetworkApplianceWarmSpareRequest)

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

let apiInstance = new MerakiDashboardApi.WarmSpareApi();
let networkId = "networkId_example"; // String | 
let updateNetworkApplianceWarmSpareRequest = new MerakiDashboardApi.UpdateNetworkApplianceWarmSpareRequest(); // UpdateNetworkApplianceWarmSpareRequest | 
apiInstance.updateNetworkApplianceWarmSpare_1(networkId, updateNetworkApplianceWarmSpareRequest, (error, data, response) => {
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
 **updateNetworkApplianceWarmSpareRequest** | [**UpdateNetworkApplianceWarmSpareRequest**](UpdateNetworkApplianceWarmSpareRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

