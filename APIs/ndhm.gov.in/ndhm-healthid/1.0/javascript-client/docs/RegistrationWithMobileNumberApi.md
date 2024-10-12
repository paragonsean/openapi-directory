# HealthIdService.RegistrationWithMobileNumberApi

All URIs are relative to *https://healthidsbx.ndhm.gov.in/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generateMobileOTPUsingPOST1**](RegistrationWithMobileNumberApi.md#generateMobileOTPUsingPOST1) | **POST** /v1/registration/mobile/generateOtp | Generate Mobile OTP to start registration
[**resentOtpUsingPOST**](RegistrationWithMobileNumberApi.md#resentOtpUsingPOST) | **POST** /v1/registration/mobile/resendOtp | Resend Mobile OTP for Health ID registration
[**verifyMobileOTPUsingPOST**](RegistrationWithMobileNumberApi.md#verifyMobileOTPUsingPOST) | **POST** /v1/registration/mobile/verifyOtp | Verify Mobile OTP sent as part of registration transaction.
[**verifyUserViaMobileUsingPOST**](RegistrationWithMobileNumberApi.md#verifyUserViaMobileUsingPOST) | **POST** /v1/registration/mobile/createHealthId | Create Health ID with verified mobile token



## generateMobileOTPUsingPOST1

> TxnResponse generateMobileOTPUsingPOST1(generateOtpRequest, opts)

Generate Mobile OTP to start registration

Generate Mobile OTP to start registration transaction.

### Example

```javascript
import HealthIdService from 'health_id_service';
let defaultClient = HealthIdService.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';
// Configure API key authorization: X-HIP-ID
let X-HIP-ID = defaultClient.authentications['X-HIP-ID'];
X-HIP-ID.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-HIP-ID.apiKeyPrefix = 'Token';

let apiInstance = new HealthIdService.RegistrationWithMobileNumberApi();
let generateOtpRequest = new HealthIdService.GenerateMobileOTPRequest(); // GenerateMobileOTPRequest | generateOtpRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.generateMobileOTPUsingPOST1(generateOtpRequest, opts, (error, data, response) => {
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
 **generateOtpRequest** | [**GenerateMobileOTPRequest**](GenerateMobileOTPRequest.md)| generateOtpRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TxnResponse**](TxnResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## resentOtpUsingPOST

> Boolean resentOtpUsingPOST(resendRequest, opts)

Resend Mobile OTP for Health ID registration

Resend Mobile OTP in an existing transaction in case previous OTP is not received.

### Example

```javascript
import HealthIdService from 'health_id_service';
let defaultClient = HealthIdService.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';
// Configure API key authorization: X-HIP-ID
let X-HIP-ID = defaultClient.authentications['X-HIP-ID'];
X-HIP-ID.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-HIP-ID.apiKeyPrefix = 'Token';

let apiInstance = new HealthIdService.RegistrationWithMobileNumberApi();
let resendRequest = new HealthIdService.ResendOTPRequest(); // ResendOTPRequest | resendRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.resentOtpUsingPOST(resendRequest, opts, (error, data, response) => {
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
 **resendRequest** | [**ResendOTPRequest**](ResendOTPRequest.md)| resendRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**Boolean**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## verifyMobileOTPUsingPOST

> MobileVerificationToken verifyMobileOTPUsingPOST(verifyOtpRequest, opts)

Verify Mobile OTP sent as part of registration transaction.

Verify Mobile OTP in current registration transaction.

### Example

```javascript
import HealthIdService from 'health_id_service';
let defaultClient = HealthIdService.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';
// Configure API key authorization: X-HIP-ID
let X-HIP-ID = defaultClient.authentications['X-HIP-ID'];
X-HIP-ID.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-HIP-ID.apiKeyPrefix = 'Token';

let apiInstance = new HealthIdService.RegistrationWithMobileNumberApi();
let verifyOtpRequest = new HealthIdService.VerifyMobileRequest(); // VerifyMobileRequest | verifyOtpRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.verifyMobileOTPUsingPOST(verifyOtpRequest, opts, (error, data, response) => {
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
 **verifyOtpRequest** | [**VerifyMobileRequest**](VerifyMobileRequest.md)| verifyOtpRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**MobileVerificationToken**](MobileVerificationToken.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## verifyUserViaMobileUsingPOST

> CreateAccountJwtResponse verifyUserViaMobileUsingPOST(createAccountRequest, opts)

Create Health ID with verified mobile token

### Example

```javascript
import HealthIdService from 'health_id_service';
let defaultClient = HealthIdService.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';
// Configure API key authorization: X-HIP-ID
let X-HIP-ID = defaultClient.authentications['X-HIP-ID'];
X-HIP-ID.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-HIP-ID.apiKeyPrefix = 'Token';

let apiInstance = new HealthIdService.RegistrationWithMobileNumberApi();
let createAccountRequest = new HealthIdService.CreateAccountByVerifiedMobileRequest(); // CreateAccountByVerifiedMobileRequest | createAccountRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.verifyUserViaMobileUsingPOST(createAccountRequest, opts, (error, data, response) => {
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
 **createAccountRequest** | [**CreateAccountByVerifiedMobileRequest**](CreateAccountByVerifiedMobileRequest.md)| createAccountRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**CreateAccountJwtResponse**](CreateAccountJwtResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

