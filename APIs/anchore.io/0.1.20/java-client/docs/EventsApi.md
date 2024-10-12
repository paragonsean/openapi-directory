# EventsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteEvent**](EventsApi.md#deleteEvent) | **DELETE** /events/{eventId} | Delete Event |
| [**deleteEvents**](EventsApi.md#deleteEvents) | **DELETE** /events | Delete Events |
| [**getEvent**](EventsApi.md#getEvent) | **GET** /events/{eventId} | Get Event |
| [**listEventTypes**](EventsApi.md#listEventTypes) | **GET** /event_types | List Event Types |
| [**listEvents**](EventsApi.md#listEvents) | **GET** /events | List Events |


<a id="deleteEvent"></a>
# **deleteEvent**
> deleteEvent(eventId, xAnchoreAccount)

Delete Event

Delete an event by its event ID

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
    defaultClient.setBasePath("http://localhost");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String eventId = "eventId_example"; // String | Event ID of the event to be deleted
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      apiInstance.deleteEvent(eventId, xAnchoreAccount);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#deleteEvent");
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
| **eventId** | **String**| Event ID of the event to be deleted | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete success |  -  |

<a id="deleteEvents"></a>
# **deleteEvents**
> List&lt;String&gt; deleteEvents(before, since, level, xAnchoreAccount)

Delete Events

Delete all or a subset of events filtered using the optional query parameters

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
    defaultClient.setBasePath("http://localhost");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String before = "before_example"; // String | Delete events that occurred before the timestamp
    String since = "since_example"; // String | Delete events that occurred after the timestamp
    String level = "level_example"; // String | Delete events that match the level - INFO or ERROR
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<String> result = apiInstance.deleteEvents(before, since, level, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#deleteEvents");
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
| **before** | **String**| Delete events that occurred before the timestamp | [optional] |
| **since** | **String**| Delete events that occurred after the timestamp | [optional] |
| **level** | **String**| Delete events that match the level - INFO or ERROR | [optional] |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of deleted event IDs |  -  |
| **500** | Internal Error |  -  |

<a id="getEvent"></a>
# **getEvent**
> EventResponse getEvent(eventId, xAnchoreAccount)

Get Event

Lookup an event by its event ID

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
    defaultClient.setBasePath("http://localhost");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String eventId = "eventId_example"; // String | Event ID of the event for lookup
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      EventResponse result = apiInstance.getEvent(eventId, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#getEvent");
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
| **eventId** | **String**| Event ID of the event for lookup | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single event record |  -  |

<a id="listEventTypes"></a>
# **listEventTypes**
> List&lt;EventCategory&gt; listEventTypes()

List Event Types

Returns list of event types in the category hierarchy

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
    defaultClient.setBasePath("http://localhost");

    EventsApi apiInstance = new EventsApi(defaultClient);
    try {
      List<EventCategory> result = apiInstance.listEventTypes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#listEventTypes");
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

[**List&lt;EventCategory&gt;**](EventCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of event types |  -  |

<a id="listEvents"></a>
# **listEvents**
> EventsList listEvents(sourceServicename, sourceHostid, eventType, resourceType, resourceId, level, since, before, page, limit, xAnchoreAccount)

List Events

Returns a paginated list of events in the descending order of their occurrence. Optional query parameters may be used for filtering results

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
    defaultClient.setBasePath("http://localhost");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String sourceServicename = "sourceServicename_example"; // String | Filter events by the originating service
    String sourceHostid = "sourceHostid_example"; // String | Filter events by the originating host ID
    String eventType = "eventType_example"; // String | Filter events by a prefix match on the event type (e.g. \"user.image.\")
    String resourceType = "resourceType_example"; // String | Filter events by the type of resource - tag, imageDigest, repository etc
    String resourceId = "resourceId_example"; // String | Filter events by the id of the resource
    String level = "level_example"; // String | Filter events by the level - INFO or ERROR
    String since = "since_example"; // String | Return events that occurred after the timestamp
    String before = "before_example"; // String | Return events that occurred before the timestamp
    Integer page = 1; // Integer | Pagination controls - return the nth page of results. Defaults to first page if left empty
    Integer limit = 100; // Integer | Number of events in the result set. Defaults to 100 if left empty
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      EventsList result = apiInstance.listEvents(sourceServicename, sourceHostid, eventType, resourceType, resourceId, level, since, before, page, limit, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#listEvents");
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
| **sourceServicename** | **String**| Filter events by the originating service | [optional] |
| **sourceHostid** | **String**| Filter events by the originating host ID | [optional] |
| **eventType** | **String**| Filter events by a prefix match on the event type (e.g. \&quot;user.image.\&quot;) | [optional] |
| **resourceType** | **String**| Filter events by the type of resource - tag, imageDigest, repository etc | [optional] |
| **resourceId** | **String**| Filter events by the id of the resource | [optional] |
| **level** | **String**| Filter events by the level - INFO or ERROR | [optional] |
| **since** | **String**| Return events that occurred after the timestamp | [optional] |
| **before** | **String**| Return events that occurred before the timestamp | [optional] |
| **page** | **Integer**| Pagination controls - return the nth page of results. Defaults to first page if left empty | [optional] [default to 1] |
| **limit** | **Integer**| Number of events in the result set. Defaults to 100 if left empty | [optional] [default to 100] |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**EventsList**](EventsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated list of event records and the next token |  -  |

