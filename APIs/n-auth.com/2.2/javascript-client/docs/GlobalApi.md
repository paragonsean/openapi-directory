# NextAuthApi.GlobalApi

All URIs are relative to *https://api.nextauth.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteGlobalAttribute**](GlobalApi.md#deleteGlobalAttribute) | **DELETE** /attributes/{attributekey} | Delete specific global attribute
[**deleteGlobalAttributes**](GlobalApi.md#deleteGlobalAttributes) | **DELETE** /attributes/ | Delete all global attributes
[**deleteServerPrivilegedAttribute**](GlobalApi.md#deleteServerPrivilegedAttribute) | **DELETE** /servers/{serverid}/privilegedattributes/{attributekey} | Delete specific privileged attribute of a specific server
[**deleteServerPrivilegedAttributes**](GlobalApi.md#deleteServerPrivilegedAttributes) | **DELETE** /servers/{serverid}/privilegedattributes/ | Delete all privileged attributes of a specific server
[**getGlobalAttributes**](GlobalApi.md#getGlobalAttributes) | **GET** /attributes/ | Get all global attributes
[**getServerPrivilegedAttributes**](GlobalApi.md#getServerPrivilegedAttributes) | **GET** /servers/{serverid}/privilegedattributes/ | Get all privileged attributes of a specific server
[**setGlobalAttributes**](GlobalApi.md#setGlobalAttributes) | **POST** /attributes/ | Set all global attributes
[**setServerPrivilegedAttributes**](GlobalApi.md#setServerPrivilegedAttributes) | **POST** /servers/{serverid}/privilegedattributes/ | Set all privileged attributes of a specific server
[**updateGlobalAttributes**](GlobalApi.md#updateGlobalAttributes) | **PUT** /attributes/ | Update specified global attributes
[**updateServerPrivilegedAttributes**](GlobalApi.md#updateServerPrivilegedAttributes) | **PUT** /servers/{serverid}/privilegedattributes/ | Update privileged specified attributes of a specific server



## deleteGlobalAttribute

> deleteGlobalAttribute(attributekey)

Delete specific global attribute

Delete global attribute with the specified key. Required: global &#39;servers&#39;.

### Example

```javascript
import NextAuthApi from 'next_auth_api';
let defaultClient = NextAuthApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: role_id
let role_id = defaultClient.authentications['role_id'];
role_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//role_id.apiKeyPrefix = 'Token';

let apiInstance = new NextAuthApi.GlobalApi();
let attributekey = "attributekey_example"; // String | Key of the attribute
apiInstance.deleteGlobalAttribute(attributekey, (error, data, response) => {
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
 **attributekey** | **String**| Key of the attribute | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteGlobalAttributes

> deleteGlobalAttributes()

Delete all global attributes

Delete all global attributes. Required permission: global &#39;servers&#39;.

### Example

```javascript
import NextAuthApi from 'next_auth_api';
let defaultClient = NextAuthApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: role_id
let role_id = defaultClient.authentications['role_id'];
role_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//role_id.apiKeyPrefix = 'Token';

let apiInstance = new NextAuthApi.GlobalApi();
apiInstance.deleteGlobalAttributes((error, data, response) => {
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

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteServerPrivilegedAttribute

> deleteServerPrivilegedAttribute(serverid, attributekey)

Delete specific privileged attribute of a specific server

Delete privileged attribute with the specified key of a specific server. Required permission: global &#39;servers&#39;.

### Example

```javascript
import NextAuthApi from 'next_auth_api';
let defaultClient = NextAuthApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: role_id
let role_id = defaultClient.authentications['role_id'];
role_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//role_id.apiKeyPrefix = 'Token';

let apiInstance = new NextAuthApi.GlobalApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let attributekey = "attributekey_example"; // String | Key of the attribute
apiInstance.deleteServerPrivilegedAttribute(serverid, attributekey, (error, data, response) => {
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
 **serverid** | **String**| Base64 encoded server id | 
 **attributekey** | **String**| Key of the attribute | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteServerPrivilegedAttributes

> deleteServerPrivilegedAttributes(serverid)

Delete all privileged attributes of a specific server

Delete all privileged attributes of a specific server. Required permission: global &#39;servers&#39;.

### Example

```javascript
import NextAuthApi from 'next_auth_api';
let defaultClient = NextAuthApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: role_id
let role_id = defaultClient.authentications['role_id'];
role_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//role_id.apiKeyPrefix = 'Token';

let apiInstance = new NextAuthApi.GlobalApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
apiInstance.deleteServerPrivilegedAttributes(serverid, (error, data, response) => {
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
 **serverid** | **String**| Base64 encoded server id | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getGlobalAttributes

> String getGlobalAttributes()

Get all global attributes

Returns an array containing all global attributes. Required permission: global &#39;servers&#39;.

### Example

```javascript
import NextAuthApi from 'next_auth_api';
let defaultClient = NextAuthApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: role_id
let role_id = defaultClient.authentications['role_id'];
role_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//role_id.apiKeyPrefix = 'Token';

let apiInstance = new NextAuthApi.GlobalApi();
apiInstance.getGlobalAttributes((error, data, response) => {
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

**String**

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## getServerPrivilegedAttributes

> String getServerPrivilegedAttributes(serverid)

Get all privileged attributes of a specific server

Returns an array containing all privileged attributes corresponding to this server. Required permission: global &#39;servers&#39;.

### Example

```javascript
import NextAuthApi from 'next_auth_api';
let defaultClient = NextAuthApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: role_id
let role_id = defaultClient.authentications['role_id'];
role_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//role_id.apiKeyPrefix = 'Token';

let apiInstance = new NextAuthApi.GlobalApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
apiInstance.getServerPrivilegedAttributes(serverid, (error, data, response) => {
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
 **serverid** | **String**| Base64 encoded server id | 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## setGlobalAttributes

> setGlobalAttributes(attributes)

Set all global attributes

Set the global attributes. Prior attributes with keys that are not provided in the body of the request will be deleted. Required permission: global &#39;servers&#39;.

### Example

```javascript
import NextAuthApi from 'next_auth_api';
let defaultClient = NextAuthApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: role_id
let role_id = defaultClient.authentications['role_id'];
role_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//role_id.apiKeyPrefix = 'Token';

let apiInstance = new NextAuthApi.GlobalApi();
let attributes = {key: null}; // Object | Array of attributes
apiInstance.setGlobalAttributes(attributes, (error, data, response) => {
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
 **attributes** | **Object**| Array of attributes | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setServerPrivilegedAttributes

> setServerPrivilegedAttributes(serverid, attributes)

Set all privileged attributes of a specific server

Set the privileged attributes of a specific server. Prior attributes with keys that are not provided in the body of the request will be deleted. Required permission: global &#39;servers&#39;.

### Example

```javascript
import NextAuthApi from 'next_auth_api';
let defaultClient = NextAuthApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: role_id
let role_id = defaultClient.authentications['role_id'];
role_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//role_id.apiKeyPrefix = 'Token';

let apiInstance = new NextAuthApi.GlobalApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let attributes = {key: null}; // Object | Array of attributes
apiInstance.setServerPrivilegedAttributes(serverid, attributes, (error, data, response) => {
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
 **serverid** | **String**| Base64 encoded server id | 
 **attributes** | **Object**| Array of attributes | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateGlobalAttributes

> updateGlobalAttributes(attributes)

Update specified global attributes

Update the specified global attributes. Prior attributes with keys that are not provided in the body of the request will not be deleted. Required permission: &#39;servers&#39;.

### Example

```javascript
import NextAuthApi from 'next_auth_api';
let defaultClient = NextAuthApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: role_id
let role_id = defaultClient.authentications['role_id'];
role_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//role_id.apiKeyPrefix = 'Token';

let apiInstance = new NextAuthApi.GlobalApi();
let attributes = {key: null}; // Object | Array of attributes
apiInstance.updateGlobalAttributes(attributes, (error, data, response) => {
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
 **attributes** | **Object**| Array of attributes | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateServerPrivilegedAttributes

> updateServerPrivilegedAttributes(serverid, attributes)

Update privileged specified attributes of a specific server

Update the specified privileged attributes of a specific server. Prior privileged attributes with keys that are not provided in the body of the request will not be deleted. Required permission: global &#39;servers&#39;.

### Example

```javascript
import NextAuthApi from 'next_auth_api';
let defaultClient = NextAuthApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: role_id
let role_id = defaultClient.authentications['role_id'];
role_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//role_id.apiKeyPrefix = 'Token';

let apiInstance = new NextAuthApi.GlobalApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let attributes = {key: null}; // Object | Array of attributes
apiInstance.updateServerPrivilegedAttributes(serverid, attributes, (error, data, response) => {
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
 **serverid** | **String**| Base64 encoded server id | 
 **attributes** | **Object**| Array of attributes | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

