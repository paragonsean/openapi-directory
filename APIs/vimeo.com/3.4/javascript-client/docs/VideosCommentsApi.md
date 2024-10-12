# Vimeo.VideosCommentsApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createComment**](VideosCommentsApi.md#createComment) | **POST** /videos/{video_id}/comments | Add a comment to a video
[**createCommentAlt1**](VideosCommentsApi.md#createCommentAlt1) | **POST** /channels/{channel_id}/videos/{video_id}/comments | Add a comment to a video
[**createCommentReply**](VideosCommentsApi.md#createCommentReply) | **POST** /videos/{video_id}/comments/{comment_id}/replies | Add a reply to a video comment
[**deleteComment**](VideosCommentsApi.md#deleteComment) | **DELETE** /videos/{video_id}/comments/{comment_id} | Delete a video comment
[**editComment**](VideosCommentsApi.md#editComment) | **PATCH** /videos/{video_id}/comments/{comment_id} | Edit a video comment
[**getComment**](VideosCommentsApi.md#getComment) | **GET** /videos/{video_id}/comments/{comment_id} | Get a specific video comment
[**getCommentReplies**](VideosCommentsApi.md#getCommentReplies) | **GET** /videos/{video_id}/comments/{comment_id}/replies | Get all the replies to a video comment
[**getComments**](VideosCommentsApi.md#getComments) | **GET** /videos/{video_id}/comments | Get all the comments on a video
[**getCommentsAlt1**](VideosCommentsApi.md#getCommentsAlt1) | **GET** /channels/{channel_id}/videos/{video_id}/comments | Get all the comments on a video



## createComment

> Comment createComment(videoId, createCommentAlt1Request)

Add a comment to a video

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

let apiInstance = new Vimeo.VideosCommentsApi();
let videoId = 258684937; // Number | The ID of the video.
let createCommentAlt1Request = new Vimeo.CreateCommentAlt1Request(); // CreateCommentAlt1Request | 
apiInstance.createComment(videoId, createCommentAlt1Request, (error, data, response) => {
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
 **createCommentAlt1Request** | [**CreateCommentAlt1Request**](CreateCommentAlt1Request.md)|  | 

### Return type

[**Comment**](Comment.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.comment+json
- **Accept**: application/vnd.vimeo.comment+json


## createCommentAlt1

> Comment createCommentAlt1(channelId, videoId, createCommentAlt1Request)

Add a comment to a video

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

let apiInstance = new Vimeo.VideosCommentsApi();
let channelId = 927; // Number | The ID of the channel.
let videoId = 258684937; // Number | The ID of the video.
let createCommentAlt1Request = new Vimeo.CreateCommentAlt1Request(); // CreateCommentAlt1Request | 
apiInstance.createCommentAlt1(channelId, videoId, createCommentAlt1Request, (error, data, response) => {
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
 **createCommentAlt1Request** | [**CreateCommentAlt1Request**](CreateCommentAlt1Request.md)|  | 

### Return type

[**Comment**](Comment.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.comment+json
- **Accept**: application/vnd.vimeo.comment+json


## createCommentReply

> Comment createCommentReply(commentId, videoId, createCommentReplyRequest)

Add a reply to a video comment

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

let apiInstance = new Vimeo.VideosCommentsApi();
let commentId = 12345; // Number | The ID of the comment.
let videoId = 258684937; // Number | The ID of the video.
let createCommentReplyRequest = new Vimeo.CreateCommentReplyRequest(); // CreateCommentReplyRequest | 
apiInstance.createCommentReply(commentId, videoId, createCommentReplyRequest, (error, data, response) => {
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
 **commentId** | **Number**| The ID of the comment. | 
 **videoId** | **Number**| The ID of the video. | 
 **createCommentReplyRequest** | [**CreateCommentReplyRequest**](CreateCommentReplyRequest.md)|  | 

### Return type

[**Comment**](Comment.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.comment+json
- **Accept**: application/vnd.vimeo.comment+json


## deleteComment

> deleteComment(commentId, videoId)

Delete a video comment

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

let apiInstance = new Vimeo.VideosCommentsApi();
let commentId = 12345; // Number | The ID of the comment.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.deleteComment(commentId, videoId, (error, data, response) => {
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
 **commentId** | **Number**| The ID of the comment. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## editComment

> Comment editComment(commentId, videoId, editCommentRequest)

Edit a video comment

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

let apiInstance = new Vimeo.VideosCommentsApi();
let commentId = 12345; // Number | The ID of the comment.
let videoId = 258684937; // Number | The ID of the video.
let editCommentRequest = new Vimeo.EditCommentRequest(); // EditCommentRequest | 
apiInstance.editComment(commentId, videoId, editCommentRequest, (error, data, response) => {
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
 **commentId** | **Number**| The ID of the comment. | 
 **videoId** | **Number**| The ID of the video. | 
 **editCommentRequest** | [**EditCommentRequest**](EditCommentRequest.md)|  | 

### Return type

[**Comment**](Comment.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.comment+json
- **Accept**: application/vnd.vimeo.comment+json


## getComment

> Comment getComment(commentId, videoId)

Get a specific video comment

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

let apiInstance = new Vimeo.VideosCommentsApi();
let commentId = 12345; // Number | The ID of the comment.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.getComment(commentId, videoId, (error, data, response) => {
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
 **commentId** | **Number**| The ID of the comment. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

[**Comment**](Comment.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.comment+json


## getCommentReplies

> [Comment] getCommentReplies(commentId, videoId, opts)

Get all the replies to a video comment

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

let apiInstance = new Vimeo.VideosCommentsApi();
let commentId = 12345; // Number | The ID of the comment.
let videoId = 258684937; // Number | The ID of the video.
let opts = {
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10 // Number | The number of items to show on each page of results, up to a maximum of 100.
};
apiInstance.getCommentReplies(commentId, videoId, opts, (error, data, response) => {
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
 **commentId** | **Number**| The ID of the comment. | 
 **videoId** | **Number**| The ID of the video. | 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 

### Return type

[**[Comment]**](Comment.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.comment+json


## getComments

> [Comment] getComments(videoId, opts)

Get all the comments on a video

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

let apiInstance = new Vimeo.VideosCommentsApi();
let videoId = 258684937; // Number | The ID of the video.
let opts = {
  'direction': "asc", // String | The sort direction of the results.
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10 // Number | The number of items to show on each page of results, up to a maximum of 100.
};
apiInstance.getComments(videoId, opts, (error, data, response) => {
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
 **direction** | **String**| The sort direction of the results. | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 

### Return type

[**[Comment]**](Comment.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.comment+json


## getCommentsAlt1

> [Comment] getCommentsAlt1(channelId, videoId, opts)

Get all the comments on a video

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

let apiInstance = new Vimeo.VideosCommentsApi();
let channelId = 927; // Number | The ID of the channel.
let videoId = 258684937; // Number | The ID of the video.
let opts = {
  'direction': "asc", // String | The sort direction of the results.
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10 // Number | The number of items to show on each page of results, up to a maximum of 100.
};
apiInstance.getCommentsAlt1(channelId, videoId, opts, (error, data, response) => {
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
 **direction** | **String**| The sort direction of the results. | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 

### Return type

[**[Comment]**](Comment.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.comment+json

