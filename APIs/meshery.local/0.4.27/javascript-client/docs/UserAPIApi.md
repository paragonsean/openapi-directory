# MesheryApi.UserAPIApi

All URIs are relative to *http://meshery.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**idDeleteLoadPreferences**](UserAPIApi.md#idDeleteLoadPreferences) | **DELETE** /api/user/prefs/perf | Handle DELETE request for load test preferences
[**idGetLoadPreferences**](UserAPIApi.md#idGetLoadPreferences) | **GET** /api/user/prefs/perf | Handle GET request for load test preferences
[**idGetTokenProvider**](UserAPIApi.md#idGetTokenProvider) | **GET** /api/user/token | Handle GET request for tokens
[**idGetUserLogin**](UserAPIApi.md#idGetUserLogin) | **GET** /api/user/login | Handlers GET request for User login
[**idGetUserLogout**](UserAPIApi.md#idGetUserLogout) | **GET** /api/user/logout | Handlers GET request for User logout
[**idGetUserTestPrefs**](UserAPIApi.md#idGetUserTestPrefs) | **GET** /api/user/prefs | Handle GET for User Load Test Preferences
[**idPostLoadPreferences**](UserAPIApi.md#idPostLoadPreferences) | **POST** /api/user/prefs/perf | Handle POST request for load test preferences
[**idPostTokenProvider**](UserAPIApi.md#idPostTokenProvider) | **POST** /api/user/token | Handle POST request for tokens
[**idPostUserTestPrefs**](UserAPIApi.md#idPostUserTestPrefs) | **POST** /api/user/prefs | Handle GET for User Load Test Preferences



## idDeleteLoadPreferences

> idDeleteLoadPreferences(opts)

Handle DELETE request for load test preferences

Used for deleting load test preferences

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.UserAPIApi();
let opts = {
  'uuid': "uuid_example" // String | 
};
apiInstance.idDeleteLoadPreferences(opts, (error, data, response) => {
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
 **uuid** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## idGetLoadPreferences

> PerformanceTestConfig idGetLoadPreferences(opts)

Handle GET request for load test preferences

Used for fetching load test preferences

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.UserAPIApi();
let opts = {
  'uuid': "uuid_example" // String | 
};
apiInstance.idGetLoadPreferences(opts, (error, data, response) => {
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
 **uuid** | **String**|  | [optional] 

### Return type

[**PerformanceTestConfig**](PerformanceTestConfig.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idGetTokenProvider

> idGetTokenProvider()

Handle GET request for tokens

Returns token from the actual provider in a file resposese: 200:

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.UserAPIApi();
apiInstance.idGetTokenProvider((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## idGetUserLogin

> idGetUserLogin()

Handlers GET request for User login

Redirects user for auth or issues session

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.UserAPIApi();
apiInstance.idGetUserLogin((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## idGetUserLogout

> idGetUserLogout()

Handlers GET request for User logout

Redirects user for auth or issues session

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.UserAPIApi();
apiInstance.idGetUserLogout((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## idGetUserTestPrefs

> Preference idGetUserTestPrefs()

Handle GET for User Load Test Preferences

Returns User Load Test Preferences

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.UserAPIApi();
apiInstance.idGetUserTestPrefs((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Preference**](Preference.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idPostLoadPreferences

> idPostLoadPreferences(opts)

Handle POST request for load test preferences

Used for persisting load test preferences

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.UserAPIApi();
let opts = {
  'performanceTestConfig': new MesheryApi.PerformanceTestConfig() // PerformanceTestConfig | 
};
apiInstance.idPostLoadPreferences(opts, (error, data, response) => {
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
 **performanceTestConfig** | [**PerformanceTestConfig**](PerformanceTestConfig.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: Not defined


## idPostTokenProvider

> idPostTokenProvider()

Handle POST request for tokens

Receives token from the actual provider resposese: 200:

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.UserAPIApi();
apiInstance.idPostTokenProvider((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## idPostUserTestPrefs

> Preference idPostUserTestPrefs()

Handle GET for User Load Test Preferences

Updates User Load Test Preferences

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.UserAPIApi();
apiInstance.idPostUserTestPrefs((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Preference**](Preference.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

