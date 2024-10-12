# SalesLoftPlatform.CalendarEventsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2CalendarEventsGet**](CalendarEventsApi.md#v2CalendarEventsGet) | **GET** /v2/calendar/events | List calendar events
[**v2CalendarEventsUpsertPost**](CalendarEventsApi.md#v2CalendarEventsUpsertPost) | **POST** /v2/calendar/events/upsert | Upsert a calendar event



## v2CalendarEventsGet

> [CalendarEvent] v2CalendarEventsGet(opts)

List calendar events

Returns all calendar events, paginated and filtered by the date.

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.CalendarEventsApi();
let opts = {
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: start_time. Defaults to start_time
  'sortDirection': "sortDirection_example", // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
  'startTime': "startTime_example", // String | Lower bound (inclusive) for a calendar event's end time to filter by. Must be in ISO 8601 format.  Example: `2022-02-14T10:12:59+00:00`. 
  'endTime': "endTime_example", // String | Upper bound (exclusive) for a calendar event's start time to filter by. Must be in ISO 8601 format.  Example: `2022-02-14T10:12:59+00:00`. 
  'userGuid': "userGuid_example", // String | user_guid of the user who created or included as a guest to the event. 
  'calendarId': "calendarId_example" // String | calendar_id of the user who created or included as a guest to the event. 
};
apiInstance.v2CalendarEventsGet(opts, (error, data, response) => {
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
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: start_time. Defaults to start_time | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] 
 **startTime** | **String**| Lower bound (inclusive) for a calendar event&#39;s end time to filter by. Must be in ISO 8601 format.  Example: &#x60;2022-02-14T10:12:59+00:00&#x60;.  | [optional] 
 **endTime** | **String**| Upper bound (exclusive) for a calendar event&#39;s start time to filter by. Must be in ISO 8601 format.  Example: &#x60;2022-02-14T10:12:59+00:00&#x60;.  | [optional] 
 **userGuid** | **String**| user_guid of the user who created or included as a guest to the event.  | [optional] 
 **calendarId** | **String**| calendar_id of the user who created or included as a guest to the event.  | [optional] 

### Return type

[**[CalendarEvent]**](CalendarEvent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2CalendarEventsUpsertPost

> CalendarEvent v2CalendarEventsUpsertPost(calendarId, endTime, iCalUid, id, startTime, opts)

Upsert a calendar event

  Upserts a calendar event object.   Upsert key is a combination of &#x60;id&#x60; and &#x60;i_cal_uid&#x60; scoped to the given &#x60;calendar_id&#x60;.   Bulk operations:   This endpoint is used for bulk operations, see https://developers.salesloft.com/bulk.html for integration instructions.   Use &#x60;calendar/events/upsert&#x60; as an event type, and this spec as a data spec.   This endpoint should be used directly for the time sensitive calendar event updates. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.CalendarEventsApi();
let calendarId = "calendarId_example"; // String |   Calendar ID of the calendar event owner.   For the External Calendar connection use `external_{salesloft_user_guid}` format.   Example: `external_00210d1a-df8a-459f-af75-89b953b618b0`. 
let endTime = new Date("2013-10-20"); // Date |   End time of the calendar event, as a combined date-time value in the ISO 8601 format with a time zone offset.   Example: `2022-02-14T10:12:59+00:00`. 
let iCalUid = "iCalUid_example"; // String |   icalUID of the calendar event. Unique identifier for a calendar event across calendars.    Used as an upsert key. 
let id = "id_example"; // String |   Id of the calendar event, different for each occurrence in a recurring series.    Used as an upsert key. 
let startTime = new Date("2013-10-20"); // Date |   Start time of the calendar event, as a combined date-time value in the ISO 8601 format with a time zone offset.   Example: `2022-02-14T10:12:59+00:00`. 
let opts = {
  'allDay': true, // Boolean | Should be set to `true` for all day calendar events.
  'attendees': {key: null}, // Object |   List of attendees of the calendar event.   Example:   ```     {       ...       \\\"attendees\\\": [         {           \\\"name\\\": \\\"Alice\\\",           \\\"email\\\": \\\"alice@example.com\\\",           \\\"status\\\": \\\"accepted\\\",           \\\"organizer\\\": true         },         {           \\\"name\\\": \\\"Bob\\\",           \\\"email\\\": \\\"bob@example.com\\\",           \\\"status\\\": \\\"needsAction\\\",           \\\"organizer\\\": false         }       ]     }   ```   `name`: full name of the attendee    `email`: email address of the attendee    `status`: one of the following - needsAction, accepted, tentative, declined    `organizer`: whether the attendee is the organizer of the calendar event 
  'canceledAt': "canceledAt_example", // String |   Cancellation time of the calendar event, as a combined date-time value in the ISO 8601 format with a time zone offset.   Example: `2022-02-14T10:12:59+00:00`. 
  'description': "description_example", // String | Description of the calendar event
  'location': "location_example", // String | Location of the calendar event as free-form text.
  'organizer': "organizer_example", // String |   Email address of the organizer 
  'recurring': true, // Boolean | Should be set to `true` if this is one of recurring series calendar event.
  'status': "status_example", // String |   Status of the calendar event. Depending on the status, the calendar event will or will not impact user's availability.   Possible values: `confirmed`, `tentative`, `cancelled`.   Example: `confirmed`. 
  'title': "title_example", // String | Title of the calendar event
  'updatedAt': "updatedAt_example" // String |   Last modification time of the event in the ISO 8601 format with a time zone offset. The event will not be updated if the 'updated_at' timestamp from the payload is earlier than the one in the database.   Example: `2022-02-14T10:12:59+00:00`. 
};
apiInstance.v2CalendarEventsUpsertPost(calendarId, endTime, iCalUid, id, startTime, opts, (error, data, response) => {
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
 **calendarId** | **String**|   Calendar ID of the calendar event owner.   For the External Calendar connection use &#x60;external_{salesloft_user_guid}&#x60; format.   Example: &#x60;external_00210d1a-df8a-459f-af75-89b953b618b0&#x60;.  | 
 **endTime** | **Date**|   End time of the calendar event, as a combined date-time value in the ISO 8601 format with a time zone offset.   Example: &#x60;2022-02-14T10:12:59+00:00&#x60;.  | 
 **iCalUid** | **String**|   icalUID of the calendar event. Unique identifier for a calendar event across calendars.    Used as an upsert key.  | 
 **id** | **String**|   Id of the calendar event, different for each occurrence in a recurring series.    Used as an upsert key.  | 
 **startTime** | **Date**|   Start time of the calendar event, as a combined date-time value in the ISO 8601 format with a time zone offset.   Example: &#x60;2022-02-14T10:12:59+00:00&#x60;.  | 
 **allDay** | **Boolean**| Should be set to &#x60;true&#x60; for all day calendar events. | [optional] 
 **attendees** | [**Object**](Object.md)|   List of attendees of the calendar event.   Example:   &#x60;&#x60;&#x60;     {       ...       \\\&quot;attendees\\\&quot;: [         {           \\\&quot;name\\\&quot;: \\\&quot;Alice\\\&quot;,           \\\&quot;email\\\&quot;: \\\&quot;alice@example.com\\\&quot;,           \\\&quot;status\\\&quot;: \\\&quot;accepted\\\&quot;,           \\\&quot;organizer\\\&quot;: true         },         {           \\\&quot;name\\\&quot;: \\\&quot;Bob\\\&quot;,           \\\&quot;email\\\&quot;: \\\&quot;bob@example.com\\\&quot;,           \\\&quot;status\\\&quot;: \\\&quot;needsAction\\\&quot;,           \\\&quot;organizer\\\&quot;: false         }       ]     }   &#x60;&#x60;&#x60;   &#x60;name&#x60;: full name of the attendee    &#x60;email&#x60;: email address of the attendee    &#x60;status&#x60;: one of the following - needsAction, accepted, tentative, declined    &#x60;organizer&#x60;: whether the attendee is the organizer of the calendar event  | [optional] 
 **canceledAt** | **String**|   Cancellation time of the calendar event, as a combined date-time value in the ISO 8601 format with a time zone offset.   Example: &#x60;2022-02-14T10:12:59+00:00&#x60;.  | [optional] 
 **description** | **String**| Description of the calendar event | [optional] 
 **location** | **String**| Location of the calendar event as free-form text. | [optional] 
 **organizer** | **String**|   Email address of the organizer  | [optional] 
 **recurring** | **Boolean**| Should be set to &#x60;true&#x60; if this is one of recurring series calendar event. | [optional] 
 **status** | **String**|   Status of the calendar event. Depending on the status, the calendar event will or will not impact user&#39;s availability.   Possible values: &#x60;confirmed&#x60;, &#x60;tentative&#x60;, &#x60;cancelled&#x60;.   Example: &#x60;confirmed&#x60;.  | [optional] 
 **title** | **String**| Title of the calendar event | [optional] 
 **updatedAt** | **String**|   Last modification time of the event in the ISO 8601 format with a time zone offset. The event will not be updated if the &#39;updated_at&#39; timestamp from the payload is earlier than the one in the database.   Example: &#x60;2022-02-14T10:12:59+00:00&#x60;.  | [optional] 

### Return type

[**CalendarEvent**](CalendarEvent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*

