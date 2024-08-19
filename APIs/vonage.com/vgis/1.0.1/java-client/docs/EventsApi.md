# EventsApi

All URIs are relative to *https://api.vonage.com/t/vbc.prod/vis/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEvent**](EventsApi.md#getEvent) | **GET** /self/events/{id} | Get event |
| [**getEventsCount**](EventsApi.md#getEventsCount) | **GET** /self/events/count | Get events count |
| [**listEvents**](EventsApi.md#listEvents) | **GET** /self/events | List events |


<a id="getEvent"></a>
# **getEvent**
> List&lt;Event&gt; getEvent(id)

Get event

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
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/vis/v1");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of the event
    try {
      List<Event> result = apiInstance.getEvent(id);
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
| **id** | **String**| Unique identifier of the event | |

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
| **200** | Successful |  -  |
| **400** | Bad Request: The client should not repeat the request without modifications |  -  |
| **401** | Unauthorized: Invalid access token |  -  |
| **403** | Forbidden: The user has no rights to access the resource(s) |  -  |
| **408** | Timeout: The client may repeat the request without modifications |  -  |
| **422** | Validation Error |  -  |
| **500** | Internal Server Error |  -  |
| **502** | Bad Gateway |  -  |

<a id="getEventsCount"></a>
# **getEventsCount**
> EventsCount getEventsCount(fromDate, toDate, direction, states)

Get events count

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
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/vis/v1");

    EventsApi apiInstance = new EventsApi(defaultClient);
    Integer fromDate = 56; // Integer | Return events that occurred after this point in time
    Integer toDate = 56; // Integer | Return events that occurred before this point in time
    String direction = "INBOUND"; // String | Filter by event direction
    String states = "INITIALIZING"; // String | Filter events by state
    try {
      EventsCount result = apiInstance.getEventsCount(fromDate, toDate, direction, states);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#getEventsCount");
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
| **fromDate** | **Integer**| Return events that occurred after this point in time | [optional] |
| **toDate** | **Integer**| Return events that occurred before this point in time | [optional] |
| **direction** | **String**| Filter by event direction | [optional] [enum: INBOUND, OUTBOUND] |
| **states** | **String**| Filter events by state | [optional] [enum: INITIALIZING, RINGING, ACTIVE, HELD, REMOTE_HELD] |

### Return type

[**EventsCount**](EventsCount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |
| **400** | Bad Request: The client should not repeat the request without modifications |  -  |
| **401** | Unauthorized: Invalid access token |  -  |
| **403** | Forbidden: The user has no rights to access the resource(s) |  -  |
| **408** | Timeout: The client may repeat the request without modifications |  -  |
| **422** | Validation Error |  -  |
| **500** | Internal Server Error |  -  |
| **502** | Bad Gateway |  -  |

<a id="listEvents"></a>
# **listEvents**
> List&lt;Event&gt; listEvents(types, fromDate, toDate, direction, states, offset, size, order, sort)

List events

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
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/vis/v1");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String types = "CALL"; // String | Record type
    Integer fromDate = 56; // Integer | Return events that occurred after this point in time
    Integer toDate = 56; // Integer | Return events that occurred before this point in time
    String direction = "INBOUND"; // String | Filter by event direction
    String states = "INITIALIZING"; // String | Filter events by state
    Long offset = 56L; // Long | Page number of events to return
    Integer size = 20; // Integer | Return this amount of events in the response
    String order = "DESC"; // String | Sort in either ascending or descending order'
    String sort = "sort_example"; // String | Sort events by property
    try {
      List<Event> result = apiInstance.listEvents(types, fromDate, toDate, direction, states, offset, size, order, sort);
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
| **types** | **String**| Record type | [optional] [enum: CALL] |
| **fromDate** | **Integer**| Return events that occurred after this point in time | [optional] |
| **toDate** | **Integer**| Return events that occurred before this point in time | [optional] |
| **direction** | **String**| Filter by event direction | [optional] [enum: INBOUND, OUTBOUND] |
| **states** | **String**| Filter events by state | [optional] [enum: INITIALIZING, RINGING, ACTIVE, HELD, REMOTE_HELD, DETACHED, REJECTED, CANCELLED, ANSWERED, MISSED] |
| **offset** | **Long**| Page number of events to return | [optional] |
| **size** | **Integer**| Return this amount of events in the response | [optional] [default to 20] |
| **order** | **String**| Sort in either ascending or descending order&#39; | [optional] [default to ASC] [enum: DESC, ASC] |
| **sort** | **String**| Sort events by property | [optional] |

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
| **200** | Successful |  -  |
| **400** | Bad Request: The client should not repeat the request without modifications |  -  |
| **401** | Unauthorized: Invalid access token |  -  |
| **403** | Forbidden: The user has no rights to access the resource(s) |  -  |
| **408** | Timeout: The client may repeat the request without modifications |  -  |
| **422** | Validation Error |  -  |
| **500** | Internal Server Error |  -  |
| **502** | Bad Gateway |  -  |

