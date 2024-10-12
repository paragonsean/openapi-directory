# IQualifyManagementApi.CourseMappingsApi

All URIs are relative to *https://api.iqualify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**courseMappingsExternalcourseExternalCourseIdGet**](CourseMappingsApi.md#courseMappingsExternalcourseExternalCourseIdGet) | **GET** /course-mappings/externalcourse/{externalCourseId} | Find course mappings by externalCourseId
[**courseMappingsGet**](CourseMappingsApi.md#courseMappingsGet) | **GET** /course-mappings | Find course mappings
[**courseMappingsOfferingIdExternalCourseIdDelete**](CourseMappingsApi.md#courseMappingsOfferingIdExternalCourseIdDelete) | **DELETE** /course-mappings/{offeringId}/{externalCourseId} | Remove course mapping
[**courseMappingsOfferingIdExternalCourseIdPut**](CourseMappingsApi.md#courseMappingsOfferingIdExternalCourseIdPut) | **PUT** /course-mappings/{offeringId}/{externalCourseId} | Add course mapping
[**courseMappingsOfferingIdGet**](CourseMappingsApi.md#courseMappingsOfferingIdGet) | **GET** /course-mappings/{offeringId} | Find course mappings by offeringId



## courseMappingsExternalcourseExternalCourseIdGet

> [String] courseMappingsExternalcourseExternalCourseIdGet(externalCourseId)

Find course mappings by externalCourseId

Responds with course mapping details by externalCourseId.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.CourseMappingsApi();
let externalCourseId = "externalCourseId_example"; // String | external course's id
apiInstance.courseMappingsExternalcourseExternalCourseIdGet(externalCourseId, (error, data, response) => {
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
 **externalCourseId** | **String**| external course&#39;s id | 

### Return type

**[String]**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## courseMappingsGet

> {String: String} courseMappingsGet()

Find course mappings

Returns all course mappings for course offerings.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.CourseMappingsApi();
apiInstance.courseMappingsGet((error, data, response) => {
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

**{String: String}**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## courseMappingsOfferingIdExternalCourseIdDelete

> [String] courseMappingsOfferingIdExternalCourseIdDelete(offeringId, externalCourseId)

Remove course mapping

Removes the course mapping between the offering and the externalCourseId.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.CourseMappingsApi();
let offeringId = "offeringId_example"; // String | offering's id
let externalCourseId = "externalCourseId_example"; // String | external course's id
apiInstance.courseMappingsOfferingIdExternalCourseIdDelete(offeringId, externalCourseId, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 
 **externalCourseId** | **String**| external course&#39;s id | 

### Return type

**[String]**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## courseMappingsOfferingIdExternalCourseIdPut

> [String] courseMappingsOfferingIdExternalCourseIdPut(offeringId, externalCourseId)

Add course mapping

Creates a mapping between the offering and the externalCourseId.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.CourseMappingsApi();
let offeringId = "offeringId_example"; // String | offering's id
let externalCourseId = "externalCourseId_example"; // String | external course's id
apiInstance.courseMappingsOfferingIdExternalCourseIdPut(offeringId, externalCourseId, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 
 **externalCourseId** | **String**| external course&#39;s id | 

### Return type

**[String]**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## courseMappingsOfferingIdGet

> [String] courseMappingsOfferingIdGet(offeringId)

Find course mappings by offeringId

Responds with course mapping details by offeringId.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.CourseMappingsApi();
let offeringId = "offeringId_example"; // String | offering's id
apiInstance.courseMappingsOfferingIdGet(offeringId, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 

### Return type

**[String]**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

