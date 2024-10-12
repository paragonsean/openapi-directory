# VideosCreditsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addVideoCredit**](VideosCreditsApi.md#addVideoCredit) | **POST** /videos/{video_id}/credits | Credit a user in a video |
| [**addVideoCreditAlt1**](VideosCreditsApi.md#addVideoCreditAlt1) | **POST** /channels/{channel_id}/videos/{video_id}/credits | Credit a user in a video |
| [**deleteVideoCredit**](VideosCreditsApi.md#deleteVideoCredit) | **DELETE** /videos/{video_id}/credits/{credit_id} | Delete a credit for a user in a video |
| [**editVideoCredit**](VideosCreditsApi.md#editVideoCredit) | **PATCH** /videos/{video_id}/credits/{credit_id} | Edit a credit for a user in a video |
| [**getVideoCredit**](VideosCreditsApi.md#getVideoCredit) | **GET** /videos/{video_id}/credits/{credit_id} | Get a specific credited user in a video |
| [**getVideoCredits**](VideosCreditsApi.md#getVideoCredits) | **GET** /videos/{video_id}/credits | Get all the credited users in a video |
| [**getVideoCreditsAlt1**](VideosCreditsApi.md#getVideoCreditsAlt1) | **GET** /channels/{channel_id}/videos/{video_id}/credits | Get all the credited users in a video |


<a id="addVideoCredit"></a>
# **addVideoCredit**
> Credit addVideoCredit(videoId, addVideoCreditAlt1Request)

Credit a user in a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosCreditsApi;

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

    VideosCreditsApi apiInstance = new VideosCreditsApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    AddVideoCreditAlt1Request addVideoCreditAlt1Request = new AddVideoCreditAlt1Request(); // AddVideoCreditAlt1Request | 
    try {
      Credit result = apiInstance.addVideoCredit(videoId, addVideoCreditAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosCreditsApi#addVideoCredit");
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
| **addVideoCreditAlt1Request** | [**AddVideoCreditAlt1Request**](AddVideoCreditAlt1Request.md)|  | |

### Return type

[**Credit**](Credit.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.credit+json
 - **Accept**: application/vnd.vimeo.credit+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The credit was added. |  -  |
| **400** | * The credit was added. * A parameter is invalid. * The authenticated user has an unverified email address. * There is a user block between the video owner and the person receiving credit. |  -  |
| **403** | The authenticated user doesn&#39;t own the video. |  -  |

<a id="addVideoCreditAlt1"></a>
# **addVideoCreditAlt1**
> Credit addVideoCreditAlt1(channelId, videoId, addVideoCreditAlt1Request)

Credit a user in a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosCreditsApi;

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

    VideosCreditsApi apiInstance = new VideosCreditsApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    AddVideoCreditAlt1Request addVideoCreditAlt1Request = new AddVideoCreditAlt1Request(); // AddVideoCreditAlt1Request | 
    try {
      Credit result = apiInstance.addVideoCreditAlt1(channelId, videoId, addVideoCreditAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosCreditsApi#addVideoCreditAlt1");
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
| **addVideoCreditAlt1Request** | [**AddVideoCreditAlt1Request**](AddVideoCreditAlt1Request.md)|  | |

### Return type

[**Credit**](Credit.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.credit+json
 - **Accept**: application/vnd.vimeo.credit+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The credit was added. |  -  |
| **400** | * The credit was added. * A parameter is invalid. * The authenticated user has an unverified email address. * There is a user block between the video owner and the person receiving credit. |  -  |
| **403** | The authenticated user doesn&#39;t own the video. |  -  |

<a id="deleteVideoCredit"></a>
# **deleteVideoCredit**
> deleteVideoCredit(creditId, videoId)

Delete a credit for a user in a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosCreditsApi;

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

    VideosCreditsApi apiInstance = new VideosCreditsApi(defaultClient);
    BigDecimal creditId = new BigDecimal("12345"); // BigDecimal | The ID of the credit.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.deleteVideoCredit(creditId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosCreditsApi#deleteVideoCredit");
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
| **creditId** | **BigDecimal**| The ID of the credit. | |
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
| **204** | The credit was deleted. |  -  |
| **400** | The authenticated user is neither the creator of the credit nor the credited user. |  -  |

<a id="editVideoCredit"></a>
# **editVideoCredit**
> Credit editVideoCredit(creditId, videoId, editVideoCreditRequest)

Edit a credit for a user in a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosCreditsApi;

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

    VideosCreditsApi apiInstance = new VideosCreditsApi(defaultClient);
    BigDecimal creditId = new BigDecimal("12345"); // BigDecimal | The ID of the credit.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    EditVideoCreditRequest editVideoCreditRequest = new EditVideoCreditRequest(); // EditVideoCreditRequest | 
    try {
      Credit result = apiInstance.editVideoCredit(creditId, videoId, editVideoCreditRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosCreditsApi#editVideoCredit");
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
| **creditId** | **BigDecimal**| The ID of the credit. | |
| **videoId** | **BigDecimal**| The ID of the video. | |
| **editVideoCreditRequest** | [**EditVideoCreditRequest**](EditVideoCreditRequest.md)|  | [optional] |

### Return type

[**Credit**](Credit.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.credit+json
 - **Accept**: application/vnd.vimeo.credit+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The credit was edited. |  -  |
| **400** | A parameter is invalid. |  -  |
| **404** | No such video or credit exists. |  -  |

<a id="getVideoCredit"></a>
# **getVideoCredit**
> Credit getVideoCredit(creditId, videoId)

Get a specific credited user in a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosCreditsApi;

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

    VideosCreditsApi apiInstance = new VideosCreditsApi(defaultClient);
    BigDecimal creditId = new BigDecimal("12345"); // BigDecimal | The ID of the credit.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      Credit result = apiInstance.getVideoCredit(creditId, videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosCreditsApi#getVideoCredit");
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
| **creditId** | **BigDecimal**| The ID of the credit. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

[**Credit**](Credit.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.credit+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The credit was returned. |  -  |
| **404** | No such video or credit exists. |  -  |

<a id="getVideoCredits"></a>
# **getVideoCredits**
> List&lt;Credit&gt; getVideoCredits(videoId, direction, page, perPage, query, sort)

Get all the credited users in a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosCreditsApi;

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

    VideosCreditsApi apiInstance = new VideosCreditsApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    String direction = "asc"; // String | The sort direction of the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String query = "Stop motion"; // String | The search query to use to filter the results.
    String sort = "alphabetical"; // String | The way to sort the results.
    try {
      List<Credit> result = apiInstance.getVideoCredits(videoId, direction, page, perPage, query, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosCreditsApi#getVideoCredits");
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
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **query** | **String**| The search query to use to filter the results. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: alphabetical, date] |

### Return type

[**List&lt;Credit&gt;**](Credit.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.credit+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The users were returned. |  -  |

<a id="getVideoCreditsAlt1"></a>
# **getVideoCreditsAlt1**
> List&lt;Credit&gt; getVideoCreditsAlt1(channelId, videoId, direction, page, perPage, query, sort)

Get all the credited users in a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosCreditsApi;

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

    VideosCreditsApi apiInstance = new VideosCreditsApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    String direction = "asc"; // String | The sort direction of the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String query = "Stop motion"; // String | The search query to use to filter the results.
    String sort = "alphabetical"; // String | The way to sort the results.
    try {
      List<Credit> result = apiInstance.getVideoCreditsAlt1(channelId, videoId, direction, page, perPage, query, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosCreditsApi#getVideoCreditsAlt1");
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
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **query** | **String**| The search query to use to filter the results. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: alphabetical, date] |

### Return type

[**List&lt;Credit&gt;**](Credit.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.credit+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The users were returned. |  -  |

