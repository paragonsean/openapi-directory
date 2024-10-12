# PeerTube.VideoCommentsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1VideosIdCommentThreadsGet**](VideoCommentsApi.md#apiV1VideosIdCommentThreadsGet) | **GET** /api/v1/videos/{id}/comment-threads | List threads of a video
[**apiV1VideosIdCommentThreadsPost**](VideoCommentsApi.md#apiV1VideosIdCommentThreadsPost) | **POST** /api/v1/videos/{id}/comment-threads | Create a thread
[**apiV1VideosIdCommentThreadsThreadIdGet**](VideoCommentsApi.md#apiV1VideosIdCommentThreadsThreadIdGet) | **GET** /api/v1/videos/{id}/comment-threads/{threadId} | Get a thread
[**apiV1VideosIdCommentsCommentIdDelete**](VideoCommentsApi.md#apiV1VideosIdCommentsCommentIdDelete) | **DELETE** /api/v1/videos/{id}/comments/{commentId} | Delete a comment or a reply
[**apiV1VideosIdCommentsCommentIdPost**](VideoCommentsApi.md#apiV1VideosIdCommentsCommentIdPost) | **POST** /api/v1/videos/{id}/comments/{commentId} | Reply to a thread of a video



## apiV1VideosIdCommentThreadsGet

> CommentThreadResponse apiV1VideosIdCommentThreadsGet(id, opts)

List threads of a video

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoCommentsApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "sort_example" // String | Sort comments by criteria
};
apiInstance.apiV1VideosIdCommentThreadsGet(id, opts, (error, data, response) => {
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
 **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | 
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort comments by criteria | [optional] 

### Return type

[**CommentThreadResponse**](CommentThreadResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1VideosIdCommentThreadsPost

> CommentThreadPostResponse apiV1VideosIdCommentThreadsPost(id, opts)

Create a thread

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoCommentsApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
let opts = {
  'apiV1VideosIdCommentThreadsPostRequest': new PeerTube.ApiV1VideosIdCommentThreadsPostRequest() // ApiV1VideosIdCommentThreadsPostRequest | 
};
apiInstance.apiV1VideosIdCommentThreadsPost(id, opts, (error, data, response) => {
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
 **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | 
 **apiV1VideosIdCommentThreadsPostRequest** | [**ApiV1VideosIdCommentThreadsPostRequest**](ApiV1VideosIdCommentThreadsPostRequest.md)|  | [optional] 

### Return type

[**CommentThreadPostResponse**](CommentThreadPostResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiV1VideosIdCommentThreadsThreadIdGet

> VideoCommentThreadTree apiV1VideosIdCommentThreadsThreadIdGet(id, threadId)

Get a thread

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoCommentsApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
let threadId = 56; // Number | The thread id (root comment id)
apiInstance.apiV1VideosIdCommentThreadsThreadIdGet(id, threadId, (error, data, response) => {
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
 **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | 
 **threadId** | **Number**| The thread id (root comment id) | 

### Return type

[**VideoCommentThreadTree**](VideoCommentThreadTree.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1VideosIdCommentsCommentIdDelete

> apiV1VideosIdCommentsCommentIdDelete(id, commentId)

Delete a comment or a reply

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoCommentsApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
let commentId = 56; // Number | The comment id
apiInstance.apiV1VideosIdCommentsCommentIdDelete(id, commentId, (error, data, response) => {
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
 **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | 
 **commentId** | **Number**| The comment id | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1VideosIdCommentsCommentIdPost

> CommentThreadPostResponse apiV1VideosIdCommentsCommentIdPost(id, commentId, opts)

Reply to a thread of a video

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoCommentsApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
let commentId = 56; // Number | The comment id
let opts = {
  'apiV1VideosIdCommentThreadsPostRequest': new PeerTube.ApiV1VideosIdCommentThreadsPostRequest() // ApiV1VideosIdCommentThreadsPostRequest | 
};
apiInstance.apiV1VideosIdCommentsCommentIdPost(id, commentId, opts, (error, data, response) => {
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
 **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | 
 **commentId** | **Number**| The comment id | 
 **apiV1VideosIdCommentThreadsPostRequest** | [**ApiV1VideosIdCommentThreadsPostRequest**](ApiV1VideosIdCommentThreadsPostRequest.md)|  | [optional] 

### Return type

[**CommentThreadPostResponse**](CommentThreadPostResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

