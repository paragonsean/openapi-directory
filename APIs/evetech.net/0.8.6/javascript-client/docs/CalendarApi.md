# EveSwaggerInterface.CalendarApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCharactersCharacterIdCalendar**](CalendarApi.md#getCharactersCharacterIdCalendar) | **GET** /characters/{character_id}/calendar/ | List calendar event summaries
[**getCharactersCharacterIdCalendarEventId**](CalendarApi.md#getCharactersCharacterIdCalendarEventId) | **GET** /characters/{character_id}/calendar/{event_id}/ | Get an event
[**getCharactersCharacterIdCalendarEventIdAttendees**](CalendarApi.md#getCharactersCharacterIdCalendarEventIdAttendees) | **GET** /characters/{character_id}/calendar/{event_id}/attendees/ | Get attendees
[**putCharactersCharacterIdCalendarEventId**](CalendarApi.md#putCharactersCharacterIdCalendarEventId) | **PUT** /characters/{character_id}/calendar/{event_id}/ | Respond to an event



## getCharactersCharacterIdCalendar

> [GetCharactersCharacterIdCalendar200Ok] getCharactersCharacterIdCalendar(characterId, opts)

List calendar event summaries

Get 50 event summaries from the calendar. If no from_event ID is given, the resource will return the next 50 chronological event summaries from now. If a from_event ID is specified, it will return the next 50 chronological event summaries from after that event  --- Alternate route: &#x60;/dev/characters/{character_id}/calendar/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/calendar/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/calendar/&#x60;  --- This route is cached for up to 5 seconds

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.CalendarApi();
let characterId = 56; // Number | An EVE character ID
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'fromEvent': 56, // Number | The event ID to retrieve events from
  'ifNoneMatch': "ifNoneMatch_example", // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.getCharactersCharacterIdCalendar(characterId, opts, (error, data, response) => {
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
 **characterId** | **Number**| An EVE character ID | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **fromEvent** | **Number**| The event ID to retrieve events from | [optional] 
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **String**| Access token to use if unable to set a header | [optional] 

### Return type

[**[GetCharactersCharacterIdCalendar200Ok]**](GetCharactersCharacterIdCalendar200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCharactersCharacterIdCalendarEventId

> GetCharactersCharacterIdCalendarEventIdOk getCharactersCharacterIdCalendarEventId(characterId, eventId, opts)

Get an event

Get all the information for a specific event  --- Alternate route: &#x60;/dev/characters/{character_id}/calendar/{event_id}/&#x60;  Alternate route: &#x60;/v3/characters/{character_id}/calendar/{event_id}/&#x60;  --- This route is cached for up to 5 seconds

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.CalendarApi();
let characterId = 56; // Number | An EVE character ID
let eventId = 56; // Number | The id of the event requested
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example", // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.getCharactersCharacterIdCalendarEventId(characterId, eventId, opts, (error, data, response) => {
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
 **characterId** | **Number**| An EVE character ID | 
 **eventId** | **Number**| The id of the event requested | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **String**| Access token to use if unable to set a header | [optional] 

### Return type

[**GetCharactersCharacterIdCalendarEventIdOk**](GetCharactersCharacterIdCalendarEventIdOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCharactersCharacterIdCalendarEventIdAttendees

> [GetCharactersCharacterIdCalendarEventIdAttendees200Ok] getCharactersCharacterIdCalendarEventIdAttendees(characterId, eventId, opts)

Get attendees

Get all invited attendees for a given event  --- Alternate route: &#x60;/dev/characters/{character_id}/calendar/{event_id}/attendees/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/calendar/{event_id}/attendees/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/calendar/{event_id}/attendees/&#x60;  --- This route is cached for up to 600 seconds

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.CalendarApi();
let characterId = 56; // Number | An EVE character ID
let eventId = 56; // Number | The id of the event requested
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example", // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.getCharactersCharacterIdCalendarEventIdAttendees(characterId, eventId, opts, (error, data, response) => {
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
 **characterId** | **Number**| An EVE character ID | 
 **eventId** | **Number**| The id of the event requested | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **String**| Access token to use if unable to set a header | [optional] 

### Return type

[**[GetCharactersCharacterIdCalendarEventIdAttendees200Ok]**](GetCharactersCharacterIdCalendarEventIdAttendees200Ok.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putCharactersCharacterIdCalendarEventId

> putCharactersCharacterIdCalendarEventId(characterId, eventId, response, opts)

Respond to an event

Set your response status to an event  --- Alternate route: &#x60;/dev/characters/{character_id}/calendar/{event_id}/&#x60;  Alternate route: &#x60;/v3/characters/{character_id}/calendar/{event_id}/&#x60; 

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.CalendarApi();
let characterId = 56; // Number | An EVE character ID
let eventId = 56; // Number | The ID of the event requested
let response = new EveSwaggerInterface.PutCharactersCharacterIdCalendarEventIdResponse(); // PutCharactersCharacterIdCalendarEventIdResponse | The response value to set, overriding current value
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.putCharactersCharacterIdCalendarEventId(characterId, eventId, response, opts, (error, data, response) => {
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
 **characterId** | **Number**| An EVE character ID | 
 **eventId** | **Number**| The ID of the event requested | 
 **response** | [**PutCharactersCharacterIdCalendarEventIdResponse**](PutCharactersCharacterIdCalendarEventIdResponse.md)| The response value to set, overriding current value | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **token** | **String**| Access token to use if unable to set a header | [optional] 

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

