# AttendeesApi

All URIs are relative to *https://api.getgo.com/G2W/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAttendee**](AttendeesApi.md#getAttendee) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/sessions/{sessionKey}/attendees/{registrantKey} | Get attendee |
| [**getAttendeePollAnswers**](AttendeesApi.md#getAttendeePollAnswers) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/sessions/{sessionKey}/attendees/{registrantKey}/polls | Get attendee poll answers |
| [**getAttendeeQuestions**](AttendeesApi.md#getAttendeeQuestions) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/sessions/{sessionKey}/attendees/{registrantKey}/questions | Get attendee questions |
| [**getAttendeeSurveyAnswers**](AttendeesApi.md#getAttendeeSurveyAnswers) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/sessions/{sessionKey}/attendees/{registrantKey}/surveys | Get attendee survey answers |
| [**getAttendees**](AttendeesApi.md#getAttendees) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/sessions/{sessionKey}/attendees | Get session attendees |


<a id="getAttendee"></a>
# **getAttendee**
> Registrant getAttendee(authorization, organizerKey, webinarKey, sessionKey, registrantKey)

Get attendee

Retrieve registration details for a particular attendee of a specific webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttendeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    AttendeesApi apiInstance = new AttendeesApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    Long sessionKey = 56L; // Long | The key of the webinar session
    Long registrantKey = 56L; // Long | The key of the registrant
    try {
      Registrant result = apiInstance.getAttendee(authorization, organizerKey, webinarKey, sessionKey, registrantKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttendeesApi#getAttendee");
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
| **registrantKey** | **Long**| The key of the registrant | |

### Return type

[**Registrant**](Registrant.md)

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

<a id="getAttendeePollAnswers"></a>
# **getAttendeePollAnswers**
> List&lt;PollAnswer&gt; getAttendeePollAnswers(authorization, organizerKey, webinarKey, sessionKey, registrantKey)

Get attendee poll answers

Get poll answers from a particular attendee of a specific webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttendeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    AttendeesApi apiInstance = new AttendeesApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    Long sessionKey = 56L; // Long | The key of the webinar session
    Long registrantKey = 56L; // Long | The key of the registrant
    try {
      List<PollAnswer> result = apiInstance.getAttendeePollAnswers(authorization, organizerKey, webinarKey, sessionKey, registrantKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttendeesApi#getAttendeePollAnswers");
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
| **registrantKey** | **Long**| The key of the registrant | |

### Return type

[**List&lt;PollAnswer&gt;**](PollAnswer.md)

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

<a id="getAttendeeQuestions"></a>
# **getAttendeeQuestions**
> List&lt;AttendeeQuestion&gt; getAttendeeQuestions(authorization, organizerKey, webinarKey, sessionKey, registrantKey)

Get attendee questions

Get questions asked by an attendee during a webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttendeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    AttendeesApi apiInstance = new AttendeesApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    Long sessionKey = 56L; // Long | The key of the webinar session
    Long registrantKey = 56L; // Long | The key of the registrant
    try {
      List<AttendeeQuestion> result = apiInstance.getAttendeeQuestions(authorization, organizerKey, webinarKey, sessionKey, registrantKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttendeesApi#getAttendeeQuestions");
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
| **registrantKey** | **Long**| The key of the registrant | |

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
| **404** | Not found |  -  |

<a id="getAttendeeSurveyAnswers"></a>
# **getAttendeeSurveyAnswers**
> List&lt;PollAnswer&gt; getAttendeeSurveyAnswers(authorization, organizerKey, webinarKey, sessionKey, registrantKey)

Get attendee survey answers

Retrieve survey answers from a particular attendee during a webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttendeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    AttendeesApi apiInstance = new AttendeesApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    Long sessionKey = 56L; // Long | The key of the webinar session
    Long registrantKey = 56L; // Long | The key of the registrant
    try {
      List<PollAnswer> result = apiInstance.getAttendeeSurveyAnswers(authorization, organizerKey, webinarKey, sessionKey, registrantKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttendeesApi#getAttendeeSurveyAnswers");
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
| **registrantKey** | **Long**| The key of the registrant | |

### Return type

[**List&lt;PollAnswer&gt;**](PollAnswer.md)

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

<a id="getAttendees"></a>
# **getAttendees**
> List&lt;Attendee&gt; getAttendees(authorization, organizerKey, webinarKey, sessionKey)

Get session attendees

Retrieve details for all attendees of a specific webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttendeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    AttendeesApi apiInstance = new AttendeesApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    Long sessionKey = 56L; // Long | The key of the webinar session
    try {
      List<Attendee> result = apiInstance.getAttendees(authorization, organizerKey, webinarKey, sessionKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttendeesApi#getAttendees");
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
| **404** | Not found |  -  |

