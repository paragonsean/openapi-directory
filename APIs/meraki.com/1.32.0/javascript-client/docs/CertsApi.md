# MerakiDashboardApi.CertsApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkSmDeviceCerts_2**](CertsApi.md#getNetworkSmDeviceCerts_2) | **GET** /networks/{networkId}/sm/devices/{deviceId}/certs | List the certs on a device



## getNetworkSmDeviceCerts_2

> [GetNetworkSmDeviceCerts200ResponseInner] getNetworkSmDeviceCerts_2(networkId, deviceId)

List the certs on a device

List the certs on a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.CertsApi();
let networkId = "networkId_example"; // String | 
let deviceId = "deviceId_example"; // String | 
apiInstance.getNetworkSmDeviceCerts_2(networkId, deviceId, (error, data, response) => {
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
 **deviceId** | **String**|  | 

### Return type

[**[GetNetworkSmDeviceCerts200ResponseInner]**](GetNetworkSmDeviceCerts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

