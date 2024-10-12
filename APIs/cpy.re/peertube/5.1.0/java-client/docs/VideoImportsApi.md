# VideoImportsApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1VideosImportsIdCancelPost**](VideoImportsApi.md#apiV1VideosImportsIdCancelPost) | **POST** /api/v1/videos/imports/{id}/cancel | Cancel video import |
| [**apiV1VideosImportsIdDelete**](VideoImportsApi.md#apiV1VideosImportsIdDelete) | **DELETE** /api/v1/videos/imports/{id} | Delete video import |
| [**importVideo**](VideoImportsApi.md#importVideo) | **POST** /api/v1/videos/imports | Import a video |


<a id="apiV1VideosImportsIdCancelPost"></a>
# **apiV1VideosImportsIdCancelPost**
> apiV1VideosImportsIdCancelPost(id)

Cancel video import

Cancel a pending video import

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoImportsApi apiInstance = new VideoImportsApi(defaultClient);
    Integer id = 56; // Integer | Entity id
    try {
      apiInstance.apiV1VideosImportsIdCancelPost(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoImportsApi#apiV1VideosImportsIdCancelPost");
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
| **id** | **Integer**| Entity id | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |

<a id="apiV1VideosImportsIdDelete"></a>
# **apiV1VideosImportsIdDelete**
> apiV1VideosImportsIdDelete(id)

Delete video import

Delete ended video import

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoImportsApi apiInstance = new VideoImportsApi(defaultClient);
    Integer id = 56; // Integer | Entity id
    try {
      apiInstance.apiV1VideosImportsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoImportsApi#apiV1VideosImportsIdDelete");
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
| **id** | **Integer**| Entity id | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |

<a id="importVideo"></a>
# **importVideo**
> VideoUploadResponse importVideo(channelId, name, targetUrl, magnetUri, torrentfile, category, commentsEnabled, description, downloadEnabled, language, licence, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding)

Import a video

Import a torrent or magnetURI or HTTP resource (if enabled by the instance administrator)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoImportsApi apiInstance = new VideoImportsApi(defaultClient);
    Integer channelId = 56; // Integer | Channel id that will contain this video
    String name = "name_example"; // String | Video name
    String targetUrl = "targetUrl_example"; // String | remote URL where to find the import's source video
    URI magnetUri = new URI(); // URI | magnet URI allowing to resolve the import's source video
    File torrentfile = new File("/path/to/file"); // File | Torrent file containing only the video file
    Integer category = 56; // Integer | category id of the video (see [/videos/categories](#operation/getCategories))
    Boolean commentsEnabled = true; // Boolean | Enable or disable comments for this video
    String description = "description_example"; // String | Video description
    Boolean downloadEnabled = true; // Boolean | Enable or disable downloading for this video
    String language = "language_example"; // String | language id of the video (see [/videos/languages](#operation/getLanguages))
    Integer licence = 56; // Integer | licence id of the video (see [/videos/licences](#operation/getLicences))
    Boolean nsfw = true; // Boolean | Whether or not this video contains sensitive content
    OffsetDateTime originallyPublishedAt = OffsetDateTime.now(); // OffsetDateTime | Date when the content was originally published
    File previewfile = new File("/path/to/file"); // File | Video preview file
    VideoPrivacySet privacy = VideoPrivacySet.fromValue("1"); // VideoPrivacySet | 
    VideoScheduledUpdate scheduleUpdate = new VideoScheduledUpdate(); // VideoScheduledUpdate | 
    String support = "support_example"; // String | A text tell the audience how to support the video creator
    Set<String> tags = Arrays.asList(); // Set<String> | Video tags (maximum 5 tags each between 2 and 30 characters)
    File thumbnailfile = new File("/path/to/file"); // File | Video thumbnail file
    Boolean waitTranscoding = true; // Boolean | Whether or not we wait transcoding before publish the video
    try {
      VideoUploadResponse result = apiInstance.importVideo(channelId, name, targetUrl, magnetUri, torrentfile, category, commentsEnabled, description, downloadEnabled, language, licence, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoImportsApi#importVideo");
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
| **channelId** | **Integer**| Channel id that will contain this video | |
| **name** | **String**| Video name | |
| **targetUrl** | [**String**](String.md)| remote URL where to find the import&#39;s source video | [optional] |
| **magnetUri** | [**URI**](URI.md)| magnet URI allowing to resolve the import&#39;s source video | [optional] |
| **torrentfile** | [**File**](File.md)| Torrent file containing only the video file | [optional] |
| **category** | **Integer**| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] |
| **commentsEnabled** | **Boolean**| Enable or disable comments for this video | [optional] |
| **description** | **String**| Video description | [optional] |
| **downloadEnabled** | **Boolean**| Enable or disable downloading for this video | [optional] |
| **language** | **String**| language id of the video (see [/videos/languages](#operation/getLanguages)) | [optional] |
| **licence** | **Integer**| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] |
| **nsfw** | **Boolean**| Whether or not this video contains sensitive content | [optional] |
| **originallyPublishedAt** | **OffsetDateTime**| Date when the content was originally published | [optional] |
| **previewfile** | **File**| Video preview file | [optional] |
| **privacy** | [**VideoPrivacySet**](VideoPrivacySet.md)|  | [optional] [enum: 1, 2, 3, 4] |
| **scheduleUpdate** | [**VideoScheduledUpdate**](VideoScheduledUpdate.md)|  | [optional] |
| **support** | **String**| A text tell the audience how to support the video creator | [optional] |
| **tags** | [**Set&lt;String&gt;**](String.md)| Video tags (maximum 5 tags each between 2 and 30 characters) | [optional] |
| **thumbnailfile** | **File**| Video thumbnail file | [optional] |
| **waitTranscoding** | **Boolean**| Whether or not we wait transcoding before publish the video | [optional] |

### Return type

[**VideoUploadResponse**](VideoUploadResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | &#x60;magnetUri&#x60; or &#x60;targetUrl&#x60; or a torrent file missing |  -  |
| **403** | video didn&#39;t pass pre-import filter |  -  |
| **409** | HTTP or Torrent/magnetURI import not enabled |  -  |

