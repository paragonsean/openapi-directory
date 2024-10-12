# Vimeo.ChannelsModeratorsApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addChannelModerator**](ChannelsModeratorsApi.md#addChannelModerator) | **PUT** /channels/{channel_id}/moderators/{user_id} | Add a specific channel moderator
[**addChannelModerators**](ChannelsModeratorsApi.md#addChannelModerators) | **PUT** /channels/{channel_id}/moderators | Add a list of channel moderators
[**getChannelModerator**](ChannelsModeratorsApi.md#getChannelModerator) | **GET** /channels/{channel_id}/moderators/{user_id} | Get a specific channel moderator
[**getChannelModerators**](ChannelsModeratorsApi.md#getChannelModerators) | **GET** /channels/{channel_id}/moderators | Get all the moderators in a channel
[**removeChannelModerator**](ChannelsModeratorsApi.md#removeChannelModerator) | **DELETE** /channels/{channel_id}/moderators/{user_id} | Remove a specific channel moderator
[**removeChannelModerators**](ChannelsModeratorsApi.md#removeChannelModerators) | **DELETE** /channels/{channel_id}/moderators | Remove a list of channel moderators
[**replaceChannelModerators**](ChannelsModeratorsApi.md#replaceChannelModerators) | **PATCH** /channels/{channel_id}/moderators | Replace the moderators of a channel



## addChannelModerator

> addChannelModerator(channelId, userId)

Add a specific channel moderator

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.ChannelsModeratorsApi();
let channelId = 927; // Number | The ID of the channel.
let userId = 152184; // Number | The ID of the user.
apiInstance.addChannelModerator(channelId, userId, (error, data, response) => {
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
 **channelId** | **Number**| The ID of the channel. | 
 **userId** | **Number**| The ID of the user. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.user+json


## addChannelModerators

> addChannelModerators(channelId, addChannelModeratorsRequest)

Add a list of channel moderators

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.ChannelsModeratorsApi();
let channelId = 927; // Number | The ID of the channel.
let addChannelModeratorsRequest = new Vimeo.AddChannelModeratorsRequest(); // AddChannelModeratorsRequest | 
apiInstance.addChannelModerators(channelId, addChannelModeratorsRequest, (error, data, response) => {
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
 **channelId** | **Number**| The ID of the channel. | 
 **addChannelModeratorsRequest** | [**AddChannelModeratorsRequest**](AddChannelModeratorsRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getChannelModerator

> User getChannelModerator(channelId, userId)

Get a specific channel moderator

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.ChannelsModeratorsApi();
let channelId = 927; // Number | The ID of the channel.
let userId = 152184; // Number | The ID of the user.
apiInstance.getChannelModerator(channelId, userId, (error, data, response) => {
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
 **channelId** | **Number**| The ID of the channel. | 
 **userId** | **Number**| The ID of the user. | 

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.user+json


## getChannelModerators

> [User] getChannelModerators(channelId, opts)

Get all the moderators in a channel

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.ChannelsModeratorsApi();
let channelId = 927; // Number | The ID of the channel.
let opts = {
  'direction': "asc", // String | The sort direction of the results.
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10, // Number | The number of items to show on each page of results, up to a maximum of 100.
  'query': "Stop motion", // String | The search query to use to filter the results.
  'sort': "sort_example" // String | The way to sort the results.
};
apiInstance.getChannelModerators(channelId, opts, (error, data, response) => {
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
 **channelId** | **Number**| The ID of the channel. | 
 **direction** | **String**| The sort direction of the results. | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 
 **query** | **String**| The search query to use to filter the results. | [optional] 
 **sort** | **String**| The way to sort the results. | [optional] 

### Return type

[**[User]**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.user+json


## removeChannelModerator

> removeChannelModerator(channelId, userId)

Remove a specific channel moderator

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.ChannelsModeratorsApi();
let channelId = 927; // Number | The ID of the channel.
let userId = 152184; // Number | The ID of the user.
apiInstance.removeChannelModerator(channelId, userId, (error, data, response) => {
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
 **channelId** | **Number**| The ID of the channel. | 
 **userId** | **Number**| The ID of the user. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.user+json


## removeChannelModerators

> User removeChannelModerators(channelId, removeChannelModeratorsRequest)

Remove a list of channel moderators

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.ChannelsModeratorsApi();
let channelId = 927; // Number | The ID of the channel.
let removeChannelModeratorsRequest = new Vimeo.RemoveChannelModeratorsRequest(); // RemoveChannelModeratorsRequest | 
apiInstance.removeChannelModerators(channelId, removeChannelModeratorsRequest, (error, data, response) => {
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
 **channelId** | **Number**| The ID of the channel. | 
 **removeChannelModeratorsRequest** | [**RemoveChannelModeratorsRequest**](RemoveChannelModeratorsRequest.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.user+json
- **Accept**: application/vnd.vimeo.user+json


## replaceChannelModerators

> [User] replaceChannelModerators(channelId, replaceChannelModeratorsRequest)

Replace the moderators of a channel

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.ChannelsModeratorsApi();
let channelId = 927; // Number | The ID of the channel.
let replaceChannelModeratorsRequest = new Vimeo.ReplaceChannelModeratorsRequest(); // ReplaceChannelModeratorsRequest | 
apiInstance.replaceChannelModerators(channelId, replaceChannelModeratorsRequest, (error, data, response) => {
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
 **channelId** | **Number**| The ID of the channel. | 
 **replaceChannelModeratorsRequest** | [**ReplaceChannelModeratorsRequest**](ReplaceChannelModeratorsRequest.md)|  | 

### Return type

[**[User]**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

