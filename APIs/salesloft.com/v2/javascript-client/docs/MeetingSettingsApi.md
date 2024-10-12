# SalesLoftPlatform.MeetingSettingsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2MeetingsSettingsIdJsonPut**](MeetingSettingsApi.md#v2MeetingsSettingsIdJsonPut) | **PUT** /v2/meetings/settings/{id}.json | Update a meeting setting



## v2MeetingsSettingsIdJsonPut

> MeetingSetting v2MeetingsSettingsIdJsonPut(id, opts)

Update a meeting setting

Updates a meeting setting, by ID only. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.MeetingSettingsApi();
let id = "id_example"; // String | MeetingSetting ID
let opts = {
  'allowBookingOnBehalf': true, // Boolean | Allow other team members to schedule on you behalf.
  'allowBookingOvertime': true, // Boolean | Allow team members to insert available time outside your working hours.
  'allowEventOverlap': true, // Boolean | Allow team members to double book events on your calendar.
  'availabilityLimit': 56, // Number | The number of days out the user allows a prospect to schedule a meeting
  'availabilityLimitEnabled': true, // Boolean | If Availability Limits have been turned on
  'bufferTimeDuration': 56, // Number | Default buffer duration in minutes set by a user
  'calendarType': "calendarType_example", // String | Calendar type
  'defaultMeetingLength': 56, // Number | Default meeting length in minutes set by the user
  'description': "description_example", // String | Default description of the meeting
  'enableCalendarSync': true, // Boolean | Determines if a user enabled Calendar Sync feature
  'enableDynamicLocation': true, // Boolean | Determines if location will be filled via third-party service (Zoom, GoToMeeting, etc.)
  'location': "location_example", // String | Default location of the meeting
  'primaryCalendarConnectionFailed': true, // Boolean | Determines if the user lost calendar connection
  'primaryCalendarId': "primaryCalendarId_example", // String | ID of the primary calendar
  'primaryCalendarName': "primaryCalendarName_example", // String | Display name of the primary calendar
  'rescheduleMeetingsEnabled': true, // Boolean | Determines if a user enabled reschedule meetings feature
  'scheduleBufferEnabled': true, // Boolean | Determines if meetings are scheduled with a 15 minute buffer between them
  'scheduleDelay': 56, // Number | The number of hours in advance a user requires someone to a book a meeting with them
  'shareEventDetail': true, // Boolean | Allow team members to see the details of events on your calendar.
  'timeZone': "timeZone_example", // String | Time zone for current calendar
  'timesAvailable': {key: null}, // Object | Times available set by a user that can be used to book meetings
  'title': "title_example" // String | Default title of the meeting
};
apiInstance.v2MeetingsSettingsIdJsonPut(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| MeetingSetting ID | 
 **allowBookingOnBehalf** | **Boolean**| Allow other team members to schedule on you behalf. | [optional] 
 **allowBookingOvertime** | **Boolean**| Allow team members to insert available time outside your working hours. | [optional] 
 **allowEventOverlap** | **Boolean**| Allow team members to double book events on your calendar. | [optional] 
 **availabilityLimit** | **Number**| The number of days out the user allows a prospect to schedule a meeting | [optional] 
 **availabilityLimitEnabled** | **Boolean**| If Availability Limits have been turned on | [optional] 
 **bufferTimeDuration** | **Number**| Default buffer duration in minutes set by a user | [optional] 
 **calendarType** | **String**| Calendar type | [optional] 
 **defaultMeetingLength** | **Number**| Default meeting length in minutes set by the user | [optional] 
 **description** | **String**| Default description of the meeting | [optional] 
 **enableCalendarSync** | **Boolean**| Determines if a user enabled Calendar Sync feature | [optional] 
 **enableDynamicLocation** | **Boolean**| Determines if location will be filled via third-party service (Zoom, GoToMeeting, etc.) | [optional] 
 **location** | **String**| Default location of the meeting | [optional] 
 **primaryCalendarConnectionFailed** | **Boolean**| Determines if the user lost calendar connection | [optional] 
 **primaryCalendarId** | **String**| ID of the primary calendar | [optional] 
 **primaryCalendarName** | **String**| Display name of the primary calendar | [optional] 
 **rescheduleMeetingsEnabled** | **Boolean**| Determines if a user enabled reschedule meetings feature | [optional] 
 **scheduleBufferEnabled** | **Boolean**| Determines if meetings are scheduled with a 15 minute buffer between them | [optional] 
 **scheduleDelay** | **Number**| The number of hours in advance a user requires someone to a book a meeting with them | [optional] 
 **shareEventDetail** | **Boolean**| Allow team members to see the details of events on your calendar. | [optional] 
 **timeZone** | **String**| Time zone for current calendar | [optional] 
 **timesAvailable** | [**Object**](Object.md)| Times available set by a user that can be used to book meetings | [optional] 
 **title** | **String**| Default title of the meeting | [optional] 

### Return type

[**MeetingSetting**](MeetingSetting.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*

