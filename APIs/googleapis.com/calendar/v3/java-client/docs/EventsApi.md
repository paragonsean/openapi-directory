# EventsApi

All URIs are relative to *https://www.googleapis.com/calendar/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**calendarEventsDelete**](EventsApi.md#calendarEventsDelete) | **DELETE** /calendars/{calendarId}/events/{eventId} |  |
| [**calendarEventsGet**](EventsApi.md#calendarEventsGet) | **GET** /calendars/{calendarId}/events/{eventId} |  |
| [**calendarEventsImport**](EventsApi.md#calendarEventsImport) | **POST** /calendars/{calendarId}/events/import |  |
| [**calendarEventsInsert**](EventsApi.md#calendarEventsInsert) | **POST** /calendars/{calendarId}/events |  |
| [**calendarEventsInstances**](EventsApi.md#calendarEventsInstances) | **GET** /calendars/{calendarId}/events/{eventId}/instances |  |
| [**calendarEventsList**](EventsApi.md#calendarEventsList) | **GET** /calendars/{calendarId}/events |  |
| [**calendarEventsMove**](EventsApi.md#calendarEventsMove) | **POST** /calendars/{calendarId}/events/{eventId}/move |  |
| [**calendarEventsPatch**](EventsApi.md#calendarEventsPatch) | **PATCH** /calendars/{calendarId}/events/{eventId} |  |
| [**calendarEventsQuickAdd**](EventsApi.md#calendarEventsQuickAdd) | **POST** /calendars/{calendarId}/events/quickAdd |  |
| [**calendarEventsUpdate**](EventsApi.md#calendarEventsUpdate) | **PUT** /calendars/{calendarId}/events/{eventId} |  |
| [**calendarEventsWatch**](EventsApi.md#calendarEventsWatch) | **POST** /calendars/{calendarId}/events/watch |  |


<a id="calendarEventsDelete"></a>
# **calendarEventsDelete**
> calendarEventsDelete(calendarId, eventId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, sendNotifications, sendUpdates)



Deletes an event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/calendar/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String calendarId = "calendarId_example"; // String | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \"primary\" keyword.
    String eventId = "eventId_example"; // String | Event identifier.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean sendNotifications = true; // Boolean | Deprecated. Please use sendUpdates instead.  Whether to send notifications about the deletion of the event. Note that some emails might still be sent even if you set the value to false. The default is false.
    String sendUpdates = "all"; // String | Guests who should receive notifications about the deletion of the event.
    try {
      apiInstance.calendarEventsDelete(calendarId, eventId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, sendNotifications, sendUpdates);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#calendarEventsDelete");
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
| **calendarId** | **String**| Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword. | |
| **eventId** | **String**| Event identifier. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **sendNotifications** | **Boolean**| Deprecated. Please use sendUpdates instead.  Whether to send notifications about the deletion of the event. Note that some emails might still be sent even if you set the value to false. The default is false. | [optional] |
| **sendUpdates** | **String**| Guests who should receive notifications about the deletion of the event. | [optional] [enum: all, externalOnly, none] |

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="calendarEventsGet"></a>
# **calendarEventsGet**
> Event calendarEventsGet(calendarId, eventId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, alwaysIncludeEmail, maxAttendees, timeZone)



Returns an event based on its Google Calendar ID. To retrieve an event using its iCalendar ID, call the events.list method using the iCalUID parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/calendar/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String calendarId = "calendarId_example"; // String | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \"primary\" keyword.
    String eventId = "eventId_example"; // String | Event identifier.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean alwaysIncludeEmail = true; // Boolean | Deprecated and ignored. A value will always be returned in the email field for the organizer, creator and attendees, even if no real email address is available (i.e. a generated, non-working value will be provided).
    Integer maxAttendees = 56; // Integer | The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.
    String timeZone = "timeZone_example"; // String | Time zone used in the response. Optional. The default is the time zone of the calendar.
    try {
      Event result = apiInstance.calendarEventsGet(calendarId, eventId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, alwaysIncludeEmail, maxAttendees, timeZone);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#calendarEventsGet");
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
| **calendarId** | **String**| Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword. | |
| **eventId** | **String**| Event identifier. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **alwaysIncludeEmail** | **Boolean**| Deprecated and ignored. A value will always be returned in the email field for the organizer, creator and attendees, even if no real email address is available (i.e. a generated, non-working value will be provided). | [optional] |
| **maxAttendees** | **Integer**| The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional. | [optional] |
| **timeZone** | **String**| Time zone used in the response. Optional. The default is the time zone of the calendar. | [optional] |

### Return type

[**Event**](Event.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="calendarEventsImport"></a>
# **calendarEventsImport**
> Event calendarEventsImport(calendarId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, conferenceDataVersion, supportsAttachments, event)



Imports an event. This operation is used to add a private copy of an existing event to a calendar.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/calendar/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String calendarId = "calendarId_example"; // String | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \"primary\" keyword.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Integer conferenceDataVersion = 56; // Integer | Version number of conference data supported by the API client. Version 0 assumes no conference data support and ignores conference data in the event's body. Version 1 enables support for copying of ConferenceData as well as for creating new conferences using the createRequest field of conferenceData. The default is 0.
    Boolean supportsAttachments = true; // Boolean | Whether API client performing operation supports event attachments. Optional. The default is False.
    Event event = new Event(); // Event | 
    try {
      Event result = apiInstance.calendarEventsImport(calendarId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, conferenceDataVersion, supportsAttachments, event);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#calendarEventsImport");
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
| **calendarId** | **String**| Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **conferenceDataVersion** | **Integer**| Version number of conference data supported by the API client. Version 0 assumes no conference data support and ignores conference data in the event&#39;s body. Version 1 enables support for copying of ConferenceData as well as for creating new conferences using the createRequest field of conferenceData. The default is 0. | [optional] |
| **supportsAttachments** | **Boolean**| Whether API client performing operation supports event attachments. Optional. The default is False. | [optional] |
| **event** | [**Event**](Event.md)|  | [optional] |

### Return type

[**Event**](Event.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="calendarEventsInsert"></a>
# **calendarEventsInsert**
> Event calendarEventsInsert(calendarId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, conferenceDataVersion, maxAttendees, sendNotifications, sendUpdates, supportsAttachments, event)



Creates an event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/calendar/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String calendarId = "calendarId_example"; // String | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \"primary\" keyword.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Integer conferenceDataVersion = 56; // Integer | Version number of conference data supported by the API client. Version 0 assumes no conference data support and ignores conference data in the event's body. Version 1 enables support for copying of ConferenceData as well as for creating new conferences using the createRequest field of conferenceData. The default is 0.
    Integer maxAttendees = 56; // Integer | The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.
    Boolean sendNotifications = true; // Boolean | Deprecated. Please use sendUpdates instead.  Whether to send notifications about the creation of the new event. Note that some emails might still be sent even if you set the value to false. The default is false.
    String sendUpdates = "all"; // String | Whether to send notifications about the creation of the new event. Note that some emails might still be sent. The default is false.
    Boolean supportsAttachments = true; // Boolean | Whether API client performing operation supports event attachments. Optional. The default is False.
    Event event = new Event(); // Event | 
    try {
      Event result = apiInstance.calendarEventsInsert(calendarId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, conferenceDataVersion, maxAttendees, sendNotifications, sendUpdates, supportsAttachments, event);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#calendarEventsInsert");
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
| **calendarId** | **String**| Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **conferenceDataVersion** | **Integer**| Version number of conference data supported by the API client. Version 0 assumes no conference data support and ignores conference data in the event&#39;s body. Version 1 enables support for copying of ConferenceData as well as for creating new conferences using the createRequest field of conferenceData. The default is 0. | [optional] |
| **maxAttendees** | **Integer**| The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional. | [optional] |
| **sendNotifications** | **Boolean**| Deprecated. Please use sendUpdates instead.  Whether to send notifications about the creation of the new event. Note that some emails might still be sent even if you set the value to false. The default is false. | [optional] |
| **sendUpdates** | **String**| Whether to send notifications about the creation of the new event. Note that some emails might still be sent. The default is false. | [optional] [enum: all, externalOnly, none] |
| **supportsAttachments** | **Boolean**| Whether API client performing operation supports event attachments. Optional. The default is False. | [optional] |
| **event** | [**Event**](Event.md)|  | [optional] |

### Return type

[**Event**](Event.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="calendarEventsInstances"></a>
# **calendarEventsInstances**
> Events calendarEventsInstances(calendarId, eventId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, alwaysIncludeEmail, maxAttendees, maxResults, originalStart, pageToken, showDeleted, timeMax, timeMin, timeZone)



Returns instances of the specified recurring event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/calendar/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String calendarId = "calendarId_example"; // String | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \"primary\" keyword.
    String eventId = "eventId_example"; // String | Recurring event identifier.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean alwaysIncludeEmail = true; // Boolean | Deprecated and ignored. A value will always be returned in the email field for the organizer, creator and attendees, even if no real email address is available (i.e. a generated, non-working value will be provided).
    Integer maxAttendees = 56; // Integer | The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.
    Integer maxResults = 56; // Integer | Maximum number of events returned on one result page. By default the value is 250 events. The page size can never be larger than 2500 events. Optional.
    String originalStart = "originalStart_example"; // String | The original start time of the instance in the result. Optional.
    String pageToken = "pageToken_example"; // String | Token specifying which result page to return. Optional.
    Boolean showDeleted = true; // Boolean | Whether to include deleted events (with status equals \"cancelled\") in the result. Cancelled instances of recurring events will still be included if singleEvents is False. Optional. The default is False.
    String timeMax = "timeMax_example"; // String | Upper bound (exclusive) for an event's start time to filter by. Optional. The default is not to filter by start time. Must be an RFC3339 timestamp with mandatory time zone offset.
    String timeMin = "timeMin_example"; // String | Lower bound (inclusive) for an event's end time to filter by. Optional. The default is not to filter by end time. Must be an RFC3339 timestamp with mandatory time zone offset.
    String timeZone = "timeZone_example"; // String | Time zone used in the response. Optional. The default is the time zone of the calendar.
    try {
      Events result = apiInstance.calendarEventsInstances(calendarId, eventId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, alwaysIncludeEmail, maxAttendees, maxResults, originalStart, pageToken, showDeleted, timeMax, timeMin, timeZone);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#calendarEventsInstances");
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
| **calendarId** | **String**| Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword. | |
| **eventId** | **String**| Recurring event identifier. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **alwaysIncludeEmail** | **Boolean**| Deprecated and ignored. A value will always be returned in the email field for the organizer, creator and attendees, even if no real email address is available (i.e. a generated, non-working value will be provided). | [optional] |
| **maxAttendees** | **Integer**| The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional. | [optional] |
| **maxResults** | **Integer**| Maximum number of events returned on one result page. By default the value is 250 events. The page size can never be larger than 2500 events. Optional. | [optional] |
| **originalStart** | **String**| The original start time of the instance in the result. Optional. | [optional] |
| **pageToken** | **String**| Token specifying which result page to return. Optional. | [optional] |
| **showDeleted** | **Boolean**| Whether to include deleted events (with status equals \&quot;cancelled\&quot;) in the result. Cancelled instances of recurring events will still be included if singleEvents is False. Optional. The default is False. | [optional] |
| **timeMax** | **String**| Upper bound (exclusive) for an event&#39;s start time to filter by. Optional. The default is not to filter by start time. Must be an RFC3339 timestamp with mandatory time zone offset. | [optional] |
| **timeMin** | **String**| Lower bound (inclusive) for an event&#39;s end time to filter by. Optional. The default is not to filter by end time. Must be an RFC3339 timestamp with mandatory time zone offset. | [optional] |
| **timeZone** | **String**| Time zone used in the response. Optional. The default is the time zone of the calendar. | [optional] |

### Return type

[**Events**](Events.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="calendarEventsList"></a>
# **calendarEventsList**
> Events calendarEventsList(calendarId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, alwaysIncludeEmail, eventTypes, iCalUID, maxAttendees, maxResults, orderBy, pageToken, privateExtendedProperty, q, sharedExtendedProperty, showDeleted, showHiddenInvitations, singleEvents, syncToken, timeMax, timeMin, timeZone, updatedMin)



Returns events on the specified calendar.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/calendar/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String calendarId = "calendarId_example"; // String | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \"primary\" keyword.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean alwaysIncludeEmail = true; // Boolean | Deprecated and ignored.
    List<String> eventTypes = Arrays.asList(); // List<String> | Event types to return. Optional. This parameter can be repeated multiple times to return events of different types. The default is [\"default\", \"focusTime\", \"outOfOffice\"].
    String iCalUID = "iCalUID_example"; // String | Specifies an event ID in the iCalendar format to be provided in the response. Optional. Use this if you want to search for an event by its iCalendar ID.
    Integer maxAttendees = 56; // Integer | The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.
    Integer maxResults = 56; // Integer | Maximum number of events returned on one result page. The number of events in the resulting page may be less than this value, or none at all, even if there are more events matching the query. Incomplete pages can be detected by a non-empty nextPageToken field in the response. By default the value is 250 events. The page size can never be larger than 2500 events. Optional.
    String orderBy = "startTime"; // String | The order of the events returned in the result. Optional. The default is an unspecified, stable order.
    String pageToken = "pageToken_example"; // String | Token specifying which result page to return. Optional.
    List<String> privateExtendedProperty = Arrays.asList(); // List<String> | Extended properties constraint specified as propertyName=value. Matches only private properties. This parameter might be repeated multiple times to return events that match all given constraints.
    String q = "q_example"; // String | Free text search terms to find events that match these terms in the following fields:  - summary  - description  - location  - attendee's displayName  - attendee's email  - organizer's displayName  - organizer's email  - workingLocationProperties.officeLocation.buildingId  - workingLocationProperties.officeLocation.deskId  - workingLocationProperties.officeLocation.label  - workingLocationProperties.customLocation.label  These search terms also match predefined keywords against all display title translations of working location, out-of-office, and focus-time events. For example, searching for \"Office\" or \"Bureau\" returns working location events of type officeLocation, whereas searching for \"Out of office\" or \"Abwesend\" returns out-of-office events. Optional.
    List<String> sharedExtendedProperty = Arrays.asList(); // List<String> | Extended properties constraint specified as propertyName=value. Matches only shared properties. This parameter might be repeated multiple times to return events that match all given constraints.
    Boolean showDeleted = true; // Boolean | Whether to include deleted events (with status equals \"cancelled\") in the result. Cancelled instances of recurring events (but not the underlying recurring event) will still be included if showDeleted and singleEvents are both False. If showDeleted and singleEvents are both True, only single instances of deleted events (but not the underlying recurring events) are returned. Optional. The default is False.
    Boolean showHiddenInvitations = true; // Boolean | Whether to include hidden invitations in the result. Optional. The default is False.
    Boolean singleEvents = true; // Boolean | Whether to expand recurring events into instances and only return single one-off events and instances of recurring events, but not the underlying recurring events themselves. Optional. The default is False.
    String syncToken = "syncToken_example"; // String | Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. All events deleted since the previous list request will always be in the result set and it is not allowed to set showDeleted to False. There are several query parameters that cannot be specified together with nextSyncToken to ensure consistency of the client state.  These are:  - iCalUID  - orderBy  - privateExtendedProperty  - q  - sharedExtendedProperty  - timeMin  - timeMax  - updatedMin All other query parameters should be the same as for the initial synchronization to avoid undefined behavior. If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken. Learn more about incremental synchronization. Optional. The default is to return all entries.
    String timeMax = "timeMax_example"; // String | Upper bound (exclusive) for an event's start time to filter by. Optional. The default is not to filter by start time. Must be an RFC3339 timestamp with mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but are ignored. If timeMin is set, timeMax must be greater than timeMin.
    String timeMin = "timeMin_example"; // String | Lower bound (exclusive) for an event's end time to filter by. Optional. The default is not to filter by end time. Must be an RFC3339 timestamp with mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but are ignored. If timeMax is set, timeMin must be smaller than timeMax.
    String timeZone = "timeZone_example"; // String | Time zone used in the response. Optional. The default is the time zone of the calendar.
    String updatedMin = "updatedMin_example"; // String | Lower bound for an event's last modification time (as a RFC3339 timestamp) to filter by. When specified, entries deleted since this time will always be included regardless of showDeleted. Optional. The default is not to filter by last modification time.
    try {
      Events result = apiInstance.calendarEventsList(calendarId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, alwaysIncludeEmail, eventTypes, iCalUID, maxAttendees, maxResults, orderBy, pageToken, privateExtendedProperty, q, sharedExtendedProperty, showDeleted, showHiddenInvitations, singleEvents, syncToken, timeMax, timeMin, timeZone, updatedMin);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#calendarEventsList");
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
| **calendarId** | **String**| Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **alwaysIncludeEmail** | **Boolean**| Deprecated and ignored. | [optional] |
| **eventTypes** | [**List&lt;String&gt;**](String.md)| Event types to return. Optional. This parameter can be repeated multiple times to return events of different types. The default is [\&quot;default\&quot;, \&quot;focusTime\&quot;, \&quot;outOfOffice\&quot;]. | [optional] [enum: default, focusTime, outOfOffice, workingLocation] |
| **iCalUID** | **String**| Specifies an event ID in the iCalendar format to be provided in the response. Optional. Use this if you want to search for an event by its iCalendar ID. | [optional] |
| **maxAttendees** | **Integer**| The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional. | [optional] |
| **maxResults** | **Integer**| Maximum number of events returned on one result page. The number of events in the resulting page may be less than this value, or none at all, even if there are more events matching the query. Incomplete pages can be detected by a non-empty nextPageToken field in the response. By default the value is 250 events. The page size can never be larger than 2500 events. Optional. | [optional] |
| **orderBy** | **String**| The order of the events returned in the result. Optional. The default is an unspecified, stable order. | [optional] [enum: startTime, updated] |
| **pageToken** | **String**| Token specifying which result page to return. Optional. | [optional] |
| **privateExtendedProperty** | [**List&lt;String&gt;**](String.md)| Extended properties constraint specified as propertyName&#x3D;value. Matches only private properties. This parameter might be repeated multiple times to return events that match all given constraints. | [optional] |
| **q** | **String**| Free text search terms to find events that match these terms in the following fields:  - summary  - description  - location  - attendee&#39;s displayName  - attendee&#39;s email  - organizer&#39;s displayName  - organizer&#39;s email  - workingLocationProperties.officeLocation.buildingId  - workingLocationProperties.officeLocation.deskId  - workingLocationProperties.officeLocation.label  - workingLocationProperties.customLocation.label  These search terms also match predefined keywords against all display title translations of working location, out-of-office, and focus-time events. For example, searching for \&quot;Office\&quot; or \&quot;Bureau\&quot; returns working location events of type officeLocation, whereas searching for \&quot;Out of office\&quot; or \&quot;Abwesend\&quot; returns out-of-office events. Optional. | [optional] |
| **sharedExtendedProperty** | [**List&lt;String&gt;**](String.md)| Extended properties constraint specified as propertyName&#x3D;value. Matches only shared properties. This parameter might be repeated multiple times to return events that match all given constraints. | [optional] |
| **showDeleted** | **Boolean**| Whether to include deleted events (with status equals \&quot;cancelled\&quot;) in the result. Cancelled instances of recurring events (but not the underlying recurring event) will still be included if showDeleted and singleEvents are both False. If showDeleted and singleEvents are both True, only single instances of deleted events (but not the underlying recurring events) are returned. Optional. The default is False. | [optional] |
| **showHiddenInvitations** | **Boolean**| Whether to include hidden invitations in the result. Optional. The default is False. | [optional] |
| **singleEvents** | **Boolean**| Whether to expand recurring events into instances and only return single one-off events and instances of recurring events, but not the underlying recurring events themselves. Optional. The default is False. | [optional] |
| **syncToken** | **String**| Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. All events deleted since the previous list request will always be in the result set and it is not allowed to set showDeleted to False. There are several query parameters that cannot be specified together with nextSyncToken to ensure consistency of the client state.  These are:  - iCalUID  - orderBy  - privateExtendedProperty  - q  - sharedExtendedProperty  - timeMin  - timeMax  - updatedMin All other query parameters should be the same as for the initial synchronization to avoid undefined behavior. If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken. Learn more about incremental synchronization. Optional. The default is to return all entries. | [optional] |
| **timeMax** | **String**| Upper bound (exclusive) for an event&#39;s start time to filter by. Optional. The default is not to filter by start time. Must be an RFC3339 timestamp with mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but are ignored. If timeMin is set, timeMax must be greater than timeMin. | [optional] |
| **timeMin** | **String**| Lower bound (exclusive) for an event&#39;s end time to filter by. Optional. The default is not to filter by end time. Must be an RFC3339 timestamp with mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but are ignored. If timeMax is set, timeMin must be smaller than timeMax. | [optional] |
| **timeZone** | **String**| Time zone used in the response. Optional. The default is the time zone of the calendar. | [optional] |
| **updatedMin** | **String**| Lower bound for an event&#39;s last modification time (as a RFC3339 timestamp) to filter by. When specified, entries deleted since this time will always be included regardless of showDeleted. Optional. The default is not to filter by last modification time. | [optional] |

### Return type

[**Events**](Events.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="calendarEventsMove"></a>
# **calendarEventsMove**
> Event calendarEventsMove(calendarId, eventId, destination, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, sendNotifications, sendUpdates)



Moves an event to another calendar, i.e. changes an event&#39;s organizer. Note that only default events can be moved; outOfOffice, focusTime and workingLocation events cannot be moved.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/calendar/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String calendarId = "calendarId_example"; // String | Calendar identifier of the source calendar where the event currently is on.
    String eventId = "eventId_example"; // String | Event identifier.
    String destination = "destination_example"; // String | Calendar identifier of the target calendar where the event is to be moved to.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean sendNotifications = true; // Boolean | Deprecated. Please use sendUpdates instead.  Whether to send notifications about the change of the event's organizer. Note that some emails might still be sent even if you set the value to false. The default is false.
    String sendUpdates = "all"; // String | Guests who should receive notifications about the change of the event's organizer.
    try {
      Event result = apiInstance.calendarEventsMove(calendarId, eventId, destination, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, sendNotifications, sendUpdates);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#calendarEventsMove");
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
| **calendarId** | **String**| Calendar identifier of the source calendar where the event currently is on. | |
| **eventId** | **String**| Event identifier. | |
| **destination** | **String**| Calendar identifier of the target calendar where the event is to be moved to. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **sendNotifications** | **Boolean**| Deprecated. Please use sendUpdates instead.  Whether to send notifications about the change of the event&#39;s organizer. Note that some emails might still be sent even if you set the value to false. The default is false. | [optional] |
| **sendUpdates** | **String**| Guests who should receive notifications about the change of the event&#39;s organizer. | [optional] [enum: all, externalOnly, none] |

### Return type

[**Event**](Event.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="calendarEventsPatch"></a>
# **calendarEventsPatch**
> Event calendarEventsPatch(calendarId, eventId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, alwaysIncludeEmail, conferenceDataVersion, maxAttendees, sendNotifications, sendUpdates, supportsAttachments, event)



Updates an event. This method supports patch semantics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/calendar/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String calendarId = "calendarId_example"; // String | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \"primary\" keyword.
    String eventId = "eventId_example"; // String | Event identifier.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean alwaysIncludeEmail = true; // Boolean | Deprecated and ignored. A value will always be returned in the email field for the organizer, creator and attendees, even if no real email address is available (i.e. a generated, non-working value will be provided).
    Integer conferenceDataVersion = 56; // Integer | Version number of conference data supported by the API client. Version 0 assumes no conference data support and ignores conference data in the event's body. Version 1 enables support for copying of ConferenceData as well as for creating new conferences using the createRequest field of conferenceData. The default is 0.
    Integer maxAttendees = 56; // Integer | The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.
    Boolean sendNotifications = true; // Boolean | Deprecated. Please use sendUpdates instead.  Whether to send notifications about the event update (for example, description changes, etc.). Note that some emails might still be sent even if you set the value to false. The default is false.
    String sendUpdates = "all"; // String | Guests who should receive notifications about the event update (for example, title changes, etc.).
    Boolean supportsAttachments = true; // Boolean | Whether API client performing operation supports event attachments. Optional. The default is False.
    Event event = new Event(); // Event | 
    try {
      Event result = apiInstance.calendarEventsPatch(calendarId, eventId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, alwaysIncludeEmail, conferenceDataVersion, maxAttendees, sendNotifications, sendUpdates, supportsAttachments, event);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#calendarEventsPatch");
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
| **calendarId** | **String**| Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword. | |
| **eventId** | **String**| Event identifier. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **alwaysIncludeEmail** | **Boolean**| Deprecated and ignored. A value will always be returned in the email field for the organizer, creator and attendees, even if no real email address is available (i.e. a generated, non-working value will be provided). | [optional] |
| **conferenceDataVersion** | **Integer**| Version number of conference data supported by the API client. Version 0 assumes no conference data support and ignores conference data in the event&#39;s body. Version 1 enables support for copying of ConferenceData as well as for creating new conferences using the createRequest field of conferenceData. The default is 0. | [optional] |
| **maxAttendees** | **Integer**| The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional. | [optional] |
| **sendNotifications** | **Boolean**| Deprecated. Please use sendUpdates instead.  Whether to send notifications about the event update (for example, description changes, etc.). Note that some emails might still be sent even if you set the value to false. The default is false. | [optional] |
| **sendUpdates** | **String**| Guests who should receive notifications about the event update (for example, title changes, etc.). | [optional] [enum: all, externalOnly, none] |
| **supportsAttachments** | **Boolean**| Whether API client performing operation supports event attachments. Optional. The default is False. | [optional] |
| **event** | [**Event**](Event.md)|  | [optional] |

### Return type

[**Event**](Event.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="calendarEventsQuickAdd"></a>
# **calendarEventsQuickAdd**
> Event calendarEventsQuickAdd(calendarId, text, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, sendNotifications, sendUpdates)



Creates an event based on a simple text string.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/calendar/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String calendarId = "calendarId_example"; // String | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \"primary\" keyword.
    String text = "text_example"; // String | The text describing the event to be created.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean sendNotifications = true; // Boolean | Deprecated. Please use sendUpdates instead.  Whether to send notifications about the creation of the event. Note that some emails might still be sent even if you set the value to false. The default is false.
    String sendUpdates = "all"; // String | Guests who should receive notifications about the creation of the new event.
    try {
      Event result = apiInstance.calendarEventsQuickAdd(calendarId, text, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, sendNotifications, sendUpdates);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#calendarEventsQuickAdd");
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
| **calendarId** | **String**| Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword. | |
| **text** | **String**| The text describing the event to be created. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **sendNotifications** | **Boolean**| Deprecated. Please use sendUpdates instead.  Whether to send notifications about the creation of the event. Note that some emails might still be sent even if you set the value to false. The default is false. | [optional] |
| **sendUpdates** | **String**| Guests who should receive notifications about the creation of the new event. | [optional] [enum: all, externalOnly, none] |

### Return type

[**Event**](Event.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="calendarEventsUpdate"></a>
# **calendarEventsUpdate**
> Event calendarEventsUpdate(calendarId, eventId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, alwaysIncludeEmail, conferenceDataVersion, maxAttendees, sendNotifications, sendUpdates, supportsAttachments, event)



Updates an event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/calendar/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String calendarId = "calendarId_example"; // String | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \"primary\" keyword.
    String eventId = "eventId_example"; // String | Event identifier.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean alwaysIncludeEmail = true; // Boolean | Deprecated and ignored. A value will always be returned in the email field for the organizer, creator and attendees, even if no real email address is available (i.e. a generated, non-working value will be provided).
    Integer conferenceDataVersion = 56; // Integer | Version number of conference data supported by the API client. Version 0 assumes no conference data support and ignores conference data in the event's body. Version 1 enables support for copying of ConferenceData as well as for creating new conferences using the createRequest field of conferenceData. The default is 0.
    Integer maxAttendees = 56; // Integer | The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.
    Boolean sendNotifications = true; // Boolean | Deprecated. Please use sendUpdates instead.  Whether to send notifications about the event update (for example, description changes, etc.). Note that some emails might still be sent even if you set the value to false. The default is false.
    String sendUpdates = "all"; // String | Guests who should receive notifications about the event update (for example, title changes, etc.).
    Boolean supportsAttachments = true; // Boolean | Whether API client performing operation supports event attachments. Optional. The default is False.
    Event event = new Event(); // Event | 
    try {
      Event result = apiInstance.calendarEventsUpdate(calendarId, eventId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, alwaysIncludeEmail, conferenceDataVersion, maxAttendees, sendNotifications, sendUpdates, supportsAttachments, event);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#calendarEventsUpdate");
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
| **calendarId** | **String**| Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword. | |
| **eventId** | **String**| Event identifier. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **alwaysIncludeEmail** | **Boolean**| Deprecated and ignored. A value will always be returned in the email field for the organizer, creator and attendees, even if no real email address is available (i.e. a generated, non-working value will be provided). | [optional] |
| **conferenceDataVersion** | **Integer**| Version number of conference data supported by the API client. Version 0 assumes no conference data support and ignores conference data in the event&#39;s body. Version 1 enables support for copying of ConferenceData as well as for creating new conferences using the createRequest field of conferenceData. The default is 0. | [optional] |
| **maxAttendees** | **Integer**| The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional. | [optional] |
| **sendNotifications** | **Boolean**| Deprecated. Please use sendUpdates instead.  Whether to send notifications about the event update (for example, description changes, etc.). Note that some emails might still be sent even if you set the value to false. The default is false. | [optional] |
| **sendUpdates** | **String**| Guests who should receive notifications about the event update (for example, title changes, etc.). | [optional] [enum: all, externalOnly, none] |
| **supportsAttachments** | **Boolean**| Whether API client performing operation supports event attachments. Optional. The default is False. | [optional] |
| **event** | [**Event**](Event.md)|  | [optional] |

### Return type

[**Event**](Event.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="calendarEventsWatch"></a>
# **calendarEventsWatch**
> Channel calendarEventsWatch(calendarId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, alwaysIncludeEmail, eventTypes, iCalUID, maxAttendees, maxResults, orderBy, pageToken, privateExtendedProperty, q, sharedExtendedProperty, showDeleted, showHiddenInvitations, singleEvents, syncToken, timeMax, timeMin, timeZone, updatedMin, channel)



Watch for changes to Events resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/calendar/v3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String calendarId = "calendarId_example"; // String | Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \"primary\" keyword.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean alwaysIncludeEmail = true; // Boolean | Deprecated and ignored.
    List<String> eventTypes = Arrays.asList(); // List<String> | Event types to return. Optional. This parameter can be repeated multiple times to return events of different types. The default is [\"default\", \"focusTime\", \"outOfOffice\"].
    String iCalUID = "iCalUID_example"; // String | Specifies an event ID in the iCalendar format to be provided in the response. Optional. Use this if you want to search for an event by its iCalendar ID.
    Integer maxAttendees = 56; // Integer | The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.
    Integer maxResults = 56; // Integer | Maximum number of events returned on one result page. The number of events in the resulting page may be less than this value, or none at all, even if there are more events matching the query. Incomplete pages can be detected by a non-empty nextPageToken field in the response. By default the value is 250 events. The page size can never be larger than 2500 events. Optional.
    String orderBy = "startTime"; // String | The order of the events returned in the result. Optional. The default is an unspecified, stable order.
    String pageToken = "pageToken_example"; // String | Token specifying which result page to return. Optional.
    List<String> privateExtendedProperty = Arrays.asList(); // List<String> | Extended properties constraint specified as propertyName=value. Matches only private properties. This parameter might be repeated multiple times to return events that match all given constraints.
    String q = "q_example"; // String | Free text search terms to find events that match these terms in the following fields:  - summary  - description  - location  - attendee's displayName  - attendee's email  - organizer's displayName  - organizer's email  - workingLocationProperties.officeLocation.buildingId  - workingLocationProperties.officeLocation.deskId  - workingLocationProperties.officeLocation.label  - workingLocationProperties.customLocation.label  These search terms also match predefined keywords against all display title translations of working location, out-of-office, and focus-time events. For example, searching for \"Office\" or \"Bureau\" returns working location events of type officeLocation, whereas searching for \"Out of office\" or \"Abwesend\" returns out-of-office events. Optional.
    List<String> sharedExtendedProperty = Arrays.asList(); // List<String> | Extended properties constraint specified as propertyName=value. Matches only shared properties. This parameter might be repeated multiple times to return events that match all given constraints.
    Boolean showDeleted = true; // Boolean | Whether to include deleted events (with status equals \"cancelled\") in the result. Cancelled instances of recurring events (but not the underlying recurring event) will still be included if showDeleted and singleEvents are both False. If showDeleted and singleEvents are both True, only single instances of deleted events (but not the underlying recurring events) are returned. Optional. The default is False.
    Boolean showHiddenInvitations = true; // Boolean | Whether to include hidden invitations in the result. Optional. The default is False.
    Boolean singleEvents = true; // Boolean | Whether to expand recurring events into instances and only return single one-off events and instances of recurring events, but not the underlying recurring events themselves. Optional. The default is False.
    String syncToken = "syncToken_example"; // String | Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. All events deleted since the previous list request will always be in the result set and it is not allowed to set showDeleted to False. There are several query parameters that cannot be specified together with nextSyncToken to ensure consistency of the client state.  These are:  - iCalUID  - orderBy  - privateExtendedProperty  - q  - sharedExtendedProperty  - timeMin  - timeMax  - updatedMin All other query parameters should be the same as for the initial synchronization to avoid undefined behavior. If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken. Learn more about incremental synchronization. Optional. The default is to return all entries.
    String timeMax = "timeMax_example"; // String | Upper bound (exclusive) for an event's start time to filter by. Optional. The default is not to filter by start time. Must be an RFC3339 timestamp with mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but are ignored. If timeMin is set, timeMax must be greater than timeMin.
    String timeMin = "timeMin_example"; // String | Lower bound (exclusive) for an event's end time to filter by. Optional. The default is not to filter by end time. Must be an RFC3339 timestamp with mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but are ignored. If timeMax is set, timeMin must be smaller than timeMax.
    String timeZone = "timeZone_example"; // String | Time zone used in the response. Optional. The default is the time zone of the calendar.
    String updatedMin = "updatedMin_example"; // String | Lower bound for an event's last modification time (as a RFC3339 timestamp) to filter by. When specified, entries deleted since this time will always be included regardless of showDeleted. Optional. The default is not to filter by last modification time.
    Channel channel = new Channel(); // Channel | 
    try {
      Channel result = apiInstance.calendarEventsWatch(calendarId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, alwaysIncludeEmail, eventTypes, iCalUID, maxAttendees, maxResults, orderBy, pageToken, privateExtendedProperty, q, sharedExtendedProperty, showDeleted, showHiddenInvitations, singleEvents, syncToken, timeMax, timeMin, timeZone, updatedMin, channel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#calendarEventsWatch");
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
| **calendarId** | **String**| Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **alwaysIncludeEmail** | **Boolean**| Deprecated and ignored. | [optional] |
| **eventTypes** | [**List&lt;String&gt;**](String.md)| Event types to return. Optional. This parameter can be repeated multiple times to return events of different types. The default is [\&quot;default\&quot;, \&quot;focusTime\&quot;, \&quot;outOfOffice\&quot;]. | [optional] [enum: default, focusTime, outOfOffice, workingLocation] |
| **iCalUID** | **String**| Specifies an event ID in the iCalendar format to be provided in the response. Optional. Use this if you want to search for an event by its iCalendar ID. | [optional] |
| **maxAttendees** | **Integer**| The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional. | [optional] |
| **maxResults** | **Integer**| Maximum number of events returned on one result page. The number of events in the resulting page may be less than this value, or none at all, even if there are more events matching the query. Incomplete pages can be detected by a non-empty nextPageToken field in the response. By default the value is 250 events. The page size can never be larger than 2500 events. Optional. | [optional] |
| **orderBy** | **String**| The order of the events returned in the result. Optional. The default is an unspecified, stable order. | [optional] [enum: startTime, updated] |
| **pageToken** | **String**| Token specifying which result page to return. Optional. | [optional] |
| **privateExtendedProperty** | [**List&lt;String&gt;**](String.md)| Extended properties constraint specified as propertyName&#x3D;value. Matches only private properties. This parameter might be repeated multiple times to return events that match all given constraints. | [optional] |
| **q** | **String**| Free text search terms to find events that match these terms in the following fields:  - summary  - description  - location  - attendee&#39;s displayName  - attendee&#39;s email  - organizer&#39;s displayName  - organizer&#39;s email  - workingLocationProperties.officeLocation.buildingId  - workingLocationProperties.officeLocation.deskId  - workingLocationProperties.officeLocation.label  - workingLocationProperties.customLocation.label  These search terms also match predefined keywords against all display title translations of working location, out-of-office, and focus-time events. For example, searching for \&quot;Office\&quot; or \&quot;Bureau\&quot; returns working location events of type officeLocation, whereas searching for \&quot;Out of office\&quot; or \&quot;Abwesend\&quot; returns out-of-office events. Optional. | [optional] |
| **sharedExtendedProperty** | [**List&lt;String&gt;**](String.md)| Extended properties constraint specified as propertyName&#x3D;value. Matches only shared properties. This parameter might be repeated multiple times to return events that match all given constraints. | [optional] |
| **showDeleted** | **Boolean**| Whether to include deleted events (with status equals \&quot;cancelled\&quot;) in the result. Cancelled instances of recurring events (but not the underlying recurring event) will still be included if showDeleted and singleEvents are both False. If showDeleted and singleEvents are both True, only single instances of deleted events (but not the underlying recurring events) are returned. Optional. The default is False. | [optional] |
| **showHiddenInvitations** | **Boolean**| Whether to include hidden invitations in the result. Optional. The default is False. | [optional] |
| **singleEvents** | **Boolean**| Whether to expand recurring events into instances and only return single one-off events and instances of recurring events, but not the underlying recurring events themselves. Optional. The default is False. | [optional] |
| **syncToken** | **String**| Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. All events deleted since the previous list request will always be in the result set and it is not allowed to set showDeleted to False. There are several query parameters that cannot be specified together with nextSyncToken to ensure consistency of the client state.  These are:  - iCalUID  - orderBy  - privateExtendedProperty  - q  - sharedExtendedProperty  - timeMin  - timeMax  - updatedMin All other query parameters should be the same as for the initial synchronization to avoid undefined behavior. If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken. Learn more about incremental synchronization. Optional. The default is to return all entries. | [optional] |
| **timeMax** | **String**| Upper bound (exclusive) for an event&#39;s start time to filter by. Optional. The default is not to filter by start time. Must be an RFC3339 timestamp with mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but are ignored. If timeMin is set, timeMax must be greater than timeMin. | [optional] |
| **timeMin** | **String**| Lower bound (exclusive) for an event&#39;s end time to filter by. Optional. The default is not to filter by end time. Must be an RFC3339 timestamp with mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but are ignored. If timeMax is set, timeMin must be smaller than timeMax. | [optional] |
| **timeZone** | **String**| Time zone used in the response. Optional. The default is the time zone of the calendar. | [optional] |
| **updatedMin** | **String**| Lower bound for an event&#39;s last modification time (as a RFC3339 timestamp) to filter by. When specified, entries deleted since this time will always be included regardless of showDeleted. Optional. The default is not to filter by last modification time. | [optional] |
| **channel** | [**Channel**](Channel.md)|  | [optional] |

### Return type

[**Channel**](Channel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

