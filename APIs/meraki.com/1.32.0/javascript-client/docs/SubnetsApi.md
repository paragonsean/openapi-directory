# MerakiDashboardApi.SubnetsApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeviceApplianceDhcpSubnets_2**](SubnetsApi.md#getDeviceApplianceDhcpSubnets_2) | **GET** /devices/{serial}/appliance/dhcp/subnets | Return the DHCP subnet information for an appliance



## getDeviceApplianceDhcpSubnets_2

> [Object] getDeviceApplianceDhcpSubnets_2(serial)

Return the DHCP subnet information for an appliance

Return the DHCP subnet information for an appliance

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SubnetsApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceApplianceDhcpSubnets_2(serial, (error, data, response) => {
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
 **serial** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

