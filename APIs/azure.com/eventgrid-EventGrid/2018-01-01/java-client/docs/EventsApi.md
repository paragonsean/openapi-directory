# EventsApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**publishEvents**](EventsApi.md#publishEvents) | **POST** /api/events |  |


<a id="publishEvents"></a>
# **publishEvents**
> publishEvents(apiVersion, events)



Publishes a batch of events to an Azure Event Grid topic.

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
    defaultClient.setBasePath("https://azure.local");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    List<EventGridEvent> events = Arrays.asList(); // List<EventGridEvent> | An array of events to be published to Event Grid.
    try {
      apiInstance.publishEvents(apiVersion, events);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#publishEvents");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **events** | [**List&lt;EventGridEvent&gt;**](EventGridEvent.md)| An array of events to be published to Event Grid. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 500 Internal Server Error.   * 429 Too Many Events   * 404 Not Found. |  -  |

