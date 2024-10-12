# MerakiDashboardApi.SiteToSiteVpnApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkApplianceVpnSiteToSiteVpn_2**](SiteToSiteVpnApi.md#getNetworkApplianceVpnSiteToSiteVpn_2) | **GET** /networks/{networkId}/appliance/vpn/siteToSiteVpn | Return the site-to-site VPN settings of a network
[**updateNetworkApplianceVpnSiteToSiteVpn_2**](SiteToSiteVpnApi.md#updateNetworkApplianceVpnSiteToSiteVpn_2) | **PUT** /networks/{networkId}/appliance/vpn/siteToSiteVpn | Update the site-to-site VPN settings of a network



## getNetworkApplianceVpnSiteToSiteVpn_2

> GetNetworkApplianceVpnSiteToSiteVpn200Response getNetworkApplianceVpnSiteToSiteVpn_2(networkId)

Return the site-to-site VPN settings of a network

Return the site-to-site VPN settings of a network. Only valid for MX networks.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SiteToSiteVpnApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceVpnSiteToSiteVpn_2(networkId, (error, data, response) => {
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

[**GetNetworkApplianceVpnSiteToSiteVpn200Response**](GetNetworkApplianceVpnSiteToSiteVpn200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkApplianceVpnSiteToSiteVpn_2

> GetNetworkApplianceVpnSiteToSiteVpn200Response updateNetworkApplianceVpnSiteToSiteVpn_2(networkId, updateNetworkApplianceVpnSiteToSiteVpnRequest)

Update the site-to-site VPN settings of a network

Update the site-to-site VPN settings of a network. Only valid for MX networks in NAT mode.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SiteToSiteVpnApi();
let networkId = "networkId_example"; // String | 
let updateNetworkApplianceVpnSiteToSiteVpnRequest = new MerakiDashboardApi.UpdateNetworkApplianceVpnSiteToSiteVpnRequest(); // UpdateNetworkApplianceVpnSiteToSiteVpnRequest | 
apiInstance.updateNetworkApplianceVpnSiteToSiteVpn_2(networkId, updateNetworkApplianceVpnSiteToSiteVpnRequest, (error, data, response) => {
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
 **updateNetworkApplianceVpnSiteToSiteVpnRequest** | [**UpdateNetworkApplianceVpnSiteToSiteVpnRequest**](UpdateNetworkApplianceVpnSiteToSiteVpnRequest.md)|  | 

### Return type

[**GetNetworkApplianceVpnSiteToSiteVpn200Response**](GetNetworkApplianceVpnSiteToSiteVpn200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

