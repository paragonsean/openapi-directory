# MerakiDashboardApi.BgpApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkApplianceVpnBgp_2**](BgpApi.md#getNetworkApplianceVpnBgp_2) | **GET** /networks/{networkId}/appliance/vpn/bgp | Return a Hub BGP Configuration
[**updateNetworkApplianceVpnBgp_2**](BgpApi.md#updateNetworkApplianceVpnBgp_2) | **PUT** /networks/{networkId}/appliance/vpn/bgp | Update a Hub BGP Configuration



## getNetworkApplianceVpnBgp_2

> Object getNetworkApplianceVpnBgp_2(networkId)

Return a Hub BGP Configuration

Return a Hub BGP Configuration

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.BgpApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceVpnBgp_2(networkId, (error, data, response) => {
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


## updateNetworkApplianceVpnBgp_2

> Object updateNetworkApplianceVpnBgp_2(networkId, updateNetworkApplianceVpnBgpRequest)

Update a Hub BGP Configuration

Update a Hub BGP Configuration

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.BgpApi();
let networkId = "networkId_example"; // String | 
let updateNetworkApplianceVpnBgpRequest = new MerakiDashboardApi.UpdateNetworkApplianceVpnBgpRequest(); // UpdateNetworkApplianceVpnBgpRequest | 
apiInstance.updateNetworkApplianceVpnBgp_2(networkId, updateNetworkApplianceVpnBgpRequest, (error, data, response) => {
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
 **updateNetworkApplianceVpnBgpRequest** | [**UpdateNetworkApplianceVpnBgpRequest**](UpdateNetworkApplianceVpnBgpRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

