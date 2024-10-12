# SlackWebApi.DndApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dndEndDnd**](DndApi.md#dndEndDnd) | **POST** /dnd.endDnd | 
[**dndEndSnooze**](DndApi.md#dndEndSnooze) | **POST** /dnd.endSnooze | 
[**dndInfo**](DndApi.md#dndInfo) | **GET** /dnd.info | 
[**dndSetSnooze**](DndApi.md#dndSetSnooze) | **POST** /dnd.setSnooze | 
[**dndTeamInfo**](DndApi.md#dndTeamInfo) | **GET** /dnd.teamInfo | 



## dndEndDnd

> DndEndDndSchema dndEndDnd(token)



Ends the current user&#39;s Do Not Disturb session immediately.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.DndApi();
let token = "token_example"; // String | Authentication token. Requires scope: `dnd:write`
apiInstance.dndEndDnd(token, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;dnd:write&#x60; | 

### Return type

[**DndEndDndSchema**](DndEndDndSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dndEndSnooze

> DndEndSnoozeSchema dndEndSnooze(token)



Ends the current user&#39;s snooze mode immediately.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.DndApi();
let token = "token_example"; // String | Authentication token. Requires scope: `dnd:write`
apiInstance.dndEndSnooze(token, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;dnd:write&#x60; | 

### Return type

[**DndEndSnoozeSchema**](DndEndSnoozeSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dndInfo

> DndInfoSchema dndInfo(opts)



Retrieves a user&#39;s current Do Not Disturb status.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.DndApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `dnd:read`
  'user': "user_example" // String | User to fetch status for (defaults to current user)
};
apiInstance.dndInfo(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;dnd:read&#x60; | [optional] 
 **user** | **String**| User to fetch status for (defaults to current user) | [optional] 

### Return type

[**DndInfoSchema**](DndInfoSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dndSetSnooze

> DndSetSnoozeSchema dndSetSnooze(numMinutes, token)



Turns on Do Not Disturb mode for the current user, or changes its duration.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.DndApi();
let numMinutes = "numMinutes_example"; // String | Number of minutes, from now, to snooze until.
let token = "token_example"; // String | Authentication token. Requires scope: `dnd:write`
apiInstance.dndSetSnooze(numMinutes, token, (error, data, response) => {
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
 **numMinutes** | **String**| Number of minutes, from now, to snooze until. | 
 **token** | **String**| Authentication token. Requires scope: &#x60;dnd:write&#x60; | 

### Return type

[**DndSetSnoozeSchema**](DndSetSnoozeSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## dndTeamInfo

> DefaultSuccessTemplate dndTeamInfo(opts)



Retrieves the Do Not Disturb status for up to 50 users on a team.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.DndApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `dnd:read`
  'users': "users_example" // String | Comma-separated list of users to fetch Do Not Disturb status for
};
apiInstance.dndTeamInfo(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;dnd:read&#x60; | [optional] 
 **users** | **String**| Comma-separated list of users to fetch Do Not Disturb status for | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

