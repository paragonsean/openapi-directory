# MerakiDashboardApi.MXCellularFirewallApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkCellularFirewallRules**](MXCellularFirewallApi.md#getNetworkCellularFirewallRules) | **GET** /networks/{networkId}/cellularFirewallRules | Return the cellular firewall rules for an MX network
[**updateNetworkCellularFirewallRules**](MXCellularFirewallApi.md#updateNetworkCellularFirewallRules) | **PUT** /networks/{networkId}/cellularFirewallRules | Update the cellular firewall rules of an MX network



## getNetworkCellularFirewallRules

> [Object] getNetworkCellularFirewallRules(networkId)

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

let apiInstance = new MerakiDashboardApi.MXCellularFirewallApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkCellularFirewallRules(networkId, (error, data, response) => {
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


## updateNetworkCellularFirewallRules

> [Object] updateNetworkCellularFirewallRules(networkId, opts)

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

let apiInstance = new MerakiDashboardApi.MXCellularFirewallApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkCellularFirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkCellularFirewallRulesRequest() // UpdateNetworkCellularFirewallRulesRequest | 
};
apiInstance.updateNetworkCellularFirewallRules(networkId, opts, (error, data, response) => {
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
 **updateNetworkCellularFirewallRulesRequest** | [**UpdateNetworkCellularFirewallRulesRequest**](UpdateNetworkCellularFirewallRulesRequest.md)|  | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

