# DataApi.TeachersApi

All URIs are relative to *https://api.clever.com/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDistrictForTeacher**](TeachersApi.md#getDistrictForTeacher) | **GET** /teachers/{id}/district | 
[**getGradeLevelsForTeacher**](TeachersApi.md#getGradeLevelsForTeacher) | **GET** /teachers/{id}/grade_levels | 
[**getSchoolForTeacher**](TeachersApi.md#getSchoolForTeacher) | **GET** /teachers/{id}/school | 
[**getSectionsForTeacher**](TeachersApi.md#getSectionsForTeacher) | **GET** /teachers/{id}/sections | 
[**getStudentsForTeacher**](TeachersApi.md#getStudentsForTeacher) | **GET** /teachers/{id}/students | 
[**getTeacher**](TeachersApi.md#getTeacher) | **GET** /teachers/{id} | 
[**getTeachers**](TeachersApi.md#getTeachers) | **GET** /teachers | 



## getDistrictForTeacher

> DistrictResponse getDistrictForTeacher(id)



Returns the district for a teacher

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.TeachersApi();
let id = "id_example"; // String | 
apiInstance.getDistrictForTeacher(id, (error, data, response) => {
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

[**DistrictResponse**](DistrictResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGradeLevelsForTeacher

> GradeLevelsResponse getGradeLevelsForTeacher(id)



Returns the grade levels for sections a teacher teaches

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.TeachersApi();
let id = "id_example"; // String | 
apiInstance.getGradeLevelsForTeacher(id, (error, data, response) => {
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

[**GradeLevelsResponse**](GradeLevelsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSchoolForTeacher

> SchoolResponse getSchoolForTeacher(id)



Retrieves school info for a teacher.

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.TeachersApi();
let id = "id_example"; // String | 
apiInstance.getSchoolForTeacher(id, (error, data, response) => {
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

[**SchoolResponse**](SchoolResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSectionsForTeacher

> SectionsResponse getSectionsForTeacher(id, opts)



Returns the sections for a teacher

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.TeachersApi();
let id = "id_example"; // String | 
let opts = {
  'limit': 56, // Number | 
  'startingAfter': "startingAfter_example", // String | 
  'endingBefore': "endingBefore_example" // String | 
};
apiInstance.getSectionsForTeacher(id, opts, (error, data, response) => {
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
 **limit** | **Number**|  | [optional] 
 **startingAfter** | **String**|  | [optional] 
 **endingBefore** | **String**|  | [optional] 

### Return type

[**SectionsResponse**](SectionsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStudentsForTeacher

> StudentsResponse getStudentsForTeacher(id, opts)



Returns the students for a teacher

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.TeachersApi();
let id = "id_example"; // String | 
let opts = {
  'limit': 56, // Number | 
  'startingAfter': "startingAfter_example", // String | 
  'endingBefore': "endingBefore_example" // String | 
};
apiInstance.getStudentsForTeacher(id, opts, (error, data, response) => {
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
 **limit** | **Number**|  | [optional] 
 **startingAfter** | **String**|  | [optional] 
 **endingBefore** | **String**|  | [optional] 

### Return type

[**StudentsResponse**](StudentsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeacher

> TeacherResponse getTeacher(id, opts)



Returns a specific teacher

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.TeachersApi();
let id = "id_example"; // String | 
let opts = {
  'include': "include_example" // String | 
};
apiInstance.getTeacher(id, opts, (error, data, response) => {
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
 **include** | **String**|  | [optional] 

### Return type

[**TeacherResponse**](TeacherResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeachers

> TeachersResponse getTeachers(opts)



Returns a list of teachers

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.TeachersApi();
let opts = {
  'limit': 56, // Number | 
  'startingAfter': "startingAfter_example", // String | 
  'endingBefore': "endingBefore_example", // String | 
  'where': "where_example" // String | 
};
apiInstance.getTeachers(opts, (error, data, response) => {
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
 **limit** | **Number**|  | [optional] 
 **startingAfter** | **String**|  | [optional] 
 **endingBefore** | **String**|  | [optional] 
 **where** | **String**|  | [optional] 

### Return type

[**TeachersResponse**](TeachersResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

