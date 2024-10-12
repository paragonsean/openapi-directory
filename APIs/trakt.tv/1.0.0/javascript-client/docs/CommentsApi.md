# TraktApi.CommentsApi

All URIs are relative to *https://api.trakt.tv*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteACommentOrReply**](CommentsApi.md#deleteACommentOrReply) | **DELETE** /comments/{id} | Delete a comment or reply
[**getACommentOrReply**](CommentsApi.md#getACommentOrReply) | **GET** /comments/{id} | Get a comment or reply
[**getAllUsersWhoLikedAComment**](CommentsApi.md#getAllUsersWhoLikedAComment) | **GET** /comments/{id}/likes | Get all users who liked a comment
[**getRecentlyCreatedComments**](CommentsApi.md#getRecentlyCreatedComments) | **GET** /comments/recent/{comment_type}/{type} | Get recently created comments
[**getRecentlyUpdatedComments**](CommentsApi.md#getRecentlyUpdatedComments) | **GET** /comments/updates/{comment_type}/{type} | Get recently updated comments
[**getRepliesForAComment**](CommentsApi.md#getRepliesForAComment) | **GET** /comments/{id}/replies | Get replies for a comment
[**getTheAttachedMediaItem**](CommentsApi.md#getTheAttachedMediaItem) | **GET** /comments/{id}/item | Get the attached media item
[**getTrendingComments**](CommentsApi.md#getTrendingComments) | **GET** /comments/trending/{comment_type}/{type} | Get trending comments
[**likeAComment**](CommentsApi.md#likeAComment) | **POST** /comments/{id}/like | Like a comment
[**postAComment**](CommentsApi.md#postAComment) | **POST** /comments | Post a comment
[**postAReplyForAComment**](CommentsApi.md#postAReplyForAComment) | **POST** /comments/{id}/replies | Post a reply for a comment
[**removeLikeOnAComment**](CommentsApi.md#removeLikeOnAComment) | **DELETE** /comments/{id}/like | Remove like on a comment
[**updateACommentOrReply**](CommentsApi.md#updateACommentOrReply) | **PUT** /comments/{id} | Update a comment or reply



## deleteACommentOrReply

> deleteACommentOrReply(id, opts)

Delete a comment or reply

#### &amp;#128274; OAuth Required  Delete a single comment. The OAuth user must match the author of the comment in order to delete it. If not, a &#x60;401&#x60; HTTP status code is returned. The comment must also be less than 2 weeks old or have 0 replies. If not, a &#x60;409&#x60; HTTP status is returned.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.CommentsApi();
let id = "id_example"; // String | Automatically added
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.deleteACommentOrReply(id, opts, (error, data, response) => {
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
 **id** | **String**| Automatically added | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getACommentOrReply

> getACommentOrReply(id, opts)

Get a comment or reply

####  &amp;#128513; Emojis  Returns a single comment and indicates how many replies it has. Use [**_/comments/:id/replies**](/reference/comments/replies/) to get the actual replies.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.CommentsApi();
let id = "417"; // String | A specific comment ID.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getACommentOrReply(id, opts, (error, data, response) => {
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
 **id** | **String**| A specific comment ID. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllUsersWhoLikedAComment

> getAllUsersWhoLikedAComment(id, opts)

Get all users who liked a comment

#### &amp;#128196; Pagination  Returns all users who liked a comment. If you only need the &#x60;replies&#x60; count, the main &#x60;comment&#x60; object already has that, so no need to use this method.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.CommentsApi();
let id = 417; // Number | A specific comment ID.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAllUsersWhoLikedAComment(id, opts, (error, data, response) => {
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
 **id** | **Number**| A specific comment ID. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRecentlyCreatedComments

> getRecentlyCreatedComments(commentType, type, opts)

Get recently created comments

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#128513; Emojis  Returns the most recently written comments across all of Trakt. You can optionally filter by the &#x60;comment_type&#x60; and media &#x60;type&#x60; to limit what gets returned. If you want to &#x60;include_replies&#x60; that will return replies in place alongside top level comments.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.CommentsApi();
let commentType = "all"; // String | 
let type = "all"; // String | 
let opts = {
  'includeReplies': "false", // String | include comment replies
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getRecentlyCreatedComments(commentType, type, opts, (error, data, response) => {
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
 **commentType** | **String**|  | 
 **type** | **String**|  | 
 **includeReplies** | **String**| include comment replies | [optional] 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRecentlyUpdatedComments

> getRecentlyUpdatedComments(commentType, type, opts)

Get recently updated comments

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#128513; Emojis  Returns the most recently updated comments across all of Trakt. You can optionally filter by the &#x60;comment_type&#x60; and media &#x60;type&#x60; to limit what gets returned. If you want to &#x60;include_replies&#x60; that will return replies in place alongside top level comments.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.CommentsApi();
let commentType = "all"; // String | 
let type = "all"; // String | 
let opts = {
  'includeReplies': "false", // String | include comment replies
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getRecentlyUpdatedComments(commentType, type, opts, (error, data, response) => {
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
 **commentType** | **String**|  | 
 **type** | **String**|  | 
 **includeReplies** | **String**| include comment replies | [optional] 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRepliesForAComment

> getRepliesForAComment(id, opts)

Get replies for a comment

#### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all replies for a comment. It is possible these replies could have replies themselves, so in that case you would just call [**_/comments/:id/replies**](/reference/comments/replies/) again with the new comment &#x60;id&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.CommentsApi();
let id = "417"; // String | A specific comment ID.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getRepliesForAComment(id, opts, (error, data, response) => {
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
 **id** | **String**| A specific comment ID. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTheAttachedMediaItem

> getTheAttachedMediaItem(id, opts)

Get the attached media item

#### &amp;#10024; Extended Info  Returns the media item this comment is attached to. The media type can be &#x60;movie&#x60;, &#x60;show&#x60;, &#x60;season&#x60;, &#x60;episode&#x60;, or &#x60;list&#x60; and it also returns the standard media object for that media type.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.CommentsApi();
let id = 417; // Number | A specific comment ID.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getTheAttachedMediaItem(id, opts, (error, data, response) => {
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
 **id** | **Number**| A specific comment ID. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrendingComments

> getTrendingComments(commentType, type, opts)

Get trending comments

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#128513; Emojis  Returns all comments with the most likes and replies over the last 7 days. You can optionally filter by the &#x60;comment_type&#x60; and media &#x60;type&#x60; to limit what gets returned. If you want to &#x60;include_replies&#x60; that will return replies in place alongside top level comments.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.CommentsApi();
let commentType = "all"; // String | 
let type = "all"; // String | 
let opts = {
  'includeReplies': "false", // String | include comment replies
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getTrendingComments(commentType, type, opts, (error, data, response) => {
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
 **commentType** | **String**|  | 
 **type** | **String**|  | 
 **includeReplies** | **String**| include comment replies | [optional] 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## likeAComment

> likeAComment(id, opts)

Like a comment

#### &amp;#128274; OAuth Required  Votes help determine popular comments. Only one like is allowed per comment per user.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.CommentsApi();
let id = "417"; // String | A specific comment ID.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.likeAComment(id, opts, (error, data, response) => {
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
 **id** | **String**| A specific comment ID. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postAComment

> postAComment(opts)

Post a comment

#### &amp;#128274; OAuth Required &amp;#128513; Emojis  Add a new comment to a movie, show, season, episode, or list. Make sure to allow and encourage *spoilers* to be indicated in your app and follow the rules listed above.  #### JSON POST Data  | Key | Type | Default | Value | |---|---|---|---| | item &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | object | | &#x60;movie&#x60;, &#x60;show&#x60;, &#x60;season&#x60;, &#x60;episode&#x60;, or &#x60;list&#x60; object. (see examples &amp;#8594;) | | &#x60;comment&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string |  | Text for the comment. | | &#x60;spoiler&#x60; | boolean | &#x60;false&#x60; | Is this a spoiler? | | &#x60;sharing&#x60;  | object | | Control sharing to any connected social networks. (see below &amp;#8595;) |  #### Sharing  The &#x60;sharing&#x60; object is optional and will apply the user&#39;s settings if not sent. If &#x60;sharing&#x60; is sent, each key will override the user&#39;s setting for that social network. Send &#x60;true&#x60; to post or &#x60;false&#x60; to not post on the indicated social network. You can see which social networks a user has connected with the [**_/users/settings**](/reference/users/settings) method.  | Key | Type | |---|---| | &#x60;twitter&#x60; | boolean | | &#x60;tumblr&#x60; | boolean | | &#x60;medium&#x60; | boolean |

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.CommentsApi();
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]", // String | e.g. [client_id]
  'postACommentRequest': new TraktApi.PostACommentRequest() // PostACommentRequest | 
};
apiInstance.postAComment(opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 
 **postACommentRequest** | [**PostACommentRequest**](PostACommentRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postAReplyForAComment

> postAReplyForAComment(id, opts)

Post a reply for a comment

#### &amp;#128274; OAuth Required &amp;#128513; Emojis  Add a new reply to an existing comment. Make sure to allow and encourage *spoilers* to be indicated in your app and follow the rules listed above.  #### JSON POST Data  | Key | Type | Default | Value | |---|---|---|---| | &#x60;comment&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string |  | Text for the reply. | | &#x60;spoiler&#x60; | boolean | &#x60;false&#x60; | Is this a spoiler? |

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.CommentsApi();
let id = "id_example"; // String | Automatically added
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]", // String | e.g. [client_id]
  'postAReplyForACommentRequest': new TraktApi.PostAReplyForACommentRequest() // PostAReplyForACommentRequest | 
};
apiInstance.postAReplyForAComment(id, opts, (error, data, response) => {
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
 **id** | **String**| Automatically added | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 
 **postAReplyForACommentRequest** | [**PostAReplyForACommentRequest**](PostAReplyForACommentRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeLikeOnAComment

> removeLikeOnAComment(id, opts)

Remove like on a comment

#### &amp;#128274; OAuth Required  Remove a like on a comment.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.CommentsApi();
let id = "id_example"; // String | Automatically added
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.removeLikeOnAComment(id, opts, (error, data, response) => {
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
 **id** | **String**| Automatically added | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateACommentOrReply

> updateACommentOrReply(id, opts)

Update a comment or reply

#### &amp;#128274; OAuth Required &amp;#128513; Emojis  Update a single comment. The OAuth user must match the author of the comment in order to update it. If not, a &#x60;401&#x60; HTTP status is returned.  #### JSON POST Data  | Key | Type | Default | Value | |---|---|---|---| | &#x60;comment&#x60; | string |  | Text for the comment. | | &#x60;spoiler&#x60; | boolean | &#x60;false&#x60; | Is this a spoiler? |

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.CommentsApi();
let id = "id_example"; // String | Automatically added
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]", // String | e.g. [client_id]
  'updateACommentOrReplyRequest': new TraktApi.UpdateACommentOrReplyRequest() // UpdateACommentOrReplyRequest | 
};
apiInstance.updateACommentOrReply(id, opts, (error, data, response) => {
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
 **id** | **String**| Automatically added | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 
 **updateACommentOrReplyRequest** | [**UpdateACommentOrReplyRequest**](UpdateACommentOrReplyRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

