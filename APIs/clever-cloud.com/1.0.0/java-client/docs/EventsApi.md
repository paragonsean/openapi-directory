# EventsApi

All URIs are relative to *https://api.clever-cloud.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**eventsEventSocketGet_0**](EventsApi.md#eventsEventSocketGet_0) | **GET** /events/event-socket |  |
| [**notificationsInfoEventsGet_0**](EventsApi.md#notificationsInfoEventsGet_0) | **GET** /notifications/info/events |  |


<a id="eventsEventSocketGet_0"></a>
# **eventsEventSocketGet_0**
> eventsEventSocketGet_0()



Retrieve events as they come through a websocket connection. To have authorization, you have to send a &#x60;{ \&quot;message_type\&quot;: \&quot;oauth\&quot;, \&quot;authorization\&quot;: \&quot;oauth authorization string\&quot; }&#x60; message

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
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    EventsApi apiInstance = new EventsApi(defaultClient);
    try {
      apiInstance.eventsEventSocketGet_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventsEventSocketGet_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |

<a id="notificationsInfoEventsGet_0"></a>
# **notificationsInfoEventsGet_0**
> notificationsInfoEventsGet_0()



list available events

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
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    EventsApi apiInstance = new EventsApi(defaultClient);
    try {
      apiInstance.notificationsInfoEventsGet_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#notificationsInfoEventsGet_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |

