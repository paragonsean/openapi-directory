# SlackWebApi.BotsApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**botsInfo**](BotsApi.md#botsInfo) | **GET** /bots.info | 



## botsInfo

> BotsInfoSchema botsInfo(token, opts)



Gets information about a bot user.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.BotsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `users:read`
let opts = {
  'bot': "bot_example" // String | Bot user to get info on
};
apiInstance.botsInfo(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;users:read&#x60; | 
 **bot** | **String**| Bot user to get info on | [optional] 

### Return type

[**BotsInfoSchema**](BotsInfoSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

