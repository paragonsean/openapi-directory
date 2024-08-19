# UserApi.DefaultApi

All URIs are relative to *https://api.vonage.com/t/vbc.prod/provisioning*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userCtrlGetUserByID**](DefaultApi.md#userCtrlGetUserByID) | **GET** /api/accounts/{account_id}/users/{user_id} | Get user data by account ID and user ID
[**userCtrlGetUsers**](DefaultApi.md#userCtrlGetUsers) | **GET** /api/accounts/{account_id}/users | Get account users data by account ID



## userCtrlGetUserByID

> UserHalResponse userCtrlGetUserByID(accountId, userId)

Get user data by account ID and user ID

### Example

```javascript
import UserApi from 'user_api';
let defaultClient = UserApi.ApiClient.instance;
// Configure Bearer (OAuth) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new UserApi.DefaultApi();
let accountId = "451496"; // String | The Vonage Business Cloud account ID
let userId = 3.4; // Number | The Vonage Business Cloud user ID
apiInstance.userCtrlGetUserByID(accountId, userId, (error, data, response) => {
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
 **accountId** | **String**| The Vonage Business Cloud account ID | 
 **userId** | **Number**| The Vonage Business Cloud user ID | 

### Return type

[**UserHalResponse**](UserHalResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userCtrlGetUsers

> UsersHalResponse userCtrlGetUsers(accountId, opts)

Get account users data by account ID

### Example

```javascript
import UserApi from 'user_api';
let defaultClient = UserApi.ApiClient.instance;
// Configure Bearer (OAuth) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new UserApi.DefaultApi();
let accountId = "451496"; // String | The Vonage Business Cloud account ID
let opts = {
  'pageSize': 10, // Number | Number of records per page
  'page': 10, // Number | Current page number
  'firstName': "John", // String | Filter by first name
  'lastName': "Smith", // String | Filter by last name
  'loginName': "jsmith", // String | Filter by login name
  'email': "john.smith@example.com" // String | Filter by email address
};
apiInstance.userCtrlGetUsers(accountId, opts, (error, data, response) => {
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
 **accountId** | **String**| The Vonage Business Cloud account ID | 
 **pageSize** | **Number**| Number of records per page | [optional] 
 **page** | **Number**| Current page number | [optional] 
 **firstName** | **String**| Filter by first name | [optional] 
 **lastName** | **String**| Filter by last name | [optional] 
 **loginName** | **String**| Filter by login name | [optional] 
 **email** | **String**| Filter by email address | [optional] 

### Return type

[**UsersHalResponse**](UsersHalResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

