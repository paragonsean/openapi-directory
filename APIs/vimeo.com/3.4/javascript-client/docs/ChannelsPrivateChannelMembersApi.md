# Vimeo.ChannelsPrivateChannelMembersApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteChannelPrivacyUser**](ChannelsPrivateChannelMembersApi.md#deleteChannelPrivacyUser) | **DELETE** /channels/{channel_id}/privacy/users/{user_id} | Restrict a user from viewing a private channel
[**getChannelPrivacyUsers**](ChannelsPrivateChannelMembersApi.md#getChannelPrivacyUsers) | **GET** /channels/{channel_id}/privacy/users | Get all the users who can view a private channel
[**setChannelPrivacyUser**](ChannelsPrivateChannelMembersApi.md#setChannelPrivacyUser) | **PUT** /channels/{channel_id}/privacy/users/{user_id} | Permit a specific user to view a private channel
[**setChannelPrivacyUsers**](ChannelsPrivateChannelMembersApi.md#setChannelPrivacyUsers) | **PUT** /channels/{channel_id}/privacy/users | Permit a list of users to view a private channel



## deleteChannelPrivacyUser

> deleteChannelPrivacyUser(channelId, userId)

Restrict a user from viewing a private channel

This method prevents a single user from being able to access the specified private channel.

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

let apiInstance = new Vimeo.ChannelsPrivateChannelMembersApi();
let channelId = 927; // Number | The ID of the channel.
let userId = 152184; // Number | The ID of the user.
apiInstance.deleteChannelPrivacyUser(channelId, userId, (error, data, response) => {
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


## getChannelPrivacyUsers

> [User] getChannelPrivacyUsers(channelId, opts)

Get all the users who can view a private channel

This method gets all the users who have access to the specified private channel.

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

let apiInstance = new Vimeo.ChannelsPrivateChannelMembersApi();
let channelId = 927; // Number | The ID of the channel.
let opts = {
  'direction': "asc", // String | The sort direction of the results.
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10 // Number | The number of items to show on each page of results, up to a maximum of 100.
};
apiInstance.getChannelPrivacyUsers(channelId, opts, (error, data, response) => {
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

### Return type

[**[User]**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.user+json


## setChannelPrivacyUser

> setChannelPrivacyUser(channelId, userId)

Permit a specific user to view a private channel

This method gives a single user access to the specified private channel.

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

let apiInstance = new Vimeo.ChannelsPrivateChannelMembersApi();
let channelId = 927; // Number | The ID of the channel.
let userId = 152184; // Number | The ID of the user.
apiInstance.setChannelPrivacyUser(channelId, userId, (error, data, response) => {
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


## setChannelPrivacyUsers

> [User] setChannelPrivacyUsers(channelId, setChannelPrivacyUsersRequest)

Permit a list of users to view a private channel

This method gives multiple users access to the specified private channel.

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

let apiInstance = new Vimeo.ChannelsPrivateChannelMembersApi();
let channelId = 927; // Number | The ID of the channel.
let setChannelPrivacyUsersRequest = new Vimeo.SetChannelPrivacyUsersRequest(); // SetChannelPrivacyUsersRequest | 
apiInstance.setChannelPrivacyUsers(channelId, setChannelPrivacyUsersRequest, (error, data, response) => {
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
 **setChannelPrivacyUsersRequest** | [**SetChannelPrivacyUsersRequest**](SetChannelPrivacyUsersRequest.md)|  | 

### Return type

[**[User]**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.user+json
- **Accept**: application/vnd.vimeo.user+json

