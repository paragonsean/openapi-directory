# SlackWebApi.OauthV2Api

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauthV2Access**](OauthV2Api.md#oauthV2Access) | **GET** /oauth.v2.access | 



## oauthV2Access

> DefaultSuccessTemplate oauthV2Access(code, opts)



Exchanges a temporary OAuth verifier code for an access token.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.OauthV2Api();
let code = "code_example"; // String | The `code` param returned via the OAuth callback.
let opts = {
  'clientId': "clientId_example", // String | Issued when you created your application.
  'clientSecret': "clientSecret_example", // String | Issued when you created your application.
  'redirectUri': "redirectUri_example" // String | This must match the originally submitted URI (if one was sent).
};
apiInstance.oauthV2Access(code, opts, (error, data, response) => {
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

