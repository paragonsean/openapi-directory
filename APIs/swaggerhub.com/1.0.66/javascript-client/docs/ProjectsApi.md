# SwaggerHubRegistryApi.ProjectsApi

All URIs are relative to *https://api.swaggerhub.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addSpecToProjectV2**](ProjectsApi.md#addSpecToProjectV2) | **PUT** /projects/{owner}/{projectId}/{specType}/{name} | Add an API or domain to a project
[**createProject**](ProjectsApi.md#createProject) | **POST** /projects/{owner} | Create a project in an organization
[**deleteProjectV2**](ProjectsApi.md#deleteProjectV2) | **DELETE** /projects/{owner}/{projectId} | Delete a project
[**getOrgProjectsV2**](ProjectsApi.md#getOrgProjectsV2) | **GET** /projects/{owner} | Get all projects of an organization
[**getProjectMembersV2**](ProjectsApi.md#getProjectMembersV2) | **GET** /projects/{owner}/{projectId}/members | Get project members
[**getProjectV2**](ProjectsApi.md#getProjectV2) | **GET** /projects/{owner}/{projectId} | Get project information
[**getUserProjects**](ProjectsApi.md#getUserProjects) | **GET** /projects | Get all projects that a user has access to
[**saveProjectV2**](ProjectsApi.md#saveProjectV2) | **PUT** /projects/{owner}/{projectId} | Update a project
[**updateProjectMembersV2**](ProjectsApi.md#updateProjectMembersV2) | **PUT** /projects/{owner}/{projectId}/members | Update a project&#39;s members list



## addSpecToProjectV2

> addSpecToProjectV2(owner, projectId, specType, name)

Add an API or domain to a project

Use this operation to add a single API or domain to the specified project.  To add multiple APIs or domains at once, use &#x60;PUT /projects/{owner}/{projectId}&#x60;.

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.ProjectsApi();
let owner = "owner_example"; // String | Organization name (case-sensitive)
let projectId = "projectId_example"; // String | Project name (case-sensitive)
let specType = "specType_example"; // String | Definition type - `apis` or `domains`.
let name = "name_example"; // String | The name of an API or domain that you want to add to the project. Case-sensitive.
apiInstance.addSpecToProjectV2(owner, projectId, specType, name, (error, data, response) => {
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
 **owner** | **String**| Organization name (case-sensitive) | 
 **projectId** | **String**| Project name (case-sensitive) | 
 **specType** | **String**| Definition type - &#x60;apis&#x60; or &#x60;domains&#x60;. | 
 **name** | **String**| The name of an API or domain that you want to add to the project. Case-sensitive. | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createProject

> createProject(owner, projectRequest)

Create a project in an organization

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.ProjectsApi();
let owner = "owner_example"; // String | Organization name (case-sensitive)
let projectRequest = new SwaggerHubRegistryApi.Project(); // Project | The project data. Properties that are not provided are set to empty values. 
apiInstance.createProject(owner, projectRequest, (error, data, response) => {
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
 **owner** | **String**| Organization name (case-sensitive) | 
 **projectRequest** | [**Project**](Project.md)| The project data. Properties that are not provided are set to empty values.  | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteProjectV2

> deleteProjectV2(owner, projectId)

Delete a project

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.ProjectsApi();
let owner = "owner_example"; // String | Organization name (case-sensitive)
let projectId = "projectId_example"; // String | Project name (case-sensitive)
apiInstance.deleteProjectV2(owner, projectId, (error, data, response) => {
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
 **owner** | **String**| Organization name (case-sensitive) | 
 **projectId** | **String**| Project name (case-sensitive) | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrgProjectsV2

> ProjectsJson getOrgProjectsV2(owner, opts)

Get all projects of an organization

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.ProjectsApi();
let owner = "owner_example"; // String | Organization name (case-sensitive)
let opts = {
  'nameOnly': false, // Boolean | Return the project information excluding APIs and domains
  'page': 0, // Number | Page to return
  'limit': 10, // Number | Number of results per page (1 .. 100)
  'order': "'ASC'" // String | Sort order
};
apiInstance.getOrgProjectsV2(owner, opts, (error, data, response) => {
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
 **owner** | **String**| Organization name (case-sensitive) | 
 **nameOnly** | **Boolean**| Return the project information excluding APIs and domains | [optional] [default to false]
 **page** | **Number**| Page to return | [optional] [default to 0]
 **limit** | **Number**| Number of results per page (1 .. 100) | [optional] [default to 10]
 **order** | **String**| Sort order | [optional] [default to &#39;ASC&#39;]

### Return type

[**ProjectsJson**](ProjectsJson.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProjectMembersV2

> ProjectMemberList getProjectMembersV2(owner, projectId)

Get project members

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.ProjectsApi();
let owner = "owner_example"; // String | Organization name (case-sensitive)
let projectId = "projectId_example"; // String | Project name (case-sensitive)
apiInstance.getProjectMembersV2(owner, projectId, (error, data, response) => {
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
 **owner** | **String**| Organization name (case-sensitive) | 
 **projectId** | **String**| Project name (case-sensitive) | 

### Return type

[**ProjectMemberList**](ProjectMemberList.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProjectV2

> Project getProjectV2(owner, projectId)

Get project information

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.ProjectsApi();
let owner = "owner_example"; // String | Organization name (case-sensitive)
let projectId = "projectId_example"; // String | Project name (case-sensitive)
apiInstance.getProjectV2(owner, projectId, (error, data, response) => {
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
 **owner** | **String**| Organization name (case-sensitive) | 
 **projectId** | **String**| Project name (case-sensitive) | 

### Return type

[**Project**](Project.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserProjects

> ProjectsJson getUserProjects(opts)

Get all projects that a user has access to

Returns all projects that the authenticating user has access to. Organization owners get a list of all projects in owned organizations. Other members get a list of just the projects they are member of.

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.ProjectsApi();
let opts = {
  'nameOnly': false, // Boolean | Return the project information excluding APIs and domains
  'page': 0, // Number | Page to return
  'limit': 10, // Number | Number of results per page (1 .. 100)
  'sort': "'NAME'", // String | Sort criteria or result set: * NAME * OWNER 
  'order': "'ASC'" // String | Sort order
};
apiInstance.getUserProjects(opts, (error, data, response) => {
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
 **nameOnly** | **Boolean**| Return the project information excluding APIs and domains | [optional] [default to false]
 **page** | **Number**| Page to return | [optional] [default to 0]
 **limit** | **Number**| Number of results per page (1 .. 100) | [optional] [default to 10]
 **sort** | **String**| Sort criteria or result set: * NAME * OWNER  | [optional] [default to &#39;NAME&#39;]
 **order** | **String**| Sort order | [optional] [default to &#39;ASC&#39;]

### Return type

[**ProjectsJson**](ProjectsJson.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## saveProjectV2

> saveProjectV2(owner, projectId, projectRequest)

Update a project

Use this operation to update an existing project, for example, add or remove APIs, or change the project description.  When updating a project, the &#x60;apis&#x60; and &#x60;domains&#x60; lists _replace_ the existing ones. This means that to add new APIs and domains to a project, you need to send the &#x60;apis&#x60; and &#x60;domains&#x60; lists containing both the existing and new APIs and domains.  To add a single API or domain to a project, you can use &#x60;PUT /projects/{owner}/{projectId}/{specType}/{name}&#x60; instead.

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.ProjectsApi();
let owner = "owner_example"; // String | Organization name (case-sensitive)
let projectId = "projectId_example"; // String | Project name (case-sensitive)
let projectRequest = new SwaggerHubRegistryApi.Project(); // Project | The project data. Properties that are not provided are set to empty values. 
apiInstance.saveProjectV2(owner, projectId, projectRequest, (error, data, response) => {
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
 **owner** | **String**| Organization name (case-sensitive) | 
 **projectId** | **String**| Project name (case-sensitive) | 
 **projectRequest** | [**Project**](Project.md)| The project data. Properties that are not provided are set to empty values.  | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateProjectMembersV2

> updateProjectMembersV2(owner, projectId, projectMemberList)

Update a project&#39;s members list

When updating a project, the &#x60;members&#x60; list _replaces_ the existing one. This means that to add new members to a project, you need to send the &#x60;members&#x60; list containing both the existing and new members. 

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.ProjectsApi();
let owner = "owner_example"; // String | Organization name (case-sensitive)
let projectId = "projectId_example"; // String | Project name (case-sensitive)
let projectMemberList = new SwaggerHubRegistryApi.ProjectMemberList(); // ProjectMemberList | A list of users and teams to add to the project
apiInstance.updateProjectMembersV2(owner, projectId, projectMemberList, (error, data, response) => {
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
 **owner** | **String**| Organization name (case-sensitive) | 
 **projectId** | **String**| Project name (case-sensitive) | 
 **projectMemberList** | [**ProjectMemberList**](ProjectMemberList.md)| A list of users and teams to add to the project | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

