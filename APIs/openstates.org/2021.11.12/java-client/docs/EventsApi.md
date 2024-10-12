# EventsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**eventDetailEventsEventIdGet**](EventsApi.md#eventDetailEventsEventIdGet) | **GET** /events/{event_id} | Event Detail |
| [**eventListEventsGet**](EventsApi.md#eventListEventsGet) | **GET** /events | Event List |


<a id="eventDetailEventsEventIdGet"></a>
# **eventDetailEventsEventIdGet**
> Event eventDetailEventsEventIdGet(eventId, include, apikey, xApiKey)

Event Detail

Get details on a single event by ID.

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
    String eventId = "eventId_example"; // String | 
    List<EventInclude> include = Arrays.asList(); // List<EventInclude> | Additional includes for the Event response.
    String apikey = "apikey_example"; // String | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      Event result = apiInstance.eventDetailEventsEventIdGet(eventId, include, apikey, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventDetailEventsEventIdGet");
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
| **eventId** | **String**|  | |
| **include** | [**List&lt;EventInclude&gt;**](EventInclude.md)| Additional includes for the Event response. | [optional] |
| **apikey** | **String**|  | [optional] |
| **xApiKey** | **String**|  | [optional] |

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
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="eventListEventsGet"></a>
# **eventListEventsGet**
> EventList eventListEventsGet(jurisdiction, deleted, before, after, requireBills, include, apikey, page, perPage, xApiKey)

Event List

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
    String jurisdiction = "jurisdiction_example"; // String | Filter by jurisdiction name or ID.
    Boolean deleted = false; // Boolean | Return events marked as deleted?
    String before = "before_example"; // String | Limit results to those starting before a given datetime.
    String after = "after_example"; // String | Limit results to those starting before a given datetime.
    Boolean requireBills = false; // Boolean | Limit results to events with associated bills.
    List<EventInclude> include = Arrays.asList(); // List<EventInclude> | Additional includes for the Event response.
    String apikey = "apikey_example"; // String | 
    Integer page = 1; // Integer | 
    Integer perPage = 20; // Integer | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      EventList result = apiInstance.eventListEventsGet(jurisdiction, deleted, before, after, requireBills, include, apikey, page, perPage, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventListEventsGet");
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
| **jurisdiction** | **String**| Filter by jurisdiction name or ID. | [optional] |
| **deleted** | **Boolean**| Return events marked as deleted? | [optional] [default to false] |
| **before** | **String**| Limit results to those starting before a given datetime. | [optional] |
| **after** | **String**| Limit results to those starting before a given datetime. | [optional] |
| **requireBills** | **Boolean**| Limit results to events with associated bills. | [optional] [default to false] |
| **include** | [**List&lt;EventInclude&gt;**](EventInclude.md)| Additional includes for the Event response. | [optional] |
| **apikey** | **String**|  | [optional] |
| **page** | **Integer**|  | [optional] [default to 1] |
| **perPage** | **Integer**|  | [optional] [default to 20] |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**EventList**](EventList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

