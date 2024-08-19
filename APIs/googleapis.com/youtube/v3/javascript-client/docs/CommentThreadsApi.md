# YouTubeDataApiV3.CommentThreadsApi

All URIs are relative to *https://youtube.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**youtubeCommentThreadsInsert**](CommentThreadsApi.md#youtubeCommentThreadsInsert) | **POST** /youtube/v3/commentThreads | 
[**youtubeCommentThreadsList**](CommentThreadsApi.md#youtubeCommentThreadsList) | **GET** /youtube/v3/commentThreads | 



## youtubeCommentThreadsInsert

> CommentThread youtubeCommentThreadsInsert(part, opts)



Inserts a new resource into this collection.

### Example

```javascript
import YouTubeDataApiV3 from 'you_tube_data_api_v3';
let defaultClient = YouTubeDataApiV3.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new YouTubeDataApiV3.CommentThreadsApi();
let part = ["null"]; // [String] | The *part* parameter identifies the properties that the API response will include. Set the parameter value to snippet. The snippet part has a quota cost of 2 units.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'commentThread': new YouTubeDataApiV3.CommentThread() // CommentThread | 
};
apiInstance.youtubeCommentThreadsInsert(part, opts, (error, data, response) => {
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
 **part** | [**[String]**](String.md)| The *part* parameter identifies the properties that the API response will include. Set the parameter value to snippet. The snippet part has a quota cost of 2 units. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **commentThread** | [**CommentThread**](CommentThread.md)|  | [optional] 

### Return type

[**CommentThread**](CommentThread.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## youtubeCommentThreadsList

> CommentThreadListResponse youtubeCommentThreadsList(part, opts)



Retrieves a list of resources, possibly filtered.

### Example

```javascript
import YouTubeDataApiV3 from 'you_tube_data_api_v3';
let defaultClient = YouTubeDataApiV3.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new YouTubeDataApiV3.CommentThreadsApi();
let part = ["null"]; // [String] | The *part* parameter specifies a comma-separated list of one or more commentThread resource properties that the API response will include.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'allThreadsRelatedToChannelId': "allThreadsRelatedToChannelId_example", // String | Returns the comment threads of all videos of the channel and the channel comments as well.
  'channelId': "channelId_example", // String | Returns the comment threads for all the channel comments (ie does not include comments left on videos).
  'id': ["null"], // [String] | Returns the comment threads with the given IDs for Stubby or Apiary.
  'maxResults': 56, // Number | The *maxResults* parameter specifies the maximum number of items that should be returned in the result set.
  'moderationStatus': "moderationStatus_example", // String | Limits the returned comment threads to those with the specified moderation status. Not compatible with the 'id' filter. Valid values: published, heldForReview, likelySpam.
  'order': "order_example", // String | 
  'pageToken': "pageToken_example", // String | The *pageToken* parameter identifies a specific page in the result set that should be returned. In an API response, the nextPageToken and prevPageToken properties identify other pages that could be retrieved.
  'searchTerms': "searchTerms_example", // String | Limits the returned comment threads to those matching the specified key words. Not compatible with the 'id' filter.
  'textFormat': "textFormat_example", // String | The requested text format for the returned comments.
  'videoId': "videoId_example" // String | Returns the comment threads of the specified video.
};
apiInstance.youtubeCommentThreadsList(part, opts, (error, data, response) => {
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
 **part** | [**[String]**](String.md)| The *part* parameter specifies a comma-separated list of one or more commentThread resource properties that the API response will include. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **allThreadsRelatedToChannelId** | **String**| Returns the comment threads of all videos of the channel and the channel comments as well. | [optional] 
 **channelId** | **String**| Returns the comment threads for all the channel comments (ie does not include comments left on videos). | [optional] 
 **id** | [**[String]**](String.md)| Returns the comment threads with the given IDs for Stubby or Apiary. | [optional] 
 **maxResults** | **Number**| The *maxResults* parameter specifies the maximum number of items that should be returned in the result set. | [optional] 
 **moderationStatus** | **String**| Limits the returned comment threads to those with the specified moderation status. Not compatible with the &#39;id&#39; filter. Valid values: published, heldForReview, likelySpam. | [optional] 
 **order** | **String**|  | [optional] 
 **pageToken** | **String**| The *pageToken* parameter identifies a specific page in the result set that should be returned. In an API response, the nextPageToken and prevPageToken properties identify other pages that could be retrieved. | [optional] 
 **searchTerms** | **String**| Limits the returned comment threads to those matching the specified key words. Not compatible with the &#39;id&#39; filter. | [optional] 
 **textFormat** | **String**| The requested text format for the returned comments. | [optional] 
 **videoId** | **String**| Returns the comment threads of the specified video. | [optional] 

### Return type

[**CommentThreadListResponse**](CommentThreadListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

