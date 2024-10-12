# EventGridClient.EventsApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publishEvents**](EventsApi.md#publishEvents) | **POST** /api/events | 



## publishEvents

> publishEvents(apiVersion, events)



Publishes a batch of events to an Azure Event Grid topic.

### Example

```javascript
import EventGridClient from 'event_grid_client';

let apiInstance = new EventGridClient.EventsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let events = [new EventGridClient.EventGridEvent()]; // [EventGridEvent] | An array of events to be published to Event Grid.
apiInstance.publishEvents(apiVersion, events, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **events** | [**[EventGridEvent]**](EventGridEvent.md)| An array of events to be published to Event Grid. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

