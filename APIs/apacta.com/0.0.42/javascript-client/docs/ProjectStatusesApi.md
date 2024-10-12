# Apacta.ProjectStatusesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectStatusesBulkDeleteDelete**](ProjectStatusesApi.md#projectStatusesBulkDeleteDelete) | **DELETE** /project_statuses/bulkDelete | Bulk delete project statuses
[**projectStatusesGet**](ProjectStatusesApi.md#projectStatusesGet) | **GET** /project_statuses | Get list of project statuses
[**projectStatusesPost**](ProjectStatusesApi.md#projectStatusesPost) | **POST** /project_statuses | Create a new project status
[**projectStatusesProjectStatusIdDelete**](ProjectStatusesApi.md#projectStatusesProjectStatusIdDelete) | **DELETE** /project_statuses/{project_status_id} | Delete a project status
[**projectStatusesProjectStatusIdGet**](ProjectStatusesApi.md#projectStatusesProjectStatusIdGet) | **GET** /project_statuses/{project_status_id} | Get a single project status
[**projectStatusesProjectStatusIdPut**](ProjectStatusesApi.md#projectStatusesProjectStatusIdPut) | **PUT** /project_statuses/{project_status_id} | Edit a project status
[**projectsHasProjectsWithCustomStatusesGet**](ProjectStatusesApi.md#projectsHasProjectsWithCustomStatusesGet) | **GET** /projects/has_projects_with_custom_statuses | Check if the company has projects with custom statuses



## projectStatusesBulkDeleteDelete

> EmptySuccessResponse projectStatusesBulkDeleteDelete(bulkActionRequestBody)

Bulk delete project statuses

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.ProjectStatusesApi();
let bulkActionRequestBody = new Apacta.BulkActionRequestBody(); // BulkActionRequestBody | Project statuses ids
apiInstance.projectStatusesBulkDeleteDelete(bulkActionRequestBody, (error, data, response) => {
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
 **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| Project statuses ids | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectStatusesGet

> ProjectStatusesGet200Response projectStatusesGet()

Get list of project statuses

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectStatusesApi();
apiInstance.projectStatusesGet((error, data, response) => {
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

[**ProjectStatusesGet200Response**](ProjectStatusesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectStatusesPost

> CreateSuccessResponse projectStatusesPost(projectStatusesPostRequest)

Create a new project status

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectStatusesApi();
let projectStatusesPostRequest = new Apacta.ProjectStatusesPostRequest(); // ProjectStatusesPostRequest | 
apiInstance.projectStatusesPost(projectStatusesPostRequest, (error, data, response) => {
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
 **projectStatusesPostRequest** | [**ProjectStatusesPostRequest**](ProjectStatusesPostRequest.md)|  | 

### Return type

[**CreateSuccessResponse**](CreateSuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectStatusesProjectStatusIdDelete

> EmptySuccessResponse projectStatusesProjectStatusIdDelete(projectStatusId)

Delete a project status

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.ProjectStatusesApi();
let projectStatusId = "projectStatusId_example"; // String | 
apiInstance.projectStatusesProjectStatusIdDelete(projectStatusId, (error, data, response) => {
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
 **projectStatusId** | **String**|  | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectStatusesProjectStatusIdGet

> ProjectStatusesProjectStatusIdGet200Response projectStatusesProjectStatusIdGet(projectStatusId)

Get a single project status

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectStatusesApi();
let projectStatusId = "projectStatusId_example"; // String | 
apiInstance.projectStatusesProjectStatusIdGet(projectStatusId, (error, data, response) => {
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
 **projectStatusId** | **String**|  | 

### Return type

[**ProjectStatusesProjectStatusIdGet200Response**](ProjectStatusesProjectStatusIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectStatusesProjectStatusIdPut

> EmptySuccessResponse projectStatusesProjectStatusIdPut(projectStatusId)

Edit a project status

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectStatusesApi();
let projectStatusId = "projectStatusId_example"; // String | 
apiInstance.projectStatusesProjectStatusIdPut(projectStatusId, (error, data, response) => {
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
 **projectStatusId** | **String**|  | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsHasProjectsWithCustomStatusesGet

> ProjectsHasProjectsWithCustomStatusesGet200Response projectsHasProjectsWithCustomStatusesGet()

Check if the company has projects with custom statuses

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectStatusesApi();
apiInstance.projectsHasProjectsWithCustomStatusesGet((error, data, response) => {
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

[**ProjectsHasProjectsWithCustomStatusesGet200Response**](ProjectsHasProjectsWithCustomStatusesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

