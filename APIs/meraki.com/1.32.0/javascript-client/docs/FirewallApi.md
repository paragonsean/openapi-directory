# MerakiDashboardApi.FirewallApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkApplianceFirewallCellularFirewallRules_1**](FirewallApi.md#getNetworkApplianceFirewallCellularFirewallRules_1) | **GET** /networks/{networkId}/appliance/firewall/cellularFirewallRules | Return the cellular firewall rules for an MX network
[**getNetworkApplianceFirewallFirewalledService_1**](FirewallApi.md#getNetworkApplianceFirewallFirewalledService_1) | **GET** /networks/{networkId}/appliance/firewall/firewalledServices/{service} | Return the accessibility settings of the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)
[**getNetworkApplianceFirewallFirewalledServices_1**](FirewallApi.md#getNetworkApplianceFirewallFirewalledServices_1) | **GET** /networks/{networkId}/appliance/firewall/firewalledServices | List the appliance services and their accessibility rules
[**getNetworkApplianceFirewallInboundCellularFirewallRules_1**](FirewallApi.md#getNetworkApplianceFirewallInboundCellularFirewallRules_1) | **GET** /networks/{networkId}/appliance/firewall/inboundCellularFirewallRules | Return the inbound cellular firewall rules for an MX network
[**getNetworkApplianceFirewallInboundFirewallRules_1**](FirewallApi.md#getNetworkApplianceFirewallInboundFirewallRules_1) | **GET** /networks/{networkId}/appliance/firewall/inboundFirewallRules | Return the inbound firewall rules for an MX network
[**getNetworkApplianceFirewallL3FirewallRules_1**](FirewallApi.md#getNetworkApplianceFirewallL3FirewallRules_1) | **GET** /networks/{networkId}/appliance/firewall/l3FirewallRules | Return the L3 firewall rules for an MX network
[**getNetworkApplianceFirewallL7FirewallRulesApplicationCategories_1**](FirewallApi.md#getNetworkApplianceFirewallL7FirewallRulesApplicationCategories_1) | **GET** /networks/{networkId}/appliance/firewall/l7FirewallRules/applicationCategories | Return the L7 firewall application categories and their associated applications for an MX network
[**getNetworkApplianceFirewallL7FirewallRules_1**](FirewallApi.md#getNetworkApplianceFirewallL7FirewallRules_1) | **GET** /networks/{networkId}/appliance/firewall/l7FirewallRules | List the MX L7 firewall rules for an MX network
[**getNetworkApplianceFirewallOneToManyNatRules_1**](FirewallApi.md#getNetworkApplianceFirewallOneToManyNatRules_1) | **GET** /networks/{networkId}/appliance/firewall/oneToManyNatRules | Return the 1:Many NAT mapping rules for an MX network
[**getNetworkApplianceFirewallOneToOneNatRules_1**](FirewallApi.md#getNetworkApplianceFirewallOneToOneNatRules_1) | **GET** /networks/{networkId}/appliance/firewall/oneToOneNatRules | Return the 1:1 NAT mapping rules for an MX network
[**getNetworkApplianceFirewallPortForwardingRules_1**](FirewallApi.md#getNetworkApplianceFirewallPortForwardingRules_1) | **GET** /networks/{networkId}/appliance/firewall/portForwardingRules | Return the port forwarding rules for an MX network
[**getNetworkApplianceFirewallSettings_1**](FirewallApi.md#getNetworkApplianceFirewallSettings_1) | **GET** /networks/{networkId}/appliance/firewall/settings | Return the firewall settings for this network
[**getNetworkWirelessSsidFirewallL3FirewallRules_2**](FirewallApi.md#getNetworkWirelessSsidFirewallL3FirewallRules_2) | **GET** /networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules | Return the L3 firewall rules for an SSID on an MR network
[**getNetworkWirelessSsidFirewallL7FirewallRules_2**](FirewallApi.md#getNetworkWirelessSsidFirewallL7FirewallRules_2) | **GET** /networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules | Return the L7 firewall rules for an SSID on an MR network
[**updateNetworkApplianceFirewallCellularFirewallRules_1**](FirewallApi.md#updateNetworkApplianceFirewallCellularFirewallRules_1) | **PUT** /networks/{networkId}/appliance/firewall/cellularFirewallRules | Update the cellular firewall rules of an MX network
[**updateNetworkApplianceFirewallFirewalledService_1**](FirewallApi.md#updateNetworkApplianceFirewallFirewalledService_1) | **PUT** /networks/{networkId}/appliance/firewall/firewalledServices/{service} | Updates the accessibility settings for the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)
[**updateNetworkApplianceFirewallInboundCellularFirewallRules_1**](FirewallApi.md#updateNetworkApplianceFirewallInboundCellularFirewallRules_1) | **PUT** /networks/{networkId}/appliance/firewall/inboundCellularFirewallRules | Update the inbound cellular firewall rules of an MX network
[**updateNetworkApplianceFirewallInboundFirewallRules_1**](FirewallApi.md#updateNetworkApplianceFirewallInboundFirewallRules_1) | **PUT** /networks/{networkId}/appliance/firewall/inboundFirewallRules | Update the inbound firewall rules of an MX network
[**updateNetworkApplianceFirewallL3FirewallRules_1**](FirewallApi.md#updateNetworkApplianceFirewallL3FirewallRules_1) | **PUT** /networks/{networkId}/appliance/firewall/l3FirewallRules | Update the L3 firewall rules of an MX network
[**updateNetworkApplianceFirewallL7FirewallRules_1**](FirewallApi.md#updateNetworkApplianceFirewallL7FirewallRules_1) | **PUT** /networks/{networkId}/appliance/firewall/l7FirewallRules | Update the MX L7 firewall rules for an MX network
[**updateNetworkApplianceFirewallOneToManyNatRules_1**](FirewallApi.md#updateNetworkApplianceFirewallOneToManyNatRules_1) | **PUT** /networks/{networkId}/appliance/firewall/oneToManyNatRules | Set the 1:Many NAT mapping rules for an MX network
[**updateNetworkApplianceFirewallOneToOneNatRules_1**](FirewallApi.md#updateNetworkApplianceFirewallOneToOneNatRules_1) | **PUT** /networks/{networkId}/appliance/firewall/oneToOneNatRules | Set the 1:1 NAT mapping rules for an MX network
[**updateNetworkApplianceFirewallPortForwardingRules_1**](FirewallApi.md#updateNetworkApplianceFirewallPortForwardingRules_1) | **PUT** /networks/{networkId}/appliance/firewall/portForwardingRules | Update the port forwarding rules for an MX network
[**updateNetworkApplianceFirewallSettings_1**](FirewallApi.md#updateNetworkApplianceFirewallSettings_1) | **PUT** /networks/{networkId}/appliance/firewall/settings | Update the firewall settings for this network
[**updateNetworkWirelessSsidFirewallL3FirewallRules_2**](FirewallApi.md#updateNetworkWirelessSsidFirewallL3FirewallRules_2) | **PUT** /networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules | Update the L3 firewall rules of an SSID on an MR network
[**updateNetworkWirelessSsidFirewallL7FirewallRules_2**](FirewallApi.md#updateNetworkWirelessSsidFirewallL7FirewallRules_2) | **PUT** /networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules | Update the L7 firewall rules of an SSID on an MR network



## getNetworkApplianceFirewallCellularFirewallRules_1

> Object getNetworkApplianceFirewallCellularFirewallRules_1(networkId)

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

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallCellularFirewallRules_1(networkId, (error, data, response) => {
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


## getNetworkApplianceFirewallFirewalledService_1

> Object getNetworkApplianceFirewallFirewalledService_1(networkId, service)

Return the accessibility settings of the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

Return the accessibility settings of the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
let service = "service_example"; // String | 
apiInstance.getNetworkApplianceFirewallFirewalledService_1(networkId, service, (error, data, response) => {
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
 **service** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceFirewallFirewalledServices_1

> [Object] getNetworkApplianceFirewallFirewalledServices_1(networkId)

List the appliance services and their accessibility rules

List the appliance services and their accessibility rules

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallFirewalledServices_1(networkId, (error, data, response) => {
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


## getNetworkApplianceFirewallInboundCellularFirewallRules_1

> [Object] getNetworkApplianceFirewallInboundCellularFirewallRules_1(networkId)

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

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallInboundCellularFirewallRules_1(networkId, (error, data, response) => {
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


## getNetworkApplianceFirewallInboundFirewallRules_1

> Object getNetworkApplianceFirewallInboundFirewallRules_1(networkId)

Return the inbound firewall rules for an MX network

Return the inbound firewall rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallInboundFirewallRules_1(networkId, (error, data, response) => {
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


## getNetworkApplianceFirewallL3FirewallRules_1

> Object getNetworkApplianceFirewallL3FirewallRules_1(networkId)

Return the L3 firewall rules for an MX network

Return the L3 firewall rules for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallL3FirewallRules_1(networkId, (error, data, response) => {
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


## getNetworkApplianceFirewallL7FirewallRulesApplicationCategories_1

> Object getNetworkApplianceFirewallL7FirewallRulesApplicationCategories_1(networkId)

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

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallL7FirewallRulesApplicationCategories_1(networkId, (error, data, response) => {
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


## getNetworkApplianceFirewallL7FirewallRules_1

> Object getNetworkApplianceFirewallL7FirewallRules_1(networkId)

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

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallL7FirewallRules_1(networkId, (error, data, response) => {
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


## getNetworkApplianceFirewallOneToManyNatRules_1

> Object getNetworkApplianceFirewallOneToManyNatRules_1(networkId)

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

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallOneToManyNatRules_1(networkId, (error, data, response) => {
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


## getNetworkApplianceFirewallOneToOneNatRules_1

> Object getNetworkApplianceFirewallOneToOneNatRules_1(networkId)

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

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallOneToOneNatRules_1(networkId, (error, data, response) => {
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


## getNetworkApplianceFirewallPortForwardingRules_1

> Object getNetworkApplianceFirewallPortForwardingRules_1(networkId)

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

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallPortForwardingRules_1(networkId, (error, data, response) => {
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


## getNetworkApplianceFirewallSettings_1

> Object getNetworkApplianceFirewallSettings_1(networkId)

Return the firewall settings for this network

Return the firewall settings for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceFirewallSettings_1(networkId, (error, data, response) => {
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


## getNetworkWirelessSsidFirewallL3FirewallRules_2

> Object getNetworkWirelessSsidFirewallL3FirewallRules_2(networkId, number)

Return the L3 firewall rules for an SSID on an MR network

Return the L3 firewall rules for an SSID on an MR network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidFirewallL3FirewallRules_2(networkId, number, (error, data, response) => {
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
 **number** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessSsidFirewallL7FirewallRules_2

> Object getNetworkWirelessSsidFirewallL7FirewallRules_2(networkId, number)

Return the L7 firewall rules for an SSID on an MR network

Return the L7 firewall rules for an SSID on an MR network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
apiInstance.getNetworkWirelessSsidFirewallL7FirewallRules_2(networkId, number, (error, data, response) => {
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
 **number** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkApplianceFirewallCellularFirewallRules_1

> Object updateNetworkApplianceFirewallCellularFirewallRules_1(networkId, opts)

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

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceFirewallCellularFirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkApplianceFirewallCellularFirewallRulesRequest() // UpdateNetworkApplianceFirewallCellularFirewallRulesRequest | 
};
apiInstance.updateNetworkApplianceFirewallCellularFirewallRules_1(networkId, opts, (error, data, response) => {
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


## updateNetworkApplianceFirewallFirewalledService_1

> Object updateNetworkApplianceFirewallFirewalledService_1(networkId, service, updateNetworkApplianceFirewallFirewalledServiceRequest)

Updates the accessibility settings for the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

Updates the accessibility settings for the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
let service = "service_example"; // String | 
let updateNetworkApplianceFirewallFirewalledServiceRequest = new MerakiDashboardApi.UpdateNetworkApplianceFirewallFirewalledServiceRequest(); // UpdateNetworkApplianceFirewallFirewalledServiceRequest | 
apiInstance.updateNetworkApplianceFirewallFirewalledService_1(networkId, service, updateNetworkApplianceFirewallFirewalledServiceRequest, (error, data, response) => {
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
 **service** | **String**|  | 
 **updateNetworkApplianceFirewallFirewalledServiceRequest** | [**UpdateNetworkApplianceFirewallFirewalledServiceRequest**](UpdateNetworkApplianceFirewallFirewalledServiceRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceFirewallInboundCellularFirewallRules_1

> [Object] updateNetworkApplianceFirewallInboundCellularFirewallRules_1(networkId, opts)

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

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceFirewallCellularFirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkApplianceFirewallCellularFirewallRulesRequest() // UpdateNetworkApplianceFirewallCellularFirewallRulesRequest | 
};
apiInstance.updateNetworkApplianceFirewallInboundCellularFirewallRules_1(networkId, opts, (error, data, response) => {
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


## updateNetworkApplianceFirewallInboundFirewallRules_1

> Object updateNetworkApplianceFirewallInboundFirewallRules_1(networkId, opts)

Update the inbound firewall rules of an MX network

Update the inbound firewall rules of an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceFirewallInboundFirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkApplianceFirewallInboundFirewallRulesRequest() // UpdateNetworkApplianceFirewallInboundFirewallRulesRequest | 
};
apiInstance.updateNetworkApplianceFirewallInboundFirewallRules_1(networkId, opts, (error, data, response) => {
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
 **updateNetworkApplianceFirewallInboundFirewallRulesRequest** | [**UpdateNetworkApplianceFirewallInboundFirewallRulesRequest**](UpdateNetworkApplianceFirewallInboundFirewallRulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceFirewallL3FirewallRules_1

> Object updateNetworkApplianceFirewallL3FirewallRules_1(networkId, opts)

Update the L3 firewall rules of an MX network

Update the L3 firewall rules of an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceFirewallInboundFirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkApplianceFirewallInboundFirewallRulesRequest() // UpdateNetworkApplianceFirewallInboundFirewallRulesRequest | 
};
apiInstance.updateNetworkApplianceFirewallL3FirewallRules_1(networkId, opts, (error, data, response) => {
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
 **updateNetworkApplianceFirewallInboundFirewallRulesRequest** | [**UpdateNetworkApplianceFirewallInboundFirewallRulesRequest**](UpdateNetworkApplianceFirewallInboundFirewallRulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceFirewallL7FirewallRules_1

> Object updateNetworkApplianceFirewallL7FirewallRules_1(networkId, opts)

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

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceFirewallL7FirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkApplianceFirewallL7FirewallRulesRequest() // UpdateNetworkApplianceFirewallL7FirewallRulesRequest | 
};
apiInstance.updateNetworkApplianceFirewallL7FirewallRules_1(networkId, opts, (error, data, response) => {
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
 **updateNetworkApplianceFirewallL7FirewallRulesRequest** | [**UpdateNetworkApplianceFirewallL7FirewallRulesRequest**](UpdateNetworkApplianceFirewallL7FirewallRulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceFirewallOneToManyNatRules_1

> Object updateNetworkApplianceFirewallOneToManyNatRules_1(networkId, updateNetworkApplianceFirewallOneToManyNatRulesRequest)

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

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
let updateNetworkApplianceFirewallOneToManyNatRulesRequest = new MerakiDashboardApi.UpdateNetworkApplianceFirewallOneToManyNatRulesRequest(); // UpdateNetworkApplianceFirewallOneToManyNatRulesRequest | 
apiInstance.updateNetworkApplianceFirewallOneToManyNatRules_1(networkId, updateNetworkApplianceFirewallOneToManyNatRulesRequest, (error, data, response) => {
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
 **updateNetworkApplianceFirewallOneToManyNatRulesRequest** | [**UpdateNetworkApplianceFirewallOneToManyNatRulesRequest**](UpdateNetworkApplianceFirewallOneToManyNatRulesRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceFirewallOneToOneNatRules_1

> Object updateNetworkApplianceFirewallOneToOneNatRules_1(networkId, updateNetworkApplianceFirewallOneToOneNatRulesRequest)

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

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
let updateNetworkApplianceFirewallOneToOneNatRulesRequest = new MerakiDashboardApi.UpdateNetworkApplianceFirewallOneToOneNatRulesRequest(); // UpdateNetworkApplianceFirewallOneToOneNatRulesRequest | 
apiInstance.updateNetworkApplianceFirewallOneToOneNatRules_1(networkId, updateNetworkApplianceFirewallOneToOneNatRulesRequest, (error, data, response) => {
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
 **updateNetworkApplianceFirewallOneToOneNatRulesRequest** | [**UpdateNetworkApplianceFirewallOneToOneNatRulesRequest**](UpdateNetworkApplianceFirewallOneToOneNatRulesRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceFirewallPortForwardingRules_1

> Object updateNetworkApplianceFirewallPortForwardingRules_1(networkId, updateNetworkApplianceFirewallPortForwardingRulesRequest)

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

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
let updateNetworkApplianceFirewallPortForwardingRulesRequest = new MerakiDashboardApi.UpdateNetworkApplianceFirewallPortForwardingRulesRequest(); // UpdateNetworkApplianceFirewallPortForwardingRulesRequest | 
apiInstance.updateNetworkApplianceFirewallPortForwardingRules_1(networkId, updateNetworkApplianceFirewallPortForwardingRulesRequest, (error, data, response) => {
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
 **updateNetworkApplianceFirewallPortForwardingRulesRequest** | [**UpdateNetworkApplianceFirewallPortForwardingRulesRequest**](UpdateNetworkApplianceFirewallPortForwardingRulesRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkApplianceFirewallSettings_1

> Object updateNetworkApplianceFirewallSettings_1(networkId, opts)

Update the firewall settings for this network

Update the firewall settings for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceFirewallSettingsRequest': new MerakiDashboardApi.UpdateNetworkApplianceFirewallSettingsRequest() // UpdateNetworkApplianceFirewallSettingsRequest | 
};
apiInstance.updateNetworkApplianceFirewallSettings_1(networkId, opts, (error, data, response) => {
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
 **updateNetworkApplianceFirewallSettingsRequest** | [**UpdateNetworkApplianceFirewallSettingsRequest**](UpdateNetworkApplianceFirewallSettingsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidFirewallL3FirewallRules_2

> Object updateNetworkWirelessSsidFirewallL3FirewallRules_2(networkId, number, opts)

Update the L3 firewall rules of an SSID on an MR network

Update the L3 firewall rules of an SSID on an MR network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidFirewallL3FirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest() // UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest | 
};
apiInstance.updateNetworkWirelessSsidFirewallL3FirewallRules_2(networkId, number, opts, (error, data, response) => {
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
 **number** | **String**|  | 
 **updateNetworkWirelessSsidFirewallL3FirewallRulesRequest** | [**UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest**](UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessSsidFirewallL7FirewallRules_2

> Object updateNetworkWirelessSsidFirewallL7FirewallRules_2(networkId, number, opts)

Update the L7 firewall rules of an SSID on an MR network

Update the L7 firewall rules of an SSID on an MR network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FirewallApi();
let networkId = "networkId_example"; // String | 
let number = "number_example"; // String | 
let opts = {
  'updateNetworkWirelessSsidFirewallL7FirewallRulesRequest': new MerakiDashboardApi.UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest() // UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest | 
};
apiInstance.updateNetworkWirelessSsidFirewallL7FirewallRules_2(networkId, number, opts, (error, data, response) => {
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
 **number** | **String**|  | 
 **updateNetworkWirelessSsidFirewallL7FirewallRulesRequest** | [**UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest**](UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

