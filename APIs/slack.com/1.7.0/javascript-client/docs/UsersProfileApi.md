# SlackWebApi.UsersProfileApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersProfileGet**](UsersProfileApi.md#usersProfileGet) | **GET** /users.profile.get | 
[**usersProfileSet**](UsersProfileApi.md#usersProfileSet) | **POST** /users.profile.set | 



## usersProfileGet

> UsersProfileGetSchema usersProfileGet(token, opts)



Retrieves a user&#39;s profile information.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsersProfileApi();
let token = "token_example"; // String | Authentication token. Requires scope: `users.profile:read`
let opts = {
  'includeLabels': true, // Boolean | Include labels for each ID in custom profile fields
  'user': "user_example" // String | User to retrieve profile info for
};
apiInstance.usersProfileGet(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;users.profile:read&#x60; | 
 **includeLabels** | **Boolean**| Include labels for each ID in custom profile fields | [optional] 
 **user** | **String**| User to retrieve profile info for | [optional] 

### Return type

[**UsersProfileGetSchema**](UsersProfileGetSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersProfileSet

> UsersProfileSetSchema usersProfileSet(token, opts)



Set the profile information for a user.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsersProfileApi();
let token = "token_example"; // String | Authentication token. Requires scope: `users.profile:write`
let opts = {
  'name': "name_example", // String | Name of a single key to set. Usable only if `profile` is not passed.
  'profile': "profile_example", // String | Collection of key:value pairs presented as a URL-encoded JSON hash. At most 50 fields may be set. Each field name is limited to 255 characters.
  'user': "user_example", // String | ID of user to change. This argument may only be specified by team admins on paid teams.
  'value': "value_example" // String | Value to set a single key to. Usable only if `profile` is not passed.
};
apiInstance.usersProfileSet(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;users.profile:write&#x60; | 
 **name** | **String**| Name of a single key to set. Usable only if &#x60;profile&#x60; is not passed. | [optional] 
 **profile** | **String**| Collection of key:value pairs presented as a URL-encoded JSON hash. At most 50 fields may be set. Each field name is limited to 255 characters. | [optional] 
 **user** | **String**| ID of user to change. This argument may only be specified by team admins on paid teams. | [optional] 
 **value** | **String**| Value to set a single key to. Usable only if &#x60;profile&#x60; is not passed. | [optional] 

### Return type

[**UsersProfileSetSchema**](UsersProfileSetSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

