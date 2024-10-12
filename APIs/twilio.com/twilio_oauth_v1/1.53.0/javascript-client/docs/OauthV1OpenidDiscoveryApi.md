# TwilioOauth.OauthV1OpenidDiscoveryApi

All URIs are relative to *https://oauth.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchOpenidDiscovery**](OauthV1OpenidDiscoveryApi.md#fetchOpenidDiscovery) | **GET** /v1/.well-known/openid-configuration | 



## fetchOpenidDiscovery

> OauthV1OpenidDiscovery fetchOpenidDiscovery()



Fetch configuration details about the OpenID Connect Authorization Server

### Example

```javascript
import TwilioOauth from 'twilio_oauth';
let defaultClient = TwilioOauth.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioOauth.OauthV1OpenidDiscoveryApi();
apiInstance.fetchOpenidDiscovery((error, data, response) => {
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

[**OauthV1OpenidDiscovery**](OauthV1OpenidDiscovery.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

