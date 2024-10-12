# EventsV1SubscribedEventApi

All URIs are relative to *https://events.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSubscribedEvent**](EventsV1SubscribedEventApi.md#createSubscribedEvent) | **POST** /v1/Subscriptions/{SubscriptionSid}/SubscribedEvents |  |
| [**deleteSubscribedEvent**](EventsV1SubscribedEventApi.md#deleteSubscribedEvent) | **DELETE** /v1/Subscriptions/{SubscriptionSid}/SubscribedEvents/{Type} |  |
| [**fetchSubscribedEvent**](EventsV1SubscribedEventApi.md#fetchSubscribedEvent) | **GET** /v1/Subscriptions/{SubscriptionSid}/SubscribedEvents/{Type} |  |
| [**listSubscribedEvent**](EventsV1SubscribedEventApi.md#listSubscribedEvent) | **GET** /v1/Subscriptions/{SubscriptionSid}/SubscribedEvents |  |
| [**updateSubscribedEvent**](EventsV1SubscribedEventApi.md#updateSubscribedEvent) | **POST** /v1/Subscriptions/{SubscriptionSid}/SubscribedEvents/{Type} |  |


<a id="createSubscribedEvent"></a>
# **createSubscribedEvent**
> EventsV1SubscriptionSubscribedEvent createSubscribedEvent(subscriptionSid, type, schemaVersion)



Add an event type to a Subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsV1SubscribedEventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    EventsV1SubscribedEventApi apiInstance = new EventsV1SubscribedEventApi(defaultClient);
    String subscriptionSid = "subscriptionSid_example"; // String | The unique SID identifier of the Subscription.
    String type = "type_example"; // String | Type of event being subscribed to.
    Integer schemaVersion = 56; // Integer | The schema version that the Subscription should use.
    try {
      EventsV1SubscriptionSubscribedEvent result = apiInstance.createSubscribedEvent(subscriptionSid, type, schemaVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsV1SubscribedEventApi#createSubscribedEvent");
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
| **subscriptionSid** | **String**| The unique SID identifier of the Subscription. | |
| **type** | **String**| Type of event being subscribed to. | |
| **schemaVersion** | **Integer**| The schema version that the Subscription should use. | [optional] |

### Return type

[**EventsV1SubscriptionSubscribedEvent**](EventsV1SubscriptionSubscribedEvent.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSubscribedEvent"></a>
# **deleteSubscribedEvent**
> deleteSubscribedEvent(subscriptionSid, type)



Remove an event type from a Subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsV1SubscribedEventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    EventsV1SubscribedEventApi apiInstance = new EventsV1SubscribedEventApi(defaultClient);
    String subscriptionSid = "subscriptionSid_example"; // String | The unique SID identifier of the Subscription.
    String type = "type_example"; // String | Type of event being subscribed to.
    try {
      apiInstance.deleteSubscribedEvent(subscriptionSid, type);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsV1SubscribedEventApi#deleteSubscribedEvent");
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
| **subscriptionSid** | **String**| The unique SID identifier of the Subscription. | |
| **type** | **String**| Type of event being subscribed to. | |

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

<a id="fetchSubscribedEvent"></a>
# **fetchSubscribedEvent**
> EventsV1SubscriptionSubscribedEvent fetchSubscribedEvent(subscriptionSid, type)



Read an Event for a Subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsV1SubscribedEventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    EventsV1SubscribedEventApi apiInstance = new EventsV1SubscribedEventApi(defaultClient);
    String subscriptionSid = "subscriptionSid_example"; // String | The unique SID identifier of the Subscription.
    String type = "type_example"; // String | Type of event being subscribed to.
    try {
      EventsV1SubscriptionSubscribedEvent result = apiInstance.fetchSubscribedEvent(subscriptionSid, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsV1SubscribedEventApi#fetchSubscribedEvent");
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
| **subscriptionSid** | **String**| The unique SID identifier of the Subscription. | |
| **type** | **String**| Type of event being subscribed to. | |

### Return type

[**EventsV1SubscriptionSubscribedEvent**](EventsV1SubscriptionSubscribedEvent.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSubscribedEvent"></a>
# **listSubscribedEvent**
> ListSubscribedEventResponse listSubscribedEvent(subscriptionSid, pageSize, page, pageToken)



Retrieve a list of all Subscribed Event types for a Subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsV1SubscribedEventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    EventsV1SubscribedEventApi apiInstance = new EventsV1SubscribedEventApi(defaultClient);
    String subscriptionSid = "subscriptionSid_example"; // String | The unique SID identifier of the Subscription.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSubscribedEventResponse result = apiInstance.listSubscribedEvent(subscriptionSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsV1SubscribedEventApi#listSubscribedEvent");
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
| **subscriptionSid** | **String**| The unique SID identifier of the Subscription. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSubscribedEventResponse**](ListSubscribedEventResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSubscribedEvent"></a>
# **updateSubscribedEvent**
> EventsV1SubscriptionSubscribedEvent updateSubscribedEvent(subscriptionSid, type, schemaVersion)



Update an Event for a Subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsV1SubscribedEventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    EventsV1SubscribedEventApi apiInstance = new EventsV1SubscribedEventApi(defaultClient);
    String subscriptionSid = "subscriptionSid_example"; // String | The unique SID identifier of the Subscription.
    String type = "type_example"; // String | Type of event being subscribed to.
    Integer schemaVersion = 56; // Integer | The schema version that the Subscription should use.
    try {
      EventsV1SubscriptionSubscribedEvent result = apiInstance.updateSubscribedEvent(subscriptionSid, type, schemaVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsV1SubscribedEventApi#updateSubscribedEvent");
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
| **subscriptionSid** | **String**| The unique SID identifier of the Subscription. | |
| **type** | **String**| Type of event being subscribed to. | |
| **schemaVersion** | **Integer**| The schema version that the Subscription should use. | [optional] |

### Return type

[**EventsV1SubscriptionSubscribedEvent**](EventsV1SubscriptionSubscribedEvent.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

