# JellyfinApi.QuickConnectApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate**](QuickConnectApi.md#activate) | **POST** /QuickConnect/Activate | Temporarily activates quick connect for five minutes.
[**authorize**](QuickConnectApi.md#authorize) | **POST** /QuickConnect/Authorize | Authorizes a pending quick connect request.
[**available**](QuickConnectApi.md#available) | **POST** /QuickConnect/Available | Enables or disables quick connect.
[**connect**](QuickConnectApi.md#connect) | **GET** /QuickConnect/Connect | Attempts to retrieve authentication information.
[**deauthorize**](QuickConnectApi.md#deauthorize) | **POST** /QuickConnect/Deauthorize | Deauthorize all quick connect devices for the current user.
[**getStatus**](QuickConnectApi.md#getStatus) | **GET** /QuickConnect/Status | Gets the current quick connect state.
[**initiate**](QuickConnectApi.md#initiate) | **GET** /QuickConnect/Initiate | Initiate a new quick connect request.



## activate

> activate()

Temporarily activates quick connect for five minutes.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.QuickConnectApi();
apiInstance.activate((error, data, response) => {
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

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## authorize

> Boolean authorize(code)

Authorizes a pending quick connect request.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.QuickConnectApi();
let code = "code_example"; // String | Quick connect code to authorize.
apiInstance.authorize(code, (error, data, response) => {
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
 **code** | **String**| Quick connect code to authorize. | 

### Return type

**Boolean**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## available

> available(opts)

Enables or disables quick connect.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.QuickConnectApi();
let opts = {
  'status': new JellyfinApi.QuickConnectState() // QuickConnectState | New MediaBrowser.Model.QuickConnect.QuickConnectState.
};
apiInstance.available(opts, (error, data, response) => {
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
 **status** | [**QuickConnectState**](.md)| New MediaBrowser.Model.QuickConnect.QuickConnectState. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## connect

> QuickConnectResult connect(secret)

Attempts to retrieve authentication information.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.QuickConnectApi();
let secret = "secret_example"; // String | Secret previously returned from the Initiate endpoint.
apiInstance.connect(secret, (error, data, response) => {
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
 **secret** | **String**| Secret previously returned from the Initiate endpoint. | 

### Return type

[**QuickConnectResult**](QuickConnectResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## deauthorize

> Number deauthorize()

Deauthorize all quick connect devices for the current user.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.QuickConnectApi();
apiInstance.deauthorize((error, data, response) => {
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

**Number**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getStatus

> QuickConnectState getStatus()

Gets the current quick connect state.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.QuickConnectApi();
apiInstance.getStatus((error, data, response) => {
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

[**QuickConnectState**](QuickConnectState.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## initiate

> QuickConnectResult initiate()

Initiate a new quick connect request.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.QuickConnectApi();
apiInstance.initiate((error, data, response) => {
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

[**QuickConnectResult**](QuickConnectResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

