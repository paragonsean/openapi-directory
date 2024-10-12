# EventsApi

All URIs are relative to *https://api.journy.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEvents**](EventsApi.md#getEvents) | **GET** /events | Get events |
| [**trackJourneyEvent**](EventsApi.md#trackJourneyEvent) | **POST** /events | Track event |


<a id="getEvents"></a>
# **getEvents**
> GetEvents200Response getEvents()

Get events

Endpoint to list events.

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
    defaultClient.setBasePath("https://api.journy.io");

    EventsApi apiInstance = new EventsApi(defaultClient);
    try {
      GetEvents200Response result = apiInstance.getEvents();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#getEvents");
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

[**GetEvents200Response**](GetEvents200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Events |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **400** | Bad request, some fields or parameters are incorrect |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **401** | No API Key was provided or the key is not authorised to perform the action |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **403** | The API Key provided is currently not enabled |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **429** | Too many API requests were send |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **500** | An unexpected error occurred |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |

<a id="trackJourneyEvent"></a>
# **trackJourneyEvent**
> DeleteAccount202Response trackJourneyEvent(trackJourneyEventRequest)

Track event

Endpoint used to track an event for a user or an account.  This endpoint is moved to [Track](#operation/trackEvent).

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
    defaultClient.setBasePath("https://api.journy.io");

    EventsApi apiInstance = new EventsApi(defaultClient);
    TrackJourneyEventRequest trackJourneyEventRequest = new TrackJourneyEventRequest(); // TrackJourneyEventRequest | 
    try {
      DeleteAccount202Response result = apiInstance.trackJourneyEvent(trackJourneyEventRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#trackJourneyEvent");
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
| **trackJourneyEventRequest** | [**TrackJourneyEventRequest**](TrackJourneyEventRequest.md)|  | |

### Return type

[**DeleteAccount202Response**](DeleteAccount202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Object was created |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **400** | Bad request, some fields or parameters are incorrect |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **401** | No API Key was provided or the key is not authorised to perform the action |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **403** | The API Key provided is currently not enabled |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **429** | Too many API requests were send |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **500** | An unexpected error occurred |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |

