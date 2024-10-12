# GooglePlayEmmApi.ManagedconfigurationsfordeviceApi

All URIs are relative to *https://androidenterprise.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**androidenterpriseManagedconfigurationsfordeviceDelete**](ManagedconfigurationsfordeviceApi.md#androidenterpriseManagedconfigurationsfordeviceDelete) | **DELETE** /androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/managedConfigurationsForDevice/{managedConfigurationForDeviceId} | 
[**androidenterpriseManagedconfigurationsfordeviceGet**](ManagedconfigurationsfordeviceApi.md#androidenterpriseManagedconfigurationsfordeviceGet) | **GET** /androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/managedConfigurationsForDevice/{managedConfigurationForDeviceId} | 
[**androidenterpriseManagedconfigurationsfordeviceList**](ManagedconfigurationsfordeviceApi.md#androidenterpriseManagedconfigurationsfordeviceList) | **GET** /androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/managedConfigurationsForDevice | 
[**androidenterpriseManagedconfigurationsfordeviceUpdate**](ManagedconfigurationsfordeviceApi.md#androidenterpriseManagedconfigurationsfordeviceUpdate) | **PUT** /androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/managedConfigurationsForDevice/{managedConfigurationForDeviceId} | 



## androidenterpriseManagedconfigurationsfordeviceDelete

> androidenterpriseManagedconfigurationsfordeviceDelete(enterpriseId, userId, deviceId, managedConfigurationForDeviceId, opts)



Removes a per-device managed configuration for an app for the specified device.

### Example

```javascript
import GooglePlayEmmApi from 'google_play_emm_api';
let defaultClient = GooglePlayEmmApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayEmmApi.ManagedconfigurationsfordeviceApi();
let enterpriseId = "enterpriseId_example"; // String | The ID of the enterprise.
let userId = "userId_example"; // String | The ID of the user.
let deviceId = "deviceId_example"; // String | The Android ID of the device.
let managedConfigurationForDeviceId = "managedConfigurationForDeviceId_example"; // String | The ID of the managed configuration (a product ID), e.g. \"app:com.google.android.gm\".
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.androidenterpriseManagedconfigurationsfordeviceDelete(enterpriseId, userId, deviceId, managedConfigurationForDeviceId, opts, (error, data, response) => {
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
 **enterpriseId** | **String**| The ID of the enterprise. | 
 **userId** | **String**| The ID of the user. | 
 **deviceId** | **String**| The Android ID of the device. | 
 **managedConfigurationForDeviceId** | **String**| The ID of the managed configuration (a product ID), e.g. \&quot;app:com.google.android.gm\&quot;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## androidenterpriseManagedconfigurationsfordeviceGet

> ManagedConfiguration androidenterpriseManagedconfigurationsfordeviceGet(enterpriseId, userId, deviceId, managedConfigurationForDeviceId, opts)



Retrieves details of a per-device managed configuration.

### Example

```javascript
import GooglePlayEmmApi from 'google_play_emm_api';
let defaultClient = GooglePlayEmmApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayEmmApi.ManagedconfigurationsfordeviceApi();
let enterpriseId = "enterpriseId_example"; // String | The ID of the enterprise.
let userId = "userId_example"; // String | The ID of the user.
let deviceId = "deviceId_example"; // String | The Android ID of the device.
let managedConfigurationForDeviceId = "managedConfigurationForDeviceId_example"; // String | The ID of the managed configuration (a product ID), e.g. \"app:com.google.android.gm\".
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.androidenterpriseManagedconfigurationsfordeviceGet(enterpriseId, userId, deviceId, managedConfigurationForDeviceId, opts, (error, data, response) => {
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
 **enterpriseId** | **String**| The ID of the enterprise. | 
 **userId** | **String**| The ID of the user. | 
 **deviceId** | **String**| The Android ID of the device. | 
 **managedConfigurationForDeviceId** | **String**| The ID of the managed configuration (a product ID), e.g. \&quot;app:com.google.android.gm\&quot;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**ManagedConfiguration**](ManagedConfiguration.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## androidenterpriseManagedconfigurationsfordeviceList

> ManagedConfigurationsForDeviceListResponse androidenterpriseManagedconfigurationsfordeviceList(enterpriseId, userId, deviceId, opts)



Lists all the per-device managed configurations for the specified device. Only the ID is set.

### Example

```javascript
import GooglePlayEmmApi from 'google_play_emm_api';
let defaultClient = GooglePlayEmmApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayEmmApi.ManagedconfigurationsfordeviceApi();
let enterpriseId = "enterpriseId_example"; // String | The ID of the enterprise.
let userId = "userId_example"; // String | The ID of the user.
let deviceId = "deviceId_example"; // String | The Android ID of the device.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.androidenterpriseManagedconfigurationsfordeviceList(enterpriseId, userId, deviceId, opts, (error, data, response) => {
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
 **enterpriseId** | **String**| The ID of the enterprise. | 
 **userId** | **String**| The ID of the user. | 
 **deviceId** | **String**| The Android ID of the device. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**ManagedConfigurationsForDeviceListResponse**](ManagedConfigurationsForDeviceListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## androidenterpriseManagedconfigurationsfordeviceUpdate

> ManagedConfiguration androidenterpriseManagedconfigurationsfordeviceUpdate(enterpriseId, userId, deviceId, managedConfigurationForDeviceId, opts)



Adds or updates a per-device managed configuration for an app for the specified device.

### Example

```javascript
import GooglePlayEmmApi from 'google_play_emm_api';
let defaultClient = GooglePlayEmmApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayEmmApi.ManagedconfigurationsfordeviceApi();
let enterpriseId = "enterpriseId_example"; // String | The ID of the enterprise.
let userId = "userId_example"; // String | The ID of the user.
let deviceId = "deviceId_example"; // String | The Android ID of the device.
let managedConfigurationForDeviceId = "managedConfigurationForDeviceId_example"; // String | The ID of the managed configuration (a product ID), e.g. \"app:com.google.android.gm\".
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'managedConfiguration': new GooglePlayEmmApi.ManagedConfiguration() // ManagedConfiguration | 
};
apiInstance.androidenterpriseManagedconfigurationsfordeviceUpdate(enterpriseId, userId, deviceId, managedConfigurationForDeviceId, opts, (error, data, response) => {
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
 **enterpriseId** | **String**| The ID of the enterprise. | 
 **userId** | **String**| The ID of the user. | 
 **deviceId** | **String**| The Android ID of the device. | 
 **managedConfigurationForDeviceId** | **String**| The ID of the managed configuration (a product ID), e.g. \&quot;app:com.google.android.gm\&quot;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **managedConfiguration** | [**ManagedConfiguration**](ManagedConfiguration.md)|  | [optional] 

### Return type

[**ManagedConfiguration**](ManagedConfiguration.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

