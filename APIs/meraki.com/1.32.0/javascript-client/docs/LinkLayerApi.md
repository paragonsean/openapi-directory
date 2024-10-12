# MerakiDashboardApi.LinkLayerApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkTopologyLinkLayer_2**](LinkLayerApi.md#getNetworkTopologyLinkLayer_2) | **GET** /networks/{networkId}/topology/linkLayer | List the LLDP and CDP information for all discovered devices and connections in a network.



## getNetworkTopologyLinkLayer_2

> Object getNetworkTopologyLinkLayer_2(networkId)

List the LLDP and CDP information for all discovered devices and connections in a network.

List the LLDP and CDP information for all discovered devices and connections in a network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.LinkLayerApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkTopologyLinkLayer_2(networkId, (error, data, response) => {
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

