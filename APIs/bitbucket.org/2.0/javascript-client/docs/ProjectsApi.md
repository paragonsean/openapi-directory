# BitbucketApi.ProjectsApi

All URIs are relative to *https://api.bitbucket.org/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workspacesWorkspaceProjectsPost**](ProjectsApi.md#workspacesWorkspaceProjectsPost) | **POST** /workspaces/{workspace}/projects | Create a project in a workspace
[**workspacesWorkspaceProjectsProjectKeyDefaultReviewersGet**](ProjectsApi.md#workspacesWorkspaceProjectsProjectKeyDefaultReviewersGet) | **GET** /workspaces/{workspace}/projects/{project_key}/default-reviewers | List the default reviewers in a project
[**workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserDelete**](ProjectsApi.md#workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserDelete) | **DELETE** /workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user} | Remove the specific user from the project&#39;s default reviewers
[**workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserGet**](ProjectsApi.md#workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserGet) | **GET** /workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user} | Get a default reviewer
[**workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserPut**](ProjectsApi.md#workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserPut) | **PUT** /workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user} | Add the specific user as a default reviewer for the project
[**workspacesWorkspaceProjectsProjectKeyDelete**](ProjectsApi.md#workspacesWorkspaceProjectsProjectKeyDelete) | **DELETE** /workspaces/{workspace}/projects/{project_key} | Delete a project for a workspace
[**workspacesWorkspaceProjectsProjectKeyGet**](ProjectsApi.md#workspacesWorkspaceProjectsProjectKeyGet) | **GET** /workspaces/{workspace}/projects/{project_key} | Get a project for a workspace
[**workspacesWorkspaceProjectsProjectKeyPut**](ProjectsApi.md#workspacesWorkspaceProjectsProjectKeyPut) | **PUT** /workspaces/{workspace}/projects/{project_key} | Update a project for a workspace



## workspacesWorkspaceProjectsPost

> Project workspacesWorkspaceProjectsPost(workspace, project)

Create a project in a workspace

Creates a new project.  Note that the avatar has to be embedded as either a data-url or a URL to an external image as shown in the examples below:  &#x60;&#x60;&#x60; $ body&#x3D;$(cat &lt;&lt; EOF {     \&quot;name\&quot;: \&quot;Mars Project\&quot;,     \&quot;key\&quot;: \&quot;MARS\&quot;,     \&quot;description\&quot;: \&quot;Software for colonizing mars.\&quot;,     \&quot;links\&quot;: {         \&quot;avatar\&quot;: {             \&quot;href\&quot;: \&quot;data:image/gif;base64,R0lGODlhEAAQAMQAAORHHOVSKudfOulrSOp3WOyDZu6QdvCchPGolfO0o/...\&quot;         }     },     \&quot;is_private\&quot;: false } EOF ) $ curl -H \&quot;Content-Type: application/json\&quot; \\        -X POST \\        -d \&quot;$body\&quot; \\        https://api.bitbucket.org/2.0/teams/teams-in-space/projects/ | jq . {   // Serialized project document } &#x60;&#x60;&#x60;  or even:  &#x60;&#x60;&#x60; $ body&#x3D;$(cat &lt;&lt; EOF {     \&quot;name\&quot;: \&quot;Mars Project\&quot;,     \&quot;key\&quot;: \&quot;MARS\&quot;,     \&quot;description\&quot;: \&quot;Software for colonizing mars.\&quot;,     \&quot;links\&quot;: {         \&quot;avatar\&quot;: {             \&quot;href\&quot;: \&quot;http://i.imgur.com/72tRx4w.gif\&quot;         }     },     \&quot;is_private\&quot;: false } EOF ) $ curl -H \&quot;Content-Type: application/json\&quot; \\        -X POST \\        -d \&quot;$body\&quot; \\        https://api.bitbucket.org/2.0/teams/teams-in-space/projects/ | jq . {   // Serialized project document } &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.ProjectsApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
let project = new BitbucketApi.Project(); // Project | 
apiInstance.workspacesWorkspaceProjectsPost(workspace, project, (error, data, response) => {
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
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 
 **project** | [**Project**](Project.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workspacesWorkspaceProjectsProjectKeyDefaultReviewersGet

> PaginatedDefaultReviewerAndType workspacesWorkspaceProjectsProjectKeyDefaultReviewersGet(projectKey, workspace)

List the default reviewers in a project

Return a list of all default reviewers for a project. This is a list of users that will be added as default reviewers to pull requests for any repository within the project.  Example: &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/.../projects/.../default-reviewers | jq . {     \&quot;pagelen\&quot;: 10,     \&quot;values\&quot;: [         {             \&quot;user\&quot;: {                 \&quot;display_name\&quot;: \&quot;Davis Lee\&quot;,                 \&quot;uuid\&quot;: \&quot;{f0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6}\&quot;             },             \&quot;reviewer_type\&quot;: \&quot;project\&quot;,             \&quot;type\&quot;: \&quot;default_reviewer\&quot;         },         {             \&quot;user\&quot;: {                 \&quot;display_name\&quot;: \&quot;Jorge Rodriguez\&quot;,                 \&quot;uuid\&quot;: \&quot;{1aa43376-260d-4a0b-9660-f62672b9655d}\&quot;             },             \&quot;reviewer_type\&quot;: \&quot;project\&quot;,             \&quot;type\&quot;: \&quot;default_reviewer\&quot;         }     ],     \&quot;page\&quot;: 1,     \&quot;size\&quot;: 2 } &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.ProjectsApi();
let projectKey = "projectKey_example"; // String | The project in question. This is the actual `key` assigned to the project. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.workspacesWorkspaceProjectsProjectKeyDefaultReviewersGet(projectKey, workspace, (error, data, response) => {
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
 **projectKey** | **String**| The project in question. This is the actual &#x60;key&#x60; assigned to the project.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**PaginatedDefaultReviewerAndType**](PaginatedDefaultReviewerAndType.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserDelete

> workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserDelete(projectKey, selectedUser, workspace)

Remove the specific user from the project&#39;s default reviewers

Removes a default reviewer from the project.  Example: &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/.../default-reviewers/%7Bf0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6%7D  HTTP/1.1 204 &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.ProjectsApi();
let projectKey = "projectKey_example"; // String | The project in question. This can either be the actual `key` assigned to the project or the `UUID` (surrounded by curly-braces (`{}`)). 
let selectedUser = "selectedUser_example"; // String | This can either be the username or the UUID of the default reviewer, surrounded by curly-braces, for example: `{account UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserDelete(projectKey, selectedUser, workspace, (error, data, response) => {
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
 **projectKey** | **String**| The project in question. This can either be the actual &#x60;key&#x60; assigned to the project or the &#x60;UUID&#x60; (surrounded by curly-braces (&#x60;{}&#x60;)).  | 
 **selectedUser** | **String**| This can either be the username or the UUID of the default reviewer, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserGet

> User workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserGet(projectKey, selectedUser, workspace)

Get a default reviewer

Returns the specified default reviewer.  Example: &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/.../default-reviewers/%7Bf0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6%7D {     \&quot;display_name\&quot;: \&quot;Davis Lee\&quot;,     \&quot;type\&quot;: \&quot;user\&quot;,     \&quot;uuid\&quot;: \&quot;{f0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6}\&quot; } &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.ProjectsApi();
let projectKey = "projectKey_example"; // String | The project in question. This can either be the actual `key` assigned to the project or the `UUID` (surrounded by curly-braces (`{}`)). 
let selectedUser = "selectedUser_example"; // String | This can either be the username or the UUID of the default reviewer, surrounded by curly-braces, for example: `{account UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserGet(projectKey, selectedUser, workspace, (error, data, response) => {
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
 **projectKey** | **String**| The project in question. This can either be the actual &#x60;key&#x60; assigned to the project or the &#x60;UUID&#x60; (surrounded by curly-braces (&#x60;{}&#x60;)).  | 
 **selectedUser** | **String**| This can either be the username or the UUID of the default reviewer, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserPut

> User workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserPut(projectKey, selectedUser, workspace)

Add the specific user as a default reviewer for the project

Adds the specified user to the project&#39;s list of default reviewers. The method is idempotent. Accepts an optional body containing the &#x60;uuid&#x60; of the user to be added.  Example: &#x60;&#x60;&#x60; $ curl -XPUT https://api.bitbucket.org/2.0/.../default-reviewers/%7Bf0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6%7D -d { &#39;uuid&#39;: &#39;{f0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6}&#39; }  HTTP/1.1 204 &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.ProjectsApi();
let projectKey = "projectKey_example"; // String | The project in question. This can either be the actual `key` assigned to the project or the `UUID` (surrounded by curly-braces (`{}`)). 
let selectedUser = "selectedUser_example"; // String | This can either be the username or the UUID of the default reviewer, surrounded by curly-braces, for example: `{account UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.workspacesWorkspaceProjectsProjectKeyDefaultReviewersSelectedUserPut(projectKey, selectedUser, workspace, (error, data, response) => {
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
 **projectKey** | **String**| The project in question. This can either be the actual &#x60;key&#x60; assigned to the project or the &#x60;UUID&#x60; (surrounded by curly-braces (&#x60;{}&#x60;)).  | 
 **selectedUser** | **String**| This can either be the username or the UUID of the default reviewer, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesWorkspaceProjectsProjectKeyDelete

> workspacesWorkspaceProjectsProjectKeyDelete(projectKey, workspace)

Delete a project for a workspace

Deletes this project. This is an irreversible operation.  You cannot delete a project that still contains repositories. To delete the project, [delete](/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-delete) or transfer the repositories first.  Example: &#x60;&#x60;&#x60; $ curl -X DELETE https://api.bitbucket.org/2.0/bbworkspace1/PROJ &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.ProjectsApi();
let projectKey = "projectKey_example"; // String | The project in question. This is the actual `key` assigned to the project. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.workspacesWorkspaceProjectsProjectKeyDelete(projectKey, workspace, (error, data, response) => {
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
 **projectKey** | **String**| The project in question. This is the actual &#x60;key&#x60; assigned to the project.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesWorkspaceProjectsProjectKeyGet

> Project workspacesWorkspaceProjectsProjectKeyGet(projectKey, workspace)

Get a project for a workspace

Returns the requested project.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.ProjectsApi();
let projectKey = "projectKey_example"; // String | The project in question. This is the actual `key` assigned to the project. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.workspacesWorkspaceProjectsProjectKeyGet(projectKey, workspace, (error, data, response) => {
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
 **projectKey** | **String**| The project in question. This is the actual &#x60;key&#x60; assigned to the project.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**Project**](Project.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspacesWorkspaceProjectsProjectKeyPut

> Project workspacesWorkspaceProjectsProjectKeyPut(projectKey, workspace, project)

Update a project for a workspace

Since this endpoint can be used to both update and to create a project, the request body depends on the intent.  #### Creation  See the POST documentation for the project collection for an example of the request body.  Note: The &#x60;key&#x60; should not be specified in the body of request (since it is already present in the URL). The &#x60;name&#x60; is required, everything else is optional.  #### Update  See the POST documentation for the project collection for an example of the request body.  Note: The key is not required in the body (since it is already in the URL). The key may be specified in the body, if the intent is to change the key itself. In such a scenario, the location of the project is changed and is returned in the &#x60;Location&#x60; header of the response.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.ProjectsApi();
let projectKey = "projectKey_example"; // String | The project in question. This is the actual `key` assigned to the project. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
let project = new BitbucketApi.Project(); // Project | 
apiInstance.workspacesWorkspaceProjectsProjectKeyPut(projectKey, workspace, project, (error, data, response) => {
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
 **projectKey** | **String**| The project in question. This is the actual &#x60;key&#x60; assigned to the project.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 
 **project** | [**Project**](Project.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

