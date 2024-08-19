# DataApi.StudentsApi

All URIs are relative to *https://api.clever.com/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getContactsForStudent**](StudentsApi.md#getContactsForStudent) | **GET** /students/{id}/contacts | 
[**getDistrictForStudent**](StudentsApi.md#getDistrictForStudent) | **GET** /students/{id}/district | 
[**getSchoolForStudent**](StudentsApi.md#getSchoolForStudent) | **GET** /students/{id}/school | 
[**getSectionsForStudent**](StudentsApi.md#getSectionsForStudent) | **GET** /students/{id}/sections | 
[**getStudent**](StudentsApi.md#getStudent) | **GET** /students/{id} | 
[**getStudents**](StudentsApi.md#getStudents) | **GET** /students | 
[**getTeachersForStudent**](StudentsApi.md#getTeachersForStudent) | **GET** /students/{id}/teachers | 



## getContactsForStudent

> StudentContactsForStudentResponse getContactsForStudent(id, opts)



Returns the contacts for a student

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.StudentsApi();
let id = "id_example"; // String | 
let opts = {
  'limit': 56 // Number | 
};
apiInstance.getContactsForStudent(id, opts, (error, data, response) => {
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

### Return type

[**StudentContactsForStudentResponse**](StudentContactsForStudentResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDistrictForStudent

> DistrictResponse getDistrictForStudent(id)



Returns the district for a student

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.StudentsApi();
let id = "id_example"; // String | 
apiInstance.getDistrictForStudent(id, (error, data, response) => {
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


## getSchoolForStudent

> SchoolResponse getSchoolForStudent(id)



Returns the primary school for a student

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.StudentsApi();
let id = "id_example"; // String | 
apiInstance.getSchoolForStudent(id, (error, data, response) => {
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


## getSectionsForStudent

> SectionsResponse getSectionsForStudent(id, opts)



Returns the sections for a student

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.StudentsApi();
let id = "id_example"; // String | 
let opts = {
  'limit': 56, // Number | 
  'startingAfter': "startingAfter_example", // String | 
  'endingBefore': "endingBefore_example" // String | 
};
apiInstance.getSectionsForStudent(id, opts, (error, data, response) => {
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


## getStudent

> StudentResponse getStudent(id, opts)



Returns a specific student

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.StudentsApi();
let id = "id_example"; // String | 
let opts = {
  'include': "include_example" // String | 
};
apiInstance.getStudent(id, opts, (error, data, response) => {
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

[**StudentResponse**](StudentResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStudents

> StudentsResponse getStudents(opts)



Returns a list of students

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.StudentsApi();
let opts = {
  'limit': 56, // Number | 
  'startingAfter': "startingAfter_example", // String | 
  'endingBefore': "endingBefore_example", // String | 
  'where': "where_example" // String | 
};
apiInstance.getStudents(opts, (error, data, response) => {
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

[**StudentsResponse**](StudentsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeachersForStudent

> TeachersResponse getTeachersForStudent(id, opts)



Returns the teachers for a student

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.StudentsApi();
let id = "id_example"; // String | 
let opts = {
  'limit': 56, // Number | 
  'startingAfter': "startingAfter_example", // String | 
  'endingBefore': "endingBefore_example" // String | 
};
apiInstance.getTeachersForStudent(id, opts, (error, data, response) => {
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

[**TeachersResponse**](TeachersResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

