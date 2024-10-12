# AvazaApiDocumentation.TaskApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**taskDelete**](TaskApi.md#taskDelete) | **DELETE** /api/Task | Delete a Task
[**taskGet**](TaskApi.md#taskGet) | **GET** /api/Task | Gets list of Tasks
[**taskGetByID**](TaskApi.md#taskGetByID) | **GET** /api/Task/{id} | Gets Task by Task ID
[**taskLookup**](TaskApi.md#taskLookup) | **GET** /api/Task/Lookup | Gets minimal list of Tasks for the current user
[**taskPost**](TaskApi.md#taskPost) | **POST** /api/Task | Create a Task
[**taskPut**](TaskApi.md#taskPut) | **PUT** /api/Task | Update a Task.



## taskDelete

> Object taskDelete(taskID)

Delete a Task

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.TaskApi();
let taskID = 789; // Number | 
apiInstance.taskDelete(taskID, (error, data, response) => {
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
 **taskID** | **Number**|  | 

### Return type

**Object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## taskGet

> TaskList taskGet(opts)

Gets list of Tasks

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.TaskApi();
let opts = {
  'updatedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional filter to records updated after a specific date.
  'pageSize': 56, // Number | Number of items per page. Defaults to 20.
  'pageNumber': 56, // Number | Page to display. Starts from 1. Defaults to 1
  'sort': "sort_example", // String | Optional sorting instruction. Currently possible values: \"DateUpdated\", \"DateCreated\", \"DateUpdated desc\", \"DateCreated desc\", \"SectionTitle\", \"Title\"
  'isComplete': true, // Boolean | Optional filter to only display tasks linked to a Task Status where isComplete=false, or where isComplete=true
  'projectID': 56 // Number | Optional filter to only display tasks belonging to a specific ProjectID
};
apiInstance.taskGet(opts, (error, data, response) => {
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
 **updatedAfter** | **Date**| Optional filter to records updated after a specific date. | [optional] 
 **pageSize** | **Number**| Number of items per page. Defaults to 20. | [optional] 
 **pageNumber** | **Number**| Page to display. Starts from 1. Defaults to 1 | [optional] 
 **sort** | **String**| Optional sorting instruction. Currently possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot;, \&quot;SectionTitle\&quot;, \&quot;Title\&quot; | [optional] 
 **isComplete** | **Boolean**| Optional filter to only display tasks linked to a Task Status where isComplete&#x3D;false, or where isComplete&#x3D;true | [optional] 
 **projectID** | **Number**| Optional filter to only display tasks belonging to a specific ProjectID | [optional] 

### Return type

[**TaskList**](TaskList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## taskGetByID

> TaskDetails taskGetByID(id)

Gets Task by Task ID

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.TaskApi();
let id = 789; // Number | Task ID number
apiInstance.taskGetByID(id, (error, data, response) => {
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
 **id** | **Number**| Task ID number | 

### Return type

[**TaskDetails**](TaskDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## taskLookup

> TaskDropdownList taskLookup(projectID, opts)

Gets minimal list of Tasks for the current user

Groups Tasks by Section. Default sort is by Section Title followed by Task Title

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.TaskApi();
let projectID = 56; // Number | (required) The ProjectID to use when filtering Tasks
let opts = {
  'pageSize': 56, // Number | Number of items per page (max 1000)
  'pageNumber': 56, // Number | Page to display. Starts from 1.
  'hideCompleted': true, // Boolean | (optional) true/false to hide completed tasks. Defaults false
  'search': "search_example" // String | (optional) Search string to match against Task title. Performs begins-with match
};
apiInstance.taskLookup(projectID, opts, (error, data, response) => {
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
 **projectID** | **Number**| (required) The ProjectID to use when filtering Tasks | 
 **pageSize** | **Number**| Number of items per page (max 1000) | [optional] 
 **pageNumber** | **Number**| Page to display. Starts from 1. | [optional] 
 **hideCompleted** | **Boolean**| (optional) true/false to hide completed tasks. Defaults false | [optional] 
 **search** | **String**| (optional) Search string to match against Task title. Performs begins-with match | [optional] 

### Return type

[**TaskDropdownList**](TaskDropdownList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## taskPost

> TaskDetails taskPost(model)

Create a Task

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.TaskApi();
let model = new AvazaApiDocumentation.NewTask(); // NewTask | 
apiInstance.taskPost(model, (error, data, response) => {
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
 **model** | [**NewTask**](NewTask.md)|  | 

### Return type

[**TaskDetails**](TaskDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## taskPut

> TaskDetails taskPut(model)

Update a Task.

Requires TaskID and a list of field names to update. The FieldsToUpdate field accepts a string array containing field names that should be updated.

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.TaskApi();
let model = new AvazaApiDocumentation.UpdateTask(); // UpdateTask | 
apiInstance.taskPut(model, (error, data, response) => {
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
 **model** | [**UpdateTask**](UpdateTask.md)|  | 

### Return type

[**TaskDetails**](TaskDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml

