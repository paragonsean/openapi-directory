# Tradeworks.UsersApi

All URIs are relative to *http://devui.magick.nu/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getUsersEmailEmail**](UsersApi.md#getUsersEmailEmail) | **GET** /users/email/{email} | Check if email is available
[**getUsersUsernameUsername**](UsersApi.md#getUsersUsernameUsername) | **GET** /users/username/{username} | Check if username is available
[**postUsers**](UsersApi.md#postUsers) | **POST** /users | Create a new Tradeworks User
[**putUsersPasswordUsername**](UsersApi.md#putUsersPasswordUsername) | **PUT** /users/password/{username} | Update user&#39;s password



## getUsersEmailEmail

> getUsersEmailEmail(email)

Check if email is available

### Example

```javascript
import Tradeworks from 'tradeworks';

let apiInstance = new Tradeworks.UsersApi();
let email = "email_example"; // String | 
apiInstance.getUsersEmailEmail(email, (error, data, response) => {
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
 **email** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getUsersUsernameUsername

> getUsersUsernameUsername(username)

Check if username is available

### Example

```javascript
import Tradeworks from 'tradeworks';

let apiInstance = new Tradeworks.UsersApi();
let username = "username_example"; // String | 
apiInstance.getUsersUsernameUsername(username, (error, data, response) => {
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
 **username** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postUsers

> postUsers(body)

Create a new Tradeworks User

### Example

```javascript
import Tradeworks from 'tradeworks';

let apiInstance = new Tradeworks.UsersApi();
let body = new Tradeworks.UserDTO(); // UserDTO | 
apiInstance.postUsers(body, (error, data, response) => {
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
 **body** | [**UserDTO**](UserDTO.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putUsersPasswordUsername

> putUsersPasswordUsername(username, body)

Update user&#39;s password

### Example

```javascript
import Tradeworks from 'tradeworks';

let apiInstance = new Tradeworks.UsersApi();
let username = "username_example"; // String | 
let body = new Tradeworks.PasswordDTO(); // PasswordDTO | 
apiInstance.putUsersPasswordUsername(username, body, (error, data, response) => {
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
 **username** | **String**|  | 
 **body** | [**PasswordDTO**](PasswordDTO.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

