# GoToWebinar.SessionsApi

All URIs are relative to *https://api.getgo.com/G2W/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllSessions**](SessionsApi.md#getAllSessions) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/sessions | Get webinar sessions
[**getOrganizerSessions**](SessionsApi.md#getOrganizerSessions) | **GET** /organizers/{organizerKey}/sessions | Get organizer sessions
[**getPerformance**](SessionsApi.md#getPerformance) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/sessions/{sessionKey}/performance | Get session performance
[**getPolls**](SessionsApi.md#getPolls) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/sessions/{sessionKey}/polls | Get session polls
[**getQuestions**](SessionsApi.md#getQuestions) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/sessions/{sessionKey}/questions | Get session questions
[**getSurveys**](SessionsApi.md#getSurveys) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/sessions/{sessionKey}/surveys | Get session surveys
[**getWebinarSession**](SessionsApi.md#getWebinarSession) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/sessions/{sessionKey} | Get webinar session



## getAllSessions

> [Session] getAllSessions(authorization, organizerKey, webinarKey)

Get webinar sessions

Retrieves details for all past sessions of a specific webinar.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.SessionsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
apiInstance.getAllSessions(authorization, organizerKey, webinarKey, (error, data, response) => {
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
 **webinarKey** | **Number**| The key of the webinar | 

### Return type

[**[Session]**](Session.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizerSessions

> [Session] getOrganizerSessions(authorization, organizerKey, fromTime, toTime)

Get organizer sessions

Retrieve all completed sessions of all the webinars of a given organizer.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.SessionsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let fromTime = new Date("2013-10-20T19:20:30+01:00"); // Date | A required start of datetime range in ISO8601 UTC format, e.g. 2015-07-13T10:00:00Z
let toTime = new Date("2013-10-20T19:20:30+01:00"); // Date | A required end of datetime range in ISO8601 UTC format, e.g. 2015-07-13T22:00:00Z
apiInstance.getOrganizerSessions(authorization, organizerKey, fromTime, toTime, (error, data, response) => {
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
 **fromTime** | **Date**| A required start of datetime range in ISO8601 UTC format, e.g. 2015-07-13T10:00:00Z | 
 **toTime** | **Date**| A required end of datetime range in ISO8601 UTC format, e.g. 2015-07-13T22:00:00Z | 

### Return type

[**[Session]**](Session.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPerformance

> SessionPerformance getPerformance(authorization, organizerKey, webinarKey, sessionKey)

Get session performance

Get performance details for a session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.SessionsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
let sessionKey = 789; // Number | The key of the webinar session
apiInstance.getPerformance(authorization, organizerKey, webinarKey, sessionKey, (error, data, response) => {
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
 **webinarKey** | **Number**| The key of the webinar | 
 **sessionKey** | **Number**| The key of the webinar session | 

### Return type

[**SessionPerformance**](SessionPerformance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPolls

> [Poll] getPolls(authorization, organizerKey, webinarKey, sessionKey)

Get session polls

Retrieve all collated attendee questions and answers for polls from a specific webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.SessionsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
let sessionKey = 789; // Number | The key of the webinar session
apiInstance.getPolls(authorization, organizerKey, webinarKey, sessionKey, (error, data, response) => {
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
 **webinarKey** | **Number**| The key of the webinar | 
 **sessionKey** | **Number**| The key of the webinar session | 

### Return type

[**[Poll]**](Poll.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getQuestions

> [AttendeeQuestion] getQuestions(authorization, organizerKey, webinarKey, sessionKey)

Get session questions

Retrieve questions and answers for a past webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.SessionsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
let sessionKey = 789; // Number | The key of the webinar session
apiInstance.getQuestions(authorization, organizerKey, webinarKey, sessionKey, (error, data, response) => {
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
 **webinarKey** | **Number**| The key of the webinar | 
 **sessionKey** | **Number**| The key of the webinar session | 

### Return type

[**[AttendeeQuestion]**](AttendeeQuestion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSurveys

> [Poll] getSurveys(authorization, organizerKey, webinarKey, sessionKey)

Get session surveys

Retrieve surveys for a past webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.SessionsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
let sessionKey = 789; // Number | The key of the webinar session
apiInstance.getSurveys(authorization, organizerKey, webinarKey, sessionKey, (error, data, response) => {
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
 **webinarKey** | **Number**| The key of the webinar | 
 **sessionKey** | **Number**| The key of the webinar session | 

### Return type

[**[Poll]**](Poll.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWebinarSession

> [Attendee] getWebinarSession(authorization, organizerKey, webinarKey, sessionKey)

Get webinar session

Retrieves attendance details for a specific webinar session that has ended. If attendees attended the session (&#39;registrantsAttended&#39;), specific attendance details, such as attendenceTime for a registrant, will also be retrieved. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.SessionsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
let sessionKey = 789; // Number | The key of the webinar session
apiInstance.getWebinarSession(authorization, organizerKey, webinarKey, sessionKey, (error, data, response) => {
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
 **webinarKey** | **Number**| The key of the webinar | 
 **sessionKey** | **Number**| The key of the webinar session | 

### Return type

[**[Attendee]**](Attendee.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

