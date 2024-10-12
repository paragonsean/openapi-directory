# GoToTraining.ReportsApi

All URIs are relative to *https://api.getgo.com/G2T/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAttendanceDetails**](ReportsApi.md#getAttendanceDetails) | **GET** /reports/organizers/{organizerKey}/sessions/{sessionKey}/attendees | Get Attendance Details
[**getSessionDetailsForDateRange**](ReportsApi.md#getSessionDetailsForDateRange) | **POST** /reports/organizers/{organizerKey}/sessions | Get Sessions by Date Range
[**getSessionDetailsForTraining**](ReportsApi.md#getSessionDetailsForTraining) | **GET** /reports/organizers/{organizerKey}/trainings/{trainingKey} | Get Sessions By Training



## getAttendanceDetails

> [Attendee] getAttendanceDetails(authorization, organizerKey, sessionKey)

Get Attendance Details

This call retrieves a list of registrants from a specific completed training session. The response includes the registrants&#39; email addresses, and if they attended, it includes the duration of each period of their attendance in minutes, and the times at which they joined and left. If a registrant does not attend, they appear at the bottom of the listing with timeInSession &#x3D; 0.

### Example

```javascript
import GoToTraining from 'go_to_training';

let apiInstance = new GoToTraining.ReportsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the training organizer
let sessionKey = 789; // Number | The key of the training session
apiInstance.getAttendanceDetails(authorization, organizerKey, sessionKey, (error, data, response) => {
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
 **organizerKey** | **Number**| The key of the training organizer | 
 **sessionKey** | **Number**| The key of the training session | 

### Return type

[**[Attendee]**](Attendee.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSessionDetailsForDateRange

> [Session] getSessionDetailsForDateRange(authorization, organizerKey, body)

Get Sessions by Date Range

This call returns all session details over a given date range for a given organizer. A session is a completed training event.

### Example

```javascript
import GoToTraining from 'go_to_training';

let apiInstance = new GoToTraining.ReportsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the training organizer
let body = new GoToTraining.DateTimeRange(); // DateTimeRange | The start and end times for the time range over which to retrieve training sessions
apiInstance.getSessionDetailsForDateRange(authorization, organizerKey, body, (error, data, response) => {
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
 **organizerKey** | **Number**| The key of the training organizer | 
 **body** | [**DateTimeRange**](DateTimeRange.md)| The start and end times for the time range over which to retrieve training sessions | 

### Return type

[**[Session]**](Session.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSessionDetailsForTraining

> [Session] getSessionDetailsForTraining(authorization, organizerKey, trainingKey)

Get Sessions By Training

This call returns session details for a given training. A session is a completed training event. Each training may contain one or more sessions.

### Example

```javascript
import GoToTraining from 'go_to_training';

let apiInstance = new GoToTraining.ReportsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the training organizer
let trainingKey = 789; // Number | The key of the training
apiInstance.getSessionDetailsForTraining(authorization, organizerKey, trainingKey, (error, data, response) => {
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
 **organizerKey** | **Number**| The key of the training organizer | 
 **trainingKey** | **Number**| The key of the training | 

### Return type

[**[Session]**](Session.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

