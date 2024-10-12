# GoToMeeting.MeetingsApi

All URIs are relative to *https://api.citrixonline.com/G2M/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**historicalMeetingsGet**](MeetingsApi.md#historicalMeetingsGet) | **GET** /historicalMeetings | Get historical meetings
[**meetingsGet**](MeetingsApi.md#meetingsGet) | **GET** /meetings | DEPRECATED: Get historical meetings
[**meetingsMeetingIdAttendeesGet**](MeetingsApi.md#meetingsMeetingIdAttendeesGet) | **GET** /meetings/{meetingId}/attendees | Get attendees by meeting
[**meetingsMeetingIdDelete**](MeetingsApi.md#meetingsMeetingIdDelete) | **DELETE** /meetings/{meetingId} | Delete meeting
[**meetingsMeetingIdGet**](MeetingsApi.md#meetingsMeetingIdGet) | **GET** /meetings/{meetingId} | Get meeting
[**meetingsMeetingIdPut**](MeetingsApi.md#meetingsMeetingIdPut) | **PUT** /meetings/{meetingId} | Update meeting
[**meetingsMeetingIdStartGet**](MeetingsApi.md#meetingsMeetingIdStartGet) | **GET** /meetings/{meetingId}/start | Start meeting
[**meetingsPost**](MeetingsApi.md#meetingsPost) | **POST** /meetings | Create meeting
[**upcomingMeetingsGet**](MeetingsApi.md#upcomingMeetingsGet) | **GET** /upcomingMeetings | Get upcoming meetings



## historicalMeetingsGet

> [HistoricalMeeting] historicalMeetingsGet(authorization, startDate, endDate)

Get historical meetings

Get historical meetings for the currently authenticated organizer that started within the specified date/time range. Remark: Meetings which are still ongoing at the time of the request are NOT contained in the result array.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.MeetingsApi();
let authorization = "authorization_example"; // String | Access token
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
let endDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
apiInstance.historicalMeetingsGet(authorization, startDate, endDate, (error, data, response) => {
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
 **authorization** | **String**| Access token | 
 **startDate** | **Date**| Required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z | 
 **endDate** | **Date**| Required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z | 

### Return type

[**[HistoricalMeeting]**](HistoricalMeeting.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meetingsGet

> [MeetingHistory] meetingsGet(authorization, opts)

DEPRECATED: Get historical meetings

DEPRECATED: Please use the new API calls &#39;Get historical meetings&#39; and &#39;Get upcoming meetings&#39;.  Gets historical meetings for the current authenticated organizer. Requires date range for filtering results to only meetings within specified dates. History searches will contain the parameter &#39;meetingInstanceKey&#39; which is used in conjunction with the call &#39;Get Attendees by Meeting&#39; to get attendee information for a past meeting.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.MeetingsApi();
let authorization = "authorization_example"; // String | Access token
let opts = {
  'history': true, // Boolean | When 'true', returns all past meetings within date range
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | If history=true, required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
  'endDate': new Date("2013-10-20T19:20:30+01:00") // Date | If history=true, required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
};
apiInstance.meetingsGet(authorization, opts, (error, data, response) => {
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
 **authorization** | **String**| Access token | 
 **history** | **Boolean**| When &#39;true&#39;, returns all past meetings within date range | [optional] 
 **startDate** | **Date**| If history&#x3D;true, required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z | [optional] 
 **endDate** | **Date**| If history&#x3D;true, required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z | [optional] 

### Return type

[**[MeetingHistory]**](MeetingHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meetingsMeetingIdAttendeesGet

> [AttendeeByMeeting] meetingsMeetingIdAttendeesGet(authorization, meetingId)

Get attendees by meeting

List all attendees for specified meetingId of historical meeting. The historical meetings can be fetched using &#39;Get historical meetings&#39;, &#39;Get historical meetings by organizer&#39;, and &#39;Get historical meetings by group&#39;. For users with the admin role this call returns attendees for any meeting. For any other user the call will return attendees for meetings on which the user is a valid organizer.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.MeetingsApi();
let authorization = "authorization_example"; // String | Access token
let meetingId = 789; // Number | The meeting ID
apiInstance.meetingsMeetingIdAttendeesGet(authorization, meetingId, (error, data, response) => {
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
 **authorization** | **String**| Access token | 
 **meetingId** | **Number**| The meeting ID | 

### Return type

[**[AttendeeByMeeting]**](AttendeeByMeeting.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meetingsMeetingIdDelete

> meetingsMeetingIdDelete(authorization, meetingId)

Delete meeting

Deletes the meeting identified by the meetingId.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.MeetingsApi();
let authorization = "authorization_example"; // String | Access token
let meetingId = 789; // Number | The meeting ID
apiInstance.meetingsMeetingIdDelete(authorization, meetingId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **String**| Access token | 
 **meetingId** | **Number**| The meeting ID | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## meetingsMeetingIdGet

> [MeetingById] meetingsMeetingIdGet(authorization, meetingId)

Get meeting

Returns the meeting details for the specified meeting.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.MeetingsApi();
let authorization = "authorization_example"; // String | Access token
let meetingId = 789; // Number | The meeting ID
apiInstance.meetingsMeetingIdGet(authorization, meetingId, (error, data, response) => {
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
 **authorization** | **String**| Access token | 
 **meetingId** | **Number**| The meeting ID | 

### Return type

[**[MeetingById]**](MeetingById.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meetingsMeetingIdPut

> meetingsMeetingIdPut(authorization, meetingId, body)

Update meeting

Updates an existing meeting specified by meetingId.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.MeetingsApi();
let authorization = "authorization_example"; // String | Access token
let meetingId = 789; // Number | The meeting ID
let body = new GoToMeeting.MeetingReqUpdate(); // MeetingReqUpdate | The meeting details
apiInstance.meetingsMeetingIdPut(authorization, meetingId, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **String**| Access token | 
 **meetingId** | **Number**| The meeting ID | 
 **body** | [**MeetingReqUpdate**](MeetingReqUpdate.md)| The meeting details | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## meetingsMeetingIdStartGet

> StartUrl meetingsMeetingIdStartGet(authorization, meetingId)

Start meeting

Returns a host URL that can be used to start a meeting. When this URL is opened in a web browser, the GoToMeeting client will be downloaded and launched and the meeting will start. The end user is not required to login to a client.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.MeetingsApi();
let authorization = "authorization_example"; // String | Access token
let meetingId = 789; // Number | The meeting ID
apiInstance.meetingsMeetingIdStartGet(authorization, meetingId, (error, data, response) => {
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
 **authorization** | **String**| Access token | 
 **meetingId** | **Number**| The meeting ID | 

### Return type

[**StartUrl**](StartUrl.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meetingsPost

> [MeetingCreated] meetingsPost(authorization, body)

Create meeting

Create a new meeting based on the parameters specified.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.MeetingsApi();
let authorization = "authorization_example"; // String | Access token
let body = new GoToMeeting.MeetingReqCreate(); // MeetingReqCreate | The meeting details
apiInstance.meetingsPost(authorization, body, (error, data, response) => {
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
 **authorization** | **String**| Access token | 
 **body** | [**MeetingReqCreate**](MeetingReqCreate.md)| The meeting details | 

### Return type

[**[MeetingCreated]**](MeetingCreated.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## upcomingMeetingsGet

> [UpcomingMeeting] upcomingMeetingsGet(authorization)

Get upcoming meetings

Gets upcoming meetings for the current authenticated organizer.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.MeetingsApi();
let authorization = "authorization_example"; // String | Access token
apiInstance.upcomingMeetingsGet(authorization, (error, data, response) => {
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
 **authorization** | **String**| Access token | 

### Return type

[**[UpcomingMeeting]**](UpcomingMeeting.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

