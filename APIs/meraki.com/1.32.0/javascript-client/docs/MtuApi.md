# MerakiDashboardApi.MtuApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkSwitchMtu_1**](MtuApi.md#getNetworkSwitchMtu_1) | **GET** /networks/{networkId}/switch/mtu | Return the MTU configuration
[**updateNetworkSwitchMtu_1**](MtuApi.md#updateNetworkSwitchMtu_1) | **PUT** /networks/{networkId}/switch/mtu | Update the MTU configuration



## getNetworkSwitchMtu_1

> GetNetworkSwitchMtu200Response getNetworkSwitchMtu_1(networkId)

Return the MTU configuration

Return the MTU configuration

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MtuApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchMtu_1(networkId, (error, data, response) => {
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

[**GetNetworkSwitchMtu200Response**](GetNetworkSwitchMtu200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkSwitchMtu_1

> Object updateNetworkSwitchMtu_1(networkId, opts)

Update the MTU configuration

Update the MTU configuration

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MtuApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkSwitchMtuRequest': new MerakiDashboardApi.UpdateNetworkSwitchMtuRequest() // UpdateNetworkSwitchMtuRequest | 
};
apiInstance.updateNetworkSwitchMtu_1(networkId, opts, (error, data, response) => {
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
 **updateNetworkSwitchMtuRequest** | [**UpdateNetworkSwitchMtuRequest**](UpdateNetworkSwitchMtuRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

