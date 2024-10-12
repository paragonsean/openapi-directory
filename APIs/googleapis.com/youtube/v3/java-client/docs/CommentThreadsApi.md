# CommentThreadsApi

All URIs are relative to *https://youtube.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**youtubeCommentThreadsInsert**](CommentThreadsApi.md#youtubeCommentThreadsInsert) | **POST** /youtube/v3/commentThreads |  |
| [**youtubeCommentThreadsList**](CommentThreadsApi.md#youtubeCommentThreadsList) | **GET** /youtube/v3/commentThreads |  |


<a id="youtubeCommentThreadsInsert"></a>
# **youtubeCommentThreadsInsert**
> CommentThread youtubeCommentThreadsInsert(part, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, commentThread)



Inserts a new resource into this collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentThreadsApi;

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

    CommentThreadsApi apiInstance = new CommentThreadsApi(defaultClient);
    List<String> part = Arrays.asList(); // List<String> | The *part* parameter identifies the properties that the API response will include. Set the parameter value to snippet. The snippet part has a quota cost of 2 units.
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
    CommentThread commentThread = new CommentThread(); // CommentThread | 
    try {
      CommentThread result = apiInstance.youtubeCommentThreadsInsert(part, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, commentThread);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentThreadsApi#youtubeCommentThreadsInsert");
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
| **part** | [**List&lt;String&gt;**](String.md)| The *part* parameter identifies the properties that the API response will include. Set the parameter value to snippet. The snippet part has a quota cost of 2 units. | |
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
| **commentThread** | [**CommentThread**](CommentThread.md)|  | [optional] |

### Return type

[**CommentThread**](CommentThread.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="youtubeCommentThreadsList"></a>
# **youtubeCommentThreadsList**
> CommentThreadListResponse youtubeCommentThreadsList(part, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, allThreadsRelatedToChannelId, channelId, id, maxResults, moderationStatus, order, pageToken, searchTerms, textFormat, videoId)



Retrieves a list of resources, possibly filtered.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentThreadsApi;

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

    CommentThreadsApi apiInstance = new CommentThreadsApi(defaultClient);
    List<String> part = Arrays.asList(); // List<String> | The *part* parameter specifies a comma-separated list of one or more commentThread resource properties that the API response will include.
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
    String allThreadsRelatedToChannelId = "allThreadsRelatedToChannelId_example"; // String | Returns the comment threads of all videos of the channel and the channel comments as well.
    String channelId = "channelId_example"; // String | Returns the comment threads for all the channel comments (ie does not include comments left on videos).
    List<String> id = Arrays.asList(); // List<String> | Returns the comment threads with the given IDs for Stubby or Apiary.
    Integer maxResults = 56; // Integer | The *maxResults* parameter specifies the maximum number of items that should be returned in the result set.
    String moderationStatus = "published"; // String | Limits the returned comment threads to those with the specified moderation status. Not compatible with the 'id' filter. Valid values: published, heldForReview, likelySpam.
    String order = "orderUnspecified"; // String | 
    String pageToken = "pageToken_example"; // String | The *pageToken* parameter identifies a specific page in the result set that should be returned. In an API response, the nextPageToken and prevPageToken properties identify other pages that could be retrieved.
    String searchTerms = "searchTerms_example"; // String | Limits the returned comment threads to those matching the specified key words. Not compatible with the 'id' filter.
    String textFormat = "textFormatUnspecified"; // String | The requested text format for the returned comments.
    String videoId = "videoId_example"; // String | Returns the comment threads of the specified video.
    try {
      CommentThreadListResponse result = apiInstance.youtubeCommentThreadsList(part, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, allThreadsRelatedToChannelId, channelId, id, maxResults, moderationStatus, order, pageToken, searchTerms, textFormat, videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentThreadsApi#youtubeCommentThreadsList");
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
| **part** | [**List&lt;String&gt;**](String.md)| The *part* parameter specifies a comma-separated list of one or more commentThread resource properties that the API response will include. | |
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
| **allThreadsRelatedToChannelId** | **String**| Returns the comment threads of all videos of the channel and the channel comments as well. | [optional] |
| **channelId** | **String**| Returns the comment threads for all the channel comments (ie does not include comments left on videos). | [optional] |
| **id** | [**List&lt;String&gt;**](String.md)| Returns the comment threads with the given IDs for Stubby or Apiary. | [optional] |
| **maxResults** | **Integer**| The *maxResults* parameter specifies the maximum number of items that should be returned in the result set. | [optional] |
| **moderationStatus** | **String**| Limits the returned comment threads to those with the specified moderation status. Not compatible with the &#39;id&#39; filter. Valid values: published, heldForReview, likelySpam. | [optional] [enum: published, heldForReview, likelySpam, rejected] |
| **order** | **String**|  | [optional] [enum: orderUnspecified, time, relevance] |
| **pageToken** | **String**| The *pageToken* parameter identifies a specific page in the result set that should be returned. In an API response, the nextPageToken and prevPageToken properties identify other pages that could be retrieved. | [optional] |
| **searchTerms** | **String**| Limits the returned comment threads to those matching the specified key words. Not compatible with the &#39;id&#39; filter. | [optional] |
| **textFormat** | **String**| The requested text format for the returned comments. | [optional] [enum: textFormatUnspecified, html, plainText] |
| **videoId** | **String**| Returns the comment threads of the specified video. | [optional] |

### Return type

[**CommentThreadListResponse**](CommentThreadListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

