# MerakiDashboardApi.MRL3FirewallApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkSsidL3FirewallRules**](MRL3FirewallApi.md#getNetworkSsidL3FirewallRules) | **GET** /networks/{networkId}/ssids/{number}/l3FirewallRules | Return the L3 firewall rules for an SSID on an MR network
[**updateNetworkSsidL3FirewallRules**](MRL3FirewallApi.md#updateNetworkSsidL3FirewallRules) | **PUT** /networks/{networkId}/ssids/{number}/l3FirewallRules | Update the L3 firewall rules of an SSID on an MR network



## getNetworkSsidL3FirewallRules

> [Object] getNetworkSsidL3FirewallRules(networkId, number)

Return the L3 firewall rules for an SSID on an MR network

Return the L3 firewall rules for an SSID on an MR network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MRL3FirewallApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkSsidL3FirewallRules(networkId, number, (error, data, response) => {
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
 **number** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkSsidL3FirewallRules

> [Object] updateNetworkSsidL3FirewallRules(networkId, number, opts)

Update the L3 firewall rules of an SSID on an MR network

Update the L3 firewall rules of an SSID on an MR network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MRL3FirewallApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkSsidL3FirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkSsidL3FirewallRulesRequest() // UpdateNetworkSsidL3FirewallRulesRequest | 
};
apiInstance.updateNetworkSsidL3FirewallRules(networkId, number, opts, (error, data, response) => {
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
 **number** | **String**|  | 
 **updateNetworkSsidL3FirewallRulesRequest** | [**UpdateNetworkSsidL3FirewallRulesRequest**](UpdateNetworkSsidL3FirewallRulesRequest.md)|  | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

