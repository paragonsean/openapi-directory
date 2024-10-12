# TwilioOauth.OauthV1UserInfoApi

All URIs are relative to *https://oauth.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchUserInfo**](OauthV1UserInfoApi.md#fetchUserInfo) | **GET** /v1/userinfo | 



## fetchUserInfo

> OauthV1UserInfo fetchUserInfo()



Retrieves the consented UserInfo and other claims about the logged-in subject (end-user).

### Example

```javascript
import TwilioOauth from 'twilio_oauth';
let defaultClient = TwilioOauth.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioOauth.OauthV1UserInfoApi();
apiInstance.fetchUserInfo((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**OauthV1UserInfo**](OauthV1UserInfo.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

