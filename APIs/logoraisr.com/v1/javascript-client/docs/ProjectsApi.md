# ApiDocsLogoraisrCom.ProjectsApi

All URIs are relative to *https://api.logoraisr.com/rest-v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectsCreate**](ProjectsApi.md#projectsCreate) | **POST** /projects/ | Create a new project.
[**projectsList**](ProjectsApi.md#projectsList) | **GET** /projects/ | Get user project list.
[**projectsRead**](ProjectsApi.md#projectsRead) | **GET** /projects/{project_number}/ | Get project details.



## projectsCreate

> ProjectResponse projectsCreate(projectRequest)

Create a new project.

This POST-Method creates a new project.

### Example

```javascript
import ApiDocsLogoraisrCom from 'api_docs___logoraisr_com';
let defaultClient = ApiDocsLogoraisrCom.ApiClient.instance;
// Configure API key authorization: Token
let Token = defaultClient.authentications['Token'];
Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token.apiKeyPrefix = 'Token';

let apiInstance = new ApiDocsLogoraisrCom.ProjectsApi();
let projectRequest = new ApiDocsLogoraisrCom.ProjectRequest(); // ProjectRequest | 
apiInstance.projectsCreate(projectRequest, (error, data, response) => {
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
 **projectRequest** | [**ProjectRequest**](ProjectRequest.md)|  | 

### Return type

[**ProjectResponse**](ProjectResponse.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectsList

> Project projectsList()

Get user project list.

This GET-Method lists the user&#39;s projects.

### Example

```javascript
import ApiDocsLogoraisrCom from 'api_docs___logoraisr_com';
let defaultClient = ApiDocsLogoraisrCom.ApiClient.instance;
// Configure API key authorization: Token
let Token = defaultClient.authentications['Token'];
Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token.apiKeyPrefix = 'Token';

let apiInstance = new ApiDocsLogoraisrCom.ProjectsApi();
apiInstance.projectsList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Project**](Project.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsRead

> Project projectsRead(projectNumber)

Get project details.

This GET-Method returns a specific project.

### Example

```javascript
import ApiDocsLogoraisrCom from 'api_docs___logoraisr_com';
let defaultClient = ApiDocsLogoraisrCom.ApiClient.instance;
// Configure API key authorization: Token
let Token = defaultClient.authentications['Token'];
Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token.apiKeyPrefix = 'Token';

let apiInstance = new ApiDocsLogoraisrCom.ProjectsApi();
let projectNumber = "projectNumber_example"; // String | Number of the project.
apiInstance.projectsRead(projectNumber, (error, data, response) => {
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
 **projectNumber** | **String**| Number of the project. | 

### Return type

[**Project**](Project.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

