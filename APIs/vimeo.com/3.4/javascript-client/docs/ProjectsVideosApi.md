# Vimeo.ProjectsVideosApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addVideoToProject**](ProjectsVideosApi.md#addVideoToProject) | **PUT** /users/{user_id}/projects/{project_id}/videos/{video_id} | Add a specific video to a project
[**addVideoToProjectAlt1**](ProjectsVideosApi.md#addVideoToProjectAlt1) | **PUT** /me/projects/{project_id}/videos/{video_id} | Add a specific video to a project
[**addVideosToProject**](ProjectsVideosApi.md#addVideosToProject) | **PUT** /users/{user_id}/projects/{project_id}/videos | Add a list of videos to a project
[**addVideosToProjectAlt1**](ProjectsVideosApi.md#addVideosToProjectAlt1) | **PUT** /me/projects/{project_id}/videos | Add a list of videos to a project
[**getProjectVideos**](ProjectsVideosApi.md#getProjectVideos) | **GET** /users/{user_id}/projects/{project_id}/videos | Get all the videos in a project
[**getProjectVideosAlt1**](ProjectsVideosApi.md#getProjectVideosAlt1) | **GET** /me/projects/{project_id}/videos | Get all the videos in a project
[**removeVideoFromProject**](ProjectsVideosApi.md#removeVideoFromProject) | **DELETE** /users/{user_id}/projects/{project_id}/videos/{video_id} | Remove a specific video from a project
[**removeVideoFromProjectAlt1**](ProjectsVideosApi.md#removeVideoFromProjectAlt1) | **DELETE** /me/projects/{project_id}/videos/{video_id} | Remove a specific video from a project
[**removeVideosFromProject**](ProjectsVideosApi.md#removeVideosFromProject) | **DELETE** /users/{user_id}/projects/{project_id}/videos | Remove a list of videos from a project
[**removeVideosFromProjectAlt1**](ProjectsVideosApi.md#removeVideosFromProjectAlt1) | **DELETE** /me/projects/{project_id}/videos | Remove a list of videos from a project



## addVideoToProject

> addVideoToProject(projectId, userId, videoId)

Add a specific video to a project

This method adds a single video to the specified project.

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.ProjectsVideosApi();
let projectId = 12345; // Number | The ID of the project.
let userId = 152184; // Number | The ID of the user.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.addVideoToProject(projectId, userId, videoId, (error, data, response) => {
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
 **projectId** | **Number**| The ID of the project. | 
 **userId** | **Number**| The ID of the user. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addVideoToProjectAlt1

> addVideoToProjectAlt1(projectId, videoId)

Add a specific video to a project

This method adds a single video to the specified project.

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.ProjectsVideosApi();
let projectId = 12345; // Number | The ID of the project.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.addVideoToProjectAlt1(projectId, videoId, (error, data, response) => {
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
 **projectId** | **Number**| The ID of the project. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addVideosToProject

> addVideosToProject(projectId, userId, uris)

Add a list of videos to a project

This method adds multiple videos to the specified project.

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.ProjectsVideosApi();
let projectId = 12345; // Number | The ID of the project.
let userId = 152184; // Number | The ID of the user.
let uris = "/videos/258684937,/videos/273576296"; // String | A comma-separated list of video URIs to add.
apiInstance.addVideosToProject(projectId, userId, uris, (error, data, response) => {
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
 **projectId** | **Number**| The ID of the project. | 
 **userId** | **Number**| The ID of the user. | 
 **uris** | **String**| A comma-separated list of video URIs to add. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addVideosToProjectAlt1

> addVideosToProjectAlt1(projectId, uris)

Add a list of videos to a project

This method adds multiple videos to the specified project.

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.ProjectsVideosApi();
let projectId = 12345; // Number | The ID of the project.
let uris = "/videos/258684937,/videos/273576296"; // String | A comma-separated list of video URIs to add.
apiInstance.addVideosToProjectAlt1(projectId, uris, (error, data, response) => {
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
 **projectId** | **Number**| The ID of the project. | 
 **uris** | **String**| A comma-separated list of video URIs to add. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProjectVideos

> [Video] getProjectVideos(projectId, userId, opts)

Get all the videos in a project

This method gets all the videos that belong to the specified project.

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.ProjectsVideosApi();
let projectId = 12345; // Number | The ID of the project.
let userId = 152184; // Number | The ID of the user.
let opts = {
  'direction': "asc", // String | The sort direction of the results.
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10, // Number | The number of items to show on each page of results, up to a maximum of 100.
  'sort': "sort_example" // String | The way to sort the results.
};
apiInstance.getProjectVideos(projectId, userId, opts, (error, data, response) => {
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
 **projectId** | **Number**| The ID of the project. | 
 **userId** | **Number**| The ID of the user. | 
 **direction** | **String**| The sort direction of the results. | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 
 **sort** | **String**| The way to sort the results. | [optional] 

### Return type

[**[Video]**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProjectVideosAlt1

> [Video] getProjectVideosAlt1(projectId, opts)

Get all the videos in a project

This method gets all the videos that belong to the specified project.

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.ProjectsVideosApi();
let projectId = 12345; // Number | The ID of the project.
let opts = {
  'direction': "asc", // String | The sort direction of the results.
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10, // Number | The number of items to show on each page of results, up to a maximum of 100.
  'sort': "sort_example" // String | The way to sort the results.
};
apiInstance.getProjectVideosAlt1(projectId, opts, (error, data, response) => {
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
 **projectId** | **Number**| The ID of the project. | 
 **direction** | **String**| The sort direction of the results. | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 
 **sort** | **String**| The way to sort the results. | [optional] 

### Return type

[**[Video]**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeVideoFromProject

> removeVideoFromProject(projectId, userId, videoId)

Remove a specific video from a project

This method removes a single video from the specified project.

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.ProjectsVideosApi();
let projectId = 12345; // Number | The ID of the project.
let userId = 152184; // Number | The ID of the user.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.removeVideoFromProject(projectId, userId, videoId, (error, data, response) => {
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
 **projectId** | **Number**| The ID of the project. | 
 **userId** | **Number**| The ID of the user. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeVideoFromProjectAlt1

> removeVideoFromProjectAlt1(projectId, videoId)

Remove a specific video from a project

This method removes a single video from the specified project.

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.ProjectsVideosApi();
let projectId = 12345; // Number | The ID of the project.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.removeVideoFromProjectAlt1(projectId, videoId, (error, data, response) => {
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
 **projectId** | **Number**| The ID of the project. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeVideosFromProject

> removeVideosFromProject(projectId, userId, uris, opts)

Remove a list of videos from a project

This method removed multiple videos from the specified project.

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.ProjectsVideosApi();
let projectId = 12345; // Number | The ID of the project.
let userId = 152184; // Number | The ID of the user.
let uris = "/videos/258684937,/videos/273576296"; // String | A comma-separated list of the video URIs to remove.
let opts = {
  'shouldDeleteClips': false // Boolean | Whether to delete the videos when removing them from the project.
};
apiInstance.removeVideosFromProject(projectId, userId, uris, opts, (error, data, response) => {
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
 **projectId** | **Number**| The ID of the project. | 
 **userId** | **Number**| The ID of the user. | 
 **uris** | **String**| A comma-separated list of the video URIs to remove. | 
 **shouldDeleteClips** | **Boolean**| Whether to delete the videos when removing them from the project. | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeVideosFromProjectAlt1

> removeVideosFromProjectAlt1(projectId, uris, opts)

Remove a list of videos from a project

This method removed multiple videos from the specified project.

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.ProjectsVideosApi();
let projectId = 12345; // Number | The ID of the project.
let uris = "/videos/258684937,/videos/273576296"; // String | A comma-separated list of the video URIs to remove.
let opts = {
  'shouldDeleteClips': false // Boolean | Whether to delete the videos when removing them from the project.
};
apiInstance.removeVideosFromProjectAlt1(projectId, uris, opts, (error, data, response) => {
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
 **projectId** | **Number**| The ID of the project. | 
 **uris** | **String**| A comma-separated list of the video URIs to remove. | 
 **shouldDeleteClips** | **Boolean**| Whether to delete the videos when removing them from the project. | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

