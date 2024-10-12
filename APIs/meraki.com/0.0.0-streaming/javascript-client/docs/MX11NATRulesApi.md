# MerakiDashboardApi.MX11NATRulesApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkOneToOneNatRules**](MX11NATRulesApi.md#getNetworkOneToOneNatRules) | **GET** /networks/{networkId}/oneToOneNatRules | Return the 1:1 NAT mapping rules for an MX network
[**updateNetworkOneToOneNatRules**](MX11NATRulesApi.md#updateNetworkOneToOneNatRules) | **PUT** /networks/{networkId}/oneToOneNatRules | Set the 1:1 NAT mapping rules for an MX network



## getNetworkOneToOneNatRules

> Object getNetworkOneToOneNatRules(networkId)

Return the 1:1 NAT mapping rules for an MX network

Return the 1:1 NAT mapping rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MX11NATRulesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkOneToOneNatRules(networkId, (error, data, response) => {
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


## updateNetworkOneToOneNatRules

> Object updateNetworkOneToOneNatRules(networkId, updateNetworkOneToOneNatRulesRequest)

Set the 1:1 NAT mapping rules for an MX network

Set the 1:1 NAT mapping rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MX11NATRulesApi();
let networkId = "networkId_example"; // String | 
let updateNetworkOneToOneNatRulesRequest = new MerakiDashboardApi.UpdateNetworkOneToOneNatRulesRequest(); // UpdateNetworkOneToOneNatRulesRequest | 
apiInstance.updateNetworkOneToOneNatRules(networkId, updateNetworkOneToOneNatRulesRequest, (error, data, response) => {
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
 **updateNetworkOneToOneNatRulesRequest** | [**UpdateNetworkOneToOneNatRulesRequest**](UpdateNetworkOneToOneNatRulesRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

