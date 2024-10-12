# EventsApi

All URIs are relative to */story*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storyIdEventsGet**](EventsApi.md#storyIdEventsGet) | **GET** /{id}/events | Events: List Events |
| [**storyIdEventsPost**](EventsApi.md#storyIdEventsPost) | **POST** /{id}/events | Events: Manage Events |


<a id="storyIdEventsGet"></a>
# **storyIdEventsGet**
> List&lt;Event&gt; storyIdEventsGet(id)

Events: List Events

Get a list of Events available to users of this story

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    EventsApi apiInstance = new EventsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    try {
      List<Event> result = apiInstance.storyIdEventsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#storyIdEventsGet");
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
| **id** | **UUID**| the id from the story object | |

### Return type

[**List&lt;Event&gt;**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Array of events |  -  |
| **401** | Unauthorized |  -  |

<a id="storyIdEventsPost"></a>
# **storyIdEventsPost**
> Object storyIdEventsPost(id, manageEvent)

Events: Manage Events

Add a message to the Story&#39;s conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    EventsApi apiInstance = new EventsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    ManageEvent manageEvent = new ManageEvent(); // ManageEvent | Collaborator user id and permission type
    try {
      Object result = apiInstance.storyIdEventsPost(id, manageEvent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#storyIdEventsPost");
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
| **id** | **UUID**| the id from the story object | |
| **manageEvent** | [**ManageEvent**](ManageEvent.md)| Collaborator user id and permission type | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A repsonse to the requested action |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

