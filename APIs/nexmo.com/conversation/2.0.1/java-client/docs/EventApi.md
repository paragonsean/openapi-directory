# EventApi

All URIs are relative to *https://api.nexmo.com/v0.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createEvent**](EventApi.md#createEvent) | **POST** /conversations/{conversation_id}/events | Create an event |
| [**deleteEvent**](EventApi.md#deleteEvent) | **DELETE** /conversations/{conversation_id}/events/{event_id} | Delete an event |
| [**getEvent**](EventApi.md#getEvent) | **GET** /conversations/{conversation_id}/events/{event_id} | Retrieve an event |
| [**getEvents**](EventApi.md#getEvents) | **GET** /conversations/{conversation_id}/events | List events |


<a id="createEvent"></a>
# **createEvent**
> CreateEvent201Response createEvent(conversationId, createEventRequest)

Create an event

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v0.1");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    EventApi apiInstance = new EventApi(defaultClient);
    String conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
    CreateEventRequest createEventRequest = new CreateEventRequest(); // CreateEventRequest | 
    try {
      CreateEvent201Response result = apiInstance.createEvent(conversationId, createEventRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#createEvent");
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
| **conversationId** | **String**| Conversation ID | |
| **createEventRequest** | [**CreateEventRequest**](CreateEventRequest.md)|  | [optional] |

### Return type

[**CreateEvent201Response**](CreateEvent201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create New Event Response Payload Object |  -  |

<a id="deleteEvent"></a>
# **deleteEvent**
> Object deleteEvent(conversationId, eventId)

Delete an event

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v0.1");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    EventApi apiInstance = new EventApi(defaultClient);
    String conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
    String eventId = "eventId_example"; // String | Event ID
    try {
      Object result = apiInstance.deleteEvent(conversationId, eventId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#deleteEvent");
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
| **conversationId** | **String**| Conversation ID | |
| **eventId** | **String**| Event ID | |

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success response with empty JSON |  -  |

<a id="getEvent"></a>
# **getEvent**
> EventRetrieved getEvent(conversationId, eventId)

Retrieve an event

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v0.1");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    EventApi apiInstance = new EventApi(defaultClient);
    String conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
    String eventId = "eventId_example"; // String | Event ID
    try {
      EventRetrieved result = apiInstance.getEvent(conversationId, eventId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getEvent");
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
| **conversationId** | **String**| Conversation ID | |
| **eventId** | **String**| Event ID | |

### Return type

[**EventRetrieved**](EventRetrieved.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieve an event Content Payload |  -  |

<a id="getEvents"></a>
# **getEvents**
> List&lt;EventRetrieved&gt; getEvents(conversationId)

List events

This endpoint is **DEPRECATED**. Please use [/v0.2/events](/api/conversation.v2#get-events).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v0.1");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    EventApi apiInstance = new EventApi(defaultClient);
    String conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
    try {
      List<EventRetrieved> result = apiInstance.getEvents(conversationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventApi#getEvents");
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
| **conversationId** | **String**| Conversation ID | |

### Return type

[**List&lt;EventRetrieved&gt;**](EventRetrieved.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieve Events Response Payload Object |  -  |

