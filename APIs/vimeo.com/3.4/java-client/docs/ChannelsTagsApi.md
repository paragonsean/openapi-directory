# ChannelsTagsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addChannelTag**](ChannelsTagsApi.md#addChannelTag) | **PUT** /channels/{channel_id}/tags/{word} | Add a specific tag to a channel |
| [**addTagsToChannel**](ChannelsTagsApi.md#addTagsToChannel) | **PUT** /channels/{channel_id}/tags | Add a list of tags to a channel |
| [**checkIfChannelHasTag**](ChannelsTagsApi.md#checkIfChannelHasTag) | **GET** /channels/{channel_id}/tags/{word} | Check if a tag has been added to a channel |
| [**deleteTagFromChannel**](ChannelsTagsApi.md#deleteTagFromChannel) | **DELETE** /channels/{channel_id}/tags/{word} | Remove a tag from a channel |
| [**getChannelTags**](ChannelsTagsApi.md#getChannelTags) | **GET** /channels/{channel_id}/tags | Get all the tags that have been added to a channel |


<a id="addChannelTag"></a>
# **addChannelTag**
> addChannelTag(channelId, word)

Add a specific tag to a channel

This method adds a single tag to the specified channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsTagsApi;

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

    ChannelsTagsApi apiInstance = new ChannelsTagsApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    String word = "awesome"; // String | The word to use as the tag.
    try {
      apiInstance.addChannelTag(channelId, word);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsTagsApi#addChannelTag");
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
| **word** | **String**| The word to use as the tag. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.tag+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The tag was added. |  -  |
| **400** | * The tag is invalid, or a parameter is invalid. * Error code 2501: The channel has already reached its maximum number of 20 tags. |  -  |
| **401** | Error code 8003: The user credentials are invalid. |  -  |
| **403** | Error code 3200: The authenticated user can&#39;t add tags to this channel. |  -  |

<a id="addTagsToChannel"></a>
# **addTagsToChannel**
> List&lt;Tag&gt; addTagsToChannel(channelId, addTagsToChannelRequest)

Add a list of tags to a channel

This method adds multiple tags to the specified channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsTagsApi;

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

    ChannelsTagsApi apiInstance = new ChannelsTagsApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    AddTagsToChannelRequest addTagsToChannelRequest = new AddTagsToChannelRequest(); // AddTagsToChannelRequest | 
    try {
      List<Tag> result = apiInstance.addTagsToChannel(channelId, addTagsToChannelRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsTagsApi#addTagsToChannel");
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
| **addTagsToChannelRequest** | [**AddTagsToChannelRequest**](AddTagsToChannelRequest.md)|  | |

### Return type

[**List&lt;Tag&gt;**](Tag.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.tag+json
 - **Accept**: application/vnd.vimeo.tag+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tags were added. |  -  |
| **400** | * No such channel exists, or a parameter is invalid. * Error code 2501: You tried to add more than 20 tags to the channel. * Error code 2205: There was no request body, or the request body is malformed. |  -  |
| **401** | Error code 8003: The user credentials are invalid. |  -  |
| **403** | Error code 3200: The authenticated user can&#39;t add tags to this channel. |  -  |

<a id="checkIfChannelHasTag"></a>
# **checkIfChannelHasTag**
> checkIfChannelHasTag(channelId, word)

Check if a tag has been added to a channel

This method determines whether a specific tag has been added to the channel in question.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsTagsApi;

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

    ChannelsTagsApi apiInstance = new ChannelsTagsApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    String word = "awesome"; // String | The word to use as the tag.
    try {
      apiInstance.checkIfChannelHasTag(channelId, word);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsTagsApi#checkIfChannelHasTag");
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
| **word** | **String**| The word to use as the tag. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.tag+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The tag has been added to the channel. |  -  |
| **400** | No such tag exists. |  -  |
| **404** | Error code 5000: The tag exists, but the channel isn&#39;t tagged by it. |  -  |

<a id="deleteTagFromChannel"></a>
# **deleteTagFromChannel**
> deleteTagFromChannel(channelId, word)

Remove a tag from a channel

This method removes a single tag from the specified channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsTagsApi;

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

    ChannelsTagsApi apiInstance = new ChannelsTagsApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    String word = "awesome"; // String | The word to use as the tag.
    try {
      apiInstance.deleteTagFromChannel(channelId, word);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsTagsApi#deleteTagFromChannel");
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
| **word** | **String**| The word to use as the tag. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.tag+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The tag was removed. |  -  |
| **400** | The tag is invalid, or a parameter is invalid. |  -  |
| **401** | Error code 8003: The user credentials are invalid. |  -  |
| **403** | Error code 3200: The authenticated user can&#39;t remove tags from this channel. |  -  |

<a id="getChannelTags"></a>
# **getChannelTags**
> List&lt;Tag&gt; getChannelTags(channelId)

Get all the tags that have been added to a channel

This method gets all the tags that have been added to the specified channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsTagsApi;

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

    ChannelsTagsApi apiInstance = new ChannelsTagsApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    try {
      List<Tag> result = apiInstance.getChannelTags(channelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsTagsApi#getChannelTags");
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

[**List&lt;Tag&gt;**](Tag.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.tag+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tags were returned. |  -  |
| **400** | No such channel exists. |  -  |

