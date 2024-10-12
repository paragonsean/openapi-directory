# CalendarEventResponseApi

All URIs are relative to *https://api.twinehealth.com/pub*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCalendarEventResponse**](CalendarEventResponseApi.md#createCalendarEventResponse) | **POST** /calendar_event_response | Create calendar event response |


<a id="createCalendarEventResponse"></a>
# **createCalendarEventResponse**
> CreateCalendarEventResponseRequest createCalendarEventResponse(createCalendarEventResponseRequest)

Create calendar event response

Create a calendar event response for an attendee of a calendar event, the attendee can be a coach or patient.  Calendar event responses cannot be fetched, updated nor deleted.  Use calendar event api to fetch the response status for attendees.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarEventResponseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    CalendarEventResponseApi apiInstance = new CalendarEventResponseApi(defaultClient);
    CreateCalendarEventResponseRequest createCalendarEventResponseRequest = new CreateCalendarEventResponseRequest(); // CreateCalendarEventResponseRequest | 
    try {
      CreateCalendarEventResponseRequest result = apiInstance.createCalendarEventResponse(createCalendarEventResponseRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarEventResponseApi#createCalendarEventResponse");
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
| **createCalendarEventResponseRequest** | [**CreateCalendarEventResponseRequest**](CreateCalendarEventResponseRequest.md)|  | |

### Return type

[**CreateCalendarEventResponseRequest**](CreateCalendarEventResponseRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **409** | Invalid Request |  -  |

