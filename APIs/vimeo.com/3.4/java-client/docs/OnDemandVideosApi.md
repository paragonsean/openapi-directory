# OnDemandVideosApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addVideoToVod**](OnDemandVideosApi.md#addVideoToVod) | **PUT** /ondemand/pages/{ondemand_id}/videos/{video_id} | Add a video to an On Demand page |
| [**deleteVideoFromVod**](OnDemandVideosApi.md#deleteVideoFromVod) | **DELETE** /ondemand/pages/{ondemand_id}/videos/{video_id} | Remove a video from an On Demand page |
| [**getVodVideo**](OnDemandVideosApi.md#getVodVideo) | **GET** /ondemand/pages/{ondemand_id}/videos/{video_id} | Get a specific video on an On Demand page |
| [**getVodVideos**](OnDemandVideosApi.md#getVodVideos) | **GET** /ondemand/pages/{ondemand_id}/videos | Get all the videos on an On Demand page |


<a id="addVideoToVod"></a>
# **addVideoToVod**
> OnDemandVideo addVideoToVod(ondemandId, videoId, addVideoToVodRequest)

Add a video to an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandVideosApi;

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

    OnDemandVideosApi apiInstance = new OnDemandVideosApi(defaultClient);
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    BigDecimal videoId = new BigDecimal("12345"); // BigDecimal | The ID of the video.
    AddVideoToVodRequest addVideoToVodRequest = new AddVideoToVodRequest(); // AddVideoToVodRequest | 
    try {
      OnDemandVideo result = apiInstance.addVideoToVod(ondemandId, videoId, addVideoToVodRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandVideosApi#addVideoToVod");
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
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |
| **videoId** | **BigDecimal**| The ID of the video. | |
| **addVideoToVodRequest** | [**AddVideoToVodRequest**](AddVideoToVodRequest.md)|  | |

### Return type

[**OnDemandVideo**](OnDemandVideo.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.ondemand.video+json
 - **Accept**: application/vnd.vimeo.ondemand.video+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The video was added. |  -  |
| **400** | You can&#39;t add the video to this On Demand page. |  -  |
| **403** | You can&#39;t modify an On Demand page that you don&#39;t own. |  -  |

<a id="deleteVideoFromVod"></a>
# **deleteVideoFromVod**
> deleteVideoFromVod(ondemandId, videoId)

Remove a video from an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandVideosApi;

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

    OnDemandVideosApi apiInstance = new OnDemandVideosApi(defaultClient);
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    BigDecimal videoId = new BigDecimal("12345"); // BigDecimal | The ID of the video.
    try {
      apiInstance.deleteVideoFromVod(ondemandId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandVideosApi#deleteVideoFromVod");
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
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.video+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The video was deleted. |  -  |
| **403** | You can&#39;t modify an On Demand page that you don&#39;t own. |  -  |

<a id="getVodVideo"></a>
# **getVodVideo**
> Video getVodVideo(ondemandId, videoId)

Get a specific video on an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandVideosApi;

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

    OnDemandVideosApi apiInstance = new OnDemandVideosApi(defaultClient);
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    BigDecimal videoId = new BigDecimal("12345"); // BigDecimal | The ID of the video.
    try {
      Video result = apiInstance.getVodVideo(ondemandId, videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandVideosApi#getVodVideo");
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
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

[**Video**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.video+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The video is on the On Demand page. |  -  |

<a id="getVodVideos"></a>
# **getVodVideos**
> List&lt;Video&gt; getVodVideos(ondemandId, direction, filter, page, perPage, sort)

Get all the videos on an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandVideosApi;

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

    OnDemandVideosApi apiInstance = new OnDemandVideosApi(defaultClient);
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    String direction = "asc"; // String | The sort direction of the results.
    String filter = "all"; // String | The attribute by which to filter the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String sort = "date"; // String | The way to sort the results.
    try {
      List<Video> result = apiInstance.getVodVideos(ondemandId, direction, filter, page, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandVideosApi#getVodVideos");
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
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **filter** | **String**| The attribute by which to filter the results. | [optional] [enum: all, buy, expiring_soon, extra, main, main.viewable, rent, trailer, unwatched, viewable, watched] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: date, default, episode, manual, name, purchase_time, release_date] |

### Return type

[**List&lt;Video&gt;**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.video+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | * The videos were returned. * The videos were returned. |  -  |

