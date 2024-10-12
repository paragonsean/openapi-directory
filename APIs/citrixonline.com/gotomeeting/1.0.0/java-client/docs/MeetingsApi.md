# MeetingsApi

All URIs are relative to *https://api.citrixonline.com/G2M/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**historicalMeetingsGet**](MeetingsApi.md#historicalMeetingsGet) | **GET** /historicalMeetings | Get historical meetings |
| [**meetingsGet**](MeetingsApi.md#meetingsGet) | **GET** /meetings | DEPRECATED: Get historical meetings |
| [**meetingsMeetingIdAttendeesGet**](MeetingsApi.md#meetingsMeetingIdAttendeesGet) | **GET** /meetings/{meetingId}/attendees | Get attendees by meeting |
| [**meetingsMeetingIdDelete**](MeetingsApi.md#meetingsMeetingIdDelete) | **DELETE** /meetings/{meetingId} | Delete meeting |
| [**meetingsMeetingIdGet**](MeetingsApi.md#meetingsMeetingIdGet) | **GET** /meetings/{meetingId} | Get meeting |
| [**meetingsMeetingIdPut**](MeetingsApi.md#meetingsMeetingIdPut) | **PUT** /meetings/{meetingId} | Update meeting |
| [**meetingsMeetingIdStartGet**](MeetingsApi.md#meetingsMeetingIdStartGet) | **GET** /meetings/{meetingId}/start | Start meeting |
| [**meetingsPost**](MeetingsApi.md#meetingsPost) | **POST** /meetings | Create meeting |
| [**upcomingMeetingsGet**](MeetingsApi.md#upcomingMeetingsGet) | **GET** /upcomingMeetings | Get upcoming meetings |


<a id="historicalMeetingsGet"></a>
# **historicalMeetingsGet**
> List&lt;HistoricalMeeting&gt; historicalMeetingsGet(authorization, startDate, endDate)

Get historical meetings

Get historical meetings for the currently authenticated organizer that started within the specified date/time range. Remark: Meetings which are still ongoing at the time of the request are NOT contained in the result array.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeetingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    MeetingsApi apiInstance = new MeetingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
    try {
      List<HistoricalMeeting> result = apiInstance.historicalMeetingsGet(authorization, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeetingsApi#historicalMeetingsGet");
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
| **startDate** | **OffsetDateTime**| Required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z | |
| **endDate** | **OffsetDateTime**| Required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z | |

### Return type

[**List&lt;HistoricalMeeting&gt;**](HistoricalMeeting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |

<a id="meetingsGet"></a>
# **meetingsGet**
> List&lt;MeetingHistory&gt; meetingsGet(authorization, history, startDate, endDate)

DEPRECATED: Get historical meetings

DEPRECATED: Please use the new API calls &#39;Get historical meetings&#39; and &#39;Get upcoming meetings&#39;.  Gets historical meetings for the current authenticated organizer. Requires date range for filtering results to only meetings within specified dates. History searches will contain the parameter &#39;meetingInstanceKey&#39; which is used in conjunction with the call &#39;Get Attendees by Meeting&#39; to get attendee information for a past meeting.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeetingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    MeetingsApi apiInstance = new MeetingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Boolean history = true; // Boolean | When 'true', returns all past meetings within date range
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | If history=true, required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | If history=true, required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
    try {
      List<MeetingHistory> result = apiInstance.meetingsGet(authorization, history, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeetingsApi#meetingsGet");
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
| **history** | **Boolean**| When &#39;true&#39;, returns all past meetings within date range | [optional] |
| **startDate** | **OffsetDateTime**| If history&#x3D;true, required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z | [optional] |
| **endDate** | **OffsetDateTime**| If history&#x3D;true, required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z | [optional] |

### Return type

[**List&lt;MeetingHistory&gt;**](MeetingHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="meetingsMeetingIdAttendeesGet"></a>
# **meetingsMeetingIdAttendeesGet**
> List&lt;AttendeeByMeeting&gt; meetingsMeetingIdAttendeesGet(authorization, meetingId)

Get attendees by meeting

List all attendees for specified meetingId of historical meeting. The historical meetings can be fetched using &#39;Get historical meetings&#39;, &#39;Get historical meetings by organizer&#39;, and &#39;Get historical meetings by group&#39;. For users with the admin role this call returns attendees for any meeting. For any other user the call will return attendees for meetings on which the user is a valid organizer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeetingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    MeetingsApi apiInstance = new MeetingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long meetingId = 56L; // Long | The meeting ID
    try {
      List<AttendeeByMeeting> result = apiInstance.meetingsMeetingIdAttendeesGet(authorization, meetingId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeetingsApi#meetingsMeetingIdAttendeesGet");
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
| **meetingId** | **Long**| The meeting ID | |

### Return type

[**List&lt;AttendeeByMeeting&gt;**](AttendeeByMeeting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="meetingsMeetingIdDelete"></a>
# **meetingsMeetingIdDelete**
> meetingsMeetingIdDelete(authorization, meetingId)

Delete meeting

Deletes the meeting identified by the meetingId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeetingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    MeetingsApi apiInstance = new MeetingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long meetingId = 56L; // Long | The meeting ID
    try {
      apiInstance.meetingsMeetingIdDelete(authorization, meetingId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeetingsApi#meetingsMeetingIdDelete");
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
| **meetingId** | **Long**| The meeting ID | |

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
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |

<a id="meetingsMeetingIdGet"></a>
# **meetingsMeetingIdGet**
> List&lt;MeetingById&gt; meetingsMeetingIdGet(authorization, meetingId)

Get meeting

Returns the meeting details for the specified meeting.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeetingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    MeetingsApi apiInstance = new MeetingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long meetingId = 56L; // Long | The meeting ID
    try {
      List<MeetingById> result = apiInstance.meetingsMeetingIdGet(authorization, meetingId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeetingsApi#meetingsMeetingIdGet");
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
| **meetingId** | **Long**| The meeting ID | |

### Return type

[**List&lt;MeetingById&gt;**](MeetingById.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="meetingsMeetingIdPut"></a>
# **meetingsMeetingIdPut**
> meetingsMeetingIdPut(authorization, meetingId, body)

Update meeting

Updates an existing meeting specified by meetingId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeetingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    MeetingsApi apiInstance = new MeetingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long meetingId = 56L; // Long | The meeting ID
    MeetingReqUpdate body = new MeetingReqUpdate(); // MeetingReqUpdate | The meeting details
    try {
      apiInstance.meetingsMeetingIdPut(authorization, meetingId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeetingsApi#meetingsMeetingIdPut");
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
| **meetingId** | **Long**| The meeting ID | |
| **body** | [**MeetingReqUpdate**](MeetingReqUpdate.md)| The meeting details | |

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
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |

<a id="meetingsMeetingIdStartGet"></a>
# **meetingsMeetingIdStartGet**
> StartUrl meetingsMeetingIdStartGet(authorization, meetingId)

Start meeting

Returns a host URL that can be used to start a meeting. When this URL is opened in a web browser, the GoToMeeting client will be downloaded and launched and the meeting will start. The end user is not required to login to a client.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeetingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    MeetingsApi apiInstance = new MeetingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long meetingId = 56L; // Long | The meeting ID
    try {
      StartUrl result = apiInstance.meetingsMeetingIdStartGet(authorization, meetingId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeetingsApi#meetingsMeetingIdStartGet");
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
| **meetingId** | **Long**| The meeting ID | |

### Return type

[**StartUrl**](StartUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="meetingsPost"></a>
# **meetingsPost**
> List&lt;MeetingCreated&gt; meetingsPost(authorization, body)

Create meeting

Create a new meeting based on the parameters specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeetingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    MeetingsApi apiInstance = new MeetingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    MeetingReqCreate body = new MeetingReqCreate(); // MeetingReqCreate | The meeting details
    try {
      List<MeetingCreated> result = apiInstance.meetingsPost(authorization, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeetingsApi#meetingsPost");
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
| **body** | [**MeetingReqCreate**](MeetingReqCreate.md)| The meeting details | |

### Return type

[**List&lt;MeetingCreated&gt;**](MeetingCreated.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |

<a id="upcomingMeetingsGet"></a>
# **upcomingMeetingsGet**
> List&lt;UpcomingMeeting&gt; upcomingMeetingsGet(authorization)

Get upcoming meetings

Gets upcoming meetings for the current authenticated organizer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeetingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.citrixonline.com/G2M/rest");

    MeetingsApi apiInstance = new MeetingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    try {
      List<UpcomingMeeting> result = apiInstance.upcomingMeetingsGet(authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeetingsApi#upcomingMeetingsGet");
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

### Return type

[**List&lt;UpcomingMeeting&gt;**](UpcomingMeeting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |

