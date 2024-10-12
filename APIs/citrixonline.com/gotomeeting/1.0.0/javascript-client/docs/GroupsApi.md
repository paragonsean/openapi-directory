# GoToMeeting.GroupsApi

All URIs are relative to *https://api.citrixonline.com/G2M/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groupsGet**](GroupsApi.md#groupsGet) | **GET** /groups | Get groups
[**groupsGroupKeyAttendeesGet**](GroupsApi.md#groupsGroupKeyAttendeesGet) | **GET** /groups/{groupKey}/attendees | Get attendees by group
[**groupsGroupKeyHistoricalMeetingsGet**](GroupsApi.md#groupsGroupKeyHistoricalMeetingsGet) | **GET** /groups/{groupKey}/historicalMeetings | Get historical meetings by group
[**groupsGroupKeyMeetingsGet**](GroupsApi.md#groupsGroupKeyMeetingsGet) | **GET** /groups/{groupKey}/meetings | DEPRECATED: Get historical meetings by group
[**groupsGroupKeyOrganizersGet**](GroupsApi.md#groupsGroupKeyOrganizersGet) | **GET** /groups/{groupKey}/organizers | Get organizers by group
[**groupsGroupKeyOrganizersPost**](GroupsApi.md#groupsGroupKeyOrganizersPost) | **POST** /groups/{groupKey}/organizers | Create organizer in group
[**groupsGroupKeyUpcomingMeetingsGet**](GroupsApi.md#groupsGroupKeyUpcomingMeetingsGet) | **GET** /groups/{groupKey}/upcomingMeetings | Get upcoming meetings by group



## groupsGet

> [Group] groupsGet(authorization)

Get groups

List all groups for an account. This API call is only available to users with the admin role.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.GroupsApi();
let authorization = "authorization_example"; // String | Access token
apiInstance.groupsGet(authorization, (error, data, response) => {
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

[**[Group]**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupsGroupKeyAttendeesGet

> [AttendeeByGroup] groupsGroupKeyAttendeesGet(authorization, groupKey, opts)

Get attendees by group

Returns all attendees for all meetings within specified date range held by organizers within the specified group. This API call is only available to users with the admin role. This API call can be used only for groups with maximum 50 organizers.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.GroupsApi();
let authorization = "authorization_example"; // String | Access token
let groupKey = 789; // Number | The key of the group
let opts = {
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
  'endDate': new Date("2013-10-20T19:20:30+01:00") // Date | End of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
};
apiInstance.groupsGroupKeyAttendeesGet(authorization, groupKey, opts, (error, data, response) => {
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
 **groupKey** | **Number**| The key of the group | 
 **startDate** | **Date**| Start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z | [optional] 
 **endDate** | **Date**| End of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z | [optional] 

### Return type

[**[AttendeeByGroup]**](AttendeeByGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupsGroupKeyHistoricalMeetingsGet

> [HistoricalMeetingByGroup] groupsGroupKeyHistoricalMeetingsGet(authorization, groupKey, startDate, endDate)

Get historical meetings by group

Get historical meetings for the specified group that started within the specified date/time range. This API call is only available to users with the admin role. This API call is restricted to groups with a maximum of 50 organizers. Remark: Meetings which are still ongoing at the time of the request are NOT contained in the result array.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.GroupsApi();
let authorization = "authorization_example"; // String | Access token
let groupKey = 789; // Number | The key of the group
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
let endDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
apiInstance.groupsGroupKeyHistoricalMeetingsGet(authorization, groupKey, startDate, endDate, (error, data, response) => {
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
 **groupKey** | **Number**| The key of the group | 
 **startDate** | **Date**| Required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z | 
 **endDate** | **Date**| Required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z | 

### Return type

[**[HistoricalMeetingByGroup]**](HistoricalMeetingByGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupsGroupKeyMeetingsGet

> [HistoryMeetingByGroup] groupsGroupKeyMeetingsGet(authorization, groupKey, history, startDate, endDate)

DEPRECATED: Get historical meetings by group

DEPRECATED: Please use the new API calls &#39;Get historical meetings by group&#39; and &#39;Get upcoming meetings by group&#39;. Get meetings for a specified group. Additional filters can be used to view only meetings within a specified date range. This API call is only available to users with the admin role.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.GroupsApi();
let authorization = "authorization_example"; // String | Access token
let groupKey = 789; // Number | The key of the group
let history = true; // Boolean | When 'true', returns all past meetings within date range
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | If history=true, required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
let endDate = new Date("2013-10-20T19:20:30+01:00"); // Date | If history=true, required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
apiInstance.groupsGroupKeyMeetingsGet(authorization, groupKey, history, startDate, endDate, (error, data, response) => {
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
 **groupKey** | **Number**| The key of the group | 
 **history** | **Boolean**| When &#39;true&#39;, returns all past meetings within date range | 
 **startDate** | **Date**| If history&#x3D;true, required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z | 
 **endDate** | **Date**| If history&#x3D;true, required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z | 

### Return type

[**[HistoryMeetingByGroup]**](HistoryMeetingByGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupsGroupKeyOrganizersGet

> [OrganizerByGroup] groupsGroupKeyOrganizersGet(authorization, groupKey)

Get organizers by group

Returns all the organizers within a specific group. This API call is only available to users with the admin role.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.GroupsApi();
let authorization = "authorization_example"; // String | Access token
let groupKey = 789; // Number | The key of the group
apiInstance.groupsGroupKeyOrganizersGet(authorization, groupKey, (error, data, response) => {
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
 **groupKey** | **Number**| The key of the group | 

### Return type

[**[OrganizerByGroup]**](OrganizerByGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupsGroupKeyOrganizersPost

> [OrganizerShort] groupsGroupKeyOrganizersPost(authorization, groupKey, body)

Create organizer in group

Creates a new organizer and sends an email to the email address defined in request. This API call is only available to users with the admin role. You may also pass &#39;G2W&#39; or &#39;G2T&#39; or &#39;OPENVOICE&#39; as productType variables, creating organizers for those products. A G2W or G2T organizer will also have access to G2M.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.GroupsApi();
let authorization = "authorization_example"; // String | Access token
let groupKey = 789; // Number | The key of the group
let body = new GoToMeeting.OrganizerReq(); // OrganizerReq | The details of the organizer to be created
apiInstance.groupsGroupKeyOrganizersPost(authorization, groupKey, body, (error, data, response) => {
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
 **groupKey** | **Number**| The key of the group | 
 **body** | [**OrganizerReq**](OrganizerReq.md)| The details of the organizer to be created | 

### Return type

[**[OrganizerShort]**](OrganizerShort.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## groupsGroupKeyUpcomingMeetingsGet

> [UpcomingMeetingByGroup] groupsGroupKeyUpcomingMeetingsGet(authorization, groupKey)

Get upcoming meetings by group

Get upcoming meetings for a specified group. This API call is only available to users with the admin role. This API call can be used only for groups with maximum 50 organizers.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.GroupsApi();
let authorization = "authorization_example"; // String | Access token
let groupKey = 789; // Number | The key of the group
apiInstance.groupsGroupKeyUpcomingMeetingsGet(authorization, groupKey, (error, data, response) => {
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
 **groupKey** | **Number**| The key of the group | 

### Return type

[**[UpcomingMeetingByGroup]**](UpcomingMeetingByGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

