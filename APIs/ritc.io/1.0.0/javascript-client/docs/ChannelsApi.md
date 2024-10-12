# Ritc.ChannelsApi

All URIs are relative to *https://api.ritc.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addChannel**](ChannelsApi.md#addChannel) | **POST** /channels | 
[**addChannelFunction**](ChannelsApi.md#addChannelFunction) | **POST** /channels/{channel_id}/functions | 
[**getChannel**](ChannelsApi.md#getChannel) | **GET** /channels/{channel_id} | 
[**getChannelFunction**](ChannelsApi.md#getChannelFunction) | **GET** /channels/{channel_id}/functions/{function_id} | 
[**listAnonymousChannels**](ChannelsApi.md#listAnonymousChannels) | **GET** /channels/anonymous | 
[**listChannelFunctions**](ChannelsApi.md#listChannelFunctions) | **GET** /channels/{channel_id}/functions | 
[**listChannels**](ChannelsApi.md#listChannels) | **GET** /channels | 
[**removeChannel**](ChannelsApi.md#removeChannel) | **DELETE** /channels/{channel_id} | 
[**updateChannel**](ChannelsApi.md#updateChannel) | **PATCH** /channels/{channel_id} | 



## addChannel

> ChannelResponse addChannel(channelObject)



Create a channel

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.ChannelsApi();
let channelObject = new Ritc.Channel(); // Channel | Channel information
apiInstance.addChannel(channelObject, (error, data, response) => {
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
 **channelObject** | [**Channel**](Channel.md)| Channel information | 

### Return type

[**ChannelResponse**](ChannelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## addChannelFunction

> FunctionResponse addChannelFunction(channelId, channelFunctionObject)



Create a channel function

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.ChannelsApi();
let channelId = "channelId_example"; // String | Id of Channel
let channelFunctionObject = new Ritc.Function7(); // Function7 | Channel Function information
apiInstance.addChannelFunction(channelId, channelFunctionObject, (error, data, response) => {
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
 **channelId** | **String**| Id of Channel | 
 **channelFunctionObject** | [**Function7**](Function7.md)| Channel Function information | 

### Return type

[**FunctionResponse**](FunctionResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getChannel

> [ChannelResponse] getChannel(channelId)



Get channel information

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.ChannelsApi();
let channelId = "channelId_example"; // String | Id of Channel
apiInstance.getChannel(channelId, (error, data, response) => {
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
 **channelId** | **String**| Id of Channel | 

### Return type

[**[ChannelResponse]**](ChannelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannelFunction

> [FunctionResponse] getChannelFunction(channelId, functionId)



Get channel function information

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.ChannelsApi();
let channelId = "channelId_example"; // String | Id of Channel
let functionId = "functionId_example"; // String | Id of Channel Function
apiInstance.getChannelFunction(channelId, functionId, (error, data, response) => {
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
 **channelId** | **String**| Id of Channel | 
 **functionId** | **String**| Id of Channel Function | 

### Return type

[**[FunctionResponse]**](FunctionResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAnonymousChannels

> [ChannelResponse] listAnonymousChannels()



Retrieve Channels anonymously

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.ChannelsApi();
apiInstance.listAnonymousChannels((error, data, response) => {
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

[**[ChannelResponse]**](ChannelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannelFunctions

> [FunctionResponse] listChannelFunctions(channelId)



Retrieve Channel Functions

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.ChannelsApi();
let channelId = "channelId_example"; // String | Id of Channel
apiInstance.listChannelFunctions(channelId, (error, data, response) => {
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
 **channelId** | **String**| Id of Channel | 

### Return type

[**[FunctionResponse]**](FunctionResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannels

> [ChannelResponse] listChannels()



Retrieve Channels

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.ChannelsApi();
apiInstance.listChannels((error, data, response) => {
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

[**[ChannelResponse]**](ChannelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeChannel

> removeChannel(channelId)



Delete a channel

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.ChannelsApi();
let channelId = "channelId_example"; // String | Id of Channel
apiInstance.removeChannel(channelId, (error, data, response) => {
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
 **channelId** | **String**| Id of Channel | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateChannel

> ChannelResponse updateChannel(channelId, channelObject)



Update a channel

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.ChannelsApi();
let channelId = "channelId_example"; // String | Id of Channel
let channelObject = new Ritc.Rule(); // Rule | Channel information
apiInstance.updateChannel(channelId, channelObject, (error, data, response) => {
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
 **channelId** | **String**| Id of Channel | 
 **channelObject** | [**Rule**](Rule.md)| Channel information | 

### Return type

[**ChannelResponse**](ChannelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

