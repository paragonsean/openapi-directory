# MerakiDashboardApi.MX1ManyNATRulesApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkOneToManyNatRules**](MX1ManyNATRulesApi.md#getNetworkOneToManyNatRules) | **GET** /networks/{networkId}/oneToManyNatRules | Return the 1:Many NAT mapping rules for an MX network
[**updateNetworkOneToManyNatRules**](MX1ManyNATRulesApi.md#updateNetworkOneToManyNatRules) | **PUT** /networks/{networkId}/oneToManyNatRules | Set the 1:Many NAT mapping rules for an MX network



## getNetworkOneToManyNatRules

> Object getNetworkOneToManyNatRules(networkId)

Return the 1:Many NAT mapping rules for an MX network

Return the 1:Many NAT mapping rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MX1ManyNATRulesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkOneToManyNatRules(networkId, (error, data, response) => {
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


## updateNetworkOneToManyNatRules

> Object updateNetworkOneToManyNatRules(networkId, updateNetworkOneToManyNatRulesRequest)

Set the 1:Many NAT mapping rules for an MX network

Set the 1:Many NAT mapping rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MX1ManyNATRulesApi();
let networkId = "networkId_example"; // String | 
let updateNetworkOneToManyNatRulesRequest = new MerakiDashboardApi.UpdateNetworkOneToManyNatRulesRequest(); // UpdateNetworkOneToManyNatRulesRequest | 
apiInstance.updateNetworkOneToManyNatRules(networkId, updateNetworkOneToManyNatRulesRequest, (error, data, response) => {
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
 **updateNetworkOneToManyNatRulesRequest** | [**UpdateNetworkOneToManyNatRulesRequest**](UpdateNetworkOneToManyNatRulesRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

