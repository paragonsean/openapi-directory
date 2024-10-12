# MerakiDashboardApi.UsersApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteOrganizationUser_1**](UsersApi.md#deleteOrganizationUser_1) | **DELETE** /organizations/{organizationId}/users/{userId} | Delete a user and all of its authentication methods.
[**getNetworkSmUserDeviceProfiles_1**](UsersApi.md#getNetworkSmUserDeviceProfiles_1) | **GET** /networks/{networkId}/sm/users/{userId}/deviceProfiles | Get the profiles associated with a user
[**getNetworkSmUserSoftwares_1**](UsersApi.md#getNetworkSmUserSoftwares_1) | **GET** /networks/{networkId}/sm/users/{userId}/softwares | Get a list of softwares associated with a user
[**getNetworkSmUsers_1**](UsersApi.md#getNetworkSmUsers_1) | **GET** /networks/{networkId}/sm/users | List the owners in an SM network with various specified fields and filters



## deleteOrganizationUser_1

> deleteOrganizationUser_1(organizationId, userId)

Delete a user and all of its authentication methods.

Delete a user and all of its authentication methods.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.UsersApi();
let organizationId = "organizationId_example"; // String | 
let userId = "userId_example"; // String | 
apiInstance.deleteOrganizationUser_1(organizationId, userId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizationId** | **String**|  | 
 **userId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNetworkSmUserDeviceProfiles_1

> [GetNetworkSmDeviceDeviceProfiles200ResponseInner] getNetworkSmUserDeviceProfiles_1(networkId, userId)

Get the profiles associated with a user

Get the profiles associated with a user

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.UsersApi();
let networkId = "networkId_example"; // String | 
let userId = "userId_example"; // String | 
apiInstance.getNetworkSmUserDeviceProfiles_1(networkId, userId, (error, data, response) => {
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
 **userId** | **String**|  | 

### Return type

[**[GetNetworkSmDeviceDeviceProfiles200ResponseInner]**](GetNetworkSmDeviceDeviceProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmUserSoftwares_1

> [GetNetworkSmDeviceSoftwares200ResponseInner] getNetworkSmUserSoftwares_1(networkId, userId)

Get a list of softwares associated with a user

Get a list of softwares associated with a user

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.UsersApi();
let networkId = "networkId_example"; // String | 
let userId = "userId_example"; // String | 
apiInstance.getNetworkSmUserSoftwares_1(networkId, userId, (error, data, response) => {
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
 **userId** | **String**|  | 

### Return type

[**[GetNetworkSmDeviceSoftwares200ResponseInner]**](GetNetworkSmDeviceSoftwares200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmUsers_1

> [GetNetworkSmUsers200ResponseInner] getNetworkSmUsers_1(networkId, opts)

List the owners in an SM network with various specified fields and filters

List the owners in an SM network with various specified fields and filters

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.UsersApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'ids': ["null"], // [String] | Filter users by id(s).
  'usernames': ["null"], // [String] | Filter users by username(s).
  'emails': ["null"], // [String] | Filter users by email(s).
  'scope': ["null"] // [String] | Specifiy a scope (one of all, none, withAny, withAll, withoutAny, withoutAll) and a set of tags.
};
apiInstance.getNetworkSmUsers_1(networkId, opts, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)| Filter users by id(s). | [optional] 
 **usernames** | [**[String]**](String.md)| Filter users by username(s). | [optional] 
 **emails** | [**[String]**](String.md)| Filter users by email(s). | [optional] 
 **scope** | [**[String]**](String.md)| Specifiy a scope (one of all, none, withAny, withAll, withoutAny, withoutAll) and a set of tags. | [optional] 

### Return type

[**[GetNetworkSmUsers200ResponseInner]**](GetNetworkSmUsers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

