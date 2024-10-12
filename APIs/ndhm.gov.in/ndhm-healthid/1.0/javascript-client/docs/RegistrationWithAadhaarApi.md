# HealthIdService.RegistrationWithAadhaarApi

All URIs are relative to *https://healthidsbx.ndhm.gov.in/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAadhaarAccountUsingPOST**](RegistrationWithAadhaarApi.md#createAadhaarAccountUsingPOST) | **POST** /v1/registration/aadhaar/createHealthIdWithPreVerified | Create Health ID using pre-verified Aadhaar &amp; Mobile.
[**generateAadharOTPUsingPOST**](RegistrationWithAadhaarApi.md#generateAadharOTPUsingPOST) | **POST** /v1/registration/aadhaar/generateOtp | Generate Aadhaar OTP on registrered mobile number
[**generateMobileOTPForTxnUsingPOST**](RegistrationWithAadhaarApi.md#generateMobileOTPForTxnUsingPOST) | **POST** /v1/registration/aadhaar/generateMobileOTP | Generate Mobile OTP for verification.
[**getHealthIdNumbersByAadharUsingPOST**](RegistrationWithAadhaarApi.md#getHealthIdNumbersByAadharUsingPOST) | **POST** /v1/registration/aadhaar/search/aadhar | Search health id number using aadhar.
[**resendAadharOTPUsingPOST**](RegistrationWithAadhaarApi.md#resendAadharOTPUsingPOST) | **POST** /v1/registration/aadhaar/resendAadhaarOtp | Resend Aadhaar OTP on registrered mobile number to create Health ID.
[**verifyAadharBioUsingPOST**](RegistrationWithAadhaarApi.md#verifyAadharBioUsingPOST) | **POST** /v1/registration/aadhaar/verifyBio | Verify Aadhaar using biometrics.
[**verifyAadharOTPOnlyUsingPOST**](RegistrationWithAadhaarApi.md#verifyAadharOTPOnlyUsingPOST) | **POST** /v1/registration/aadhaar/verifyOTP | Verify Aadhaar OTP and continue for mobile verification.
[**verifyAadharOTPUsingPOST**](RegistrationWithAadhaarApi.md#verifyAadharOTPUsingPOST) | **POST** /v1/registration/aadhaar/createHealthIdWithAadhaarOtp | Verify Aadhaar OTP on registrered mobile number to create Health ID.
[**verifyMobileOTPForTxnUsingPOST**](RegistrationWithAadhaarApi.md#verifyMobileOTPForTxnUsingPOST) | **POST** /v1/registration/aadhaar/verifyMobileOTP | Verify Mobile OTP in an existing transaction.



## createAadhaarAccountUsingPOST

> CreateAccountJwtResponse createAadhaarAccountUsingPOST(accountRequest, opts)

Create Health ID using pre-verified Aadhaar &amp; Mobile.

Create Health ID using pre-verified Aadhaar &amp; Mobile.

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

let apiInstance = new HealthIdService.RegistrationWithAadhaarApi();
let accountRequest = new HealthIdService.CreateAccountWithPreVerifiedAadhaar(); // CreateAccountWithPreVerifiedAadhaar | accountRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.createAadhaarAccountUsingPOST(accountRequest, opts, (error, data, response) => {
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
 **accountRequest** | [**CreateAccountWithPreVerifiedAadhaar**](CreateAccountWithPreVerifiedAadhaar.md)| accountRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**CreateAccountJwtResponse**](CreateAccountJwtResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## generateAadharOTPUsingPOST

> TxnResponse generateAadharOTPUsingPOST(generateOtpRequest, opts)

Generate Aadhaar OTP on registrered mobile number

Generate Aadhaar OTP on registrered mobile number

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

let apiInstance = new HealthIdService.RegistrationWithAadhaarApi();
let generateOtpRequest = new HealthIdService.AadharOtpGenerateRequestPayLoad(); // AadharOtpGenerateRequestPayLoad | generateOtpRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.generateAadharOTPUsingPOST(generateOtpRequest, opts, (error, data, response) => {
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
 **generateOtpRequest** | [**AadharOtpGenerateRequestPayLoad**](AadharOtpGenerateRequestPayLoad.md)| generateOtpRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TxnResponse**](TxnResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## generateMobileOTPForTxnUsingPOST

> TxnResponse generateMobileOTPForTxnUsingPOST(request, opts)

Generate Mobile OTP for verification.

Generate Mobile OTP to verify mobile number.

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

let apiInstance = new HealthIdService.RegistrationWithAadhaarApi();
let request = new HealthIdService.GenerateMobileOTPForTxnRequest(); // GenerateMobileOTPForTxnRequest | request
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.generateMobileOTPForTxnUsingPOST(request, opts, (error, data, response) => {
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
 **request** | [**GenerateMobileOTPForTxnRequest**](GenerateMobileOTPForTxnRequest.md)| request | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TxnResponse**](TxnResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## getHealthIdNumbersByAadharUsingPOST

> [Object] getHealthIdNumbersByAadharUsingPOST(aadharNumberRequestPayload, opts)

Search health id number using aadhar.

Search health id number using aadhar.

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

let apiInstance = new HealthIdService.RegistrationWithAadhaarApi();
let aadharNumberRequestPayload = new HealthIdService.AadharNumberRequestPayload(); // AadharNumberRequestPayload | aadharNumberRequestPayload
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.getHealthIdNumbersByAadharUsingPOST(aadharNumberRequestPayload, opts, (error, data, response) => {
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
 **aadharNumberRequestPayload** | [**AadharNumberRequestPayload**](AadharNumberRequestPayload.md)| aadharNumberRequestPayload | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**[Object]**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## resendAadharOTPUsingPOST

> CreateAccountJwtResponse resendAadharOTPUsingPOST(request, opts)

Resend Aadhaar OTP on registrered mobile number to create Health ID.

Resend Aadhar OTP on registrered mobile number

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

let apiInstance = new HealthIdService.RegistrationWithAadhaarApi();
let request = new HealthIdService.ResendOTPRequest(); // ResendOTPRequest | request
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.resendAadharOTPUsingPOST(request, opts, (error, data, response) => {
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
 **request** | [**ResendOTPRequest**](ResendOTPRequest.md)| request | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**CreateAccountJwtResponse**](CreateAccountJwtResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## verifyAadharBioUsingPOST

> TxnResponse verifyAadharBioUsingPOST(verifyAadharOtpRequest, opts)

Verify Aadhaar using biometrics.

Verify Aadhaar using biometrics

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

let apiInstance = new HealthIdService.RegistrationWithAadhaarApi();
let verifyAadharOtpRequest = new HealthIdService.VerifyAadhaarWithBio(); // VerifyAadhaarWithBio | verifyAadharOtpRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.verifyAadharBioUsingPOST(verifyAadharOtpRequest, opts, (error, data, response) => {
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
 **verifyAadharOtpRequest** | [**VerifyAadhaarWithBio**](VerifyAadhaarWithBio.md)| verifyAadharOtpRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TxnResponse**](TxnResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## verifyAadharOTPOnlyUsingPOST

> TxnResponse verifyAadharOTPOnlyUsingPOST(verifyAadhaarOtp, opts)

Verify Aadhaar OTP and continue for mobile verification.

Verify Aadhaar OTP received on registrered mobile number

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

let apiInstance = new HealthIdService.RegistrationWithAadhaarApi();
let verifyAadhaarOtp = new HealthIdService.VerifyAadhaarOtp(); // VerifyAadhaarOtp | verifyAadhaarOtp
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.verifyAadharOTPOnlyUsingPOST(verifyAadhaarOtp, opts, (error, data, response) => {
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
 **verifyAadhaarOtp** | [**VerifyAadhaarOtp**](VerifyAadhaarOtp.md)| verifyAadhaarOtp | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TxnResponse**](TxnResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## verifyAadharOTPUsingPOST

> CreateAccountJwtResponse verifyAadharOTPUsingPOST(verifyAadharOtpRequest, opts)

Verify Aadhaar OTP on registrered mobile number to create Health ID.

Verify Aadhar OTP received on registrered mobile number

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

let apiInstance = new HealthIdService.RegistrationWithAadhaarApi();
let verifyAadharOtpRequest = new HealthIdService.CreateAccountWithAadhaarOtp(); // CreateAccountWithAadhaarOtp | verifyAadharOtpRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.verifyAadharOTPUsingPOST(verifyAadharOtpRequest, opts, (error, data, response) => {
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
 **verifyAadharOtpRequest** | [**CreateAccountWithAadhaarOtp**](CreateAccountWithAadhaarOtp.md)| verifyAadharOtpRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**CreateAccountJwtResponse**](CreateAccountJwtResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## verifyMobileOTPForTxnUsingPOST

> TxnResponse verifyMobileOTPForTxnUsingPOST(request, opts)

Verify Mobile OTP in an existing transaction.

Verify Mobile OTP in an existing transaction.

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

let apiInstance = new HealthIdService.RegistrationWithAadhaarApi();
let request = new HealthIdService.VerifyMobileRequest(); // VerifyMobileRequest | request
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.verifyMobileOTPForTxnUsingPOST(request, opts, (error, data, response) => {
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
 **request** | [**VerifyMobileRequest**](VerifyMobileRequest.md)| request | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TxnResponse**](TxnResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

