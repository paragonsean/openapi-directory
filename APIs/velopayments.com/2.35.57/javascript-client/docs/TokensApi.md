# VeloPaymentsApis.TokensApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resendToken**](TokensApi.md#resendToken) | **POST** /v2/users/{userId}/tokens | Resend a token



## resendToken

> resendToken(userId, resendTokenRequest)

Resend a token

&lt;p&gt;Resend the specified token &lt;/p&gt; &lt;p&gt;The token to resend must already exist for the user &lt;/p&gt; &lt;p&gt;It will be revoked and a new one issued&lt;/p&gt; 

### Example

```javascript
import VeloPaymentsApis from 'velo_payments_apis';
let defaultClient = VeloPaymentsApis.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VeloPaymentsApis.TokensApi();
let userId = "userId_example"; // String | The UUID of the User.
let resendTokenRequest = new VeloPaymentsApis.ResendTokenRequest(); // ResendTokenRequest | The type of token to resend
apiInstance.resendToken(userId, resendTokenRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **String**| The UUID of the User. | 
 **resendTokenRequest** | [**ResendTokenRequest**](ResendTokenRequest.md)| The type of token to resend | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

