# FortniteRestApi.UserApi

All URIs are relative to *https://skynewz-api-fortnite.herokuapp.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userPlateformUsernameGet**](UserApi.md#userPlateformUsernameGet) | **GET** /user/{plateform}/{username} | Get a user by username



## userPlateformUsernameGet

> UserPlateformUsernameGet200Response userPlateformUsernameGet(plateform, username)

Get a user by username

### Example

```javascript
import FortniteRestApi from 'fortnite_rest_api';
let defaultClient = FortniteRestApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new FortniteRestApi.UserApi();
let plateform = "plateform_example"; // String | Playing plateform, can be xb1, ps4 or pc
let username = "username_example"; // String | Player username
apiInstance.userPlateformUsernameGet(plateform, username, (error, data, response) => {
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
 **plateform** | **String**| Playing plateform, can be xb1, ps4 or pc | 
 **username** | **String**| Player username | 

### Return type

[**UserPlateformUsernameGet200Response**](UserPlateformUsernameGet200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

