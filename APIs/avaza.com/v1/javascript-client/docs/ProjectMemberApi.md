# AvazaApiDocumentation.ProjectMemberApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectMemberGet**](ProjectMemberApi.md#projectMemberGet) | **GET** /api/ProjectMember | Gets list of Project Members
[**projectMemberPost**](ProjectMemberApi.md#projectMemberPost) | **POST** /api/ProjectMember | Assign a user as a Member of a Project
[**projectMemberPut**](ProjectMemberApi.md#projectMemberPut) | **PUT** /api/ProjectMember | Update a Member of a Project



## projectMemberGet

> ProjectMemberList projectMemberGet(opts)

Gets list of Project Members

Include at least one of ProjectID or UserID parameters.

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ProjectMemberApi();
let opts = {
  'projectID': 56, // Number | Get Project members filtered by ProjectID
  'userID': 56 // Number | Get Project members filtered by UserID
};
apiInstance.projectMemberGet(opts, (error, data, response) => {
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
 **projectID** | **Number**| Get Project members filtered by ProjectID | [optional] 
 **userID** | **Number**| Get Project members filtered by UserID | [optional] 

### Return type

[**ProjectMemberList**](ProjectMemberList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## projectMemberPost

> ProjectMemberDetails projectMemberPost(model)

Assign a user as a Member of a Project

the Amount columns for Cost, Budget, Rates should be specified as a decimal. Financial amounts assume the currency of the Customer company. Budget units depend on the Budget method set on the Project.

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ProjectMemberApi();
let model = new AvazaApiDocumentation.NewProjectMember(); // NewProjectMember | 
apiInstance.projectMemberPost(model, (error, data, response) => {
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
 **model** | [**NewProjectMember**](NewProjectMember.md)|  | 

### Return type

[**ProjectMemberDetails**](ProjectMemberDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## projectMemberPut

> ProjectMemberDetails projectMemberPut(model)

Update a Member of a Project

Fields are only updated if their field name is in the FieldsToUpdate string collection. The Amount columns for Cost, Budget, Rates if specified should be a decimal. Financial amounts assume the currency of the parent Company. Budget units depend on the Budget method set on the Project.

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ProjectMemberApi();
let model = new AvazaApiDocumentation.UpdateProjectMember(); // UpdateProjectMember | 
apiInstance.projectMemberPut(model, (error, data, response) => {
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
 **model** | [**UpdateProjectMember**](UpdateProjectMember.md)|  | 

### Return type

[**ProjectMemberDetails**](ProjectMemberDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml

