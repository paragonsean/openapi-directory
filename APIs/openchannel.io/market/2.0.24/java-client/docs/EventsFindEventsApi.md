# EventsFindEventsApi

All URIs are relative to *https://market.openchannel.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**eventsEventIdGet**](EventsFindEventsApi.md#eventsEventIdGet) | **GET** /events/{eventId} | Returns an event |


<a id="eventsEventIdGet"></a>
# **eventsEventIdGet**
> Event eventsEventIdGet(eventId)

Returns an event

- Results are returned for the market provided within the basic authentication credentials 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsFindEventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    EventsFindEventsApi apiInstance = new EventsFindEventsApi(defaultClient);
    String eventId = "eventId_example"; // String | The id of the event
    try {
      Event result = apiInstance.eventsEventIdGet(eventId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsFindEventsApi#eventsEventIdGet");
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
| **eventId** | **String**| The id of the event | |

### Return type

[**Event**](Event.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - The event was not found |  -  |
| **0** | OK |  -  |

