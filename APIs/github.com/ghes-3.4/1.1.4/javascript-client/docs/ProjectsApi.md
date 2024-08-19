# GitHubV3RestApi.ProjectsApi

All URIs are relative to *https://github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectsAddCollaborator**](ProjectsApi.md#projectsAddCollaborator) | **PUT** /projects/{project_id}/collaborators/{username} | Add project collaborator
[**projectsCreateCard**](ProjectsApi.md#projectsCreateCard) | **POST** /projects/columns/{column_id}/cards | Create a project card
[**projectsCreateColumn**](ProjectsApi.md#projectsCreateColumn) | **POST** /projects/{project_id}/columns | Create a project column
[**projectsCreateForAuthenticatedUser**](ProjectsApi.md#projectsCreateForAuthenticatedUser) | **POST** /user/projects | Create a user project
[**projectsCreateForOrg**](ProjectsApi.md#projectsCreateForOrg) | **POST** /orgs/{org}/projects | Create an organization project
[**projectsCreateForRepo**](ProjectsApi.md#projectsCreateForRepo) | **POST** /repos/{owner}/{repo}/projects | Create a repository project
[**projectsDelete**](ProjectsApi.md#projectsDelete) | **DELETE** /projects/{project_id} | Delete a project
[**projectsDeleteCard**](ProjectsApi.md#projectsDeleteCard) | **DELETE** /projects/columns/cards/{card_id} | Delete a project card
[**projectsDeleteColumn**](ProjectsApi.md#projectsDeleteColumn) | **DELETE** /projects/columns/{column_id} | Delete a project column
[**projectsGet**](ProjectsApi.md#projectsGet) | **GET** /projects/{project_id} | Get a project
[**projectsGetCard**](ProjectsApi.md#projectsGetCard) | **GET** /projects/columns/cards/{card_id} | Get a project card
[**projectsGetColumn**](ProjectsApi.md#projectsGetColumn) | **GET** /projects/columns/{column_id} | Get a project column
[**projectsGetPermissionForUser**](ProjectsApi.md#projectsGetPermissionForUser) | **GET** /projects/{project_id}/collaborators/{username}/permission | Get project permission for a user
[**projectsListCards**](ProjectsApi.md#projectsListCards) | **GET** /projects/columns/{column_id}/cards | List project cards
[**projectsListCollaborators**](ProjectsApi.md#projectsListCollaborators) | **GET** /projects/{project_id}/collaborators | List project collaborators
[**projectsListColumns**](ProjectsApi.md#projectsListColumns) | **GET** /projects/{project_id}/columns | List project columns
[**projectsListForOrg**](ProjectsApi.md#projectsListForOrg) | **GET** /orgs/{org}/projects | List organization projects
[**projectsListForRepo**](ProjectsApi.md#projectsListForRepo) | **GET** /repos/{owner}/{repo}/projects | List repository projects
[**projectsListForUser**](ProjectsApi.md#projectsListForUser) | **GET** /users/{username}/projects | List user projects
[**projectsMoveCard**](ProjectsApi.md#projectsMoveCard) | **POST** /projects/columns/cards/{card_id}/moves | Move a project card
[**projectsMoveColumn**](ProjectsApi.md#projectsMoveColumn) | **POST** /projects/columns/{column_id}/moves | Move a project column
[**projectsRemoveCollaborator**](ProjectsApi.md#projectsRemoveCollaborator) | **DELETE** /projects/{project_id}/collaborators/{username} | Remove user as a collaborator
[**projectsUpdate**](ProjectsApi.md#projectsUpdate) | **PATCH** /projects/{project_id} | Update a project
[**projectsUpdateCard**](ProjectsApi.md#projectsUpdateCard) | **PATCH** /projects/columns/cards/{card_id} | Update an existing project card
[**projectsUpdateColumn**](ProjectsApi.md#projectsUpdateColumn) | **PATCH** /projects/columns/{column_id} | Update an existing project column



## projectsAddCollaborator

> projectsAddCollaborator(projectId, username, opts)

Add project collaborator

Adds a collaborator to an organization project and sets their permission level. You must be an organization owner or a project &#x60;admin&#x60; to add a collaborator.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let projectId = 56; // Number | The unique identifier of the project.
let username = "username_example"; // String | The handle for the GitHub user account.
let opts = {
  'projectsAddCollaboratorRequest': {"permission":"write"} // ProjectsAddCollaboratorRequest | 
};
apiInstance.projectsAddCollaborator(projectId, username, opts, (error, data, response) => {
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
 **projectId** | **Number**| The unique identifier of the project. | 
 **username** | **String**| The handle for the GitHub user account. | 
 **projectsAddCollaboratorRequest** | [**ProjectsAddCollaboratorRequest**](ProjectsAddCollaboratorRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectsCreateCard

> ProjectCard projectsCreateCard(columnId, projectsCreateCardRequest)

Create a project card



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let columnId = 56; // Number | The unique identifier of the column.
let projectsCreateCardRequest = {"note":"Add payload for delete Project column"}; // ProjectsCreateCardRequest | 
apiInstance.projectsCreateCard(columnId, projectsCreateCardRequest, (error, data, response) => {
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
 **columnId** | **Number**| The unique identifier of the column. | 
 **projectsCreateCardRequest** | [**ProjectsCreateCardRequest**](ProjectsCreateCardRequest.md)|  | 

### Return type

[**ProjectCard**](ProjectCard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectsCreateColumn

> ProjectColumn projectsCreateColumn(projectId, projectsUpdateColumnRequest)

Create a project column



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let projectId = 56; // Number | The unique identifier of the project.
let projectsUpdateColumnRequest = {"name":"Remaining tasks"}; // ProjectsUpdateColumnRequest | 
apiInstance.projectsCreateColumn(projectId, projectsUpdateColumnRequest, (error, data, response) => {
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
 **projectId** | **Number**| The unique identifier of the project. | 
 **projectsUpdateColumnRequest** | [**ProjectsUpdateColumnRequest**](ProjectsUpdateColumnRequest.md)|  | 

### Return type

[**ProjectColumn**](ProjectColumn.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectsCreateForAuthenticatedUser

> Project projectsCreateForAuthenticatedUser(projectsCreateForAuthenticatedUserRequest)

Create a user project

Creates a user project board. Returns a &#x60;410 Gone&#x60; status if the user does not have existing classic projects. If you do not have sufficient privileges to perform this action, a &#x60;401 Unauthorized&#x60; or &#x60;410 Gone&#x60; status is returned.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let projectsCreateForAuthenticatedUserRequest = {"body":"A board to manage my personal projects.","name":"My Projects"}; // ProjectsCreateForAuthenticatedUserRequest | 
apiInstance.projectsCreateForAuthenticatedUser(projectsCreateForAuthenticatedUserRequest, (error, data, response) => {
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
 **projectsCreateForAuthenticatedUserRequest** | [**ProjectsCreateForAuthenticatedUserRequest**](ProjectsCreateForAuthenticatedUserRequest.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectsCreateForOrg

> Project projectsCreateForOrg(org, projectsCreateForOrgRequest)

Create an organization project

Creates an organization project board. Returns a &#x60;410 Gone&#x60; status if projects are disabled in the organization or if the organization does not have existing classic projects. If you do not have sufficient privileges to perform this action, a &#x60;401 Unauthorized&#x60; or &#x60;410 Gone&#x60; status is returned.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let projectsCreateForOrgRequest = {"body":"High-level roadmap for the upcoming year.","name":"Organization Roadmap"}; // ProjectsCreateForOrgRequest | 
apiInstance.projectsCreateForOrg(org, projectsCreateForOrgRequest, (error, data, response) => {
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
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **projectsCreateForOrgRequest** | [**ProjectsCreateForOrgRequest**](ProjectsCreateForOrgRequest.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectsCreateForRepo

> Project projectsCreateForRepo(owner, repo, projectsCreateForOrgRequest)

Create a repository project

Creates a repository project board. Returns a &#x60;410 Gone&#x60; status if projects are disabled in the repository or if the repository does not have existing classic projects. If you do not have sufficient privileges to perform this action, a &#x60;401 Unauthorized&#x60; or &#x60;410 Gone&#x60; status is returned.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let projectsCreateForOrgRequest = {"body":"Developer documentation project for the developer site.","name":"Projects Documentation"}; // ProjectsCreateForOrgRequest | 
apiInstance.projectsCreateForRepo(owner, repo, projectsCreateForOrgRequest, (error, data, response) => {
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
 **owner** | **String**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **String**| The name of the repository. The name is not case sensitive. | 
 **projectsCreateForOrgRequest** | [**ProjectsCreateForOrgRequest**](ProjectsCreateForOrgRequest.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectsDelete

> projectsDelete(projectId)

Delete a project

Deletes a project board. Returns a &#x60;404 Not Found&#x60; status if projects are disabled.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let projectId = 56; // Number | The unique identifier of the project.
apiInstance.projectsDelete(projectId, (error, data, response) => {
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
 **projectId** | **Number**| The unique identifier of the project. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsDeleteCard

> projectsDeleteCard(cardId)

Delete a project card



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let cardId = 56; // Number | The unique identifier of the card.
apiInstance.projectsDeleteCard(cardId, (error, data, response) => {
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
 **cardId** | **Number**| The unique identifier of the card. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsDeleteColumn

> projectsDeleteColumn(columnId)

Delete a project column



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let columnId = 56; // Number | The unique identifier of the column.
apiInstance.projectsDeleteColumn(columnId, (error, data, response) => {
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
 **columnId** | **Number**| The unique identifier of the column. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsGet

> Project projectsGet(projectId)

Get a project

Gets a project by its &#x60;id&#x60;. Returns a &#x60;404 Not Found&#x60; status if projects are disabled. If you do not have sufficient privileges to perform this action, a &#x60;401 Unauthorized&#x60; or &#x60;410 Gone&#x60; status is returned.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let projectId = 56; // Number | The unique identifier of the project.
apiInstance.projectsGet(projectId, (error, data, response) => {
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
 **projectId** | **Number**| The unique identifier of the project. | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsGetCard

> ProjectCard projectsGetCard(cardId)

Get a project card



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let cardId = 56; // Number | The unique identifier of the card.
apiInstance.projectsGetCard(cardId, (error, data, response) => {
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
 **cardId** | **Number**| The unique identifier of the card. | 

### Return type

[**ProjectCard**](ProjectCard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsGetColumn

> ProjectColumn projectsGetColumn(columnId)

Get a project column



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let columnId = 56; // Number | The unique identifier of the column.
apiInstance.projectsGetColumn(columnId, (error, data, response) => {
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
 **columnId** | **Number**| The unique identifier of the column. | 

### Return type

[**ProjectColumn**](ProjectColumn.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsGetPermissionForUser

> ProjectCollaboratorPermission projectsGetPermissionForUser(projectId, username)

Get project permission for a user

Returns the collaborator&#39;s permission level for an organization project. Possible values for the &#x60;permission&#x60; key: &#x60;admin&#x60;, &#x60;write&#x60;, &#x60;read&#x60;, &#x60;none&#x60;. You must be an organization owner or a project &#x60;admin&#x60; to review a user&#39;s permission level.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let projectId = 56; // Number | The unique identifier of the project.
let username = "username_example"; // String | The handle for the GitHub user account.
apiInstance.projectsGetPermissionForUser(projectId, username, (error, data, response) => {
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
 **projectId** | **Number**| The unique identifier of the project. | 
 **username** | **String**| The handle for the GitHub user account. | 

### Return type

[**ProjectCollaboratorPermission**](ProjectCollaboratorPermission.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsListCards

> [ProjectCard] projectsListCards(columnId, opts)

List project cards



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let columnId = 56; // Number | The unique identifier of the column.
let opts = {
  'archivedState': "'not_archived'", // String | Filters the project cards that are returned by the card's state.
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.projectsListCards(columnId, opts, (error, data, response) => {
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
 **columnId** | **Number**| The unique identifier of the column. | 
 **archivedState** | **String**| Filters the project cards that are returned by the card&#39;s state. | [optional] [default to &#39;not_archived&#39;]
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[ProjectCard]**](ProjectCard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsListCollaborators

> [SimpleUser] projectsListCollaborators(projectId, opts)

List project collaborators

Lists the collaborators for an organization project. For a project, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners. You must be an organization owner or a project &#x60;admin&#x60; to list collaborators.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let projectId = 56; // Number | The unique identifier of the project.
let opts = {
  'affiliation': "'all'", // String | Filters the collaborators by their affiliation. `outside` means outside collaborators of a project that are not a member of the project's organization. `direct` means collaborators with permissions to a project, regardless of organization membership status. `all` means all collaborators the authenticated user can see.
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.projectsListCollaborators(projectId, opts, (error, data, response) => {
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
 **projectId** | **Number**| The unique identifier of the project. | 
 **affiliation** | **String**| Filters the collaborators by their affiliation. &#x60;outside&#x60; means outside collaborators of a project that are not a member of the project&#39;s organization. &#x60;direct&#x60; means collaborators with permissions to a project, regardless of organization membership status. &#x60;all&#x60; means all collaborators the authenticated user can see. | [optional] [default to &#39;all&#39;]
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[SimpleUser]**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsListColumns

> [ProjectColumn] projectsListColumns(projectId, opts)

List project columns



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let projectId = 56; // Number | The unique identifier of the project.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.projectsListColumns(projectId, opts, (error, data, response) => {
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
 **projectId** | **Number**| The unique identifier of the project. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[ProjectColumn]**](ProjectColumn.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsListForOrg

> [Project] projectsListForOrg(org, opts)

List organization projects

Lists the projects in an organization. Returns a &#x60;404 Not Found&#x60; status if projects are disabled in the organization. If you do not have sufficient privileges to perform this action, a &#x60;401 Unauthorized&#x60; or &#x60;410 Gone&#x60; status is returned.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let opts = {
  'state': "'open'", // String | Indicates the state of the projects to return.
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.projectsListForOrg(org, opts, (error, data, response) => {
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
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **state** | **String**| Indicates the state of the projects to return. | [optional] [default to &#39;open&#39;]
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsListForRepo

> [Project] projectsListForRepo(owner, repo, opts)

List repository projects

Lists the projects in a repository. Returns a &#x60;404 Not Found&#x60; status if projects are disabled in the repository. If you do not have sufficient privileges to perform this action, a &#x60;401 Unauthorized&#x60; or &#x60;410 Gone&#x60; status is returned.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let opts = {
  'state': "'open'", // String | Indicates the state of the projects to return.
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.projectsListForRepo(owner, repo, opts, (error, data, response) => {
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
 **owner** | **String**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **String**| The name of the repository. The name is not case sensitive. | 
 **state** | **String**| Indicates the state of the projects to return. | [optional] [default to &#39;open&#39;]
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsListForUser

> [Project] projectsListForUser(username, opts)

List user projects



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let username = "username_example"; // String | The handle for the GitHub user account.
let opts = {
  'state': "'open'", // String | Indicates the state of the projects to return.
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.projectsListForUser(username, opts, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 
 **state** | **String**| Indicates the state of the projects to return. | [optional] [default to &#39;open&#39;]
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsMoveCard

> Object projectsMoveCard(cardId, projectsMoveCardRequest)

Move a project card



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let cardId = 56; // Number | The unique identifier of the card.
let projectsMoveCardRequest = {"column_id":42,"position":"bottom"}; // ProjectsMoveCardRequest | 
apiInstance.projectsMoveCard(cardId, projectsMoveCardRequest, (error, data, response) => {
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
 **cardId** | **Number**| The unique identifier of the card. | 
 **projectsMoveCardRequest** | [**ProjectsMoveCardRequest**](ProjectsMoveCardRequest.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectsMoveColumn

> Object projectsMoveColumn(columnId, projectsMoveColumnRequest)

Move a project column



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let columnId = 56; // Number | The unique identifier of the column.
let projectsMoveColumnRequest = {"position":"last"}; // ProjectsMoveColumnRequest | 
apiInstance.projectsMoveColumn(columnId, projectsMoveColumnRequest, (error, data, response) => {
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
 **columnId** | **Number**| The unique identifier of the column. | 
 **projectsMoveColumnRequest** | [**ProjectsMoveColumnRequest**](ProjectsMoveColumnRequest.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectsRemoveCollaborator

> projectsRemoveCollaborator(projectId, username)

Remove user as a collaborator

Removes a collaborator from an organization project. You must be an organization owner or a project &#x60;admin&#x60; to remove a collaborator.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let projectId = 56; // Number | The unique identifier of the project.
let username = "username_example"; // String | The handle for the GitHub user account.
apiInstance.projectsRemoveCollaborator(projectId, username, (error, data, response) => {
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
 **projectId** | **Number**| The unique identifier of the project. | 
 **username** | **String**| The handle for the GitHub user account. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsUpdate

> Project projectsUpdate(projectId, opts)

Update a project

Updates a project board&#39;s information. Returns a &#x60;404 Not Found&#x60; status if projects are disabled. If you do not have sufficient privileges to perform this action, a &#x60;401 Unauthorized&#x60; or &#x60;410 Gone&#x60; status is returned.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let projectId = 56; // Number | The unique identifier of the project.
let opts = {
  'projectsUpdateRequest': {"name":"Week One Sprint","organization_permission":"write","state":"open"} // ProjectsUpdateRequest | 
};
apiInstance.projectsUpdate(projectId, opts, (error, data, response) => {
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
 **projectId** | **Number**| The unique identifier of the project. | 
 **projectsUpdateRequest** | [**ProjectsUpdateRequest**](ProjectsUpdateRequest.md)|  | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectsUpdateCard

> ProjectCard projectsUpdateCard(cardId, opts)

Update an existing project card



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let cardId = 56; // Number | The unique identifier of the card.
let opts = {
  'projectsUpdateCardRequest': {"note":"Add payload for delete Project column"} // ProjectsUpdateCardRequest | 
};
apiInstance.projectsUpdateCard(cardId, opts, (error, data, response) => {
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
 **cardId** | **Number**| The unique identifier of the card. | 
 **projectsUpdateCardRequest** | [**ProjectsUpdateCardRequest**](ProjectsUpdateCardRequest.md)|  | [optional] 

### Return type

[**ProjectCard**](ProjectCard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectsUpdateColumn

> ProjectColumn projectsUpdateColumn(columnId, projectsUpdateColumnRequest)

Update an existing project column



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ProjectsApi();
let columnId = 56; // Number | The unique identifier of the column.
let projectsUpdateColumnRequest = {"name":"To Do"}; // ProjectsUpdateColumnRequest | 
apiInstance.projectsUpdateColumn(columnId, projectsUpdateColumnRequest, (error, data, response) => {
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
 **columnId** | **Number**| The unique identifier of the column. | 
 **projectsUpdateColumnRequest** | [**ProjectsUpdateColumnRequest**](ProjectsUpdateColumnRequest.md)|  | 

### Return type

[**ProjectColumn**](ProjectColumn.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

