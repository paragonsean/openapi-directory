

# Meeting


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | ID of the account the recipient associated to |  [optional] |
|**allDay** | **Boolean** | Whether the meeting is an all-day meeting |  [optional] |
|**attendees** | [**List&lt;EmbeddedAttendeeResource&gt;**](EmbeddedAttendeeResource.md) | The attendees of the meeting. Each attendee includes the following fields: status, email, name, organizer |  [optional] |
|**bookedByMeetingsSettings** | [**EventMeetingSetting**](EventMeetingSetting.md) |  |  [optional] |
|**bookedByUser** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**cadence** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**calendarId** | **String** | Calendar ID of the meeting owner |  [optional] |
|**calendarType** | **String** | Calendar type of the meeting owner. Possible values are: gmail, azure, nylas, linkedin_azure, cerebro, external |  [optional] |
|**canceledAt** | **LocalDate** | Datetime of when the meeting was canceled |  [optional] |
|**createdAt** | **LocalDate** | Datetime of when the meeting was created |  [optional] |
|**crmCustomFields** | **Object** | List of crm custom fields which will be logged to SFDC |  [optional] |
|**crmReferences** | **Object** | List of crm references associated with the meeting |  [optional] |
|**description** | **String** | Description of the meeting |  [optional] |
|**endTime** | **LocalDate** | End time of the meeting |  [optional] |
|**eventId** | **String** | ID of the meeting created by target calendar |  [optional] |
|**eventSource** | **String** | Source of the meeting. Possible values are: &#39;external&#39; - The event was synced to Salesloft platform via Calendar Sync, &#39;internal&#39; - The event was created via Salesloft platform |  [optional] |
|**guests** | **List&lt;String&gt;** | The list of attendees emails of the meeting |  [optional] |
|**iCalUid** | **String** | UID of the meeting provided by target calendar provider |  [optional] |
|**id** | **Integer** | ID of the meeting |  [optional] |
|**location** | **String** | Location of the meeting |  [optional] |
|**meetingType** | **String** | Meeting type |  [optional] |
|**noShow** | **Boolean** | Whether the meeting is a No Show meeting |  [optional] |
|**ownedByMeetingsSettings** | [**EventMeetingSetting**](EventMeetingSetting.md) |  |  [optional] |
|**person** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**recipientEmail** | **String** | Email of the meeting invite recipient |  [optional] |
|**recipientName** | **String** | Name of the meeting invite recipient |  [optional] |
|**rescheduleStatus** | **String** | Status of the meeting rescheduling progress. Possible values are: pending, booked, failed, retry |  [optional] |
|**startTime** | **LocalDate** | Start time of the meeting |  [optional] |
|**status** | **String** | Status of the meeting. Possible values are: pending, booked, failed, retry |  [optional] |
|**step** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**strictAttribution** | **Boolean** | Strict attribution means that we 100% sure which cadence generate the meeting |  [optional] |
|**taskId** | **String** | ID of the created task |  [optional] |
|**title** | **String** | Title of the meeting |  [optional] |
|**updatedAt** | **LocalDate** | Datetime of when the meeting was last updated |  [optional] |



