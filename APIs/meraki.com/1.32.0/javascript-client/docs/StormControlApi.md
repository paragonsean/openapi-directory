# MerakiDashboardApi.StormControlApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkSwitchStormControl_1**](StormControlApi.md#getNetworkSwitchStormControl_1) | **GET** /networks/{networkId}/switch/stormControl | Return the storm control configuration for a switch network
[**updateNetworkSwitchStormControl_1**](StormControlApi.md#updateNetworkSwitchStormControl_1) | **PUT** /networks/{networkId}/switch/stormControl | Update the storm control configuration for a switch network



## getNetworkSwitchStormControl_1

> GetNetworkSwitchStormControl200Response getNetworkSwitchStormControl_1(networkId)

Return the storm control configuration for a switch network

Return the storm control configuration for a switch network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.StormControlApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchStormControl_1(networkId, (error, data, response) => {
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

[**GetNetworkSwitchStormControl200Response**](GetNetworkSwitchStormControl200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkSwitchStormControl_1

> Object updateNetworkSwitchStormControl_1(networkId, opts)

Update the storm control configuration for a switch network

Update the storm control configuration for a switch network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.StormControlApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkSwitchStormControlRequest': new MerakiDashboardApi.UpdateNetworkSwitchStormControlRequest() // UpdateNetworkSwitchStormControlRequest | 
};
apiInstance.updateNetworkSwitchStormControl_1(networkId, opts, (error, data, response) => {
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
 **updateNetworkSwitchStormControlRequest** | [**UpdateNetworkSwitchStormControlRequest**](UpdateNetworkSwitchStormControlRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

