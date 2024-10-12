# Story.EventsApi

All URIs are relative to */story*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storyIdEventsGet**](EventsApi.md#storyIdEventsGet) | **GET** /{id}/events | Events: List Events
[**storyIdEventsPost**](EventsApi.md#storyIdEventsPost) | **POST** /{id}/events | Events: Manage Events



## storyIdEventsGet

> [Event] storyIdEventsGet(id)

Events: List Events

Get a list of Events available to users of this story

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.EventsApi();
let id = "id_example"; // String | the id from the story object
apiInstance.storyIdEventsGet(id, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 

### Return type

[**[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storyIdEventsPost

> Object storyIdEventsPost(id, manageEvent)

Events: Manage Events

Add a message to the Story&#39;s conversation

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.EventsApi();
let id = "id_example"; // String | the id from the story object
let manageEvent = new Story.ManageEvent(); // ManageEvent | Collaborator user id and permission type
apiInstance.storyIdEventsPost(id, manageEvent, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 
 **manageEvent** | [**ManageEvent**](ManageEvent.md)| Collaborator user id and permission type | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

