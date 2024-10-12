# MerakiDashboardApi.VlanAssignmentsApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeviceAppliancePrefixesDelegatedVlanAssignments_3**](VlanAssignmentsApi.md#getDeviceAppliancePrefixesDelegatedVlanAssignments_3) | **GET** /devices/{serial}/appliance/prefixes/delegated/vlanAssignments | Return prefixes assigned to all IPv6 enabled VLANs on an appliance.



## getDeviceAppliancePrefixesDelegatedVlanAssignments_3

> [Object] getDeviceAppliancePrefixesDelegatedVlanAssignments_3(serial)

Return prefixes assigned to all IPv6 enabled VLANs on an appliance.

Return prefixes assigned to all IPv6 enabled VLANs on an appliance.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.VlanAssignmentsApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceAppliancePrefixesDelegatedVlanAssignments_3(serial, (error, data, response) => {
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

