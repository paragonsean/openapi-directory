# TwilioOauth.OauthV1OauthApi

All URIs are relative to *https://oauth.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchCerts**](OauthV1OauthApi.md#fetchCerts) | **GET** /v1/certs | 



## fetchCerts

> OauthV1Certs fetchCerts()



Fetches public JWKs

### Example

```javascript
import TwilioOauth from 'twilio_oauth';
let defaultClient = TwilioOauth.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioOauth.OauthV1OauthApi();
apiInstance.fetchCerts((error, data, response) => {
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

[**OauthV1Certs**](OauthV1Certs.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

