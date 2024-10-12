# AlbumsAlbumVideosApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addVideoToAlbum**](AlbumsAlbumVideosApi.md#addVideoToAlbum) | **PUT** /users/{user_id}/albums/{album_id}/videos/{video_id} | Add a specific video to an album |
| [**addVideoToAlbumAlt1**](AlbumsAlbumVideosApi.md#addVideoToAlbumAlt1) | **PUT** /me/albums/{album_id}/videos/{video_id} | Add a specific video to an album |
| [**getAlbumVideo**](AlbumsAlbumVideosApi.md#getAlbumVideo) | **GET** /users/{user_id}/albums/{album_id}/videos/{video_id} | Get a specific video in an album |
| [**getAlbumVideoAlt1**](AlbumsAlbumVideosApi.md#getAlbumVideoAlt1) | **GET** /me/albums/{album_id}/videos/{video_id} | Get a specific video in an album |
| [**getAlbumVideos**](AlbumsAlbumVideosApi.md#getAlbumVideos) | **GET** /users/{user_id}/albums/{album_id}/videos | Get all the videos in an album |
| [**getAlbumVideosAlt1**](AlbumsAlbumVideosApi.md#getAlbumVideosAlt1) | **GET** /me/albums/{album_id}/videos | Get all the videos in an album |
| [**removeVideoFromAlbum**](AlbumsAlbumVideosApi.md#removeVideoFromAlbum) | **DELETE** /users/{user_id}/albums/{album_id}/videos/{video_id} | Remove a video from an album |
| [**removeVideoFromAlbumAlt1**](AlbumsAlbumVideosApi.md#removeVideoFromAlbumAlt1) | **DELETE** /me/albums/{album_id}/videos/{video_id} | Remove a video from an album |
| [**replaceVideosInAlbum**](AlbumsAlbumVideosApi.md#replaceVideosInAlbum) | **PUT** /users/{user_id}/albums/{album_id}/videos | Replace all the videos in an album |
| [**replaceVideosInAlbumAlt1**](AlbumsAlbumVideosApi.md#replaceVideosInAlbumAlt1) | **PUT** /me/albums/{album_id}/videos | Replace all the videos in an album |
| [**setVideoAsAlbumThumbnail**](AlbumsAlbumVideosApi.md#setVideoAsAlbumThumbnail) | **POST** /users/{user_id}/albums/{album_id}/videos/{video_id}/set_album_thumbnail | Set a video as the album thumbnail |
| [**setVideoAsAlbumThumbnailAlt1**](AlbumsAlbumVideosApi.md#setVideoAsAlbumThumbnailAlt1) | **POST** /me/albums/{album_id}/videos/{video_id}/set_album_thumbnail | Set a video as the album thumbnail |


<a id="addVideoToAlbum"></a>
# **addVideoToAlbum**
> addVideoToAlbum(albumId, userId, videoId)

Add a specific video to an album

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsAlbumVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlbumsAlbumVideosApi apiInstance = new AlbumsAlbumVideosApi(defaultClient);
    BigDecimal albumId = new BigDecimal("12345"); // BigDecimal | The ID of the album.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    BigDecimal videoId = new BigDecimal("196367152"); // BigDecimal | The ID of the video.
    try {
      apiInstance.addVideoToAlbum(albumId, userId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsAlbumVideosApi#addVideoToAlbum");
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
| **albumId** | **BigDecimal**| The ID of the album. | |
| **userId** | **BigDecimal**| The ID of the user. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The video was added. |  -  |
| **403** | The supplied token doesn&#39;t have the proper scopes, or the authenticated user can&#39;t edit the album. |  -  |
| **404** | No such album exists. |  -  |

<a id="addVideoToAlbumAlt1"></a>
# **addVideoToAlbumAlt1**
> addVideoToAlbumAlt1(albumId, videoId)

Add a specific video to an album

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsAlbumVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlbumsAlbumVideosApi apiInstance = new AlbumsAlbumVideosApi(defaultClient);
    BigDecimal albumId = new BigDecimal("12345"); // BigDecimal | The ID of the album.
    BigDecimal videoId = new BigDecimal("196367152"); // BigDecimal | The ID of the video.
    try {
      apiInstance.addVideoToAlbumAlt1(albumId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsAlbumVideosApi#addVideoToAlbumAlt1");
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
| **albumId** | **BigDecimal**| The ID of the album. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The video was added. |  -  |
| **403** | The supplied token doesn&#39;t have the proper scopes, or the authenticated user can&#39;t edit the album. |  -  |
| **404** | No such album exists. |  -  |

<a id="getAlbumVideo"></a>
# **getAlbumVideo**
> Video getAlbumVideo(albumId, userId, videoId, password)

Get a specific video in an album

This method gets a single video from an album. You can use this method to determine whether the album contains the specified video.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsAlbumVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlbumsAlbumVideosApi apiInstance = new AlbumsAlbumVideosApi(defaultClient);
    BigDecimal albumId = new BigDecimal("3706071"); // BigDecimal | The ID of the album.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    BigDecimal videoId = new BigDecimal("196367152"); // BigDecimal | The ID of the video.
    String password = "hunter1"; // String | The password of the album.
    try {
      Video result = apiInstance.getAlbumVideo(albumId, userId, videoId, password);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsAlbumVideosApi#getAlbumVideo");
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
| **albumId** | **BigDecimal**| The ID of the album. | |
| **userId** | **BigDecimal**| The ID of the user. | |
| **videoId** | **BigDecimal**| The ID of the video. | |
| **password** | **String**| The password of the album. | [optional] |

### Return type

[**Video**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.video+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The video was returned. |  -  |
| **404** | No such album exists, or the video wasn&#39;t found in it. |  -  |

<a id="getAlbumVideoAlt1"></a>
# **getAlbumVideoAlt1**
> Video getAlbumVideoAlt1(albumId, videoId, password)

Get a specific video in an album

This method gets a single video from an album. You can use this method to determine whether the album contains the specified video.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsAlbumVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlbumsAlbumVideosApi apiInstance = new AlbumsAlbumVideosApi(defaultClient);
    BigDecimal albumId = new BigDecimal("3706071"); // BigDecimal | The ID of the album.
    BigDecimal videoId = new BigDecimal("196367152"); // BigDecimal | The ID of the video.
    String password = "hunter1"; // String | The password of the album.
    try {
      Video result = apiInstance.getAlbumVideoAlt1(albumId, videoId, password);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsAlbumVideosApi#getAlbumVideoAlt1");
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
| **albumId** | **BigDecimal**| The ID of the album. | |
| **videoId** | **BigDecimal**| The ID of the video. | |
| **password** | **String**| The password of the album. | [optional] |

### Return type

[**Video**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.video+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The video was returned. |  -  |
| **404** | No such album exists, or the video wasn&#39;t found in it. |  -  |

<a id="getAlbumVideos"></a>
# **getAlbumVideos**
> List&lt;Video&gt; getAlbumVideos(albumId, userId, containingUri, direction, filter, filterEmbeddable, page, password, perPage, query, sort, weakSearch)

Get all the videos in an album

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsAlbumVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlbumsAlbumVideosApi apiInstance = new AlbumsAlbumVideosApi(defaultClient);
    BigDecimal albumId = new BigDecimal("3706071"); // BigDecimal | The ID of the album.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    String containingUri = "/videos/258684937"; // String | The page containing the video URI.
    String direction = "asc"; // String | The sort direction of the results.
    String filter = "embeddable"; // String | The attribute by which to filter the results.
    Boolean filterEmbeddable = true; // Boolean | Whether to filter the results by embeddable videos (`true`) or non-embeddable videos (`false`). Required only if **filter** is `embeddable`.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    String password = "hunter1"; // String | The password of the album.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String query = "Stop motion"; // String | The search query to use to filter the results.
    String sort = "alphabetical"; // String | The way to sort the results.
    Boolean weakSearch = false; // Boolean | Whether to include private videos in the search. Please note that a separate search service provides this functionality. The service performs a partial text search on the video's name.
    try {
      List<Video> result = apiInstance.getAlbumVideos(albumId, userId, containingUri, direction, filter, filterEmbeddable, page, password, perPage, query, sort, weakSearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsAlbumVideosApi#getAlbumVideos");
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
| **albumId** | **BigDecimal**| The ID of the album. | |
| **userId** | **BigDecimal**| The ID of the user. | |
| **containingUri** | **String**| The page containing the video URI. | [optional] |
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **filter** | **String**| The attribute by which to filter the results. | [optional] [enum: embeddable] |
| **filterEmbeddable** | **Boolean**| Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;. | [optional] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **password** | **String**| The password of the album. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **query** | **String**| The search query to use to filter the results. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: alphabetical, comments, date, default, duration, likes, manual, modified_time, plays] |
| **weakSearch** | **Boolean**| Whether to include private videos in the search. Please note that a separate search service provides this functionality. The service performs a partial text search on the video&#39;s name. | [optional] |

### Return type

[**List&lt;Video&gt;**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.video+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The videos were returned. |  -  |
| **404** | No such album exists. |  -  |

<a id="getAlbumVideosAlt1"></a>
# **getAlbumVideosAlt1**
> List&lt;Video&gt; getAlbumVideosAlt1(albumId, containingUri, direction, filter, filterEmbeddable, page, password, perPage, query, sort, weakSearch)

Get all the videos in an album

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsAlbumVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlbumsAlbumVideosApi apiInstance = new AlbumsAlbumVideosApi(defaultClient);
    BigDecimal albumId = new BigDecimal("3706071"); // BigDecimal | The ID of the album.
    String containingUri = "/videos/258684937"; // String | The page containing the video URI.
    String direction = "asc"; // String | The sort direction of the results.
    String filter = "embeddable"; // String | The attribute by which to filter the results.
    Boolean filterEmbeddable = true; // Boolean | Whether to filter the results by embeddable videos (`true`) or non-embeddable videos (`false`). Required only if **filter** is `embeddable`.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    String password = "hunter1"; // String | The password of the album.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String query = "Stop motion"; // String | The search query to use to filter the results.
    String sort = "alphabetical"; // String | The way to sort the results.
    Boolean weakSearch = false; // Boolean | Whether to include private videos in the search. Please note that a separate search service provides this functionality. The service performs a partial text search on the video's name.
    try {
      List<Video> result = apiInstance.getAlbumVideosAlt1(albumId, containingUri, direction, filter, filterEmbeddable, page, password, perPage, query, sort, weakSearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsAlbumVideosApi#getAlbumVideosAlt1");
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
| **albumId** | **BigDecimal**| The ID of the album. | |
| **containingUri** | **String**| The page containing the video URI. | [optional] |
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **filter** | **String**| The attribute by which to filter the results. | [optional] [enum: embeddable] |
| **filterEmbeddable** | **Boolean**| Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;. | [optional] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **password** | **String**| The password of the album. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **query** | **String**| The search query to use to filter the results. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: alphabetical, comments, date, default, duration, likes, manual, modified_time, plays] |
| **weakSearch** | **Boolean**| Whether to include private videos in the search. Please note that a separate search service provides this functionality. The service performs a partial text search on the video&#39;s name. | [optional] |

### Return type

[**List&lt;Video&gt;**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.video+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The videos were returned. |  -  |
| **404** | No such album exists. |  -  |

<a id="removeVideoFromAlbum"></a>
# **removeVideoFromAlbum**
> removeVideoFromAlbum(albumId, userId, videoId)

Remove a video from an album

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsAlbumVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlbumsAlbumVideosApi apiInstance = new AlbumsAlbumVideosApi(defaultClient);
    BigDecimal albumId = new BigDecimal("12345"); // BigDecimal | The ID of the album.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    BigDecimal videoId = new BigDecimal("196367152"); // BigDecimal | The ID of the video.
    try {
      apiInstance.removeVideoFromAlbum(albumId, userId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsAlbumVideosApi#removeVideoFromAlbum");
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
| **albumId** | **BigDecimal**| The ID of the album. | |
| **userId** | **BigDecimal**| The ID of the user. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The video was removed. |  -  |
| **403** | The supplied token doesn&#39;t have the proper scopes, or the authenticated user can&#39;t edit the album. |  -  |
| **404** | No such album exists. |  -  |

<a id="removeVideoFromAlbumAlt1"></a>
# **removeVideoFromAlbumAlt1**
> removeVideoFromAlbumAlt1(albumId, videoId)

Remove a video from an album

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsAlbumVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlbumsAlbumVideosApi apiInstance = new AlbumsAlbumVideosApi(defaultClient);
    BigDecimal albumId = new BigDecimal("12345"); // BigDecimal | The ID of the album.
    BigDecimal videoId = new BigDecimal("196367152"); // BigDecimal | The ID of the video.
    try {
      apiInstance.removeVideoFromAlbumAlt1(albumId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsAlbumVideosApi#removeVideoFromAlbumAlt1");
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
| **albumId** | **BigDecimal**| The ID of the album. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The video was removed. |  -  |
| **403** | The supplied token doesn&#39;t have the proper scopes, or the authenticated user can&#39;t edit the album. |  -  |
| **404** | No such album exists. |  -  |

<a id="replaceVideosInAlbum"></a>
# **replaceVideosInAlbum**
> replaceVideosInAlbum(albumId, userId, replaceVideosInAlbumAlt1Request)

Replace all the videos in an album

This method replaces all the existing videos in an album with one or more videos.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsAlbumVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlbumsAlbumVideosApi apiInstance = new AlbumsAlbumVideosApi(defaultClient);
    BigDecimal albumId = new BigDecimal("3706071"); // BigDecimal | The ID of the album.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    ReplaceVideosInAlbumAlt1Request replaceVideosInAlbumAlt1Request = new ReplaceVideosInAlbumAlt1Request(); // ReplaceVideosInAlbumAlt1Request | 
    try {
      apiInstance.replaceVideosInAlbum(albumId, userId, replaceVideosInAlbumAlt1Request);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsAlbumVideosApi#replaceVideosInAlbum");
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
| **albumId** | **BigDecimal**| The ID of the album. | |
| **userId** | **BigDecimal**| The ID of the user. | |
| **replaceVideosInAlbumAlt1Request** | [**ReplaceVideosInAlbumAlt1Request**](ReplaceVideosInAlbumAlt1Request.md)|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The videos were added. |  -  |
| **403** | The authenticated user can&#39;t add videos to albums. |  -  |
| **404** | No such album exists. |  -  |

<a id="replaceVideosInAlbumAlt1"></a>
# **replaceVideosInAlbumAlt1**
> replaceVideosInAlbumAlt1(albumId, replaceVideosInAlbumAlt1Request)

Replace all the videos in an album

This method replaces all the existing videos in an album with one or more videos.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsAlbumVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlbumsAlbumVideosApi apiInstance = new AlbumsAlbumVideosApi(defaultClient);
    BigDecimal albumId = new BigDecimal("3706071"); // BigDecimal | The ID of the album.
    ReplaceVideosInAlbumAlt1Request replaceVideosInAlbumAlt1Request = new ReplaceVideosInAlbumAlt1Request(); // ReplaceVideosInAlbumAlt1Request | 
    try {
      apiInstance.replaceVideosInAlbumAlt1(albumId, replaceVideosInAlbumAlt1Request);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsAlbumVideosApi#replaceVideosInAlbumAlt1");
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
| **albumId** | **BigDecimal**| The ID of the album. | |
| **replaceVideosInAlbumAlt1Request** | [**ReplaceVideosInAlbumAlt1Request**](ReplaceVideosInAlbumAlt1Request.md)|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The videos were added. |  -  |
| **403** | The authenticated user can&#39;t add videos to albums. |  -  |
| **404** | No such album exists. |  -  |

<a id="setVideoAsAlbumThumbnail"></a>
# **setVideoAsAlbumThumbnail**
> Album setVideoAsAlbumThumbnail(albumId, userId, videoId, setVideoAsAlbumThumbnailAlt1Request)

Set a video as the album thumbnail

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsAlbumVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlbumsAlbumVideosApi apiInstance = new AlbumsAlbumVideosApi(defaultClient);
    BigDecimal albumId = new BigDecimal("12345"); // BigDecimal | The ID of the album.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    BigDecimal videoId = new BigDecimal("196367152"); // BigDecimal | The ID of the video.
    SetVideoAsAlbumThumbnailAlt1Request setVideoAsAlbumThumbnailAlt1Request = new SetVideoAsAlbumThumbnailAlt1Request(); // SetVideoAsAlbumThumbnailAlt1Request | 
    try {
      Album result = apiInstance.setVideoAsAlbumThumbnail(albumId, userId, videoId, setVideoAsAlbumThumbnailAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsAlbumVideosApi#setVideoAsAlbumThumbnail");
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
| **albumId** | **BigDecimal**| The ID of the album. | |
| **userId** | **BigDecimal**| The ID of the user. | |
| **videoId** | **BigDecimal**| The ID of the video. | |
| **setVideoAsAlbumThumbnailAlt1Request** | [**SetVideoAsAlbumThumbnailAlt1Request**](SetVideoAsAlbumThumbnailAlt1Request.md)|  | [optional] |

### Return type

[**Album**](Album.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The album was updated with a new thumbnail. |  -  |
| **403** | Error code 3429: The authenticated user can&#39;t edit the album. |  -  |
| **404** | Error code 5000: No such album, or user, or video exists. |  -  |
| **500** | Error code 4016: Unexpected error while setting thumbnail. |  -  |

<a id="setVideoAsAlbumThumbnailAlt1"></a>
# **setVideoAsAlbumThumbnailAlt1**
> Album setVideoAsAlbumThumbnailAlt1(albumId, videoId, setVideoAsAlbumThumbnailAlt1Request)

Set a video as the album thumbnail

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsAlbumVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlbumsAlbumVideosApi apiInstance = new AlbumsAlbumVideosApi(defaultClient);
    BigDecimal albumId = new BigDecimal("12345"); // BigDecimal | The ID of the album.
    BigDecimal videoId = new BigDecimal("196367152"); // BigDecimal | The ID of the video.
    SetVideoAsAlbumThumbnailAlt1Request setVideoAsAlbumThumbnailAlt1Request = new SetVideoAsAlbumThumbnailAlt1Request(); // SetVideoAsAlbumThumbnailAlt1Request | 
    try {
      Album result = apiInstance.setVideoAsAlbumThumbnailAlt1(albumId, videoId, setVideoAsAlbumThumbnailAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsAlbumVideosApi#setVideoAsAlbumThumbnailAlt1");
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
| **albumId** | **BigDecimal**| The ID of the album. | |
| **videoId** | **BigDecimal**| The ID of the video. | |
| **setVideoAsAlbumThumbnailAlt1Request** | [**SetVideoAsAlbumThumbnailAlt1Request**](SetVideoAsAlbumThumbnailAlt1Request.md)|  | [optional] |

### Return type

[**Album**](Album.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The album was updated with a new thumbnail. |  -  |
| **403** | Error code 3429: The authenticated user can&#39;t edit the album. |  -  |
| **404** | Error code 5000: No such album, or user, or video exists. |  -  |
| **500** | Error code 4016: Unexpected error while setting thumbnail. |  -  |

