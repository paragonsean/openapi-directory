# AnchoreEngineApiServer.EventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteEvent**](EventsApi.md#deleteEvent) | **DELETE** /events/{eventId} | Delete Event
[**deleteEvents**](EventsApi.md#deleteEvents) | **DELETE** /events | Delete Events
[**getEvent**](EventsApi.md#getEvent) | **GET** /events/{eventId} | Get Event
[**listEventTypes**](EventsApi.md#listEventTypes) | **GET** /event_types | List Event Types
[**listEvents**](EventsApi.md#listEvents) | **GET** /events | List Events



## deleteEvent

> deleteEvent(eventId, opts)

Delete Event

Delete an event by its event ID

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.EventsApi();
let eventId = "eventId_example"; // String | Event ID of the event to be deleted
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.deleteEvent(eventId, opts, (error, data, response) => {
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
 **eventId** | **String**| Event ID of the event to be deleted | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteEvents

> [String] deleteEvents(opts)

Delete Events

Delete all or a subset of events filtered using the optional query parameters

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.EventsApi();
let opts = {
  'before': "before_example", // String | Delete events that occurred before the timestamp
  'since': "since_example", // String | Delete events that occurred after the timestamp
  'level': "level_example", // String | Delete events that match the level - INFO or ERROR
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.deleteEvents(opts, (error, data, response) => {
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
 **before** | **String**| Delete events that occurred before the timestamp | [optional] 
 **since** | **String**| Delete events that occurred after the timestamp | [optional] 
 **level** | **String**| Delete events that match the level - INFO or ERROR | [optional] 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEvent

> EventResponse getEvent(eventId, opts)

Get Event

Lookup an event by its event ID

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.EventsApi();
let eventId = "eventId_example"; // String | Event ID of the event for lookup
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.getEvent(eventId, opts, (error, data, response) => {
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
 **eventId** | **String**| Event ID of the event for lookup | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEventTypes

> [EventCategory] listEventTypes()

List Event Types

Returns list of event types in the category hierarchy

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.EventsApi();
apiInstance.listEventTypes((error, data, response) => {
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

[**[EventCategory]**](EventCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEvents

> EventsList listEvents(opts)

List Events

Returns a paginated list of events in the descending order of their occurrence. Optional query parameters may be used for filtering results

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.EventsApi();
let opts = {
  'sourceServicename': "sourceServicename_example", // String | Filter events by the originating service
  'sourceHostid': "sourceHostid_example", // String | Filter events by the originating host ID
  'eventType': "eventType_example", // String | Filter events by a prefix match on the event type (e.g. \"user.image.\")
  'resourceType': "resourceType_example", // String | Filter events by the type of resource - tag, imageDigest, repository etc
  'resourceId': "resourceId_example", // String | Filter events by the id of the resource
  'level': "level_example", // String | Filter events by the level - INFO or ERROR
  'since': "since_example", // String | Return events that occurred after the timestamp
  'before': "before_example", // String | Return events that occurred before the timestamp
  'page': 1, // Number | Pagination controls - return the nth page of results. Defaults to first page if left empty
  'limit': 100, // Number | Number of events in the result set. Defaults to 100 if left empty
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
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
 **sourceServicename** | **String**| Filter events by the originating service | [optional] 
 **sourceHostid** | **String**| Filter events by the originating host ID | [optional] 
 **eventType** | **String**| Filter events by a prefix match on the event type (e.g. \&quot;user.image.\&quot;) | [optional] 
 **resourceType** | **String**| Filter events by the type of resource - tag, imageDigest, repository etc | [optional] 
 **resourceId** | **String**| Filter events by the id of the resource | [optional] 
 **level** | **String**| Filter events by the level - INFO or ERROR | [optional] 
 **since** | **String**| Return events that occurred after the timestamp | [optional] 
 **before** | **String**| Return events that occurred before the timestamp | [optional] 
 **page** | **Number**| Pagination controls - return the nth page of results. Defaults to first page if left empty | [optional] [default to 1]
 **limit** | **Number**| Number of events in the result set. Defaults to 100 if left empty | [optional] [default to 100]
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**EventsList**](EventsList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

