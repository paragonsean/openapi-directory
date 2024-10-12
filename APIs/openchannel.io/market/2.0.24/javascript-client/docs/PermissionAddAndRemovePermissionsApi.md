# OpenChannelMarketApi.PermissionAddAndRemovePermissionsApi

All URIs are relative to *https://market.openchannel.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**permissionAppsAppIdDelete**](PermissionAddAndRemovePermissionsApi.md#permissionAppsAppIdDelete) | **DELETE** /permission/apps/{appId} | Removes permission that allows the app to access this user&#39;s data
[**permissionAppsAppIdGet**](PermissionAddAndRemovePermissionsApi.md#permissionAppsAppIdGet) | **GET** /permission/apps/{appId} | Returns permission that allows the app to access this user&#39;s data
[**permissionAppsAppIdPost**](PermissionAddAndRemovePermissionsApi.md#permissionAppsAppIdPost) | **POST** /permission/apps/{appId} | Adds permission to allow the app to access this user&#39;s data



## permissionAppsAppIdDelete

> permissionAppsAppIdDelete(appId, userId)

Removes permission that allows the app to access this user&#39;s data

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.PermissionAddAndRemovePermissionsApi();
let appId = "appId_example"; // String | The id of the app
let userId = "userId_example"; // String | The id of the user
apiInstance.permissionAppsAppIdDelete(appId, userId, (error, data, response) => {
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
 **appId** | **String**| The id of the app | 
 **userId** | **String**| The id of the user | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## permissionAppsAppIdGet

> Access permissionAppsAppIdGet(appId, userId)

Returns permission that allows the app to access this user&#39;s data

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.PermissionAddAndRemovePermissionsApi();
let appId = "appId_example"; // String | The id of the app
let userId = "userId_example"; // String | The id of the user
apiInstance.permissionAppsAppIdGet(appId, userId, (error, data, response) => {
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
 **appId** | **String**| The id of the app | 
 **userId** | **String**| The id of the user | 

### Return type

[**Access**](Access.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## permissionAppsAppIdPost

> Access permissionAppsAppIdPost(appId, userId, opts)

Adds permission to allow the app to access this user&#39;s data

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.PermissionAddAndRemovePermissionsApi();
let appId = "appId_example"; // String | The id of the app
let userId = "userId_example"; // String | The id of the user
let opts = {
  'date': 789, // Number | The time (in milliseconds) of when the user agreed to the access request
  'ip': "ip_example" // String | The ip address of the user agreeing to the access request
};
apiInstance.permissionAppsAppIdPost(appId, userId, opts, (error, data, response) => {
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
 **appId** | **String**| The id of the app | 
 **userId** | **String**| The id of the user | 
 **date** | **Number**| The time (in milliseconds) of when the user agreed to the access request | [optional] 
 **ip** | **String**| The ip address of the user agreeing to the access request | [optional] 

### Return type

[**Access**](Access.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

