# VideosThumbnailsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createVideoThumbnail**](VideosThumbnailsApi.md#createVideoThumbnail) | **POST** /videos/{video_id}/pictures | Add a video thumbnail |
| [**createVideoThumbnailAlt1**](VideosThumbnailsApi.md#createVideoThumbnailAlt1) | **POST** /channels/{channel_id}/videos/{video_id}/pictures | Add a video thumbnail |
| [**deleteVideoThumbnail**](VideosThumbnailsApi.md#deleteVideoThumbnail) | **DELETE** /videos/{video_id}/pictures/{picture_id} | Delete a video thumbnail |
| [**editVideoThumbnail**](VideosThumbnailsApi.md#editVideoThumbnail) | **PATCH** /videos/{video_id}/pictures/{picture_id} | Edit a video thumbnail |
| [**getVideoThumbnail**](VideosThumbnailsApi.md#getVideoThumbnail) | **GET** /videos/{video_id}/pictures/{picture_id} | Get a video thumbnail |
| [**getVideoThumbnails**](VideosThumbnailsApi.md#getVideoThumbnails) | **GET** /videos/{video_id}/pictures | Get all the thumbnails of a video |
| [**getVideoThumbnailsAlt1**](VideosThumbnailsApi.md#getVideoThumbnailsAlt1) | **GET** /channels/{channel_id}/videos/{video_id}/pictures | Get all the thumbnails of a video |


<a id="createVideoThumbnail"></a>
# **createVideoThumbnail**
> Picture createVideoThumbnail(videoId, createVideoThumbnailAlt1Request)

Add a video thumbnail

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosThumbnailsApi;

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

    VideosThumbnailsApi apiInstance = new VideosThumbnailsApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    CreateVideoThumbnailAlt1Request createVideoThumbnailAlt1Request = new CreateVideoThumbnailAlt1Request(); // CreateVideoThumbnailAlt1Request | 
    try {
      Picture result = apiInstance.createVideoThumbnail(videoId, createVideoThumbnailAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosThumbnailsApi#createVideoThumbnail");
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
| **createVideoThumbnailAlt1Request** | [**CreateVideoThumbnailAlt1Request**](CreateVideoThumbnailAlt1Request.md)|  | [optional] |

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.picture+json
 - **Accept**: application/vnd.vimeo.picture+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The thumbnail was created. |  -  |

<a id="createVideoThumbnailAlt1"></a>
# **createVideoThumbnailAlt1**
> Picture createVideoThumbnailAlt1(channelId, videoId, createVideoThumbnailAlt1Request)

Add a video thumbnail

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosThumbnailsApi;

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

    VideosThumbnailsApi apiInstance = new VideosThumbnailsApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    CreateVideoThumbnailAlt1Request createVideoThumbnailAlt1Request = new CreateVideoThumbnailAlt1Request(); // CreateVideoThumbnailAlt1Request | 
    try {
      Picture result = apiInstance.createVideoThumbnailAlt1(channelId, videoId, createVideoThumbnailAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosThumbnailsApi#createVideoThumbnailAlt1");
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
| **channelId** | **BigDecimal**| The ID of the channel. | |
| **videoId** | **BigDecimal**| The ID of the video. | |
| **createVideoThumbnailAlt1Request** | [**CreateVideoThumbnailAlt1Request**](CreateVideoThumbnailAlt1Request.md)|  | [optional] |

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.picture+json
 - **Accept**: application/vnd.vimeo.picture+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The thumbnail was created. |  -  |

<a id="deleteVideoThumbnail"></a>
# **deleteVideoThumbnail**
> deleteVideoThumbnail(pictureId, videoId)

Delete a video thumbnail

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosThumbnailsApi;

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

    VideosThumbnailsApi apiInstance = new VideosThumbnailsApi(defaultClient);
    BigDecimal pictureId = new BigDecimal("12345"); // BigDecimal | The ID of the picture.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.deleteVideoThumbnail(pictureId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosThumbnailsApi#deleteVideoThumbnail");
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
| **pictureId** | **BigDecimal**| The ID of the picture. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The thumbnail was deleted. |  -  |

<a id="editVideoThumbnail"></a>
# **editVideoThumbnail**
> Picture editVideoThumbnail(pictureId, videoId, editVideoThumbnailRequest)

Edit a video thumbnail

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosThumbnailsApi;

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

    VideosThumbnailsApi apiInstance = new VideosThumbnailsApi(defaultClient);
    BigDecimal pictureId = new BigDecimal("12345"); // BigDecimal | The ID of the picture.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    EditVideoThumbnailRequest editVideoThumbnailRequest = new EditVideoThumbnailRequest(); // EditVideoThumbnailRequest | 
    try {
      Picture result = apiInstance.editVideoThumbnail(pictureId, videoId, editVideoThumbnailRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosThumbnailsApi#editVideoThumbnail");
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
| **pictureId** | **BigDecimal**| The ID of the picture. | |
| **videoId** | **BigDecimal**| The ID of the video. | |
| **editVideoThumbnailRequest** | [**EditVideoThumbnailRequest**](EditVideoThumbnailRequest.md)|  | [optional] |

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.picture+json
 - **Accept**: application/vnd.vimeo.picture+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The thumbnail was edited. |  -  |

<a id="getVideoThumbnail"></a>
# **getVideoThumbnail**
> Picture getVideoThumbnail(pictureId, videoId)

Get a video thumbnail

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosThumbnailsApi;

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

    VideosThumbnailsApi apiInstance = new VideosThumbnailsApi(defaultClient);
    BigDecimal pictureId = new BigDecimal("12345"); // BigDecimal | The ID of the picture.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      Picture result = apiInstance.getVideoThumbnail(pictureId, videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosThumbnailsApi#getVideoThumbnail");
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
| **pictureId** | **BigDecimal**| The ID of the picture. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.picture+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The thumbnail was returned. |  -  |

<a id="getVideoThumbnails"></a>
# **getVideoThumbnails**
> List&lt;Picture&gt; getVideoThumbnails(videoId, page, perPage)

Get all the thumbnails of a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosThumbnailsApi;

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

    VideosThumbnailsApi apiInstance = new VideosThumbnailsApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    try {
      List<Picture> result = apiInstance.getVideoThumbnails(videoId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosThumbnailsApi#getVideoThumbnails");
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
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |

### Return type

[**List&lt;Picture&gt;**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.picture+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The thumbnails were returned. |  -  |

<a id="getVideoThumbnailsAlt1"></a>
# **getVideoThumbnailsAlt1**
> List&lt;Picture&gt; getVideoThumbnailsAlt1(channelId, videoId, page, perPage)

Get all the thumbnails of a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosThumbnailsApi;

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

    VideosThumbnailsApi apiInstance = new VideosThumbnailsApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    try {
      List<Picture> result = apiInstance.getVideoThumbnailsAlt1(channelId, videoId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosThumbnailsApi#getVideoThumbnailsAlt1");
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
| **channelId** | **BigDecimal**| The ID of the channel. | |
| **videoId** | **BigDecimal**| The ID of the video. | |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |

### Return type

[**List&lt;Picture&gt;**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.picture+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The thumbnails were returned. |  -  |

