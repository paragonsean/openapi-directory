# MerakiDashboardApi.MXVLANPortsApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkAppliancePort**](MXVLANPortsApi.md#getNetworkAppliancePort) | **GET** /networks/{networkId}/appliancePorts/{appliancePortId} | Return per-port VLAN settings for a single MX port.
[**getNetworkAppliancePorts**](MXVLANPortsApi.md#getNetworkAppliancePorts) | **GET** /networks/{networkId}/appliancePorts | List per-port VLAN settings for all ports of a MX.
[**updateNetworkAppliancePort**](MXVLANPortsApi.md#updateNetworkAppliancePort) | **PUT** /networks/{networkId}/appliancePorts/{appliancePortId} | Update the per-port VLAN settings for a single MX port.



## getNetworkAppliancePort

> Object getNetworkAppliancePort(networkId, appliancePortId)

Return per-port VLAN settings for a single MX port.

Return per-port VLAN settings for a single MX port.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MXVLANPortsApi();
let networkId = "networkId_example"; // String | 
let appliancePortId = "appliancePortId_example"; // String | 
apiInstance.getNetworkAppliancePort(networkId, appliancePortId, (error, data, response) => {
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
 **appliancePortId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkAppliancePorts

> [Object] getNetworkAppliancePorts(networkId)

List per-port VLAN settings for all ports of a MX.

List per-port VLAN settings for all ports of a MX.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MXVLANPortsApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkAppliancePorts(networkId, (error, data, response) => {
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


## updateNetworkAppliancePort

> Object updateNetworkAppliancePort(networkId, appliancePortId, opts)

Update the per-port VLAN settings for a single MX port.

Update the per-port VLAN settings for a single MX port.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MXVLANPortsApi();
let networkId = "networkId_example"; // String | 
let appliancePortId = "appliancePortId_example"; // String | 
let opts = {
  'updateNetworkAppliancePortRequest': new MerakiDashboardApi.UpdateNetworkAppliancePortRequest() // UpdateNetworkAppliancePortRequest | 
};
apiInstance.updateNetworkAppliancePort(networkId, appliancePortId, opts, (error, data, response) => {
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
 **appliancePortId** | **String**|  | 
 **updateNetworkAppliancePortRequest** | [**UpdateNetworkAppliancePortRequest**](UpdateNetworkAppliancePortRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

