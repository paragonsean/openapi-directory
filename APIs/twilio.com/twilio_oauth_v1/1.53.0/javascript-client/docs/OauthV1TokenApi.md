# TwilioOauth.OauthV1TokenApi

All URIs are relative to *https://oauth.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createToken**](OauthV1TokenApi.md#createToken) | **POST** /v1/token | 



## createToken

> OauthV1Token createToken(clientSid, grantType, opts)



Issues a new Access token (optionally identity_token &amp; refresh_token) in exchange of Oauth grant

### Example

```javascript
import TwilioOauth from 'twilio_oauth';
let defaultClient = TwilioOauth.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioOauth.OauthV1TokenApi();
let clientSid = "clientSid_example"; // String | A 34 character string that uniquely identifies this OAuth App.
let grantType = "grantType_example"; // String | Grant type is a credential representing resource owner's authorization which can be used by client to obtain access token.
let opts = {
  'clientSecret': "clientSecret_example", // String | The credential for confidential OAuth App.
  'code': "code_example", // String | JWT token related to the authorization code grant type.
  'codeVerifier': "codeVerifier_example", // String | A code which is generation cryptographically.
  'deviceCode': "deviceCode_example", // String | JWT token related to the device code grant type.
  'deviceId': "deviceId_example", // String | The Id of the device associated with the token (refresh token).
  'refreshToken': "refreshToken_example" // String | JWT token related to the refresh token grant type.
};
apiInstance.createToken(clientSid, grantType, opts, (error, data, response) => {
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
 **clientSid** | **String**| A 34 character string that uniquely identifies this OAuth App. | 
 **grantType** | **String**| Grant type is a credential representing resource owner&#39;s authorization which can be used by client to obtain access token. | 
 **clientSecret** | **String**| The credential for confidential OAuth App. | [optional] 
 **code** | **String**| JWT token related to the authorization code grant type. | [optional] 
 **codeVerifier** | **String**| A code which is generation cryptographically. | [optional] 
 **deviceCode** | **String**| JWT token related to the device code grant type. | [optional] 
 **deviceId** | **String**| The Id of the device associated with the token (refresh token). | [optional] 
 **refreshToken** | **String**| JWT token related to the refresh token grant type. | [optional] 

### Return type

[**OauthV1Token**](OauthV1Token.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

