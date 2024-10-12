# SlackWebApi.AuthApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authRevoke**](AuthApi.md#authRevoke) | **GET** /auth.revoke | 
[**authTest**](AuthApi.md#authTest) | **GET** /auth.test | 



## authRevoke

> AuthRevokeSchema authRevoke(token, opts)



Revokes a token.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AuthApi();
let token = "token_example"; // String | Authentication token. Requires scope: `none`
let opts = {
  'test': true // Boolean | Setting this parameter to `1` triggers a _testing mode_ where the specified token will not actually be revoked.
};
apiInstance.authRevoke(token, opts, (error, data, response) => {
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
 **test** | **Boolean**| Setting this parameter to &#x60;1&#x60; triggers a _testing mode_ where the specified token will not actually be revoked. | [optional] 

### Return type

[**AuthRevokeSchema**](AuthRevokeSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## authTest

> AuthTestSuccessSchema authTest(token)



Checks authentication &amp; identity.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AuthApi();
let token = "token_example"; // String | Authentication token. Requires scope: `none`
apiInstance.authTest(token, (error, data, response) => {
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

### Return type

[**AuthTestSuccessSchema**](AuthTestSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

