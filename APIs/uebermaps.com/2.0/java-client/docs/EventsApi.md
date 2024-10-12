# EventsApi

All URIs are relative to *http://uebermaps.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**eventsGet**](EventsApi.md#eventsGet) | **GET** /events | List your own events |
| [**eventsIdDelete**](EventsApi.md#eventsIdDelete) | **DELETE** /events/{id} | Delete event |
| [**eventsIdGet**](EventsApi.md#eventsIdGet) | **GET** /events/{id} | Get event |
| [**eventsIdPatch**](EventsApi.md#eventsIdPatch) | **PATCH** /events/{id} | Update event |
| [**spotsIdEventsGet**](EventsApi.md#spotsIdEventsGet) | **GET** /spots/{id}/events | List events for a given spot |
| [**spotsIdEventsPost**](EventsApi.md#spotsIdEventsPost) | **POST** /spots/{id}/events | Create event |


<a id="eventsGet"></a>
# **eventsGet**
> List&lt;Event&gt; eventsGet(timeframeStart, timeframeEnd, bounds)

List your own events

List your own events.

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
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String timeframeStart = "timeframeStart_example"; // String | Begin of time range of event (ISO 8601 date format).
    String timeframeEnd = "timeframeEnd_example"; // String | End of time range of event (ISO 8601 date format).
    String bounds = "bounds_example"; // String | To refine your event index request to contain only events within                                                             a geographical box pass the followng bounds parameters.                                                             F. e. to get events within 'Hamburg, St. Pauli':                                                             bounds[sw_lat]=53.54831449741324                                                             bounds[sw_lon]=9.943227767944336                                                             bounds[ne_lat]=53.5571103674878                                                             bounds[ne_lon]=9.9776029586792
    try {
      List<Event> result = apiInstance.eventsGet(timeframeStart, timeframeEnd, bounds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventsGet");
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
| **timeframeStart** | **String**| Begin of time range of event (ISO 8601 date format). | [optional] |
| **timeframeEnd** | **String**| End of time range of event (ISO 8601 date format). | [optional] |
| **bounds** | **String**| To refine your event index request to contain only events within                                                             a geographical box pass the followng bounds parameters.                                                             F. e. to get events within &#39;Hamburg, St. Pauli&#39;:                                                             bounds[sw_lat]&#x3D;53.54831449741324                                                             bounds[sw_lon]&#x3D;9.943227767944336                                                             bounds[ne_lat]&#x3D;53.5571103674878                                                             bounds[ne_lon]&#x3D;9.9776029586792 | [optional] |

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
| **200** | Contains list of events. |  -  |

<a id="eventsIdDelete"></a>
# **eventsIdDelete**
> Event eventsIdDelete(id)

Delete event

Delete event.

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
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    EventsApi apiInstance = new EventsApi(defaultClient);
    Integer id = 56; // Integer | Event id
    try {
      Event result = apiInstance.eventsIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventsIdDelete");
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
| **id** | **Integer**| Event id | |

### Return type

[**Event**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains deleted event. |  -  |

<a id="eventsIdGet"></a>
# **eventsIdGet**
> Event eventsIdGet(id)

Get event

Get basic information about an event

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
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    EventsApi apiInstance = new EventsApi(defaultClient);
    Integer id = 56; // Integer | Id of event
    try {
      Event result = apiInstance.eventsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventsIdGet");
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
| **id** | **Integer**| Id of event | |

### Return type

[**Event**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains event data. |  -  |

<a id="eventsIdPatch"></a>
# **eventsIdPatch**
> Map eventsIdPatch(id, event)

Update event

Update event. Wrap event parameters in [event].

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
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    EventsApi apiInstance = new EventsApi(defaultClient);
    Integer id = 56; // Integer | Event id
    EventEditable event = new EventEditable(); // EventEditable | Event attributes
    try {
      Map result = apiInstance.eventsIdPatch(id, event);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventsIdPatch");
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
| **id** | **Integer**| Event id | |
| **event** | [**EventEditable**](EventEditable.md)| Event attributes | [optional] |

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains map data, map settings and your relation to this map |  -  |

<a id="spotsIdEventsGet"></a>
# **spotsIdEventsGet**
> List&lt;Event&gt; spotsIdEventsGet(id, timeframeStart, timeframeEnd, bounds)

List events for a given spot

List maps for a given spot.

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
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    EventsApi apiInstance = new EventsApi(defaultClient);
    Integer id = 56; // Integer | Id of spot
    String timeframeStart = "timeframeStart_example"; // String | Begin of time range of event (ISO 8601 date format).
    String timeframeEnd = "timeframeEnd_example"; // String | End of time range of event (ISO 8601 date format).
    String bounds = "bounds_example"; // String | To refine your event index request to contain only events within                                                             a geographical box pass the followng bounds parameters.                                                             F. e. to get events within 'Hamburg, St. Pauli':                                                             bounds[sw_lat]=53.54831449741324                                                             bounds[sw_lon]=9.943227767944336                                                             bounds[ne_lat]=53.5571103674878                                                             bounds[ne_lon]=9.9776029586792
    try {
      List<Event> result = apiInstance.spotsIdEventsGet(id, timeframeStart, timeframeEnd, bounds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#spotsIdEventsGet");
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
| **id** | **Integer**| Id of spot | |
| **timeframeStart** | **String**| Begin of time range of event (ISO 8601 date format). | [optional] |
| **timeframeEnd** | **String**| End of time range of event (ISO 8601 date format). | [optional] |
| **bounds** | **String**| To refine your event index request to contain only events within                                                             a geographical box pass the followng bounds parameters.                                                             F. e. to get events within &#39;Hamburg, St. Pauli&#39;:                                                             bounds[sw_lat]&#x3D;53.54831449741324                                                             bounds[sw_lon]&#x3D;9.943227767944336                                                             bounds[ne_lat]&#x3D;53.5571103674878                                                             bounds[ne_lon]&#x3D;9.9776029586792 | [optional] |

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
| **200** | Contains list of events. |  -  |

<a id="spotsIdEventsPost"></a>
# **spotsIdEventsPost**
> Event spotsIdEventsPost(id, event)

Create event

Create event. Wrap map parameters in [event].

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
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    EventsApi apiInstance = new EventsApi(defaultClient);
    Integer id = 56; // Integer | Spot id
    EventEditable event = new EventEditable(); // EventEditable | Event attributes
    try {
      Event result = apiInstance.spotsIdEventsPost(id, event);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#spotsIdEventsPost");
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
| **id** | **Integer**| Spot id | |
| **event** | [**EventEditable**](EventEditable.md)| Event attributes | [optional] |

### Return type

[**Event**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains event data |  -  |

