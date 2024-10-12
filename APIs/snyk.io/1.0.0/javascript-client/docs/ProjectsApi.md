# SnykApi.ProjectsApi

All URIs are relative to *https://api.snyk.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate**](ProjectsApi.md#activate) | **POST** /org/{orgId}/project/{projectId}/activate | Activate
[**addATagToAProject**](ProjectsApi.md#addATagToAProject) | **POST** /org/{orgId}/project/{projectId}/tags | Add a tag to a project
[**addIgnore**](ProjectsApi.md#addIgnore) | **POST** /org/{orgId}/project/{projectId}/ignore/{issueId} | Add ignore
[**applyingAttributes**](ProjectsApi.md#applyingAttributes) | **POST** /org/{orgId}/project/{projectId}/attributes | Applying attributes
[**createJiraIssue**](ProjectsApi.md#createJiraIssue) | **POST** /org/{orgId}/project/{projectId}/issue/{issueId}/jira-issue | Create jira issue
[**deactivate**](ProjectsApi.md#deactivate) | **POST** /org/{orgId}/project/{projectId}/deactivate | Deactivate
[**deleteAProject**](ProjectsApi.md#deleteAProject) | **DELETE** /org/{orgId}/project/{projectId} | Delete a project
[**deleteIgnores**](ProjectsApi.md#deleteIgnores) | **DELETE** /org/{orgId}/project/{projectId}/ignore/{issueId} | Delete ignores
[**deleteProjectSettings**](ProjectsApi.md#deleteProjectSettings) | **DELETE** /org/{orgId}/project/{projectId}/settings | Delete project settings
[**getProjectDependencyGraph**](ProjectsApi.md#getProjectDependencyGraph) | **GET** /org/{orgId}/project/{projectId}/dep-graph | Get Project dependency graph
[**listAllAggregatedIssues**](ProjectsApi.md#listAllAggregatedIssues) | **POST** /org/{orgId}/project/{projectId}/aggregated-issues | List all Aggregated issues
[**listAllIgnores**](ProjectsApi.md#listAllIgnores) | **GET** /org/{orgId}/project/{projectId}/ignores | List all ignores
[**listAllJiraIssues**](ProjectsApi.md#listAllJiraIssues) | **GET** /org/{orgId}/project/{projectId}/jira-issues | List all jira issues
[**listAllProjectIssuePaths**](ProjectsApi.md#listAllProjectIssuePaths) | **GET** /org/{orgId}/project/{projectId}/issue/{issueId}/paths | List all project issue paths
[**listAllProjectSnapshotAggregatedIssues**](ProjectsApi.md#listAllProjectSnapshotAggregatedIssues) | **POST** /org/{orgId}/project/{projectId}/history/{snapshotId}/aggregated-issues | List all project snapshot aggregated issues
[**listAllProjectSnapshotIssuePaths**](ProjectsApi.md#listAllProjectSnapshotIssuePaths) | **GET** /org/{orgId}/project/{projectId}/history/{snapshotId}/issue/{issueId}/paths | List all project snapshot issue paths
[**listAllProjectSnapshots**](ProjectsApi.md#listAllProjectSnapshots) | **POST** /org/{orgId}/project/{projectId}/history | List all project snapshots
[**listAllProjects**](ProjectsApi.md#listAllProjects) | **POST** /org/{orgId}/projects | List all projects
[**listProjectSettings**](ProjectsApi.md#listProjectSettings) | **GET** /org/{orgId}/project/{projectId}/settings | List project settings
[**moveProjectToADifferentOrganization**](ProjectsApi.md#moveProjectToADifferentOrganization) | **PUT** /org/{orgId}/project/{projectId}/move | Move project to a different organization
[**removeATagFromAProject**](ProjectsApi.md#removeATagFromAProject) | **POST** /org/{orgId}/project/{projectId}/tags/remove | Remove a tag from a project
[**replaceIgnores**](ProjectsApi.md#replaceIgnores) | **PUT** /org/{orgId}/project/{projectId}/ignore/{issueId} | Replace ignores
[**retrieveASingleProject**](ProjectsApi.md#retrieveASingleProject) | **GET** /org/{orgId}/project/{projectId} | Retrieve a single project
[**retrieveIgnore**](ProjectsApi.md#retrieveIgnore) | **GET** /org/{orgId}/project/{projectId}/ignore/{issueId} | Retrieve ignore
[**updateAProject**](ProjectsApi.md#updateAProject) | **PUT** /org/{orgId}/project/{projectId} | Update a project
[**updateProjectSettings**](ProjectsApi.md#updateProjectSettings) | **PUT** /org/{orgId}/project/{projectId}/settings | Update project settings



## activate

> activate(orgId, projectId)

Activate

Activating a project will:  - Add a repository webhook for supported integrations.  - Enable pull request tests for new vulnerabilities.  - Open Fix pull request for newly disclosed vulnerabilities.  - Enable recurring tests, sending email alerts about newly disclosed vulnerabilities.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID the project belongs to. The `API_KEY` must have access to this organization.
let projectId = "463c1ee5-31bc-428c-b451-b79a3270db08"; // String | The project ID.
apiInstance.activate(orgId, projectId, (error, data, response) => {
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
 **orgId** | **String**| The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **projectId** | **String**| The project ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addATagToAProject

> AddATagToAProject200Response addATagToAProject(orgId, projectId, opts)

Add a tag to a project

​

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
let projectId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454545"; // String | The project ID to apply the tag to
let opts = {
  'addATagToAProjectRequest': new SnykApi.AddATagToAProjectRequest() // AddATagToAProjectRequest | 
};
apiInstance.addATagToAProject(orgId, projectId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **projectId** | **String**| The project ID to apply the tag to | 
 **addATagToAProjectRequest** | [**AddATagToAProjectRequest**](AddATagToAProjectRequest.md)|  | [optional] 

### Return type

[**AddATagToAProject200Response**](AddATagToAProject200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## addIgnore

> Object addIgnore(orgId, projectId, issueId, opts)

Add ignore



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "orgId_example"; // String | Automatically added
let projectId = "projectId_example"; // String | Automatically added
let issueId = "issueId_example"; // String | Automatically added
let opts = {
  'addIgnoreRequest': new SnykApi.AddIgnoreRequest() // AddIgnoreRequest | 
};
apiInstance.addIgnore(orgId, projectId, issueId, opts, (error, data, response) => {
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
 **orgId** | **String**| Automatically added | 
 **projectId** | **String**| Automatically added | 
 **issueId** | **String**| Automatically added | 
 **addIgnoreRequest** | [**AddIgnoreRequest**](AddIgnoreRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## applyingAttributes

> ApplyingAttributes200Response applyingAttributes(orgId, projectId, opts)

Applying attributes

Applies an attribute to the provided project. It is possible to assign multiple values to each attribute, but you can only assign values to one of the predefined attribute categories, using the predefined options for this category. Assigning an attribute requires the caller to be either an Organization Administrator or a Group Administrator. Assigning an attribute will override any existing values that the specific attribute already has set. In order to clear out an attribute value, an empty array can be set.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
let projectId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454545"; // String | The project ID to remove a tag from
let opts = {
  'applyingAttributesRequest': new SnykApi.ApplyingAttributesRequest() // ApplyingAttributesRequest | 
};
apiInstance.applyingAttributes(orgId, projectId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **projectId** | **String**| The project ID to remove a tag from | 
 **applyingAttributesRequest** | [**ApplyingAttributesRequest**](ApplyingAttributesRequest.md)|  | [optional] 

### Return type

[**ApplyingAttributes200Response**](ApplyingAttributes200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## createJiraIssue

> CreateJiraIssue200Response createJiraIssue(issueId, orgId, projectId, opts)

Create jira issue



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let issueId = "npm:qs:20140806-1"; // String | The issue ID to create Jira issue for.
let orgId = "orgId_example"; // String | Automatically added
let projectId = "projectId_example"; // String | Automatically added
let opts = {
  'createJiraIssueRequest': new SnykApi.CreateJiraIssueRequest() // CreateJiraIssueRequest | 
};
apiInstance.createJiraIssue(issueId, orgId, projectId, opts, (error, data, response) => {
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
 **issueId** | **String**| The issue ID to create Jira issue for. | 
 **orgId** | **String**| Automatically added | 
 **projectId** | **String**| Automatically added | 
 **createJiraIssueRequest** | [**CreateJiraIssueRequest**](CreateJiraIssueRequest.md)|  | [optional] 

### Return type

[**CreateJiraIssue200Response**](CreateJiraIssue200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## deactivate

> deactivate(orgId, projectId)

Deactivate

Deactivating a project will:  - Disable pull request tests for new vulnerabilities.  - Disable Fix pull request from being opened for newly disclosed vulnerabilities.  - Disable recurring tests - email alerts about newly disclosed vulnerabilities will be turned off.  - If the repository has no other active projects, then remove any webhooks related to the project.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID the project belongs to. The `API_KEY` must have access to this organization.
let projectId = "463c1ee5-31bc-428c-b451-b79a3270db08"; // String | The project ID.
apiInstance.deactivate(orgId, projectId, (error, data, response) => {
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
 **orgId** | **String**| The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **projectId** | **String**| The project ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteAProject

> deleteAProject(orgId, projectId)

Delete a project



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "orgId_example"; // String | Automatically added
let projectId = "projectId_example"; // String | Automatically added
apiInstance.deleteAProject(orgId, projectId, (error, data, response) => {
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
 **orgId** | **String**| Automatically added | 
 **projectId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteIgnores

> deleteIgnores(orgId, projectId, issueId)

Delete ignores



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "orgId_example"; // String | Automatically added
let projectId = "projectId_example"; // String | Automatically added
let issueId = "issueId_example"; // String | Automatically added
apiInstance.deleteIgnores(orgId, projectId, issueId, (error, data, response) => {
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
 **orgId** | **String**| Automatically added | 
 **projectId** | **String**| Automatically added | 
 **issueId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteProjectSettings

> deleteProjectSettings(orgId, projectId)

Delete project settings

Deleting project settings will set the project to inherit default settings from its integration.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "orgId_example"; // String | Automatically added
let projectId = "projectId_example"; // String | Automatically added
apiInstance.deleteProjectSettings(orgId, projectId, (error, data, response) => {
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
 **orgId** | **String**| Automatically added | 
 **projectId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProjectDependencyGraph

> GetProjectDependencyGraph200Response getProjectDependencyGraph(orgId, projectId)

Get Project dependency graph



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
let projectId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454545"; // String | The project ID to return issues for.
apiInstance.getProjectDependencyGraph(orgId, projectId, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **projectId** | **String**| The project ID to return issues for. | 

### Return type

[**GetProjectDependencyGraph200Response**](GetProjectDependencyGraph200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## listAllAggregatedIssues

> ListAllAggregatedIssues200Response listAllAggregatedIssues(orgId, projectId, opts)

List all Aggregated issues



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
let projectId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454545"; // String | The project ID to return issues for.
let opts = {
  'listAllAggregatedIssuesRequest': new SnykApi.ListAllAggregatedIssuesRequest() // ListAllAggregatedIssuesRequest | 
};
apiInstance.listAllAggregatedIssues(orgId, projectId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **projectId** | **String**| The project ID to return issues for. | 
 **listAllAggregatedIssuesRequest** | [**ListAllAggregatedIssuesRequest**](ListAllAggregatedIssuesRequest.md)|  | [optional] 

### Return type

[**ListAllAggregatedIssues200Response**](ListAllAggregatedIssues200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## listAllIgnores

> Object listAllIgnores(orgId, projectId)

List all ignores

Temporary ignores include an &#x60;expires&#x60; attribute, while permanent ignores do not.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to list ignores for. The `API_KEY` must have access to this organization.
let projectId = "463c1ee5-31bc-428c-b451-b79a3270db08"; // String | The project ID to list ignores for.
apiInstance.listAllIgnores(orgId, projectId, (error, data, response) => {
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
 **orgId** | **String**| The organization ID to list ignores for. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **projectId** | **String**| The project ID to list ignores for. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## listAllJiraIssues

> Object listAllJiraIssues(orgId, projectId)

List all jira issues



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to list Jira issues for. The `API_KEY` must have access to this organization.
let projectId = "463c1ee5-31bc-428c-b451-b79a3270db08"; // String | The project ID to list Jira issues for.
apiInstance.listAllJiraIssues(orgId, projectId, (error, data, response) => {
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
 **orgId** | **String**| The organization ID to list Jira issues for. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **projectId** | **String**| The project ID to list Jira issues for. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## listAllProjectIssuePaths

> ListAllProjectSnapshotIssuePaths200Response listAllProjectIssuePaths(orgId, projectId, issueId, opts)

List all project issue paths



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
let projectId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454545"; // String | The project ID for which to return issue paths.
let issueId = "SNYK-JS-LODASH-590103"; // String | The issue ID for which to return issue paths.
let opts = {
  'snapshotId': "6d5813be-7e6d-4ab8-80c2-1e3e2a454553", // String | The project snapshot ID for which to return issue paths. If set to `latest`, the most recent snapshot will be used. Use the \"List all project snapshots\" endpoint to find suitable values for this.
  'perPage': 3, // Number | The number of results to return per page (1 - 1000, inclusive).
  'page': 2 // Number | The page of results to return.
};
apiInstance.listAllProjectIssuePaths(orgId, projectId, issueId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **projectId** | **String**| The project ID for which to return issue paths. | 
 **issueId** | **String**| The issue ID for which to return issue paths. | 
 **snapshotId** | **String**| The project snapshot ID for which to return issue paths. If set to &#x60;latest&#x60;, the most recent snapshot will be used. Use the \&quot;List all project snapshots\&quot; endpoint to find suitable values for this. | [optional] [default to &#39;latest&#39;]
 **perPage** | **Number**| The number of results to return per page (1 - 1000, inclusive). | [optional] [default to 100]
 **page** | **Number**| The page of results to return. | [optional] [default to 1]

### Return type

[**ListAllProjectSnapshotIssuePaths200Response**](ListAllProjectSnapshotIssuePaths200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## listAllProjectSnapshotAggregatedIssues

> ListAllAggregatedIssues200Response listAllProjectSnapshotAggregatedIssues(orgId, projectId, snapshotId, opts)

List all project snapshot aggregated issues



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "2d5c4d0c-c6d6-4658-a703-c2721c135b26"; // String | The organization ID. The `API_KEY` must have access to this organization.
let projectId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454545"; // String | The project ID.
let snapshotId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454553"; // String | The snapshot ID. If set to latest, the most recent snapshot will be used.
let opts = {
  'listAllAggregatedIssuesRequest': new SnykApi.ListAllAggregatedIssuesRequest() // ListAllAggregatedIssuesRequest | 
};
apiInstance.listAllProjectSnapshotAggregatedIssues(orgId, projectId, snapshotId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **projectId** | **String**| The project ID. | 
 **snapshotId** | **String**| The snapshot ID. If set to latest, the most recent snapshot will be used. | 
 **listAllAggregatedIssuesRequest** | [**ListAllAggregatedIssuesRequest**](ListAllAggregatedIssuesRequest.md)|  | [optional] 

### Return type

[**ListAllAggregatedIssues200Response**](ListAllAggregatedIssues200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## listAllProjectSnapshotIssuePaths

> ListAllProjectSnapshotIssuePaths200Response listAllProjectSnapshotIssuePaths(orgId, projectId, snapshotId, issueId, opts)

List all project snapshot issue paths



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
let projectId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454545"; // String | The project ID for which to return issue paths.
let snapshotId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454553"; // String | The project snapshot ID for which to return issue paths. If set to `latest`, the most recent snapshot will be used. Use the \"List all project snapshots\" endpoint to find suitable values for this.
let issueId = "SNYK-JS-LODASH-590103"; // String | The issue ID for which to return issue paths.
let opts = {
  'perPage': 3, // Number | The number of results to return per page (1 - 1000, inclusive).
  'page': 2 // Number | The page of results to return.
};
apiInstance.listAllProjectSnapshotIssuePaths(orgId, projectId, snapshotId, issueId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **projectId** | **String**| The project ID for which to return issue paths. | 
 **snapshotId** | **String**| The project snapshot ID for which to return issue paths. If set to &#x60;latest&#x60;, the most recent snapshot will be used. Use the \&quot;List all project snapshots\&quot; endpoint to find suitable values for this. | 
 **issueId** | **String**| The issue ID for which to return issue paths. | 
 **perPage** | **Number**| The number of results to return per page (1 - 1000, inclusive). | [optional] [default to 100]
 **page** | **Number**| The page of results to return. | [optional] [default to 1]

### Return type

[**ListAllProjectSnapshotIssuePaths200Response**](ListAllProjectSnapshotIssuePaths200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## listAllProjectSnapshots

> ListAllProjectSnapshots200Response listAllProjectSnapshots(orgId, projectId, opts)

List all project snapshots



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
let projectId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454545"; // String | The project ID to return snapshots for.
let opts = {
  'perPage': 10, // Number | The number of results to return (the default is 10, the maximum is 100).
  'page': 1, // Number | The offset from which to start returning results from.
  'listAllProjectSnapshotsRequest': new SnykApi.ListAllProjectSnapshotsRequest() // ListAllProjectSnapshotsRequest | 
};
apiInstance.listAllProjectSnapshots(orgId, projectId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **projectId** | **String**| The project ID to return snapshots for. | 
 **perPage** | **Number**| The number of results to return (the default is 10, the maximum is 100). | [optional] 
 **page** | **Number**| The offset from which to start returning results from. | [optional] 
 **listAllProjectSnapshotsRequest** | [**ListAllProjectSnapshotsRequest**](ListAllProjectSnapshotsRequest.md)|  | [optional] 

### Return type

[**ListAllProjectSnapshots200Response**](ListAllProjectSnapshots200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## listAllProjects

> ListAllProjects200Response listAllProjects(orgId, opts)

List all projects



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to list projects for. The `API_KEY` must have access to this organization.
let opts = {
  'listAllProjectsRequest': new SnykApi.ListAllProjectsRequest() // ListAllProjectsRequest | 
};
apiInstance.listAllProjects(orgId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID to list projects for. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **listAllProjectsRequest** | [**ListAllProjectsRequest**](ListAllProjectsRequest.md)|  | [optional] 

### Return type

[**ListAllProjects200Response**](ListAllProjects200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## listProjectSettings

> ListProjectSettings200Response listProjectSettings(orgId, projectId)

List project settings



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to which the project belongs. The API_KEY must have access to this organization.
let projectId = "463c1ee5-31bc-428c-b451-b79a3270db08"; // String | The project ID
apiInstance.listProjectSettings(orgId, projectId, (error, data, response) => {
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
 **orgId** | **String**| The organization ID to which the project belongs. The API_KEY must have access to this organization. | 
 **projectId** | **String**| The project ID | 

### Return type

[**ListProjectSettings200Response**](ListProjectSettings200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## moveProjectToADifferentOrganization

> moveProjectToADifferentOrganization(orgId, projectId, opts)

Move project to a different organization

Note: when moving a project to a new organization, the historical data used for reporting does not move with it.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to which the project belongs. The API_KEY must have group admin permissions. If the project is moved to a new group, a personal level API key is needed.
let projectId = "463c1ee5-31bc-428c-b451-b79a3270db08"; // String | The project ID.
let opts = {
  'moveProjectToADifferentOrganizationRequest': new SnykApi.MoveProjectToADifferentOrganizationRequest() // MoveProjectToADifferentOrganizationRequest | 
};
apiInstance.moveProjectToADifferentOrganization(orgId, projectId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID to which the project belongs. The API_KEY must have group admin permissions. If the project is moved to a new group, a personal level API key is needed. | 
 **projectId** | **String**| The project ID. | 
 **moveProjectToADifferentOrganizationRequest** | [**MoveProjectToADifferentOrganizationRequest**](MoveProjectToADifferentOrganizationRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## removeATagFromAProject

> AddATagToAProject200Response removeATagFromAProject(orgId, projectId, opts)

Remove a tag from a project



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
let projectId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454545"; // String | The project ID to remove a tag from
let opts = {
  'addATagToAProjectRequest': new SnykApi.AddATagToAProjectRequest() // AddATagToAProjectRequest | 
};
apiInstance.removeATagFromAProject(orgId, projectId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **projectId** | **String**| The project ID to remove a tag from | 
 **addATagToAProjectRequest** | [**AddATagToAProjectRequest**](AddATagToAProjectRequest.md)|  | [optional] 

### Return type

[**AddATagToAProject200Response**](AddATagToAProject200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## replaceIgnores

> [Object] replaceIgnores(orgId, projectId, issueId)

Replace ignores



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "orgId_example"; // String | Automatically added
let projectId = "projectId_example"; // String | Automatically added
let issueId = "issueId_example"; // String | Automatically added
apiInstance.replaceIgnores(orgId, projectId, issueId, (error, data, response) => {
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
 **orgId** | **String**| Automatically added | 
 **projectId** | **String**| Automatically added | 
 **issueId** | **String**| Automatically added | 

### Return type

**[Object]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## retrieveASingleProject

> RetrieveASingleProject200Response retrieveASingleProject(orgId, projectId)

Retrieve a single project



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID the project belongs to. The `API_KEY` must have access to this organization.
let projectId = "463c1ee5-31bc-428c-b451-b79a3270db08"; // String | The project ID.
apiInstance.retrieveASingleProject(orgId, projectId, (error, data, response) => {
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
 **orgId** | **String**| The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **projectId** | **String**| The project ID. | 

### Return type

[**RetrieveASingleProject200Response**](RetrieveASingleProject200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## retrieveIgnore

> Object retrieveIgnore(orgId, projectId, issueId)

Retrieve ignore



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to modify ignores for. The `API_KEY` must have access to this organization.
let projectId = "463c1ee5-31bc-428c-b451-b79a3270db08"; // String | The project ID to modify ignores for.
let issueId = "npm:qs:20140806-1"; // String | The issue ID to modify ignores for. Can be a vulnerability or a license Issue.
apiInstance.retrieveIgnore(orgId, projectId, issueId, (error, data, response) => {
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
 **orgId** | **String**| The organization ID to modify ignores for. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **projectId** | **String**| The project ID to modify ignores for. | 
 **issueId** | **String**| The issue ID to modify ignores for. Can be a vulnerability or a license Issue. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## updateAProject

> RetrieveASingleProject200Response updateAProject(orgId, projectId, opts)

Update a project



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "orgId_example"; // String | Automatically added
let projectId = "projectId_example"; // String | Automatically added
let opts = {
  'updateAProjectRequest': new SnykApi.UpdateAProjectRequest() // UpdateAProjectRequest | 
};
apiInstance.updateAProject(orgId, projectId, opts, (error, data, response) => {
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
 **orgId** | **String**| Automatically added | 
 **projectId** | **String**| Automatically added | 
 **updateAProjectRequest** | [**UpdateAProjectRequest**](UpdateAProjectRequest.md)|  | [optional] 

### Return type

[**RetrieveASingleProject200Response**](RetrieveASingleProject200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## updateProjectSettings

> ListProjectSettings200Response updateProjectSettings(orgId, projectId, opts)

Update project settings



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ProjectsApi();
let orgId = "orgId_example"; // String | Automatically added
let projectId = "projectId_example"; // String | Automatically added
let opts = {
  'updateProjectSettingsRequest': new SnykApi.UpdateProjectSettingsRequest() // UpdateProjectSettingsRequest | 
};
apiInstance.updateProjectSettings(orgId, projectId, opts, (error, data, response) => {
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
 **orgId** | **String**| Automatically added | 
 **projectId** | **String**| Automatically added | 
 **updateProjectSettingsRequest** | [**UpdateProjectSettingsRequest**](UpdateProjectSettingsRequest.md)|  | [optional] 

### Return type

[**ListProjectSettings200Response**](ListProjectSettings200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8

