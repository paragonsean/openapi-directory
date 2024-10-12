# DefaultApi

All URIs are relative to *https://listening.api.npr.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAggRecommendations**](DefaultApi.md#getAggRecommendations) | **GET** /v2/aggregation/{aggId}/recommendations | Get a set of recommendations for an aggregation independent of the user&#39;s listening history |
| [**getChannels**](DefaultApi.md#getChannels) | **GET** /v2/channels | Get the list of available channels |
| [**getHistory**](DefaultApi.md#getHistory) | **GET** /v2/history | Get recent ratings the logged-in user has submitted |
| [**getOrganizationCategory**](DefaultApi.md#getOrganizationCategory) | **GET** /v2/organizations/{orgId}/categories/{category}/recommendations | Get a list of recommendations from a category of content from an organization |
| [**getOrganizationOverview**](DefaultApi.md#getOrganizationOverview) | **GET** /v2/organizations/{orgId}/recommendations | Get a variety of details about an organization including various lists of recent audio items |
| [**getPromo**](DefaultApi.md#getPromo) | **GET** /v2/promo/recommendations | Retrieve the most recent promo audio heard by the logged-in user |
| [**getRecommendations**](DefaultApi.md#getRecommendations) | **GET** /v2/recommendations | Get a list of media for the logged-in user from NPR&#39;s recommendation engine |
| [**getSearchRecommendations**](DefaultApi.md#getSearchRecommendations) | **GET** /v2/search/recommendations | Get a list of recent audio and aggregation items associated with search terms |
| [**postRating**](DefaultApi.md#postRating) | **POST** /v2/ratings | Collect new ratings for media previously recommended to the logged-in user |


<a id="getAggRecommendations"></a>
# **getAggRecommendations**
> AggregationAudioItemListDocument getAggRecommendations(aggId, authorization, startNum)

Get a set of recommendations for an aggregation independent of the user&#39;s listening history

This endpoint provides a list of recent audio items associated with the aggregation along with metadata about the aggregation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listening.api.npr.org");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long aggId = 56L; // Long | ID of an aggregation such as a program or podcast. If the specified ID is a program that publishes rundowns, the latest rundown will be returned.
    String authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
    Integer startNum = 0; // Integer | The result to start with. Allows paging through the episodes of a podcast or program, with the default, `startNum=0`, being the most recent episode. Ignored for programs that publish a rundown.
    try {
      AggregationAudioItemListDocument result = apiInstance.getAggRecommendations(aggId, authorization, startNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAggRecommendations");
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
| **aggId** | **Long**| ID of an aggregation such as a program or podcast. If the specified ID is a program that publishes rundowns, the latest rundown will be returned. | |
| **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | |
| **startNum** | **Integer**| The result to start with. Allows paging through the episodes of a podcast or program, with the default, &#x60;startNum&#x3D;0&#x60;, being the most recent episode. Ignored for programs that publish a rundown. | [optional] [default to 0] |

### Return type

[**AggregationAudioItemListDocument**](AggregationAudioItemListDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.collection.doc+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of audio items from the specified aggregation |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **401** | The client is not authorized to complete this request. Check to ensure a valid access token was passed in the headers. |  -  |
| **404** | The resource with the requested ID could not be found, and the server was unable to complete the request. |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **429** | The client has exceeded the number of daily calls as per their rate limit. For now, this only applies to prototype applications and untrusted clients. Trusted clients will never be rate-limited, nor will any production apps. |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **500** | A server error |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **503** | The system is undergoing maintenance and we are unable to fulfill this request. Look for a &#x60;Retry-After&#x60; header to see the predicted time the system will be back up. |  * Retry-After - The predicted time the system will be back up <br>  |

<a id="getChannels"></a>
# **getChannels**
> ChannelsDocument getChannels(authorization, exploreOnly)

Get the list of available channels

These channels allow the user to specify a focus for the content returned in the recommendations endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listening.api.npr.org");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
    Boolean exploreOnly = false; // Boolean | If set to `true`, this call will return only channels that should be shown in the client's `Explore` view
    try {
      ChannelsDocument result = apiInstance.getChannels(authorization, exploreOnly);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getChannels");
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
| **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | |
| **exploreOnly** | **Boolean**| If set to &#x60;true&#x60;, this call will return only channels that should be shown in the client&#39;s &#x60;Explore&#x60; view | [optional] [default to false] |

### Return type

[**ChannelsDocument**](ChannelsDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.collection.doc+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of channels |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **401** | The client is not authorized to complete this request. Check to ensure a valid access token was passed in the headers. |  -  |
| **429** | The client has exceeded the number of daily calls as per their rate limit. For now, this only applies to prototype applications and untrusted clients. Trusted clients will never be rate-limited, nor will any production apps. |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **503** | The system is undergoing maintenance and we are unable to fulfill this request. Look for a &#x60;Retry-After&#x60; header to see the predicted time the system will be back up. |  * Retry-After - The predicted time the system will be back up <br>  |

<a id="getHistory"></a>
# **getHistory**
> AudioItemListDocument getHistory(authorization)

Get recent ratings the logged-in user has submitted

This endpoint provides the list of recently-rated audio recommendations that the logged-in user has consumed. Some rated recommendations are filtered, such as sponsorship and donation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listening.api.npr.org");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
    try {
      AudioItemListDocument result = apiInstance.getHistory(authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getHistory");
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
| **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | |

### Return type

[**AudioItemListDocument**](AudioItemListDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.collection.doc+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of audio items (recommendations) |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **401** | The client is not authorized to complete this request. Check to ensure a valid access token was passed in the headers. |  -  |
| **429** | The client has exceeded the number of daily calls as per their rate limit. For now, this only applies to prototype applications and untrusted clients. Trusted clients will never be rate-limited, nor will any production apps. |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **500** | A server error |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **503** | The system is undergoing maintenance and we are unable to fulfill this request. Look for a &#x60;Retry-After&#x60; header to see the predicted time the system will be back up. |  * Retry-After - The predicted time the system will be back up <br>  |

<a id="getOrganizationCategory"></a>
# **getOrganizationCategory**
> OrganizationCategoryAudioListDocument getOrganizationCategory(orgId, category, authorization)

Get a list of recommendations from a category of content from an organization

This endpoint provides a list of recommendations from a category of content from  an organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listening.api.npr.org");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long orgId = 56L; // Long | ID of an organization, such as an NPR One station
    String category = "newscast"; // String | One of the three categories of content - newscast, story, or podcast
    String authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
    try {
      OrganizationCategoryAudioListDocument result = apiInstance.getOrganizationCategory(orgId, category, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getOrganizationCategory");
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
| **orgId** | **Long**| ID of an organization, such as an NPR One station | |
| **category** | **String**| One of the three categories of content - newscast, story, or podcast | [default to story] [enum: newscast, story, podcast] |
| **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | |

### Return type

[**OrganizationCategoryAudioListDocument**](OrganizationCategoryAudioListDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.collection.doc+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of audio items from a category of content from an organization |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **401** | The client is not authorized to complete this request. Check to ensure a valid access token was passed in the headers. |  -  |
| **404** | The resource with the requested ID could not be found, and the server was unable to complete the request. |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **429** | The client has exceeded the number of daily calls as per their rate limit. For now, this only applies to prototype applications and untrusted clients. Trusted clients will never be rate-limited, nor will any production apps. |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **500** | A server error |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **503** | The system is undergoing maintenance and we are unable to fulfill this request. Look for a &#x60;Retry-After&#x60; header to see the predicted time the system will be back up. |  * Retry-After - The predicted time the system will be back up <br>  |

<a id="getOrganizationOverview"></a>
# **getOrganizationOverview**
> OrganizationOverviewDocument getOrganizationOverview(orgId, authorization)

Get a variety of details about an organization including various lists of recent audio items

This endpoint provides a variety of details about an organization including various lists of recent audio items.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listening.api.npr.org");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long orgId = 56L; // Long | ID of an organization, such as an NPR One station
    String authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
    try {
      OrganizationOverviewDocument result = apiInstance.getOrganizationOverview(orgId, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getOrganizationOverview");
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
| **orgId** | **Long**| ID of an organization, such as an NPR One station | |
| **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | |

### Return type

[**OrganizationOverviewDocument**](OrganizationOverviewDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.collection.doc+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of up to four different categories of audio items from a specific organization |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **401** | The client is not authorized to complete this request. Check to ensure a valid access token was passed in the headers. |  -  |
| **404** | The resource with the requested ID could not be found, and the server was unable to complete the request. |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **429** | The client has exceeded the number of daily calls as per their rate limit. For now, this only applies to prototype applications and untrusted clients. Trusted clients will never be rate-limited, nor will any production apps. |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **500** | A server error |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **503** | The system is undergoing maintenance and we are unable to fulfill this request. Look for a &#x60;Retry-After&#x60; header to see the predicted time the system will be back up. |  * Retry-After - The predicted time the system will be back up <br>  |

<a id="getPromo"></a>
# **getPromo**
> AudioItemListDocument getPromo(authorization)

Retrieve the most recent promo audio heard by the logged-in user

Gets the most recently played promo for which the user has neither tapped through the promo or listened to the target story.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listening.api.npr.org");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
    try {
      AudioItemListDocument result = apiInstance.getPromo(authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPromo");
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
| **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | |

### Return type

[**AudioItemListDocument**](AudioItemListDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.collection.doc+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of audio items (recommendations) |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **401** | The client is not authorized to complete this request. Check to ensure a valid access token was passed in the headers. |  -  |
| **429** | The client has exceeded the number of daily calls as per their rate limit. For now, this only applies to prototype applications and untrusted clients. Trusted clients will never be rate-limited, nor will any production apps. |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **500** | A server error |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **503** | The system is undergoing maintenance and we are unable to fulfill this request. Look for a &#x60;Retry-After&#x60; header to see the predicted time the system will be back up. |  * Retry-After - The predicted time the system will be back up <br>  |

<a id="getRecommendations"></a>
# **getRecommendations**
> AudioItemListDocument getRecommendations(authorization, xAdvertisingID, channel, sharedMediaId, notifiedMediaId)

Get a list of media for the logged-in user from NPR&#39;s recommendation engine

This endpoint returns a list of audio recommendations. It is designed to be used for an initial list of recommendations, and then &#x60;POST /v2/ratings?recommend&#x3D;true&#x60; should be used for subsequent requests for recommendations.  A fully-populated link to the ratings endpoint is returned with each individual recommendation and is located in the AudioItemDocument under the &#x60;links[&#39;recommendations&#39;]&#x60; object. The query parameters in this link should not be modified. Be sure to copy and send back the entire ratings object (RatingData), as new fields may be added to it in the future.  A 500 will be returned if there are no eligible remaining recommendations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listening.api.npr.org");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
    String xAdvertisingID = "xAdvertisingID_example"; // String | A device-specific advertising identifier, if possible. Apple's IDFA is an example.
    String channel = "npr"; // String | Determines the focus of the recommendations returned. Channel `npr` is recommended for most use cases.
    String sharedMediaId = "sharedMediaId_example"; // String | This media was shared directly with the user; if provided, the service will add this recommendation to the top of the list
    String notifiedMediaId = "notifiedMediaId_example"; // String | The user received a push notification about this media; if provided, the service will add this recommendation to the top of the list
    try {
      AudioItemListDocument result = apiInstance.getRecommendations(authorization, xAdvertisingID, channel, sharedMediaId, notifiedMediaId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRecommendations");
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
| **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | |
| **xAdvertisingID** | **String**| A device-specific advertising identifier, if possible. Apple&#39;s IDFA is an example. | [optional] |
| **channel** | **String**| Determines the focus of the recommendations returned. Channel &#x60;npr&#x60; is recommended for most use cases. | [optional] [default to npr] [enum: npr, followed, recommended, emailstories, emailprograms, lapsedusersemail, ongoing email, newscasts, shows] |
| **sharedMediaId** | **String**| This media was shared directly with the user; if provided, the service will add this recommendation to the top of the list | [optional] |
| **notifiedMediaId** | **String**| The user received a push notification about this media; if provided, the service will add this recommendation to the top of the list | [optional] |

### Return type

[**AudioItemListDocument**](AudioItemListDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.collection.doc+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of audio items (recommendations) |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **400** | A bad request; generally, one or more parameters passed in were incorrect or missing |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **401** | The client is not authorized to complete this request. Check to ensure a valid access token was passed in the headers. |  -  |
| **429** | The client has exceeded the number of daily calls as per their rate limit. For now, this only applies to prototype applications and untrusted clients. Trusted clients will never be rate-limited, nor will any production apps. |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **500** | A server error |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **503** | The system is undergoing maintenance and we are unable to fulfill this request. Look for a &#x60;Retry-After&#x60; header to see the predicted time the system will be back up. |  * Retry-After - The predicted time the system will be back up <br>  |

<a id="getSearchRecommendations"></a>
# **getSearchRecommendations**
> SearchListDocument getSearchRecommendations(authorization, searchTerms)

Get a list of recent audio and aggregation items associated with search terms

In the schema shown below, SearchItemDocument is not an actual type of returned object; the object returned by a search will be either an AggregationAudioItemListDocument or an AudioItemDocument.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listening.api.npr.org");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
    String searchTerms = "searchTerms_example"; // String | Search terms to search on; can include URL-encoded punctuation
    try {
      SearchListDocument result = apiInstance.getSearchRecommendations(authorization, searchTerms);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSearchRecommendations");
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
| **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | |
| **searchTerms** | **String**| Search terms to search on; can include URL-encoded punctuation | |

### Return type

[**SearchListDocument**](SearchListDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.collection.doc+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of audio and aggregation items matching the search query |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **401** | The client is not authorized to complete this request. Check to ensure a valid access token was passed in the headers. |  -  |
| **429** | The client has exceeded the number of daily calls as per their rate limit. For now, this only applies to prototype applications and untrusted clients. Trusted clients will never be rate-limited, nor will any production apps. |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **500** | A server error |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **503** | The system is undergoing maintenance and we are unable to fulfill this request. Look for a &#x60;Retry-After&#x60; header to see the predicted time the system will be back up. |  * Retry-After - The predicted time the system will be back up <br>  |

<a id="postRating"></a>
# **postRating**
> AudioItemListDocument postRating(authorization, body, xAdvertisingID, channel, recommend)

Collect new ratings for media previously recommended to the logged-in user

This endpoint is the main mechanism for providing feedback from the user to NPR about the recommendations that are obtained from &#x60;GET /listening/v2/recommendations&#x60;.  A fully-populated link to this endpoint is returned with each individual recommendation and is located in the AudioItemDocument under the &#x60;links[&#39;recommendations&#39;]&#x60; object. The query parameters in this link should not be modified. Be sure to copy and send back the entire ratings object (RatingData), as new fields may be added to it in the future.  This endpoint can return a blank JSON.doc or AudioItemDocument depending on the &#x60;recommend&#x3D;true|false&#x60; parameter. The &#x60;recommend&#x3D;true&#x60; flag allows this endpoint to both receive ratings and send back recommendations in the same call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listening.api.npr.org");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
    List<RatingData> body = Arrays.asList(); // List<RatingData> | A list of RatingData objects which contains data about ratings such as the id of the content, the rating value, elapsed time and more.
    String xAdvertisingID = "xAdvertisingID_example"; // String | A device-specific advertising identifier, if possible. Apple's IDFA is an example.
    String channel = "npr"; // String | Determines the focus of the recommendations returned. Channel `npr` is recommended for most use cases.
    Boolean recommend = true; // Boolean | If set to `false`, this call will return a blank document; otherwise it will return a new recommendation object
    try {
      AudioItemListDocument result = apiInstance.postRating(authorization, body, xAdvertisingID, channel, recommend);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#postRating");
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
| **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | |
| **body** | [**List&lt;RatingData&gt;**](RatingData.md)| A list of RatingData objects which contains data about ratings such as the id of the content, the rating value, elapsed time and more. | |
| **xAdvertisingID** | **String**| A device-specific advertising identifier, if possible. Apple&#39;s IDFA is an example. | [optional] |
| **channel** | **String**| Determines the focus of the recommendations returned. Channel &#x60;npr&#x60; is recommended for most use cases. | [optional] [default to npr] [enum: npr, followed, recommended, emailstories, emailprograms, lapsedusersemail, ongoing email, newscasts, shows] |
| **recommend** | **Boolean**| If set to &#x60;false&#x60;, this call will return a blank document; otherwise it will return a new recommendation object | [optional] [default to true] |

### Return type

[**AudioItemListDocument**](AudioItemListDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/vnd.collection.doc+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If the &#x60;recommend&#x60; param was set to &#x60;true&#x60;, this returns a list of audio items; otherwise, a blank document is returned. |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **400** | A bad request; generally, one or more parameters passed in were incorrect or missing |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **401** | The client is not authorized to complete this request. Check to ensure a valid access token was passed in the headers. |  -  |
| **429** | The client has exceeded the number of daily calls as per their rate limit. For now, this only applies to prototype applications and untrusted clients. Trusted clients will never be rate-limited, nor will any production apps. |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **500** | A server error |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **503** | The system is undergoing maintenance and we are unable to fulfill this request. Look for a &#x60;Retry-After&#x60; header to see the predicted time the system will be back up. |  * Retry-After - The predicted time the system will be back up <br>  |

