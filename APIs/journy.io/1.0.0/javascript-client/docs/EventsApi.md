# DeveloperDocumentation.EventsApi

All URIs are relative to *https://api.journy.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEvents**](EventsApi.md#getEvents) | **GET** /events | Get events
[**trackJourneyEvent**](EventsApi.md#trackJourneyEvent) | **POST** /events | Track event



## getEvents

> GetEvents200Response getEvents()

Get events

Endpoint to list events.

### Example

```javascript
import DeveloperDocumentation from 'developer_documentation';

let apiInstance = new DeveloperDocumentation.EventsApi();
apiInstance.getEvents((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetEvents200Response**](GetEvents200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trackJourneyEvent

> DeleteAccount202Response trackJourneyEvent(trackJourneyEventRequest)

Track event

Endpoint used to track an event for a user or an account.  This endpoint is moved to [Track](#operation/trackEvent).

### Example

```javascript
import DeveloperDocumentation from 'developer_documentation';

let apiInstance = new DeveloperDocumentation.EventsApi();
let trackJourneyEventRequest = new DeveloperDocumentation.TrackJourneyEventRequest(); // TrackJourneyEventRequest | 
apiInstance.trackJourneyEvent(trackJourneyEventRequest, (error, data, response) => {
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
 **trackJourneyEventRequest** | [**TrackJourneyEventRequest**](TrackJourneyEventRequest.md)|  | 

### Return type

[**DeleteAccount202Response**](DeleteAccount202Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

