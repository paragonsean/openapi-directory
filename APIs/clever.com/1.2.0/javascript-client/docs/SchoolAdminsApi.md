# DataApi.SchoolAdminsApi

All URIs are relative to *https://api.clever.com/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSchoolAdmin**](SchoolAdminsApi.md#getSchoolAdmin) | **GET** /school_admins/{id} | 
[**getSchoolAdmins**](SchoolAdminsApi.md#getSchoolAdmins) | **GET** /school_admins | 
[**getSchoolsForSchoolAdmin**](SchoolAdminsApi.md#getSchoolsForSchoolAdmin) | **GET** /school_admins/{id}/schools | 



## getSchoolAdmin

> SchoolAdminResponse getSchoolAdmin(id, opts)



Returns a specific school admin

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.SchoolAdminsApi();
let id = "id_example"; // String | 
let opts = {
  'include': "include_example" // String | 
};
apiInstance.getSchoolAdmin(id, opts, (error, data, response) => {
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

[**SchoolAdminResponse**](SchoolAdminResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSchoolAdmins

> SchoolAdminsResponse getSchoolAdmins(opts)



Returns a list of school admins

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.SchoolAdminsApi();
let opts = {
  'limit': 56, // Number | 
  'startingAfter': "startingAfter_example", // String | 
  'endingBefore': "endingBefore_example", // String | 
  'where': "where_example" // String | 
};
apiInstance.getSchoolAdmins(opts, (error, data, response) => {
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

[**SchoolAdminsResponse**](SchoolAdminsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSchoolsForSchoolAdmin

> SchoolsResponse getSchoolsForSchoolAdmin(id, opts)



Returns the schools for a school admin

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.SchoolAdminsApi();
let id = "id_example"; // String | 
let opts = {
  'limit': 56, // Number | 
  'startingAfter': "startingAfter_example", // String | 
  'endingBefore': "endingBefore_example" // String | 
};
apiInstance.getSchoolsForSchoolAdmin(id, opts, (error, data, response) => {
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

[**SchoolsResponse**](SchoolsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

