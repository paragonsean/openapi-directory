# MerakiDashboardApi.InboundCellularFirewallRulesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkApplianceFirewallInboundCellularFirewallRules_2**](InboundCellularFirewallRulesApi.md#getNetworkApplianceFirewallInboundCellularFirewallRules_2) | **GET** /networks/{networkId}/appliance/firewall/inboundCellularFirewallRules | Return the inbound cellular firewall rules for an MX network
[**updateNetworkApplianceFirewallInboundCellularFirewallRules_2**](InboundCellularFirewallRulesApi.md#updateNetworkApplianceFirewallInboundCellularFirewallRules_2) | **PUT** /networks/{networkId}/appliance/firewall/inboundCellularFirewallRules | Update the inbound cellular firewall rules of an MX network



## getNetworkApplianceFirewallInboundCellularFirewallRules_2

> [Object] getNetworkApplianceFirewallInboundCellularFirewallRules_2(networkId)

Return the inbound cellular firewall rules for an MX network

Return the inbound cellular firewall rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.InboundCellularFirewallRulesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallInboundCellularFirewallRules_2(networkId, (error, data, response) => {
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

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkApplianceFirewallInboundCellularFirewallRules_2

> [Object] updateNetworkApplianceFirewallInboundCellularFirewallRules_2(networkId, opts)

Update the inbound cellular firewall rules of an MX network

Update the inbound cellular firewall rules of an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.InboundCellularFirewallRulesApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceFirewallCellularFirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkApplianceFirewallCellularFirewallRulesRequest() // UpdateNetworkApplianceFirewallCellularFirewallRulesRequest | 
};
apiInstance.updateNetworkApplianceFirewallInboundCellularFirewallRules_2(networkId, opts, (error, data, response) => {
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
 **updateNetworkApplianceFirewallCellularFirewallRulesRequest** | [**UpdateNetworkApplianceFirewallCellularFirewallRulesRequest**](UpdateNetworkApplianceFirewallCellularFirewallRulesRequest.md)|  | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

