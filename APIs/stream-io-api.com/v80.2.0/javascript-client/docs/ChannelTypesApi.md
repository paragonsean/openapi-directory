# StreamChatApi.ChannelTypesApi

All URIs are relative to *https://chat.stream-io-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createChannelType_0**](ChannelTypesApi.md#createChannelType_0) | **POST** /channeltypes | Create channel type
[**deleteChannelType_0**](ChannelTypesApi.md#deleteChannelType_0) | **DELETE** /channeltypes/{name} | Delete channel type
[**getChannelType_0**](ChannelTypesApi.md#getChannelType_0) | **GET** /channeltypes/{name} | Get channel type
[**listChannelTypes_0**](ChannelTypesApi.md#listChannelTypes_0) | **GET** /channeltypes | List channel types
[**updateChannelType_0**](ChannelTypesApi.md#updateChannelType_0) | **PUT** /channeltypes/{name} | Update channel type



## createChannelType_0

> CreateChannelTypeResponse createChannelType_0(createChannelTypeRequest)

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

let apiInstance = new StreamChatApi.ChannelTypesApi();
let createChannelTypeRequest = new StreamChatApi.CreateChannelTypeRequest(); // CreateChannelTypeRequest | 
apiInstance.createChannelType_0(createChannelTypeRequest, (error, data, response) => {
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


## deleteChannelType_0

> Response deleteChannelType_0(name)

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

let apiInstance = new StreamChatApi.ChannelTypesApi();
let name = "name_example"; // String | 
apiInstance.deleteChannelType_0(name, (error, data, response) => {
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


## getChannelType_0

> Response getChannelType_0(name)

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

let apiInstance = new StreamChatApi.ChannelTypesApi();
let name = "name_example"; // String | 
apiInstance.getChannelType_0(name, (error, data, response) => {
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


## listChannelTypes_0

> ListChannelTypesResponse listChannelTypes_0()

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

let apiInstance = new StreamChatApi.ChannelTypesApi();
apiInstance.listChannelTypes_0((error, data, response) => {
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


## updateChannelType_0

> UpdateChannelTypeResponse updateChannelType_0(name, updateChannelTypeRequest)

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

let apiInstance = new StreamChatApi.ChannelTypesApi();
let name = "name_example"; // String | 
let updateChannelTypeRequest = new StreamChatApi.UpdateChannelTypeRequest(); // UpdateChannelTypeRequest | 
apiInstance.updateChannelType_0(name, updateChannelTypeRequest, (error, data, response) => {
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

