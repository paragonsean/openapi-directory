# HealthIdService.HealthFacilityApi

All URIs are relative to *https://healthidsbx.ndhm.gov.in/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticateHealthFacilityUsingPOST**](HealthFacilityApi.md#authenticateHealthFacilityUsingPOST) | **POST** /v1/health/facility/authenticate | Generate token for heath facility id.
[**changePasswordUsingPOST**](HealthFacilityApi.md#changePasswordUsingPOST) | **POST** /v1/health/facility/change/password | Change password for heath facility id.
[**createAadhaarAccountUsingPOST1**](HealthFacilityApi.md#createAadhaarAccountUsingPOST1) | **POST** /v1/health/facility/createHealthIdWithPreVerified | Generate Health ID card SVG
[**generateFacilityOTPUsingPOST**](HealthFacilityApi.md#generateFacilityOTPUsingPOST) | **POST** /v1/health/facility/generateOtp | Generate health hacility OTP on registrered mobile number
[**generatePasswordUsingPOST**](HealthFacilityApi.md#generatePasswordUsingPOST) | **POST** /v1/health/facility/generate/password | Generates password for heath facility id.
[**generateSvgCardUsingGET1**](HealthFacilityApi.md#generateSvgCardUsingGET1) | **GET** /v1/health/facility/getSvgCard | generateSvgCard
[**resetPasswordUsingPOST**](HealthFacilityApi.md#resetPasswordUsingPOST) | **POST** /v1/health/facility/reset/password | Reset password for heath facility id.



## authenticateHealthFacilityUsingPOST

> String authenticateHealthFacilityUsingPOST(healthFacilityAuthenticationRequest, opts)

Generate token for heath facility id.

Generate token for heath facility id.

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

let apiInstance = new HealthIdService.HealthFacilityApi();
let healthFacilityAuthenticationRequest = new HealthIdService.HealthFacilityAuthenticationRequest(); // HealthFacilityAuthenticationRequest | healthFacilityAuthenticationRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.authenticateHealthFacilityUsingPOST(healthFacilityAuthenticationRequest, opts, (error, data, response) => {
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
 **healthFacilityAuthenticationRequest** | [**HealthFacilityAuthenticationRequest**](HealthFacilityAuthenticationRequest.md)| healthFacilityAuthenticationRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**String**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## changePasswordUsingPOST

> String changePasswordUsingPOST(healthFacilityPasswordRequest, opts)

Change password for heath facility id.

Change password for heath facility id.

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

let apiInstance = new HealthIdService.HealthFacilityApi();
let healthFacilityPasswordRequest = new HealthIdService.HealthFacilityChangedPasswordRequest(); // HealthFacilityChangedPasswordRequest | healthFacilityPasswordRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.changePasswordUsingPOST(healthFacilityPasswordRequest, opts, (error, data, response) => {
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
 **healthFacilityPasswordRequest** | [**HealthFacilityChangedPasswordRequest**](HealthFacilityChangedPasswordRequest.md)| healthFacilityPasswordRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**String**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## createAadhaarAccountUsingPOST1

> CreateAccountJwtResponse createAadhaarAccountUsingPOST1(accountRequest, opts)

Generate Health ID card SVG

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

let apiInstance = new HealthIdService.HealthFacilityApi();
let accountRequest = new HealthIdService.CreateAccountWithPreVerifiedAadhaar(); // CreateAccountWithPreVerifiedAadhaar | accountRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.createAadhaarAccountUsingPOST1(accountRequest, opts, (error, data, response) => {
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


## generateFacilityOTPUsingPOST

> TxnResponse generateFacilityOTPUsingPOST(xToken, generateOtpRequest, opts)

Generate health hacility OTP on registrered mobile number

Generate health facility OTP on registrered mobile number

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

let apiInstance = new HealthIdService.HealthFacilityApi();
let xToken = "Bearer XToken"; // String | Auth Token
let generateOtpRequest = new HealthIdService.AadharOtpGenerateRequestPayLoad(); // AadharOtpGenerateRequestPayLoad | generateOtpRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.generateFacilityOTPUsingPOST(xToken, generateOtpRequest, opts, (error, data, response) => {
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
 **xToken** | **String**| Auth Token | 
 **generateOtpRequest** | [**AadharOtpGenerateRequestPayLoad**](AadharOtpGenerateRequestPayLoad.md)| generateOtpRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TxnResponse**](TxnResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## generatePasswordUsingPOST

> String generatePasswordUsingPOST(healthFacilityPasswordRequest, opts)

Generates password for heath facility id.

Generates password for heath facility id.

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

let apiInstance = new HealthIdService.HealthFacilityApi();
let healthFacilityPasswordRequest = new HealthIdService.HealthFacilityPasswordRequest(); // HealthFacilityPasswordRequest | healthFacilityPasswordRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.generatePasswordUsingPOST(healthFacilityPasswordRequest, opts, (error, data, response) => {
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
 **healthFacilityPasswordRequest** | [**HealthFacilityPasswordRequest**](HealthFacilityPasswordRequest.md)| healthFacilityPasswordRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**String**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## generateSvgCardUsingGET1

> Blob generateSvgCardUsingGET1(healthID, xToken, opts)

generateSvgCard

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

let apiInstance = new HealthIdService.HealthFacilityApi();
let healthID = "demo@ndhm"; // String | Your health id
let xToken = "Bearer X-Token"; // String | Auth Token
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.generateSvgCardUsingGET1(healthID, xToken, opts, (error, data, response) => {
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
 **healthID** | **String**| Your health id | 
 **xToken** | **String**| Auth Token | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**Blob**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## resetPasswordUsingPOST

> String resetPasswordUsingPOST(healthFacilityPasswordRequest, opts)

Reset password for heath facility id.

Reset password for heath facility id.

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

let apiInstance = new HealthIdService.HealthFacilityApi();
let healthFacilityPasswordRequest = new HealthIdService.HealthFacilityPasswordRequest(); // HealthFacilityPasswordRequest | healthFacilityPasswordRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.resetPasswordUsingPOST(healthFacilityPasswordRequest, opts, (error, data, response) => {
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
 **healthFacilityPasswordRequest** | [**HealthFacilityPasswordRequest**](HealthFacilityPasswordRequest.md)| healthFacilityPasswordRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**String**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

