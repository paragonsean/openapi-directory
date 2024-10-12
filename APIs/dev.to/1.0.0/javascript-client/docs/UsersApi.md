# ForemApiV1.UsersApi

All URIs are relative to *https://dev.to/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOrgUsers_0**](UsersApi.md#getOrgUsers_0) | **GET** /api/organizations/{username}/users | Organization&#39;s users
[**getUser**](UsersApi.md#getUser) | **GET** /api/users/{id} | A User
[**getUserAllArticles_0**](UsersApi.md#getUserAllArticles_0) | **GET** /api/articles/me/all | User&#39;s all articles
[**getUserArticles_0**](UsersApi.md#getUserArticles_0) | **GET** /api/articles/me | User&#39;s articles
[**getUserMe**](UsersApi.md#getUserMe) | **GET** /api/users/me | The authenticated user
[**getUserPublishedArticles_0**](UsersApi.md#getUserPublishedArticles_0) | **GET** /api/articles/me/published | User&#39;s published articles
[**getUserUnpublishedArticles_0**](UsersApi.md#getUserUnpublishedArticles_0) | **GET** /api/articles/me/unpublished | User&#39;s unpublished articles
[**postAdminUsersCreate**](UsersApi.md#postAdminUsersCreate) | **POST** /api/admin/users | Invite a User
[**suspendUser**](UsersApi.md#suspendUser) | **PUT** /api/users/{id}/suspend | Suspend a User
[**unpublishUser**](UsersApi.md#unpublishUser) | **PUT** /api/users/{id}/unpublish | Unpublish a User&#39;s Articles and Comments



## getOrgUsers_0

> [User] getOrgUsers_0(username, opts)

Organization&#39;s users

This endpoint allows the client to retrieve a list of users belonging to the organization  It supports pagination, each page will contain &#x60;30&#x60; users by default.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';

let apiInstance = new ForemApiV1.UsersApi();
let username = "username_example"; // String | 
let opts = {
  'page': 1, // Number | Pagination page
  'perPage': 30 // Number | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
};
apiInstance.getOrgUsers_0(username, opts, (error, data, response) => {
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
 **username** | **String**|  | 
 **page** | **Number**| Pagination page | [optional] [default to 1]
 **perPage** | **Number**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 30]

### Return type

[**[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUser

> [User] getUser(id)

A User

This endpoint allows the client to retrieve a single user, either by id or by the user&#39;s username.  For complete documentation, see the v0 API docs: https://developers.forem.com/api/v0#tag/users/operation/getUser

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';
let defaultClient = ForemApiV1.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ForemApiV1.UsersApi();
let id = "id_example"; // String | 
apiInstance.getUser(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**[User]**](User.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserAllArticles_0

> [ArticleIndex] getUserAllArticles_0(opts)

User&#39;s all articles

This endpoint allows the client to retrieve a list of all articles on behalf of an authenticated user.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.  It will return both published and unpublished articles with pagination.  Unpublished articles will be at the top of the list in reverse chronological creation order. Published articles will follow in reverse chronological publication order.  By default a page will contain 30 articles.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';
let defaultClient = ForemApiV1.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ForemApiV1.UsersApi();
let opts = {
  'page': 1, // Number | Pagination page
  'perPage': 30 // Number | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
};
apiInstance.getUserAllArticles_0(opts, (error, data, response) => {
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
 **page** | **Number**| Pagination page | [optional] [default to 1]
 **perPage** | **Number**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 30]

### Return type

[**[ArticleIndex]**](ArticleIndex.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserArticles_0

> [ArticleIndex] getUserArticles_0(opts)

User&#39;s articles

This endpoint allows the client to retrieve a list of published articles on behalf of an authenticated user.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.  Published articles will be in reverse chronological publication order.  It will return published articles with pagination. By default a page will contain 30 articles.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';
let defaultClient = ForemApiV1.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ForemApiV1.UsersApi();
let opts = {
  'page': 1, // Number | Pagination page
  'perPage': 30 // Number | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
};
apiInstance.getUserArticles_0(opts, (error, data, response) => {
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
 **page** | **Number**| Pagination page | [optional] [default to 1]
 **perPage** | **Number**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 30]

### Return type

[**[ArticleIndex]**](ArticleIndex.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserMe

> [User] getUserMe()

The authenticated user

This endpoint allows the client to retrieve information about the authenticated user

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';
let defaultClient = ForemApiV1.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ForemApiV1.UsersApi();
apiInstance.getUserMe((error, data, response) => {
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

[**[User]**](User.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserPublishedArticles_0

> [ArticleIndex] getUserPublishedArticles_0(opts)

User&#39;s published articles

This endpoint allows the client to retrieve a list of published articles on behalf of an authenticated user.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.  Published articles will be in reverse chronological publication order.  It will return published articles with pagination. By default a page will contain 30 articles.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';
let defaultClient = ForemApiV1.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ForemApiV1.UsersApi();
let opts = {
  'page': 1, // Number | Pagination page
  'perPage': 30 // Number | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
};
apiInstance.getUserPublishedArticles_0(opts, (error, data, response) => {
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
 **page** | **Number**| Pagination page | [optional] [default to 1]
 **perPage** | **Number**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 30]

### Return type

[**[ArticleIndex]**](ArticleIndex.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserUnpublishedArticles_0

> [ArticleIndex] getUserUnpublishedArticles_0(opts)

User&#39;s unpublished articles

This endpoint allows the client to retrieve a list of unpublished articles on behalf of an authenticated user.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.  Unpublished articles will be in reverse chronological creation order.  It will return unpublished articles with pagination. By default a page will contain 30 articles.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';
let defaultClient = ForemApiV1.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ForemApiV1.UsersApi();
let opts = {
  'page': 1, // Number | Pagination page
  'perPage': 30 // Number | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
};
apiInstance.getUserUnpublishedArticles_0(opts, (error, data, response) => {
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
 **page** | **Number**| Pagination page | [optional] [default to 1]
 **perPage** | **Number**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 30]

### Return type

[**[ArticleIndex]**](ArticleIndex.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postAdminUsersCreate

> postAdminUsersCreate(opts)

Invite a User

This endpoint allows the client to trigger an invitation to the provided email address.          It requires a token from a user with &#x60;super_admin&#x60; privileges.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';
let defaultClient = ForemApiV1.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ForemApiV1.UsersApi();
let opts = {
  'userInviteParam': new ForemApiV1.UserInviteParam() // UserInviteParam | 
};
apiInstance.postAdminUsersCreate(opts, (error, data, response) => {
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
 **userInviteParam** | [**UserInviteParam**](UserInviteParam.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## suspendUser

> suspendUser(id)

Suspend a User

This endpoint allows the client to suspend a user.  The user associated with the API key must have any &#39;admin&#39; or &#39;moderator&#39; role.  This specified user will be assigned the &#39;suspended&#39; role. Suspending a user will stop the user from posting new posts and comments. It doesn&#39;t delete any of the user&#39;s content, just prevents them from creating new content while suspended. Users are not notified of their suspension in the UI, so if you want them to know about this, you must notify them.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';
let defaultClient = ForemApiV1.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ForemApiV1.UsersApi();
let id = 1; // Number | The ID of the user to suspend.
apiInstance.suspendUser(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the user to suspend. | 

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## unpublishUser

> unpublishUser(id)

Unpublish a User&#39;s Articles and Comments

This endpoint allows the client to unpublish all of the articles and comments created by a user.  The user associated with the API key must have any &#39;admin&#39; or &#39;moderator&#39; role.  This specified user&#39;s articles and comments will be unpublished and will no longer be visible to the public. They will remain in the database and will set back to draft status on the specified user&#39;s  dashboard. Any notifications associated with the specified user&#39;s articles and comments will be deleted.  Note this endpoint unpublishes articles and comments asychronously: it will return a 204 NO CONTENT status code immediately, but the articles and comments will not be unpublished until the request is completed on the server.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';
let defaultClient = ForemApiV1.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ForemApiV1.UsersApi();
let id = 1; // Number | The ID of the user to unpublish.
apiInstance.unpublishUser(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the user to unpublish. | 

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

