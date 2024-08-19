# VonageIntegrationSuite.EventsApi

All URIs are relative to *https://api.vonage.com/t/vbc.prod/vis/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEvent**](EventsApi.md#getEvent) | **GET** /self/events/{id} | Get event
[**getEventsCount**](EventsApi.md#getEventsCount) | **GET** /self/events/count | Get events count
[**listEvents**](EventsApi.md#listEvents) | **GET** /self/events | List events



## getEvent

> [Event] getEvent(id)

Get event

### Example

```javascript
import VonageIntegrationSuite from 'vonage_integration_suite';

let apiInstance = new VonageIntegrationSuite.EventsApi();
let id = "id_example"; // String | Unique identifier of the event
apiInstance.getEvent(id, (error, data, response) => {
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
 **id** | **String**| Unique identifier of the event | 

### Return type

[**[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventsCount

> EventsCount getEventsCount(opts)

Get events count

### Example

```javascript
import VonageIntegrationSuite from 'vonage_integration_suite';

let apiInstance = new VonageIntegrationSuite.EventsApi();
let opts = {
  'fromDate': 56, // Number | Return events that occurred after this point in time
  'toDate': 56, // Number | Return events that occurred before this point in time
  'direction': "INBOUND,OUTBOUND", // String | Filter by event direction
  'states': "ACTIVE,RINGING" // String | Filter events by state
};
apiInstance.getEventsCount(opts, (error, data, response) => {
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
 **fromDate** | **Number**| Return events that occurred after this point in time | [optional] 
 **toDate** | **Number**| Return events that occurred before this point in time | [optional] 
 **direction** | **String**| Filter by event direction | [optional] 
 **states** | **String**| Filter events by state | [optional] 

### Return type

[**EventsCount**](EventsCount.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEvents

> [Event] listEvents(opts)

List events

### Example

```javascript
import VonageIntegrationSuite from 'vonage_integration_suite';

let apiInstance = new VonageIntegrationSuite.EventsApi();
let opts = {
  'types': "CALL", // String | Record type
  'fromDate': 56, // Number | Return events that occurred after this point in time
  'toDate': 56, // Number | Return events that occurred before this point in time
  'direction': "INBOUND,OUTBOUND", // String | Filter by event direction
  'states': "ACTIVE,RINGING", // String | Filter events by state
  'offset': 789, // Number | Page number of events to return
  'size': 20, // Number | Return this amount of events in the response
  'order': "'ASC'", // String | Sort in either ascending or descending order'
  'sort': "sort_example" // String | Sort events by property
};
apiInstance.listEvents(opts, (error, data, response) => {
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
 **types** | **String**| Record type | [optional] 
 **fromDate** | **Number**| Return events that occurred after this point in time | [optional] 
 **toDate** | **Number**| Return events that occurred before this point in time | [optional] 
 **direction** | **String**| Filter by event direction | [optional] 
 **states** | **String**| Filter events by state | [optional] 
 **offset** | **Number**| Page number of events to return | [optional] 
 **size** | **Number**| Return this amount of events in the response | [optional] [default to 20]
 **order** | **String**| Sort in either ascending or descending order&#39; | [optional] [default to &#39;ASC&#39;]
 **sort** | **String**| Sort events by property | [optional] 

### Return type

[**[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

