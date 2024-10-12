# SlackWebApi.DialogApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dialogOpen**](DialogApi.md#dialogOpen) | **GET** /dialog.open | 



## dialogOpen

> DialogOpenSchema dialogOpen(token, dialog, triggerId)



Open a dialog with a user

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.DialogApi();
let token = "token_example"; // String | Authentication token. Requires scope: `none`
let dialog = "dialog_example"; // String | The dialog definition. This must be a JSON-encoded string.
let triggerId = "triggerId_example"; // String | Exchange a trigger to post to the user.
apiInstance.dialogOpen(token, dialog, triggerId, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;none&#x60; | 
 **dialog** | **String**| The dialog definition. This must be a JSON-encoded string. | 
 **triggerId** | **String**| Exchange a trigger to post to the user. | 

### Return type

[**DialogOpenSchema**](DialogOpenSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

