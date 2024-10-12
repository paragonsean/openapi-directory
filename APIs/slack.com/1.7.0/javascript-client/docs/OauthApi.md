# SlackWebApi.OauthApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauthAccess**](OauthApi.md#oauthAccess) | **GET** /oauth.access | 
[**oauthToken**](OauthApi.md#oauthToken) | **GET** /oauth.token | 
[**oauthV2Access_0**](OauthApi.md#oauthV2Access_0) | **GET** /oauth.v2.access | 



## oauthAccess

> DefaultSuccessTemplate oauthAccess(opts)



Exchanges a temporary OAuth verifier code for an access token.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.OauthApi();
let opts = {
  'clientId': "clientId_example", // String | Issued when you created your application.
  'clientSecret': "clientSecret_example", // String | Issued when you created your application.
  'code': "code_example", // String | The `code` param returned via the OAuth callback.
  'redirectUri': "redirectUri_example", // String | This must match the originally submitted URI (if one was sent).
  'singleChannel': true // Boolean | Request the user to add your app only to a single channel. Only valid with a [legacy workspace app](https://api.slack.com/legacy-workspace-apps).
};
apiInstance.oauthAccess(opts, (error, data, response) => {
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
 **clientId** | **String**| Issued when you created your application. | [optional] 
 **clientSecret** | **String**| Issued when you created your application. | [optional] 
 **code** | **String**| The &#x60;code&#x60; param returned via the OAuth callback. | [optional] 
 **redirectUri** | **String**| This must match the originally submitted URI (if one was sent). | [optional] 
 **singleChannel** | **Boolean**| Request the user to add your app only to a single channel. Only valid with a [legacy workspace app](https://api.slack.com/legacy-workspace-apps). | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## oauthToken

> DefaultSuccessTemplate oauthToken(opts)



Exchanges a temporary OAuth verifier code for a workspace token.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.OauthApi();
let opts = {
  'clientId': "clientId_example", // String | Issued when you created your application.
  'clientSecret': "clientSecret_example", // String | Issued when you created your application.
  'code': "code_example", // String | The `code` param returned via the OAuth callback.
  'redirectUri': "redirectUri_example", // String | This must match the originally submitted URI (if one was sent).
  'singleChannel': true // Boolean | Request the user to add your app only to a single channel.
};
apiInstance.oauthToken(opts, (error, data, response) => {
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
 **clientId** | **String**| Issued when you created your application. | [optional] 
 **clientSecret** | **String**| Issued when you created your application. | [optional] 
 **code** | **String**| The &#x60;code&#x60; param returned via the OAuth callback. | [optional] 
 **redirectUri** | **String**| This must match the originally submitted URI (if one was sent). | [optional] 
 **singleChannel** | **Boolean**| Request the user to add your app only to a single channel. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## oauthV2Access_0

> DefaultSuccessTemplate oauthV2Access_0(code, opts)



Exchanges a temporary OAuth verifier code for an access token.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.OauthApi();
let code = "code_example"; // String | The `code` param returned via the OAuth callback.
let opts = {
  'clientId': "clientId_example", // String | Issued when you created your application.
  'clientSecret': "clientSecret_example", // String | Issued when you created your application.
  'redirectUri': "redirectUri_example" // String | This must match the originally submitted URI (if one was sent).
};
apiInstance.oauthV2Access_0(code, opts, (error, data, response) => {
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
 **code** | **String**| The &#x60;code&#x60; param returned via the OAuth callback. | 
 **clientId** | **String**| Issued when you created your application. | [optional] 
 **clientSecret** | **String**| Issued when you created your application. | [optional] 
 **redirectUri** | **String**| This must match the originally submitted URI (if one was sent). | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

