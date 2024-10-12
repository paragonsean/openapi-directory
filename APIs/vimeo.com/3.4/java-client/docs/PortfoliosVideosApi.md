# PortfoliosVideosApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addVideoToPortfolio**](PortfoliosVideosApi.md#addVideoToPortfolio) | **PUT** /users/{user_id}/portfolios/{portfolio_id}/videos/{video_id} | Add a video to a portfolio |
| [**addVideoToPortfolioAlt1**](PortfoliosVideosApi.md#addVideoToPortfolioAlt1) | **PUT** /me/portfolios/{portfolio_id}/videos/{video_id} | Add a video to a portfolio |
| [**deleteVideoFromPortfolio**](PortfoliosVideosApi.md#deleteVideoFromPortfolio) | **DELETE** /users/{user_id}/portfolios/{portfolio_id}/videos/{video_id} | Remove a video from a portfolio |
| [**deleteVideoFromPortfolioAlt1**](PortfoliosVideosApi.md#deleteVideoFromPortfolioAlt1) | **DELETE** /me/portfolios/{portfolio_id}/videos/{video_id} | Remove a video from a portfolio |
| [**getPortfolioVideo**](PortfoliosVideosApi.md#getPortfolioVideo) | **GET** /users/{user_id}/portfolios/{portfolio_id}/videos/{video_id} | Get a specific video in a portfolio |
| [**getPortfolioVideoAlt1**](PortfoliosVideosApi.md#getPortfolioVideoAlt1) | **GET** /me/portfolios/{portfolio_id}/videos/{video_id} | Get a specific video in a portfolio |
| [**getPortfolioVideos**](PortfoliosVideosApi.md#getPortfolioVideos) | **GET** /users/{user_id}/portfolios/{portfolio_id}/videos | Get all the videos in a portfolio |
| [**getPortfolioVideosAlt1**](PortfoliosVideosApi.md#getPortfolioVideosAlt1) | **GET** /me/portfolios/{portfolio_id}/videos | Get all the videos in a portfolio |


<a id="addVideoToPortfolio"></a>
# **addVideoToPortfolio**
> addVideoToPortfolio(portfolioId, userId, videoId)

Add a video to a portfolio

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortfoliosVideosApi;

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

    PortfoliosVideosApi apiInstance = new PortfoliosVideosApi(defaultClient);
    BigDecimal portfolioId = new BigDecimal("12345"); // BigDecimal | The ID of the portfolio.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.addVideoToPortfolio(portfolioId, userId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortfoliosVideosApi#addVideoToPortfolio");
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
| **portfolioId** | **BigDecimal**| The ID of the portfolio. | |
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
| **404** | The portfolio wasn&#39;t found, or the video wasn&#39;t found. |  -  |

<a id="addVideoToPortfolioAlt1"></a>
# **addVideoToPortfolioAlt1**
> addVideoToPortfolioAlt1(portfolioId, videoId)

Add a video to a portfolio

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortfoliosVideosApi;

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

    PortfoliosVideosApi apiInstance = new PortfoliosVideosApi(defaultClient);
    BigDecimal portfolioId = new BigDecimal("12345"); // BigDecimal | The ID of the portfolio.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.addVideoToPortfolioAlt1(portfolioId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortfoliosVideosApi#addVideoToPortfolioAlt1");
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
| **portfolioId** | **BigDecimal**| The ID of the portfolio. | |
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
| **404** | The portfolio wasn&#39;t found, or the video wasn&#39;t found. |  -  |

<a id="deleteVideoFromPortfolio"></a>
# **deleteVideoFromPortfolio**
> deleteVideoFromPortfolio(portfolioId, userId, videoId)

Remove a video from a portfolio

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortfoliosVideosApi;

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

    PortfoliosVideosApi apiInstance = new PortfoliosVideosApi(defaultClient);
    BigDecimal portfolioId = new BigDecimal("12345"); // BigDecimal | The ID of the portfolio.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.deleteVideoFromPortfolio(portfolioId, userId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortfoliosVideosApi#deleteVideoFromPortfolio");
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
| **portfolioId** | **BigDecimal**| The ID of the portfolio. | |
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
| **204** | The video was deleted. |  -  |
| **404** | The portfolio wasn&#39;t found, or the video wasn&#39;t found. |  -  |

<a id="deleteVideoFromPortfolioAlt1"></a>
# **deleteVideoFromPortfolioAlt1**
> deleteVideoFromPortfolioAlt1(portfolioId, videoId)

Remove a video from a portfolio

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortfoliosVideosApi;

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

    PortfoliosVideosApi apiInstance = new PortfoliosVideosApi(defaultClient);
    BigDecimal portfolioId = new BigDecimal("12345"); // BigDecimal | The ID of the portfolio.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.deleteVideoFromPortfolioAlt1(portfolioId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortfoliosVideosApi#deleteVideoFromPortfolioAlt1");
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
| **portfolioId** | **BigDecimal**| The ID of the portfolio. | |
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
| **204** | The video was deleted. |  -  |
| **404** | The portfolio wasn&#39;t found, or the video wasn&#39;t found. |  -  |

<a id="getPortfolioVideo"></a>
# **getPortfolioVideo**
> Video getPortfolioVideo(portfolioId, userId, videoId)

Get a specific video in a portfolio

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortfoliosVideosApi;

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

    PortfoliosVideosApi apiInstance = new PortfoliosVideosApi(defaultClient);
    BigDecimal portfolioId = new BigDecimal("12345"); // BigDecimal | The ID of the portfolio.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      Video result = apiInstance.getPortfolioVideo(portfolioId, userId, videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortfoliosVideosApi#getPortfolioVideo");
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
| **portfolioId** | **BigDecimal**| The ID of the portfolio. | |
| **userId** | **BigDecimal**| The ID of the user. | |
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
| **200** | The video was returned. |  -  |

<a id="getPortfolioVideoAlt1"></a>
# **getPortfolioVideoAlt1**
> Video getPortfolioVideoAlt1(portfolioId, videoId)

Get a specific video in a portfolio

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortfoliosVideosApi;

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

    PortfoliosVideosApi apiInstance = new PortfoliosVideosApi(defaultClient);
    BigDecimal portfolioId = new BigDecimal("12345"); // BigDecimal | The ID of the portfolio.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      Video result = apiInstance.getPortfolioVideoAlt1(portfolioId, videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortfoliosVideosApi#getPortfolioVideoAlt1");
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
| **portfolioId** | **BigDecimal**| The ID of the portfolio. | |
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
| **200** | The video was returned. |  -  |

<a id="getPortfolioVideos"></a>
# **getPortfolioVideos**
> List&lt;Video&gt; getPortfolioVideos(portfolioId, userId, containingUri, filter, filterEmbeddable, page, perPage, sort)

Get all the videos in a portfolio

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortfoliosVideosApi;

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

    PortfoliosVideosApi apiInstance = new PortfoliosVideosApi(defaultClient);
    BigDecimal portfolioId = new BigDecimal("12345"); // BigDecimal | The ID of the portfolio.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    String containingUri = "/videos/258684937"; // String | The page that contains the video URI.
    String filter = "embeddable"; // String | The attribute by which to filter the results.
    Boolean filterEmbeddable = true; // Boolean | Whether to filter the results by embeddable videos (`true`) or non-embeddable videos (`false`). Required only if **filter** is `embeddable`.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String sort = "alphabetical"; // String | The way to sort the results.  Option descriptions:  * `default` - This will sort to the default sort set on the portfolio. 
    try {
      List<Video> result = apiInstance.getPortfolioVideos(portfolioId, userId, containingUri, filter, filterEmbeddable, page, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortfoliosVideosApi#getPortfolioVideos");
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
| **portfolioId** | **BigDecimal**| The ID of the portfolio. | |
| **userId** | **BigDecimal**| The ID of the user. | |
| **containingUri** | **String**| The page that contains the video URI. | [optional] |
| **filter** | **String**| The attribute by which to filter the results. | [optional] [enum: embeddable] |
| **filterEmbeddable** | **Boolean**| Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;. | [optional] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **sort** | **String**| The way to sort the results.  Option descriptions:  * &#x60;default&#x60; - This will sort to the default sort set on the portfolio.  | [optional] [enum: alphabetical, comments, date, default, likes, manual, plays] |

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

<a id="getPortfolioVideosAlt1"></a>
# **getPortfolioVideosAlt1**
> List&lt;Video&gt; getPortfolioVideosAlt1(portfolioId, containingUri, filter, filterEmbeddable, page, perPage, sort)

Get all the videos in a portfolio

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortfoliosVideosApi;

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

    PortfoliosVideosApi apiInstance = new PortfoliosVideosApi(defaultClient);
    BigDecimal portfolioId = new BigDecimal("12345"); // BigDecimal | The ID of the portfolio.
    String containingUri = "/videos/258684937"; // String | The page that contains the video URI.
    String filter = "embeddable"; // String | The attribute by which to filter the results.
    Boolean filterEmbeddable = true; // Boolean | Whether to filter the results by embeddable videos (`true`) or non-embeddable videos (`false`). Required only if **filter** is `embeddable`.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String sort = "alphabetical"; // String | The way to sort the results.  Option descriptions:  * `default` - This will sort to the default sort set on the portfolio. 
    try {
      List<Video> result = apiInstance.getPortfolioVideosAlt1(portfolioId, containingUri, filter, filterEmbeddable, page, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortfoliosVideosApi#getPortfolioVideosAlt1");
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
| **portfolioId** | **BigDecimal**| The ID of the portfolio. | |
| **containingUri** | **String**| The page that contains the video URI. | [optional] |
| **filter** | **String**| The attribute by which to filter the results. | [optional] [enum: embeddable] |
| **filterEmbeddable** | **Boolean**| Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;. | [optional] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **sort** | **String**| The way to sort the results.  Option descriptions:  * &#x60;default&#x60; - This will sort to the default sort set on the portfolio.  | [optional] [enum: alphabetical, comments, date, default, likes, manual, plays] |

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

