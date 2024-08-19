# DataApi.SchoolsApi

All URIs are relative to *https://api.clever.com/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDistrictForSchool**](SchoolsApi.md#getDistrictForSchool) | **GET** /schools/{id}/district | 
[**getSchool**](SchoolsApi.md#getSchool) | **GET** /schools/{id} | 
[**getSchools**](SchoolsApi.md#getSchools) | **GET** /schools | 
[**getSectionsForSchool**](SchoolsApi.md#getSectionsForSchool) | **GET** /schools/{id}/sections | 
[**getStudentsForSchool**](SchoolsApi.md#getStudentsForSchool) | **GET** /schools/{id}/students | 
[**getTeachersForSchool**](SchoolsApi.md#getTeachersForSchool) | **GET** /schools/{id}/teachers | 



## getDistrictForSchool

> DistrictResponse getDistrictForSchool(id)



Returns the district for a school

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.SchoolsApi();
let id = "id_example"; // String | 
apiInstance.getDistrictForSchool(id, (error, data, response) => {
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


## getSchool

> SchoolResponse getSchool(id)



Returns a specific school

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.SchoolsApi();
let id = "id_example"; // String | 
apiInstance.getSchool(id, (error, data, response) => {
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


## getSchools

> SchoolsResponse getSchools(opts)



Returns a list of schools

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.SchoolsApi();
let opts = {
  'limit': 56, // Number | 
  'startingAfter': "startingAfter_example", // String | 
  'endingBefore': "endingBefore_example", // String | 
  'where': "where_example" // String | 
};
apiInstance.getSchools(opts, (error, data, response) => {
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

[**SchoolsResponse**](SchoolsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSectionsForSchool

> SectionsResponse getSectionsForSchool(id, opts)



Returns the sections for a school

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.SchoolsApi();
let id = "id_example"; // String | 
let opts = {
  'limit': 56, // Number | 
  'startingAfter': "startingAfter_example", // String | 
  'endingBefore': "endingBefore_example", // String | 
  'where': "where_example" // String | 
};
apiInstance.getSectionsForSchool(id, opts, (error, data, response) => {
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
 **where** | **String**|  | [optional] 

### Return type

[**SectionsResponse**](SectionsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStudentsForSchool

> StudentsResponse getStudentsForSchool(id, opts)



Returns the students for a school

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.SchoolsApi();
let id = "id_example"; // String | 
let opts = {
  'limit': 56, // Number | 
  'startingAfter': "startingAfter_example", // String | 
  'endingBefore': "endingBefore_example", // String | 
  'where': "where_example" // String | 
};
apiInstance.getStudentsForSchool(id, opts, (error, data, response) => {
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
 **where** | **String**|  | [optional] 

### Return type

[**StudentsResponse**](StudentsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeachersForSchool

> TeachersResponse getTeachersForSchool(id, opts)



Returns the teachers for a school

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.SchoolsApi();
let id = "id_example"; // String | 
let opts = {
  'limit': 56, // Number | 
  'startingAfter': "startingAfter_example", // String | 
  'endingBefore': "endingBefore_example", // String | 
  'where': "where_example" // String | 
};
apiInstance.getTeachersForSchool(id, opts, (error, data, response) => {
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
 **where** | **String**|  | [optional] 

### Return type

[**TeachersResponse**](TeachersResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

