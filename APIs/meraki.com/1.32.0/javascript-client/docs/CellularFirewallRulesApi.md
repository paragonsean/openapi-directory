# MerakiDashboardApi.CellularFirewallRulesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkApplianceFirewallCellularFirewallRules_2**](CellularFirewallRulesApi.md#getNetworkApplianceFirewallCellularFirewallRules_2) | **GET** /networks/{networkId}/appliance/firewall/cellularFirewallRules | Return the cellular firewall rules for an MX network
[**updateNetworkApplianceFirewallCellularFirewallRules_2**](CellularFirewallRulesApi.md#updateNetworkApplianceFirewallCellularFirewallRules_2) | **PUT** /networks/{networkId}/appliance/firewall/cellularFirewallRules | Update the cellular firewall rules of an MX network



## getNetworkApplianceFirewallCellularFirewallRules_2

> Object getNetworkApplianceFirewallCellularFirewallRules_2(networkId)

Return the cellular firewall rules for an MX network

Return the cellular firewall rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.CellularFirewallRulesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallCellularFirewallRules_2(networkId, (error, data, response) => {
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


## updateNetworkApplianceFirewallCellularFirewallRules_2

> Object updateNetworkApplianceFirewallCellularFirewallRules_2(networkId, opts)

Update the cellular firewall rules of an MX network

Update the cellular firewall rules of an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.CellularFirewallRulesApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceFirewallCellularFirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkApplianceFirewallCellularFirewallRulesRequest() // UpdateNetworkApplianceFirewallCellularFirewallRulesRequest | 
};
apiInstance.updateNetworkApplianceFirewallCellularFirewallRules_2(networkId, opts, (error, data, response) => {
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

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

