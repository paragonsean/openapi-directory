# FilesComApi.UserRequestsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteUserRequestsId**](UserRequestsApi.md#deleteUserRequestsId) | **DELETE** /user_requests/{id} | Delete User Request
[**getUserRequests**](UserRequestsApi.md#getUserRequests) | **GET** /user_requests | List User Requests
[**getUserRequestsId**](UserRequestsApi.md#getUserRequestsId) | **GET** /user_requests/{id} | Show User Request
[**postUserRequests**](UserRequestsApi.md#postUserRequests) | **POST** /user_requests | Create User Request



## deleteUserRequestsId

> deleteUserRequestsId(id)

Delete User Request

Delete User Request

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UserRequestsApi();
let id = 56; // Number | User Request ID.
apiInstance.deleteUserRequestsId(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| User Request ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getUserRequests

> [UserRequestEntity] getUserRequests(opts)

List User Requests

List User Requests

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UserRequestsApi();
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56 // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
};
apiInstance.getUserRequests(opts, (error, data, response) => {
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
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 

### Return type

[**[UserRequestEntity]**](UserRequestEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserRequestsId

> UserRequestEntity getUserRequestsId(id)

Show User Request

Show User Request

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UserRequestsApi();
let id = 56; // Number | User Request ID.
apiInstance.getUserRequestsId(id, (error, data, response) => {
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
 **id** | **Number**| User Request ID. | 

### Return type

[**UserRequestEntity**](UserRequestEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postUserRequests

> UserRequestEntity postUserRequests(details, email, name)

Create User Request

Create User Request

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UserRequestsApi();
let details = "details_example"; // String | Details of the user request
let email = "email_example"; // String | Email of user requested
let name = "name_example"; // String | Name of user requested
apiInstance.postUserRequests(details, email, name, (error, data, response) => {
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
 **details** | **String**| Details of the user request | 
 **email** | **String**| Email of user requested | 
 **name** | **String**| Name of user requested | 

### Return type

[**UserRequestEntity**](UserRequestEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

