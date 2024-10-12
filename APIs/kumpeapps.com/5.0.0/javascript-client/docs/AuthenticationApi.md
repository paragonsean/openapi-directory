# KumpeAppsApi.AuthenticationApi

All URIs are relative to *https://restapi.kumpeapps.com/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appkeyPatch**](AuthenticationApi.md#appkeyPatch) | **PATCH** /appkey | Compromise app key
[**appkeyPost**](AuthenticationApi.md#appkeyPost) | **POST** /appkey | Request app key
[**appkeyPut**](AuthenticationApi.md#appkeyPut) | **PUT** /appkey | Deactivate app key
[**authAppkeyPatch**](AuthenticationApi.md#authAppkeyPatch) | **PATCH** /authentication/appkey | Compromise app key
[**authAppkeyPost**](AuthenticationApi.md#authAppkeyPost) | **POST** /authentication/appkey | Request app key
[**authAppkeyPut**](AuthenticationApi.md#authAppkeyPut) | **PUT** /authentication/appkey | Deactivate app key
[**authAuthkeyGet**](AuthenticationApi.md#authAuthkeyGet) | **GET** /authentication/authkey | Request auth key for user (login user)
[**authAuthkeyPatch**](AuthenticationApi.md#authAuthkeyPatch) | **PATCH** /authentication/authkey | Compromise auth key
[**authAuthkeyPost**](AuthenticationApi.md#authAuthkeyPost) | **POST** /authentication/authkey | Request auth key for user (login user)
[**authAuthkeyPut**](AuthenticationApi.md#authAuthkeyPut) | **PUT** /authentication/authkey | Deactivate auth key (logout)
[**authVerifyotpGet**](AuthenticationApi.md#authVerifyotpGet) | **GET** /authentication/verifyotp | Verifies YubiKey OTP for authenticated user
[**authkeyGet**](AuthenticationApi.md#authkeyGet) | **GET** /authkey | Request auth key for user (login user)
[**authkeyPatch**](AuthenticationApi.md#authkeyPatch) | **PATCH** /authkey | Compromise auth key
[**authkeyPost**](AuthenticationApi.md#authkeyPost) | **POST** /authkey | Request auth key for user (login user)
[**authkeyPut**](AuthenticationApi.md#authkeyPut) | **PUT** /authkey | Deactivate auth key (logout)



## appkeyPatch

> InlineResponse202 appkeyPatch(appKey, opts)

Compromise app key

Pass an app key to mark it as compromised. This may be submitted by the app owner or a concerned party that has optained the compromised app key.

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';

let apiInstance = new KumpeAppsApi.AuthenticationApi();
let appKey = "appKey_example"; // String | compromised app key
let opts = {
  'comments': "comments_example" // String | Comments (like how was this compromised)
};
apiInstance.appkeyPatch(appKey, opts, (error, data, response) => {
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
 **appKey** | **String**| compromised app key | 
 **comments** | **String**| Comments (like how was this compromised) | [optional] 

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appkeyPost

> InlineResponse201 appkeyPost(username, password, supportsYubikey)

Request app key

Request a new app key by passing username and password for app account

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';

let apiInstance = new KumpeAppsApi.AuthenticationApi();
let username = "username_example"; // String | Username assigned to your app
let password = "password_example"; // String | Password assigned to your app
let supportsYubikey = true; // Boolean | App supports YubiKey OTP
apiInstance.appkeyPost(username, password, supportsYubikey, (error, data, response) => {
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
 **username** | **String**| Username assigned to your app | 
 **password** | **String**| Password assigned to your app | 
 **supportsYubikey** | **Boolean**| App supports YubiKey OTP | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appkeyPut

> InlineResponse202 appkeyPut(appKey)

Deactivate app key

Pass your app key to deactivate the key

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: app_key
let app_key = defaultClient.authentications['app_key'];
app_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//app_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.AuthenticationApi();
let appKey = "appKey_example"; // String | app key to deactivate
apiInstance.appkeyPut(appKey, (error, data, response) => {
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
 **appKey** | **String**| app key to deactivate | 

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## authAppkeyPatch

> InlineResponse202 authAppkeyPatch(appKey, opts)

Compromise app key

Pass an app key to mark it as compromised. This may be submitted by the app owner or a concerned party that has optained the compromised app key.

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';

let apiInstance = new KumpeAppsApi.AuthenticationApi();
let appKey = "appKey_example"; // String | compromised app key
let opts = {
  'comments': "comments_example" // String | Comments (like how was this compromised)
};
apiInstance.authAppkeyPatch(appKey, opts, (error, data, response) => {
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
 **appKey** | **String**| compromised app key | 
 **comments** | **String**| Comments (like how was this compromised) | [optional] 

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## authAppkeyPost

> InlineResponse201 authAppkeyPost(username, password, supportsYubikey)

Request app key

Request a new app key by passing username and password for app account

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';

let apiInstance = new KumpeAppsApi.AuthenticationApi();
let username = "username_example"; // String | Username assigned to your app
let password = "password_example"; // String | Password assigned to your app
let supportsYubikey = true; // Boolean | App supports YubiKey OTP
apiInstance.authAppkeyPost(username, password, supportsYubikey, (error, data, response) => {
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
 **username** | **String**| Username assigned to your app | 
 **password** | **String**| Password assigned to your app | 
 **supportsYubikey** | **Boolean**| App supports YubiKey OTP | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## authAppkeyPut

> InlineResponse202 authAppkeyPut(appKey)

Deactivate app key

Pass your app key to deactivate the key

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: app_key
let app_key = defaultClient.authentications['app_key'];
app_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//app_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.AuthenticationApi();
let appKey = "appKey_example"; // String | app key to deactivate
apiInstance.authAppkeyPut(appKey, (error, data, response) => {
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
 **appKey** | **String**| app key to deactivate | 

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## authAuthkeyGet

> InlineResponse2011 authAuthkeyGet(username, password, opts)

Request auth key for user (login user)

Obtain auth key for user that has provided their username and password to login to your app. (or to obtain an auth key for a script like IFTTT)

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: app_key
let app_key = defaultClient.authentications['app_key'];
app_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//app_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.AuthenticationApi();
let username = "username_example"; // String | Authenticated username
let password = "password_example"; // String | Authenticated password
let opts = {
  'otp': "otp_example", // String | YubiKey OTP (if configured for user)
  'deviceName': "deviceName_example", // String | User's device name
  'identifierForVendor': "identifierForVendor_example" // String | identifierForVendor for User's Device (if app is iOS)
};
apiInstance.authAuthkeyGet(username, password, opts, (error, data, response) => {
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
 **username** | **String**| Authenticated username | 
 **password** | **String**| Authenticated password | 
 **otp** | **String**| YubiKey OTP (if configured for user) | [optional] 
 **deviceName** | **String**| User&#39;s device name | [optional] 
 **identifierForVendor** | **String**| identifierForVendor for User&#39;s Device (if app is iOS) | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## authAuthkeyPatch

> InlineResponse202 authAuthkeyPatch(authKey, opts)

Compromise auth key

Mark user auth key as compromised

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';

let apiInstance = new KumpeAppsApi.AuthenticationApi();
let authKey = "authKey_example"; // String | auth key to mark as compromised
let opts = {
  'comments': "comments_example" // String | Comments (like how was this compromised)
};
apiInstance.authAuthkeyPatch(authKey, opts, (error, data, response) => {
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
 **authKey** | **String**| auth key to mark as compromised | 
 **comments** | **String**| Comments (like how was this compromised) | [optional] 

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## authAuthkeyPost

> InlineResponse2011 authAuthkeyPost(username, password, opts)

Request auth key for user (login user)

Obtain auth key for user that has provided their username and password to login to your app. (or to obtain an auth key for a script like IFTTT)

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: app_key
let app_key = defaultClient.authentications['app_key'];
app_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//app_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.AuthenticationApi();
let username = "username_example"; // String | Authenticated username
let password = "password_example"; // String | Authenticated password
let opts = {
  'otp': "otp_example" // String | YubiKey OTP (if configured for user)
};
apiInstance.authAuthkeyPost(username, password, opts, (error, data, response) => {
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
 **username** | **String**| Authenticated username | 
 **password** | **String**| Authenticated password | 
 **otp** | **String**| YubiKey OTP (if configured for user) | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## authAuthkeyPut

> InlineResponse202 authAuthkeyPut(authKey)

Deactivate auth key (logout)

Deactivate auth key for user logging them out of your application

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: app_key
let app_key = defaultClient.authentications['app_key'];
app_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//app_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.AuthenticationApi();
let authKey = "authKey_example"; // String | auth key to logout
apiInstance.authAuthkeyPut(authKey, (error, data, response) => {
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
 **authKey** | **String**| auth key to logout | 

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## authVerifyotpGet

> authVerifyotpGet(otp)

Verifies YubiKey OTP for authenticated user

Verifies YubiKey OTP for authenticated user

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: auth_key
let auth_key = defaultClient.authentications['auth_key'];
auth_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.AuthenticationApi();
let otp = "otp_example"; // String | YubiKey OTP code
apiInstance.authVerifyotpGet(otp, (error, data, response) => {
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
 **otp** | **String**| YubiKey OTP code | 

### Return type

null (empty response body)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## authkeyGet

> InlineResponse2011 authkeyGet(username, password, opts)

Request auth key for user (login user)

Obtain auth key for user that has provided their username and password to login to your app. (or to obtain an auth key for a script like IFTTT)

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: app_key
let app_key = defaultClient.authentications['app_key'];
app_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//app_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.AuthenticationApi();
let username = "username_example"; // String | Authenticated username
let password = "password_example"; // String | Authenticated password
let opts = {
  'otp': "otp_example" // String | YubiKey OTP (if configured for user)
};
apiInstance.authkeyGet(username, password, opts, (error, data, response) => {
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
 **username** | **String**| Authenticated username | 
 **password** | **String**| Authenticated password | 
 **otp** | **String**| YubiKey OTP (if configured for user) | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## authkeyPatch

> InlineResponse202 authkeyPatch(authKey, opts)

Compromise auth key

Mark user auth key as compromised

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';

let apiInstance = new KumpeAppsApi.AuthenticationApi();
let authKey = "authKey_example"; // String | auth key to mark as compromised
let opts = {
  'comments': "comments_example" // String | Comments (like how was this compromised)
};
apiInstance.authkeyPatch(authKey, opts, (error, data, response) => {
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
 **authKey** | **String**| auth key to mark as compromised | 
 **comments** | **String**| Comments (like how was this compromised) | [optional] 

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## authkeyPost

> InlineResponse2011 authkeyPost(username, password, opts)

Request auth key for user (login user)

Obtain auth key for user that has provided their username and password to login to your app. (or to obtain an auth key for a script like IFTTT)

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: app_key
let app_key = defaultClient.authentications['app_key'];
app_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//app_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.AuthenticationApi();
let username = "username_example"; // String | Authenticated username
let password = "password_example"; // String | Authenticated password
let opts = {
  'otp': "otp_example" // String | YubiKey OTP (if configured for user)
};
apiInstance.authkeyPost(username, password, opts, (error, data, response) => {
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
 **username** | **String**| Authenticated username | 
 **password** | **String**| Authenticated password | 
 **otp** | **String**| YubiKey OTP (if configured for user) | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## authkeyPut

> InlineResponse202 authkeyPut(authKey)

Deactivate auth key (logout)

Deactivate auth key for user logging them out of your application

### Example

```javascript
import KumpeAppsApi from 'kumpe_apps_api';
let defaultClient = KumpeAppsApi.ApiClient.instance;
// Configure API key authorization: app_key
let app_key = defaultClient.authentications['app_key'];
app_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//app_key.apiKeyPrefix = 'Token';

let apiInstance = new KumpeAppsApi.AuthenticationApi();
let authKey = "authKey_example"; // String | auth key to logout
apiInstance.authkeyPut(authKey, (error, data, response) => {
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
 **authKey** | **String**| auth key to logout | 

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

