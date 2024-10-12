# StreamChatApi.SettingsApi

All URIs are relative to *https://chat.stream-io-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkPush**](SettingsApi.md#checkPush) | **POST** /check_push | Check push
[**checkSQS**](SettingsApi.md#checkSQS) | **POST** /check_sqs | Check SQS
[**createBlockList**](SettingsApi.md#createBlockList) | **POST** /blocklists | Create block list
[**createChannelType**](SettingsApi.md#createChannelType) | **POST** /channeltypes | Create channel type
[**deleteBlockList**](SettingsApi.md#deleteBlockList) | **DELETE** /blocklists/{name} | Delete block list
[**deleteChannelType**](SettingsApi.md#deleteChannelType) | **DELETE** /channeltypes/{name} | Delete channel type
[**deletePushProvider_0**](SettingsApi.md#deletePushProvider_0) | **DELETE** /push_providers/{type}/{name} | Delete a push provider
[**getApp**](SettingsApi.md#getApp) | **GET** /app | Get App Settings
[**getBlockList**](SettingsApi.md#getBlockList) | **GET** /blocklists/{name} | Get block list
[**getChannelType**](SettingsApi.md#getChannelType) | **GET** /channeltypes/{name} | Get channel type
[**getRateLimits**](SettingsApi.md#getRateLimits) | **GET** /rate_limits | Get rate limits
[**listBlockLists**](SettingsApi.md#listBlockLists) | **GET** /blocklists | List block lists
[**listChannelTypes**](SettingsApi.md#listChannelTypes) | **GET** /channeltypes | List channel types
[**listPushProviders_0**](SettingsApi.md#listPushProviders_0) | **GET** /push_providers | List push providers
[**updateApp**](SettingsApi.md#updateApp) | **PATCH** /app | Update App Settings
[**updateBlockList**](SettingsApi.md#updateBlockList) | **PUT** /blocklists/{name} | Update block list
[**updateChannelType**](SettingsApi.md#updateChannelType) | **PUT** /channeltypes/{name} | Update channel type
[**upsertPushProvider_0**](SettingsApi.md#upsertPushProvider_0) | **POST** /push_providers | Upsert a push provider



## checkPush

> CheckPushResponse checkPush(checkPushRequest)

Check push

Sends a test message via push, this is a test endpoint to verify your push settings 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.SettingsApi();
let checkPushRequest = new StreamChatApi.CheckPushRequest(); // CheckPushRequest | 
apiInstance.checkPush(checkPushRequest, (error, data, response) => {
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
 **checkPushRequest** | [**CheckPushRequest**](CheckPushRequest.md)|  | 

### Return type

[**CheckPushResponse**](CheckPushResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## checkSQS

> CheckSQSResponse checkSQS(checkSQSRequest)

Check SQS

Validates Amazon SQS credentials 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.SettingsApi();
let checkSQSRequest = new StreamChatApi.CheckSQSRequest(); // CheckSQSRequest | 
apiInstance.checkSQS(checkSQSRequest, (error, data, response) => {
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
 **checkSQSRequest** | [**CheckSQSRequest**](CheckSQSRequest.md)|  | 

### Return type

[**CheckSQSResponse**](CheckSQSResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBlockList

> Response createBlockList(createBlockListRequest)

Create block list

Creates a new application blocklist, once created the blocklist can be used by any channel type 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.SettingsApi();
let createBlockListRequest = new StreamChatApi.CreateBlockListRequest(); // CreateBlockListRequest | Block list
apiInstance.createBlockList(createBlockListRequest, (error, data, response) => {
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
 **createBlockListRequest** | [**CreateBlockListRequest**](CreateBlockListRequest.md)| Block list | 

### Return type

[**Response**](Response.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createChannelType

> CreateChannelTypeResponse createChannelType(createChannelTypeRequest)

Create channel type

Creates new channel type 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.SettingsApi();
let createChannelTypeRequest = new StreamChatApi.CreateChannelTypeRequest(); // CreateChannelTypeRequest | 
apiInstance.createChannelType(createChannelTypeRequest, (error, data, response) => {
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
 **createChannelTypeRequest** | [**CreateChannelTypeRequest**](CreateChannelTypeRequest.md)|  | 

### Return type

[**CreateChannelTypeResponse**](CreateChannelTypeResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteBlockList

> Response deleteBlockList(name)

Delete block list

Deletes previously created application blocklist 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.SettingsApi();
let name = "name_example"; // String | 
apiInstance.deleteBlockList(name, (error, data, response) => {
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
 **name** | **String**|  | 

### Return type

[**Response**](Response.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteChannelType

> Response deleteChannelType(name)

Delete channel type

Deletes channel type 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.SettingsApi();
let name = "name_example"; // String | 
apiInstance.deleteChannelType(name, (error, data, response) => {
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
 **name** | **String**|  | 

### Return type

[**Response**](Response.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePushProvider_0

> Response deletePushProvider_0(type, name)

Delete a push provider

Delete a push provider from v2 with multi bundle/package support. v1 isn&#39;t supported in this endpoint 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.SettingsApi();
let type = "type_example"; // String | 
let name = "name_example"; // String | 
apiInstance.deletePushProvider_0(type, name, (error, data, response) => {
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
 **type** | **String**|  | 
 **name** | **String**|  | 

### Return type

[**Response**](Response.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApp

> GetApplicationResponse getApp()

Get App Settings

This method returns the application settings 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.SettingsApi();
apiInstance.getApp((error, data, response) => {
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

[**GetApplicationResponse**](GetApplicationResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBlockList

> GetBlockListResponse getBlockList(name)

Get block list

Returns block list by given name 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.SettingsApi();
let name = "name_example"; // String | 
apiInstance.getBlockList(name, (error, data, response) => {
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
 **name** | **String**|  | 

### Return type

[**GetBlockListResponse**](GetBlockListResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannelType

> Response getChannelType(name)

Get channel type

Gets channel type 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.SettingsApi();
let name = "name_example"; // String | 
apiInstance.getChannelType(name, (error, data, response) => {
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
 **name** | **String**|  | 

### Return type

[**Response**](Response.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRateLimits

> GetRateLimitsResponse getRateLimits(opts)

Get rate limits

Get rate limits usage and quotas 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.SettingsApi();
let opts = {
  'serverSide': true, // Boolean | 
  'android': true, // Boolean | 
  'ios': true, // Boolean | 
  'web': true, // Boolean | 
  'endpoints': "endpoints_example" // String | 
};
apiInstance.getRateLimits(opts, (error, data, response) => {
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
 **serverSide** | **Boolean**|  | [optional] 
 **android** | **Boolean**|  | [optional] 
 **ios** | **Boolean**|  | [optional] 
 **web** | **Boolean**|  | [optional] 
 **endpoints** | **String**|  | [optional] 

### Return type

[**GetRateLimitsResponse**](GetRateLimitsResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBlockLists

> ListBlockListResponse listBlockLists()

List block lists

Returns all available block lists 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.SettingsApi();
apiInstance.listBlockLists((error, data, response) => {
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

[**ListBlockListResponse**](ListBlockListResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannelTypes

> ListChannelTypesResponse listChannelTypes()

List channel types

Lists all available channel types 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.SettingsApi();
apiInstance.listChannelTypes((error, data, response) => {
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

[**ListChannelTypesResponse**](ListChannelTypesResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPushProviders_0

> ListPushProvidersResponse listPushProviders_0()

List push providers

List details of all push providers. 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.SettingsApi();
apiInstance.listPushProviders_0((error, data, response) => {
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

[**ListPushProvidersResponse**](ListPushProvidersResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateApp

> Response updateApp(updateAppRequest)

Update App Settings

This method updates one or more application settings 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.SettingsApi();
let updateAppRequest = new StreamChatApi.UpdateAppRequest(); // UpdateAppRequest | 
apiInstance.updateApp(updateAppRequest, (error, data, response) => {
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
 **updateAppRequest** | [**UpdateAppRequest**](UpdateAppRequest.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateBlockList

> Response updateBlockList(name, updateBlockListRequest)

Update block list

Updates contents of the block list 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.SettingsApi();
let name = "name_example"; // String | 
let updateBlockListRequest = new StreamChatApi.UpdateBlockListRequest(); // UpdateBlockListRequest | 
apiInstance.updateBlockList(name, updateBlockListRequest, (error, data, response) => {
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
 **name** | **String**|  | 
 **updateBlockListRequest** | [**UpdateBlockListRequest**](UpdateBlockListRequest.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateChannelType

> UpdateChannelTypeResponse updateChannelType(name, updateChannelTypeRequest)

Update channel type

Updates channel type 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.SettingsApi();
let name = "name_example"; // String | 
let updateChannelTypeRequest = new StreamChatApi.UpdateChannelTypeRequest(); // UpdateChannelTypeRequest | 
apiInstance.updateChannelType(name, updateChannelTypeRequest, (error, data, response) => {
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
 **name** | **String**|  | 
 **updateChannelTypeRequest** | [**UpdateChannelTypeRequest**](UpdateChannelTypeRequest.md)|  | 

### Return type

[**UpdateChannelTypeResponse**](UpdateChannelTypeResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## upsertPushProvider_0

> UpsertPushProviderResponse upsertPushProvider_0(upsertPushProviderRequest)

Upsert a push provider

Upsert a push provider for v2 with multi bundle/package support 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.SettingsApi();
let upsertPushProviderRequest = new StreamChatApi.UpsertPushProviderRequest(); // UpsertPushProviderRequest | 
apiInstance.upsertPushProvider_0(upsertPushProviderRequest, (error, data, response) => {
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
 **upsertPushProviderRequest** | [**UpsertPushProviderRequest**](UpsertPushProviderRequest.md)|  | 

### Return type

[**UpsertPushProviderResponse**](UpsertPushProviderResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

