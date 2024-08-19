# SearchApi

All URIs are relative to *https://youtube.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**youtubeSearchList**](SearchApi.md#youtubeSearchList) | **GET** /youtube/v3/search |  |


<a id="youtubeSearchList"></a>
# **youtubeSearchList**
> SearchListResponse youtubeSearchList(part, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, channelId, channelType, eventType, forContentOwner, forDeveloper, forMine, location, locationRadius, maxResults, onBehalfOfContentOwner, order, pageToken, publishedAfter, publishedBefore, q, regionCode, relevanceLanguage, safeSearch, topicId, type, videoCaption, videoCategoryId, videoDefinition, videoDimension, videoDuration, videoEmbeddable, videoLicense, videoPaidProductPlacement, videoSyndicated, videoType)



Retrieves a list of search resources

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://youtube.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SearchApi apiInstance = new SearchApi(defaultClient);
    List<String> part = Arrays.asList(); // List<String> | The *part* parameter specifies a comma-separated list of one or more search resource properties that the API response will include. Set the parameter value to snippet.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String channelId = "channelId_example"; // String | Filter on resources belonging to this channelId.
    String channelType = "channelTypeUnspecified"; // String | Add a filter on the channel search.
    String eventType = "none"; // String | Filter on the livestream status of the videos.
    Boolean forContentOwner = true; // Boolean | Search owned by a content owner.
    Boolean forDeveloper = true; // Boolean | Restrict the search to only retrieve videos uploaded using the project id of the authenticated user.
    Boolean forMine = true; // Boolean | Search for the private videos of the authenticated user.
    String location = "location_example"; // String | Filter on location of the video
    String locationRadius = "locationRadius_example"; // String | Filter on distance from the location (specified above).
    Integer maxResults = 56; // Integer | The *maxResults* parameter specifies the maximum number of items that should be returned in the result set.
    String onBehalfOfContentOwner = "onBehalfOfContentOwner_example"; // String | *Note:* This parameter is intended exclusively for YouTube content partners. The *onBehalfOfContentOwner* parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.
    String order = "searchSortUnspecified"; // String | Sort order of the results.
    String pageToken = "pageToken_example"; // String | The *pageToken* parameter identifies a specific page in the result set that should be returned. In an API response, the nextPageToken and prevPageToken properties identify other pages that could be retrieved.
    String publishedAfter = "publishedAfter_example"; // String | Filter on resources published after this date.
    String publishedBefore = "publishedBefore_example"; // String | Filter on resources published before this date.
    String q = "q_example"; // String | Textual search terms to match.
    String regionCode = "regionCode_example"; // String | Display the content as seen by viewers in this country.
    String relevanceLanguage = "relevanceLanguage_example"; // String | Return results relevant to this language.
    String safeSearch = "safeSearchSettingUnspecified"; // String | Indicates whether the search results should include restricted content as well as standard content.
    String topicId = "topicId_example"; // String | Restrict results to a particular topic.
    List<String> type = Arrays.asList(); // List<String> | Restrict results to a particular set of resource types from One Platform.
    String videoCaption = "videoCaptionUnspecified"; // String | Filter on the presence of captions on the videos.
    String videoCategoryId = "videoCategoryId_example"; // String | Filter on videos in a specific category.
    String videoDefinition = "any"; // String | Filter on the definition of the videos.
    String videoDimension = "any"; // String | Filter on 3d videos.
    String videoDuration = "videoDurationUnspecified"; // String | Filter on the duration of the videos.
    String videoEmbeddable = "videoEmbeddableUnspecified"; // String | Filter on embeddable videos.
    String videoLicense = "any"; // String | Filter on the license of the videos.
    String videoPaidProductPlacement = "videoPaidProductPlacementUnspecified"; // String | 
    String videoSyndicated = "videoSyndicatedUnspecified"; // String | Filter on syndicated videos.
    String videoType = "videoTypeUnspecified"; // String | Filter on videos of a specific type.
    try {
      SearchListResponse result = apiInstance.youtubeSearchList(part, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, channelId, channelType, eventType, forContentOwner, forDeveloper, forMine, location, locationRadius, maxResults, onBehalfOfContentOwner, order, pageToken, publishedAfter, publishedBefore, q, regionCode, relevanceLanguage, safeSearch, topicId, type, videoCaption, videoCategoryId, videoDefinition, videoDimension, videoDuration, videoEmbeddable, videoLicense, videoPaidProductPlacement, videoSyndicated, videoType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#youtubeSearchList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **part** | [**List&lt;String&gt;**](String.md)| The *part* parameter specifies a comma-separated list of one or more search resource properties that the API response will include. Set the parameter value to snippet. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **channelId** | **String**| Filter on resources belonging to this channelId. | [optional] |
| **channelType** | **String**| Add a filter on the channel search. | [optional] [enum: channelTypeUnspecified, any, show] |
| **eventType** | **String**| Filter on the livestream status of the videos. | [optional] [enum: none, upcoming, live, completed] |
| **forContentOwner** | **Boolean**| Search owned by a content owner. | [optional] |
| **forDeveloper** | **Boolean**| Restrict the search to only retrieve videos uploaded using the project id of the authenticated user. | [optional] |
| **forMine** | **Boolean**| Search for the private videos of the authenticated user. | [optional] |
| **location** | **String**| Filter on location of the video | [optional] |
| **locationRadius** | **String**| Filter on distance from the location (specified above). | [optional] |
| **maxResults** | **Integer**| The *maxResults* parameter specifies the maximum number of items that should be returned in the result set. | [optional] |
| **onBehalfOfContentOwner** | **String**| *Note:* This parameter is intended exclusively for YouTube content partners. The *onBehalfOfContentOwner* parameter indicates that the request&#39;s authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner. | [optional] |
| **order** | **String**| Sort order of the results. | [optional] [enum: searchSortUnspecified, date, rating, viewCount, relevance, title, videoCount] |
| **pageToken** | **String**| The *pageToken* parameter identifies a specific page in the result set that should be returned. In an API response, the nextPageToken and prevPageToken properties identify other pages that could be retrieved. | [optional] |
| **publishedAfter** | **String**| Filter on resources published after this date. | [optional] |
| **publishedBefore** | **String**| Filter on resources published before this date. | [optional] |
| **q** | **String**| Textual search terms to match. | [optional] |
| **regionCode** | **String**| Display the content as seen by viewers in this country. | [optional] |
| **relevanceLanguage** | **String**| Return results relevant to this language. | [optional] |
| **safeSearch** | **String**| Indicates whether the search results should include restricted content as well as standard content. | [optional] [enum: safeSearchSettingUnspecified, none, moderate, strict] |
| **topicId** | **String**| Restrict results to a particular topic. | [optional] |
| **type** | [**List&lt;String&gt;**](String.md)| Restrict results to a particular set of resource types from One Platform. | [optional] |
| **videoCaption** | **String**| Filter on the presence of captions on the videos. | [optional] [enum: videoCaptionUnspecified, any, closedCaption, none] |
| **videoCategoryId** | **String**| Filter on videos in a specific category. | [optional] |
| **videoDefinition** | **String**| Filter on the definition of the videos. | [optional] [enum: any, standard, high] |
| **videoDimension** | **String**| Filter on 3d videos. | [optional] [enum: any, 2d, 3d] |
| **videoDuration** | **String**| Filter on the duration of the videos. | [optional] [enum: videoDurationUnspecified, any, short, medium, long] |
| **videoEmbeddable** | **String**| Filter on embeddable videos. | [optional] [enum: videoEmbeddableUnspecified, any, true] |
| **videoLicense** | **String**| Filter on the license of the videos. | [optional] [enum: any, youtube, creativeCommon] |
| **videoPaidProductPlacement** | **String**|  | [optional] [enum: videoPaidProductPlacementUnspecified, any, true] |
| **videoSyndicated** | **String**| Filter on syndicated videos. | [optional] [enum: videoSyndicatedUnspecified, any, true] |
| **videoType** | **String**| Filter on videos of a specific type. | [optional] [enum: videoTypeUnspecified, any, movie, episode] |

### Return type

[**SearchListResponse**](SearchListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

