# MerakiDashboardApi.ApplicationCategoriesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkApplianceFirewallL7FirewallRulesApplicationCategories_3**](ApplicationCategoriesApi.md#getNetworkApplianceFirewallL7FirewallRulesApplicationCategories_3) | **GET** /networks/{networkId}/appliance/firewall/l7FirewallRules/applicationCategories | Return the L7 firewall application categories and their associated applications for an MX network
[**getNetworkTrafficShapingApplicationCategories_2**](ApplicationCategoriesApi.md#getNetworkTrafficShapingApplicationCategories_2) | **GET** /networks/{networkId}/trafficShaping/applicationCategories | Returns the application categories for traffic shaping rules.



## getNetworkApplianceFirewallL7FirewallRulesApplicationCategories_3

> Object getNetworkApplianceFirewallL7FirewallRulesApplicationCategories_3(networkId)

Return the L7 firewall application categories and their associated applications for an MX network

Return the L7 firewall application categories and their associated applications for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ApplicationCategoriesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallL7FirewallRulesApplicationCategories_3(networkId, (error, data, response) => {
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


## getNetworkTrafficShapingApplicationCategories_2

> Object getNetworkTrafficShapingApplicationCategories_2(networkId)

Returns the application categories for traffic shaping rules.

Returns the application categories for traffic shaping rules.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ApplicationCategoriesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkTrafficShapingApplicationCategories_2(networkId, (error, data, response) => {
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

