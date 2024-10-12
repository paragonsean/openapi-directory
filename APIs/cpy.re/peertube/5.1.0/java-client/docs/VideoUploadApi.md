# VideoUploadApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**importVideo_0**](VideoUploadApi.md#importVideo_0) | **POST** /api/v1/videos/imports | Import a video |
| [**uploadLegacy_0**](VideoUploadApi.md#uploadLegacy_0) | **POST** /api/v1/videos/upload | Upload a video |
| [**uploadResumableCancel_0**](VideoUploadApi.md#uploadResumableCancel_0) | **DELETE** /api/v1/videos/upload-resumable | Cancel the resumable upload of a video, deleting any data uploaded so far |
| [**uploadResumableInit_0**](VideoUploadApi.md#uploadResumableInit_0) | **POST** /api/v1/videos/upload-resumable | Initialize the resumable upload of a video |
| [**uploadResumable_0**](VideoUploadApi.md#uploadResumable_0) | **PUT** /api/v1/videos/upload-resumable | Send chunk for the resumable upload of a video |


<a id="importVideo_0"></a>
# **importVideo_0**
> VideoUploadResponse importVideo_0(channelId, name, targetUrl, magnetUri, torrentfile, category, commentsEnabled, description, downloadEnabled, language, licence, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding)

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
import org.openapitools.client.api.VideoUploadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoUploadApi apiInstance = new VideoUploadApi(defaultClient);
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
      VideoUploadResponse result = apiInstance.importVideo_0(channelId, name, targetUrl, magnetUri, torrentfile, category, commentsEnabled, description, downloadEnabled, language, licence, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoUploadApi#importVideo_0");
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

<a id="uploadLegacy_0"></a>
# **uploadLegacy_0**
> VideoUploadResponse uploadLegacy_0(channelId, name, videofile, category, commentsEnabled, description, downloadEnabled, language, licence, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding)

Upload a video

Uses a single request to upload a video.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoUploadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoUploadApi apiInstance = new VideoUploadApi(defaultClient);
    Integer channelId = 56; // Integer | Channel id that will contain this video
    String name = "name_example"; // String | Video name
    File videofile = new File("/path/to/file"); // File | Video file
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
      VideoUploadResponse result = apiInstance.uploadLegacy_0(channelId, name, videofile, category, commentsEnabled, description, downloadEnabled, language, licence, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoUploadApi#uploadLegacy_0");
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
| **videofile** | **File**| Video file | |
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
| **403** | video didn&#39;t pass upload filter |  -  |
| **408** | upload has timed out |  -  |
| **413** | If the response has no body, it means the reverse-proxy didn&#39;t let it through. Otherwise disambiguate via &#x60;type&#x60;: - &#x60;quota_reached&#x60; for quota limits whether daily or global  |  * X-File-Maximum-Size - Maximum file size for the video <br>  |
| **415** | video type unsupported |  -  |
| **422** | video unreadable |  -  |

<a id="uploadResumableCancel_0"></a>
# **uploadResumableCancel_0**
> uploadResumableCancel_0(uploadId, contentLength)

Cancel the resumable upload of a video, deleting any data uploaded so far

Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to cancel the upload of a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoUploadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoUploadApi apiInstance = new VideoUploadApi(defaultClient);
    String uploadId = "uploadId_example"; // String | Created session id to proceed with. If you didn't send chunks in the last 12 hours, it is not valid anymore and the upload session has already been deleted with its data ;-) 
    BigDecimal contentLength = new BigDecimal("0"); // BigDecimal | 
    try {
      apiInstance.uploadResumableCancel_0(uploadId, contentLength);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoUploadApi#uploadResumableCancel_0");
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
| **uploadId** | **String**| Created session id to proceed with. If you didn&#39;t send chunks in the last 12 hours, it is not valid anymore and the upload session has already been deleted with its data ;-)  | |
| **contentLength** | **BigDecimal**|  | |

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
| **204** | upload cancelled |  * Content-Length -  <br>  |
| **404** | upload not found |  -  |

<a id="uploadResumableInit_0"></a>
# **uploadResumableInit_0**
> uploadResumableInit_0(xUploadContentLength, xUploadContentType, videoUploadRequestResumable)

Initialize the resumable upload of a video

Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to initialize the upload of a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoUploadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoUploadApi apiInstance = new VideoUploadApi(defaultClient);
    BigDecimal xUploadContentLength = new BigDecimal("2469036"); // BigDecimal | Number of bytes that will be uploaded in subsequent requests. Set this value to the size of the file you are uploading.
    String xUploadContentType = "video/mp4"; // String | MIME type of the file that you are uploading. Depending on your instance settings, acceptable values might vary.
    VideoUploadRequestResumable videoUploadRequestResumable = new VideoUploadRequestResumable(); // VideoUploadRequestResumable | 
    try {
      apiInstance.uploadResumableInit_0(xUploadContentLength, xUploadContentType, videoUploadRequestResumable);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoUploadApi#uploadResumableInit_0");
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
| **xUploadContentLength** | **BigDecimal**| Number of bytes that will be uploaded in subsequent requests. Set this value to the size of the file you are uploading. | |
| **xUploadContentType** | **String**| MIME type of the file that you are uploading. Depending on your instance settings, acceptable values might vary. | |
| **videoUploadRequestResumable** | [**VideoUploadRequestResumable**](VideoUploadRequestResumable.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | file already exists, send a [&#x60;resume&#x60;](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) request instead |  -  |
| **201** | created |  * Content-Length -  <br>  * Location -  <br>  |
| **413** | Disambiguate via &#x60;type&#x60;: - &#x60;max_file_size_reached&#x60; for the absolute file size limit - &#x60;quota_reached&#x60; for quota limits whether daily or global  |  -  |
| **415** | video type unsupported |  -  |

<a id="uploadResumable_0"></a>
# **uploadResumable_0**
> VideoUploadResponse uploadResumable_0(uploadId, contentRange, contentLength, body)

Send chunk for the resumable upload of a video

Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to continue, pause or resume the upload of a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoUploadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoUploadApi apiInstance = new VideoUploadApi(defaultClient);
    String uploadId = "uploadId_example"; // String | Created session id to proceed with. If you didn't send chunks in the last hour, it is not valid anymore and you need to initialize a new upload. 
    String contentRange = "bytes 0-262143/2469036"; // String | Specifies the bytes in the file that the request is uploading.  For example, a value of `bytes 0-262143/1000000` shows that the request is sending the first 262144 bytes (256 x 1024) in a 2,469,036 byte file. 
    BigDecimal contentLength = new BigDecimal("262144"); // BigDecimal | Size of the chunk that the request is sending.  Remember that larger chunks are more efficient. PeerTube's web client uses chunks varying from 1048576 bytes (~1MB) and increases or reduces size depending on connection health. 
    File body = new File("/path/to/file"); // File | 
    try {
      VideoUploadResponse result = apiInstance.uploadResumable_0(uploadId, contentRange, contentLength, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoUploadApi#uploadResumable_0");
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
| **uploadId** | **String**| Created session id to proceed with. If you didn&#39;t send chunks in the last hour, it is not valid anymore and you need to initialize a new upload.  | |
| **contentRange** | **String**| Specifies the bytes in the file that the request is uploading.  For example, a value of &#x60;bytes 0-262143/1000000&#x60; shows that the request is sending the first 262144 bytes (256 x 1024) in a 2,469,036 byte file.  | |
| **contentLength** | **BigDecimal**| Size of the chunk that the request is sending.  Remember that larger chunks are more efficient. PeerTube&#39;s web client uses chunks varying from 1048576 bytes (~1MB) and increases or reduces size depending on connection health.  | |
| **body** | **File**|  | [optional] |

### Return type

[**VideoUploadResponse**](VideoUploadResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | last chunk received |  * Content-Length -  <br>  |
| **308** | resume incomplete |  * Content-Length -  <br>  * Range -  <br>  |
| **403** | video didn&#39;t pass upload filter |  -  |
| **404** | upload not found |  -  |
| **409** | chunk doesn&#39;t match range |  -  |
| **422** | video unreadable |  -  |
| **429** | too many concurrent requests |  -  |
| **503** | upload is already being processed |  * Retry-After -  <br>  |

