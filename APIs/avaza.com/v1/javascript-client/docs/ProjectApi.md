# AvazaApiDocumentation.ProjectApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectGet**](ProjectApi.md#projectGet) | **GET** /api/Project | Gets list of Projects
[**projectGetByID**](ProjectApi.md#projectGetByID) | **GET** /api/Project/{id} | Gets Project by Project ID
[**projectLookup**](ProjectApi.md#projectLookup) | **GET** /api/Project/Lookup | Gets minimal list of active Projects for the current user
[**projectPost**](ProjectApi.md#projectPost) | **POST** /api/Project | Create a Project
[**projectPut**](ProjectApi.md#projectPut) | **PUT** /api/Project | Update an Project



## projectGet

> ProjectList projectGet(opts)

Gets list of Projects

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ProjectApi();
let opts = {
  'updatedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Only show project records updated after a certain date (UTC)
  'pageSize': 56, // Number | Number of items per page (max 1000)
  'pageNumber': 56, // Number | Page to display. Starts from 1.
  'sort': "sort_example", // String | A column to sort on. Current possible values: \"DateUpdated\", \"DateCreated\", \"DateUpdated desc\", \"DateCreated desc\"
  'timesheetUserID': 56, // Number | Filter to the projects that the supplied UserID can add timesheets to
  'includeArchived': true // Boolean | Include Archived Projects in the results
};
apiInstance.projectGet(opts, (error, data, response) => {
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
 **updatedAfter** | **Date**| Only show project records updated after a certain date (UTC) | [optional] 
 **pageSize** | **Number**| Number of items per page (max 1000) | [optional] 
 **pageNumber** | **Number**| Page to display. Starts from 1. | [optional] 
 **sort** | **String**| A column to sort on. Current possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot; | [optional] 
 **timesheetUserID** | **Number**| Filter to the projects that the supplied UserID can add timesheets to | [optional] 
 **includeArchived** | **Boolean**| Include Archived Projects in the results | [optional] 

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## projectGetByID

> ProjectDetails projectGetByID(id)

Gets Project by Project ID

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ProjectApi();
let id = 789; // Number | Project ID number
apiInstance.projectGetByID(id, (error, data, response) => {
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
 **id** | **Number**| Project ID number | 

### Return type

[**ProjectDetails**](ProjectDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## projectLookup

> ProjectDropdownList projectLookup(opts)

Gets minimal list of active Projects for the current user

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ProjectApi();
let opts = {
  'pageSize': 56, // Number | Number of items per page (max 1000)
  'pageNumber': 56, // Number | Page to display. Starts from 1.
  'timesheetUserID': 56, // Number | Optionally Filter to the projects that the supplied UserID can add timesheets to
  'companyIDFK': 56, // Number | Optionally Filter for a specific Company ID
  'search': "search_example" // String | Search string to match against Project title and Customer name
};
apiInstance.projectLookup(opts, (error, data, response) => {
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
 **pageSize** | **Number**| Number of items per page (max 1000) | [optional] 
 **pageNumber** | **Number**| Page to display. Starts from 1. | [optional] 
 **timesheetUserID** | **Number**| Optionally Filter to the projects that the supplied UserID can add timesheets to | [optional] 
 **companyIDFK** | **Number**| Optionally Filter for a specific Company ID | [optional] 
 **search** | **String**| Search string to match against Project title and Customer name | [optional] 

### Return type

[**ProjectDropdownList**](ProjectDropdownList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## projectPost

> ProjectDetails projectPost(model)

Create a Project

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ProjectApi();
let model = new AvazaApiDocumentation.NewProjectModel(); // NewProjectModel | 
apiInstance.projectPost(model, (error, data, response) => {
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
 **model** | [**NewProjectModel**](NewProjectModel.md)|  | 

### Return type

[**ProjectDetails**](ProjectDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## projectPut

> ProjectDetails projectPut(model)

Update an Project

Update a Project

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ProjectApi();
let model = new AvazaApiDocumentation.UpdateProjectModel(); // UpdateProjectModel | 
apiInstance.projectPut(model, (error, data, response) => {
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
 **model** | [**UpdateProjectModel**](UpdateProjectModel.md)|  | 

### Return type

[**ProjectDetails**](ProjectDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml

