# NowPaymentsApi.PayoutsAPIApi

All URIs are relative to *https://api.nowpayments.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verifyPayout**](PayoutsAPIApi.md#verifyPayout) | **POST** /v1/payout/{withdrawals-id}/verify | Verify payout



## verifyPayout

> verifyPayout(withdrawalsId, opts)

Verify payout

This method is required to verify payouts by using your 2fa code.   You’ll have 10 attempts to verify the payout. If it is not verified after 10 attempts, the payout will remain in ‘creating’ status.   Payout will be processed only when it is verified.  Make sure to have your 2fa authentication enabled in your NOWPayments Account (in Account Settings).   When 2fa is disabled, the code automatically goes to your registration email.   The code sent by email is valid for one hour.  Next is a description of the required request fields:  - :batch-withdrawal-id - payout id you received in &#x60;2. Create payout&#x60; method - verification_code - 2fa code you received with your Google Auth app or via email       In order to establish an automatic verification of payouts, you should switch 2FA through the application.   There are several libraries for different frameworks aimed on generating a 2FA codes based on a secret key from your account settings.   e.g: Speakeasy for JavaScript.   We do not recommend to change any default settings.    &#x60;&#x60;&#x60; const 2faVerificationCode &#x3D; speakeasy.totp({       your_2fa_secret_key,       encoding: &#39;base32&#39;, }) &#x60;&#x60;&#x60;

### Example

```javascript
import NowPaymentsApi from 'now_payments_api';

let apiInstance = new NowPaymentsApi.PayoutsAPIApi();
let withdrawalsId = "5000000191"; // String | 
let opts = {
  'xApiKey': "{{your_api_key}}", // String | 
  'verifyPayoutRequest': {"verification_code":"123456"} // VerifyPayoutRequest | 
};
apiInstance.verifyPayout(withdrawalsId, opts, (error, data, response) => {
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
 **withdrawalsId** | **String**|  | 
 **xApiKey** | **String**|  | [optional] 
 **verifyPayoutRequest** | [**VerifyPayoutRequest**](VerifyPayoutRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain

