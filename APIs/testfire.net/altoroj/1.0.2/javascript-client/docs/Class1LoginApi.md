# AltoroJRestApi.Class1LoginApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkLogin**](Class1LoginApi.md#checkLogin) | **GET** /login | Check if any user is logged in
[**login**](Class1LoginApi.md#login) | **POST** /login | Login method



## checkLogin

> checkLogin(authorization)

Check if any user is logged in

If a user is loggedin the username will be returned

### Example

```javascript
import AltoroJRestApi from 'altoro_j_rest_api';

let apiInstance = new AltoroJRestApi.Class1LoginApi();
let authorization = "authorization_example"; // String | Authorization token (provided upon successful login)
apiInstance.checkLogin(authorization, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## login

> login(body)

Login method

After a successful login a token is returned. This is a Bearer token. To authenticate with it use the Authorization header and set value to Bearer empty space and the token value.

### Example

```javascript
import AltoroJRestApi from 'altoro_j_rest_api';

let apiInstance = new AltoroJRestApi.Class1LoginApi();
let body = new AltoroJRestApi.Login(); // Login | Username and password combination to allow users to log-in
apiInstance.login(body, (error, data, response) => {
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
 **body** | [**Login**](Login.md)| Username and password combination to allow users to log-in | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

