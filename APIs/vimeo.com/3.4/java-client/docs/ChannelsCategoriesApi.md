# ChannelsCategoriesApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addChannelCategories**](ChannelsCategoriesApi.md#addChannelCategories) | **PUT** /channels/{channel_id}/categories | Add a list of categories to a channel |
| [**categorizeChannel**](ChannelsCategoriesApi.md#categorizeChannel) | **PUT** /channels/{channel_id}/categories/{category} | Categorize a channel |
| [**deleteChannelCategory**](ChannelsCategoriesApi.md#deleteChannelCategory) | **DELETE** /channels/{channel_id}/categories/{category} | Remove a category from a channel |
| [**getChannelCategories**](ChannelsCategoriesApi.md#getChannelCategories) | **GET** /channels/{channel_id}/categories | Get all the categories in a channel |


<a id="addChannelCategories"></a>
# **addChannelCategories**
> addChannelCategories(channelId, addChannelCategoriesRequest)

Add a list of categories to a channel

This method adds multiple categories to the specified channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsCategoriesApi;

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

    ChannelsCategoriesApi apiInstance = new ChannelsCategoriesApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    AddChannelCategoriesRequest addChannelCategoriesRequest = new AddChannelCategoriesRequest(); // AddChannelCategoriesRequest | 
    try {
      apiInstance.addChannelCategories(channelId, addChannelCategoriesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsCategoriesApi#addChannelCategories");
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
| **addChannelCategoriesRequest** | [**AddChannelCategoriesRequest**](AddChannelCategoriesRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The categories were added. |  -  |
| **400** | * Error code 2205: There was no request body, or the request body is malformed. * Error code 2204: You exceeded the maximum number of channel categories. |  -  |
| **401** | Error code 8003: The user credentials are invalid. |  -  |
| **403** | Error code 3200: The authenticated user can&#39;t add categories to the channel. |  -  |
| **404** | No such channel exists. |  -  |

<a id="categorizeChannel"></a>
# **categorizeChannel**
> categorizeChannel(category, channelId)

Categorize a channel

This method adds a channel to a category.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsCategoriesApi;

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

    ChannelsCategoriesApi apiInstance = new ChannelsCategoriesApi(defaultClient);
    String category = "animation"; // String | The name of the category.
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    try {
      apiInstance.categorizeChannel(category, channelId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsCategoriesApi#categorizeChannel");
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
| **channelId** | **BigDecimal**| The ID of the channel. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.category+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The channel was categorized. |  -  |
| **400** | Error code 2204: You exceeded the maximum number of channel categories. |  -  |
| **401** | Error code 8003: The user credentials are invalid. |  -  |
| **403** | Error code 3200: The authenticated user doesn&#39;t own the channel or isn&#39;t a channel moderator. |  -  |
| **404** | No such channel or category exists. |  -  |

<a id="deleteChannelCategory"></a>
# **deleteChannelCategory**
> deleteChannelCategory(category, channelId)

Remove a category from a channel

This method removes a single category from the specified channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsCategoriesApi;

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

    ChannelsCategoriesApi apiInstance = new ChannelsCategoriesApi(defaultClient);
    String category = "animation"; // String | The name of the category.
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    try {
      apiInstance.deleteChannelCategory(category, channelId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsCategoriesApi#deleteChannelCategory");
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
| **channelId** | **BigDecimal**| The ID of the channel. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.category+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The channel was removed. |  -  |
| **401** | Error code 8003: The user credentials are invalid. |  -  |
| **403** | Error code 3200: The authenticated user doesn&#39;t own the channel or isn&#39;t a channel moderator. |  -  |
| **404** | No such channel or category exists. |  -  |

<a id="getChannelCategories"></a>
# **getChannelCategories**
> List&lt;Category&gt; getChannelCategories(channelId)

Get all the categories in a channel

This method gets all the categories in the specified channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsCategoriesApi;

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

    ChannelsCategoriesApi apiInstance = new ChannelsCategoriesApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    try {
      List<Category> result = apiInstance.getChannelCategories(channelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsCategoriesApi#getChannelCategories");
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
| **404** | No such channel exists. |  -  |

