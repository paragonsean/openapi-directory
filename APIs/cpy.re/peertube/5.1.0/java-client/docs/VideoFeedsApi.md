# VideoFeedsApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSyndicatedComments**](VideoFeedsApi.md#getSyndicatedComments) | **GET** /feeds/video-comments.{format} | List comments on videos |
| [**getSyndicatedSubscriptionVideos**](VideoFeedsApi.md#getSyndicatedSubscriptionVideos) | **GET** /feeds/subscriptions.{format} | List videos of subscriptions tied to a token |
| [**getSyndicatedVideos**](VideoFeedsApi.md#getSyndicatedVideos) | **GET** /feeds/videos.{format} | List videos |


<a id="getSyndicatedComments"></a>
# **getSyndicatedComments**
> List&lt;VideoCommentsForXMLInner&gt; getSyndicatedComments(format, videoId, accountId, accountName, videoChannelId, videoChannelName)

List comments on videos

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoFeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoFeedsApi apiInstance = new VideoFeedsApi(defaultClient);
    String format = "xml"; // String | format expected (we focus on making `rss` the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss))
    String videoId = "videoId_example"; // String | limit listing to a specific video
    String accountId = "accountId_example"; // String | limit listing to a specific account
    String accountName = "accountName_example"; // String | limit listing to a specific account
    String videoChannelId = "videoChannelId_example"; // String | limit listing to a specific video channel
    String videoChannelName = "videoChannelName_example"; // String | limit listing to a specific video channel
    try {
      List<VideoCommentsForXMLInner> result = apiInstance.getSyndicatedComments(format, videoId, accountId, accountName, videoChannelId, videoChannelName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoFeedsApi#getSyndicatedComments");
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
| **format** | **String**| format expected (we focus on making &#x60;rss&#x60; the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss)) | [enum: xml, rss, rss2, atom, atom1, json, json1] |
| **videoId** | **String**| limit listing to a specific video | [optional] |
| **accountId** | **String**| limit listing to a specific account | [optional] |
| **accountName** | **String**| limit listing to a specific account | [optional] |
| **videoChannelId** | **String**| limit listing to a specific video channel | [optional] |
| **videoChannelName** | **String**| limit listing to a specific video channel | [optional] |

### Return type

[**List&lt;VideoCommentsForXMLInner&gt;**](VideoCommentsForXMLInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/atom+xml, application/json, application/rss+xml, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  * Cache-Control -  <br>  |
| **400** | Arises when:   - videoId filter is mixed with a channel filter  |  -  |
| **404** | video, video channel or account not found |  -  |
| **406** | accept header unsupported |  -  |

<a id="getSyndicatedSubscriptionVideos"></a>
# **getSyndicatedSubscriptionVideos**
> List&lt;VideosForXMLInner&gt; getSyndicatedSubscriptionVideos(format, accountId, token, sort, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles)

List videos of subscriptions tied to a token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoFeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoFeedsApi apiInstance = new VideoFeedsApi(defaultClient);
    String format = "xml"; // String | format expected (we focus on making `rss` the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss))
    String accountId = "accountId_example"; // String | limit listing to a specific account
    String token = "token_example"; // String | private token allowing access
    String sort = "-createdAt"; // String | Sort column
    String nsfw = "true"; // String | whether to include nsfw videos, if any
    Boolean isLocal = true; // Boolean | **PeerTube >= 4.0** Display only local or remote videos
    Integer include = 0; // Integer | **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES 
    VideoPrivacySet privacyOneOf = VideoPrivacySet.fromValue("1"); // VideoPrivacySet | **PeerTube >= 4.0** Display only videos in this specific privacy/privacies
    Boolean hasHLSFiles = true; // Boolean | **PeerTube >= 4.0** Display only videos that have HLS files
    Boolean hasWebtorrentFiles = true; // Boolean | **PeerTube >= 4.0** Display only videos that have WebTorrent files
    try {
      List<VideosForXMLInner> result = apiInstance.getSyndicatedSubscriptionVideos(format, accountId, token, sort, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoFeedsApi#getSyndicatedSubscriptionVideos");
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
| **format** | **String**| format expected (we focus on making &#x60;rss&#x60; the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss)) | [enum: xml, rss, rss2, atom, atom1, json, json1] |
| **accountId** | **String**| limit listing to a specific account | |
| **token** | **String**| private token allowing access | |
| **sort** | **String**| Sort column | [optional] |
| **nsfw** | **String**| whether to include nsfw videos, if any | [optional] [enum: true, false] |
| **isLocal** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos | [optional] |
| **include** | **Integer**| **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  | [optional] [enum: 0, 1, 2, 4, 8] |
| **privacyOneOf** | [**VideoPrivacySet**](.md)| **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies | [optional] [enum: 1, 2, 3, 4] |
| **hasHLSFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files | [optional] |
| **hasWebtorrentFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files | [optional] |

### Return type

[**List&lt;VideosForXMLInner&gt;**](VideosForXMLInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/atom+xml, application/json, application/rss+xml, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  * Cache-Control -  <br>  |
| **406** | accept header unsupported |  -  |

<a id="getSyndicatedVideos"></a>
# **getSyndicatedVideos**
> List&lt;VideosForXMLInner&gt; getSyndicatedVideos(format, accountId, accountName, videoChannelId, videoChannelName, sort, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles)

List videos

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoFeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoFeedsApi apiInstance = new VideoFeedsApi(defaultClient);
    String format = "xml"; // String | format expected (we focus on making `rss` the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss))
    String accountId = "accountId_example"; // String | limit listing to a specific account
    String accountName = "accountName_example"; // String | limit listing to a specific account
    String videoChannelId = "videoChannelId_example"; // String | limit listing to a specific video channel
    String videoChannelName = "videoChannelName_example"; // String | limit listing to a specific video channel
    String sort = "-createdAt"; // String | Sort column
    String nsfw = "true"; // String | whether to include nsfw videos, if any
    Boolean isLocal = true; // Boolean | **PeerTube >= 4.0** Display only local or remote videos
    Integer include = 0; // Integer | **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES 
    VideoPrivacySet privacyOneOf = VideoPrivacySet.fromValue("1"); // VideoPrivacySet | **PeerTube >= 4.0** Display only videos in this specific privacy/privacies
    Boolean hasHLSFiles = true; // Boolean | **PeerTube >= 4.0** Display only videos that have HLS files
    Boolean hasWebtorrentFiles = true; // Boolean | **PeerTube >= 4.0** Display only videos that have WebTorrent files
    try {
      List<VideosForXMLInner> result = apiInstance.getSyndicatedVideos(format, accountId, accountName, videoChannelId, videoChannelName, sort, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoFeedsApi#getSyndicatedVideos");
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
| **format** | **String**| format expected (we focus on making &#x60;rss&#x60; the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss)) | [enum: xml, rss, rss2, atom, atom1, json, json1] |
| **accountId** | **String**| limit listing to a specific account | [optional] |
| **accountName** | **String**| limit listing to a specific account | [optional] |
| **videoChannelId** | **String**| limit listing to a specific video channel | [optional] |
| **videoChannelName** | **String**| limit listing to a specific video channel | [optional] |
| **sort** | **String**| Sort column | [optional] |
| **nsfw** | **String**| whether to include nsfw videos, if any | [optional] [enum: true, false] |
| **isLocal** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos | [optional] |
| **include** | **Integer**| **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  | [optional] [enum: 0, 1, 2, 4, 8] |
| **privacyOneOf** | [**VideoPrivacySet**](.md)| **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies | [optional] [enum: 1, 2, 3, 4] |
| **hasHLSFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files | [optional] |
| **hasWebtorrentFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files | [optional] |

### Return type

[**List&lt;VideosForXMLInner&gt;**](VideosForXMLInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/atom+xml, application/json, application/rss+xml, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  * Cache-Control -  <br>  |
| **404** | video channel or account not found |  -  |
| **406** | accept header unsupported |  -  |

