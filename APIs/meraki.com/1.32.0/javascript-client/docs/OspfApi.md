# MerakiDashboardApi.OspfApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkSwitchRoutingOspf_2**](OspfApi.md#getNetworkSwitchRoutingOspf_2) | **GET** /networks/{networkId}/switch/routing/ospf | Return layer 3 OSPF routing configuration
[**updateNetworkSwitchRoutingOspf_2**](OspfApi.md#updateNetworkSwitchRoutingOspf_2) | **PUT** /networks/{networkId}/switch/routing/ospf | Update layer 3 OSPF routing configuration



## getNetworkSwitchRoutingOspf_2

> Object getNetworkSwitchRoutingOspf_2(networkId)

Return layer 3 OSPF routing configuration

Return layer 3 OSPF routing configuration

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.OspfApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchRoutingOspf_2(networkId, (error, data, response) => {
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


## updateNetworkSwitchRoutingOspf_2

> Object updateNetworkSwitchRoutingOspf_2(networkId, opts)

Update layer 3 OSPF routing configuration

Update layer 3 OSPF routing configuration

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.OspfApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkSwitchRoutingOspfRequest': new MerakiDashboardApi.UpdateNetworkSwitchRoutingOspfRequest() // UpdateNetworkSwitchRoutingOspfRequest | 
};
apiInstance.updateNetworkSwitchRoutingOspf_2(networkId, opts, (error, data, response) => {
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
 **updateNetworkSwitchRoutingOspfRequest** | [**UpdateNetworkSwitchRoutingOspfRequest**](UpdateNetworkSwitchRoutingOspfRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

