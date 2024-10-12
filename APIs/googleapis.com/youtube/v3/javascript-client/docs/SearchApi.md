# YouTubeDataApiV3.SearchApi

All URIs are relative to *https://youtube.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**youtubeSearchList**](SearchApi.md#youtubeSearchList) | **GET** /youtube/v3/search | 



## youtubeSearchList

> SearchListResponse youtubeSearchList(part, opts)



Retrieves a list of search resources

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

let apiInstance = new YouTubeDataApiV3.SearchApi();
let part = ["null"]; // [String] | The *part* parameter specifies a comma-separated list of one or more search resource properties that the API response will include. Set the parameter value to snippet.
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
  'channelId': "channelId_example", // String | Filter on resources belonging to this channelId.
  'channelType': "channelType_example", // String | Add a filter on the channel search.
  'eventType': "eventType_example", // String | Filter on the livestream status of the videos.
  'forContentOwner': true, // Boolean | Search owned by a content owner.
  'forDeveloper': true, // Boolean | Restrict the search to only retrieve videos uploaded using the project id of the authenticated user.
  'forMine': true, // Boolean | Search for the private videos of the authenticated user.
  'location': "location_example", // String | Filter on location of the video
  'locationRadius': "locationRadius_example", // String | Filter on distance from the location (specified above).
  'maxResults': 56, // Number | The *maxResults* parameter specifies the maximum number of items that should be returned in the result set.
  'onBehalfOfContentOwner': "onBehalfOfContentOwner_example", // String | *Note:* This parameter is intended exclusively for YouTube content partners. The *onBehalfOfContentOwner* parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.
  'order': "order_example", // String | Sort order of the results.
  'pageToken': "pageToken_example", // String | The *pageToken* parameter identifies a specific page in the result set that should be returned. In an API response, the nextPageToken and prevPageToken properties identify other pages that could be retrieved.
  'publishedAfter': "publishedAfter_example", // String | Filter on resources published after this date.
  'publishedBefore': "publishedBefore_example", // String | Filter on resources published before this date.
  'q': "q_example", // String | Textual search terms to match.
  'regionCode': "regionCode_example", // String | Display the content as seen by viewers in this country.
  'relevanceLanguage': "relevanceLanguage_example", // String | Return results relevant to this language.
  'safeSearch': "safeSearch_example", // String | Indicates whether the search results should include restricted content as well as standard content.
  'topicId': "topicId_example", // String | Restrict results to a particular topic.
  'type': ["null"], // [String] | Restrict results to a particular set of resource types from One Platform.
  'videoCaption': "videoCaption_example", // String | Filter on the presence of captions on the videos.
  'videoCategoryId': "videoCategoryId_example", // String | Filter on videos in a specific category.
  'videoDefinition': "videoDefinition_example", // String | Filter on the definition of the videos.
  'videoDimension': "videoDimension_example", // String | Filter on 3d videos.
  'videoDuration': "videoDuration_example", // String | Filter on the duration of the videos.
  'videoEmbeddable': "videoEmbeddable_example", // String | Filter on embeddable videos.
  'videoLicense': "videoLicense_example", // String | Filter on the license of the videos.
  'videoPaidProductPlacement': "videoPaidProductPlacement_example", // String | 
  'videoSyndicated': "videoSyndicated_example", // String | Filter on syndicated videos.
  'videoType': "videoType_example" // String | Filter on videos of a specific type.
};
apiInstance.youtubeSearchList(part, opts, (error, data, response) => {
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
 **part** | [**[String]**](String.md)| The *part* parameter specifies a comma-separated list of one or more search resource properties that the API response will include. Set the parameter value to snippet. | 
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
 **channelId** | **String**| Filter on resources belonging to this channelId. | [optional] 
 **channelType** | **String**| Add a filter on the channel search. | [optional] 
 **eventType** | **String**| Filter on the livestream status of the videos. | [optional] 
 **forContentOwner** | **Boolean**| Search owned by a content owner. | [optional] 
 **forDeveloper** | **Boolean**| Restrict the search to only retrieve videos uploaded using the project id of the authenticated user. | [optional] 
 **forMine** | **Boolean**| Search for the private videos of the authenticated user. | [optional] 
 **location** | **String**| Filter on location of the video | [optional] 
 **locationRadius** | **String**| Filter on distance from the location (specified above). | [optional] 
 **maxResults** | **Number**| The *maxResults* parameter specifies the maximum number of items that should be returned in the result set. | [optional] 
 **onBehalfOfContentOwner** | **String**| *Note:* This parameter is intended exclusively for YouTube content partners. The *onBehalfOfContentOwner* parameter indicates that the request&#39;s authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner. | [optional] 
 **order** | **String**| Sort order of the results. | [optional] 
 **pageToken** | **String**| The *pageToken* parameter identifies a specific page in the result set that should be returned. In an API response, the nextPageToken and prevPageToken properties identify other pages that could be retrieved. | [optional] 
 **publishedAfter** | **String**| Filter on resources published after this date. | [optional] 
 **publishedBefore** | **String**| Filter on resources published before this date. | [optional] 
 **q** | **String**| Textual search terms to match. | [optional] 
 **regionCode** | **String**| Display the content as seen by viewers in this country. | [optional] 
 **relevanceLanguage** | **String**| Return results relevant to this language. | [optional] 
 **safeSearch** | **String**| Indicates whether the search results should include restricted content as well as standard content. | [optional] 
 **topicId** | **String**| Restrict results to a particular topic. | [optional] 
 **type** | [**[String]**](String.md)| Restrict results to a particular set of resource types from One Platform. | [optional] 
 **videoCaption** | **String**| Filter on the presence of captions on the videos. | [optional] 
 **videoCategoryId** | **String**| Filter on videos in a specific category. | [optional] 
 **videoDefinition** | **String**| Filter on the definition of the videos. | [optional] 
 **videoDimension** | **String**| Filter on 3d videos. | [optional] 
 **videoDuration** | **String**| Filter on the duration of the videos. | [optional] 
 **videoEmbeddable** | **String**| Filter on embeddable videos. | [optional] 
 **videoLicense** | **String**| Filter on the license of the videos. | [optional] 
 **videoPaidProductPlacement** | **String**|  | [optional] 
 **videoSyndicated** | **String**| Filter on syndicated videos. | [optional] 
 **videoType** | **String**| Filter on videos of a specific type. | [optional] 

### Return type

[**SearchListResponse**](SearchListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

