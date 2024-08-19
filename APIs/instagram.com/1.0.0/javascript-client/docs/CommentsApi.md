# InstagramApi.CommentsApi

All URIs are relative to *https://api.instagram.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mediaMediaIdCommentsCommentIdDelete**](CommentsApi.md#mediaMediaIdCommentsCommentIdDelete) | **DELETE** /media/{media-id}/comments/{comment-id} | Remove a comment.
[**mediaMediaIdCommentsGet**](CommentsApi.md#mediaMediaIdCommentsGet) | **GET** /media/{media-id}/comments | Get a list of recent comments on a media object.
[**mediaMediaIdCommentsPost**](CommentsApi.md#mediaMediaIdCommentsPost) | **POST** /media/{media-id}/comments | Create a comment on a media object.



## mediaMediaIdCommentsCommentIdDelete

> StatusResponse mediaMediaIdCommentsCommentIdDelete(mediaId, commentId)

Remove a comment.

Remove a comment either on the authenticated user&#39;s media object or authored by the authenticated user. 

### Example

```javascript
import InstagramApi from 'instagram_api';
let defaultClient = InstagramApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: instagram_auth
let instagram_auth = defaultClient.authentications['instagram_auth'];
instagram_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new InstagramApi.CommentsApi();
let mediaId = "mediaId_example"; // String | The ID of the media resource.
let commentId = "commentId_example"; // String | The ID of the comment entry.
apiInstance.mediaMediaIdCommentsCommentIdDelete(mediaId, commentId, (error, data, response) => {
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
 **mediaId** | **String**| The ID of the media resource. | 
 **commentId** | **String**| The ID of the comment entry. | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mediaMediaIdCommentsGet

> CommentsResponse mediaMediaIdCommentsGet(mediaId)

Get a list of recent comments on a media object.

Get a list of recent comments on a media object.

### Example

```javascript
import InstagramApi from 'instagram_api';
let defaultClient = InstagramApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: instagram_auth
let instagram_auth = defaultClient.authentications['instagram_auth'];
instagram_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new InstagramApi.CommentsApi();
let mediaId = "mediaId_example"; // String | The ID of the media resource.
apiInstance.mediaMediaIdCommentsGet(mediaId, (error, data, response) => {
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
 **mediaId** | **String**| The ID of the media resource. | 

### Return type

[**CommentsResponse**](CommentsResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mediaMediaIdCommentsPost

> StatusResponse mediaMediaIdCommentsPost(mediaId, text)

Create a comment on a media object.

Create a comment on a media object with the following rules:    * The total length of the comment cannot exceed 300 characters.   * The comment cannot contain more than 4 hashtags.   * The comment cannot contain more than 1 URL.   * The comment cannot consist of all capital letters. 

### Example

```javascript
import InstagramApi from 'instagram_api';
let defaultClient = InstagramApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: instagram_auth
let instagram_auth = defaultClient.authentications['instagram_auth'];
instagram_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new InstagramApi.CommentsApi();
let mediaId = "mediaId_example"; // String | The ID of the media resource.
let text = "text_example"; // String | Text to post as a comment on the media object as specified in `media-id`.
apiInstance.mediaMediaIdCommentsPost(mediaId, text, (error, data, response) => {
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
 **mediaId** | **String**| The ID of the media resource. | 
 **text** | **String**| Text to post as a comment on the media object as specified in &#x60;media-id&#x60;. | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

