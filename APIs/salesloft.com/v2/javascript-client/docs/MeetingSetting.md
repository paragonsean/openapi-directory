# SalesLoftPlatform.MeetingSetting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeMeetingUrl** | [**MeetingUrl**](MeetingUrl.md) |  | [optional] 
**allowBookingOnBehalf** | **Boolean** | Allow other team members to schedule on you behalf. | [optional] 
**allowBookingOvertime** | **Boolean** | Allow team members to insert available time outside your working hours. | [optional] 
**allowEventOverlap** | **Boolean** | Allow team members to double book events on your calendar. | [optional] 
**availabilityLimit** | **Number** | The number of days out the user allows a prospect to schedule a meeting | [optional] 
**availabilityLimitEnabled** | **Boolean** | If Availability Limits have been turned on | [optional] 
**bufferTimeDuration** | **Number** | Default buffer duration in minutes set by a user | [optional] 
**calendarType** | **String** | Calendar type | [optional] 
**createdAt** | **Date** | Datetime of when the MeetingSetting was created | [optional] 
**defaultMeetingLength** | **Number** | Default meeting length in minutes set by the user | [optional] 
**description** | **String** | Default description of the meeting | [optional] 
**emailAddress** | **String** | Calendar owner&#39;s email address | [optional] 
**enableCalendarSync** | **Boolean** | Determines if a user enabled Calendar Sync feature | [optional] 
**enableDynamicLocation** | **Boolean** | Determines if location will be filled via third-party service (Zoom, GoToMeeting, etc.) | [optional] 
**id** | **Number** | ID of the MeetingSetting | [optional] 
**location** | **String** | Default location of the meeting | [optional] 
**primaryCalendarConnectionFailed** | **Boolean** | Gets true when any issue with fetching calendar occurs | [optional] 
**primaryCalendarId** | **String** | ID of the primary calendar | [optional] 
**primaryCalendarName** | **String** | Display name of the primary calendar | [optional] 
**rescheduleMeetingsEnabled** | **Boolean** | Determines if a user enabled reschedule meetings feature | [optional] 
**scheduleBufferEnabled** | **Boolean** | Determines if meetings are scheduled with a 15 minute buffer between them | [optional] 
**scheduleDelay** | **Number** | The number of hours in advance a user requires someone to a book a meeting with them | [optional] 
**shareEventDetail** | **Boolean** | Allow team members to see the details of events on your calendar. | [optional] 
**timeZone** | **String** | Time zone for current calendar | [optional] 
**timesAvailable** | **Object** | Times available set by a user that can be used to book meetings | [optional] 
**title** | **String** | Default title of the meeting | [optional] 
**updatedAt** | **Date** | Datetime of when the MeetingSetting was last updated | [optional] 
**user** | [**EmbeddedResource**](EmbeddedResource.md) |  | [optional] 
**userDetails** | **Object** | User details | [optional] 
**userSlug** | **String** | User slug generated with a full name of the user | [optional] 


