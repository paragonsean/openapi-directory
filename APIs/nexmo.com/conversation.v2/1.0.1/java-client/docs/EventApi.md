# EventApi

All URIs are relative to *https://api.nexmo.com/v0.2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEvents**](EventApi.md#getEvents) | **GET** /conversations/{conversation_id}/events | List Events |


<a id="getEvents"></a>
# **getEvents**
> GetEvents200Response getEvents(conversationId, pageSize, order, cursor, startId, endId, eventType)

List Events

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v0.2");

    EventApi apiInstance = new EventApi(defaultClient);
    String conversationId = "CON-afe887d8-d587-4280-9aae-dfa4c9227d5e"; // String | The ID of the conversation
    Integer pageSize = 10; // Integer | The number of results returned per page.   The default value is `10`. The maximum value is `100`.
    String order = "asc"; // String | Show the most (`desc`) / least (`asc`) recently created entries first
    String cursor = "cursor_example"; // String | The cursor to start returning results from.  You are not expected to provide this manually, but to follow the url provided in `_links.next.href` in the response which contains a `cursor` value 
    String startId = "13"; // String | The ID to start returning events at
    String endId = "19"; // String | The ID to end returning events at
    String eventType = "text"; // String | The type of event to search for. Does not currently support custom events
    try {
      GetEvents200Response result = apiInstance.getEvents(conversationId, pageSize, order, cursor, startId, endId, eventType);
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
| **conversationId** | **String**| The ID of the conversation | |
| **pageSize** | **Integer**| The number of results returned per page.   The default value is &#x60;10&#x60;. The maximum value is &#x60;100&#x60;. | [optional] [default to 10] |
| **order** | **String**| Show the most (&#x60;desc&#x60;) / least (&#x60;asc&#x60;) recently created entries first | [optional] [default to asc] [enum: asc, desc] |
| **cursor** | **String**| The cursor to start returning results from.  You are not expected to provide this manually, but to follow the url provided in &#x60;_links.next.href&#x60; in the response which contains a &#x60;cursor&#x60; value  | [optional] |
| **startId** | **String**| The ID to start returning events at | [optional] |
| **endId** | **String**| The ID to end returning events at | [optional] |
| **eventType** | **String**| The type of event to search for. Does not currently support custom events | [optional] |

### Return type

[**GetEvents200Response**](GetEvents200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

