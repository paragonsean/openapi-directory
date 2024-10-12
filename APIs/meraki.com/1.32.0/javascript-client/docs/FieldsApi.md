# MerakiDashboardApi.FieldsApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**updateNetworkSmDevicesFields_2**](FieldsApi.md#updateNetworkSmDevicesFields_2) | **PUT** /networks/{networkId}/sm/devices/fields | Modify the fields of a device



## updateNetworkSmDevicesFields_2

> [UpdateNetworkSmDevicesFields200ResponseInner] updateNetworkSmDevicesFields_2(networkId, updateNetworkSmDevicesFieldsRequest)

Modify the fields of a device

Modify the fields of a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FieldsApi();
let networkId = "networkId_example"; // String | 
let updateNetworkSmDevicesFieldsRequest = new MerakiDashboardApi.UpdateNetworkSmDevicesFieldsRequest(); // UpdateNetworkSmDevicesFieldsRequest | 
apiInstance.updateNetworkSmDevicesFields_2(networkId, updateNetworkSmDevicesFieldsRequest, (error, data, response) => {
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
 **updateNetworkSmDevicesFieldsRequest** | [**UpdateNetworkSmDevicesFieldsRequest**](UpdateNetworkSmDevicesFieldsRequest.md)|  | 

### Return type

[**[UpdateNetworkSmDevicesFields200ResponseInner]**](UpdateNetworkSmDevicesFields200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

