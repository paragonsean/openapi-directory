# SlackWebApi.RemindersApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remindersAdd**](RemindersApi.md#remindersAdd) | **POST** /reminders.add | 
[**remindersComplete**](RemindersApi.md#remindersComplete) | **POST** /reminders.complete | 
[**remindersDelete**](RemindersApi.md#remindersDelete) | **POST** /reminders.delete | 
[**remindersInfo**](RemindersApi.md#remindersInfo) | **GET** /reminders.info | 
[**remindersList**](RemindersApi.md#remindersList) | **GET** /reminders.list | 



## remindersAdd

> RemindersAddSchema remindersAdd(token, text, time, opts)



Creates a reminder.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.RemindersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `reminders:write`
let text = "text_example"; // String | The content of the reminder
let time = "time_example"; // String | When this reminder should happen: the Unix timestamp (up to five years from now), the number of seconds until the reminder (if within 24 hours), or a natural language description (Ex. \\\"in 15 minutes,\\\" or \\\"every Thursday\\\")
let opts = {
  'user': "user_example" // String | The user who will receive the reminder. If no user is specified, the reminder will go to user who created it.
};
apiInstance.remindersAdd(token, text, time, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;reminders:write&#x60; | 
 **text** | **String**| The content of the reminder | 
 **time** | **String**| When this reminder should happen: the Unix timestamp (up to five years from now), the number of seconds until the reminder (if within 24 hours), or a natural language description (Ex. \\\&quot;in 15 minutes,\\\&quot; or \\\&quot;every Thursday\\\&quot;) | 
 **user** | **String**| The user who will receive the reminder. If no user is specified, the reminder will go to user who created it. | [optional] 

### Return type

[**RemindersAddSchema**](RemindersAddSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## remindersComplete

> RemindersCompleteSchema remindersComplete(opts)



Marks a reminder as complete.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.RemindersApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `reminders:write`
  'reminder': "reminder_example" // String | The ID of the reminder to be marked as complete
};
apiInstance.remindersComplete(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;reminders:write&#x60; | [optional] 
 **reminder** | **String**| The ID of the reminder to be marked as complete | [optional] 

### Return type

[**RemindersCompleteSchema**](RemindersCompleteSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## remindersDelete

> RemindersDeleteSchema remindersDelete(opts)



Deletes a reminder.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.RemindersApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `reminders:write`
  'reminder': "reminder_example" // String | The ID of the reminder
};
apiInstance.remindersDelete(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;reminders:write&#x60; | [optional] 
 **reminder** | **String**| The ID of the reminder | [optional] 

### Return type

[**RemindersDeleteSchema**](RemindersDeleteSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## remindersInfo

> RemindersInfoSchema remindersInfo(opts)



Gets information about a reminder.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.RemindersApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `reminders:read`
  'reminder': "reminder_example" // String | The ID of the reminder
};
apiInstance.remindersInfo(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;reminders:read&#x60; | [optional] 
 **reminder** | **String**| The ID of the reminder | [optional] 

### Return type

[**RemindersInfoSchema**](RemindersInfoSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remindersList

> RemindersListSchema remindersList(opts)



Lists all reminders created by or for a given user.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.RemindersApi();
let opts = {
  'token': "token_example" // String | Authentication token. Requires scope: `reminders:read`
};
apiInstance.remindersList(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;reminders:read&#x60; | [optional] 

### Return type

[**RemindersListSchema**](RemindersListSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

