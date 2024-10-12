# MerakiDashboardApi.MXVPNFirewallApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOrganizationVpnFirewallRules**](MXVPNFirewallApi.md#getOrganizationVpnFirewallRules) | **GET** /organizations/{organizationId}/vpnFirewallRules | Return the firewall rules for an organization&#39;s site-to-site VPN
[**updateOrganizationVpnFirewallRules**](MXVPNFirewallApi.md#updateOrganizationVpnFirewallRules) | **PUT** /organizations/{organizationId}/vpnFirewallRules | Update the firewall rules of an organization&#39;s site-to-site VPN



## getOrganizationVpnFirewallRules

> [Object] getOrganizationVpnFirewallRules(organizationId)

Return the firewall rules for an organization&#39;s site-to-site VPN

Return the firewall rules for an organization&#39;s site-to-site VPN

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MXVPNFirewallApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationVpnFirewallRules(organizationId, (error, data, response) => {
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
 **organizationId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateOrganizationVpnFirewallRules

> [Object] updateOrganizationVpnFirewallRules(organizationId, opts)

Update the firewall rules of an organization&#39;s site-to-site VPN

Update the firewall rules of an organization&#39;s site-to-site VPN

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MXVPNFirewallApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'updateOrganizationVpnFirewallRulesRequest': new MerakiDashboardApi.UpdateOrganizationVpnFirewallRulesRequest() // UpdateOrganizationVpnFirewallRulesRequest | 
};
apiInstance.updateOrganizationVpnFirewallRules(organizationId, opts, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **updateOrganizationVpnFirewallRulesRequest** | [**UpdateOrganizationVpnFirewallRulesRequest**](UpdateOrganizationVpnFirewallRulesRequest.md)|  | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

