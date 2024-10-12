# FitbitPlusApi.CalendarEventResponseApi

All URIs are relative to *https://api.twinehealth.com/pub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCalendarEventResponse**](CalendarEventResponseApi.md#createCalendarEventResponse) | **POST** /calendar_event_response | Create calendar event response



## createCalendarEventResponse

> CreateCalendarEventResponseRequest createCalendarEventResponse(createCalendarEventResponseRequest)

Create calendar event response

Create a calendar event response for an attendee of a calendar event, the attendee can be a coach or patient.  Calendar event responses cannot be fetched, updated nor deleted.  Use calendar event api to fetch the response status for attendees.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.CalendarEventResponseApi();
let createCalendarEventResponseRequest = new FitbitPlusApi.CreateCalendarEventResponseRequest(); // CreateCalendarEventResponseRequest | 
apiInstance.createCalendarEventResponse(createCalendarEventResponseRequest, (error, data, response) => {
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
 **createCalendarEventResponseRequest** | [**CreateCalendarEventResponseRequest**](CreateCalendarEventResponseRequest.md)|  | 

### Return type

[**CreateCalendarEventResponseRequest**](CreateCalendarEventResponseRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.api+json
- **Accept**: application/vnd.api+json

