# AltoroJRestApi.Class5AdminApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addUser**](Class5AdminApi.md#addUser) | **POST** /admin/addUser | 
[**changePassword**](Class5AdminApi.md#changePassword) | **POST** /admin/changePassword | 



## addUser

> addUser(authorization, body)



Add new user

### Example

```javascript
import AltoroJRestApi from 'altoro_j_rest_api';

let apiInstance = new AltoroJRestApi.Class5AdminApi();
let authorization = "authorization_example"; // String | Authorization token (provided upon successful login)
let body = new AltoroJRestApi.NewUser(); // NewUser | Details of a new user including first name, last name, desired username and a password
apiInstance.addUser(authorization, body, (error, data, response) => {
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
 **authorization** | **String**| Authorization token (provided upon successful login) | 
 **body** | [**NewUser**](NewUser.md)| Details of a new user including first name, last name, desired username and a password | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## changePassword

> changePassword(authorization, body)



Change user password

### Example

```javascript
import AltoroJRestApi from 'altoro_j_rest_api';

let apiInstance = new AltoroJRestApi.Class5AdminApi();
let authorization = "authorization_example"; // String | Authorization token (provided upon successful login)
let body = new AltoroJRestApi.ChangePassword(); // ChangePassword | Information about the user password to be changed including id and new password
apiInstance.changePassword(authorization, body, (error, data, response) => {
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
 **authorization** | **String**| Authorization token (provided upon successful login) | 
 **body** | [**ChangePassword**](ChangePassword.md)| Information about the user password to be changed including id and new password | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

