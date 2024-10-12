# SlackWebApi.AdminInviteRequestsApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminInviteRequestsApprove**](AdminInviteRequestsApi.md#adminInviteRequestsApprove) | **POST** /admin.inviteRequests.approve | 
[**adminInviteRequestsDeny**](AdminInviteRequestsApi.md#adminInviteRequestsDeny) | **POST** /admin.inviteRequests.deny | 
[**adminInviteRequestsList**](AdminInviteRequestsApi.md#adminInviteRequestsList) | **GET** /admin.inviteRequests.list | 



## adminInviteRequestsApprove

> DefaultSuccessTemplate adminInviteRequestsApprove(token, inviteRequestId, opts)



Approve a workspace invite request.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminInviteRequestsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.invites:write`
let inviteRequestId = "inviteRequestId_example"; // String | ID of the request to invite.
let opts = {
  'teamId': "teamId_example" // String | ID for the workspace where the invite request was made.
};
apiInstance.adminInviteRequestsApprove(token, inviteRequestId, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.invites:write&#x60; | 
 **inviteRequestId** | **String**| ID of the request to invite. | 
 **teamId** | **String**| ID for the workspace where the invite request was made. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminInviteRequestsDeny

> DefaultSuccessTemplate adminInviteRequestsDeny(token, inviteRequestId, opts)



Deny a workspace invite request.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminInviteRequestsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.invites:write`
let inviteRequestId = "inviteRequestId_example"; // String | ID of the request to invite.
let opts = {
  'teamId': "teamId_example" // String | ID for the workspace where the invite request was made.
};
apiInstance.adminInviteRequestsDeny(token, inviteRequestId, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.invites:write&#x60; | 
 **inviteRequestId** | **String**| ID of the request to invite. | 
 **teamId** | **String**| ID for the workspace where the invite request was made. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminInviteRequestsList

> DefaultSuccessTemplate adminInviteRequestsList(token, opts)



List all pending workspace invite requests.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminInviteRequestsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.invites:read`
let opts = {
  'teamId': "teamId_example", // String | ID for the workspace where the invite requests were made.
  'cursor': "cursor_example", // String | Value of the `next_cursor` field sent as part of the previous API response
  'limit': 56 // Number | The number of results that will be returned by the API on each invocation. Must be between 1 - 1000, both inclusive
};
apiInstance.adminInviteRequestsList(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.invites:read&#x60; | 
 **teamId** | **String**| ID for the workspace where the invite requests were made. | [optional] 
 **cursor** | **String**| Value of the &#x60;next_cursor&#x60; field sent as part of the previous API response | [optional] 
 **limit** | **Number**| The number of results that will be returned by the API on each invocation. Must be between 1 - 1000, both inclusive | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

