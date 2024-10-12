# FeedsApi

All URIs are relative to *https://io.adafruit.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addFeedToGroup_0**](FeedsApi.md#addFeedToGroup_0) | **POST** /{username}/groups/{group_key}/add | Add an existing Feed to a Group |
| [**allFeeds**](FeedsApi.md#allFeeds) | **GET** /{username}/feeds | All feeds for current user |
| [**allGroupFeeds_0**](FeedsApi.md#allGroupFeeds_0) | **GET** /{username}/groups/{group_key}/feeds | All feeds for current user in a given group |
| [**createFeed**](FeedsApi.md#createFeed) | **POST** /{username}/feeds | Create a new Feed |
| [**createGroupFeed**](FeedsApi.md#createGroupFeed) | **POST** /{username}/groups/{group_key}/feeds | Create a new Feed in a Group |
| [**destroyFeed**](FeedsApi.md#destroyFeed) | **DELETE** /{username}/feeds/{feed_key} | Delete an existing Feed |
| [**getFeed**](FeedsApi.md#getFeed) | **GET** /{username}/feeds/{feed_key} | Get feed by feed key |
| [**getFeedDetails**](FeedsApi.md#getFeedDetails) | **GET** /{username}/feeds/{feed_key}/details | Get detailed feed by feed key |
| [**removeFeedFromGroup_0**](FeedsApi.md#removeFeedFromGroup_0) | **POST** /{username}/groups/{group_key}/remove | Remove a Feed from a Group |
| [**replaceFeed**](FeedsApi.md#replaceFeed) | **PUT** /{username}/feeds/{feed_key} | Replace an existing Feed |
| [**updateFeed**](FeedsApi.md#updateFeed) | **PATCH** /{username}/feeds/{feed_key} | Update properties of an existing Feed |


<a id="addFeedToGroup_0"></a>
# **addFeedToGroup_0**
> Group addFeedToGroup_0(groupKey, username, feedKey)

Add an existing Feed to a Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    String groupKey = "groupKey_example"; // String | 
    String username = "username_example"; // String | a valid username string
    String feedKey = "feedKey_example"; // String | 
    try {
      Group result = apiInstance.addFeedToGroup_0(groupKey, username, feedKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#addFeedToGroup_0");
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
| **groupKey** | **String**|  | |
| **username** | **String**| a valid username string | |
| **feedKey** | **String**|  | [optional] |

### Return type

[**Group**](Group.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated group |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="allFeeds"></a>
# **allFeeds**
> List&lt;Feed&gt; allFeeds(username)

All feeds for current user

The Feeds endpoint returns information about the user&#39;s feeds. The response includes the latest value of each feed, and other metadata about each feed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    try {
      List<Feed> result = apiInstance.allFeeds(username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#allFeeds");
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
| **username** | **String**| a valid username string | |

### Return type

[**List&lt;Feed&gt;**](Feed.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of feeds |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="allGroupFeeds_0"></a>
# **allGroupFeeds_0**
> List&lt;Feed&gt; allGroupFeeds_0(groupKey, username)

All feeds for current user in a given group

The Group Feeds endpoint returns information about the user&#39;s feeds. The response includes the latest value of each feed, and other metadata about each feed, but only for feeds within the given group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    String groupKey = "groupKey_example"; // String | 
    String username = "username_example"; // String | a valid username string
    try {
      List<Feed> result = apiInstance.allGroupFeeds_0(groupKey, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#allGroupFeeds_0");
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
| **groupKey** | **String**|  | |
| **username** | **String**| a valid username string | |

### Return type

[**List&lt;Feed&gt;**](Feed.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of feeds |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="createFeed"></a>
# **createFeed**
> Feed createFeed(username, feed, groupKey)

Create a new Feed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    CreateFeedRequest feed = new CreateFeedRequest(); // CreateFeedRequest | 
    String groupKey = "groupKey_example"; // String | 
    try {
      Feed result = apiInstance.createFeed(username, feed, groupKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#createFeed");
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
| **username** | **String**| a valid username string | |
| **feed** | [**CreateFeedRequest**](CreateFeedRequest.md)|  | |
| **groupKey** | **String**|  | [optional] |

### Return type

[**Feed**](Feed.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | New feed |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="createGroupFeed"></a>
# **createGroupFeed**
> Feed createGroupFeed(username, groupKey, feed)

Create a new Feed in a Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String groupKey = "groupKey_example"; // String | 
    CreateFeedRequest feed = new CreateFeedRequest(); // CreateFeedRequest | 
    try {
      Feed result = apiInstance.createGroupFeed(username, groupKey, feed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#createGroupFeed");
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
| **username** | **String**| a valid username string | |
| **groupKey** | **String**|  | |
| **feed** | [**CreateFeedRequest**](CreateFeedRequest.md)|  | |

### Return type

[**Feed**](Feed.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | New feed |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="destroyFeed"></a>
# **destroyFeed**
> destroyFeed(username, feedKey)

Delete an existing Feed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String feedKey = "feedKey_example"; // String | a valid feed key
    try {
      apiInstance.destroyFeed(username, feedKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#destroyFeed");
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
| **username** | **String**| a valid username string | |
| **feedKey** | **String**| a valid feed key | |

### Return type

null (empty response body)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted feed successfully |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="getFeed"></a>
# **getFeed**
> Feed getFeed(username, feedKey)

Get feed by feed key

Returns feed based on the feed key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String feedKey = "feedKey_example"; // String | a valid feed key
    try {
      Feed result = apiInstance.getFeed(username, feedKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#getFeed");
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
| **username** | **String**| a valid username string | |
| **feedKey** | **String**| a valid feed key | |

### Return type

[**Feed**](Feed.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Feed response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="getFeedDetails"></a>
# **getFeedDetails**
> Feed getFeedDetails(username, feedKey)

Get detailed feed by feed key

Returns more detailed feed record based on the feed key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String feedKey = "feedKey_example"; // String | a valid feed key
    try {
      Feed result = apiInstance.getFeedDetails(username, feedKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#getFeedDetails");
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
| **username** | **String**| a valid username string | |
| **feedKey** | **String**| a valid feed key | |

### Return type

[**Feed**](Feed.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Feed response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="removeFeedFromGroup_0"></a>
# **removeFeedFromGroup_0**
> Group removeFeedFromGroup_0(groupKey, username, feedKey)

Remove a Feed from a Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    String groupKey = "groupKey_example"; // String | 
    String username = "username_example"; // String | a valid username string
    String feedKey = "feedKey_example"; // String | 
    try {
      Group result = apiInstance.removeFeedFromGroup_0(groupKey, username, feedKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#removeFeedFromGroup_0");
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
| **groupKey** | **String**|  | |
| **username** | **String**| a valid username string | |
| **feedKey** | **String**|  | [optional] |

### Return type

[**Group**](Group.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated group |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="replaceFeed"></a>
# **replaceFeed**
> Feed replaceFeed(username, feedKey, feed)

Replace an existing Feed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String feedKey = "feedKey_example"; // String | a valid feed key
    CreateFeedRequest feed = new CreateFeedRequest(); // CreateFeedRequest | 
    try {
      Feed result = apiInstance.replaceFeed(username, feedKey, feed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#replaceFeed");
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
| **username** | **String**| a valid username string | |
| **feedKey** | **String**| a valid feed key | |
| **feed** | [**CreateFeedRequest**](CreateFeedRequest.md)|  | |

### Return type

[**Feed**](Feed.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated feed |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="updateFeed"></a>
# **updateFeed**
> Feed updateFeed(username, feedKey, feed)

Update properties of an existing Feed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    FeedsApi apiInstance = new FeedsApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String feedKey = "feedKey_example"; // String | a valid feed key
    CreateFeedRequest feed = new CreateFeedRequest(); // CreateFeedRequest | 
    try {
      Feed result = apiInstance.updateFeed(username, feedKey, feed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedsApi#updateFeed");
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
| **username** | **String**| a valid username string | |
| **feedKey** | **String**| a valid feed key | |
| **feed** | [**CreateFeedRequest**](CreateFeedRequest.md)|  | |

### Return type

[**Feed**](Feed.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated feed |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

