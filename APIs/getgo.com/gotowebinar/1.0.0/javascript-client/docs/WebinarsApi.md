# GoToWebinar.WebinarsApi

All URIs are relative to *https://api.getgo.com/G2W/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelWebinar**](WebinarsApi.md#cancelWebinar) | **DELETE** /organizers/{organizerKey}/webinars/{webinarKey} | Cancel webinar
[**createWebinar**](WebinarsApi.md#createWebinar) | **POST** /organizers/{organizerKey}/webinars | Create webinar
[**getAllAccountWebinars**](WebinarsApi.md#getAllAccountWebinars) | **GET** /accounts/{accountKey}/webinars | Get all webinars for an account
[**getAllWebinars**](WebinarsApi.md#getAllWebinars) | **GET** /organizers/{organizerKey}/webinars | Get all webinars
[**getAttendeesForAllWebinarSessions**](WebinarsApi.md#getAttendeesForAllWebinarSessions) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/attendees | Get attendees for all webinar sessions
[**getAudioInformation**](WebinarsApi.md#getAudioInformation) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/audio | Get audio information
[**getHistoricalWebinars**](WebinarsApi.md#getHistoricalWebinars) | **GET** /organizers/{organizerKey}/historicalWebinars | Get historical webinars
[**getPerformanceForAllWebinarSessions**](WebinarsApi.md#getPerformanceForAllWebinarSessions) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/performance | Get performance for all webinar sessions
[**getUpcomingWebinars**](WebinarsApi.md#getUpcomingWebinars) | **GET** /organizers/{organizerKey}/upcomingWebinars | Get upcoming webinars
[**getWebinar**](WebinarsApi.md#getWebinar) | **GET** /organizers/{organizerKey}/webinars/{webinarKey} | Get webinar
[**getWebinarMeetingTimes**](WebinarsApi.md#getWebinarMeetingTimes) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/meetingtimes | Get webinar meeting times
[**updateAudioInformation**](WebinarsApi.md#updateAudioInformation) | **POST** /organizers/{organizerKey}/webinars/{webinarKey}/audio | Update audio information
[**updateWebinar**](WebinarsApi.md#updateWebinar) | **PUT** /organizers/{organizerKey}/webinars/{webinarKey} | Update webinar



## cancelWebinar

> cancelWebinar(authorization, organizerKey, webinarKey, opts)

Cancel webinar

Cancels a specific webinar. If the webinar is a series or sequence, this call deletes all scheduled sessions. To send cancellation emails to registrants set sendCancellationEmails&#x3D;true in the request. When the cancellation emails are sent, the default generated message is used in the cancellation email body.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.WebinarsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
let opts = {
  'sendCancellationEmails': true // Boolean | Indicates whether cancellation notice emails should be sent. The default value is false
};
apiInstance.cancelWebinar(authorization, organizerKey, webinarKey, opts, (error, data, response) => {
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
 **webinarKey** | **Number**| The key of the webinar | 
 **sendCancellationEmails** | **Boolean**| Indicates whether cancellation notice emails should be sent. The default value is false | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createWebinar

> CreatedWebinar createWebinar(authorization, organizerKey, body)

Create webinar

Creates a single session webinar, a sequence of webinars or a series of webinars depending on the type field in the body: \&quot;single_session\&quot; creates a single webinar session, \&quot;sequence\&quot; creates a webinar with multiple meeting times where attendees are expected to be the same for all sessions, and \&quot;series\&quot; creates a webinar with multiple meetings times where attendees choose only one to attend. The default, if no type is declared, is single_session. A sequence webinar requires a \&quot;recurrenceStart\&quot; object consisting of a \&quot;startTime\&quot; and \&quot;endTime\&quot; key for the first webinar of the sequence, a \&quot;recurrencePattern\&quot; of \&quot;daily\&quot;, \&quot;weekly\&quot;, \&quot;monthly\&quot;, and a \&quot;recurrenceEnd\&quot; which is the last date of the sequence (for example, 2016-12-01). A series webinar requires a \&quot;times\&quot; array with a discrete \&quot;startTime\&quot; and \&quot;endTime\&quot; for each webinar in the series. The call requires a webinar subject and description. The \&quot;isPasswordProtected\&quot; sets whether the webinar requires a password for attendees to join. If set to True, the organizer must go to Registration Settings at My Webinars (https://global.gotowebinar.com/webinars.tmpl) and add the password to the webinar, and send the password to the registrants. The response provides a numeric webinarKey in string format for the new webinar. Once a webinar has been created with this method, you can accept registrations.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.WebinarsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let body = new GoToWebinar.WebinarReqCreate(); // WebinarReqCreate | The webinar details
apiInstance.createWebinar(authorization, organizerKey, body, (error, data, response) => {
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
 **body** | [**WebinarReqCreate**](WebinarReqCreate.md)| The webinar details | 

### Return type

[**CreatedWebinar**](CreatedWebinar.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAllAccountWebinars

> AccountWebinarsResponse getAllAccountWebinars(authorization, accountKey, fromTime, toTime, opts)

Get all webinars for an account

Retrieves the list of webinars for an account within a given date range. __*Page*__ and __*size*__ parameters are optional. Default __*page*__ is 0 and default __*size*__ is 20. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.WebinarsApi();
let authorization = "authorization_example"; // String | Access token
let accountKey = 789; // Number | The key of the account
let fromTime = new Date("2013-10-20T19:20:30+01:00"); // Date | A required start of datetime range in ISO8601 UTC format, e.g. 2015-07-13T10:00:00Z
let toTime = new Date("2013-10-20T19:20:30+01:00"); // Date | A required end of datetime range in ISO8601 UTC format, e.g. 2015-07-13T22:00:00Z
let opts = {
  'page': 789, // Number | The page number to be displayed. The first page is 0.
  'size': 789 // Number | The size of the page.
};
apiInstance.getAllAccountWebinars(authorization, accountKey, fromTime, toTime, opts, (error, data, response) => {
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
 **accountKey** | **Number**| The key of the account | 
 **fromTime** | **Date**| A required start of datetime range in ISO8601 UTC format, e.g. 2015-07-13T10:00:00Z | 
 **toTime** | **Date**| A required end of datetime range in ISO8601 UTC format, e.g. 2015-07-13T22:00:00Z | 
 **page** | **Number**| The page number to be displayed. The first page is 0. | [optional] 
 **size** | **Number**| The size of the page. | [optional] 

### Return type

[**AccountWebinarsResponse**](AccountWebinarsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllWebinars

> [Webinar] getAllWebinars(authorization, organizerKey)

Get all webinars

Returns webinars scheduled for the future for a specified organizer.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.WebinarsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
apiInstance.getAllWebinars(authorization, organizerKey, (error, data, response) => {
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

[**[Webinar]**](Webinar.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAttendeesForAllWebinarSessions

> [Attendee] getAttendeesForAllWebinarSessions(authorization, organizerKey, webinarKey)

Get attendees for all webinar sessions

Returns all attendees for all sessions of the specified webinar.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.WebinarsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
apiInstance.getAttendeesForAllWebinarSessions(authorization, organizerKey, webinarKey, (error, data, response) => {
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

[**[Attendee]**](Attendee.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAudioInformation

> Audio getAudioInformation(authorization, organizerKey, webinarKey)

Get audio information

Retrieves the audio/conferencing information for a specific webinar.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.WebinarsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
apiInstance.getAudioInformation(authorization, organizerKey, webinarKey, (error, data, response) => {
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

[**Audio**](Audio.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHistoricalWebinars

> [HistoricalWebinar] getHistoricalWebinars(authorization, organizerKey, fromTime, toTime)

Get historical webinars

Returns details for completed webinars for the specified organizer and completed webinars of other organizers where the specified organizer is a co-organizer.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.WebinarsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let fromTime = new Date("2013-10-20T19:20:30+01:00"); // Date | A required start of datetime range in ISO8601 UTC format, e.g. 2015-07-13T10:00:00Z
let toTime = new Date("2013-10-20T19:20:30+01:00"); // Date | A required end of datetime range in ISO8601 UTC format, e.g. 2015-07-13T22:00:00Z
apiInstance.getHistoricalWebinars(authorization, organizerKey, fromTime, toTime, (error, data, response) => {
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

[**[HistoricalWebinar]**](HistoricalWebinar.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPerformanceForAllWebinarSessions

> {String: SessionPerformance} getPerformanceForAllWebinarSessions(authorization, organizerKey, webinarKey)

Get performance for all webinar sessions

Gets performance details for all sessions of a specific webinar.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.WebinarsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
apiInstance.getPerformanceForAllWebinarSessions(authorization, organizerKey, webinarKey, (error, data, response) => {
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

[**{String: SessionPerformance}**](SessionPerformance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUpcomingWebinars

> [UpcomingWebinar] getUpcomingWebinars(authorization, organizerKey)

Get upcoming webinars

Returns webinars scheduled for the future for the specified organizer and webinars of other organizers where the specified organizer is a co-organizer.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.WebinarsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
apiInstance.getUpcomingWebinars(authorization, organizerKey, (error, data, response) => {
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

[**[UpcomingWebinar]**](UpcomingWebinar.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWebinar

> WebinarByKey getWebinar(authorization, organizerKey, webinarKey)

Get webinar

Retrieve information on a specific webinar. If the type of the webinar is &#39;sequence&#39;, a sequence of future times will be provided. Webinars of type &#39;series&#39; are treated the same as normal webinars - each session in the webinar series has a different webinarKey. If an organizer cancels a webinar, then a request to get that webinar would return a &#39;404 Not Found&#39; error.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.WebinarsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
apiInstance.getWebinar(authorization, organizerKey, webinarKey, (error, data, response) => {
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

[**WebinarByKey**](WebinarByKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWebinarMeetingTimes

> [DateTimeRange] getWebinarMeetingTimes(authorization, organizerKey, webinarKey)

Get webinar meeting times

Retrieves the meeting times for a webinar.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.WebinarsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
apiInstance.getWebinarMeetingTimes(authorization, organizerKey, webinarKey, (error, data, response) => {
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

[**[DateTimeRange]**](DateTimeRange.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAudioInformation

> updateAudioInformation(authorization, organizerKey, webinarKey, body, opts)

Update audio information

Updates the audio/conferencing settings for a specific webinar

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.WebinarsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
let body = new GoToWebinar.AudioUpdate(); // AudioUpdate | The audio/conferencing settings
let opts = {
  'notifyParticipants': true // Boolean | Defines whether to send notifications to participants
};
apiInstance.updateAudioInformation(authorization, organizerKey, webinarKey, body, opts, (error, data, response) => {
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
 **webinarKey** | **Number**| The key of the webinar | 
 **body** | [**AudioUpdate**](AudioUpdate.md)| The audio/conferencing settings | 
 **notifyParticipants** | **Boolean**| Defines whether to send notifications to participants | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateWebinar

> updateWebinar(authorization, organizerKey, webinarKey, body, opts)

Update webinar

Updates a webinar. The call requires at least one of the parameters in the request body. The request completely replaces the existing session, series, or sequence and so must include the full definition of each as for the Create call. Set notifyParticipants&#x3D;true to send update emails to registrants.

### Example

```javascript
import GoToWebinar from 'go_to_webinar';

let apiInstance = new GoToWebinar.WebinarsApi();
let authorization = "authorization_example"; // String | Access token
let organizerKey = 789; // Number | The key of the organizer
let webinarKey = 789; // Number | The key of the webinar
let body = new GoToWebinar.WebinarReqUpdate(); // WebinarReqUpdate | The webinar details
let opts = {
  'notifyParticipants': true // Boolean | Defines whether to send notifications to participants
};
apiInstance.updateWebinar(authorization, organizerKey, webinarKey, body, opts, (error, data, response) => {
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
 **webinarKey** | **Number**| The key of the webinar | 
 **body** | [**WebinarReqUpdate**](WebinarReqUpdate.md)| The webinar details | 
 **notifyParticipants** | **Boolean**| Defines whether to send notifications to participants | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

