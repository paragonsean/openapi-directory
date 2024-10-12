# VideosApi

All URIs are relative to *https://ws.api.video*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dELETEVideo**](VideosApi.md#dELETEVideo) | **DELETE** /videos/{videoId} | Delete a video |
| [**gETVideo**](VideosApi.md#gETVideo) | **GET** /videos/{videoId} | Show a video |
| [**gETVideoStatus**](VideosApi.md#gETVideoStatus) | **GET** /videos/{videoId}/status | Show video status |
| [**lISTVideos**](VideosApi.md#lISTVideos) | **GET** /videos | List all videos |
| [**pATCHVideo**](VideosApi.md#pATCHVideo) | **PATCH** /videos/{videoId} | Update a video |
| [**pATCHVideosVideoIdThumbnail**](VideosApi.md#pATCHVideosVideoIdThumbnail) | **PATCH** /videos/{videoId}/thumbnail | Pick a thumbnail |
| [**pOSTVideo**](VideosApi.md#pOSTVideo) | **POST** /videos | Create a video |
| [**pOSTVideosVideoIdSource**](VideosApi.md#pOSTVideosVideoIdSource) | **POST** /videos/{videoId}/source | Upload a video |
| [**pOSTVideosVideoIdThumbnail**](VideosApi.md#pOSTVideosVideoIdThumbnail) | **POST** /videos/{videoId}/thumbnail | Upload a thumbnail |


<a id="dELETEVideo"></a>
# **dELETEVideo**
> dELETEVideo(videoId)

Delete a video

If you do not need a video any longer, you can send a request to delete it. All you need is the videoId. Tutorials using [video deletion](https://api.video/blog/endpoints/video-delete).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    String videoId = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // String | The video ID for the video you want to delete.
    try {
      apiInstance.dELETEVideo(videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#dELETEVideo");
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
| **videoId** | **String**| The video ID for the video you want to delete. | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **404** | Not Found |  -  |

<a id="gETVideo"></a>
# **gETVideo**
> Video gETVideo(videoId)

Show a video

This call provides the same JSON information provided on video creation. For private videos, it will generate a unique token url. Use this to retrieve any details you need about a video, or set up a private viewing URL. Tutorials using [video GET](https://api.video/blog/endpoints/video-get).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    String videoId = "videoId_example"; // String | The unique identifier for the video you want details about.
    try {
      Video result = apiInstance.gETVideo(videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#gETVideo");
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
| **videoId** | **String**| The unique identifier for the video you want details about. | |

### Return type

[**Video**](Video.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Not Found |  -  |

<a id="gETVideoStatus"></a>
# **gETVideoStatus**
> Videostatus gETVideoStatus(videoId)

Show video status

This API provides upload status &amp; encoding status to determine when the video is uploaded or ready to playback. Once encoding is completed, the response also lists the available stream qualities. Tutorials using [video status](https://api.video/blog/endpoints/video-status).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    String videoId = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // String | The unique identifier for the video you want the status for.
    try {
      Videostatus result = apiInstance.gETVideoStatus(videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#gETVideoStatus");
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
| **videoId** | **String**| The unique identifier for the video you want the status for. | |

### Return type

[**Videostatus**](Videostatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Not Found |  -  |

<a id="lISTVideos"></a>
# **lISTVideos**
> VideosListResponse lISTVideos().title(title).tags(tags).metadata(metadata).description(description).liveStreamId(liveStreamId).sortBy(sortBy).sortOrder(sortOrder).currentPage(currentPage).pageSize(pageSize).execute();

List all videos

Requests to this endpoint return a list of your videos (with all their details). With no parameters added to this query, the API returns all videos. You can filter what videos the API returns using the parameters described below.  We have [several tutorials](https://api.video/blog/endpoints/video-list) that demonstrate this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    String title = "My Video.mp4"; // String | The title of a specific video you want to find. The search will match exactly to what term you provide and return any videos that contain the same term as part of their titles.
    List<String> tags = Arrays.asList(); // List<String> | A tag is a category you create and apply to videos. You can search for videos with particular tags by listing one or more here. Only videos that have all the tags you list will be returned.
    List<String> metadata = Arrays.asList(); // List<String> | Videos can be tagged with metadata tags in key:value pairs. You can search for videos with specific key value pairs using this parameter. [Dynamic Metadata](https://api.video/blog/endpoints/dynamic-metadata) allows you to define a key that allows any value pair.
    String description = "New Zealand"; // String | If you described a video with a term or sentence, you can add it here to return videos containing this string.
    String liveStreamId = "li400mYKSgQ6xs7taUeSaEKr"; // String | If you know the ID for a live stream, you can retrieve the stream by adding the ID for it here.
    String sortBy = "publishedAt"; // String | Allowed: publishedAt, title. You can search by the time videos were published at, or by title.
    String sortOrder = "asc"; // String | Allowed: asc, desc. asc is ascending and sorts from A to Z. desc is descending and sorts from Z to A.
    Integer currentPage = 1; // Integer | Choose the number of search results to return per page. Minimum value: 1
    Integer pageSize = 25; // Integer | Results per page. Allowed values 1-100, default is 25.
    try {
      VideosListResponse result = apiInstance.lISTVideos()
            .title(title)
            .tags(tags)
            .metadata(metadata)
            .description(description)
            .liveStreamId(liveStreamId)
            .sortBy(sortBy)
            .sortOrder(sortOrder)
            .currentPage(currentPage)
            .pageSize(pageSize)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#lISTVideos");
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
| **title** | **String**| The title of a specific video you want to find. The search will match exactly to what term you provide and return any videos that contain the same term as part of their titles. | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| A tag is a category you create and apply to videos. You can search for videos with particular tags by listing one or more here. Only videos that have all the tags you list will be returned. | [optional] |
| **metadata** | [**List&lt;String&gt;**](String.md)| Videos can be tagged with metadata tags in key:value pairs. You can search for videos with specific key value pairs using this parameter. [Dynamic Metadata](https://api.video/blog/endpoints/dynamic-metadata) allows you to define a key that allows any value pair. | [optional] |
| **description** | **String**| If you described a video with a term or sentence, you can add it here to return videos containing this string. | [optional] |
| **liveStreamId** | **String**| If you know the ID for a live stream, you can retrieve the stream by adding the ID for it here. | [optional] |
| **sortBy** | **String**| Allowed: publishedAt, title. You can search by the time videos were published at, or by title. | [optional] |
| **sortOrder** | **String**| Allowed: asc, desc. asc is ascending and sorts from A to Z. desc is descending and sorts from Z to A. | [optional] |
| **currentPage** | **Integer**| Choose the number of search results to return per page. Minimum value: 1 | [optional] [default to 1] |
| **pageSize** | **Integer**| Results per page. Allowed values 1-100, default is 25. | [optional] [default to 25] |

### Return type

[**VideosListResponse**](VideosListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="pATCHVideo"></a>
# **pATCHVideo**
> Video pATCHVideo(videoId, videoUpdatePayload)

Update a video

Use this endpoint to update the parameters associated with your video. The video you are updating is determined by the video ID you provide in the path. For each parameter you want to update, include the update in the request body. NOTE: If you are updating an array, you must provide the entire array as what you provide here overwrites what is in the system rather than appending to it. Tutorials using [video update](https://api.video/blog/endpoints/video-update).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    String videoId = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // String | The video ID for the video you want to delete.
    VideoUpdatePayload videoUpdatePayload = new VideoUpdatePayload(); // VideoUpdatePayload | 
    try {
      Video result = apiInstance.pATCHVideo(videoId, videoUpdatePayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#pATCHVideo");
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
| **videoId** | **String**| The video ID for the video you want to delete. | |
| **videoUpdatePayload** | [**VideoUpdatePayload**](VideoUpdatePayload.md)|  | [optional] |

### Return type

[**Video**](Video.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="pATCHVideosVideoIdThumbnail"></a>
# **pATCHVideosVideoIdThumbnail**
> Video pATCHVideosVideoIdThumbnail(videoId, videoThumbnailPickPayload)

Pick a thumbnail

Pick a thumbnail from the given time code. If you&#39;d like to upload an image for your thumbnail, use the [Upload a Thumbnail](https://docs.api.video/reference#post_videos-videoid-thumbnail) endpoint. There may be a short delay for the thumbnail to update. Tutorials using [Thumbnail picking](https://api.video/blog/endpoints/video-pick-a-thumbnail).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    String videoId = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // String | Unique identifier of the video you want to add a thumbnail to, where you use a section of your video as the thumbnail.
    VideoThumbnailPickPayload videoThumbnailPickPayload = new VideoThumbnailPickPayload(); // VideoThumbnailPickPayload | 
    try {
      Video result = apiInstance.pATCHVideosVideoIdThumbnail(videoId, videoThumbnailPickPayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#pATCHVideosVideoIdThumbnail");
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
| **videoId** | **String**| Unique identifier of the video you want to add a thumbnail to, where you use a section of your video as the thumbnail. | |
| **videoThumbnailPickPayload** | [**VideoThumbnailPickPayload**](VideoThumbnailPickPayload.md)|  | [optional] |

### Return type

[**Video**](Video.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Not Found |  -  |

<a id="pOSTVideo"></a>
# **pOSTVideo**
> Video pOSTVideo(videoCreatePayload)

Create a video

To create a video, you create its container&amp;parameters first, before adding the video file (exception - when using an existing HTTP source). * Videos are public by default. [Learn about Private videos](https://api.video/blog/tutorials/tutorial-private-videos) * Up to 6 responsive video streams will be created (from 240p to 4k) * Mp4 encoded versions are created at the highest quality (max 1080p) by default. * Panoramic videos are for videos recorded in 360 degrees.  You can toggle this after your 360 video upload. * Searchable parameters: title, description, tags and metadata   &#x60;&#x60;&#x60;shell $ curl https://ws.api.video/videos \\ -H &#39;Authorization: Bearer {access_token} \\ -d &#39;{\&quot;title\&quot;:\&quot;My video\&quot;,       \&quot;description\&quot;:\&quot;so many details\&quot;,      \&quot;mp4Support\&quot;:true }&#39; &#x60;&#x60;&#x60;    ## add an URL to upload on creation You can also create a video directly from a video hosted on a third-party server by giving its URI in &#x60;source&#x60; parameter: &#x60;&#x60;&#x60;shell $ curl https://ws.api.video/videos \\ -H &#39;Authorization: Bearer {access_token} \\ -d &#39;{\&quot;source\&quot;:\&quot;http://uri/to/video.mp4\&quot;, \&quot;title\&quot;:\&quot;My video\&quot;}&#39; &#x60;&#x60;&#x60;  In this case, the service will respond &#x60;202 Accepted&#x60; and ingest the video asynchronously. ## Track users with Dynamic Metadata Metadata values can be a key:value where the values are predefined, but Dynamic metadata allows you to enter *any* value for a defined key.  To defined a dynamic metadata pair use: &#x60;&#x60;&#x60; \&quot;metadata\&quot;:[{\&quot;dynamicKey\&quot;: \&quot;__dynamicKey__\&quot;}] &#x60;&#x60;&#x60;  The double underscore on both sides of the value allows any variable to be added for a given video session. Added the the url you might have: &#x60;&#x60;&#x60; &lt;iframe type&#x3D;\&quot;text/html\&quot; src&#x3D;\&quot;https://embed.api.video/vod/vi6QvU9dhYCzW3BpPvPsZUa8?metadata[classUserName]&#x3D;Doug\&quot; width&#x3D;\&quot;960\&quot; height&#x3D;\&quot;320\&quot; frameborder&#x3D;\&quot;0\&quot; scrollling&#x3D;\&quot;no\&quot;&gt;&lt;/iframe&gt; &#x60;&#x60;&#x60;   This video session will be tagged as watched by Doug - allowing for in-depth analysis on how each viewer interacts with the videos. ### We have tutorials on: * [Creating and uploading videos](https://api.video/blog/tutorials/video-upload-tutorial) * [Uploading large videos](https://api.video/blog/tutorials/video-upload-tutorial-large-videos)   * [Using tags with videos](https://api.video/blog/tutorials/video-tagging-best-practices) * [Private videos](https://api.video/blog/tutorials/tutorial-private-videos) * [Using Dynamic Metadata](https://api.video/blog/tutorials/dynamic-metadata)  * Full list of [tutorials](https://api.video/blog/endpoints/video-create) that demonstrate this endpoint. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    VideoCreatePayload videoCreatePayload = new VideoCreatePayload(); // VideoCreatePayload | video to create
    try {
      Video result = apiInstance.pOSTVideo(videoCreatePayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#pOSTVideo");
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
| **videoCreatePayload** | [**VideoCreatePayload**](VideoCreatePayload.md)| video to create | [optional] |

### Return type

[**Video**](Video.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **202** | Accepted |  -  |
| **400** | Bad Request |  -  |

<a id="pOSTVideosVideoIdSource"></a>
# **pOSTVideosVideoIdSource**
> Video pOSTVideosVideoIdSource(videoId, _file, contentRange)

Upload a video

To upload a video to the videoId you created. Replace {videoId} with the id you&#39;d like to use, {access_token} with your token, and /path/to/video.mp4 with the path to the video you&#39;d like to upload. You can only upload your video to the videoId once. &#x60;&#x60;&#x60;bash curl https://ws.api.video/videos/{videoId}/source \\   -H &#39;Authorization: Bearer {access_token}&#39; \\   -F file&#x3D;@/path/to/video.mp4    &#x60;&#x60;&#x60; Tutorials using [video upload](https://api.video/blog/endpoints/video-upload).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    String videoId = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // String | Enter the videoId you want to use to upload your video.
    File _file = new File("/path/to/file"); // File | The path to the video you would like to upload. The path must be local. If you want to use a video from an online source, you must use the \\\"/videos\\\" endpoint and add the \\\"source\\\" parameter when you create a new video.
    String contentRange = "Content-Range: bytes 200-100/5000"; // String | Content-Range represents the range of bytes that will be returned as a result of the request. Byte ranges are inclusive, meaning that bytes 0-999 represents the first 1000 bytes in a file or object.
    try {
      Video result = apiInstance.pOSTVideosVideoIdSource(videoId, _file, contentRange);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#pOSTVideosVideoIdSource");
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
| **videoId** | **String**| Enter the videoId you want to use to upload your video. | |
| **_file** | **File**| The path to the video you would like to upload. The path must be local. If you want to use a video from an online source, you must use the \\\&quot;/videos\\\&quot; endpoint and add the \\\&quot;source\\\&quot; parameter when you create a new video. | |
| **contentRange** | **String**| Content-Range represents the range of bytes that will be returned as a result of the request. Byte ranges are inclusive, meaning that bytes 0-999 represents the first 1000 bytes in a file or object. | [optional] |

### Return type

[**Video**](Video.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="pOSTVideosVideoIdThumbnail"></a>
# **pOSTVideosVideoIdThumbnail**
> Video pOSTVideosVideoIdThumbnail(videoId, _file)

Upload a thumbnail

The thumbnail is the poster that appears in the player window before video playback begins. This endpoint allows you to upload an image for the thumbnail. To select a still frame from the video using a time stamp, use [Pick a Thumbnail](https://docs.api.video/reference#patch_videos-videoid-thumbnail) to pick a time in the video.  Note: There may be a short delay before the new thumbnail is delivered to our CDN. Tutorials using [Thumbnail upload](https://api.video/blog/endpoints/videos-upload-a-thumbnail).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    VideosApi apiInstance = new VideosApi(defaultClient);
    String videoId = "videoId_example"; // String | Unique identifier of the chosen video 
    File _file = new File("/path/to/file"); // File | The image to be added as a thumbnail.
    try {
      Video result = apiInstance.pOSTVideosVideoIdThumbnail(videoId, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosApi#pOSTVideosVideoIdThumbnail");
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
| **videoId** | **String**| Unique identifier of the chosen video  | |
| **_file** | **File**| The image to be added as a thumbnail. | |

### Return type

[**Video**](Video.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

