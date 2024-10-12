# IllumiDesk.ProjectsApi

All URIs are relative to *https://api.illumidesk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectCopy**](ProjectsApi.md#projectCopy) | **POST** /v1/{namespace}/projects/project-copy/ | Copy a project to your own account.
[**projectCopyCheck**](ProjectsApi.md#projectCopyCheck) | **HEAD** /v1/{namespace}/projects/project-copy-check/ | Check if you are able to copy a project to your account.
[**projectsCollaboratorsCreate**](ProjectsApi.md#projectsCollaboratorsCreate) | **POST** /v1/{namespace}/projects/{project}/collaborators/ | Create project collaborators
[**projectsCollaboratorsDelete**](ProjectsApi.md#projectsCollaboratorsDelete) | **DELETE** /v1/{namespace}/projects/{project}/collaborators/{collaborator}/ | Delete a project collaborator
[**projectsCollaboratorsList**](ProjectsApi.md#projectsCollaboratorsList) | **GET** /v1/{namespace}/projects/{project}/collaborators/ | Get project collaborators
[**projectsCollaboratorsRead**](ProjectsApi.md#projectsCollaboratorsRead) | **GET** /v1/{namespace}/projects/{project}/collaborators/{collaborator}/ | Get a project collaborator
[**projectsCollaboratorsUpdate**](ProjectsApi.md#projectsCollaboratorsUpdate) | **PATCH** /v1/{namespace}/projects/{project}/collaborators/{collaborator}/ | Update project collaborator
[**projectsCreate**](ProjectsApi.md#projectsCreate) | **POST** /v1/{namespace}/projects/ | Create a new project
[**projectsDelete**](ProjectsApi.md#projectsDelete) | **DELETE** /v1/{namespace}/projects/{project}/ | Delete a project
[**projectsDeploymentDelete**](ProjectsApi.md#projectsDeploymentDelete) | **DELETE** /v1/{namespace}/projects/{project}/deployments/{deployment}/ | Delete a deployment
[**projectsDeploymentsCreate**](ProjectsApi.md#projectsDeploymentsCreate) | **POST** /v1/{namespace}/projects/{project}/deployments/ | Create a new deployment
[**projectsDeploymentsDeploy**](ProjectsApi.md#projectsDeploymentsDeploy) | **POST** /v1/{namespace}/projects/{project}/deployments/{deployment}/deploy/ | Deploy an existing model
[**projectsDeploymentsList**](ProjectsApi.md#projectsDeploymentsList) | **GET** /v1/{namespace}/projects/{project}/deployments/ | Retrieve deployments
[**projectsDeploymentsRead**](ProjectsApi.md#projectsDeploymentsRead) | **GET** /v1/{namespace}/projects/{project}/deployments/{deployment}/ | Retrieve a deployment
[**projectsDeploymentsReplace**](ProjectsApi.md#projectsDeploymentsReplace) | **PUT** /v1/{namespace}/projects/{project}/deployments/{deployment}/ | Replace a deployment
[**projectsDeploymentsUpdate**](ProjectsApi.md#projectsDeploymentsUpdate) | **PATCH** /v1/{namespace}/projects/{project}/deployments/{deployment}/ | Update a deployment
[**projectsList**](ProjectsApi.md#projectsList) | **GET** /v1/{namespace}/projects/ | Get available projects
[**projectsProjectFilesCreate**](ProjectsApi.md#projectsProjectFilesCreate) | **POST** /v1/{namespace}/projects/{project}/project_files/ | Create project files
[**projectsProjectFilesDelete**](ProjectsApi.md#projectsProjectFilesDelete) | **DELETE** /v1/{namespace}/projects/{project}/project_files/{id}/ | Delete a project file
[**projectsProjectFilesList**](ProjectsApi.md#projectsProjectFilesList) | **GET** /v1/{namespace}/projects/{project}/project_files/ | Get project files
[**projectsProjectFilesRead**](ProjectsApi.md#projectsProjectFilesRead) | **GET** /v1/{namespace}/projects/{project}/project_files/{id}/ | Get a project file
[**projectsProjectFilesReplace**](ProjectsApi.md#projectsProjectFilesReplace) | **PUT** /v1/{namespace}/projects/{project}/project_files/{id}/ | Replace a project file
[**projectsProjectFilesUpdate**](ProjectsApi.md#projectsProjectFilesUpdate) | **PATCH** /v1/{namespace}/projects/{project}/project_files/{id}/ | Update a project file
[**projectsRead**](ProjectsApi.md#projectsRead) | **GET** /v1/{namespace}/projects/{project}/ | Get a project
[**projectsReplace**](ProjectsApi.md#projectsReplace) | **PUT** /v1/{namespace}/projects/{project}/ | Replace a project
[**projectsServersApiKey**](ProjectsApi.md#projectsServersApiKey) | **GET** /v1/{namespace}/projects/{project}/servers/{server}/api-key/ | Get server API key
[**projectsServersAuth**](ProjectsApi.md#projectsServersAuth) | **POST** /v1/{namespace}/projects/{project}/servers/{server}/auth/ | Server api key validation
[**projectsServersCreate**](ProjectsApi.md#projectsServersCreate) | **POST** /v1/{namespace}/projects/{project}/servers/ | Create a new server
[**projectsServersDelete**](ProjectsApi.md#projectsServersDelete) | **DELETE** /v1/{namespace}/projects/{project}/servers/{server}/ | Delete a server
[**projectsServersList**](ProjectsApi.md#projectsServersList) | **GET** /v1/{namespace}/projects/{project}/servers/ | Retrieve servers
[**projectsServersRead**](ProjectsApi.md#projectsServersRead) | **GET** /v1/{namespace}/projects/{project}/servers/{server}/ | Retrieve a server
[**projectsServersReplace**](ProjectsApi.md#projectsServersReplace) | **PUT** /v1/{namespace}/projects/{project}/servers/{server}/ | Replace a server
[**projectsServersRunStatsCreate**](ProjectsApi.md#projectsServersRunStatsCreate) | **POST** /v1/{namespace}/projects/{project}/servers/{server}/run-stats/ | Create a new server&#39;s run statistics
[**projectsServersRunStatsDelete**](ProjectsApi.md#projectsServersRunStatsDelete) | **DELETE** /v1/{namespace}/projects/{project}/servers/{server}/run-stats/{id}/ | Delete a server&#39;s statistics
[**projectsServersRunStatsRead**](ProjectsApi.md#projectsServersRunStatsRead) | **GET** /v1/{namespace}/projects/{project}/servers/{server}/run-stats/{id}/ | Retrieve statistics for a server
[**projectsServersRunStatsReplace**](ProjectsApi.md#projectsServersRunStatsReplace) | **PUT** /v1/{namespace}/projects/{project}/servers/{server}/run-stats/{id}/ | Replace a server&#39;s statistics
[**projectsServersRunStatsUpdate**](ProjectsApi.md#projectsServersRunStatsUpdate) | **PATCH** /v1/{namespace}/projects/{project}/servers/{server}/run-stats/{id}/ | Update a server&#39;s statistics
[**projectsServersSshTunnelsCreate**](ProjectsApi.md#projectsServersSshTunnelsCreate) | **POST** /v1/{namespace}/projects/{project}/servers/{server}/ssh-tunnels/ | Create SSH Tunnel associated to a server
[**projectsServersSshTunnelsDelete**](ProjectsApi.md#projectsServersSshTunnelsDelete) | **DELETE** /v1/{namespace}/projects/{project}/servers/{server}/ssh-tunnels/{tunnel}/ | Delete an SSH Tunnel associated to a server
[**projectsServersSshTunnelsList**](ProjectsApi.md#projectsServersSshTunnelsList) | **GET** /v1/{namespace}/projects/{project}/servers/{server}/ssh-tunnels/ | Get SSH Tunnels associated to a server
[**projectsServersSshTunnelsRead**](ProjectsApi.md#projectsServersSshTunnelsRead) | **GET** /v1/{namespace}/projects/{project}/servers/{server}/ssh-tunnels/{tunnel}/ | Get an SSH Tunnel associated to a server
[**projectsServersSshTunnelsReplace**](ProjectsApi.md#projectsServersSshTunnelsReplace) | **PUT** /v1/{namespace}/projects/{project}/servers/{server}/ssh-tunnels/{tunnel}/ | Replace SSH Tunnel associated to a server
[**projectsServersSshTunnelsUpdate**](ProjectsApi.md#projectsServersSshTunnelsUpdate) | **PATCH** /v1/{namespace}/projects/{project}/servers/{server}/ssh-tunnels/{tunnel}/ | Update an SSH Tunnel associated to a server
[**projectsServersStart**](ProjectsApi.md#projectsServersStart) | **POST** /v1/{namespace}/projects/{project}/servers/{server}/start/ | Start a server
[**projectsServersStatsDelete**](ProjectsApi.md#projectsServersStatsDelete) | **DELETE** /v1/{namespace}/projects/{project}/servers/{server}/stats/{id}/ | Delete a server&#39;s statistics
[**projectsServersStatsRead**](ProjectsApi.md#projectsServersStatsRead) | **GET** /v1/{namespace}/projects/{project}/servers/{server}/stats/{id}/ | Retrieve a server&#39;s statistics
[**projectsServersStatsReplace**](ProjectsApi.md#projectsServersStatsReplace) | **PUT** /v1/{namespace}/projects/{project}/servers/{server}/stats/{id}/ | Replace a server&#39;s statistics
[**projectsServersStatsUpdate**](ProjectsApi.md#projectsServersStatsUpdate) | **PATCH** /v1/{namespace}/projects/{project}/servers/{server}/stats/{id}/ | Update a server&#39;s statistics
[**projectsServersStatuses**](ProjectsApi.md#projectsServersStatuses) | **GET** /v1/{namespace}/projects/{project}/servers/statuses/ | Retrieve server statuses
[**projectsServersStop**](ProjectsApi.md#projectsServersStop) | **POST** /v1/{namespace}/projects/{project}/servers/{server}/stop/ | Stop a server
[**projectsServersUpdate**](ProjectsApi.md#projectsServersUpdate) | **PATCH** /v1/{namespace}/projects/{project}/servers/{server}/ | Update a server
[**projectsUpdate**](ProjectsApi.md#projectsUpdate) | **PATCH** /v1/{namespace}/projects/{project}/ | Update a project
[**serviceTriggerCreate**](ProjectsApi.md#serviceTriggerCreate) | **POST** /v1/{namespace}/projects/{project}/servers/{server}/triggers/ | Create a new server trigger
[**serviceTriggerDelete**](ProjectsApi.md#serviceTriggerDelete) | **DELETE** /v1/{namespace}/projects/{project}/servers/{server}/triggers/{trigger}/ | Delete a server trigger
[**serviceTriggerList**](ProjectsApi.md#serviceTriggerList) | **GET** /v1/{namespace}/projects/{project}/servers/{server}/triggers/ | Retrieve server triggers
[**serviceTriggerRead**](ProjectsApi.md#serviceTriggerRead) | **GET** /v1/{namespace}/projects/{project}/servers/{server}/triggers/{trigger}/ | Get a server trigger
[**serviceTriggerReplace**](ProjectsApi.md#serviceTriggerReplace) | **PUT** /v1/{namespace}/projects/{project}/servers/{server}/triggers/{trigger}/ | Replace a server trigger
[**serviceTriggerUpdate**](ProjectsApi.md#serviceTriggerUpdate) | **PATCH** /v1/{namespace}/projects/{project}/servers/{server}/triggers/{trigger}/ | Update a server trigger



## projectCopy

> Project projectCopy(namespace, projectCopyData)

Copy a project to your own account.

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let namespace = "namespace_example"; // String | User or team name.
let projectCopyData = new IllumiDesk.ProjectCopyRequest(); // ProjectCopyRequest | 
apiInstance.projectCopy(namespace, projectCopyData, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **projectCopyData** | [**ProjectCopyRequest**](ProjectCopyRequest.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## projectCopyCheck

> projectCopyCheck(namespace, projectCopyData)

Check if you are able to copy a project to your account.

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let namespace = "namespace_example"; // String | User or team name.
let projectCopyData = new IllumiDesk.ProjectCopyCheckRequest(); // ProjectCopyCheckRequest | 
apiInstance.projectCopyCheck(namespace, projectCopyData, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **projectCopyData** | [**ProjectCopyCheckRequest**](ProjectCopyCheckRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## projectsCollaboratorsCreate

> Collaborator projectsCollaboratorsCreate(project, namespace, opts)

Create project collaborators

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'collaboratorData': new IllumiDesk.CollaboratorData() // CollaboratorData | 
};
apiInstance.projectsCollaboratorsCreate(project, namespace, opts, (error, data, response) => {
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
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **collaboratorData** | [**CollaboratorData**](CollaboratorData.md)|  | [optional] 

### Return type

[**Collaborator**](Collaborator.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## projectsCollaboratorsDelete

> projectsCollaboratorsDelete(project, namespace, collaborator)

Delete a project collaborator

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifier.
let namespace = "namespace_example"; // String | User or team name.
let collaborator = "collaborator_example"; // String | Collaborator unique identifier.
apiInstance.projectsCollaboratorsDelete(project, namespace, collaborator, (error, data, response) => {
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
 **project** | **String**| Project unique identifier. | 
 **namespace** | **String**| User or team name. | 
 **collaborator** | **String**| Collaborator unique identifier. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsCollaboratorsList

> [Collaborator] projectsCollaboratorsList(project, namespace, opts)

Get project collaborators

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'limit': "limit_example", // String | Limit when retrieving items.
  'offset': "offset_example", // String | Offset when retrieving items.
  'ordering': "ordering_example" // String | Ordering when retrieving items.
};
apiInstance.projectsCollaboratorsList(project, namespace, opts, (error, data, response) => {
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
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **limit** | **String**| Limit when retrieving items. | [optional] 
 **offset** | **String**| Offset when retrieving items. | [optional] 
 **ordering** | **String**| Ordering when retrieving items. | [optional] 

### Return type

[**[Collaborator]**](Collaborator.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsCollaboratorsRead

> Collaborator projectsCollaboratorsRead(project, namespace, collaborator)

Get a project collaborator

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifier.
let namespace = "namespace_example"; // String | User or team name.
let collaborator = "collaborator_example"; // String | Collaborator unique identifier expressed as UUID or name.
apiInstance.projectsCollaboratorsRead(project, namespace, collaborator, (error, data, response) => {
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
 **project** | **String**| Project unique identifier. | 
 **namespace** | **String**| User or team name. | 
 **collaborator** | **String**| Collaborator unique identifier expressed as UUID or name. | 

### Return type

[**Collaborator**](Collaborator.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsCollaboratorsUpdate

> Collaborator projectsCollaboratorsUpdate(project, namespace, collaborator, opts)

Update project collaborator

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | 
let namespace = "namespace_example"; // String | User or team name.
let collaborator = "collaborator_example"; // String | 
let opts = {
  'collaboratorData': new IllumiDesk.CollaboratorData() // CollaboratorData | 
};
apiInstance.projectsCollaboratorsUpdate(project, namespace, collaborator, opts, (error, data, response) => {
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
 **project** | **String**|  | 
 **namespace** | **String**| User or team name. | 
 **collaborator** | **String**|  | 
 **collaboratorData** | [**CollaboratorData**](CollaboratorData.md)|  | [optional] 

### Return type

[**Collaborator**](Collaborator.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## projectsCreate

> Project projectsCreate(namespace, opts)

Create a new project

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'projectData': new IllumiDesk.ProjectData() // ProjectData | 
};
apiInstance.projectsCreate(namespace, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **projectData** | [**ProjectData**](ProjectData.md)|  | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## projectsDelete

> projectsDelete(namespace, project)

Delete a project

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let namespace = "namespace_example"; // String | User or team name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
apiInstance.projectsDelete(namespace, project, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsDeploymentDelete

> projectsDeploymentDelete(project, namespace, deployment)

Delete a deployment

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifier.
let namespace = "namespace_example"; // String | User or team name.
let deployment = "deployment_example"; // String | User unique identifier.
apiInstance.projectsDeploymentDelete(project, namespace, deployment, (error, data, response) => {
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
 **project** | **String**| Project unique identifier. | 
 **namespace** | **String**| User or team name. | 
 **deployment** | **String**| User unique identifier. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsDeploymentsCreate

> Deployment projectsDeploymentsCreate(project, namespace, opts)

Create a new deployment

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifer expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'deploymentData': new IllumiDesk.DeploymentData() // DeploymentData | 
};
apiInstance.projectsDeploymentsCreate(project, namespace, opts, (error, data, response) => {
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
 **project** | **String**| Project unique identifer expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **deploymentData** | [**DeploymentData**](DeploymentData.md)|  | [optional] 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## projectsDeploymentsDeploy

> projectsDeploymentsDeploy(project, namespace, deployment)

Deploy an existing model

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let deployment = "deployment_example"; // String | Deployment unique identifier expressed as UUID or name.
apiInstance.projectsDeploymentsDeploy(project, namespace, deployment, (error, data, response) => {
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
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **deployment** | **String**| Deployment unique identifier expressed as UUID or name. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## projectsDeploymentsList

> [Deployment] projectsDeploymentsList(project, namespace, opts)

Retrieve deployments

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'limit': "limit_example", // String | Limit results when getting deployment list.
  'offset': "offset_example", // String | Offset results when getting deployment list.
  'name': "name_example", // String | Server name.
  'ordering': "ordering_example" // String | Ordering option when getting deployment list.
};
apiInstance.projectsDeploymentsList(project, namespace, opts, (error, data, response) => {
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
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **limit** | **String**| Limit results when getting deployment list. | [optional] 
 **offset** | **String**| Offset results when getting deployment list. | [optional] 
 **name** | **String**| Server name. | [optional] 
 **ordering** | **String**| Ordering option when getting deployment list. | [optional] 

### Return type

[**[Deployment]**](Deployment.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsDeploymentsRead

> Deployment projectsDeploymentsRead(project, namespace, deployment)

Retrieve a deployment

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let deployment = "deployment_example"; // String | Deployment unique identifier expressed as UUID or name.
apiInstance.projectsDeploymentsRead(project, namespace, deployment, (error, data, response) => {
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
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **deployment** | **String**| Deployment unique identifier expressed as UUID or name. | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsDeploymentsReplace

> Deployment projectsDeploymentsReplace(project, namespace, deployment, opts)

Replace a deployment

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let deployment = "deployment_example"; // String | Deployment unique identifier expressed as UUID or name.
let opts = {
  'deploymentData': new IllumiDesk.DeploymentData() // DeploymentData | 
};
apiInstance.projectsDeploymentsReplace(project, namespace, deployment, opts, (error, data, response) => {
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
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **deployment** | **String**| Deployment unique identifier expressed as UUID or name. | 
 **deploymentData** | [**DeploymentData**](DeploymentData.md)|  | [optional] 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## projectsDeploymentsUpdate

> Deployment projectsDeploymentsUpdate(project, namespace, deployment, opts)

Update a deployment

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let deployment = "deployment_example"; // String | Deployment unique identifier expressed as UUID or name.
let opts = {
  'deploymentData': new IllumiDesk.DeploymentData() // DeploymentData | 
};
apiInstance.projectsDeploymentsUpdate(project, namespace, deployment, opts, (error, data, response) => {
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
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **deployment** | **String**| Deployment unique identifier expressed as UUID or name. | 
 **deploymentData** | [**DeploymentData**](DeploymentData.md)|  | [optional] 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## projectsList

> [Project] projectsList(namespace, opts)

Get available projects

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'limit': "limit_example", // String | Limit when getting data.
  'offset': "offset_example", // String | Offset when getting data.
  '_private': "_private_example", // String | Private project or public project.
  'name': "name_example", // String | Project name.
  'ordering': "ordering_example" // String | Ordering when getting projects.
};
apiInstance.projectsList(namespace, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **limit** | **String**| Limit when getting data. | [optional] 
 **offset** | **String**| Offset when getting data. | [optional] 
 **_private** | **String**| Private project or public project. | [optional] 
 **name** | **String**| Project name. | [optional] 
 **ordering** | **String**| Ordering when getting projects. | [optional] 

### Return type

[**[Project]**](Project.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsProjectFilesCreate

> ProjectFile projectsProjectFilesCreate(project, namespace, opts)

Create project files

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifier.
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'file': "/path/to/file", // File | File to send, to create new file. This parameter is only used with form data and may include multiple files.
  'base64Data': "base64Data_example", // String | Fila data, represented as base64.
  'name': "name_example", // String | File name. May include path when creating file with base64 field.
  'path': "path_example" // String | File path. Defaults to (/).
};
apiInstance.projectsProjectFilesCreate(project, namespace, opts, (error, data, response) => {
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
 **project** | **String**| Project unique identifier. | 
 **namespace** | **String**| User or team name. | 
 **file** | **File**| File to send, to create new file. This parameter is only used with form data and may include multiple files. | [optional] 
 **base64Data** | **String**| Fila data, represented as base64. | [optional] 
 **name** | **String**| File name. May include path when creating file with base64 field. | [optional] 
 **path** | **String**| File path. Defaults to (/). | [optional] 

### Return type

[**ProjectFile**](ProjectFile.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: multipart/form-data, application/json
- **Accept**: application/json, text/html


## projectsProjectFilesDelete

> projectsProjectFilesDelete(project, namespace, id)

Delete a project file

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifer.
let namespace = "namespace_example"; // String | User or team name.
let id = "id_example"; // String | File unique identifier.
apiInstance.projectsProjectFilesDelete(project, namespace, id, (error, data, response) => {
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
 **project** | **String**| Project unique identifer. | 
 **namespace** | **String**| User or team name. | 
 **id** | **String**| File unique identifier. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsProjectFilesList

> [ProjectFile] projectsProjectFilesList(project, namespace, opts)

Get project files

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Unique identifier for project file expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'limit': "limit_example", // String | Limit when getting project file list.
  'offset': "offset_example", // String | Offset when getting project file list.
  'ordering': "ordering_example", // String | Ordering of list values when getting project file list.
  'filename': "filename_example", // String | Exact file name, relative to the project root. If no such file is found, an empty list will be returned.
  'content': "content_example" // String | Determines whether or not content is returned as base64. Defaults to false.
};
apiInstance.projectsProjectFilesList(project, namespace, opts, (error, data, response) => {
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
 **project** | **String**| Unique identifier for project file expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **limit** | **String**| Limit when getting project file list. | [optional] 
 **offset** | **String**| Offset when getting project file list. | [optional] 
 **ordering** | **String**| Ordering of list values when getting project file list. | [optional] 
 **filename** | **String**| Exact file name, relative to the project root. If no such file is found, an empty list will be returned. | [optional] 
 **content** | **String**| Determines whether or not content is returned as base64. Defaults to false. | [optional] 

### Return type

[**[ProjectFile]**](ProjectFile.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsProjectFilesRead

> ProjectFile projectsProjectFilesRead(project, namespace, id, opts)

Get a project file

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifer.
let namespace = "namespace_example"; // String | User or team name.
let id = "id_example"; // String | File unique identifier.
let opts = {
  'content': "content_example" // String | Determines whether or not content is returned as base64. Defaults to false.
};
apiInstance.projectsProjectFilesRead(project, namespace, id, opts, (error, data, response) => {
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
 **project** | **String**| Project unique identifer. | 
 **namespace** | **String**| User or team name. | 
 **id** | **String**| File unique identifier. | 
 **content** | **String**| Determines whether or not content is returned as base64. Defaults to false. | [optional] 

### Return type

[**ProjectFile**](ProjectFile.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsProjectFilesReplace

> ProjectFile projectsProjectFilesReplace(project, namespace, id, opts)

Replace a project file

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifer.
let namespace = "namespace_example"; // String | User or team name.
let id = "id_example"; // String | File unique identifier.
let opts = {
  'file': "/path/to/file", // File | File to send, to create new file. This parameter is only used with form data and may include multiple files.
  'base64Data': "base64Data_example", // String | Fila data, represented as base64.
  'name': "name_example", // String | File name. May include path when creating file with base64 field.
  'path': "path_example" // String | File path. Defaults to (/).
};
apiInstance.projectsProjectFilesReplace(project, namespace, id, opts, (error, data, response) => {
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
 **project** | **String**| Project unique identifer. | 
 **namespace** | **String**| User or team name. | 
 **id** | **String**| File unique identifier. | 
 **file** | **File**| File to send, to create new file. This parameter is only used with form data and may include multiple files. | [optional] 
 **base64Data** | **String**| Fila data, represented as base64. | [optional] 
 **name** | **String**| File name. May include path when creating file with base64 field. | [optional] 
 **path** | **String**| File path. Defaults to (/). | [optional] 

### Return type

[**ProjectFile**](ProjectFile.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, text/html


## projectsProjectFilesUpdate

> ProjectFile projectsProjectFilesUpdate(project, namespace, id, opts)

Update a project file

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifer.
let namespace = "namespace_example"; // String | User or team name.
let id = "id_example"; // String | File unique identifier.
let opts = {
  'file': "/path/to/file", // File | File to send, to create new file. This parameter is only used with form data and may include multiple files.
  'base64Data': "base64Data_example", // String | Fila data, represented as base64.
  'name': "name_example", // String | File name. May include path when creating file with base64 field.
  'path': "path_example" // String | File path. Defaults to (/).
};
apiInstance.projectsProjectFilesUpdate(project, namespace, id, opts, (error, data, response) => {
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
 **project** | **String**| Project unique identifer. | 
 **namespace** | **String**| User or team name. | 
 **id** | **String**| File unique identifier. | 
 **file** | **File**| File to send, to create new file. This parameter is only used with form data and may include multiple files. | [optional] 
 **base64Data** | **String**| Fila data, represented as base64. | [optional] 
 **name** | **String**| File name. May include path when creating file with base64 field. | [optional] 
 **path** | **String**| File path. Defaults to (/). | [optional] 

### Return type

[**ProjectFile**](ProjectFile.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, text/html


## projectsRead

> Project projectsRead(namespace, project)

Get a project

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let namespace = "namespace_example"; // String | User or team name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
apiInstance.projectsRead(namespace, project, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 

### Return type

[**Project**](Project.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsReplace

> Project projectsReplace(namespace, project, opts)

Replace a project

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let namespace = "namespace_example"; // String | User or team namespace.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let opts = {
  'projectData': new IllumiDesk.ProjectData() // ProjectData | 
};
apiInstance.projectsReplace(namespace, project, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team namespace. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **projectData** | [**ProjectData**](ProjectData.md)|  | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## projectsServersApiKey

> JWT projectsServersApiKey(project, namespace, server)

Get server API key

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
apiInstance.projectsServersApiKey(project, namespace, server, (error, data, response) => {
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
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **server** | **String**| Server unique identifier expressed as UUID or name. | 

### Return type

[**JWT**](JWT.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsServersAuth

> projectsServersAuth(project, namespace, server)

Server api key validation

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
apiInstance.projectsServersAuth(project, namespace, server, (error, data, response) => {
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
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **server** | **String**| Server unique identifier expressed as UUID or name. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## projectsServersCreate

> Server projectsServersCreate(project, namespace, opts)

Create a new server

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifer expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'serverData': new IllumiDesk.ServerData() // ServerData | 
};
apiInstance.projectsServersCreate(project, namespace, opts, (error, data, response) => {
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
 **project** | **String**| Project unique identifer expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **serverData** | [**ServerData**](ServerData.md)|  | [optional] 

### Return type

[**Server**](Server.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## projectsServersDelete

> projectsServersDelete(project, namespace, server)

Delete a server

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifier.
let namespace = "namespace_example"; // String | User or team name.
let server = "server_example"; // String | User unique identifier.
apiInstance.projectsServersDelete(project, namespace, server, (error, data, response) => {
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
 **project** | **String**| Project unique identifier. | 
 **namespace** | **String**| User or team name. | 
 **server** | **String**| User unique identifier. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsServersList

> [Server] projectsServersList(project, namespace, opts)

Retrieve servers

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'limit': "limit_example", // String | Limit results when getting server list.
  'offset': "offset_example", // String | Offset results when getting server list.
  'name': "name_example", // String | Server name.
  'ordering': "ordering_example" // String | Ordering option when getting server list.
};
apiInstance.projectsServersList(project, namespace, opts, (error, data, response) => {
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
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **limit** | **String**| Limit results when getting server list. | [optional] 
 **offset** | **String**| Offset results when getting server list. | [optional] 
 **name** | **String**| Server name. | [optional] 
 **ordering** | **String**| Ordering option when getting server list. | [optional] 

### Return type

[**[Server]**](Server.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsServersRead

> Server projectsServersRead(project, namespace, server)

Retrieve a server

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
apiInstance.projectsServersRead(project, namespace, server, (error, data, response) => {
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
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **server** | **String**| Server unique identifier expressed as UUID or name. | 

### Return type

[**Server**](Server.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsServersReplace

> Server projectsServersReplace(project, namespace, server, opts)

Replace a server

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
let opts = {
  'serverData': new IllumiDesk.ServerData() // ServerData | 
};
apiInstance.projectsServersReplace(project, namespace, server, opts, (error, data, response) => {
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
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **server** | **String**| Server unique identifier expressed as UUID or name. | 
 **serverData** | [**ServerData**](ServerData.md)|  | [optional] 

### Return type

[**Server**](Server.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## projectsServersRunStatsCreate

> ServerRunStatistics projectsServersRunStatsCreate(server, project, namespace, opts)

Create a new server&#39;s run statistics

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'serverrunstatsData': new IllumiDesk.ServerRunStatisticsData() // ServerRunStatisticsData | 
};
apiInstance.projectsServersRunStatsCreate(server, project, namespace, opts, (error, data, response) => {
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
 **server** | **String**| Server unique identifier expressed as UUID or name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **serverrunstatsData** | [**ServerRunStatisticsData**](ServerRunStatisticsData.md)|  | [optional] 

### Return type

[**ServerRunStatistics**](ServerRunStatistics.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## projectsServersRunStatsDelete

> projectsServersRunStatsDelete(server, project, namespace, id)

Delete a server&#39;s statistics

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let id = "id_example"; // String | Server run statistics unique identifier expressed as UUID.
apiInstance.projectsServersRunStatsDelete(server, project, namespace, id, (error, data, response) => {
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
 **server** | **String**| Server unique identifier expressed as UUID or name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **id** | **String**| Server run statistics unique identifier expressed as UUID. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsServersRunStatsRead

> ServerRunStatistics projectsServersRunStatsRead(server, project, namespace, id)

Retrieve statistics for a server

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let id = "id_example"; // String | Run statistics unique identifier expressed as UUID.
apiInstance.projectsServersRunStatsRead(server, project, namespace, id, (error, data, response) => {
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
 **server** | **String**| Server unique identifier expressed as UUID or name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **id** | **String**| Run statistics unique identifier expressed as UUID. | 

### Return type

[**ServerRunStatistics**](ServerRunStatistics.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsServersRunStatsReplace

> ServerRunStatistics projectsServersRunStatsReplace(server, project, namespace, id, opts)

Replace a server&#39;s statistics

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let id = "id_example"; // String | Server run statistics expressed as UUID.
let opts = {
  'serverrunstatsData': new IllumiDesk.ServerRunStatisticsData() // ServerRunStatisticsData | 
};
apiInstance.projectsServersRunStatsReplace(server, project, namespace, id, opts, (error, data, response) => {
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
 **server** | **String**| Server unique identifier expressed as UUID or name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **id** | **String**| Server run statistics expressed as UUID. | 
 **serverrunstatsData** | [**ServerRunStatisticsData**](ServerRunStatisticsData.md)|  | [optional] 

### Return type

[**ServerRunStatistics**](ServerRunStatistics.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## projectsServersRunStatsUpdate

> ServerRunStatistics projectsServersRunStatsUpdate(server, project, namespace, id, opts)

Update a server&#39;s statistics

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let id = "id_example"; // String | Server run statistics unique identifier expressed as UUID.
let opts = {
  'serverrunstatsData': new IllumiDesk.ServerRunStatisticsData() // ServerRunStatisticsData | 
};
apiInstance.projectsServersRunStatsUpdate(server, project, namespace, id, opts, (error, data, response) => {
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
 **server** | **String**| Server unique identifier expressed as UUID or name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **id** | **String**| Server run statistics unique identifier expressed as UUID. | 
 **serverrunstatsData** | [**ServerRunStatisticsData**](ServerRunStatisticsData.md)|  | [optional] 

### Return type

[**ServerRunStatistics**](ServerRunStatistics.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## projectsServersSshTunnelsCreate

> SshTunnel projectsServersSshTunnelsCreate(server, project, namespace, opts)

Create SSH Tunnel associated to a server

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'sshtunnelData': new IllumiDesk.SshTunnelData() // SshTunnelData | 
};
apiInstance.projectsServersSshTunnelsCreate(server, project, namespace, opts, (error, data, response) => {
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
 **server** | **String**| Server unique identifier expressed as UUID or name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **sshtunnelData** | [**SshTunnelData**](SshTunnelData.md)|  | [optional] 

### Return type

[**SshTunnel**](SshTunnel.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## projectsServersSshTunnelsDelete

> projectsServersSshTunnelsDelete(server, project, namespace, tunnel)

Delete an SSH Tunnel associated to a server

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let tunnel = "tunnel_example"; // String | SSH tunnel unique identifier expressed as UUID or name.
apiInstance.projectsServersSshTunnelsDelete(server, project, namespace, tunnel, (error, data, response) => {
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
 **server** | **String**| Server unique identifier expressed as UUID or name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **tunnel** | **String**| SSH tunnel unique identifier expressed as UUID or name. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsServersSshTunnelsList

> [SshTunnel] projectsServersSshTunnelsList(server, project, namespace, opts)

Get SSH Tunnels associated to a server

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'limit': "limit_example", // String | Limit retrieved items.
  'offset': "offset_example", // String | Offset retrieved items.
  'ordering': "ordering_example" // String | Order retrieved items.
};
apiInstance.projectsServersSshTunnelsList(server, project, namespace, opts, (error, data, response) => {
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
 **server** | **String**| Server unique identifier expressed as UUID or name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **limit** | **String**| Limit retrieved items. | [optional] 
 **offset** | **String**| Offset retrieved items. | [optional] 
 **ordering** | **String**| Order retrieved items. | [optional] 

### Return type

[**[SshTunnel]**](SshTunnel.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsServersSshTunnelsRead

> SshTunnel projectsServersSshTunnelsRead(server, project, namespace, tunnel)

Get an SSH Tunnel associated to a server

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let tunnel = "tunnel_example"; // String | SSH tunnel unique identifier expressed as UUID or name.
apiInstance.projectsServersSshTunnelsRead(server, project, namespace, tunnel, (error, data, response) => {
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
 **server** | **String**| Server unique identifier expressed as UUID or name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **tunnel** | **String**| SSH tunnel unique identifier expressed as UUID or name. | 

### Return type

[**SshTunnel**](SshTunnel.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsServersSshTunnelsReplace

> SshTunnel projectsServersSshTunnelsReplace(server, project, namespace, tunnel, opts)

Replace SSH Tunnel associated to a server

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let tunnel = "tunnel_example"; // String | SSH tunnel unique identifier expressed as UUID or name.
let opts = {
  'sshtunnelData': new IllumiDesk.SshTunnelData() // SshTunnelData | 
};
apiInstance.projectsServersSshTunnelsReplace(server, project, namespace, tunnel, opts, (error, data, response) => {
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
 **server** | **String**| Server unique identifier expressed as UUID or name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **tunnel** | **String**| SSH tunnel unique identifier expressed as UUID or name. | 
 **sshtunnelData** | [**SshTunnelData**](SshTunnelData.md)|  | [optional] 

### Return type

[**SshTunnel**](SshTunnel.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## projectsServersSshTunnelsUpdate

> SshTunnel projectsServersSshTunnelsUpdate(server, project, namespace, tunnel, opts)

Update an SSH Tunnel associated to a server

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let server = "server_example"; // String | 
let project = "project_example"; // String | 
let namespace = "namespace_example"; // String | User or team name.
let tunnel = "tunnel_example"; // String | 
let opts = {
  'sshtunnelData': new IllumiDesk.SshTunnelData() // SshTunnelData | 
};
apiInstance.projectsServersSshTunnelsUpdate(server, project, namespace, tunnel, opts, (error, data, response) => {
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
 **server** | **String**|  | 
 **project** | **String**|  | 
 **namespace** | **String**| User or team name. | 
 **tunnel** | **String**|  | 
 **sshtunnelData** | [**SshTunnelData**](SshTunnelData.md)|  | [optional] 

### Return type

[**SshTunnel**](SshTunnel.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## projectsServersStart

> projectsServersStart(project, namespace, server)

Start a server

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
apiInstance.projectsServersStart(project, namespace, server, (error, data, response) => {
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
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **server** | **String**| Server unique identifier expressed as UUID or name. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## projectsServersStatsDelete

> projectsServersStatsDelete(server, project, namespace, id)

Delete a server&#39;s statistics

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let id = "id_example"; // String | Stats unique identifier expressed as UUID.
apiInstance.projectsServersStatsDelete(server, project, namespace, id, (error, data, response) => {
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
 **server** | **String**| Server unique identifier expressed as UUID or name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **id** | **String**| Stats unique identifier expressed as UUID. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsServersStatsRead

> ServerStatistics projectsServersStatsRead(server, project, namespace, id)

Retrieve a server&#39;s statistics

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let id = "id_example"; // String | Server statistics unique identifier expressed as UUID.
apiInstance.projectsServersStatsRead(server, project, namespace, id, (error, data, response) => {
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
 **server** | **String**| Server unique identifier expressed as UUID or name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **id** | **String**| Server statistics unique identifier expressed as UUID. | 

### Return type

[**ServerStatistics**](ServerStatistics.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsServersStatsReplace

> ServerStatistics projectsServersStatsReplace(server, project, namespace, id, opts)

Replace a server&#39;s statistics

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let id = "id_example"; // String | Server statistics unique identifier expressed as UUID.
let opts = {
  'serverstatsData': new IllumiDesk.ServerStatisticsData() // ServerStatisticsData | 
};
apiInstance.projectsServersStatsReplace(server, project, namespace, id, opts, (error, data, response) => {
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
 **server** | **String**| Server unique identifier expressed as UUID or name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **id** | **String**| Server statistics unique identifier expressed as UUID. | 
 **serverstatsData** | [**ServerStatisticsData**](ServerStatisticsData.md)|  | [optional] 

### Return type

[**ServerStatistics**](ServerStatistics.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## projectsServersStatsUpdate

> ServerStatistics projectsServersStatsUpdate(server, project, namespace, id, opts)

Update a server&#39;s statistics

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let id = "id_example"; // String | Server statistics unique identifier expressed as UUID.
let opts = {
  'serverstatsData': new IllumiDesk.ServerStatisticsData() // ServerStatisticsData | 
};
apiInstance.projectsServersStatsUpdate(server, project, namespace, id, opts, (error, data, response) => {
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
 **server** | **String**| Server unique identifier expressed as UUID or name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **id** | **String**| Server statistics unique identifier expressed as UUID. | 
 **serverstatsData** | [**ServerStatisticsData**](ServerStatisticsData.md)|  | [optional] 

### Return type

[**ServerStatistics**](ServerStatistics.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## projectsServersStatuses

> [ServerStatus] projectsServersStatuses(project, namespace)

Retrieve server statuses

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
apiInstance.projectsServersStatuses(project, namespace, (error, data, response) => {
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
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 

### Return type

[**[ServerStatus]**](ServerStatus.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## projectsServersStop

> projectsServersStop(project, namespace, server)

Stop a server

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
apiInstance.projectsServersStop(project, namespace, server, (error, data, response) => {
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
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **server** | **String**| Server unique identifier expressed as UUID or name. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## projectsServersUpdate

> Server projectsServersUpdate(project, namespace, server, opts)

Update a server

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
let opts = {
  'serverData': new IllumiDesk.ServerData() // ServerData | 
};
apiInstance.projectsServersUpdate(project, namespace, server, opts, (error, data, response) => {
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
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **server** | **String**| Server unique identifier expressed as UUID or name. | 
 **serverData** | [**ServerData**](ServerData.md)|  | [optional] 

### Return type

[**Server**](Server.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## projectsUpdate

> Project projectsUpdate(namespace, project, opts)

Update a project

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let namespace = "namespace_example"; // String | User or team name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let opts = {
  'projectData': new IllumiDesk.ProjectData() // ProjectData | 
};
apiInstance.projectsUpdate(namespace, project, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **projectData** | [**ProjectData**](ProjectData.md)|  | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## serviceTriggerCreate

> ServerAction serviceTriggerCreate(server, project, namespace, opts)

Create a new server trigger

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'serverAction': new IllumiDesk.ServerActionData() // ServerActionData | Server action.
};
apiInstance.serviceTriggerCreate(server, project, namespace, opts, (error, data, response) => {
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
 **server** | **String**| Server unique identifier expressed as UUID or name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **serverAction** | [**ServerActionData**](ServerActionData.md)| Server action. | [optional] 

### Return type

[**ServerAction**](ServerAction.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## serviceTriggerDelete

> serviceTriggerDelete(server, project, namespace, trigger)

Delete a server trigger

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let trigger = "trigger_example"; // String | Trigger identifier expressed as UUID or name.
apiInstance.serviceTriggerDelete(server, project, namespace, trigger, (error, data, response) => {
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
 **server** | **String**| Server unique identifier expressed as UUID or name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **trigger** | **String**| Trigger identifier expressed as UUID or name. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## serviceTriggerList

> [ServerAction] serviceTriggerList(server, project, namespace, opts)

Retrieve server triggers

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'name': "name_example", // String | Trigger name.
  'limit': "limit_example", // String | Limit when getting triggers.
  'offset': "offset_example", // String | Offset when getting triggers.
  'ordering': "ordering_example" // String | Ordering when getting triggers.
};
apiInstance.serviceTriggerList(server, project, namespace, opts, (error, data, response) => {
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
 **server** | **String**| Server unique identifier expressed as UUID or name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **name** | **String**| Trigger name. | [optional] 
 **limit** | **String**| Limit when getting triggers. | [optional] 
 **offset** | **String**| Offset when getting triggers. | [optional] 
 **ordering** | **String**| Ordering when getting triggers. | [optional] 

### Return type

[**[ServerAction]**](ServerAction.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## serviceTriggerRead

> ServerAction serviceTriggerRead(server, project, namespace, trigger)

Get a server trigger

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let trigger = "trigger_example"; // String | Trigger unique identifier.
apiInstance.serviceTriggerRead(server, project, namespace, trigger, (error, data, response) => {
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
 **server** | **String**| Server unique identifier expressed as UUID or name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **trigger** | **String**| Trigger unique identifier. | 

### Return type

[**ServerAction**](ServerAction.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## serviceTriggerReplace

> ServerAction serviceTriggerReplace(server, project, namespace, trigger, opts)

Replace a server trigger

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let trigger = "trigger_example"; // String | Trigger unique identifier.
let opts = {
  'serverAction': new IllumiDesk.ServerActionData() // ServerActionData | 
};
apiInstance.serviceTriggerReplace(server, project, namespace, trigger, opts, (error, data, response) => {
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
 **server** | **String**| Server unique identifier expressed as UUID or name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **trigger** | **String**| Trigger unique identifier. | 
 **serverAction** | [**ServerActionData**](ServerActionData.md)|  | [optional] 

### Return type

[**ServerAction**](ServerAction.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## serviceTriggerUpdate

> ServerAction serviceTriggerUpdate(server, project, namespace, trigger, opts)

Update a server trigger

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ProjectsApi();
let server = "server_example"; // String | Server unique identifier expressed as UUID or name.
let project = "project_example"; // String | Project unique identifier expressed as UUID or name.
let namespace = "namespace_example"; // String | User or team name.
let trigger = "trigger_example"; // String | Trigger identifier expressed as UUID or name.
let opts = {
  'serverAction': new IllumiDesk.ServerActionData() // ServerActionData | 
};
apiInstance.serviceTriggerUpdate(server, project, namespace, trigger, opts, (error, data, response) => {
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
 **server** | **String**| Server unique identifier expressed as UUID or name. | 
 **project** | **String**| Project unique identifier expressed as UUID or name. | 
 **namespace** | **String**| User or team name. | 
 **trigger** | **String**| Trigger identifier expressed as UUID or name. | 
 **serverAction** | [**ServerActionData**](ServerActionData.md)|  | [optional] 

### Return type

[**ServerAction**](ServerAction.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html

