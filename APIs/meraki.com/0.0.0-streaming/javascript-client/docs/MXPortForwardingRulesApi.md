# MerakiDashboardApi.MXPortForwardingRulesApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkPortForwardingRules**](MXPortForwardingRulesApi.md#getNetworkPortForwardingRules) | **GET** /networks/{networkId}/portForwardingRules | Return the port forwarding rules for an MX network
[**updateNetworkPortForwardingRules**](MXPortForwardingRulesApi.md#updateNetworkPortForwardingRules) | **PUT** /networks/{networkId}/portForwardingRules | Update the port forwarding rules for an MX network



## getNetworkPortForwardingRules

> Object getNetworkPortForwardingRules(networkId)

Return the port forwarding rules for an MX network

Return the port forwarding rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MXPortForwardingRulesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkPortForwardingRules(networkId, (error, data, response) => {
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


## updateNetworkPortForwardingRules

> Object updateNetworkPortForwardingRules(networkId, updateNetworkPortForwardingRulesRequest)

Update the port forwarding rules for an MX network

Update the port forwarding rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MXPortForwardingRulesApi();
let networkId = "networkId_example"; // String | 
let updateNetworkPortForwardingRulesRequest = new MerakiDashboardApi.UpdateNetworkPortForwardingRulesRequest(); // UpdateNetworkPortForwardingRulesRequest | 
apiInstance.updateNetworkPortForwardingRules(networkId, updateNetworkPortForwardingRulesRequest, (error, data, response) => {
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
 **updateNetworkPortForwardingRulesRequest** | [**UpdateNetworkPortForwardingRulesRequest**](UpdateNetworkPortForwardingRulesRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

