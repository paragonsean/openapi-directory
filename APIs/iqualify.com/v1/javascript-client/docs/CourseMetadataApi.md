# IQualifyManagementApi.CourseMetadataApi

All URIs are relative to *https://api.iqualify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**coursesContentIdMetadataCategoryPut**](CourseMetadataApi.md#coursesContentIdMetadataCategoryPut) | **PUT** /courses/{contentId}/metadata/category | Update course category
[**coursesContentIdMetadataLevelPut**](CourseMetadataApi.md#coursesContentIdMetadataLevelPut) | **PUT** /courses/{contentId}/metadata/level | Update course level
[**coursesContentIdMetadataTagsPut**](CourseMetadataApi.md#coursesContentIdMetadataTagsPut) | **PUT** /courses/{contentId}/metadata/tags | Update course tags
[**coursesContentIdMetadataTopicPut**](CourseMetadataApi.md#coursesContentIdMetadataTopicPut) | **PUT** /courses/{contentId}/metadata/topic | Update course topic



## coursesContentIdMetadataCategoryPut

> CourseMetaResponse coursesContentIdMetadataCategoryPut(contentId, coursesContentIdMetadataCategoryPutRequest)

Update course category

Add or update course category in the metadata of a course.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.CourseMetadataApi();
let contentId = "contentId_example"; // String | The content Id
let coursesContentIdMetadataCategoryPutRequest = new IQualifyManagementApi.CoursesContentIdMetadataCategoryPutRequest(); // CoursesContentIdMetadataCategoryPutRequest | 
apiInstance.coursesContentIdMetadataCategoryPut(contentId, coursesContentIdMetadataCategoryPutRequest, (error, data, response) => {
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
 **coursesContentIdMetadataCategoryPutRequest** | [**CoursesContentIdMetadataCategoryPutRequest**](CoursesContentIdMetadataCategoryPutRequest.md)|  | 

### Return type

[**CourseMetaResponse**](CourseMetaResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## coursesContentIdMetadataLevelPut

> CourseMetaResponse coursesContentIdMetadataLevelPut(contentId, coursesContentIdMetadataLevelPutRequest)

Update course level

Add or update the course level in the metadata of a course.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.CourseMetadataApi();
let contentId = "contentId_example"; // String | The content Id
let coursesContentIdMetadataLevelPutRequest = new IQualifyManagementApi.CoursesContentIdMetadataLevelPutRequest(); // CoursesContentIdMetadataLevelPutRequest | 
apiInstance.coursesContentIdMetadataLevelPut(contentId, coursesContentIdMetadataLevelPutRequest, (error, data, response) => {
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
 **coursesContentIdMetadataLevelPutRequest** | [**CoursesContentIdMetadataLevelPutRequest**](CoursesContentIdMetadataLevelPutRequest.md)|  | 

### Return type

[**CourseMetaResponse**](CourseMetaResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## coursesContentIdMetadataTagsPut

> CourseMetaResponse coursesContentIdMetadataTagsPut(contentId, coursesContentIdMetadataTagsPutRequest)

Update course tags

Add or update course tags in the metadata of a course.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.CourseMetadataApi();
let contentId = "contentId_example"; // String | The content Id
let coursesContentIdMetadataTagsPutRequest = new IQualifyManagementApi.CoursesContentIdMetadataTagsPutRequest(); // CoursesContentIdMetadataTagsPutRequest | 
apiInstance.coursesContentIdMetadataTagsPut(contentId, coursesContentIdMetadataTagsPutRequest, (error, data, response) => {
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
 **coursesContentIdMetadataTagsPutRequest** | [**CoursesContentIdMetadataTagsPutRequest**](CoursesContentIdMetadataTagsPutRequest.md)|  | 

### Return type

[**CourseMetaResponse**](CourseMetaResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## coursesContentIdMetadataTopicPut

> CourseMetaResponse coursesContentIdMetadataTopicPut(contentId, coursesContentIdMetadataTopicPutRequest)

Update course topic

Add or update the course topic in the metadata of a course.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.CourseMetadataApi();
let contentId = "contentId_example"; // String | The content Id
let coursesContentIdMetadataTopicPutRequest = new IQualifyManagementApi.CoursesContentIdMetadataTopicPutRequest(); // CoursesContentIdMetadataTopicPutRequest | 
apiInstance.coursesContentIdMetadataTopicPut(contentId, coursesContentIdMetadataTopicPutRequest, (error, data, response) => {
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
 **coursesContentIdMetadataTopicPutRequest** | [**CoursesContentIdMetadataTopicPutRequest**](CoursesContentIdMetadataTopicPutRequest.md)|  | 

### Return type

[**CourseMetaResponse**](CourseMetaResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

