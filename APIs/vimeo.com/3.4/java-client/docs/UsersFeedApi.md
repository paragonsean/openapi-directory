# UsersFeedApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getFeed**](UsersFeedApi.md#getFeed) | **GET** /users/{user_id}/feed | Get all videos in a user&#39;s feed |
| [**getFeedAlt1**](UsersFeedApi.md#getFeedAlt1) | **GET** /me/feed | Get all videos in a user&#39;s feed |


<a id="getFeed"></a>
# **getFeed**
> List&lt;Activity31&gt; getFeed(userId, offset, page, perPage, type)

Get all videos in a user&#39;s feed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersFeedApi;

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

    UsersFeedApi apiInstance = new UsersFeedApi(defaultClient);
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    String offset = "280"; // String | Necessary for proper pagination. You shouldn't provide this value yourself, and instead use the pagination links in the feed response. Please see our [pagination documentation](https://developer.vimeo.com/api/common-formats#using-the-pagination-parameter) for more information.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String type = "appears"; // String | The feed type.
    try {
      List<Activity31> result = apiInstance.getFeed(userId, offset, page, perPage, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersFeedApi#getFeed");
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
| **userId** | **BigDecimal**| The ID of the user. | |
| **offset** | **String**| Necessary for proper pagination. You shouldn&#39;t provide this value yourself, and instead use the pagination links in the feed response. Please see our [pagination documentation](https://developer.vimeo.com/api/common-formats#using-the-pagination-parameter) for more information. | [optional] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **type** | **String**| The feed type. | [optional] [enum: appears, category_featured, channel, facebook_feed, following, group, likes, ondemand_publish, share, tagged_with, twitter_timeline, uploads] |

### Return type

[**List&lt;Activity31&gt;**](Activity31.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.activity+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The videos were returned. |  -  |

<a id="getFeedAlt1"></a>
# **getFeedAlt1**
> List&lt;Activity31&gt; getFeedAlt1(offset, page, perPage, type)

Get all videos in a user&#39;s feed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersFeedApi;

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

    UsersFeedApi apiInstance = new UsersFeedApi(defaultClient);
    String offset = "280"; // String | Necessary for proper pagination. You shouldn't provide this value yourself, and instead use the pagination links in the feed response. Please see our [pagination documentation](https://developer.vimeo.com/api/common-formats#using-the-pagination-parameter) for more information.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String type = "appears"; // String | The feed type.
    try {
      List<Activity31> result = apiInstance.getFeedAlt1(offset, page, perPage, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersFeedApi#getFeedAlt1");
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
| **offset** | **String**| Necessary for proper pagination. You shouldn&#39;t provide this value yourself, and instead use the pagination links in the feed response. Please see our [pagination documentation](https://developer.vimeo.com/api/common-formats#using-the-pagination-parameter) for more information. | [optional] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **type** | **String**| The feed type. | [optional] [enum: appears, category_featured, channel, facebook_feed, following, group, likes, ondemand_publish, share, tagged_with, twitter_timeline, uploads] |

### Return type

[**List&lt;Activity31&gt;**](Activity31.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.activity+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The videos were returned. |  -  |

