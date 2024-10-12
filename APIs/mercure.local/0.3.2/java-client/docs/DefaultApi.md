# DefaultApi

All URIs are relative to *http://mercure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**wellKnownMercureGet**](DefaultApi.md#wellKnownMercureGet) | **GET** /.well-known/mercure | Subscribe to updates |
| [**wellKnownMercurePost**](DefaultApi.md#wellKnownMercurePost) | **POST** /.well-known/mercure | Publish an update |
| [**wellKnownMercureSubscriptionsGet**](DefaultApi.md#wellKnownMercureSubscriptionsGet) | **GET** /.well-known/mercure/subscriptions | Active subscriptions |
| [**wellKnownMercureSubscriptionsTopicGet**](DefaultApi.md#wellKnownMercureSubscriptionsTopicGet) | **GET** /.well-known/mercure/subscriptions/{topic} | Active subscriptions for the given topic |
| [**wellKnownMercureSubscriptionsTopicSubscriberGet**](DefaultApi.md#wellKnownMercureSubscriptionsTopicSubscriberGet) | **GET** /.well-known/mercure/subscriptions/{topic}/{subscriber} | Active subscription for the given topic and subscriber |


<a id="wellKnownMercureGet"></a>
# **wellKnownMercureGet**
> wellKnownMercureGet(topic, lastEventID, lastEventID2)

Subscribe to updates

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
    defaultClient.setBasePath("http://mercure.local");
    
    // Configure API key authorization: Cookie
    ApiKeyAuth Cookie = (ApiKeyAuth) defaultClient.getAuthentication("Cookie");
    Cookie.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Cookie.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    List<String> topic = Arrays.asList(); // List<String> | The topic to get updates from, can be a URI template (RFC6570).
    String lastEventID = "lastEventID_example"; // String | The last received event id, to retrieve missed events.
    String lastEventID2 = "lastEventID_example"; // String | The last received event id, to retrieve missed events, takes precedence over the query parameter.
    try {
      apiInstance.wellKnownMercureGet(topic, lastEventID, lastEventID2);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#wellKnownMercureGet");
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
| **topic** | [**List&lt;String&gt;**](String.md)| The topic to get updates from, can be a URI template (RFC6570). | |
| **lastEventID** | **String**| The last received event id, to retrieve missed events. | [optional] |
| **lastEventID2** | **String**| The last received event id, to retrieve missed events, takes precedence over the query parameter. | [optional] |

### Return type

null (empty response body)

### Authorization

[Cookie](../README.md#Cookie), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event stream opened. |  -  |
| **400** | Missing topic parameter or invalid URI template. |  -  |
| **401** | Not authorized (missing or invalid JWT). |  -  |

<a id="wellKnownMercurePost"></a>
# **wellKnownMercurePost**
> wellKnownMercurePost(data, topic, id, _private, retry, type)

Publish an update

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
    defaultClient.setBasePath("http://mercure.local");
    
    // Configure API key authorization: Cookie
    ApiKeyAuth Cookie = (ApiKeyAuth) defaultClient.getAuthentication("Cookie");
    Cookie.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Cookie.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String data = "data_example"; // String | The content of the new version of this topic.
    List<String> topic = Arrays.asList(); // List<String> | IRIs of the updated topic. If this key is present several times, the first occurrence is considered to be the canonical URL of the topic, and other ones are considered to be alternate URLs.
    String id = "id_example"; // String | The topic's revision identifier: it will be used as the SSE's `id` property.
    Boolean _private = true; // Boolean | To mark an update as private. If not provided, this update will be public.
    Integer retry = 56; // Integer | The SSE's `retry` property (the reconnection time).
    String type = "type_example"; // String | The SSE's `event` property (a specific event type).
    try {
      apiInstance.wellKnownMercurePost(data, topic, id, _private, retry, type);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#wellKnownMercurePost");
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
| **data** | **String**| The content of the new version of this topic. | |
| **topic** | [**List&lt;String&gt;**](String.md)| IRIs of the updated topic. If this key is present several times, the first occurrence is considered to be the canonical URL of the topic, and other ones are considered to be alternate URLs. | |
| **id** | **String**| The topic&#39;s revision identifier: it will be used as the SSE&#39;s &#x60;id&#x60; property. | [optional] |
| **_private** | **Boolean**| To mark an update as private. If not provided, this update will be public. | [optional] |
| **retry** | **Integer**| The SSE&#39;s &#x60;retry&#x60; property (the reconnection time). | [optional] |
| **type** | **String**| The SSE&#39;s &#x60;event&#x60; property (a specific event type). | [optional] |

### Return type

null (empty response body)

### Authorization

[Cookie](../README.md#Cookie), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The id of this update |  -  |
| **400** | Invalid request |  -  |
| **401** | Not authorized (missing or invalid JWT). |  -  |

<a id="wellKnownMercureSubscriptionsGet"></a>
# **wellKnownMercureSubscriptionsGet**
> Subscriptions wellKnownMercureSubscriptionsGet()

Active subscriptions

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
    defaultClient.setBasePath("http://mercure.local");
    
    // Configure API key authorization: Cookie
    ApiKeyAuth Cookie = (ApiKeyAuth) defaultClient.getAuthentication("Cookie");
    Cookie.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Cookie.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      Subscriptions result = apiInstance.wellKnownMercureSubscriptionsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#wellKnownMercureSubscriptionsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Subscriptions**](Subscriptions.md)

### Authorization

[Cookie](../README.md#Cookie), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of active subscriptions |  -  |
| **401** | Not authorized (missing or invalid JWT). |  -  |

<a id="wellKnownMercureSubscriptionsTopicGet"></a>
# **wellKnownMercureSubscriptionsTopicGet**
> Subscriptions wellKnownMercureSubscriptionsTopicGet(topic)

Active subscriptions for the given topic

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
    defaultClient.setBasePath("http://mercure.local");
    
    // Configure API key authorization: Cookie
    ApiKeyAuth Cookie = (ApiKeyAuth) defaultClient.getAuthentication("Cookie");
    Cookie.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Cookie.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String topic = "topic_example"; // String | 
    try {
      Subscriptions result = apiInstance.wellKnownMercureSubscriptionsTopicGet(topic);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#wellKnownMercureSubscriptionsTopicGet");
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
| **topic** | **String**|  | |

### Return type

[**Subscriptions**](Subscriptions.md)

### Authorization

[Cookie](../README.md#Cookie), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of active subscriptions |  -  |
| **401** | Not authorized (missing or invalid JWT). |  -  |

<a id="wellKnownMercureSubscriptionsTopicSubscriberGet"></a>
# **wellKnownMercureSubscriptionsTopicSubscriberGet**
> Subscriptions wellKnownMercureSubscriptionsTopicSubscriberGet(topic, subscriber)

Active subscription for the given topic and subscriber

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
    defaultClient.setBasePath("http://mercure.local");
    
    // Configure API key authorization: Cookie
    ApiKeyAuth Cookie = (ApiKeyAuth) defaultClient.getAuthentication("Cookie");
    Cookie.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Cookie.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String topic = "topic_example"; // String | 
    String subscriber = "subscriber_example"; // String | 
    try {
      Subscriptions result = apiInstance.wellKnownMercureSubscriptionsTopicSubscriberGet(topic, subscriber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#wellKnownMercureSubscriptionsTopicSubscriberGet");
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
| **topic** | **String**|  | |
| **subscriber** | **String**|  | |

### Return type

[**Subscriptions**](Subscriptions.md)

### Authorization

[Cookie](../README.md#Cookie), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of active subscriptions |  -  |
| **401** | Not authorized (missing or invalid JWT). |  -  |

