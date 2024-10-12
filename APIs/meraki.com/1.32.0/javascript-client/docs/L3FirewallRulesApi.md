# MerakiDashboardApi.L3FirewallRulesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkApplianceFirewallL3FirewallRules_2**](L3FirewallRulesApi.md#getNetworkApplianceFirewallL3FirewallRules_2) | **GET** /networks/{networkId}/appliance/firewall/l3FirewallRules | Return the L3 firewall rules for an MX network
[**getNetworkWirelessSsidFirewallL3FirewallRules_3**](L3FirewallRulesApi.md#getNetworkWirelessSsidFirewallL3FirewallRules_3) | **GET** /networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules | Return the L3 firewall rules for an SSID on an MR network
[**updateNetworkApplianceFirewallL3FirewallRules_2**](L3FirewallRulesApi.md#updateNetworkApplianceFirewallL3FirewallRules_2) | **PUT** /networks/{networkId}/appliance/firewall/l3FirewallRules | Update the L3 firewall rules of an MX network
[**updateNetworkWirelessSsidFirewallL3FirewallRules_3**](L3FirewallRulesApi.md#updateNetworkWirelessSsidFirewallL3FirewallRules_3) | **PUT** /networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules | Update the L3 firewall rules of an SSID on an MR network



## getNetworkApplianceFirewallL3FirewallRules_2

> Object getNetworkApplianceFirewallL3FirewallRules_2(networkId)

Return the L3 firewall rules for an MX network

Return the L3 firewall rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.L3FirewallRulesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallL3FirewallRules_2(networkId, (error, data, response) => {
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


## getNetworkWirelessSsidFirewallL3FirewallRules_3

> Object getNetworkWirelessSsidFirewallL3FirewallRules_3(networkId, number)

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

let apiInstance = new MerakiDashboardApi.L3FirewallRulesApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidFirewallL3FirewallRules_3(networkId, number, (error, data, response) => {
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

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkApplianceFirewallL3FirewallRules_2

> Object updateNetworkApplianceFirewallL3FirewallRules_2(networkId, opts)

Update the L3 firewall rules of an MX network

Update the L3 firewall rules of an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.L3FirewallRulesApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceFirewallInboundFirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkApplianceFirewallInboundFirewallRulesRequest() // UpdateNetworkApplianceFirewallInboundFirewallRulesRequest | 
};
apiInstance.updateNetworkApplianceFirewallL3FirewallRules_2(networkId, opts, (error, data, response) => {
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
 **updateNetworkApplianceFirewallInboundFirewallRulesRequest** | [**UpdateNetworkApplianceFirewallInboundFirewallRulesRequest**](UpdateNetworkApplianceFirewallInboundFirewallRulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidFirewallL3FirewallRules_3

> Object updateNetworkWirelessSsidFirewallL3FirewallRules_3(networkId, number, opts)

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

let apiInstance = new MerakiDashboardApi.L3FirewallRulesApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidFirewallL3FirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest() // UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest | 
};
apiInstance.updateNetworkWirelessSsidFirewallL3FirewallRules_3(networkId, number, opts, (error, data, response) => {
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
 **updateNetworkWirelessSsidFirewallL3FirewallRulesRequest** | [**UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest**](UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

