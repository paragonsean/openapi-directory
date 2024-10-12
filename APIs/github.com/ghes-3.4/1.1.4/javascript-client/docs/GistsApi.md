# GitHubV3RestApi.GistsApi

All URIs are relative to *https://github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gistsCheckIsStarred**](GistsApi.md#gistsCheckIsStarred) | **GET** /gists/{gist_id}/star | Check if a gist is starred
[**gistsCreate**](GistsApi.md#gistsCreate) | **POST** /gists | Create a gist
[**gistsCreateComment**](GistsApi.md#gistsCreateComment) | **POST** /gists/{gist_id}/comments | Create a gist comment
[**gistsDelete**](GistsApi.md#gistsDelete) | **DELETE** /gists/{gist_id} | Delete a gist
[**gistsDeleteComment**](GistsApi.md#gistsDeleteComment) | **DELETE** /gists/{gist_id}/comments/{comment_id} | Delete a gist comment
[**gistsFork**](GistsApi.md#gistsFork) | **POST** /gists/{gist_id}/forks | Fork a gist
[**gistsGet**](GistsApi.md#gistsGet) | **GET** /gists/{gist_id} | Get a gist
[**gistsGetComment**](GistsApi.md#gistsGetComment) | **GET** /gists/{gist_id}/comments/{comment_id} | Get a gist comment
[**gistsGetRevision**](GistsApi.md#gistsGetRevision) | **GET** /gists/{gist_id}/{sha} | Get a gist revision
[**gistsList**](GistsApi.md#gistsList) | **GET** /gists | List gists for the authenticated user
[**gistsListComments**](GistsApi.md#gistsListComments) | **GET** /gists/{gist_id}/comments | List gist comments
[**gistsListCommits**](GistsApi.md#gistsListCommits) | **GET** /gists/{gist_id}/commits | List gist commits
[**gistsListForUser**](GistsApi.md#gistsListForUser) | **GET** /users/{username}/gists | List gists for a user
[**gistsListForks**](GistsApi.md#gistsListForks) | **GET** /gists/{gist_id}/forks | List gist forks
[**gistsListPublic**](GistsApi.md#gistsListPublic) | **GET** /gists/public | List public gists
[**gistsListStarred**](GistsApi.md#gistsListStarred) | **GET** /gists/starred | List starred gists
[**gistsStar**](GistsApi.md#gistsStar) | **PUT** /gists/{gist_id}/star | Star a gist
[**gistsUnstar**](GistsApi.md#gistsUnstar) | **DELETE** /gists/{gist_id}/star | Unstar a gist
[**gistsUpdate**](GistsApi.md#gistsUpdate) | **PATCH** /gists/{gist_id} | Update a gist
[**gistsUpdateComment**](GistsApi.md#gistsUpdateComment) | **PATCH** /gists/{gist_id}/comments/{comment_id} | Update a gist comment



## gistsCheckIsStarred

> gistsCheckIsStarred(gistId)

Check if a gist is starred



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.GistsApi();
let gistId = "gistId_example"; // String | The unique identifier of the gist.
apiInstance.gistsCheckIsStarred(gistId, (error, data, response) => {
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
 **gistId** | **String**| The unique identifier of the gist. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gistsCreate

> GistSimple gistsCreate(gistsCreateRequest)

Create a gist

Allows you to add a new gist with one or more files.  **Note:** Don&#39;t name your files \&quot;gistfile\&quot; with a numerical suffix. This is the format of the automatic naming scheme that Gist uses internally.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.GistsApi();
let gistsCreateRequest = {"description":"Example of a gist","files":{"README.md":{"content":"Hello World"}},"public":false}; // GistsCreateRequest | 
apiInstance.gistsCreate(gistsCreateRequest, (error, data, response) => {
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
 **gistsCreateRequest** | [**GistsCreateRequest**](GistsCreateRequest.md)|  | 

### Return type

[**GistSimple**](GistSimple.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## gistsCreateComment

> GistComment gistsCreateComment(gistId, gistsCreateCommentRequest)

Create a gist comment



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.GistsApi();
let gistId = "gistId_example"; // String | The unique identifier of the gist.
let gistsCreateCommentRequest = {"body":"This is a comment to a gist"}; // GistsCreateCommentRequest | 
apiInstance.gistsCreateComment(gistId, gistsCreateCommentRequest, (error, data, response) => {
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
 **gistId** | **String**| The unique identifier of the gist. | 
 **gistsCreateCommentRequest** | [**GistsCreateCommentRequest**](GistsCreateCommentRequest.md)|  | 

### Return type

[**GistComment**](GistComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## gistsDelete

> gistsDelete(gistId)

Delete a gist



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.GistsApi();
let gistId = "gistId_example"; // String | The unique identifier of the gist.
apiInstance.gistsDelete(gistId, (error, data, response) => {
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
 **gistId** | **String**| The unique identifier of the gist. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gistsDeleteComment

> gistsDeleteComment(gistId, commentId)

Delete a gist comment



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.GistsApi();
let gistId = "gistId_example"; // String | The unique identifier of the gist.
let commentId = 56; // Number | The unique identifier of the comment.
apiInstance.gistsDeleteComment(gistId, commentId, (error, data, response) => {
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
 **gistId** | **String**| The unique identifier of the gist. | 
 **commentId** | **Number**| The unique identifier of the comment. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gistsFork

> BaseGist gistsFork(gistId)

Fork a gist



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.GistsApi();
let gistId = "gistId_example"; // String | The unique identifier of the gist.
apiInstance.gistsFork(gistId, (error, data, response) => {
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
 **gistId** | **String**| The unique identifier of the gist. | 

### Return type

[**BaseGist**](BaseGist.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gistsGet

> GistSimple gistsGet(gistId)

Get a gist



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.GistsApi();
let gistId = "gistId_example"; // String | The unique identifier of the gist.
apiInstance.gistsGet(gistId, (error, data, response) => {
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
 **gistId** | **String**| The unique identifier of the gist. | 

### Return type

[**GistSimple**](GistSimple.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gistsGetComment

> GistComment gistsGetComment(gistId, commentId)

Get a gist comment



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.GistsApi();
let gistId = "gistId_example"; // String | The unique identifier of the gist.
let commentId = 56; // Number | The unique identifier of the comment.
apiInstance.gistsGetComment(gistId, commentId, (error, data, response) => {
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
 **gistId** | **String**| The unique identifier of the gist. | 
 **commentId** | **Number**| The unique identifier of the comment. | 

### Return type

[**GistComment**](GistComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gistsGetRevision

> GistSimple gistsGetRevision(gistId, sha)

Get a gist revision



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.GistsApi();
let gistId = "gistId_example"; // String | The unique identifier of the gist.
let sha = "sha_example"; // String | 
apiInstance.gistsGetRevision(gistId, sha, (error, data, response) => {
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
 **gistId** | **String**| The unique identifier of the gist. | 
 **sha** | **String**|  | 

### Return type

[**GistSimple**](GistSimple.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gistsList

> [BaseGist] gistsList(opts)

List gists for the authenticated user

Lists the authenticated user&#39;s gists or if called anonymously, this endpoint returns all public gists:

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.GistsApi();
let opts = {
  'since': new Date("2013-10-20T19:20:30+01:00"), // Date | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.gistsList(opts, (error, data, response) => {
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
 **since** | **Date**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[BaseGist]**](BaseGist.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gistsListComments

> [GistComment] gistsListComments(gistId, opts)

List gist comments



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.GistsApi();
let gistId = "gistId_example"; // String | The unique identifier of the gist.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.gistsListComments(gistId, opts, (error, data, response) => {
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
 **gistId** | **String**| The unique identifier of the gist. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[GistComment]**](GistComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gistsListCommits

> [GistCommit] gistsListCommits(gistId, opts)

List gist commits



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.GistsApi();
let gistId = "gistId_example"; // String | The unique identifier of the gist.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.gistsListCommits(gistId, opts, (error, data, response) => {
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
 **gistId** | **String**| The unique identifier of the gist. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[GistCommit]**](GistCommit.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gistsListForUser

> [BaseGist] gistsListForUser(username, opts)

List gists for a user

Lists public gists for the specified user:

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.GistsApi();
let username = "username_example"; // String | The handle for the GitHub user account.
let opts = {
  'since': new Date("2013-10-20T19:20:30+01:00"), // Date | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.gistsListForUser(username, opts, (error, data, response) => {
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
 **since** | **Date**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[BaseGist]**](BaseGist.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gistsListForks

> [GistSimple] gistsListForks(gistId, opts)

List gist forks



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.GistsApi();
let gistId = "gistId_example"; // String | The unique identifier of the gist.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.gistsListForks(gistId, opts, (error, data, response) => {
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
 **gistId** | **String**| The unique identifier of the gist. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[GistSimple]**](GistSimple.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gistsListPublic

> [BaseGist] gistsListPublic(opts)

List public gists

List public gists sorted by most recently updated to least recently updated.  Note: With [pagination](https://docs.github.com/enterprise-server@3.4/rest/overview/resources-in-the-rest-api#pagination), you can fetch up to 3000 gists. For example, you can fetch 100 pages with 30 gists per page or 30 pages with 100 gists per page.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.GistsApi();
let opts = {
  'since': new Date("2013-10-20T19:20:30+01:00"), // Date | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.gistsListPublic(opts, (error, data, response) => {
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
 **since** | **Date**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[BaseGist]**](BaseGist.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gistsListStarred

> [BaseGist] gistsListStarred(opts)

List starred gists

List the authenticated user&#39;s starred gists:

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.GistsApi();
let opts = {
  'since': new Date("2013-10-20T19:20:30+01:00"), // Date | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.gistsListStarred(opts, (error, data, response) => {
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
 **since** | **Date**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[BaseGist]**](BaseGist.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gistsStar

> gistsStar(gistId)

Star a gist

Note that you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@3.4/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.GistsApi();
let gistId = "gistId_example"; // String | The unique identifier of the gist.
apiInstance.gistsStar(gistId, (error, data, response) => {
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
 **gistId** | **String**| The unique identifier of the gist. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gistsUnstar

> gistsUnstar(gistId)

Unstar a gist



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.GistsApi();
let gistId = "gistId_example"; // String | The unique identifier of the gist.
apiInstance.gistsUnstar(gistId, (error, data, response) => {
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
 **gistId** | **String**| The unique identifier of the gist. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gistsUpdate

> GistSimple gistsUpdate(gistId, gistsUpdateRequest)

Update a gist

Allows you to update a gist&#39;s description and to update, delete, or rename gist files. Files from the previous version of the gist that aren&#39;t explicitly changed during an edit are unchanged.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.GistsApi();
let gistId = "gistId_example"; // String | The unique identifier of the gist.
let gistsUpdateRequest = {"files":{"hello.py":null}}; // GistsUpdateRequest | 
apiInstance.gistsUpdate(gistId, gistsUpdateRequest, (error, data, response) => {
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
 **gistId** | **String**| The unique identifier of the gist. | 
 **gistsUpdateRequest** | [**GistsUpdateRequest**](GistsUpdateRequest.md)|  | 

### Return type

[**GistSimple**](GistSimple.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## gistsUpdateComment

> GistComment gistsUpdateComment(gistId, commentId, gistsCreateCommentRequest)

Update a gist comment



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.GistsApi();
let gistId = "gistId_example"; // String | The unique identifier of the gist.
let commentId = 56; // Number | The unique identifier of the comment.
let gistsCreateCommentRequest = {"body":"This is an update to a comment in a gist"}; // GistsCreateCommentRequest | 
apiInstance.gistsUpdateComment(gistId, commentId, gistsCreateCommentRequest, (error, data, response) => {
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
 **gistId** | **String**| The unique identifier of the gist. | 
 **commentId** | **Number**| The unique identifier of the comment. | 
 **gistsCreateCommentRequest** | [**GistsCreateCommentRequest**](GistsCreateCommentRequest.md)|  | 

### Return type

[**GistComment**](GistComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

