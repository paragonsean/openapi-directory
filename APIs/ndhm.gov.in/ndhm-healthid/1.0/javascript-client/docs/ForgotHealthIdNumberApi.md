# HealthIdService.ForgotHealthIdNumberApi

All URIs are relative to *https://healthidsbx.ndhm.gov.in/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generateAadharOTPUsingPOST1**](ForgotHealthIdNumberApi.md#generateAadharOTPUsingPOST1) | **POST** /v1/forgot/healthId/aadhaar/generateOtp | Generate Aadhaar OTP on registrered mobile number
[**generateMobileOTPUsingPOST**](ForgotHealthIdNumberApi.md#generateMobileOTPUsingPOST) | **POST** /v1/forgot/healthId/mobile/generateOtp | Generate Mobile OTP to start registration
[**retrievalHealthIdByAadharUsingPOST**](ForgotHealthIdNumberApi.md#retrievalHealthIdByAadharUsingPOST) | **POST** /v1/forgot/healthId/aadhaar | Verify aadhar OTP sent as part of forgetHealth id.
[**retrievalHealthIdByMobileUsingPOST**](ForgotHealthIdNumberApi.md#retrievalHealthIdByMobileUsingPOST) | **POST** /v1/forgot/healthId/mobile | Verify Mobile OTP sent as  part of forgetHealth id.



## generateAadharOTPUsingPOST1

> TxnResponse generateAadharOTPUsingPOST1(generateOtpRequest, opts)

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

let apiInstance = new HealthIdService.ForgotHealthIdNumberApi();
let generateOtpRequest = new HealthIdService.AadharOtpGenerateRequestPayLoad(); // AadharOtpGenerateRequestPayLoad | generateOtpRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.generateAadharOTPUsingPOST1(generateOtpRequest, opts, (error, data, response) => {
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


## generateMobileOTPUsingPOST

> TxnResponse generateMobileOTPUsingPOST(generateOtpRequest, opts)

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

let apiInstance = new HealthIdService.ForgotHealthIdNumberApi();
let generateOtpRequest = new HealthIdService.GenerateMobileOTPRequest(); // GenerateMobileOTPRequest | generateOtpRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.generateMobileOTPUsingPOST(generateOtpRequest, opts, (error, data, response) => {
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


## retrievalHealthIdByAadharUsingPOST

> RetrieveHealthIdPayloadResponse retrievalHealthIdByAadharUsingPOST(authAccountAadhaarOTPRequest, opts)

Verify aadhar OTP sent as part of forgetHealth id.

Verify aadhar OTP sent as part of forgetHealth id.

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

let apiInstance = new HealthIdService.ForgotHealthIdNumberApi();
let authAccountAadhaarOTPRequest = new HealthIdService.AuthAccountAadhaarOTPRequest(); // AuthAccountAadhaarOTPRequest | authAccountAadhaarOTPRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.retrievalHealthIdByAadharUsingPOST(authAccountAadhaarOTPRequest, opts, (error, data, response) => {
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
 **authAccountAadhaarOTPRequest** | [**AuthAccountAadhaarOTPRequest**](AuthAccountAadhaarOTPRequest.md)| authAccountAadhaarOTPRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**RetrieveHealthIdPayloadResponse**](RetrieveHealthIdPayloadResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## retrievalHealthIdByMobileUsingPOST

> RetrieveHealthIdPayloadResponse retrievalHealthIdByMobileUsingPOST(retriveHealthIdMobilePayLoad, opts)

Verify Mobile OTP sent as  part of forgetHealth id.

Verify Mobile OTP sent as  part of forgetHealth id.

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

let apiInstance = new HealthIdService.ForgotHealthIdNumberApi();
let retriveHealthIdMobilePayLoad = new HealthIdService.RetriveHealthIdMobilePayLoad(); // RetriveHealthIdMobilePayLoad | retriveHealthIdMobilePayLoad
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.retrievalHealthIdByMobileUsingPOST(retriveHealthIdMobilePayLoad, opts, (error, data, response) => {
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
 **retriveHealthIdMobilePayLoad** | [**RetriveHealthIdMobilePayLoad**](RetriveHealthIdMobilePayLoad.md)| retriveHealthIdMobilePayLoad | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**RetrieveHealthIdPayloadResponse**](RetrieveHealthIdPayloadResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

