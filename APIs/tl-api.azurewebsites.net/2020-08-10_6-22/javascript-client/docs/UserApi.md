# Api.UserApi

All URIs are relative to *https://tl-api.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userGet**](UserApi.md#userGet) | **GET** /api/User | Get all Users detail This will return all properties related to User entity             
[**userRegisterUser**](UserApi.md#userRegisterUser) | **POST** /api/User/registerUser | Register a new User             
[**userUpdateUser**](UserApi.md#userUpdateUser) | **PUT** /api/User/updateuser | Update an exsisting User             



## userGet

> UserDTO userGet()

Get all Users detail This will return all properties related to User entity             

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.UserApi();
apiInstance.userGet((error, data, response) => {
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

[**UserDTO**](UserDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userRegisterUser

> userRegisterUser(opts)

Register a new User             

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.UserApi();
let opts = {
  'userId': 56, // Number | Indentity number(primary key) for user object. Generated in DB table when inserting a record.             
  'accountNumber': "accountNumber_example", // String | Account number of the user.It can be any stakeholder of the application.even can be a gym.             
  'gymNumber': "gymNumber_example", // String | If this user is a gym, then the gym number.             
  'externalEntityNumber': "externalEntityNumber_example", // String | Entity number that make a relationship with BOX API DB.             
  'name': "name_example", // String | Name of the user.             
  'number': "number_example", // String | Unique number maintain by application to idenify user.             
  'introduceBy': 56, // Number | If Someone introduced this user to the system, then that user's UserId.             
  'guardian': 56, // Number | Gaurdian of the this user if he/she is under 18 years old.             
  'typeId': 56 // Number | Type of the user.             
};
apiInstance.userRegisterUser(opts, (error, data, response) => {
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
 **userId** | **Number**| Indentity number(primary key) for user object. Generated in DB table when inserting a record.              | [optional] 
 **accountNumber** | **String**| Account number of the user.It can be any stakeholder of the application.even can be a gym.              | [optional] 
 **gymNumber** | **String**| If this user is a gym, then the gym number.              | [optional] 
 **externalEntityNumber** | **String**| Entity number that make a relationship with BOX API DB.              | [optional] 
 **name** | **String**| Name of the user.              | [optional] 
 **number** | **String**| Unique number maintain by application to idenify user.              | [optional] 
 **introduceBy** | **Number**| If Someone introduced this user to the system, then that user&#39;s UserId.              | [optional] 
 **guardian** | **Number**| Gaurdian of the this user if he/she is under 18 years old.              | [optional] 
 **typeId** | **Number**| Type of the user.              | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## userUpdateUser

> userUpdateUser(opts)

Update an exsisting User             

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.UserApi();
let opts = {
  'userId': 56, // Number | Indentity number(primary key) for user object. Generated in DB table when inserting a record.             
  'accountNumber': "accountNumber_example", // String | Account number of the user.It can be any stakeholder of the application.even can be a gym.             
  'gymNumber': "gymNumber_example", // String | If this user is a gym, then the gym number.             
  'externalEntityNumber': "externalEntityNumber_example", // String | Entity number that make a relationship with BOX API DB.             
  'name': "name_example", // String | Name of the user.             
  'number': "number_example", // String | Unique number maintain by application to idenify user.             
  'introduceBy': 56, // Number | If Someone introduced this user to the system, then that user's UserId.             
  'guardian': 56, // Number | Gaurdian of the this user if he/she is under 18 years old.             
  'typeId': 56 // Number | Type of the user.             
};
apiInstance.userUpdateUser(opts, (error, data, response) => {
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
 **userId** | **Number**| Indentity number(primary key) for user object. Generated in DB table when inserting a record.              | [optional] 
 **accountNumber** | **String**| Account number of the user.It can be any stakeholder of the application.even can be a gym.              | [optional] 
 **gymNumber** | **String**| If this user is a gym, then the gym number.              | [optional] 
 **externalEntityNumber** | **String**| Entity number that make a relationship with BOX API DB.              | [optional] 
 **name** | **String**| Name of the user.              | [optional] 
 **number** | **String**| Unique number maintain by application to idenify user.              | [optional] 
 **introduceBy** | **Number**| If Someone introduced this user to the system, then that user&#39;s UserId.              | [optional] 
 **guardian** | **Number**| Gaurdian of the this user if he/she is under 18 years old.              | [optional] 
 **typeId** | **Number**| Type of the user.              | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

