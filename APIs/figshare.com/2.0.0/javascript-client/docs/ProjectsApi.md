# FigshareApi.ProjectsApi

All URIs are relative to *https://api.figshare.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**privateProjectArticleDelete**](ProjectsApi.md#privateProjectArticleDelete) | **DELETE** /account/projects/{project_id}/articles/{article_id} | Delete project article
[**privateProjectArticleDetails**](ProjectsApi.md#privateProjectArticleDetails) | **GET** /account/projects/{project_id}/articles/{article_id} | Project article details
[**privateProjectArticleFile**](ProjectsApi.md#privateProjectArticleFile) | **GET** /account/projects/{project_id}/articles/{article_id}/files/{file_id} | Project article file details
[**privateProjectArticleFiles**](ProjectsApi.md#privateProjectArticleFiles) | **GET** /account/projects/{project_id}/articles/{article_id}/files | Project article list files
[**privateProjectArticlesCreate**](ProjectsApi.md#privateProjectArticlesCreate) | **POST** /account/projects/{project_id}/articles | Create project article
[**privateProjectArticlesList**](ProjectsApi.md#privateProjectArticlesList) | **GET** /account/projects/{project_id}/articles | List project articles
[**privateProjectCollaboratorDelete**](ProjectsApi.md#privateProjectCollaboratorDelete) | **DELETE** /account/projects/{project_id}/collaborators/{user_id} | Remove project collaborator
[**privateProjectCollaboratorsInvite**](ProjectsApi.md#privateProjectCollaboratorsInvite) | **POST** /account/projects/{project_id}/collaborators | Invite project collaborators
[**privateProjectCollaboratorsList**](ProjectsApi.md#privateProjectCollaboratorsList) | **GET** /account/projects/{project_id}/collaborators | List project collaborators
[**privateProjectCreate**](ProjectsApi.md#privateProjectCreate) | **POST** /account/projects | Create project
[**privateProjectDelete**](ProjectsApi.md#privateProjectDelete) | **DELETE** /account/projects/{project_id} | Delete project
[**privateProjectDetails**](ProjectsApi.md#privateProjectDetails) | **GET** /account/projects/{project_id} | View project details
[**privateProjectLeave**](ProjectsApi.md#privateProjectLeave) | **POST** /account/projects/{project_id}/leave | Private Project Leave
[**privateProjectNote**](ProjectsApi.md#privateProjectNote) | **GET** /account/projects/{project_id}/notes/{note_id} | Project note details
[**privateProjectNoteDelete**](ProjectsApi.md#privateProjectNoteDelete) | **DELETE** /account/projects/{project_id}/notes/{note_id} | Delete project note
[**privateProjectNoteUpdate**](ProjectsApi.md#privateProjectNoteUpdate) | **PUT** /account/projects/{project_id}/notes/{note_id} | Update project note
[**privateProjectNotesCreate**](ProjectsApi.md#privateProjectNotesCreate) | **POST** /account/projects/{project_id}/notes | Create project note
[**privateProjectNotesList**](ProjectsApi.md#privateProjectNotesList) | **GET** /account/projects/{project_id}/notes | List project notes
[**privateProjectPublish**](ProjectsApi.md#privateProjectPublish) | **POST** /account/projects/{project_id}/publish | Private Project Publish
[**privateProjectUpdate**](ProjectsApi.md#privateProjectUpdate) | **PUT** /account/projects/{project_id} | Update project
[**privateProjectsList**](ProjectsApi.md#privateProjectsList) | **GET** /account/projects | Private Projects
[**privateProjectsSearch**](ProjectsApi.md#privateProjectsSearch) | **POST** /account/projects/search | Private Projects search
[**projectArticles**](ProjectsApi.md#projectArticles) | **GET** /projects/{project_id}/articles | Public Project Articles
[**projectDetails**](ProjectsApi.md#projectDetails) | **GET** /projects/{project_id} | Public Project
[**projectsList**](ProjectsApi.md#projectsList) | **GET** /projects | Public Projects
[**projectsSearch**](ProjectsApi.md#projectsSearch) | **POST** /projects/search | Public Projects Search



## privateProjectArticleDelete

> privateProjectArticleDelete(projectId, articleId)

Delete project article

Delete project article

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ProjectsApi();
let projectId = 789; // Number | Project unique identifier
let articleId = 789; // Number | Project Article unique identifier
apiInstance.privateProjectArticleDelete(projectId, articleId, (error, data, response) => {
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
 **projectId** | **Number**| Project unique identifier | 
 **articleId** | **Number**| Project Article unique identifier | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateProjectArticleDetails

> ProjectArticle privateProjectArticleDetails(projectId, articleId)

Project article details

Project article details

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ProjectsApi();
let projectId = 789; // Number | Project unique identifier
let articleId = 789; // Number | Project Article unique identifier
apiInstance.privateProjectArticleDetails(projectId, articleId, (error, data, response) => {
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
 **projectId** | **Number**| Project unique identifier | 
 **articleId** | **Number**| Project Article unique identifier | 

### Return type

[**ProjectArticle**](ProjectArticle.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateProjectArticleFile

> PrivateFile privateProjectArticleFile(projectId, articleId, fileId)

Project article file details

Project article file details

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ProjectsApi();
let projectId = 789; // Number | Project unique identifier
let articleId = 789; // Number | Project Article unique identifier
let fileId = 789; // Number | File unique identifier
apiInstance.privateProjectArticleFile(projectId, articleId, fileId, (error, data, response) => {
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
 **projectId** | **Number**| Project unique identifier | 
 **articleId** | **Number**| Project Article unique identifier | 
 **fileId** | **Number**| File unique identifier | 

### Return type

[**PrivateFile**](PrivateFile.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateProjectArticleFiles

> [PrivateFile] privateProjectArticleFiles(projectId, articleId)

Project article list files

List article files

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ProjectsApi();
let projectId = 789; // Number | Project unique identifier
let articleId = 789; // Number | Project Article unique identifier
apiInstance.privateProjectArticleFiles(projectId, articleId, (error, data, response) => {
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
 **projectId** | **Number**| Project unique identifier | 
 **articleId** | **Number**| Project Article unique identifier | 

### Return type

[**[PrivateFile]**](PrivateFile.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateProjectArticlesCreate

> LocationWarnings privateProjectArticlesCreate(projectId, articleProjectCreate, opts)

Create project article

Create a new Article and associate it with this project

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ProjectsApi();
let projectId = 789; // Number | Project unique identifier
let articleProjectCreate = new FigshareApi.ArticleProjectCreate(); // ArticleProjectCreate | Article description
let opts = {
  'page': 789, // Number | Page number. Used for pagination with page_size
  'pageSize': 10, // Number | The number of results included on a page. Used for pagination with page
  'limit': 789, // Number | Number of results included on a page. Used for pagination with query
  'offset': 789 // Number | Where to start the listing(the offset of the first result). Used for pagination with limit
};
apiInstance.privateProjectArticlesCreate(projectId, articleProjectCreate, opts, (error, data, response) => {
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
 **projectId** | **Number**| Project unique identifier | 
 **articleProjectCreate** | [**ArticleProjectCreate**](ArticleProjectCreate.md)| Article description | 
 **page** | **Number**| Page number. Used for pagination with page_size | [optional] 
 **pageSize** | **Number**| The number of results included on a page. Used for pagination with page | [optional] [default to 10]
 **limit** | **Number**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **Number**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 

### Return type

[**LocationWarnings**](LocationWarnings.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateProjectArticlesList

> [Article] privateProjectArticlesList(projectId, opts)

List project articles

List project articles

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ProjectsApi();
let projectId = 789; // Number | Project unique identifier
let opts = {
  'page': 789, // Number | Page number. Used for pagination with page_size
  'pageSize': 10, // Number | The number of results included on a page. Used for pagination with page
  'limit': 789, // Number | Number of results included on a page. Used for pagination with query
  'offset': 789 // Number | Where to start the listing(the offset of the first result). Used for pagination with limit
};
apiInstance.privateProjectArticlesList(projectId, opts, (error, data, response) => {
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
 **projectId** | **Number**| Project unique identifier | 
 **page** | **Number**| Page number. Used for pagination with page_size | [optional] 
 **pageSize** | **Number**| The number of results included on a page. Used for pagination with page | [optional] [default to 10]
 **limit** | **Number**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **Number**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 

### Return type

[**[Article]**](Article.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateProjectCollaboratorDelete

> privateProjectCollaboratorDelete(projectId, userId)

Remove project collaborator

Remove project collaborator

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ProjectsApi();
let projectId = 789; // Number | Project unique identifier
let userId = 789; // Number | User unique identifier
apiInstance.privateProjectCollaboratorDelete(projectId, userId, (error, data, response) => {
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
 **projectId** | **Number**| Project unique identifier | 
 **userId** | **Number**| User unique identifier | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateProjectCollaboratorsInvite

> ResponseMessage privateProjectCollaboratorsInvite(projectId, projectCollaboratorInvite)

Invite project collaborators

Invite users to collaborate on project or view the project

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ProjectsApi();
let projectId = 789; // Number | Project unique identifier
let projectCollaboratorInvite = new FigshareApi.ProjectCollaboratorInvite(); // ProjectCollaboratorInvite | viewer or collaborator role. User user_id or email of user
apiInstance.privateProjectCollaboratorsInvite(projectId, projectCollaboratorInvite, (error, data, response) => {
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
 **projectId** | **Number**| Project unique identifier | 
 **projectCollaboratorInvite** | [**ProjectCollaboratorInvite**](ProjectCollaboratorInvite.md)| viewer or collaborator role. User user_id or email of user | 

### Return type

[**ResponseMessage**](ResponseMessage.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateProjectCollaboratorsList

> [ProjectCollaborator] privateProjectCollaboratorsList(projectId)

List project collaborators

List Project collaborators and invited users

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ProjectsApi();
let projectId = 789; // Number | Project unique identifier
apiInstance.privateProjectCollaboratorsList(projectId, (error, data, response) => {
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
 **projectId** | **Number**| Project unique identifier | 

### Return type

[**[ProjectCollaborator]**](ProjectCollaborator.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateProjectCreate

> CreateProjectResponse privateProjectCreate(projectCreate)

Create project

Create a new project

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ProjectsApi();
let projectCreate = new FigshareApi.ProjectCreate(); // ProjectCreate | Project  description
apiInstance.privateProjectCreate(projectCreate, (error, data, response) => {
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
 **projectCreate** | [**ProjectCreate**](ProjectCreate.md)| Project  description | 

### Return type

[**CreateProjectResponse**](CreateProjectResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateProjectDelete

> privateProjectDelete(projectId)

Delete project

A project can be deleted only if: - it is not public - it does not have public articles.  When an individual project is deleted, all the articles are moved to my data of each owner.  When a group project is deleted, all the articles and files are deleted as well. Only project owner, group admin and above can delete a project. 

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ProjectsApi();
let projectId = 789; // Number | Project unique identifier
apiInstance.privateProjectDelete(projectId, (error, data, response) => {
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
 **projectId** | **Number**| Project unique identifier | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateProjectDetails

> ProjectCompletePrivate privateProjectDetails(projectId)

View project details

View a private project

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ProjectsApi();
let projectId = 789; // Number | Project unique identifier
apiInstance.privateProjectDetails(projectId, (error, data, response) => {
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
 **projectId** | **Number**| Project unique identifier | 

### Return type

[**ProjectCompletePrivate**](ProjectCompletePrivate.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateProjectLeave

> privateProjectLeave(projectId)

Private Project Leave

Please note: project&#39;s owner cannot leave the project.

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ProjectsApi();
let projectId = 789; // Number | Project unique identifier
apiInstance.privateProjectLeave(projectId, (error, data, response) => {
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
 **projectId** | **Number**| Project unique identifier | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateProjectNote

> ProjectNotePrivate privateProjectNote(projectId, noteId)

Project note details

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ProjectsApi();
let projectId = 789; // Number | Project unique identifier
let noteId = 789; // Number | Note unique identifier
apiInstance.privateProjectNote(projectId, noteId, (error, data, response) => {
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
 **projectId** | **Number**| Project unique identifier | 
 **noteId** | **Number**| Note unique identifier | 

### Return type

[**ProjectNotePrivate**](ProjectNotePrivate.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateProjectNoteDelete

> privateProjectNoteDelete(projectId, noteId)

Delete project note

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ProjectsApi();
let projectId = 789; // Number | Project unique identifier
let noteId = 789; // Number | Note unique identifier
apiInstance.privateProjectNoteDelete(projectId, noteId, (error, data, response) => {
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
 **projectId** | **Number**| Project unique identifier | 
 **noteId** | **Number**| Note unique identifier | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateProjectNoteUpdate

> privateProjectNoteUpdate(projectId, noteId, projectNoteCreate)

Update project note

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ProjectsApi();
let projectId = 789; // Number | Project unique identifier
let noteId = 789; // Number | Note unique identifier
let projectNoteCreate = new FigshareApi.ProjectNoteCreate(); // ProjectNoteCreate | Note message
apiInstance.privateProjectNoteUpdate(projectId, noteId, projectNoteCreate, (error, data, response) => {
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
 **projectId** | **Number**| Project unique identifier | 
 **noteId** | **Number**| Note unique identifier | 
 **projectNoteCreate** | [**ProjectNoteCreate**](ProjectNoteCreate.md)| Note message | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateProjectNotesCreate

> Location privateProjectNotesCreate(projectId, projectNoteCreate)

Create project note

Create a new project note

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ProjectsApi();
let projectId = 789; // Number | Project unique identifier
let projectNoteCreate = new FigshareApi.ProjectNoteCreate(); // ProjectNoteCreate | Note message
apiInstance.privateProjectNotesCreate(projectId, projectNoteCreate, (error, data, response) => {
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
 **projectId** | **Number**| Project unique identifier | 
 **projectNoteCreate** | [**ProjectNoteCreate**](ProjectNoteCreate.md)| Note message | 

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateProjectNotesList

> [ProjectNote] privateProjectNotesList(projectId, opts)

List project notes

List project notes

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ProjectsApi();
let projectId = 789; // Number | Project unique identifier
let opts = {
  'page': 789, // Number | Page number. Used for pagination with page_size
  'pageSize': 10, // Number | The number of results included on a page. Used for pagination with page
  'limit': 789, // Number | Number of results included on a page. Used for pagination with query
  'offset': 789 // Number | Where to start the listing(the offset of the first result). Used for pagination with limit
};
apiInstance.privateProjectNotesList(projectId, opts, (error, data, response) => {
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
 **projectId** | **Number**| Project unique identifier | 
 **page** | **Number**| Page number. Used for pagination with page_size | [optional] 
 **pageSize** | **Number**| The number of results included on a page. Used for pagination with page | [optional] [default to 10]
 **limit** | **Number**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **Number**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 

### Return type

[**[ProjectNote]**](ProjectNote.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateProjectPublish

> ResponseMessage privateProjectPublish(projectId)

Private Project Publish

Publish a project. Possible after all items inside it are public

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ProjectsApi();
let projectId = 789; // Number | Project unique identifier
apiInstance.privateProjectPublish(projectId, (error, data, response) => {
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
 **projectId** | **Number**| Project unique identifier | 

### Return type

[**ResponseMessage**](ResponseMessage.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateProjectUpdate

> privateProjectUpdate(projectId, projectUpdate)

Update project

Updating an project by passing body parameters; request can also be made with the PATCH method.

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ProjectsApi();
let projectId = 789; // Number | Project unique identifier
let projectUpdate = new FigshareApi.ProjectUpdate(); // ProjectUpdate | Project description
apiInstance.privateProjectUpdate(projectId, projectUpdate, (error, data, response) => {
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
 **projectId** | **Number**| Project unique identifier | 
 **projectUpdate** | [**ProjectUpdate**](ProjectUpdate.md)| Project description | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateProjectsList

> [ProjectPrivate] privateProjectsList(opts)

Private Projects

List private projects

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ProjectsApi();
let opts = {
  'page': 789, // Number | Page number. Used for pagination with page_size
  'pageSize': 10, // Number | The number of results included on a page. Used for pagination with page
  'limit': 789, // Number | Number of results included on a page. Used for pagination with query
  'offset': 789, // Number | Where to start the listing(the offset of the first result). Used for pagination with limit
  'order': "'published_date'", // String | The field by which to order.
  'orderDirection': "'desc'", // String | 
  'storage': "storage_example", // String | only return collections from this institution
  'roles': "roles_example" // String | Any combination of owner, collaborator, viewer separated by comma. Examples: \"owner\" or \"owner,collaborator\".
};
apiInstance.privateProjectsList(opts, (error, data, response) => {
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
 **page** | **Number**| Page number. Used for pagination with page_size | [optional] 
 **pageSize** | **Number**| The number of results included on a page. Used for pagination with page | [optional] [default to 10]
 **limit** | **Number**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **Number**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 
 **order** | **String**| The field by which to order. | [optional] [default to &#39;published_date&#39;]
 **orderDirection** | **String**|  | [optional] [default to &#39;desc&#39;]
 **storage** | **String**| only return collections from this institution | [optional] 
 **roles** | **String**| Any combination of owner, collaborator, viewer separated by comma. Examples: \&quot;owner\&quot; or \&quot;owner,collaborator\&quot;. | [optional] 

### Return type

[**[ProjectPrivate]**](ProjectPrivate.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateProjectsSearch

> [ProjectPrivate] privateProjectsSearch(opts)

Private Projects search

Search inside the private projects

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.ProjectsApi();
let opts = {
  'projectsSearch': new FigshareApi.ProjectsSearch() // ProjectsSearch | Search Parameters
};
apiInstance.privateProjectsSearch(opts, (error, data, response) => {
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
 **projectsSearch** | [**ProjectsSearch**](ProjectsSearch.md)| Search Parameters | [optional] 

### Return type

[**[ProjectPrivate]**](ProjectPrivate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectArticles

> [Article] projectArticles(projectId)

Public Project Articles

List articles in project

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.ProjectsApi();
let projectId = 789; // Number | Project Unique identifier
apiInstance.projectArticles(projectId, (error, data, response) => {
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
 **projectId** | **Number**| Project Unique identifier | 

### Return type

[**[Article]**](Article.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectDetails

> ProjectComplete projectDetails(projectId)

Public Project

View a project

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.ProjectsApi();
let projectId = 789; // Number | Project Unique identifier
apiInstance.projectDetails(projectId, (error, data, response) => {
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
 **projectId** | **Number**| Project Unique identifier | 

### Return type

[**ProjectComplete**](ProjectComplete.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsList

> [Project] projectsList(opts)

Public Projects

Returns a list of public projects

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.ProjectsApi();
let opts = {
  'xCursor': "xCursor_example", // String | Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected.
  'page': 789, // Number | Page number. Used for pagination with page_size
  'pageSize': 10, // Number | The number of results included on a page. Used for pagination with page
  'limit': 789, // Number | Number of results included on a page. Used for pagination with query
  'offset': 789, // Number | Where to start the listing(the offset of the first result). Used for pagination with limit
  'order': "'published_date'", // String | The field by which to order. Default varies by endpoint/resource.
  'orderDirection': "'desc'", // String | 
  'institution': 789, // Number | only return collections from this institution
  'publishedSince': "publishedSince_example", // String | Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD
  'group': 789 // Number | only return collections from this group
};
apiInstance.projectsList(opts, (error, data, response) => {
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
 **xCursor** | **String**| Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected. | [optional] 
 **page** | **Number**| Page number. Used for pagination with page_size | [optional] 
 **pageSize** | **Number**| The number of results included on a page. Used for pagination with page | [optional] [default to 10]
 **limit** | **Number**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **Number**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 
 **order** | **String**| The field by which to order. Default varies by endpoint/resource. | [optional] [default to &#39;published_date&#39;]
 **orderDirection** | **String**|  | [optional] [default to &#39;desc&#39;]
 **institution** | **Number**| only return collections from this institution | [optional] 
 **publishedSince** | **String**| Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD | [optional] 
 **group** | **Number**| only return collections from this group | [optional] 

### Return type

[**[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsSearch

> [Project] projectsSearch(opts)

Public Projects Search

Returns a list of public articles

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.ProjectsApi();
let opts = {
  'xCursor': "xCursor_example", // String | Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected.
  'projectsSearch': new FigshareApi.ProjectsSearch() // ProjectsSearch | Search Parameters
};
apiInstance.projectsSearch(opts, (error, data, response) => {
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
 **xCursor** | **String**| Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected. | [optional] 
 **projectsSearch** | [**ProjectsSearch**](ProjectsSearch.md)| Search Parameters | [optional] 

### Return type

[**[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

