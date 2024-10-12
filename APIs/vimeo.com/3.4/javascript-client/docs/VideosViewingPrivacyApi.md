# Vimeo.VideosViewingPrivacyApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addVideoPrivacyUser**](VideosViewingPrivacyApi.md#addVideoPrivacyUser) | **PUT** /videos/{video_id}/privacy/users/{user_id} | Permit a specific user to view a private video
[**addVideoPrivacyUsers**](VideosViewingPrivacyApi.md#addVideoPrivacyUsers) | **PUT** /videos/{video_id}/privacy/users | Permit a list of users to view a private video
[**addVideoPrivacyUsersAlt1**](VideosViewingPrivacyApi.md#addVideoPrivacyUsersAlt1) | **PUT** /channels/{channel_id}/videos/{video_id}/privacy/users | Permit a list of users to view a private video
[**deleteVideoPrivacyUser**](VideosViewingPrivacyApi.md#deleteVideoPrivacyUser) | **DELETE** /videos/{video_id}/privacy/users/{user_id} | Restrict a user from viewing a private video
[**getVideoPrivacyUsers**](VideosViewingPrivacyApi.md#getVideoPrivacyUsers) | **GET** /videos/{video_id}/privacy/users | Get all the users who can view a user&#39;s private videos by default
[**getVideoPrivacyUsersAlt1**](VideosViewingPrivacyApi.md#getVideoPrivacyUsersAlt1) | **GET** /channels/{channel_id}/videos/{video_id}/privacy/users | Get all the users who can view a user&#39;s private videos by default



## addVideoPrivacyUser

> User addVideoPrivacyUser(userId, videoId)

Permit a specific user to view a private video

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

let apiInstance = new Vimeo.VideosViewingPrivacyApi();
let userId = 152184; // Number | The ID of the user.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.addVideoPrivacyUser(userId, videoId, (error, data, response) => {
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
 **userId** | **Number**| The ID of the user. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.user+json


## addVideoPrivacyUsers

> [User] addVideoPrivacyUsers(videoId)

Permit a list of users to view a private video

The body of this request should follow our [batch request format](https://developer.vimeo.com/api/common-formats#batch-requests). Each object must contain a single &#x60;URI&#x60; field, and the value of this field must be the URI of the user who can view this video.

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

let apiInstance = new Vimeo.VideosViewingPrivacyApi();
let videoId = 258684937; // Number | The ID of the video.
apiInstance.addVideoPrivacyUsers(videoId, (error, data, response) => {
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
 **videoId** | **Number**| The ID of the video. | 

### Return type

[**[User]**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.user+json


## addVideoPrivacyUsersAlt1

> [User] addVideoPrivacyUsersAlt1(channelId, videoId)

Permit a list of users to view a private video

The body of this request should follow our [batch request format](https://developer.vimeo.com/api/common-formats#batch-requests). Each object must contain a single &#x60;URI&#x60; field, and the value of this field must be the URI of the user who can view this video.

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

let apiInstance = new Vimeo.VideosViewingPrivacyApi();
let channelId = 927; // Number | The ID of the channel.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.addVideoPrivacyUsersAlt1(channelId, videoId, (error, data, response) => {
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
 **videoId** | **Number**| The ID of the video. | 

### Return type

[**[User]**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.user+json


## deleteVideoPrivacyUser

> deleteVideoPrivacyUser(userId, videoId)

Restrict a user from viewing a private video

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

let apiInstance = new Vimeo.VideosViewingPrivacyApi();
let userId = 152184; // Number | The ID of the user.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.deleteVideoPrivacyUser(userId, videoId, (error, data, response) => {
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
 **userId** | **Number**| The ID of the user. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVideoPrivacyUsers

> [User] getVideoPrivacyUsers(videoId, opts)

Get all the users who can view a user&#39;s private videos by default

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

let apiInstance = new Vimeo.VideosViewingPrivacyApi();
let videoId = 258684937; // Number | The ID of the video.
let opts = {
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10 // Number | The number of items to show on each page of results, up to a maximum of 100.
};
apiInstance.getVideoPrivacyUsers(videoId, opts, (error, data, response) => {
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
 **videoId** | **Number**| The ID of the video. | 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 

### Return type

[**[User]**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.user+json


## getVideoPrivacyUsersAlt1

> [User] getVideoPrivacyUsersAlt1(channelId, videoId, opts)

Get all the users who can view a user&#39;s private videos by default

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

let apiInstance = new Vimeo.VideosViewingPrivacyApi();
let channelId = 927; // Number | The ID of the channel.
let videoId = 258684937; // Number | The ID of the video.
let opts = {
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10 // Number | The number of items to show on each page of results, up to a maximum of 100.
};
apiInstance.getVideoPrivacyUsersAlt1(channelId, videoId, opts, (error, data, response) => {
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
 **videoId** | **Number**| The ID of the video. | 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 

### Return type

[**[User]**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.user+json

