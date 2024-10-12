# WebinarsApi

All URIs are relative to *https://api.getgo.com/G2W/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelWebinar**](WebinarsApi.md#cancelWebinar) | **DELETE** /organizers/{organizerKey}/webinars/{webinarKey} | Cancel webinar |
| [**createWebinar**](WebinarsApi.md#createWebinar) | **POST** /organizers/{organizerKey}/webinars | Create webinar |
| [**getAllAccountWebinars**](WebinarsApi.md#getAllAccountWebinars) | **GET** /accounts/{accountKey}/webinars | Get all webinars for an account |
| [**getAllWebinars**](WebinarsApi.md#getAllWebinars) | **GET** /organizers/{organizerKey}/webinars | Get all webinars |
| [**getAttendeesForAllWebinarSessions**](WebinarsApi.md#getAttendeesForAllWebinarSessions) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/attendees | Get attendees for all webinar sessions |
| [**getAudioInformation**](WebinarsApi.md#getAudioInformation) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/audio | Get audio information |
| [**getHistoricalWebinars**](WebinarsApi.md#getHistoricalWebinars) | **GET** /organizers/{organizerKey}/historicalWebinars | Get historical webinars |
| [**getPerformanceForAllWebinarSessions**](WebinarsApi.md#getPerformanceForAllWebinarSessions) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/performance | Get performance for all webinar sessions |
| [**getUpcomingWebinars**](WebinarsApi.md#getUpcomingWebinars) | **GET** /organizers/{organizerKey}/upcomingWebinars | Get upcoming webinars |
| [**getWebinar**](WebinarsApi.md#getWebinar) | **GET** /organizers/{organizerKey}/webinars/{webinarKey} | Get webinar |
| [**getWebinarMeetingTimes**](WebinarsApi.md#getWebinarMeetingTimes) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/meetingtimes | Get webinar meeting times |
| [**updateAudioInformation**](WebinarsApi.md#updateAudioInformation) | **POST** /organizers/{organizerKey}/webinars/{webinarKey}/audio | Update audio information |
| [**updateWebinar**](WebinarsApi.md#updateWebinar) | **PUT** /organizers/{organizerKey}/webinars/{webinarKey} | Update webinar |


<a id="cancelWebinar"></a>
# **cancelWebinar**
> cancelWebinar(authorization, organizerKey, webinarKey, sendCancellationEmails)

Cancel webinar

Cancels a specific webinar. If the webinar is a series or sequence, this call deletes all scheduled sessions. To send cancellation emails to registrants set sendCancellationEmails&#x3D;true in the request. When the cancellation emails are sent, the default generated message is used in the cancellation email body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebinarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    WebinarsApi apiInstance = new WebinarsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    Boolean sendCancellationEmails = true; // Boolean | Indicates whether cancellation notice emails should be sent. The default value is false
    try {
      apiInstance.cancelWebinar(authorization, organizerKey, webinarKey, sendCancellationEmails);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebinarsApi#cancelWebinar");
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
| **organizerKey** | **Long**| The key of the organizer | |
| **webinarKey** | **Long**| The key of the webinar | |
| **sendCancellationEmails** | **Boolean**| Indicates whether cancellation notice emails should be sent. The default value is false | [optional] |

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
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **405** | Method Not Allowed (Webinar is in the past) |  -  |
| **409** | Conflict (Webinar is in session) |  -  |

<a id="createWebinar"></a>
# **createWebinar**
> CreatedWebinar createWebinar(authorization, organizerKey, body)

Create webinar

Creates a single session webinar, a sequence of webinars or a series of webinars depending on the type field in the body: \&quot;single_session\&quot; creates a single webinar session, \&quot;sequence\&quot; creates a webinar with multiple meeting times where attendees are expected to be the same for all sessions, and \&quot;series\&quot; creates a webinar with multiple meetings times where attendees choose only one to attend. The default, if no type is declared, is single_session. A sequence webinar requires a \&quot;recurrenceStart\&quot; object consisting of a \&quot;startTime\&quot; and \&quot;endTime\&quot; key for the first webinar of the sequence, a \&quot;recurrencePattern\&quot; of \&quot;daily\&quot;, \&quot;weekly\&quot;, \&quot;monthly\&quot;, and a \&quot;recurrenceEnd\&quot; which is the last date of the sequence (for example, 2016-12-01). A series webinar requires a \&quot;times\&quot; array with a discrete \&quot;startTime\&quot; and \&quot;endTime\&quot; for each webinar in the series. The call requires a webinar subject and description. The \&quot;isPasswordProtected\&quot; sets whether the webinar requires a password for attendees to join. If set to True, the organizer must go to Registration Settings at My Webinars (https://global.gotowebinar.com/webinars.tmpl) and add the password to the webinar, and send the password to the registrants. The response provides a numeric webinarKey in string format for the new webinar. Once a webinar has been created with this method, you can accept registrations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebinarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    WebinarsApi apiInstance = new WebinarsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    WebinarReqCreate body = new WebinarReqCreate(); // WebinarReqCreate | The webinar details
    try {
      CreatedWebinar result = apiInstance.createWebinar(authorization, organizerKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebinarsApi#createWebinar");
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
| **organizerKey** | **Long**| The key of the organizer | |
| **body** | [**WebinarReqCreate**](WebinarReqCreate.md)| The webinar details | |

### Return type

[**CreatedWebinar**](CreatedWebinar.md)

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
| **403** | Forbidden |  -  |

<a id="getAllAccountWebinars"></a>
# **getAllAccountWebinars**
> AccountWebinarsResponse getAllAccountWebinars(authorization, accountKey, fromTime, toTime, page, size)

Get all webinars for an account

Retrieves the list of webinars for an account within a given date range. __*Page*__ and __*size*__ parameters are optional. Default __*page*__ is 0 and default __*size*__ is 20. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebinarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    WebinarsApi apiInstance = new WebinarsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long accountKey = 56L; // Long | The key of the account
    OffsetDateTime fromTime = OffsetDateTime.now(); // OffsetDateTime | A required start of datetime range in ISO8601 UTC format, e.g. 2015-07-13T10:00:00Z
    OffsetDateTime toTime = OffsetDateTime.now(); // OffsetDateTime | A required end of datetime range in ISO8601 UTC format, e.g. 2015-07-13T22:00:00Z
    Long page = 56L; // Long | The page number to be displayed. The first page is 0.
    Long size = 56L; // Long | The size of the page.
    try {
      AccountWebinarsResponse result = apiInstance.getAllAccountWebinars(authorization, accountKey, fromTime, toTime, page, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebinarsApi#getAllAccountWebinars");
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
| **accountKey** | **Long**| The key of the account | |
| **fromTime** | **OffsetDateTime**| A required start of datetime range in ISO8601 UTC format, e.g. 2015-07-13T10:00:00Z | |
| **toTime** | **OffsetDateTime**| A required end of datetime range in ISO8601 UTC format, e.g. 2015-07-13T22:00:00Z | |
| **page** | **Long**| The page number to be displayed. The first page is 0. | [optional] |
| **size** | **Long**| The size of the page. | [optional] |

### Return type

[**AccountWebinarsResponse**](AccountWebinarsResponse.md)

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
| **404** | Not found |  -  |

<a id="getAllWebinars"></a>
# **getAllWebinars**
> List&lt;Webinar&gt; getAllWebinars(authorization, organizerKey)

Get all webinars

Returns webinars scheduled for the future for a specified organizer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebinarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    WebinarsApi apiInstance = new WebinarsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    try {
      List<Webinar> result = apiInstance.getAllWebinars(authorization, organizerKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebinarsApi#getAllWebinars");
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
| **organizerKey** | **Long**| The key of the organizer | |

### Return type

[**List&lt;Webinar&gt;**](Webinar.md)

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

<a id="getAttendeesForAllWebinarSessions"></a>
# **getAttendeesForAllWebinarSessions**
> List&lt;Attendee&gt; getAttendeesForAllWebinarSessions(authorization, organizerKey, webinarKey)

Get attendees for all webinar sessions

Returns all attendees for all sessions of the specified webinar.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebinarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    WebinarsApi apiInstance = new WebinarsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    try {
      List<Attendee> result = apiInstance.getAttendeesForAllWebinarSessions(authorization, organizerKey, webinarKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebinarsApi#getAttendeesForAllWebinarSessions");
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
| **organizerKey** | **Long**| The key of the organizer | |
| **webinarKey** | **Long**| The key of the webinar | |

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
| **404** | Not found |  -  |

<a id="getAudioInformation"></a>
# **getAudioInformation**
> Audio getAudioInformation(authorization, organizerKey, webinarKey)

Get audio information

Retrieves the audio/conferencing information for a specific webinar.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebinarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    WebinarsApi apiInstance = new WebinarsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    try {
      Audio result = apiInstance.getAudioInformation(authorization, organizerKey, webinarKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebinarsApi#getAudioInformation");
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
| **organizerKey** | **Long**| The key of the organizer | |
| **webinarKey** | **Long**| The key of the webinar | |

### Return type

[**Audio**](Audio.md)

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
| **404** | Not found |  -  |

<a id="getHistoricalWebinars"></a>
# **getHistoricalWebinars**
> List&lt;HistoricalWebinar&gt; getHistoricalWebinars(authorization, organizerKey, fromTime, toTime)

Get historical webinars

Returns details for completed webinars for the specified organizer and completed webinars of other organizers where the specified organizer is a co-organizer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebinarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    WebinarsApi apiInstance = new WebinarsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    OffsetDateTime fromTime = OffsetDateTime.now(); // OffsetDateTime | A required start of datetime range in ISO8601 UTC format, e.g. 2015-07-13T10:00:00Z
    OffsetDateTime toTime = OffsetDateTime.now(); // OffsetDateTime | A required end of datetime range in ISO8601 UTC format, e.g. 2015-07-13T22:00:00Z
    try {
      List<HistoricalWebinar> result = apiInstance.getHistoricalWebinars(authorization, organizerKey, fromTime, toTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebinarsApi#getHistoricalWebinars");
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
| **organizerKey** | **Long**| The key of the organizer | |
| **fromTime** | **OffsetDateTime**| A required start of datetime range in ISO8601 UTC format, e.g. 2015-07-13T10:00:00Z | |
| **toTime** | **OffsetDateTime**| A required end of datetime range in ISO8601 UTC format, e.g. 2015-07-13T22:00:00Z | |

### Return type

[**List&lt;HistoricalWebinar&gt;**](HistoricalWebinar.md)

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

<a id="getPerformanceForAllWebinarSessions"></a>
# **getPerformanceForAllWebinarSessions**
> Map&lt;String, SessionPerformance&gt; getPerformanceForAllWebinarSessions(authorization, organizerKey, webinarKey)

Get performance for all webinar sessions

Gets performance details for all sessions of a specific webinar.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebinarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    WebinarsApi apiInstance = new WebinarsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    try {
      Map<String, SessionPerformance> result = apiInstance.getPerformanceForAllWebinarSessions(authorization, organizerKey, webinarKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebinarsApi#getPerformanceForAllWebinarSessions");
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
| **organizerKey** | **Long**| The key of the organizer | |
| **webinarKey** | **Long**| The key of the webinar | |

### Return type

[**Map&lt;String, SessionPerformance&gt;**](SessionPerformance.md)

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
| **404** | Not found |  -  |

<a id="getUpcomingWebinars"></a>
# **getUpcomingWebinars**
> List&lt;UpcomingWebinar&gt; getUpcomingWebinars(authorization, organizerKey)

Get upcoming webinars

Returns webinars scheduled for the future for the specified organizer and webinars of other organizers where the specified organizer is a co-organizer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebinarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    WebinarsApi apiInstance = new WebinarsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    try {
      List<UpcomingWebinar> result = apiInstance.getUpcomingWebinars(authorization, organizerKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebinarsApi#getUpcomingWebinars");
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
| **organizerKey** | **Long**| The key of the organizer | |

### Return type

[**List&lt;UpcomingWebinar&gt;**](UpcomingWebinar.md)

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

<a id="getWebinar"></a>
# **getWebinar**
> WebinarByKey getWebinar(authorization, organizerKey, webinarKey)

Get webinar

Retrieve information on a specific webinar. If the type of the webinar is &#39;sequence&#39;, a sequence of future times will be provided. Webinars of type &#39;series&#39; are treated the same as normal webinars - each session in the webinar series has a different webinarKey. If an organizer cancels a webinar, then a request to get that webinar would return a &#39;404 Not Found&#39; error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebinarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    WebinarsApi apiInstance = new WebinarsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    try {
      WebinarByKey result = apiInstance.getWebinar(authorization, organizerKey, webinarKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebinarsApi#getWebinar");
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
| **organizerKey** | **Long**| The key of the organizer | |
| **webinarKey** | **Long**| The key of the webinar | |

### Return type

[**WebinarByKey**](WebinarByKey.md)

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
| **404** | Not found |  -  |

<a id="getWebinarMeetingTimes"></a>
# **getWebinarMeetingTimes**
> List&lt;DateTimeRange&gt; getWebinarMeetingTimes(authorization, organizerKey, webinarKey)

Get webinar meeting times

Retrieves the meeting times for a webinar.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebinarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    WebinarsApi apiInstance = new WebinarsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    try {
      List<DateTimeRange> result = apiInstance.getWebinarMeetingTimes(authorization, organizerKey, webinarKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebinarsApi#getWebinarMeetingTimes");
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
| **organizerKey** | **Long**| The key of the organizer | |
| **webinarKey** | **Long**| The key of the webinar | |

### Return type

[**List&lt;DateTimeRange&gt;**](DateTimeRange.md)

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
| **404** | Not found |  -  |

<a id="updateAudioInformation"></a>
# **updateAudioInformation**
> updateAudioInformation(authorization, organizerKey, webinarKey, body, notifyParticipants)

Update audio information

Updates the audio/conferencing settings for a specific webinar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebinarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    WebinarsApi apiInstance = new WebinarsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    AudioUpdate body = new AudioUpdate(); // AudioUpdate | The audio/conferencing settings
    Boolean notifyParticipants = true; // Boolean | Defines whether to send notifications to participants
    try {
      apiInstance.updateAudioInformation(authorization, organizerKey, webinarKey, body, notifyParticipants);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebinarsApi#updateAudioInformation");
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
| **organizerKey** | **Long**| The key of the organizer | |
| **webinarKey** | **Long**| The key of the webinar | |
| **body** | [**AudioUpdate**](AudioUpdate.md)| The audio/conferencing settings | |
| **notifyParticipants** | **Boolean**| Defines whether to send notifications to participants | [optional] |

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
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |

<a id="updateWebinar"></a>
# **updateWebinar**
> updateWebinar(authorization, organizerKey, webinarKey, body, notifyParticipants)

Update webinar

Updates a webinar. The call requires at least one of the parameters in the request body. The request completely replaces the existing session, series, or sequence and so must include the full definition of each as for the Create call. Set notifyParticipants&#x3D;true to send update emails to registrants.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebinarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    WebinarsApi apiInstance = new WebinarsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    WebinarReqUpdate body = new WebinarReqUpdate(); // WebinarReqUpdate | The webinar details
    Boolean notifyParticipants = true; // Boolean | Defines whether to send notifications to participants
    try {
      apiInstance.updateWebinar(authorization, organizerKey, webinarKey, body, notifyParticipants);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebinarsApi#updateWebinar");
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
| **organizerKey** | **Long**| The key of the organizer | |
| **webinarKey** | **Long**| The key of the webinar | |
| **body** | [**WebinarReqUpdate**](WebinarReqUpdate.md)| The webinar details | |
| **notifyParticipants** | **Boolean**| Defines whether to send notifications to participants | [optional] |

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
| **202** | Accepted |  -  |
| **400** | Bad Request (times not valid, webinar in progress, webinar ended, etc.) |  -  |
| **403** | Forbidden |  -  |

