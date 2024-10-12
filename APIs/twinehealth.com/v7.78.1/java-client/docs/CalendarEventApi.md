# CalendarEventApi

All URIs are relative to *https://api.twinehealth.com/pub*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCalendarEvent**](CalendarEventApi.md#createCalendarEvent) | **POST** /calendar_event | Create calendar event |
| [**deleteCalendarEvent**](CalendarEventApi.md#deleteCalendarEvent) | **DELETE** /calendar_event/{id} | Delete a calendar event |
| [**fetchCalendarEvent**](CalendarEventApi.md#fetchCalendarEvent) | **GET** /calendar_event/{id} | Get a calendar event |
| [**fetchCalendarEvents**](CalendarEventApi.md#fetchCalendarEvents) | **GET** /calendar_event | List calendar events |
| [**updateCalendarEvent**](CalendarEventApi.md#updateCalendarEvent) | **PATCH** /calendar_event/{id} | Update a calendar event |


<a id="createCalendarEvent"></a>
# **createCalendarEvent**
> CreateCalendarEventResponse createCalendarEvent(createCalendarEventRequest)

Create calendar event

Create a calendar event for a patient. Attribute &#x60;all_day&#x60; must be set to &#x60;true&#x60; and &#x60;end_at&#x60; cannot be set for &#x60;plan-check-in&#x60; event type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarEventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    CalendarEventApi apiInstance = new CalendarEventApi(defaultClient);
    CreateCalendarEventRequest createCalendarEventRequest = new CreateCalendarEventRequest(); // CreateCalendarEventRequest | 
    try {
      CreateCalendarEventResponse result = apiInstance.createCalendarEvent(createCalendarEventRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarEventApi#createCalendarEvent");
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
| **createCalendarEventRequest** | [**CreateCalendarEventRequest**](CreateCalendarEventRequest.md)|  | |

### Return type

[**CreateCalendarEventResponse**](CreateCalendarEventResponse.md)

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

<a id="deleteCalendarEvent"></a>
# **deleteCalendarEvent**
> deleteCalendarEvent(id)

Delete a calendar event

Delete a calendar event by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarEventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    CalendarEventApi apiInstance = new CalendarEventApi(defaultClient);
    String id = "id_example"; // String | Calendar event identifier
    try {
      apiInstance.deleteCalendarEvent(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarEventApi#deleteCalendarEvent");
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
| **id** | **String**| Calendar event identifier | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="fetchCalendarEvent"></a>
# **fetchCalendarEvent**
> FetchCalendarEventResponse fetchCalendarEvent(id)

Get a calendar event

Get a calendar event by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarEventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    CalendarEventApi apiInstance = new CalendarEventApi(defaultClient);
    String id = "id_example"; // String | Calendar event identifier
    try {
      FetchCalendarEventResponse result = apiInstance.fetchCalendarEvent(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarEventApi#fetchCalendarEvent");
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
| **id** | **String**| Calendar event identifier | |

### Return type

[**FetchCalendarEventResponse**](FetchCalendarEventResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="fetchCalendarEvents"></a>
# **fetchCalendarEvents**
> FetchCalendarEventsResponse fetchCalendarEvents(filterPatient, filterGroups, filterOrganization, filterAttendees, filterType, filterCompleted, filterStartAt, filterEndAt, filterCompletedAt, filterCreatedAt, filterUpdatedAt, pageNumber, pageSize, pageLimit, pageCursor, include)

List calendar events

Get a list of calendar events

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarEventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    CalendarEventApi apiInstance = new CalendarEventApi(defaultClient);
    String filterPatient = "filterPatient_example"; // String | Patient id to fetch calendar event. Note that one of the following filters must be specified: `filter[patient]`, `filter[group]`, `filter[organization]`, or `filter[attendees]`. 
    String filterGroups = "filterGroups_example"; // String | Comma-separated list of group ids. Note that one of the following filters must be specified: `filter[patient]`, `filter[group]`, `filter[organization]`, or `filter[attendees]`. 
    String filterOrganization = "filterOrganization_example"; // String | Fitbit Plus organization id. Note that one of the following filters must be specified: `filter[patient]`, `filter[group]`, `filter[organization]`, or `filter[attendees]`. 
    String filterAttendees = "filterAttendees_example"; // String | Comma-separated list of coach or patient ids. Note that one of the following filters must be specified: `filter[patient]`, `filter[group]`, `filter[organization]`, or `filter[attendees]`. 
    String filterType = "plan-check-in"; // String | Calendar event type
    Boolean filterCompleted = true; // Boolean | If not specified, return all calendar events. If set to `true` return only events marked as completed, if set to `false`, return only events not marked as completed yet.
    String filterStartAt = "filterStartAt_example"; // String | The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by `..`. Example for events starting in November 2017 (America/New_York): `filter[start_at]=2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00` 
    String filterEndAt = "filterEndAt_example"; // String | The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by `..`. Example for events ending in November 2017 (America/New_York): `filter[end_at]=2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00` 
    String filterCompletedAt = "filterCompletedAt_example"; // String | The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by `..`. Example for events completed in November 2017 (America/New_York): `filter[completed_at]=2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00` 
    String filterCreatedAt = "filterCreatedAt_example"; // String | The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by `..`. Example for events created in November 2017 (America/New_York): `filter[created_at]=2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00` 
    String filterUpdatedAt = "filterUpdatedAt_example"; // String | The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by `..`. Example for events updated in November 2017 (America/New_York): `filter[updated_at]=2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00` 
    Integer pageNumber = 1; // Integer | Page number
    Integer pageSize = 10; // Integer | Page size
    Integer pageLimit = 50; // Integer | Page limit
    String pageCursor = "pageCursor_example"; // String | Page cursor
    String include = "owner"; // String | List of related resources to include in the response
    try {
      FetchCalendarEventsResponse result = apiInstance.fetchCalendarEvents(filterPatient, filterGroups, filterOrganization, filterAttendees, filterType, filterCompleted, filterStartAt, filterEndAt, filterCompletedAt, filterCreatedAt, filterUpdatedAt, pageNumber, pageSize, pageLimit, pageCursor, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarEventApi#fetchCalendarEvents");
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
| **filterPatient** | **String**| Patient id to fetch calendar event. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, &#x60;filter[organization]&#x60;, or &#x60;filter[attendees]&#x60;.  | [optional] |
| **filterGroups** | **String**| Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, &#x60;filter[organization]&#x60;, or &#x60;filter[attendees]&#x60;.  | [optional] |
| **filterOrganization** | **String**| Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, &#x60;filter[organization]&#x60;, or &#x60;filter[attendees]&#x60;.  | [optional] |
| **filterAttendees** | **String**| Comma-separated list of coach or patient ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, &#x60;filter[organization]&#x60;, or &#x60;filter[attendees]&#x60;.  | [optional] |
| **filterType** | **String**| Calendar event type | [optional] [enum: plan-check-in, reminder, telephone-call, office-visit, video-call] |
| **filterCompleted** | **Boolean**| If not specified, return all calendar events. If set to &#x60;true&#x60; return only events marked as completed, if set to &#x60;false&#x60;, return only events not marked as completed yet. | [optional] |
| **filterStartAt** | **String**| The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for events starting in November 2017 (America/New_York): &#x60;filter[start_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60;  | [optional] |
| **filterEndAt** | **String**| The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for events ending in November 2017 (America/New_York): &#x60;filter[end_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60;  | [optional] |
| **filterCompletedAt** | **String**| The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for events completed in November 2017 (America/New_York): &#x60;filter[completed_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60;  | [optional] |
| **filterCreatedAt** | **String**| The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for events created in November 2017 (America/New_York): &#x60;filter[created_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60;  | [optional] |
| **filterUpdatedAt** | **String**| The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for events updated in November 2017 (America/New_York): &#x60;filter[updated_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60;  | [optional] |
| **pageNumber** | **Integer**| Page number | [optional] [default to 1] |
| **pageSize** | **Integer**| Page size | [optional] [default to 10] |
| **pageLimit** | **Integer**| Page limit | [optional] [default to 50] |
| **pageCursor** | **String**| Page cursor | [optional] |
| **include** | **String**| List of related resources to include in the response | [optional] [enum: owner] |

### Return type

[**FetchCalendarEventsResponse**](FetchCalendarEventsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **409** | Invalid Request |  -  |

<a id="updateCalendarEvent"></a>
# **updateCalendarEvent**
> UpdateCalendarEventResponse updateCalendarEvent(id, updateCalendarEventRequest)

Update a calendar event

Update a calendar event for a patient. Attribute &#x60;all_day&#x60; must be true and &#x60;end_at&#x60; cannot be specified for &#x60;plan-check-in&#x60; event type. To mark a calendar event as &#39;completed&#39;, set &#x60;completed_at&#x60; and &#x60;completed_by&#x60; to desired values.  To mark a completed calendar event as &#39;not completed&#39;, set &#x60;completed_at&#x60; and &#x60;completed_by&#x60; to &#x60;null&#x60;. Attendees can be added or removed, but response status cannot be updated. Use the calendar event response api for response status updates instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarEventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    CalendarEventApi apiInstance = new CalendarEventApi(defaultClient);
    String id = "id_example"; // String | Calendar event identifier
    UpdateCalendarEventRequest updateCalendarEventRequest = new UpdateCalendarEventRequest(); // UpdateCalendarEventRequest | 
    try {
      UpdateCalendarEventResponse result = apiInstance.updateCalendarEvent(id, updateCalendarEventRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarEventApi#updateCalendarEvent");
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
| **id** | **String**| Calendar event identifier | |
| **updateCalendarEventRequest** | [**UpdateCalendarEventRequest**](UpdateCalendarEventRequest.md)|  | |

### Return type

[**UpdateCalendarEventResponse**](UpdateCalendarEventResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **409** | Invalid Request |  -  |

