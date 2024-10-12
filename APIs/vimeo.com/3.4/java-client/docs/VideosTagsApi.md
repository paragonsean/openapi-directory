# VideosTagsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addVideoTag**](VideosTagsApi.md#addVideoTag) | **PUT** /videos/{video_id}/tags/{word} | Add a specific tag to a video |
| [**addVideoTags**](VideosTagsApi.md#addVideoTags) | **PUT** /videos/{video_id}/tags | Add a list of tags to a video |
| [**checkVideoForTag**](VideosTagsApi.md#checkVideoForTag) | **GET** /videos/{video_id}/tags/{word} | Check if a tag has been added to a video |
| [**deleteVideoTag**](VideosTagsApi.md#deleteVideoTag) | **DELETE** /videos/{video_id}/tags/{word} | Remove a tag from a video |
| [**getVideoTags**](VideosTagsApi.md#getVideoTags) | **GET** /videos/{video_id}/tags | Get all the tags of a video |
| [**getVideosWithTag**](VideosTagsApi.md#getVideosWithTag) | **GET** /tags/{word}/videos | Get all the videos with a specific tag |


<a id="addVideoTag"></a>
# **addVideoTag**
> Tag addVideoTag(videoId, word)

Add a specific tag to a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosTagsApi;

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

    VideosTagsApi apiInstance = new VideosTagsApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    String word = "awesome"; // String | The tag word.
    try {
      Tag result = apiInstance.addVideoTag(videoId, word);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosTagsApi#addVideoTag");
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
| **videoId** | **BigDecimal**| The ID of the video. | |
| **word** | **String**| The tag word. | |

### Return type

[**Tag**](Tag.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.tag+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The tag was added. |  -  |
| **400** | * The tag is invalid. * An unsupported parameter was supplied. |  -  |
| **403** | The number of tags on the video would exceed 20. |  -  |

<a id="addVideoTags"></a>
# **addVideoTags**
> List&lt;Tag&gt; addVideoTags(videoId, addVideoTagsRequest)

Add a list of tags to a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosTagsApi;

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

    VideosTagsApi apiInstance = new VideosTagsApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    AddVideoTagsRequest addVideoTagsRequest = new AddVideoTagsRequest(); // AddVideoTagsRequest | 
    try {
      List<Tag> result = apiInstance.addVideoTags(videoId, addVideoTagsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosTagsApi#addVideoTags");
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
| **videoId** | **BigDecimal**| The ID of the video. | |
| **addVideoTagsRequest** | [**AddVideoTagsRequest**](AddVideoTagsRequest.md)|  | |

### Return type

[**List&lt;Tag&gt;**](Tag.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.tag+json
 - **Accept**: application/vnd.vimeo.tag+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tags that were added. |  -  |
| **400** | * The request body wasn&#39;t supplied. * A parameter is invalid. * The request body isn&#39;t a JSON-encoded list of tags. |  -  |
| **403** | * The authenticated user can&#39;t add tags to a video. * The number of tags would exceed 20. |  -  |

<a id="checkVideoForTag"></a>
# **checkVideoForTag**
> Tag checkVideoForTag(videoId, word)

Check if a tag has been added to a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosTagsApi;

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

    VideosTagsApi apiInstance = new VideosTagsApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    String word = "awesome"; // String | The tag word.
    try {
      Tag result = apiInstance.checkVideoForTag(videoId, word);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosTagsApi#checkVideoForTag");
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
| **videoId** | **BigDecimal**| The ID of the video. | |
| **word** | **String**| The tag word. | |

### Return type

[**Tag**](Tag.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.tag+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The tag has been added. |  -  |
| **400** | * A parameter is invalid. * The tag is invalid. |  -  |
| **404** | No such tag exists within the video. |  -  |

<a id="deleteVideoTag"></a>
# **deleteVideoTag**
> deleteVideoTag(videoId, word)

Remove a tag from a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosTagsApi;

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

    VideosTagsApi apiInstance = new VideosTagsApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    String word = "awesome"; // String | The tag word.
    try {
      apiInstance.deleteVideoTag(videoId, word);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosTagsApi#deleteVideoTag");
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
| **videoId** | **BigDecimal**| The ID of the video. | |
| **word** | **String**| The tag word. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.tag+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The tag was deleted. |  -  |
| **400** | * A parameter is invalid. * The tag is invalid. |  -  |

<a id="getVideoTags"></a>
# **getVideoTags**
> List&lt;Tag&gt; getVideoTags(videoId)

Get all the tags of a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosTagsApi;

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

    VideosTagsApi apiInstance = new VideosTagsApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      List<Tag> result = apiInstance.getVideoTags(videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosTagsApi#getVideoTags");
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
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

[**List&lt;Tag&gt;**](Tag.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.tag+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tags were returned. |  -  |

<a id="getVideosWithTag"></a>
# **getVideosWithTag**
> List&lt;Video&gt; getVideosWithTag(word, direction, page, perPage, sort)

Get all the videos with a specific tag

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosTagsApi;

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

    VideosTagsApi apiInstance = new VideosTagsApi(defaultClient);
    String word = "awesome"; // String | The tag word.
    String direction = "asc"; // String | The sort direction of the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String sort = "created_time"; // String | The way to sort the results.
    try {
      List<Video> result = apiInstance.getVideosWithTag(word, direction, page, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosTagsApi#getVideosWithTag");
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
| **word** | **String**| The tag word. | |
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: created_time, duration, name] |

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
| **404** | No such tag exists. |  -  |

