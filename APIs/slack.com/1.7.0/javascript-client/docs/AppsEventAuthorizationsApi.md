# SlackWebApi.AppsEventAuthorizationsApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appsEventAuthorizationsList**](AppsEventAuthorizationsApi.md#appsEventAuthorizationsList) | **GET** /apps.event.authorizations.list | 



## appsEventAuthorizationsList

> DefaultSuccessTemplate appsEventAuthorizationsList(token, eventContext, opts)



Get a list of authorizations for the given event context. Each authorization represents an app installation that the event is visible to.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AppsEventAuthorizationsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `authorizations:read`
let eventContext = "eventContext_example"; // String | 
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56 // Number | 
};
apiInstance.appsEventAuthorizationsList(token, eventContext, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;authorizations:read&#x60; | 
 **eventContext** | **String**|  | 
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

