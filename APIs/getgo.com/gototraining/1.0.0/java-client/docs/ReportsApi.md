# ReportsApi

All URIs are relative to *https://api.getgo.com/G2T/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAttendanceDetails**](ReportsApi.md#getAttendanceDetails) | **GET** /reports/organizers/{organizerKey}/sessions/{sessionKey}/attendees | Get Attendance Details |
| [**getSessionDetailsForDateRange**](ReportsApi.md#getSessionDetailsForDateRange) | **POST** /reports/organizers/{organizerKey}/sessions | Get Sessions by Date Range |
| [**getSessionDetailsForTraining**](ReportsApi.md#getSessionDetailsForTraining) | **GET** /reports/organizers/{organizerKey}/trainings/{trainingKey} | Get Sessions By Training |


<a id="getAttendanceDetails"></a>
# **getAttendanceDetails**
> List&lt;Attendee&gt; getAttendanceDetails(authorization, organizerKey, sessionKey)

Get Attendance Details

This call retrieves a list of registrants from a specific completed training session. The response includes the registrants&#39; email addresses, and if they attended, it includes the duration of each period of their attendance in minutes, and the times at which they joined and left. If a registrant does not attend, they appear at the bottom of the listing with timeInSession &#x3D; 0.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2T/rest");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the training organizer
    Long sessionKey = 56L; // Long | The key of the training session
    try {
      List<Attendee> result = apiInstance.getAttendanceDetails(authorization, organizerKey, sessionKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getAttendanceDetails");
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
| **authorization** | **String**| Access token | |
| **organizerKey** | **Long**| The key of the training organizer | |
| **sessionKey** | **Long**| The key of the training session | |

### Return type

[**List&lt;Attendee&gt;**](Attendee.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getSessionDetailsForDateRange"></a>
# **getSessionDetailsForDateRange**
> List&lt;Session&gt; getSessionDetailsForDateRange(authorization, organizerKey, body)

Get Sessions by Date Range

This call returns all session details over a given date range for a given organizer. A session is a completed training event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2T/rest");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the training organizer
    DateTimeRange body = new DateTimeRange(); // DateTimeRange | The start and end times for the time range over which to retrieve training sessions
    try {
      List<Session> result = apiInstance.getSessionDetailsForDateRange(authorization, organizerKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getSessionDetailsForDateRange");
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
| **authorization** | **String**| Access token | |
| **organizerKey** | **Long**| The key of the training organizer | |
| **body** | [**DateTimeRange**](DateTimeRange.md)| The start and end times for the time range over which to retrieve training sessions | |

### Return type

[**List&lt;Session&gt;**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |

<a id="getSessionDetailsForTraining"></a>
# **getSessionDetailsForTraining**
> List&lt;Session&gt; getSessionDetailsForTraining(authorization, organizerKey, trainingKey)

Get Sessions By Training

This call returns session details for a given training. A session is a completed training event. Each training may contain one or more sessions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2T/rest");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the training organizer
    Long trainingKey = 56L; // Long | The key of the training
    try {
      List<Session> result = apiInstance.getSessionDetailsForTraining(authorization, organizerKey, trainingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getSessionDetailsForTraining");
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
| **authorization** | **String**| Access token | |
| **organizerKey** | **Long**| The key of the training organizer | |
| **trainingKey** | **Long**| The key of the training | |

### Return type

[**List&lt;Session&gt;**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

