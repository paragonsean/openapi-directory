# Story.ViewsApi

All URIs are relative to */story*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sessionsIdViewsGet**](ViewsApi.md#sessionsIdViewsGet) | **GET** /sessions/{session_id}/views | Views: List Session Views
[**sessionsIdViewsPost**](ViewsApi.md#sessionsIdViewsPost) | **POST** /sessions/{session_id}/views | Views: Create A Session View
[**viewsIdDelete**](ViewsApi.md#viewsIdDelete) | **DELETE** /views/{view_id} | Views: Delete by Id
[**viewsIdGet**](ViewsApi.md#viewsIdGet) | **GET** /views/{view_id} | Views: Get View



## sessionsIdViewsGet

> [View] sessionsIdViewsGet(sessionId)

Views: List Session Views

Get data for all views in a session

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.ViewsApi();
let sessionId = "sessionId_example"; // String | The primary key for a view session
apiInstance.sessionsIdViewsGet(sessionId, (error, data, response) => {
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

### Return type

[**[View]**](View.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sessionsIdViewsPost

> View sessionsIdViewsPost(sessionId, requiredParametersToCreateAView)

Views: Create A Session View

Create a page view object for a viewing session

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.ViewsApi();
let sessionId = "sessionId_example"; // String | The primary key for a view session
let requiredParametersToCreateAView = new Story.RequiredParametersToCreateAView(); // RequiredParametersToCreateAView | Collaborator user id and permission type
apiInstance.sessionsIdViewsPost(sessionId, requiredParametersToCreateAView, (error, data, response) => {
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
 **requiredParametersToCreateAView** | [**RequiredParametersToCreateAView**](RequiredParametersToCreateAView.md)| Collaborator user id and permission type | 

### Return type

[**View**](View.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## viewsIdDelete

> viewsIdDelete(viewId)

Views: Delete by Id

Remove a view and dependant data.

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.ViewsApi();
let viewId = "viewId_example"; // String | The primary key for a page view within a session
apiInstance.viewsIdDelete(viewId, (error, data, response) => {
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
 **viewId** | **String**| The primary key for a page view within a session | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## viewsIdGet

> View viewsIdGet(viewId)

Views: Get View

Get view meta data

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.ViewsApi();
let viewId = "viewId_example"; // String | The primary key for a page view within a session
apiInstance.viewsIdGet(viewId, (error, data, response) => {
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
 **viewId** | **String**| The primary key for a page view within a session | 

### Return type

[**View**](View.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

