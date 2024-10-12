# IQualifyManagementApi.CoursesApi

All URIs are relative to *https://api.iqualify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**coursesContentIdActivationsGet**](CoursesApi.md#coursesContentIdActivationsGet) | **GET** /courses/{contentId}/activations | Find activations for a contentId
[**coursesContentIdGet**](CoursesApi.md#coursesContentIdGet) | **GET** /courses/{contentId} | Find course by contentId
[**coursesContentIdPermissionsGet**](CoursesApi.md#coursesContentIdPermissionsGet) | **GET** /courses/{contentId}/permissions | Find users who have access to the contentId provided
[**coursesGet**](CoursesApi.md#coursesGet) | **GET** /courses | Find courses
[**coursesRootContentIdPermissionsUserEmailPost**](CoursesApi.md#coursesRootContentIdPermissionsUserEmailPost) | **POST** /courses/{rootContentId}/permissions/{userEmail} | Update course access



## coursesContentIdActivationsGet

> ActivationResponse coursesContentIdActivationsGet(contentId)

Find activations for a contentId

Responds with all activations for the contentId provided.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.CoursesApi();
let contentId = "contentId_example"; // String | The content Id
apiInstance.coursesContentIdActivationsGet(contentId, (error, data, response) => {
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
 **contentId** | **String**| The content Id | 

### Return type

[**ActivationResponse**](ActivationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## coursesContentIdGet

> CourseMetaResponse coursesContentIdGet(contentId)

Find course by contentId

Responds with a course matching the contentId.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.CoursesApi();
let contentId = "contentId_example"; // String | The content Id
apiInstance.coursesContentIdGet(contentId, (error, data, response) => {
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
 **contentId** | **String**| The content Id | 

### Return type

[**CourseMetaResponse**](CourseMetaResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## coursesContentIdPermissionsGet

> UserPermission coursesContentIdPermissionsGet(contentId)

Find users who have access to the contentId provided

Responds with users who have access to a specific course by contentId.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.CoursesApi();
let contentId = "contentId_example"; // String | The content Id
apiInstance.coursesContentIdPermissionsGet(contentId, (error, data, response) => {
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
 **contentId** | **String**| The content Id | 

### Return type

[**UserPermission**](UserPermission.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## coursesGet

> [CourseResponse] coursesGet()

Find courses

Responds with all courses (draft and published.)

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.CoursesApi();
apiInstance.coursesGet((error, data, response) => {
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

[**[CourseResponse]**](CourseResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## coursesRootContentIdPermissionsUserEmailPost

> CoursesRootContentIdPermissionsUserEmailPost201Response coursesRootContentIdPermissionsUserEmailPost(rootContentId, userEmail, permissionToBeGrantedToTheUser)

Update course access

Provide a user with access to a specific course by rootContentId.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.CoursesApi();
let rootContentId = "rootContentId_example"; // String | The content Id
let userEmail = "userEmail_example"; // String | The user email
let permissionToBeGrantedToTheUser = new IQualifyManagementApi.PermissionToBeGrantedToTheUser(); // PermissionToBeGrantedToTheUser | 
apiInstance.coursesRootContentIdPermissionsUserEmailPost(rootContentId, userEmail, permissionToBeGrantedToTheUser, (error, data, response) => {
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
 **rootContentId** | **String**| The content Id | 
 **userEmail** | **String**| The user email | 
 **permissionToBeGrantedToTheUser** | [**PermissionToBeGrantedToTheUser**](PermissionToBeGrantedToTheUser.md)|  | 

### Return type

[**CoursesRootContentIdPermissionsUserEmailPost201Response**](CoursesRootContentIdPermissionsUserEmailPost201Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

