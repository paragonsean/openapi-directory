# ChannelsApi

All URIs are relative to *https://api.iqualify.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**offeringsOfferingIdAnalyticsChannelsChannelIdCommentsGet**](ChannelsApi.md#offeringsOfferingIdAnalyticsChannelsChannelIdCommentsGet) | **GET** /offerings/{offeringId}/analytics/channels/{channelId}/comments | Find comments |
| [**offeringsOfferingIdAnalyticsChannelsChannelIdPostsGet**](ChannelsApi.md#offeringsOfferingIdAnalyticsChannelsChannelIdPostsGet) | **GET** /offerings/{offeringId}/analytics/channels/{channelId}/posts | Find posts |
| [**offeringsOfferingIdAnalyticsChannelsChannelIdRepliesGet**](ChannelsApi.md#offeringsOfferingIdAnalyticsChannelsChannelIdRepliesGet) | **GET** /offerings/{offeringId}/analytics/channels/{channelId}/replies | Find replies |
| [**offeringsOfferingIdChannelsChannelIdLearnersDelete**](ChannelsApi.md#offeringsOfferingIdChannelsChannelIdLearnersDelete) | **DELETE** /offerings/{offeringId}/channels/{channelId}/learners | Remove learners from a group channel |
| [**offeringsOfferingIdChannelsChannelIdLearnersGet**](ChannelsApi.md#offeringsOfferingIdChannelsChannelIdLearnersGet) | **GET** /offerings/{offeringId}/channels/{channelId}/learners | Find learners in a group channel |
| [**offeringsOfferingIdChannelsChannelIdLearnersPost**](ChannelsApi.md#offeringsOfferingIdChannelsChannelIdLearnersPost) | **POST** /offerings/{offeringId}/channels/{channelId}/learners | Add learners to a group channel |
| [**offeringsOfferingIdChannelsChannelIdPatch**](ChannelsApi.md#offeringsOfferingIdChannelsChannelIdPatch) | **PATCH** /offerings/{offeringId}/channels/{channelId} | Update channel |
| [**offeringsOfferingIdChannelsGet**](ChannelsApi.md#offeringsOfferingIdChannelsGet) | **GET** /offerings/{offeringId}/channels | Find channels |
| [**offeringsOfferingIdChannelsPost**](ChannelsApi.md#offeringsOfferingIdChannelsPost) | **POST** /offerings/{offeringId}/channels | Add channel |


<a id="offeringsOfferingIdAnalyticsChannelsChannelIdCommentsGet"></a>
# **offeringsOfferingIdAnalyticsChannelsChannelIdCommentsGet**
> List&lt;Comment&gt; offeringsOfferingIdAnalyticsChannelsChannelIdCommentsGet(offeringId, channelId)

Find comments

Responds with a list of comments made in any posts in a specified channel, within an offering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    ChannelsApi apiInstance = new ChannelsApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String channelId = "channelId_example"; // String | channel's id
    try {
      List<Comment> result = apiInstance.offeringsOfferingIdAnalyticsChannelsChannelIdCommentsGet(offeringId, channelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsApi#offeringsOfferingIdAnalyticsChannelsChannelIdCommentsGet");
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
| **offeringId** | **String**| offering&#39;s id | |
| **channelId** | **String**| channel&#39;s id | |

### Return type

[**List&lt;Comment&gt;**](Comment.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdAnalyticsChannelsChannelIdPostsGet"></a>
# **offeringsOfferingIdAnalyticsChannelsChannelIdPostsGet**
> List&lt;HttpPost&gt; offeringsOfferingIdAnalyticsChannelsChannelIdPostsGet(offeringId, channelId)

Find posts

Responds with a list of posts made in a specified channel, within an offering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    ChannelsApi apiInstance = new ChannelsApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String channelId = "channelId_example"; // String | channel's id
    try {
      List<HttpPost> result = apiInstance.offeringsOfferingIdAnalyticsChannelsChannelIdPostsGet(offeringId, channelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsApi#offeringsOfferingIdAnalyticsChannelsChannelIdPostsGet");
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
| **offeringId** | **String**| offering&#39;s id | |
| **channelId** | **String**| channel&#39;s id | |

### Return type

[**List&lt;HttpPost&gt;**](HttpPost.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdAnalyticsChannelsChannelIdRepliesGet"></a>
# **offeringsOfferingIdAnalyticsChannelsChannelIdRepliesGet**
> List&lt;Comment&gt; offeringsOfferingIdAnalyticsChannelsChannelIdRepliesGet(offeringId, channelId)

Find replies

Responds with a list of replies to comments in any posts in a specified channel, within an offering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    ChannelsApi apiInstance = new ChannelsApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String channelId = "channelId_example"; // String | channel's id
    try {
      List<Comment> result = apiInstance.offeringsOfferingIdAnalyticsChannelsChannelIdRepliesGet(offeringId, channelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsApi#offeringsOfferingIdAnalyticsChannelsChannelIdRepliesGet");
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
| **offeringId** | **String**| offering&#39;s id | |
| **channelId** | **String**| channel&#39;s id | |

### Return type

[**List&lt;Comment&gt;**](Comment.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdChannelsChannelIdLearnersDelete"></a>
# **offeringsOfferingIdChannelsChannelIdLearnersDelete**
> offeringsOfferingIdChannelsChannelIdLearnersDelete(offeringId, channelId, offeringsOfferingIdChannelsChannelIdLearnersPostRequest)

Remove learners from a group channel

Removes a learner from the specified group channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    ChannelsApi apiInstance = new ChannelsApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String channelId = "channelId_example"; // String | channel's id
    OfferingsOfferingIdChannelsChannelIdLearnersPostRequest offeringsOfferingIdChannelsChannelIdLearnersPostRequest = new OfferingsOfferingIdChannelsChannelIdLearnersPostRequest(); // OfferingsOfferingIdChannelsChannelIdLearnersPostRequest | 
    try {
      apiInstance.offeringsOfferingIdChannelsChannelIdLearnersDelete(offeringId, channelId, offeringsOfferingIdChannelsChannelIdLearnersPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsApi#offeringsOfferingIdChannelsChannelIdLearnersDelete");
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
| **offeringId** | **String**| offering&#39;s id | |
| **channelId** | **String**| channel&#39;s id | |
| **offeringsOfferingIdChannelsChannelIdLearnersPostRequest** | [**OfferingsOfferingIdChannelsChannelIdLearnersPostRequest**](OfferingsOfferingIdChannelsChannelIdLearnersPostRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Learner successfully removed from the channel. |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdChannelsChannelIdLearnersGet"></a>
# **offeringsOfferingIdChannelsChannelIdLearnersGet**
> ChannelResponse offeringsOfferingIdChannelsChannelIdLearnersGet(offeringId, channelId)

Find learners in a group channel

Finds all learners in a specified group channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    ChannelsApi apiInstance = new ChannelsApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String channelId = "channelId_example"; // String | channel's id
    try {
      ChannelResponse result = apiInstance.offeringsOfferingIdChannelsChannelIdLearnersGet(offeringId, channelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsApi#offeringsOfferingIdChannelsChannelIdLearnersGet");
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
| **offeringId** | **String**| offering&#39;s id | |
| **channelId** | **String**| channel&#39;s id | |

### Return type

[**ChannelResponse**](ChannelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | channel data |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdChannelsChannelIdLearnersPost"></a>
# **offeringsOfferingIdChannelsChannelIdLearnersPost**
> offeringsOfferingIdChannelsChannelIdLearnersPost(offeringId, channelId, offeringsOfferingIdChannelsChannelIdLearnersPostRequest)

Add learners to a group channel

Adds a learner to a specified group channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    ChannelsApi apiInstance = new ChannelsApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String channelId = "channelId_example"; // String | channel's id
    OfferingsOfferingIdChannelsChannelIdLearnersPostRequest offeringsOfferingIdChannelsChannelIdLearnersPostRequest = new OfferingsOfferingIdChannelsChannelIdLearnersPostRequest(); // OfferingsOfferingIdChannelsChannelIdLearnersPostRequest | 
    try {
      apiInstance.offeringsOfferingIdChannelsChannelIdLearnersPost(offeringId, channelId, offeringsOfferingIdChannelsChannelIdLearnersPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsApi#offeringsOfferingIdChannelsChannelIdLearnersPost");
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
| **offeringId** | **String**| offering&#39;s id | |
| **channelId** | **String**| channel&#39;s id | |
| **offeringsOfferingIdChannelsChannelIdLearnersPostRequest** | [**OfferingsOfferingIdChannelsChannelIdLearnersPostRequest**](OfferingsOfferingIdChannelsChannelIdLearnersPostRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Learner successfully added to the channel. |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdChannelsChannelIdPatch"></a>
# **offeringsOfferingIdChannelsChannelIdPatch**
> ChannelResponse offeringsOfferingIdChannelsChannelIdPatch(offeringId, channelId, channel)

Update channel

Updates a channel in an offering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    ChannelsApi apiInstance = new ChannelsApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String channelId = "channelId_example"; // String | channel's id
    Channel channel = new Channel(); // Channel | 
    try {
      ChannelResponse result = apiInstance.offeringsOfferingIdChannelsChannelIdPatch(offeringId, channelId, channel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsApi#offeringsOfferingIdChannelsChannelIdPatch");
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
| **offeringId** | **String**| offering&#39;s id | |
| **channelId** | **String**| channel&#39;s id | |
| **channel** | [**Channel**](Channel.md)|  | |

### Return type

[**ChannelResponse**](ChannelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | channel successfully updated |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdChannelsGet"></a>
# **offeringsOfferingIdChannelsGet**
> List&lt;ChannelResponse&gt; offeringsOfferingIdChannelsGet(offeringId)

Find channels

Responds with a list of channels in an offering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    ChannelsApi apiInstance = new ChannelsApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    try {
      List<ChannelResponse> result = apiInstance.offeringsOfferingIdChannelsGet(offeringId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsApi#offeringsOfferingIdChannelsGet");
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
| **offeringId** | **String**| offering&#39;s id | |

### Return type

[**List&lt;ChannelResponse&gt;**](ChannelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Succesful response |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdChannelsPost"></a>
# **offeringsOfferingIdChannelsPost**
> ChannelResponse offeringsOfferingIdChannelsPost(offeringId, channelRequired)

Add channel

Adds new channel to the specified offering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    ChannelsApi apiInstance = new ChannelsApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    ChannelRequired channelRequired = new ChannelRequired(); // ChannelRequired | 
    try {
      ChannelResponse result = apiInstance.offeringsOfferingIdChannelsPost(offeringId, channelRequired);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelsApi#offeringsOfferingIdChannelsPost");
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
| **offeringId** | **String**| offering&#39;s id | |
| **channelRequired** | [**ChannelRequired**](ChannelRequired.md)|  | |

### Return type

[**ChannelResponse**](ChannelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | channel successfully added |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

