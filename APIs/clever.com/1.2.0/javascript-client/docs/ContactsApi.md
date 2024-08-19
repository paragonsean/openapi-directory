# DataApi.ContactsApi

All URIs are relative to *https://api.clever.com/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getContact**](ContactsApi.md#getContact) | **GET** /contacts/{id} | 
[**getContacts**](ContactsApi.md#getContacts) | **GET** /contacts | 
[**getDistrictForStudentContact**](ContactsApi.md#getDistrictForStudentContact) | **GET** /contacts/{id}/district | 
[**getStudentForContact**](ContactsApi.md#getStudentForContact) | **GET** /contacts/{id}/student | 



## getContact

> StudentContactResponse getContact(id)



Returns a specific student contact

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.ContactsApi();
let id = "id_example"; // String | 
apiInstance.getContact(id, (error, data, response) => {
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

[**StudentContactResponse**](StudentContactResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContacts

> StudentContactsResponse getContacts(opts)



Returns a list of student contacts

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.ContactsApi();
let opts = {
  'limit': 56, // Number | 
  'startingAfter': "startingAfter_example", // String | 
  'endingBefore': "endingBefore_example" // String | 
};
apiInstance.getContacts(opts, (error, data, response) => {
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

### Return type

[**StudentContactsResponse**](StudentContactsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDistrictForStudentContact

> DistrictResponse getDistrictForStudentContact(id)



Returns the district for a student contact

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.ContactsApi();
let id = "id_example"; // String | 
apiInstance.getDistrictForStudentContact(id, (error, data, response) => {
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


## getStudentForContact

> StudentResponse getStudentForContact(id)



Returns the student for a student contact

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.ContactsApi();
let id = "id_example"; // String | 
apiInstance.getStudentForContact(id, (error, data, response) => {
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

[**StudentResponse**](StudentResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

