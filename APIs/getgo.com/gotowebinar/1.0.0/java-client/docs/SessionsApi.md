# SessionsApi

All URIs are relative to *https://api.getgo.com/G2W/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllSessions**](SessionsApi.md#getAllSessions) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/sessions | Get webinar sessions |
| [**getOrganizerSessions**](SessionsApi.md#getOrganizerSessions) | **GET** /organizers/{organizerKey}/sessions | Get organizer sessions |
| [**getPerformance**](SessionsApi.md#getPerformance) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/sessions/{sessionKey}/performance | Get session performance |
| [**getPolls**](SessionsApi.md#getPolls) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/sessions/{sessionKey}/polls | Get session polls |
| [**getQuestions**](SessionsApi.md#getQuestions) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/sessions/{sessionKey}/questions | Get session questions |
| [**getSurveys**](SessionsApi.md#getSurveys) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/sessions/{sessionKey}/surveys | Get session surveys |
| [**getWebinarSession**](SessionsApi.md#getWebinarSession) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/sessions/{sessionKey} | Get webinar session |


<a id="getAllSessions"></a>
# **getAllSessions**
> List&lt;Session&gt; getAllSessions(authorization, organizerKey, webinarKey)

Get webinar sessions

Retrieves details for all past sessions of a specific webinar.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    try {
      List<Session> result = apiInstance.getAllSessions(authorization, organizerKey, webinarKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#getAllSessions");
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

<a id="getOrganizerSessions"></a>
# **getOrganizerSessions**
> List&lt;Session&gt; getOrganizerSessions(authorization, organizerKey, fromTime, toTime)

Get organizer sessions

Retrieve all completed sessions of all the webinars of a given organizer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    OffsetDateTime fromTime = OffsetDateTime.now(); // OffsetDateTime | A required start of datetime range in ISO8601 UTC format, e.g. 2015-07-13T10:00:00Z
    OffsetDateTime toTime = OffsetDateTime.now(); // OffsetDateTime | A required end of datetime range in ISO8601 UTC format, e.g. 2015-07-13T22:00:00Z
    try {
      List<Session> result = apiInstance.getOrganizerSessions(authorization, organizerKey, fromTime, toTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#getOrganizerSessions");
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

<a id="getPerformance"></a>
# **getPerformance**
> SessionPerformance getPerformance(authorization, organizerKey, webinarKey, sessionKey)

Get session performance

Get performance details for a session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    Long sessionKey = 56L; // Long | The key of the webinar session
    try {
      SessionPerformance result = apiInstance.getPerformance(authorization, organizerKey, webinarKey, sessionKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#getPerformance");
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
| **sessionKey** | **Long**| The key of the webinar session | |

### Return type

[**SessionPerformance**](SessionPerformance.md)

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

<a id="getPolls"></a>
# **getPolls**
> List&lt;Poll&gt; getPolls(authorization, organizerKey, webinarKey, sessionKey)

Get session polls

Retrieve all collated attendee questions and answers for polls from a specific webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    Long sessionKey = 56L; // Long | The key of the webinar session
    try {
      List<Poll> result = apiInstance.getPolls(authorization, organizerKey, webinarKey, sessionKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#getPolls");
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
| **sessionKey** | **Long**| The key of the webinar session | |

### Return type

[**List&lt;Poll&gt;**](Poll.md)

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

<a id="getQuestions"></a>
# **getQuestions**
> List&lt;AttendeeQuestion&gt; getQuestions(authorization, organizerKey, webinarKey, sessionKey)

Get session questions

Retrieve questions and answers for a past webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    Long sessionKey = 56L; // Long | The key of the webinar session
    try {
      List<AttendeeQuestion> result = apiInstance.getQuestions(authorization, organizerKey, webinarKey, sessionKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#getQuestions");
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
| **sessionKey** | **Long**| The key of the webinar session | |

### Return type

[**List&lt;AttendeeQuestion&gt;**](AttendeeQuestion.md)

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

<a id="getSurveys"></a>
# **getSurveys**
> List&lt;Poll&gt; getSurveys(authorization, organizerKey, webinarKey, sessionKey)

Get session surveys

Retrieve surveys for a past webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    Long sessionKey = 56L; // Long | The key of the webinar session
    try {
      List<Poll> result = apiInstance.getSurveys(authorization, organizerKey, webinarKey, sessionKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#getSurveys");
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
| **sessionKey** | **Long**| The key of the webinar session | |

### Return type

[**List&lt;Poll&gt;**](Poll.md)

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

<a id="getWebinarSession"></a>
# **getWebinarSession**
> List&lt;Attendee&gt; getWebinarSession(authorization, organizerKey, webinarKey, sessionKey)

Get webinar session

Retrieves attendance details for a specific webinar session that has ended. If attendees attended the session (&#39;registrantsAttended&#39;), specific attendance details, such as attendenceTime for a registrant, will also be retrieved. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    Long sessionKey = 56L; // Long | The key of the webinar session
    try {
      List<Attendee> result = apiInstance.getWebinarSession(authorization, organizerKey, webinarKey, sessionKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#getWebinarSession");
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
| **sessionKey** | **Long**| The key of the webinar session | |

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

