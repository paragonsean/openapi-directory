# MerakiDashboardApi.SingleLanApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkApplianceSingleLan_1**](SingleLanApi.md#getNetworkApplianceSingleLan_1) | **GET** /networks/{networkId}/appliance/singleLan | Return single LAN configuration
[**updateNetworkApplianceSingleLan_1**](SingleLanApi.md#updateNetworkApplianceSingleLan_1) | **PUT** /networks/{networkId}/appliance/singleLan | Update single LAN configuration



## getNetworkApplianceSingleLan_1

> GetNetworkApplianceSingleLan200Response getNetworkApplianceSingleLan_1(networkId)

Return single LAN configuration

Return single LAN configuration

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SingleLanApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceSingleLan_1(networkId, (error, data, response) => {
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

[**GetNetworkApplianceSingleLan200Response**](GetNetworkApplianceSingleLan200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkApplianceSingleLan_1

> GetNetworkApplianceSingleLan200Response updateNetworkApplianceSingleLan_1(networkId, opts)

Update single LAN configuration

Update single LAN configuration

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SingleLanApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceSingleLanRequest': new MerakiDashboardApi.UpdateNetworkApplianceSingleLanRequest() // UpdateNetworkApplianceSingleLanRequest | 
};
apiInstance.updateNetworkApplianceSingleLan_1(networkId, opts, (error, data, response) => {
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
 **updateNetworkApplianceSingleLanRequest** | [**UpdateNetworkApplianceSingleLanRequest**](UpdateNetworkApplianceSingleLanRequest.md)|  | [optional] 

### Return type

[**GetNetworkApplianceSingleLan200Response**](GetNetworkApplianceSingleLan200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

