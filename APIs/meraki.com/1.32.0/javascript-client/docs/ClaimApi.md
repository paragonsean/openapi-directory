# MerakiDashboardApi.ClaimApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vmxNetworkDevicesClaim_2**](ClaimApi.md#vmxNetworkDevicesClaim_2) | **POST** /networks/{networkId}/devices/claim/vmx | Claim a vMX into a network



## vmxNetworkDevicesClaim_2

> Object vmxNetworkDevicesClaim_2(networkId, vmxNetworkDevicesClaimRequest)

Claim a vMX into a network

Claim a vMX into a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ClaimApi();
let networkId = "networkId_example"; // String | 
let vmxNetworkDevicesClaimRequest = new MerakiDashboardApi.VmxNetworkDevicesClaimRequest(); // VmxNetworkDevicesClaimRequest | 
apiInstance.vmxNetworkDevicesClaim_2(networkId, vmxNetworkDevicesClaimRequest, (error, data, response) => {
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
 **vmxNetworkDevicesClaimRequest** | [**VmxNetworkDevicesClaimRequest**](VmxNetworkDevicesClaimRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

