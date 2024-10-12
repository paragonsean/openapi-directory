# AvazaApiDocumentation.ProjectTimesheetCategoryApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectTimesheetCategoryGet**](ProjectTimesheetCategoryApi.md#projectTimesheetCategoryGet) | **GET** /api/ProjectTimesheetCategory | Gets list of Project Timesheet Categories
[**projectTimesheetCategoryPost**](ProjectTimesheetCategoryApi.md#projectTimesheetCategoryPost) | **POST** /api/ProjectTimesheetCategory | Assign a TimeSheetCategory to a Project.



## projectTimesheetCategoryGet

> ProjectTimesheetCategoryList projectTimesheetCategoryGet(opts)

Gets list of Project Timesheet Categories

The default sort order is by isBillable desc, Name asc

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ProjectTimesheetCategoryApi();
let opts = {
  'projectID': 56 // Number | Get categories filtered by ProjectID
};
apiInstance.projectTimesheetCategoryGet(opts, (error, data, response) => {
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
 **projectID** | **Number**| Get categories filtered by ProjectID | [optional] 

### Return type

[**ProjectTimesheetCategoryList**](ProjectTimesheetCategoryList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## projectTimesheetCategoryPost

> ProjectTimesheetCategoryDetails projectTimesheetCategoryPost(model)

Assign a TimeSheetCategory to a Project.

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ProjectTimesheetCategoryApi();
let model = new AvazaApiDocumentation.AssignProjectTimesheetCategory(); // AssignProjectTimesheetCategory | 
apiInstance.projectTimesheetCategoryPost(model, (error, data, response) => {
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
 **model** | [**AssignProjectTimesheetCategory**](AssignProjectTimesheetCategory.md)|  | 

### Return type

[**ProjectTimesheetCategoryDetails**](ProjectTimesheetCategoryDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml

