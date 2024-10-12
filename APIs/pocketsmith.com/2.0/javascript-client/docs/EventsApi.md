# PocketSmith.EventsApi

All URIs are relative to *https://api.pocketsmith.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eventsIdDelete**](EventsApi.md#eventsIdDelete) | **DELETE** /events/{id} | Delete event
[**eventsIdGet**](EventsApi.md#eventsIdGet) | **GET** /events/{id} | Get event
[**eventsIdPut**](EventsApi.md#eventsIdPut) | **PUT** /events/{id} | Update event
[**scenariosIdEventsGet**](EventsApi.md#scenariosIdEventsGet) | **GET** /scenarios/{id}/events | List events in scenario.
[**scenariosIdEventsPost**](EventsApi.md#scenariosIdEventsPost) | **POST** /scenarios/{id}/events | Create event in scenario
[**usersIdEventsGet**](EventsApi.md#usersIdEventsGet) | **GET** /users/{id}/events | List events in user.



## eventsIdDelete

> eventsIdDelete(id, behaviour)

Delete event

Deletes an event by its ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.EventsApi();
let id = "42-1601942400"; // String | The unique identifier of the event.
let behaviour = "behaviour_example"; // String | Whether the delete applies only to this event, to all events within the series from this event or to all events within the series.
apiInstance.eventsIdDelete(id, behaviour, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the event. | 
 **behaviour** | **String**| Whether the delete applies only to this event, to all events within the series from this event or to all events within the series. | 

### Return type

null (empty response body)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventsIdGet

> Event eventsIdGet(id)

Get event

Gets a particular event by its ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.EventsApi();
let id = "42-1601942400"; // String | The unique identifier of the event.
apiInstance.eventsIdGet(id, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the event. | 

### Return type

[**Event**](Event.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventsIdPut

> Event eventsIdPut(id, opts)

Update event

Updates an event by its ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.EventsApi();
let id = "42-1601942400"; // String | The unique identifier of the event.
let opts = {
  'eventsIdPutRequest': new PocketSmith.EventsIdPutRequest() // EventsIdPutRequest | 
};
apiInstance.eventsIdPut(id, opts, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the event. | 
 **eventsIdPutRequest** | [**EventsIdPutRequest**](EventsIdPutRequest.md)|  | [optional] 

### Return type

[**Event**](Event.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## scenariosIdEventsGet

> [Event] scenariosIdEventsGet(id, startDate, endDate)

List events in scenario.

Lists events belonging to a scenario by their ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.EventsApi();
let id = 42; // Number | The unique identifier of the scenario.
let startDate = "2020-10-01"; // String | Return the events from and including this date.
let endDate = "2020-10-30"; // String | Return the events until and including this date.
apiInstance.scenariosIdEventsGet(id, startDate, endDate, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the scenario. | 
 **startDate** | **String**| Return the events from and including this date. | 
 **endDate** | **String**| Return the events until and including this date. | 

### Return type

[**[Event]**](Event.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## scenariosIdEventsPost

> Event scenariosIdEventsPost(id, opts)

Create event in scenario

Creates an event in a scenario by its ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.EventsApi();
let id = 42; // Number | The unique identifier of the scenario.
let opts = {
  'scenariosIdEventsPostRequest': new PocketSmith.ScenariosIdEventsPostRequest() // ScenariosIdEventsPostRequest | 
};
apiInstance.scenariosIdEventsPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the scenario. | 
 **scenariosIdEventsPostRequest** | [**ScenariosIdEventsPostRequest**](ScenariosIdEventsPostRequest.md)|  | [optional] 

### Return type

[**Event**](Event.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersIdEventsGet

> [Event] usersIdEventsGet(id, startDate, endDate)

List events in user.

Lists events belonging to a user by their ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.EventsApi();
let id = 42; // Number | The unique identifier of the user.
let startDate = "2020-10-01"; // String | Return the events from and including this date.
let endDate = "2020-10-30"; // String | Return the events until and including this date.
apiInstance.usersIdEventsGet(id, startDate, endDate, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the user. | 
 **startDate** | **String**| Return the events from and including this date. | 
 **endDate** | **String**| Return the events until and including this date. | 

### Return type

[**[Event]**](Event.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

