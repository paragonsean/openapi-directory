# Vimeo.ChannelsSubscriptionsAndSubscribersApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkIfUserSubscribedToChannel**](ChannelsSubscriptionsAndSubscribersApi.md#checkIfUserSubscribedToChannel) | **GET** /users/{user_id}/channels/{channel_id} | Check if a user follows a channel
[**checkIfUserSubscribedToChannelAlt1**](ChannelsSubscriptionsAndSubscribersApi.md#checkIfUserSubscribedToChannelAlt1) | **GET** /me/channels/{channel_id} | Check if a user follows a channel
[**getChannelSubscribers**](ChannelsSubscriptionsAndSubscribersApi.md#getChannelSubscribers) | **GET** /channels/{channel_id}/users | Get all the followers of a channel
[**subscribeToChannel**](ChannelsSubscriptionsAndSubscribersApi.md#subscribeToChannel) | **PUT** /users/{user_id}/channels/{channel_id} | Subscribe a user to a specific channel
[**subscribeToChannelAlt1**](ChannelsSubscriptionsAndSubscribersApi.md#subscribeToChannelAlt1) | **PUT** /me/channels/{channel_id} | Subscribe a user to a specific channel
[**unsubscribeFromChannel**](ChannelsSubscriptionsAndSubscribersApi.md#unsubscribeFromChannel) | **DELETE** /users/{user_id}/channels/{channel_id} | Unsubscribe a user from a specific channel
[**unsubscribeFromChannelAlt1**](ChannelsSubscriptionsAndSubscribersApi.md#unsubscribeFromChannelAlt1) | **DELETE** /me/channels/{channel_id} | Unsubscribe a user from a specific channel



## checkIfUserSubscribedToChannel

> checkIfUserSubscribedToChannel(channelId, userId)

Check if a user follows a channel

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

let apiInstance = new Vimeo.ChannelsSubscriptionsAndSubscribersApi();
let channelId = 927; // Number | The ID of the channel.
let userId = 152184; // Number | The ID of the user.
apiInstance.checkIfUserSubscribedToChannel(channelId, userId, (error, data, response) => {
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
- **Accept**: application/json


## checkIfUserSubscribedToChannelAlt1

> checkIfUserSubscribedToChannelAlt1(channelId)

Check if a user follows a channel

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

let apiInstance = new Vimeo.ChannelsSubscriptionsAndSubscribersApi();
let channelId = 927; // Number | The ID of the channel.
apiInstance.checkIfUserSubscribedToChannelAlt1(channelId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannelSubscribers

> [User] getChannelSubscribers(channelId, filter, opts)

Get all the followers of a channel

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

let apiInstance = new Vimeo.ChannelsSubscriptionsAndSubscribersApi();
let channelId = 927; // Number | The ID of the channel.
let filter = "filter_example"; // String | The attribute by which to filter the results.
let opts = {
  'direction': "asc", // String | The sort direction of the results.
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10, // Number | The number of items to show on each page of results, up to a maximum of 100.
  'query': "Stop motion", // String | The search query to use to filter the results.
  'sort': "sort_example" // String | The way to sort the results.
};
apiInstance.getChannelSubscribers(channelId, filter, opts, (error, data, response) => {
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
 **filter** | **String**| The attribute by which to filter the results. | 
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


## subscribeToChannel

> subscribeToChannel(channelId, userId)

Subscribe a user to a specific channel

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

let apiInstance = new Vimeo.ChannelsSubscriptionsAndSubscribersApi();
let channelId = 927; // Number | The ID of the channel.
let userId = 152184; // Number | The ID of the user.
apiInstance.subscribeToChannel(channelId, userId, (error, data, response) => {
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
- **Accept**: application/json


## subscribeToChannelAlt1

> subscribeToChannelAlt1(channelId)

Subscribe a user to a specific channel

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

let apiInstance = new Vimeo.ChannelsSubscriptionsAndSubscribersApi();
let channelId = 927; // Number | The ID of the channel.
apiInstance.subscribeToChannelAlt1(channelId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## unsubscribeFromChannel

> unsubscribeFromChannel(channelId, userId)

Unsubscribe a user from a specific channel

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

let apiInstance = new Vimeo.ChannelsSubscriptionsAndSubscribersApi();
let channelId = 927; // Number | The ID of the channel.
let userId = 152184; // Number | The ID of the user.
apiInstance.unsubscribeFromChannel(channelId, userId, (error, data, response) => {
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
- **Accept**: application/json


## unsubscribeFromChannelAlt1

> unsubscribeFromChannelAlt1(channelId)

Unsubscribe a user from a specific channel

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

let apiInstance = new Vimeo.ChannelsSubscriptionsAndSubscribersApi();
let channelId = 927; // Number | The ID of the channel.
apiInstance.unsubscribeFromChannelAlt1(channelId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

