# MerakiDashboardApi.AccessControlListsApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkSwitchAccessControlLists_1**](AccessControlListsApi.md#getNetworkSwitchAccessControlLists_1) | **GET** /networks/{networkId}/switch/accessControlLists | Return the access control lists for a MS network
[**updateNetworkSwitchAccessControlLists_1**](AccessControlListsApi.md#updateNetworkSwitchAccessControlLists_1) | **PUT** /networks/{networkId}/switch/accessControlLists | Update the access control lists for a MS network



## getNetworkSwitchAccessControlLists_1

> GetNetworkSwitchAccessControlLists200Response getNetworkSwitchAccessControlLists_1(networkId)

Return the access control lists for a MS network

Return the access control lists for a MS network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AccessControlListsApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchAccessControlLists_1(networkId, (error, data, response) => {
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

[**GetNetworkSwitchAccessControlLists200Response**](GetNetworkSwitchAccessControlLists200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkSwitchAccessControlLists_1

> GetNetworkSwitchAccessControlLists200Response updateNetworkSwitchAccessControlLists_1(networkId, updateNetworkSwitchAccessControlListsRequest)

Update the access control lists for a MS network

Update the access control lists for a MS network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AccessControlListsApi();
let networkId = "networkId_example"; // String | 
let updateNetworkSwitchAccessControlListsRequest = new MerakiDashboardApi.UpdateNetworkSwitchAccessControlListsRequest(); // UpdateNetworkSwitchAccessControlListsRequest | 
apiInstance.updateNetworkSwitchAccessControlLists_1(networkId, updateNetworkSwitchAccessControlListsRequest, (error, data, response) => {
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
 **updateNetworkSwitchAccessControlListsRequest** | [**UpdateNetworkSwitchAccessControlListsRequest**](UpdateNetworkSwitchAccessControlListsRequest.md)|  | 

### Return type

[**GetNetworkSwitchAccessControlLists200Response**](GetNetworkSwitchAccessControlLists200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

