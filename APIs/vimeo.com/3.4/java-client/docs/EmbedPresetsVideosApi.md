# EmbedPresetsVideosApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addVideoEmbedPreset**](EmbedPresetsVideosApi.md#addVideoEmbedPreset) | **PUT** /videos/{video_id}/presets/{preset_id} | Add an embed preset to a video |
| [**createVideoCustomLogo**](EmbedPresetsVideosApi.md#createVideoCustomLogo) | **POST** /videos/{video_id}/timelinethumbnails | Add a new custom logo to a video |
| [**deleteVideoEmbedPreset**](EmbedPresetsVideosApi.md#deleteVideoEmbedPreset) | **DELETE** /videos/{video_id}/presets/{preset_id} | Remove an embed preset from a video |
| [**getEmbedPresetVideos**](EmbedPresetsVideosApi.md#getEmbedPresetVideos) | **GET** /users/{user_id}/presets/{preset_id}/videos | Get all the videos that have been added to an embed preset |
| [**getEmbedPresetVideosAlt1**](EmbedPresetsVideosApi.md#getEmbedPresetVideosAlt1) | **GET** /me/presets/{preset_id}/videos | Get all the videos that have been added to an embed preset |
| [**getVideoCustomLogo**](EmbedPresetsVideosApi.md#getVideoCustomLogo) | **GET** /videos/{video_id}/timelinethumbnails/{thumbnail_id} | Get a custom video logo |
| [**getVideoEmbedPreset**](EmbedPresetsVideosApi.md#getVideoEmbedPreset) | **GET** /videos/{video_id}/presets/{preset_id} | Check if an embed preset has been added to a video |


<a id="addVideoEmbedPreset"></a>
# **addVideoEmbedPreset**
> addVideoEmbedPreset(presetId, videoId)

Add an embed preset to a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmbedPresetsVideosApi;

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

    EmbedPresetsVideosApi apiInstance = new EmbedPresetsVideosApi(defaultClient);
    BigDecimal presetId = new BigDecimal("12345"); // BigDecimal | The ID of the preset.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.addVideoEmbedPreset(presetId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmbedPresetsVideosApi#addVideoEmbedPreset");
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
| **presetId** | **BigDecimal**| The ID of the preset. | |
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
| **204** | The embed preset was assigned. |  -  |

<a id="createVideoCustomLogo"></a>
# **createVideoCustomLogo**
> Picture createVideoCustomLogo(videoId)

Add a new custom logo to a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmbedPresetsVideosApi;

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

    EmbedPresetsVideosApi apiInstance = new EmbedPresetsVideosApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      Picture result = apiInstance.createVideoCustomLogo(videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmbedPresetsVideosApi#createVideoCustomLogo");
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

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.picture+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Standard request. |  -  |
| **403** | If the user is attempting to upload pictures for another user&#39;s videos. |  -  |
| **404** | No such video exists. |  -  |

<a id="deleteVideoEmbedPreset"></a>
# **deleteVideoEmbedPreset**
> deleteVideoEmbedPreset(presetId, videoId)

Remove an embed preset from a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmbedPresetsVideosApi;

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

    EmbedPresetsVideosApi apiInstance = new EmbedPresetsVideosApi(defaultClient);
    BigDecimal presetId = new BigDecimal("12345"); // BigDecimal | The ID of the preset.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.deleteVideoEmbedPreset(presetId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmbedPresetsVideosApi#deleteVideoEmbedPreset");
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
| **presetId** | **BigDecimal**| The ID of the preset. | |
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
| **204** | The embed preset was unassigned. |  -  |
| **404** | No such video or embed preset exists. |  -  |

<a id="getEmbedPresetVideos"></a>
# **getEmbedPresetVideos**
> List&lt;Video&gt; getEmbedPresetVideos(presetId, userId, page, perPage)

Get all the videos that have been added to an embed preset

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmbedPresetsVideosApi;

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

    EmbedPresetsVideosApi apiInstance = new EmbedPresetsVideosApi(defaultClient);
    BigDecimal presetId = new BigDecimal("12345"); // BigDecimal | The ID of the preset.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    try {
      List<Video> result = apiInstance.getEmbedPresetVideos(presetId, userId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmbedPresetsVideosApi#getEmbedPresetVideos");
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
| **presetId** | **BigDecimal**| The ID of the preset. | |
| **userId** | **BigDecimal**| The ID of the user. | |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |

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

<a id="getEmbedPresetVideosAlt1"></a>
# **getEmbedPresetVideosAlt1**
> List&lt;Video&gt; getEmbedPresetVideosAlt1(presetId, page, perPage)

Get all the videos that have been added to an embed preset

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmbedPresetsVideosApi;

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

    EmbedPresetsVideosApi apiInstance = new EmbedPresetsVideosApi(defaultClient);
    BigDecimal presetId = new BigDecimal("12345"); // BigDecimal | The ID of the preset.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    try {
      List<Video> result = apiInstance.getEmbedPresetVideosAlt1(presetId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmbedPresetsVideosApi#getEmbedPresetVideosAlt1");
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
| **presetId** | **BigDecimal**| The ID of the preset. | |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |

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

<a id="getVideoCustomLogo"></a>
# **getVideoCustomLogo**
> Picture getVideoCustomLogo(thumbnailId, videoId)

Get a custom video logo

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmbedPresetsVideosApi;

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

    EmbedPresetsVideosApi apiInstance = new EmbedPresetsVideosApi(defaultClient);
    BigDecimal thumbnailId = new BigDecimal("12345"); // BigDecimal | The ID of the picture.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      Picture result = apiInstance.getVideoCustomLogo(thumbnailId, videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmbedPresetsVideosApi#getVideoCustomLogo");
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
| **thumbnailId** | **BigDecimal**| The ID of the picture. | |
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
| **200** | The custom logo was returned. |  -  |
| **403** | If the user isn&#39;t permitted to view this custom logo. |  -  |

<a id="getVideoEmbedPreset"></a>
# **getVideoEmbedPreset**
> getVideoEmbedPreset(presetId, videoId)

Check if an embed preset has been added to a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmbedPresetsVideosApi;

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

    EmbedPresetsVideosApi apiInstance = new EmbedPresetsVideosApi(defaultClient);
    BigDecimal presetId = new BigDecimal("12345"); // BigDecimal | The ID of the preset.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.getVideoEmbedPreset(presetId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmbedPresetsVideosApi#getVideoEmbedPreset");
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
| **presetId** | **BigDecimal**| The ID of the preset. | |
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
| **204** | The embed presets exists. |  -  |
| **404** | No such video or embed preset exists. |  -  |

