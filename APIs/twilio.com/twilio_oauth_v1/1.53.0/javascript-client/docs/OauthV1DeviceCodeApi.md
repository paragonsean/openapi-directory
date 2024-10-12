# TwilioOauth.OauthV1DeviceCodeApi

All URIs are relative to *https://oauth.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDeviceCode**](OauthV1DeviceCodeApi.md#createDeviceCode) | **POST** /v1/device/code | 



## createDeviceCode

> OauthV1DeviceCode createDeviceCode(clientSid, scopes, opts)



Issues a new Access token (optionally identity_token &amp; refresh_token) in exchange of Oauth grant

### Example

```javascript
import TwilioOauth from 'twilio_oauth';
let defaultClient = TwilioOauth.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioOauth.OauthV1DeviceCodeApi();
let clientSid = "clientSid_example"; // String | A 34 character string that uniquely identifies this OAuth App.
let scopes = ["null"]; // [String] | An Array of scopes for authorization request
let opts = {
  'audiences': ["null"] // [String] | An array of intended audiences for token requests
};
apiInstance.createDeviceCode(clientSid, scopes, opts, (error, data, response) => {
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
 **scopes** | [**[String]**](String.md)| An Array of scopes for authorization request | 
 **audiences** | [**[String]**](String.md)| An array of intended audiences for token requests | [optional] 

### Return type

[**OauthV1DeviceCode**](OauthV1DeviceCode.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

