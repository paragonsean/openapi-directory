# VestorlyApi.SessionsApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](SessionsApi.md#login) | **POST** /sessions | 
[**logout**](SessionsApi.md#logout) | **DELETE** /sessions/{id} | 



## login

> Session login(username, password)



Login To Vestorly Platform

### Example

```javascript
import VestorlyApi from 'vestorly_api';

let apiInstance = new VestorlyApi.SessionsApi();
let username = "username_example"; // String | Username in the vestorly platform
let password = "password_example"; // String | Password in Vestorly Platform
apiInstance.login(username, password, (error, data, response) => {
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
 **username** | **String**| Username in the vestorly platform | 
 **password** | **String**| Password in Vestorly Platform | 

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## logout

> SessionLogoutResponse logout(vestorlyAuth, id)



Logout of the vestorly platform

### Example

```javascript
import VestorlyApi from 'vestorly_api';

let apiInstance = new VestorlyApi.SessionsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Authenication token
let id = "id_example"; // String | ID of pet to session
apiInstance.logout(vestorlyAuth, id, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Authenication token | 
 **id** | **String**| ID of pet to session | 

### Return type

[**SessionLogoutResponse**](SessionLogoutResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

