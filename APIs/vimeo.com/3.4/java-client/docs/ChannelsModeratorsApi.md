# ChannelsModeratorsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addChannelModerator**](ChannelsModeratorsApi.md#addChannelModerator) | **PUT** /channels/{channel_id}/moderators/{user_id} | Add a specific channel moderator |
| [**addChannelModerators**](ChannelsModeratorsApi.md#addChannelModerators) | **PUT** /channels/{channel_id}/moderators | Add a list of channel moderators |
| [**getChannelModerator**](ChannelsModeratorsApi.md#getChannelModerator) | **GET** /channels/{channel_id}/moderators/{user_id} | Get a specific channel moderator |
| [**getChannelModerators**](ChannelsModeratorsApi.md#getChannelModerators) | **GET** /channels/{channel_id}/moderators | Get all the moderators in a channel |
| [**removeChannelModerator**](ChannelsModeratorsApi.md#removeChannelModerator) | **DELETE** /channels/{channel_id}/moderators/{user_id} | Remove a specific channel moderator |
| [**removeChannelModerators**](ChannelsModeratorsApi.md#removeChannelModerators) | **DELETE** /channels/{channel_id}/moderators | Remove a list of channel moderators |
| [**replaceChannelModerators**](ChannelsModeratorsApi.md#replaceChannelModerators) | **PATCH** /channels/{channel_id}/moderators | Replace the moderators of a channel |


<a id="addChannelModerator"></a>
# **addChannelModerator**
> addChannelModerator(channelId, userId)

Add a specific channel moderator

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsModeratorsApi;

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

    ChannelsModeratorsApi apiInstance = new ChannelsModeratorsApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      apiInstance.addChannelModerator(channelId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsModeratorsApi#addChannelModerator");
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
| **userId** | **BigDecimal**| The ID of the user. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.user+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | The authenticated user doesn&#39;t own the channel, a user is already a moderator of the channel, or you tried to add a user that the authenticated user doesn&#39;t follow. |  -  |
| **404** | No such channel exists, or no such user exists. |  -  |

<a id="addChannelModerators"></a>
# **addChannelModerators**
> addChannelModerators(channelId, addChannelModeratorsRequest)

Add a list of channel moderators

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsModeratorsApi;

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

    ChannelsModeratorsApi apiInstance = new ChannelsModeratorsApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    AddChannelModeratorsRequest addChannelModeratorsRequest = new AddChannelModeratorsRequest(); // AddChannelModeratorsRequest | 
    try {
      apiInstance.addChannelModerators(channelId, addChannelModeratorsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsModeratorsApi#addChannelModerators");
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
| **addChannelModeratorsRequest** | [**AddChannelModeratorsRequest**](AddChannelModeratorsRequest.md)|  | |

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
| **200** | The moderators were added. |  -  |
| **400** | Error code 2908: The list contains more than 100 users. |  -  |
| **403** | The authenticated user doesn&#39;t own the channel, a user is already a moderator of the channel, or you tried to add a user that the authenticated user doesn&#39;t follow. |  -  |
| **404** | No such channel exists, or no such user exists. |  -  |

<a id="getChannelModerator"></a>
# **getChannelModerator**
> User getChannelModerator(channelId, userId)

Get a specific channel moderator

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsModeratorsApi;

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

    ChannelsModeratorsApi apiInstance = new ChannelsModeratorsApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      User result = apiInstance.getChannelModerator(channelId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsModeratorsApi#getChannelModerator");
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
| **userId** | **BigDecimal**| The ID of the user. | |

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.user+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The moderator was returned. |  -  |

<a id="getChannelModerators"></a>
# **getChannelModerators**
> List&lt;User&gt; getChannelModerators(channelId, direction, page, perPage, query, sort)

Get all the moderators in a channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsModeratorsApi;

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

    ChannelsModeratorsApi apiInstance = new ChannelsModeratorsApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    String direction = "asc"; // String | The sort direction of the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String query = "Stop motion"; // String | The search query to use to filter the results.
    String sort = "alphabetical"; // String | The way to sort the results.
    try {
      List<User> result = apiInstance.getChannelModerators(channelId, direction, page, perPage, query, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsModeratorsApi#getChannelModerators");
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
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **query** | **String**| The search query to use to filter the results. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: alphabetical, date] |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.user+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The moderators were returned. |  -  |

<a id="removeChannelModerator"></a>
# **removeChannelModerator**
> removeChannelModerator(channelId, userId)

Remove a specific channel moderator

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsModeratorsApi;

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

    ChannelsModeratorsApi apiInstance = new ChannelsModeratorsApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      apiInstance.removeChannelModerator(channelId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsModeratorsApi#removeChannelModerator");
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
| **userId** | **BigDecimal**| The ID of the user. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.user+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The moderator was removed. |  -  |
| **403** | The authenticated user doesn&#39;t own the channel, the user isn&#39;t a moderator of the channel, or you tried to remove the owner of the channel. |  -  |
| **404** | No such channel exists, or no such user exists. |  -  |

<a id="removeChannelModerators"></a>
# **removeChannelModerators**
> User removeChannelModerators(channelId, removeChannelModeratorsRequest)

Remove a list of channel moderators

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsModeratorsApi;

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

    ChannelsModeratorsApi apiInstance = new ChannelsModeratorsApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    RemoveChannelModeratorsRequest removeChannelModeratorsRequest = new RemoveChannelModeratorsRequest(); // RemoveChannelModeratorsRequest | 
    try {
      User result = apiInstance.removeChannelModerators(channelId, removeChannelModeratorsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsModeratorsApi#removeChannelModerators");
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
| **removeChannelModeratorsRequest** | [**RemoveChannelModeratorsRequest**](RemoveChannelModeratorsRequest.md)|  | |

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.user+json
 - **Accept**: application/vnd.vimeo.user+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The moderators were removed. |  -  |
| **403** | The authenticated user doesn&#39;t own the channel, the user isn&#39;t a moderator of the channel, or you tried to remove the owner of the channel. |  -  |
| **404** | No such channel exists, or no such user exists. |  -  |

<a id="replaceChannelModerators"></a>
# **replaceChannelModerators**
> List&lt;User&gt; replaceChannelModerators(channelId, replaceChannelModeratorsRequest)

Replace the moderators of a channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsModeratorsApi;

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

    ChannelsModeratorsApi apiInstance = new ChannelsModeratorsApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    ReplaceChannelModeratorsRequest replaceChannelModeratorsRequest = new ReplaceChannelModeratorsRequest(); // ReplaceChannelModeratorsRequest | 
    try {
      List<User> result = apiInstance.replaceChannelModerators(channelId, replaceChannelModeratorsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsModeratorsApi#replaceChannelModerators");
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
| **replaceChannelModeratorsRequest** | [**ReplaceChannelModeratorsRequest**](ReplaceChannelModeratorsRequest.md)|  | |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The moderators were replaced. |  -  |
| **400** | Error code 2908: The list contains more than 100 users. |  -  |
| **403** | The authenticated user owns this channel. |  -  |
| **404** | No such channel exists. |  -  |

