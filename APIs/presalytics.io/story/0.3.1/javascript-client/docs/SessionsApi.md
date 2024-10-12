# Story.SessionsApi

All URIs are relative to */story*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sessionIdDelete**](SessionsApi.md#sessionIdDelete) | **DELETE** /sessions/{session_id} | Sessions: Delete by Id
[**sessionIdGet**](SessionsApi.md#sessionIdGet) | **GET** /sessions/{session_id} | Sessions: Get
[**storyIdSessionPost**](SessionsApi.md#storyIdSessionPost) | **POST** /{id}/sessions | Sessions: Create a Session
[**storyIdSessionsGet**](SessionsApi.md#storyIdSessionsGet) | **GET** /{id}/sessions | Sessions: List Story Sessions



## sessionIdDelete

> sessionIdDelete(sessionId)

Sessions: Delete by Id

Remove a session and dependant data.

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.SessionsApi();
let sessionId = "sessionId_example"; // String | The primary key for a view session
apiInstance.sessionIdDelete(sessionId, (error, data, response) => {
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
 **sessionId** | **String**| The primary key for a view session | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sessionIdGet

> Session sessionIdGet(sessionId, opts)

Sessions: Get

Get session metadata

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.SessionsApi();
let sessionId = "sessionId_example"; // String | The primary key for a view session
let opts = {
  'includeRelationships': true // Boolean | Indicate whether the returned object should include child relationships
};
apiInstance.sessionIdGet(sessionId, opts, (error, data, response) => {
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
 **sessionId** | **String**| The primary key for a view session | 
 **includeRelationships** | **Boolean**| Indicate whether the returned object should include child relationships | [optional] 

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storyIdSessionPost

> Session storyIdSessionPost(id, createSessionRequest)

Sessions: Create a Session

Create a new session

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.SessionsApi();
let id = "id_example"; // String | the id from the story object
let createSessionRequest = new Story.CreateSessionRequest(); // CreateSessionRequest | Collaborator user id and permission type
apiInstance.storyIdSessionPost(id, createSessionRequest, (error, data, response) => {
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
 **createSessionRequest** | [**CreateSessionRequest**](CreateSessionRequest.md)| Collaborator user id and permission type | 

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storyIdSessionsGet

> [Session] storyIdSessionsGet(id, opts)

Sessions: List Story Sessions

Get a list of sessions asscoaited with this story

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.SessionsApi();
let id = "id_example"; // String | the id from the story object
let opts = {
  'includeRelationships': true // Boolean | Indicate whether the returned object should include child relationships
};
apiInstance.storyIdSessionsGet(id, opts, (error, data, response) => {
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
 **includeRelationships** | **Boolean**| Indicate whether the returned object should include child relationships | [optional] 

### Return type

[**[Session]**](Session.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

