# MerakiDashboardApi.MerakiAuthUsersApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkMerakiAuthUser**](MerakiAuthUsersApi.md#getNetworkMerakiAuthUser) | **GET** /networks/{networkId}/merakiAuthUsers/{merakiAuthUserId} | Return the Meraki Auth splash or RADIUS user
[**getNetworkMerakiAuthUsers**](MerakiAuthUsersApi.md#getNetworkMerakiAuthUsers) | **GET** /networks/{networkId}/merakiAuthUsers | List the splash or RADIUS users configured under Meraki Authentication for a network



## getNetworkMerakiAuthUser

> Object getNetworkMerakiAuthUser(networkId, merakiAuthUserId)

Return the Meraki Auth splash or RADIUS user

Return the Meraki Auth splash or RADIUS user

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MerakiAuthUsersApi();
let networkId = "networkId_example"; // String | 
let merakiAuthUserId = "merakiAuthUserId_example"; // String | 
apiInstance.getNetworkMerakiAuthUser(networkId, merakiAuthUserId, (error, data, response) => {
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
 **merakiAuthUserId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkMerakiAuthUsers

> [Object] getNetworkMerakiAuthUsers(networkId)

List the splash or RADIUS users configured under Meraki Authentication for a network

List the splash or RADIUS users configured under Meraki Authentication for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MerakiAuthUsersApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkMerakiAuthUsers(networkId, (error, data, response) => {
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

