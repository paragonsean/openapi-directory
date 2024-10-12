# EventsV1SubscriptionApi

All URIs are relative to *https://events.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSubscription**](EventsV1SubscriptionApi.md#createSubscription) | **POST** /v1/Subscriptions |  |
| [**deleteSubscription**](EventsV1SubscriptionApi.md#deleteSubscription) | **DELETE** /v1/Subscriptions/{Sid} |  |
| [**fetchSubscription**](EventsV1SubscriptionApi.md#fetchSubscription) | **GET** /v1/Subscriptions/{Sid} |  |
| [**listSubscription**](EventsV1SubscriptionApi.md#listSubscription) | **GET** /v1/Subscriptions |  |
| [**updateSubscription**](EventsV1SubscriptionApi.md#updateSubscription) | **POST** /v1/Subscriptions/{Sid} |  |


<a id="createSubscription"></a>
# **createSubscription**
> EventsV1Subscription createSubscription(description, sinkSid, types)



Create a new Subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsV1SubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    EventsV1SubscriptionApi apiInstance = new EventsV1SubscriptionApi(defaultClient);
    String description = "description_example"; // String | A human readable description for the Subscription **This value should not contain PII.**
    String sinkSid = "sinkSid_example"; // String | The SID of the sink that events selected by this subscription should be sent to. Sink must be active for the subscription to be created.
    List<Object> types = Arrays.asList(null); // List<Object> | An array of objects containing the subscribed Event Types
    try {
      EventsV1Subscription result = apiInstance.createSubscription(description, sinkSid, types);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsV1SubscriptionApi#createSubscription");
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
| **description** | **String**| A human readable description for the Subscription **This value should not contain PII.** | |
| **sinkSid** | **String**| The SID of the sink that events selected by this subscription should be sent to. Sink must be active for the subscription to be created. | |
| **types** | [**List&lt;Object&gt;**](Object.md)| An array of objects containing the subscribed Event Types | |

### Return type

[**EventsV1Subscription**](EventsV1Subscription.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSubscription"></a>
# **deleteSubscription**
> deleteSubscription(sid)



Delete a specific Subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsV1SubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    EventsV1SubscriptionApi apiInstance = new EventsV1SubscriptionApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this Subscription.
    try {
      apiInstance.deleteSubscription(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsV1SubscriptionApi#deleteSubscription");
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
| **sid** | **String**| A 34 character string that uniquely identifies this Subscription. | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchSubscription"></a>
# **fetchSubscription**
> EventsV1Subscription fetchSubscription(sid)



Fetch a specific Subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsV1SubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    EventsV1SubscriptionApi apiInstance = new EventsV1SubscriptionApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this Subscription.
    try {
      EventsV1Subscription result = apiInstance.fetchSubscription(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsV1SubscriptionApi#fetchSubscription");
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
| **sid** | **String**| A 34 character string that uniquely identifies this Subscription. | |

### Return type

[**EventsV1Subscription**](EventsV1Subscription.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSubscription"></a>
# **listSubscription**
> ListSubscriptionResponse listSubscription(sinkSid, pageSize, page, pageToken)



Retrieve a paginated list of Subscriptions belonging to the account used to make the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsV1SubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    EventsV1SubscriptionApi apiInstance = new EventsV1SubscriptionApi(defaultClient);
    String sinkSid = "sinkSid_example"; // String | The SID of the sink that the list of Subscriptions should be filtered by.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSubscriptionResponse result = apiInstance.listSubscription(sinkSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsV1SubscriptionApi#listSubscription");
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
| **sinkSid** | **String**| The SID of the sink that the list of Subscriptions should be filtered by. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSubscriptionResponse**](ListSubscriptionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSubscription"></a>
# **updateSubscription**
> EventsV1Subscription updateSubscription(sid, description, sinkSid)



Update a Subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsV1SubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    EventsV1SubscriptionApi apiInstance = new EventsV1SubscriptionApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this Subscription.
    String description = "description_example"; // String | A human readable description for the Subscription.
    String sinkSid = "sinkSid_example"; // String | The SID of the sink that events selected by this subscription should be sent to. Sink must be active for the subscription to be created.
    try {
      EventsV1Subscription result = apiInstance.updateSubscription(sid, description, sinkSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsV1SubscriptionApi#updateSubscription");
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
| **sid** | **String**| A 34 character string that uniquely identifies this Subscription. | |
| **description** | **String**| A human readable description for the Subscription. | [optional] |
| **sinkSid** | **String**| The SID of the sink that events selected by this subscription should be sent to. Sink must be active for the subscription to be created. | [optional] |

### Return type

[**EventsV1Subscription**](EventsV1Subscription.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

