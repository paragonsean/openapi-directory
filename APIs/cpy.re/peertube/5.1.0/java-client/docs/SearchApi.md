# SearchApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchChannels**](SearchApi.md#searchChannels) | **GET** /api/v1/search/video-channels | Search channels |
| [**searchPlaylists**](SearchApi.md#searchPlaylists) | **GET** /api/v1/search/video-playlists | Search playlists |
| [**searchVideos**](SearchApi.md#searchVideos) | **GET** /api/v1/search/videos | Search videos |


<a id="searchChannels"></a>
# **searchChannels**
> VideoChannelList searchChannels(search, start, count, searchTarget, sort)

Search channels

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String search = "search_example"; // String | String to search. If the user can make a remote URI search, and the string is an URI then the PeerTube instance will fetch the remote object and add it to its database. Then, you can use the REST API to fetch the complete channel information and interact with it. 
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String searchTarget = "local"; // String | If the administrator enabled search index support, you can override the default search target.  **Warning**: If you choose to make an index search, PeerTube will get results from a third party service. It means the instance may not yet know the objects you fetched. If you want to load video/channel information:   * If the current user has the ability to make a remote URI search (this information is available in the config endpoint),   then reuse the search API to make a search using the object URI so PeerTube instance fetches the remote object and fill its database.   After that, you can use the classic REST API endpoints to fetch the complete object or interact with it   * If the current user doesn't have the ability to make a remote URI search, then redirect the user on the origin instance or fetch   the data from the origin instance API 
    String sort = "-createdAt"; // String | Sort column
    try {
      VideoChannelList result = apiInstance.searchChannels(search, start, count, searchTarget, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchChannels");
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
| **search** | **String**| String to search. If the user can make a remote URI search, and the string is an URI then the PeerTube instance will fetch the remote object and add it to its database. Then, you can use the REST API to fetch the complete channel information and interact with it.  | |
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **searchTarget** | **String**| If the administrator enabled search index support, you can override the default search target.  **Warning**: If you choose to make an index search, PeerTube will get results from a third party service. It means the instance may not yet know the objects you fetched. If you want to load video/channel information:   * If the current user has the ability to make a remote URI search (this information is available in the config endpoint),   then reuse the search API to make a search using the object URI so PeerTube instance fetches the remote object and fill its database.   After that, you can use the classic REST API endpoints to fetch the complete object or interact with it   * If the current user doesn&#39;t have the ability to make a remote URI search, then redirect the user on the origin instance or fetch   the data from the origin instance API  | [optional] [enum: local, search-index] |
| **sort** | **String**| Sort column | [optional] |

### Return type

[**VideoChannelList**](VideoChannelList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **500** | search index unavailable |  -  |

<a id="searchPlaylists"></a>
# **searchPlaylists**
> ApiV1AccountsNameVideoPlaylistsGet200Response searchPlaylists(search, start, count, searchTarget, sort)

Search playlists

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String search = "search_example"; // String | String to search. If the user can make a remote URI search, and the string is an URI then the PeerTube instance will fetch the remote object and add it to its database. Then, you can use the REST API to fetch the complete playlist information and interact with it. 
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String searchTarget = "local"; // String | If the administrator enabled search index support, you can override the default search target.  **Warning**: If you choose to make an index search, PeerTube will get results from a third party service. It means the instance may not yet know the objects you fetched. If you want to load video/channel information:   * If the current user has the ability to make a remote URI search (this information is available in the config endpoint),   then reuse the search API to make a search using the object URI so PeerTube instance fetches the remote object and fill its database.   After that, you can use the classic REST API endpoints to fetch the complete object or interact with it   * If the current user doesn't have the ability to make a remote URI search, then redirect the user on the origin instance or fetch   the data from the origin instance API 
    String sort = "-createdAt"; // String | Sort column
    try {
      ApiV1AccountsNameVideoPlaylistsGet200Response result = apiInstance.searchPlaylists(search, start, count, searchTarget, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchPlaylists");
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
| **search** | **String**| String to search. If the user can make a remote URI search, and the string is an URI then the PeerTube instance will fetch the remote object and add it to its database. Then, you can use the REST API to fetch the complete playlist information and interact with it.  | |
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **searchTarget** | **String**| If the administrator enabled search index support, you can override the default search target.  **Warning**: If you choose to make an index search, PeerTube will get results from a third party service. It means the instance may not yet know the objects you fetched. If you want to load video/channel information:   * If the current user has the ability to make a remote URI search (this information is available in the config endpoint),   then reuse the search API to make a search using the object URI so PeerTube instance fetches the remote object and fill its database.   After that, you can use the classic REST API endpoints to fetch the complete object or interact with it   * If the current user doesn&#39;t have the ability to make a remote URI search, then redirect the user on the origin instance or fetch   the data from the origin instance API  | [optional] [enum: local, search-index] |
| **sort** | **String**| Sort column | [optional] |

### Return type

[**ApiV1AccountsNameVideoPlaylistsGet200Response**](ApiV1AccountsNameVideoPlaylistsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **500** | search index unavailable |  -  |

<a id="searchVideos"></a>
# **searchVideos**
> VideoListResponse searchVideos(search, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, uuids, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, searchTarget, sort, excludeAlreadyWatched, startDate, endDate, originallyPublishedStartDate, originallyPublishedEndDate, durationMin, durationMax)

Search videos

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String search = "search_example"; // String | String to search. If the user can make a remote URI search, and the string is an URI then the PeerTube instance will fetch the remote object and add it to its database. Then, you can use the REST API to fetch the complete video information and interact with it. 
    GetAccountVideosCategoryOneOfParameter categoryOneOf = new GetAccountVideosCategoryOneOfParameter(); // GetAccountVideosCategoryOneOfParameter | category id of the video (see [/videos/categories](#operation/getCategories))
    Boolean isLive = true; // Boolean | whether or not the video is a live
    GetAccountVideosTagsOneOfParameter tagsOneOf = new GetAccountVideosTagsOneOfParameter(); // GetAccountVideosTagsOneOfParameter | tag(s) of the video
    GetAccountVideosTagsAllOfParameter tagsAllOf = new GetAccountVideosTagsAllOfParameter(); // GetAccountVideosTagsAllOfParameter | tag(s) of the video, where all should be present in the video
    GetAccountVideosLicenceOneOfParameter licenceOneOf = new GetAccountVideosLicenceOneOfParameter(); // GetAccountVideosLicenceOneOfParameter | licence id of the video (see [/videos/licences](#operation/getLicences))
    GetAccountVideosLanguageOneOfParameter languageOneOf = new GetAccountVideosLanguageOneOfParameter(); // GetAccountVideosLanguageOneOfParameter | language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language
    String nsfw = "true"; // String | whether to include nsfw videos, if any
    Boolean isLocal = true; // Boolean | **PeerTube >= 4.0** Display only local or remote videos
    Integer include = 0; // Integer | **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES 
    VideoPrivacySet privacyOneOf = VideoPrivacySet.fromValue("1"); // VideoPrivacySet | **PeerTube >= 4.0** Display only videos in this specific privacy/privacies
    List<String> uuids = Arrays.asList(); // List<String> | Find videos with specific UUIDs
    Boolean hasHLSFiles = true; // Boolean | **PeerTube >= 4.0** Display only videos that have HLS files
    Boolean hasWebtorrentFiles = true; // Boolean | **PeerTube >= 4.0** Display only videos that have WebTorrent files
    String skipCount = "true"; // String | if you don't need the `total` in the response
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String searchTarget = "local"; // String | If the administrator enabled search index support, you can override the default search target.  **Warning**: If you choose to make an index search, PeerTube will get results from a third party service. It means the instance may not yet know the objects you fetched. If you want to load video/channel information:   * If the current user has the ability to make a remote URI search (this information is available in the config endpoint),   then reuse the search API to make a search using the object URI so PeerTube instance fetches the remote object and fill its database.   After that, you can use the classic REST API endpoints to fetch the complete object or interact with it   * If the current user doesn't have the ability to make a remote URI search, then redirect the user on the origin instance or fetch   the data from the origin instance API 
    String sort = "name"; // String | Sort videos by criteria (prefixing with `-` means `DESC` order): 
    Boolean excludeAlreadyWatched = true; // Boolean | Whether or not to exclude videos that are in the user's video history
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Get videos that are published after this date
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Get videos that are published before this date
    OffsetDateTime originallyPublishedStartDate = OffsetDateTime.now(); // OffsetDateTime | Get videos that are originally published after this date
    OffsetDateTime originallyPublishedEndDate = OffsetDateTime.now(); // OffsetDateTime | Get videos that are originally published before this date
    Integer durationMin = 56; // Integer | Get videos that have this minimum duration
    Integer durationMax = 56; // Integer | Get videos that have this maximum duration
    try {
      VideoListResponse result = apiInstance.searchVideos(search, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, uuids, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, searchTarget, sort, excludeAlreadyWatched, startDate, endDate, originallyPublishedStartDate, originallyPublishedEndDate, durationMin, durationMax);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchVideos");
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
| **search** | **String**| String to search. If the user can make a remote URI search, and the string is an URI then the PeerTube instance will fetch the remote object and add it to its database. Then, you can use the REST API to fetch the complete video information and interact with it.  | |
| **categoryOneOf** | [**GetAccountVideosCategoryOneOfParameter**](.md)| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] |
| **isLive** | **Boolean**| whether or not the video is a live | [optional] |
| **tagsOneOf** | [**GetAccountVideosTagsOneOfParameter**](.md)| tag(s) of the video | [optional] |
| **tagsAllOf** | [**GetAccountVideosTagsAllOfParameter**](.md)| tag(s) of the video, where all should be present in the video | [optional] |
| **licenceOneOf** | [**GetAccountVideosLicenceOneOfParameter**](.md)| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] |
| **languageOneOf** | [**GetAccountVideosLanguageOneOfParameter**](.md)| language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language | [optional] |
| **nsfw** | **String**| whether to include nsfw videos, if any | [optional] [enum: true, false] |
| **isLocal** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos | [optional] |
| **include** | **Integer**| **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  | [optional] [enum: 0, 1, 2, 4, 8] |
| **privacyOneOf** | [**VideoPrivacySet**](.md)| **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies | [optional] [enum: 1, 2, 3, 4] |
| **uuids** | [**List&lt;String&gt;**](String.md)| Find videos with specific UUIDs | [optional] |
| **hasHLSFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files | [optional] |
| **hasWebtorrentFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files | [optional] |
| **skipCount** | **String**| if you don&#39;t need the &#x60;total&#x60; in the response | [optional] [default to false] [enum: true, false] |
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **searchTarget** | **String**| If the administrator enabled search index support, you can override the default search target.  **Warning**: If you choose to make an index search, PeerTube will get results from a third party service. It means the instance may not yet know the objects you fetched. If you want to load video/channel information:   * If the current user has the ability to make a remote URI search (this information is available in the config endpoint),   then reuse the search API to make a search using the object URI so PeerTube instance fetches the remote object and fill its database.   After that, you can use the classic REST API endpoints to fetch the complete object or interact with it   * If the current user doesn&#39;t have the ability to make a remote URI search, then redirect the user on the origin instance or fetch   the data from the origin instance API  | [optional] [enum: local, search-index] |
| **sort** | **String**| Sort videos by criteria (prefixing with &#x60;-&#x60; means &#x60;DESC&#x60; order):  | [optional] [enum: name, -duration, -createdAt, -publishedAt, -views, -likes, -match] |
| **excludeAlreadyWatched** | **Boolean**| Whether or not to exclude videos that are in the user&#39;s video history | [optional] |
| **startDate** | **OffsetDateTime**| Get videos that are published after this date | [optional] |
| **endDate** | **OffsetDateTime**| Get videos that are published before this date | [optional] |
| **originallyPublishedStartDate** | **OffsetDateTime**| Get videos that are originally published after this date | [optional] |
| **originallyPublishedEndDate** | **OffsetDateTime**| Get videos that are originally published before this date | [optional] |
| **durationMin** | **Integer**| Get videos that have this minimum duration | [optional] |
| **durationMax** | **Integer**| Get videos that have this maximum duration | [optional] |

### Return type

[**VideoListResponse**](VideoListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **500** | search index unavailable |  -  |

