# SlackWebApi.AdminUsersSessionApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminUsersSessionInvalidate**](AdminUsersSessionApi.md#adminUsersSessionInvalidate) | **POST** /admin.users.session.invalidate | 
[**adminUsersSessionReset**](AdminUsersSessionApi.md#adminUsersSessionReset) | **POST** /admin.users.session.reset | 



## adminUsersSessionInvalidate

> DefaultSuccessTemplate adminUsersSessionInvalidate(token, sessionId, teamId)



Invalidate a single session for a user by session_id

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminUsersSessionApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.users:write`
let sessionId = 56; // Number | 
let teamId = "teamId_example"; // String | ID of the team that the session belongs to
apiInstance.adminUsersSessionInvalidate(token, sessionId, teamId, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.users:write&#x60; | 
 **sessionId** | **Number**|  | 
 **teamId** | **String**| ID of the team that the session belongs to | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminUsersSessionReset

> DefaultSuccessTemplate adminUsersSessionReset(token, userId, opts)



Wipes all valid sessions on all devices for a given user

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminUsersSessionApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.users:write`
let userId = "userId_example"; // String | The ID of the user to wipe sessions for
let opts = {
  'mobileOnly': true, // Boolean | Only expire mobile sessions (default: false)
  'webOnly': true // Boolean | Only expire web sessions (default: false)
};
apiInstance.adminUsersSessionReset(token, userId, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.users:write&#x60; | 
 **userId** | **String**| The ID of the user to wipe sessions for | 
 **mobileOnly** | **Boolean**| Only expire mobile sessions (default: false) | [optional] 
 **webOnly** | **Boolean**| Only expire web sessions (default: false) | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

