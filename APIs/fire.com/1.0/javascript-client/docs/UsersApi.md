# FireFinancialServicesBusinessApi.UsersApi

All URIs are relative to *https://api.fire.com/business*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getUser**](UsersApi.md#getUser) | **GET** /v1/user/{userId} | Returns details of a specific fire.com user.
[**getUsers**](UsersApi.md#getUsers) | **GET** /v1/users | Returns list of all users on your fire.com account



## getUser

> User getUser(userId)

Returns details of a specific fire.com user.

You can retrieve the details of a specific fire.com user

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.UsersApi();
let userId = 14059; // Number | 
apiInstance.getUser(userId, (error, data, response) => {
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
 **userId** | **Number**|  | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsers

> [User] getUsers()

Returns list of all users on your fire.com account

You can retrieve the details of all fire.com users on your acount.

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.UsersApi();
apiInstance.getUsers((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[User]**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

