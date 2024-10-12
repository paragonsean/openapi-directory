# ForemApiV1.OrganizationsApi

All URIs are relative to *https://dev.to/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOrgArticles**](OrganizationsApi.md#getOrgArticles) | **GET** /api/organizations/{username}/articles | Organization&#39;s Articles
[**getOrgUsers**](OrganizationsApi.md#getOrgUsers) | **GET** /api/organizations/{username}/users | Organization&#39;s users
[**getOrganization**](OrganizationsApi.md#getOrganization) | **GET** /api/organizations/{username} | An organization



## getOrgArticles

> [ArticleIndex] getOrgArticles(username, opts)

Organization&#39;s Articles

This endpoint allows the client to retrieve a list of Articles belonging to the organization  It supports pagination, each page will contain &#x60;30&#x60; users by default.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';

let apiInstance = new ForemApiV1.OrganizationsApi();
let username = "username_example"; // String | 
let opts = {
  'page': 1, // Number | Pagination page
  'perPage': 30 // Number | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
};
apiInstance.getOrgArticles(username, opts, (error, data, response) => {
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

[**[ArticleIndex]**](ArticleIndex.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrgUsers

> [User] getOrgUsers(username, opts)

Organization&#39;s users

This endpoint allows the client to retrieve a list of users belonging to the organization  It supports pagination, each page will contain &#x60;30&#x60; users by default.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';

let apiInstance = new ForemApiV1.OrganizationsApi();
let username = "username_example"; // String | 
let opts = {
  'page': 1, // Number | Pagination page
  'perPage': 30 // Number | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
};
apiInstance.getOrgUsers(username, opts, (error, data, response) => {
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


## getOrganization

> [Organization] getOrganization(username)

An organization

This endpoint allows the client to retrieve a single organization by their username

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';

let apiInstance = new ForemApiV1.OrganizationsApi();
let username = "username_example"; // String | 
apiInstance.getOrganization(username, (error, data, response) => {
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

### Return type

[**[Organization]**](Organization.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

