# MeetingSettingsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2MeetingsSettingsIdJsonPut**](MeetingSettingsApi.md#v2MeetingsSettingsIdJsonPut) | **PUT** /v2/meetings/settings/{id}.json | Update a meeting setting |


<a id="v2MeetingsSettingsIdJsonPut"></a>
# **v2MeetingsSettingsIdJsonPut**
> MeetingSetting v2MeetingsSettingsIdJsonPut(id, allowBookingOnBehalf, allowBookingOvertime, allowEventOverlap, availabilityLimit, availabilityLimitEnabled, bufferTimeDuration, calendarType, defaultMeetingLength, description, enableCalendarSync, enableDynamicLocation, location, primaryCalendarConnectionFailed, primaryCalendarId, primaryCalendarName, rescheduleMeetingsEnabled, scheduleBufferEnabled, scheduleDelay, shareEventDetail, timeZone, timesAvailable, title)

Update a meeting setting

Updates a meeting setting, by ID only. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeetingSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    MeetingSettingsApi apiInstance = new MeetingSettingsApi(defaultClient);
    String id = "id_example"; // String | MeetingSetting ID
    Boolean allowBookingOnBehalf = true; // Boolean | Allow other team members to schedule on you behalf.
    Boolean allowBookingOvertime = true; // Boolean | Allow team members to insert available time outside your working hours.
    Boolean allowEventOverlap = true; // Boolean | Allow team members to double book events on your calendar.
    Integer availabilityLimit = 56; // Integer | The number of days out the user allows a prospect to schedule a meeting
    Boolean availabilityLimitEnabled = true; // Boolean | If Availability Limits have been turned on
    Integer bufferTimeDuration = 56; // Integer | Default buffer duration in minutes set by a user
    String calendarType = "calendarType_example"; // String | Calendar type
    Integer defaultMeetingLength = 56; // Integer | Default meeting length in minutes set by the user
    String description = "description_example"; // String | Default description of the meeting
    Boolean enableCalendarSync = true; // Boolean | Determines if a user enabled Calendar Sync feature
    Boolean enableDynamicLocation = true; // Boolean | Determines if location will be filled via third-party service (Zoom, GoToMeeting, etc.)
    String location = "location_example"; // String | Default location of the meeting
    Boolean primaryCalendarConnectionFailed = true; // Boolean | Determines if the user lost calendar connection
    String primaryCalendarId = "primaryCalendarId_example"; // String | ID of the primary calendar
    String primaryCalendarName = "primaryCalendarName_example"; // String | Display name of the primary calendar
    Boolean rescheduleMeetingsEnabled = true; // Boolean | Determines if a user enabled reschedule meetings feature
    Boolean scheduleBufferEnabled = true; // Boolean | Determines if meetings are scheduled with a 15 minute buffer between them
    Integer scheduleDelay = 56; // Integer | The number of hours in advance a user requires someone to a book a meeting with them
    Boolean shareEventDetail = true; // Boolean | Allow team members to see the details of events on your calendar.
    String timeZone = "timeZone_example"; // String | Time zone for current calendar
    Object timesAvailable = null; // Object | Times available set by a user that can be used to book meetings
    String title = "title_example"; // String | Default title of the meeting
    try {
      MeetingSetting result = apiInstance.v2MeetingsSettingsIdJsonPut(id, allowBookingOnBehalf, allowBookingOvertime, allowEventOverlap, availabilityLimit, availabilityLimitEnabled, bufferTimeDuration, calendarType, defaultMeetingLength, description, enableCalendarSync, enableDynamicLocation, location, primaryCalendarConnectionFailed, primaryCalendarId, primaryCalendarName, rescheduleMeetingsEnabled, scheduleBufferEnabled, scheduleDelay, shareEventDetail, timeZone, timesAvailable, title);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeetingSettingsApi#v2MeetingsSettingsIdJsonPut");
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
| **id** | **String**| MeetingSetting ID | |
| **allowBookingOnBehalf** | **Boolean**| Allow other team members to schedule on you behalf. | [optional] |
| **allowBookingOvertime** | **Boolean**| Allow team members to insert available time outside your working hours. | [optional] |
| **allowEventOverlap** | **Boolean**| Allow team members to double book events on your calendar. | [optional] |
| **availabilityLimit** | **Integer**| The number of days out the user allows a prospect to schedule a meeting | [optional] |
| **availabilityLimitEnabled** | **Boolean**| If Availability Limits have been turned on | [optional] |
| **bufferTimeDuration** | **Integer**| Default buffer duration in minutes set by a user | [optional] |
| **calendarType** | **String**| Calendar type | [optional] |
| **defaultMeetingLength** | **Integer**| Default meeting length in minutes set by the user | [optional] |
| **description** | **String**| Default description of the meeting | [optional] |
| **enableCalendarSync** | **Boolean**| Determines if a user enabled Calendar Sync feature | [optional] |
| **enableDynamicLocation** | **Boolean**| Determines if location will be filled via third-party service (Zoom, GoToMeeting, etc.) | [optional] |
| **location** | **String**| Default location of the meeting | [optional] |
| **primaryCalendarConnectionFailed** | **Boolean**| Determines if the user lost calendar connection | [optional] |
| **primaryCalendarId** | **String**| ID of the primary calendar | [optional] |
| **primaryCalendarName** | **String**| Display name of the primary calendar | [optional] |
| **rescheduleMeetingsEnabled** | **Boolean**| Determines if a user enabled reschedule meetings feature | [optional] |
| **scheduleBufferEnabled** | **Boolean**| Determines if meetings are scheduled with a 15 minute buffer between them | [optional] |
| **scheduleDelay** | **Integer**| The number of hours in advance a user requires someone to a book a meeting with them | [optional] |
| **shareEventDetail** | **Boolean**| Allow team members to see the details of events on your calendar. | [optional] |
| **timeZone** | **String**| Time zone for current calendar | [optional] |
| **timesAvailable** | [**Object**](Object.md)| Times available set by a user that can be used to book meetings | [optional] |
| **title** | **String**| Default title of the meeting | [optional] |

### Return type

[**MeetingSetting**](MeetingSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

