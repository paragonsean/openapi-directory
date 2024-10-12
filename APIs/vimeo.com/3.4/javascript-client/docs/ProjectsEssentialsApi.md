# Vimeo.ProjectsEssentialsApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createProject**](ProjectsEssentialsApi.md#createProject) | **POST** /users/{user_id}/projects | Create a project
[**createProjectAlt1**](ProjectsEssentialsApi.md#createProjectAlt1) | **POST** /me/projects | Create a project
[**deleteProject**](ProjectsEssentialsApi.md#deleteProject) | **DELETE** /users/{user_id}/projects/{project_id} | Delete a project
[**deleteProjectAlt1**](ProjectsEssentialsApi.md#deleteProjectAlt1) | **DELETE** /me/projects/{project_id} | Delete a project
[**editProject**](ProjectsEssentialsApi.md#editProject) | **PATCH** /users/{user_id}/projects/{project_id} | Edit a project
[**editProjectAlt1**](ProjectsEssentialsApi.md#editProjectAlt1) | **PATCH** /me/projects/{project_id} | Edit a project
[**getProject**](ProjectsEssentialsApi.md#getProject) | **GET** /users/{user_id}/projects/{project_id} | Get a specific project
[**getProjectAlt1**](ProjectsEssentialsApi.md#getProjectAlt1) | **GET** /me/projects/{project_id} | Get a specific project
[**getProjects**](ProjectsEssentialsApi.md#getProjects) | **GET** /users/{user_id}/projects | Get all the projects that belong to a user
[**getProjectsAlt1**](ProjectsEssentialsApi.md#getProjectsAlt1) | **GET** /me/projects | Get all the projects that belong to a user



## createProject

> Project createProject(userId, createProjectAlt1Request)

Create a project

This method creates a new project for the specified user.

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

let apiInstance = new Vimeo.ProjectsEssentialsApi();
let userId = 152184; // Number | The ID of the user.
let createProjectAlt1Request = new Vimeo.CreateProjectAlt1Request(); // CreateProjectAlt1Request | 
apiInstance.createProject(userId, createProjectAlt1Request, (error, data, response) => {
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
 **userId** | **Number**| The ID of the user. | 
 **createProjectAlt1Request** | [**CreateProjectAlt1Request**](CreateProjectAlt1Request.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createProjectAlt1

> Project createProjectAlt1(createProjectAlt1Request)

Create a project

This method creates a new project for the specified user.

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

let apiInstance = new Vimeo.ProjectsEssentialsApi();
let createProjectAlt1Request = new Vimeo.CreateProjectAlt1Request(); // CreateProjectAlt1Request | 
apiInstance.createProjectAlt1(createProjectAlt1Request, (error, data, response) => {
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
 **createProjectAlt1Request** | [**CreateProjectAlt1Request**](CreateProjectAlt1Request.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteProject

> deleteProject(projectId, userId, opts)

Delete a project

This method deletes a project and optionally also the videos that it contains.

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

let apiInstance = new Vimeo.ProjectsEssentialsApi();
let projectId = 12345; // Number | The ID of the project.
let userId = 152184; // Number | The ID of the user.
let opts = {
  'shouldDeleteClips': true // Boolean | Whether to delete all the videos in the project along with the project itself.
};
apiInstance.deleteProject(projectId, userId, opts, (error, data, response) => {
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
 **shouldDeleteClips** | **Boolean**| Whether to delete all the videos in the project along with the project itself. | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteProjectAlt1

> deleteProjectAlt1(projectId, opts)

Delete a project

This method deletes a project and optionally also the videos that it contains.

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

let apiInstance = new Vimeo.ProjectsEssentialsApi();
let projectId = 12345; // Number | The ID of the project.
let opts = {
  'shouldDeleteClips': true // Boolean | Whether to delete all the videos in the project along with the project itself.
};
apiInstance.deleteProjectAlt1(projectId, opts, (error, data, response) => {
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
 **shouldDeleteClips** | **Boolean**| Whether to delete all the videos in the project along with the project itself. | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## editProject

> Project editProject(projectId, userId, createProjectAlt1Request)

Edit a project

This method edits an existing project.

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

let apiInstance = new Vimeo.ProjectsEssentialsApi();
let projectId = 12345; // Number | The ID of the project.
let userId = 152184; // Number | The ID of the user.
let createProjectAlt1Request = new Vimeo.CreateProjectAlt1Request(); // CreateProjectAlt1Request | 
apiInstance.editProject(projectId, userId, createProjectAlt1Request, (error, data, response) => {
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
 **createProjectAlt1Request** | [**CreateProjectAlt1Request**](CreateProjectAlt1Request.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## editProjectAlt1

> Project editProjectAlt1(projectId, createProjectAlt1Request)

Edit a project

This method edits an existing project.

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

let apiInstance = new Vimeo.ProjectsEssentialsApi();
let projectId = 12345; // Number | The ID of the project.
let createProjectAlt1Request = new Vimeo.CreateProjectAlt1Request(); // CreateProjectAlt1Request | 
apiInstance.editProjectAlt1(projectId, createProjectAlt1Request, (error, data, response) => {
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
 **createProjectAlt1Request** | [**CreateProjectAlt1Request**](CreateProjectAlt1Request.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getProject

> Project getProject(projectId, userId)

Get a specific project

This method gets a single project that belongs to the specified user.

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

let apiInstance = new Vimeo.ProjectsEssentialsApi();
let projectId = 12345; // Number | The ID of the project.
let userId = 152184; // Number | The ID of the user.
apiInstance.getProject(projectId, userId, (error, data, response) => {
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

### Return type

[**Project**](Project.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProjectAlt1

> Project getProjectAlt1(projectId)

Get a specific project

This method gets a single project that belongs to the specified user.

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

let apiInstance = new Vimeo.ProjectsEssentialsApi();
let projectId = 12345; // Number | The ID of the project.
apiInstance.getProjectAlt1(projectId, (error, data, response) => {
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

### Return type

[**Project**](Project.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProjects

> [Project] getProjects(userId, opts)

Get all the projects that belong to a user

This method gets all the projects that belong to the specified user.

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

let apiInstance = new Vimeo.ProjectsEssentialsApi();
let userId = 152184; // Number | The ID of the user.
let opts = {
  'direction': "asc", // String | The sort direction of the results.
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10, // Number | The number of items to show on each page of results, up to a maximum of 100.
  'sort': "sort_example" // String | The way to sort the results.
};
apiInstance.getProjects(userId, opts, (error, data, response) => {
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
 **userId** | **Number**| The ID of the user. | 
 **direction** | **String**| The sort direction of the results. | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 
 **sort** | **String**| The way to sort the results. | [optional] 

### Return type

[**[Project]**](Project.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProjectsAlt1

> [Project] getProjectsAlt1(opts)

Get all the projects that belong to a user

This method gets all the projects that belong to the specified user.

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

let apiInstance = new Vimeo.ProjectsEssentialsApi();
let opts = {
  'direction': "asc", // String | The sort direction of the results.
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10, // Number | The number of items to show on each page of results, up to a maximum of 100.
  'sort': "sort_example" // String | The way to sort the results.
};
apiInstance.getProjectsAlt1(opts, (error, data, response) => {
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
 **direction** | **String**| The sort direction of the results. | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 
 **sort** | **String**| The way to sort the results. | [optional] 

### Return type

[**[Project]**](Project.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

