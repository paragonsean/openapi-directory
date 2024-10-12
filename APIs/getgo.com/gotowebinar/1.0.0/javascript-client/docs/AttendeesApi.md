# GoToWebinar.AttendeesApi

All URIs are relative to *https://api.getgo.com/G2W/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAttendee**](AttendeesApi.md#getAttendee) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/sessions/{sessionKey}/attendees/{registrantKey} | Get attendee
[**getAttendeePollAnswers**](AttendeesApi.md#getAttendeePollAnswers) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/sessions/{sessionKey}/attendees/{registrantKey}/polls | Get attendee poll answers
[**getAttendeeQuestions**](AttendeesApi.md#getAttendeeQuestions) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/sessions/{sessionKey}/attendees/{registrantKey}/questions | Get attendee questions
[**getAttendeeSurveyAnswers**](AttendeesApi.md#getAttendeeSurveyAnswers) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/sessions/{sessionKey}/attendees/{registrantKey}/surveys | Get attendee survey answers
[**getAttendees**](AttendeesApi.md#getAttendees) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/sessions/{sessionKey}/attendees | Get session attendees



## getAttendee

> Registrant getAttendee(authorization, organizerKey, webinarKey, sessionKey, registrantKey)

Get attendee

Retrieve registration details for a particular attendee of a specific webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.AttendeesApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
let sessionKey = 789; // Number | The key of the webinar session
let registrantKey = 789; // Number | The key of the registrant
apiInstance.getAttendee(authorization, organizerKey, webinarKey, sessionKey, registrantKey, (error, data, response) => {
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
 **registrantKey** | **Number**| The key of the registrant | 

### Return type

[**Registrant**](Registrant.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAttendeePollAnswers

> [PollAnswer] getAttendeePollAnswers(authorization, organizerKey, webinarKey, sessionKey, registrantKey)

Get attendee poll answers

Get poll answers from a particular attendee of a specific webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.AttendeesApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
let sessionKey = 789; // Number | The key of the webinar session
let registrantKey = 789; // Number | The key of the registrant
apiInstance.getAttendeePollAnswers(authorization, organizerKey, webinarKey, sessionKey, registrantKey, (error, data, response) => {
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
 **registrantKey** | **Number**| The key of the registrant | 

### Return type

[**[PollAnswer]**](PollAnswer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAttendeeQuestions

> [AttendeeQuestion] getAttendeeQuestions(authorization, organizerKey, webinarKey, sessionKey, registrantKey)

Get attendee questions

Get questions asked by an attendee during a webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.AttendeesApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
let sessionKey = 789; // Number | The key of the webinar session
let registrantKey = 789; // Number | The key of the registrant
apiInstance.getAttendeeQuestions(authorization, organizerKey, webinarKey, sessionKey, registrantKey, (error, data, response) => {
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
 **registrantKey** | **Number**| The key of the registrant | 

### Return type

[**[AttendeeQuestion]**](AttendeeQuestion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAttendeeSurveyAnswers

> [PollAnswer] getAttendeeSurveyAnswers(authorization, organizerKey, webinarKey, sessionKey, registrantKey)

Get attendee survey answers

Retrieve survey answers from a particular attendee during a webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.AttendeesApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
let sessionKey = 789; // Number | The key of the webinar session
let registrantKey = 789; // Number | The key of the registrant
apiInstance.getAttendeeSurveyAnswers(authorization, organizerKey, webinarKey, sessionKey, registrantKey, (error, data, response) => {
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
 **registrantKey** | **Number**| The key of the registrant | 

### Return type

[**[PollAnswer]**](PollAnswer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAttendees

> [Attendee] getAttendees(authorization, organizerKey, webinarKey, sessionKey)

Get session attendees

Retrieve details for all attendees of a specific webinar session. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.AttendeesApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
let sessionKey = 789; // Number | The key of the webinar session
apiInstance.getAttendees(authorization, organizerKey, webinarKey, sessionKey, (error, data, response) => {
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

