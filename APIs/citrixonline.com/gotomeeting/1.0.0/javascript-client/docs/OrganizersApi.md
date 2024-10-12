# GoToMeeting.OrganizersApi

All URIs are relative to *https://api.citrixonline.com/G2M/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizersDelete**](OrganizersApi.md#organizersDelete) | **DELETE** /organizers | Delete organizer by email
[**organizersGet**](OrganizersApi.md#organizersGet) | **GET** /organizers | Get organizer by email / Get all organizers
[**organizersOrganizerKeyAttendeesGet**](OrganizersApi.md#organizersOrganizerKeyAttendeesGet) | **GET** /organizers/{organizerKey}/attendees | Get attendees by organizer
[**organizersOrganizerKeyDelete**](OrganizersApi.md#organizersOrganizerKeyDelete) | **DELETE** /organizers/{organizerKey} | Delete organizer
[**organizersOrganizerKeyGet**](OrganizersApi.md#organizersOrganizerKeyGet) | **GET** /organizers/{organizerKey} | Get organizer
[**organizersOrganizerKeyHistoricalMeetingsGet**](OrganizersApi.md#organizersOrganizerKeyHistoricalMeetingsGet) | **GET** /organizers/{organizerKey}/historicalMeetings | Get historical meetings by organizer
[**organizersOrganizerKeyMeetingsGet**](OrganizersApi.md#organizersOrganizerKeyMeetingsGet) | **GET** /organizers/{organizerKey}/meetings | DEPRECATED: Get meetings by organizer
[**organizersOrganizerKeyPut**](OrganizersApi.md#organizersOrganizerKeyPut) | **PUT** /organizers/{organizerKey} | Update organizer
[**organizersOrganizerKeyUpcomingMeetingsGet**](OrganizersApi.md#organizersOrganizerKeyUpcomingMeetingsGet) | **GET** /organizers/{organizerKey}/upcomingMeetings | Get upcoming meetings by organizer
[**organizersPost**](OrganizersApi.md#organizersPost) | **POST** /organizers | Create organizer



## organizersDelete

> organizersDelete(authorization, email)

Delete organizer by email

Deletes the individual organizer specified by the email address. This API call is only available to users with the admin role.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.OrganizersApi();
let authorization = "authorization_example"; // String | Access token
let email = "email_example"; // String | The email address of the organizer
apiInstance.organizersDelete(authorization, email, (error, data, response) => {
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
 **email** | **String**| The email address of the organizer | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organizersGet

> [Organizer] organizersGet(authorization, opts)

Get organizer by email / Get all organizers

Gets the individual organizer specified by the organizer&#39;s email address. If an email address is not specified, all organizers are returned. This API call is only available to users with the admin role.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.OrganizersApi();
let authorization = "authorization_example"; // String | Access token
let opts = {
  'email': "email_example" // String | The email address of the organizer
};
apiInstance.organizersGet(authorization, opts, (error, data, response) => {
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
 **email** | **String**| The email address of the organizer | [optional] 

### Return type

[**[Organizer]**](Organizer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organizersOrganizerKeyAttendeesGet

> [AttendeeByOrganizer] organizersOrganizerKeyAttendeesGet(authorization, organizerKey, startDate, endDate)

Get attendees by organizer

Lists all attendees for all meetings within a specified date range for a specified organizer. This API call is only available to users with the admin role.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.OrganizersApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | A required start of date range in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
let endDate = new Date("2013-10-20T19:20:30+01:00"); // Date | A required end of date range in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
apiInstance.organizersOrganizerKeyAttendeesGet(authorization, organizerKey, startDate, endDate, (error, data, response) => {
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
 **organizerKey** | **Number**| The key of the organizer | 
 **startDate** | **Date**| A required start of date range in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z | 
 **endDate** | **Date**| A required end of date range in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z | 

### Return type

[**[AttendeeByOrganizer]**](AttendeeByOrganizer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organizersOrganizerKeyDelete

> organizersOrganizerKeyDelete(authorization, organizerKey)

Delete organizer

Deletes the individual organizer specified by the organizer key. This API call is only available to users with the admin role.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.OrganizersApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
apiInstance.organizersOrganizerKeyDelete(authorization, organizerKey, (error, data, response) => {
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
 **organizerKey** | **Number**| The key of the organizer | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organizersOrganizerKeyGet

> [Organizer] organizersOrganizerKeyGet(authorization, organizerKey)

Get organizer

Returns the individual organizer specified by the key. This API call is only available to users with the admin role. Non-admin users can only make this call for their own organizerKey.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.OrganizersApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
apiInstance.organizersOrganizerKeyGet(authorization, organizerKey, (error, data, response) => {
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
 **organizerKey** | **Number**| The key of the organizer | 

### Return type

[**[Organizer]**](Organizer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organizersOrganizerKeyHistoricalMeetingsGet

> [HistoricalMeeting] organizersOrganizerKeyHistoricalMeetingsGet(authorization, organizerKey, startDate, endDate)

Get historical meetings by organizer

Get historical meetings for the specified organizer that started within the specified date/time range. Remark: Meetings which are still ongoing at the time of the request are NOT contained in the result array.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.OrganizersApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
let endDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
apiInstance.organizersOrganizerKeyHistoricalMeetingsGet(authorization, organizerKey, startDate, endDate, (error, data, response) => {
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
 **organizerKey** | **Number**| The key of the organizer | 
 **startDate** | **Date**| Required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z | 
 **endDate** | **Date**| Required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z | 

### Return type

[**[HistoricalMeeting]**](HistoricalMeeting.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organizersOrganizerKeyMeetingsGet

> [MeetingByOrganizer] organizersOrganizerKeyMeetingsGet(authorization, organizerKey, opts)

DEPRECATED: Get meetings by organizer

DEPRECATED: Please use the new API calls &#39;Get historical meetings by organizer&#39; and &#39;Get upcoming meetings by organizer&#39;. Gets future (scheduled) or past (history) meetings for a specified organizer. Include &#39;history&#x3D;true&#39; and the past start and end dates in the URL to retrieve past meetings. Enter &#39;scheduled&#x3D;true&#39; (without dates) to get scheduled meetings.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.OrganizersApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let opts = {
  'scheduled': true, // Boolean | When 'true', returns all future meetings. Date range not supported.
  'history': true, // Boolean | When 'true', returns all past meetings within date range
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | If history is 'true', required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z
  'endDate': new Date("2013-10-20T19:20:30+01:00") // Date | If history is 'true', required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z
};
apiInstance.organizersOrganizerKeyMeetingsGet(authorization, organizerKey, opts, (error, data, response) => {
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
 **organizerKey** | **Number**| The key of the organizer | 
 **scheduled** | **Boolean**| When &#39;true&#39;, returns all future meetings. Date range not supported. | [optional] 
 **history** | **Boolean**| When &#39;true&#39;, returns all past meetings within date range | [optional] 
 **startDate** | **Date**| If history is &#39;true&#39;, required start of date range, in ISO8601 UTC format, e.g. 2015-07-01T22:00:00Z | [optional] 
 **endDate** | **Date**| If history is &#39;true&#39;, required end of date range, in ISO8601 UTC format, e.g. 2015-07-01T23:00:00Z | [optional] 

### Return type

[**[MeetingByOrganizer]**](MeetingByOrganizer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organizersOrganizerKeyPut

> organizersOrganizerKeyPut(authorization, organizerKey, body)

Update organizer

Updates the products of the specified organizer. To add a product (G2M, G2W, G2T, OPENVOICE) for the organizer, the call must be sent once for each product you want to add. To remove all products for the organizer, set status to &#39;suspended&#39;. The call is limited to users with the admin role.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.OrganizersApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let body = new GoToMeeting.OrganizerStatus(); // OrganizerStatus | The organizer's status
apiInstance.organizersOrganizerKeyPut(authorization, organizerKey, body, (error, data, response) => {
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
 **organizerKey** | **Number**| The key of the organizer | 
 **body** | [**OrganizerStatus**](OrganizerStatus.md)| The organizer&#39;s status | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## organizersOrganizerKeyUpcomingMeetingsGet

> [UpcomingMeeting] organizersOrganizerKeyUpcomingMeetingsGet(authorization, organizerKey)

Get upcoming meetings by organizer

Get upcoming meetings for a specified organizer. This API call is only available to users with the admin role.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.OrganizersApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
apiInstance.organizersOrganizerKeyUpcomingMeetingsGet(authorization, organizerKey, (error, data, response) => {
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
 **organizerKey** | **Number**| The key of the organizer | 

### Return type

[**[UpcomingMeeting]**](UpcomingMeeting.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organizersPost

> [OrganizerShort] organizersPost(authorization, body)

Create organizer

Creates a new organizer and sends an email to the email address defined in the request. This API call is only available to users with the admin role. You may also pass &#39;G2W&#39; or &#39;G2T&#39; or &#39;OPENVOICE&#39; as productType variables, creating organizers for those products. A G2W or G2T organizer will also have access to G2M.

### Example

```javascript
import GoToMeeting from 'go_to_meeting';

let apiInstance = new GoToMeeting.OrganizersApi();
let authorization = "authorization_example"; // String | Access token
let body = new GoToMeeting.OrganizerReq(); // OrganizerReq | The details of the organizer to be created
apiInstance.organizersPost(authorization, body, (error, data, response) => {
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
 **body** | [**OrganizerReq**](OrganizerReq.md)| The details of the organizer to be created | 

### Return type

[**[OrganizerShort]**](OrganizerShort.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

