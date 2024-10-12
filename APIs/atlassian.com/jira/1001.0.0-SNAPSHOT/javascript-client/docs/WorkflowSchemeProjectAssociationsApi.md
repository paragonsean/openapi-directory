# TheJiraCloudPlatformRestApi.WorkflowSchemeProjectAssociationsApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignSchemeToProject**](WorkflowSchemeProjectAssociationsApi.md#assignSchemeToProject) | **PUT** /rest/api/3/workflowscheme/project | Assign workflow scheme to project
[**getWorkflowSchemeProjectAssociations**](WorkflowSchemeProjectAssociationsApi.md#getWorkflowSchemeProjectAssociations) | **GET** /rest/api/3/workflowscheme/project | Get workflow scheme project associations



## assignSchemeToProject

> Object assignSchemeToProject(workflowSchemeProjectAssociation)

Assign workflow scheme to project

Assigns a workflow scheme to a project. This operation is performed only when there are no issues in the project.  Workflow schemes can only be assigned to classic projects.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.WorkflowSchemeProjectAssociationsApi();
let workflowSchemeProjectAssociation = {"projectId":"10001","workflowSchemeId":"10032"}; // WorkflowSchemeProjectAssociation | 
apiInstance.assignSchemeToProject(workflowSchemeProjectAssociation, (error, data, response) => {
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
 **workflowSchemeProjectAssociation** | [**WorkflowSchemeProjectAssociation**](WorkflowSchemeProjectAssociation.md)|  | 

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getWorkflowSchemeProjectAssociations

> ContainerOfWorkflowSchemeAssociations getWorkflowSchemeProjectAssociations(projectId)

Get workflow scheme project associations

Returns a list of the workflow schemes associated with a list of projects. Each returned workflow scheme includes a list of the requested projects associated with it. Any team-managed or non-existent projects in the request are ignored and no errors are returned.  If the project is associated with the &#x60;Default Workflow Scheme&#x60; no ID is returned. This is because the way the &#x60;Default Workflow Scheme&#x60; is stored means it has no ID.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.WorkflowSchemeProjectAssociationsApi();
let projectId = [10010]; // [Number] | The ID of a project to return the workflow schemes for. To include multiple projects, provide an ampersand-Jim: oneseparated list. For example, `projectId=10000&projectId=10001`.
apiInstance.getWorkflowSchemeProjectAssociations(projectId, (error, data, response) => {
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
 **projectId** | [**[Number]**](Number.md)| The ID of a project to return the workflow schemes for. To include multiple projects, provide an ampersand-Jim: oneseparated list. For example, &#x60;projectId&#x3D;10000&amp;projectId&#x3D;10001&#x60;. | 

### Return type

[**ContainerOfWorkflowSchemeAssociations**](ContainerOfWorkflowSchemeAssociations.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

