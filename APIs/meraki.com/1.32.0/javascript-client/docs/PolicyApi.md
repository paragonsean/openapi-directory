# MerakiDashboardApi.PolicyApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkClientPolicy_2**](PolicyApi.md#getNetworkClientPolicy_2) | **GET** /networks/{networkId}/clients/{clientId}/policy | Return the policy assigned to a client on the network
[**updateNetworkClientPolicy_2**](PolicyApi.md#updateNetworkClientPolicy_2) | **PUT** /networks/{networkId}/clients/{clientId}/policy | Update the policy assigned to a client on the network



## getNetworkClientPolicy_2

> Object getNetworkClientPolicy_2(networkId, clientId)

Return the policy assigned to a client on the network

Return the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.PolicyApi();
let networkId = "networkId_example"; // String | 
let clientId = "clientId_example"; // String | 
apiInstance.getNetworkClientPolicy_2(networkId, clientId, (error, data, response) => {
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
 **clientId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkClientPolicy_2

> Object updateNetworkClientPolicy_2(networkId, clientId, updateNetworkClientPolicyRequest)

Update the policy assigned to a client on the network

Update the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.PolicyApi();
let networkId = "networkId_example"; // String | 
let clientId = "clientId_example"; // String | 
let updateNetworkClientPolicyRequest = new MerakiDashboardApi.UpdateNetworkClientPolicyRequest(); // UpdateNetworkClientPolicyRequest | 
apiInstance.updateNetworkClientPolicy_2(networkId, clientId, updateNetworkClientPolicyRequest, (error, data, response) => {
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
 **clientId** | **String**|  | 
 **updateNetworkClientPolicyRequest** | [**UpdateNetworkClientPolicyRequest**](UpdateNetworkClientPolicyRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

