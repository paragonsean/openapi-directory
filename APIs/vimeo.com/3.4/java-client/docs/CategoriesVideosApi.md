# CategoriesVideosApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkCategoryForVideo**](CategoriesVideosApi.md#checkCategoryForVideo) | **GET** /categories/{category}/videos/{video_id} | Check for a video in a category |
| [**getCategoryVideos**](CategoriesVideosApi.md#getCategoryVideos) | **GET** /categories/{category}/videos | Get all the videos in a category |
| [**getVideoCategories**](CategoriesVideosApi.md#getVideoCategories) | **GET** /videos/{video_id}/categories | Get all the categories to which a video belongs |
| [**suggestVideoCategory**](CategoriesVideosApi.md#suggestVideoCategory) | **PUT** /videos/{video_id}/categories | Suggest categories for a video |


<a id="checkCategoryForVideo"></a>
# **checkCategoryForVideo**
> Video checkCategoryForVideo(category, videoId)

Check for a video in a category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesVideosApi;

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

    CategoriesVideosApi apiInstance = new CategoriesVideosApi(defaultClient);
    String category = "animation"; // String | The name of the category.
    BigDecimal videoId = new BigDecimal("273576296"); // BigDecimal | The ID of the video.
    try {
      Video result = apiInstance.checkCategoryForVideo(category, videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesVideosApi#checkCategoryForVideo");
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
| **category** | **String**| The name of the category. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

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
| **200** | The video belongs to the category. |  -  |
| **404** | No such category exists, or the video doesn&#39;t belong to it. |  -  |

<a id="getCategoryVideos"></a>
# **getCategoryVideos**
> List&lt;Video&gt; getCategoryVideos(category, direction, filter, filterEmbeddable, page, perPage, query, sort)

Get all the videos in a category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesVideosApi;

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

    CategoriesVideosApi apiInstance = new CategoriesVideosApi(defaultClient);
    String category = "animation"; // String | The name of the category.
    String direction = "asc"; // String | The sort direction of the results.
    String filter = "conditional_featured"; // String | The attribute by which to filter the results.  Option descriptions:  * `conditional_featured` - Featured (promoted) videos 
    Boolean filterEmbeddable = true; // Boolean | Whether to filter the results by embeddable videos (`true`) or non-embeddable videos (`false`). Required only if **filter** is `embeddable`.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String query = "Stop motion"; // String | The search query to use to filter the results.
    String sort = "alphabetical"; // String | The way to sort the results.
    try {
      List<Video> result = apiInstance.getCategoryVideos(category, direction, filter, filterEmbeddable, page, perPage, query, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesVideosApi#getCategoryVideos");
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
| **category** | **String**| The name of the category. | |
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **filter** | **String**| The attribute by which to filter the results.  Option descriptions:  * &#x60;conditional_featured&#x60; - Featured (promoted) videos  | [optional] [enum: conditional_featured, embeddable] |
| **filterEmbeddable** | **Boolean**| Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;. | [optional] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **query** | **String**| The search query to use to filter the results. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: alphabetical, comments, date, duration, featured, likes, plays, relevant] |

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
| **404** | No such category exists. |  -  |

<a id="getVideoCategories"></a>
# **getVideoCategories**
> List&lt;Category&gt; getVideoCategories(videoId)

Get all the categories to which a video belongs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesVideosApi;

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

    CategoriesVideosApi apiInstance = new CategoriesVideosApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      List<Category> result = apiInstance.getVideoCategories(videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesVideosApi#getVideoCategories");
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

[**List&lt;Category&gt;**](Category.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.category+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The categories were returned. |  -  |
| **404** | No such video exists. |  -  |

<a id="suggestVideoCategory"></a>
# **suggestVideoCategory**
> Category suggestVideoCategory(videoId, suggestVideoCategoryRequest)

Suggest categories for a video

With this method, you can suggest up to two categories and one subcategory for a video. Vimeo makes the final determination about whether the video belongs in these categories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesVideosApi;

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

    CategoriesVideosApi apiInstance = new CategoriesVideosApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    SuggestVideoCategoryRequest suggestVideoCategoryRequest = new SuggestVideoCategoryRequest(); // SuggestVideoCategoryRequest | 
    try {
      Category result = apiInstance.suggestVideoCategory(videoId, suggestVideoCategoryRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesVideosApi#suggestVideoCategory");
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
| **suggestVideoCategoryRequest** | [**SuggestVideoCategoryRequest**](SuggestVideoCategoryRequest.md)|  | |

### Return type

[**Category**](Category.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.category+json
 - **Accept**: application/vnd.vimeo.category+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The categories were suggested. |  -  |
| **403** | You don&#39;t own this video. |  -  |
| **404** | No such video exists, or no such category exists. |  -  |

