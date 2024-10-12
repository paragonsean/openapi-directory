# TwilioAccounts.AccountsV1AuthTokenPromotionApi

All URIs are relative to *https://accounts.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**updateAuthTokenPromotion**](AccountsV1AuthTokenPromotionApi.md#updateAuthTokenPromotion) | **POST** /v1/AuthTokens/Promote | 



## updateAuthTokenPromotion

> AccountsV1AuthTokenPromotion updateAuthTokenPromotion()



Promote the secondary Auth Token to primary. After promoting the new token, all requests to Twilio using your old primary Auth Token will result in an error.

### Example

```javascript
import TwilioAccounts from 'twilio_accounts';
let defaultClient = TwilioAccounts.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAccounts.AccountsV1AuthTokenPromotionApi();
apiInstance.updateAuthTokenPromotion((error, data, response) => {
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

[**AccountsV1AuthTokenPromotion**](AccountsV1AuthTokenPromotion.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

