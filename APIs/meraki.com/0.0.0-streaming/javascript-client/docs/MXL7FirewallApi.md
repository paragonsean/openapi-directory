# MerakiDashboardApi.MXL7FirewallApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkL7FirewallRules**](MXL7FirewallApi.md#getNetworkL7FirewallRules) | **GET** /networks/{networkId}/l7FirewallRules | List the MX L7 firewall rules for an MX network
[**updateNetworkL7FirewallRules**](MXL7FirewallApi.md#updateNetworkL7FirewallRules) | **PUT** /networks/{networkId}/l7FirewallRules | Update the MX L7 firewall rules for an MX network



## getNetworkL7FirewallRules

> Object getNetworkL7FirewallRules(networkId)

List the MX L7 firewall rules for an MX network

List the MX L7 firewall rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MXL7FirewallApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkL7FirewallRules(networkId, (error, data, response) => {
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


## updateNetworkL7FirewallRules

> Object updateNetworkL7FirewallRules(networkId, opts)

Update the MX L7 firewall rules for an MX network

Update the MX L7 firewall rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MXL7FirewallApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkL7FirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkL7FirewallRulesRequest() // UpdateNetworkL7FirewallRulesRequest | 
};
apiInstance.updateNetworkL7FirewallRules(networkId, opts, (error, data, response) => {
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
 **updateNetworkL7FirewallRulesRequest** | [**UpdateNetworkL7FirewallRulesRequest**](UpdateNetworkL7FirewallRulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

