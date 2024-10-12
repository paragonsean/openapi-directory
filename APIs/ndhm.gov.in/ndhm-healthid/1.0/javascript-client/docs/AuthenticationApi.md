# HealthIdService.AuthenticationApi

All URIs are relative to *https://healthidsbx.ndhm.gov.in/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authAccountPasswordRequestUsingPOST**](AuthenticationApi.md#authAccountPasswordRequestUsingPOST) | **POST** /v1/auth/confirmWithPassword | Authentication with PASSWORD based auth transaction.
[**authWithMobileTokenUsingPOST**](AuthenticationApi.md#authWithMobileTokenUsingPOST) | **POST** /v1/auth/authWithMobileToken | Authenticate using verified Mobile Number and user data
[**authenticateUserUsingPOST**](AuthenticationApi.md#authenticateUserUsingPOST) | **POST** /v1/auth/authWithMobile | Authenticate request to generate Mobile OTP using Health ID number / Health ID
[**authenticateWithPasswordUsingPOST**](AuthenticationApi.md#authenticateWithPasswordUsingPOST) | **POST** /v1/auth/authPassword | Authenticate using Health ID number / Health ID and password
[**certUsingGET**](AuthenticationApi.md#certUsingGET) | **GET** /v1/auth/cert | Auth token public key.
[**confirmWithAadhaarBioUsingPOST**](AuthenticationApi.md#confirmWithAadhaarBioUsingPOST) | **POST** /v1/auth/confirmWithAadhaarBio | Authentication with Aadhaar Biometric based auth transaction.
[**confirmWithAadhaarOtpUsingPOST**](AuthenticationApi.md#confirmWithAadhaarOtpUsingPOST) | **POST** /v1/auth/confirmWithAadhaarOtp | Authentication with Aadhaar OTP based auth transaction.
[**confirmWithDemographicsUsingPOST**](AuthenticationApi.md#confirmWithDemographicsUsingPOST) | **POST** /v1/auth/confirmWithDemographics | Authenticate using demographic data of user.
[**confirmWithMobileUsingPOST**](AuthenticationApi.md#confirmWithMobileUsingPOST) | **POST** /v1/auth/confirmWithMobileOTP | Authentication with Mobile OTP based auth transaction.
[**initiateAuthUsingPOST**](AuthenticationApi.md#initiateAuthUsingPOST) | **POST** /v1/auth/init | Initiate authentication process for given Health ID
[**resendAuthMobileOTPUsingPOST**](AuthenticationApi.md#resendAuthMobileOTPUsingPOST) | **POST** /v1/auth/resendAuthOTP | Resend Aadhaar/Mobile OTP for Authentication Transaction.



## authAccountPasswordRequestUsingPOST

> JwtResponse authAccountPasswordRequestUsingPOST(authenticationRequest, opts)

Authentication with PASSWORD based auth transaction.

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

let apiInstance = new HealthIdService.AuthenticationApi();
let authenticationRequest = new HealthIdService.AuthWithPasswordRequest(); // AuthWithPasswordRequest | authenticationRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.authAccountPasswordRequestUsingPOST(authenticationRequest, opts, (error, data, response) => {
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
 **authenticationRequest** | [**AuthWithPasswordRequest**](AuthWithPasswordRequest.md)| authenticationRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**JwtResponse**](JwtResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## authWithMobileTokenUsingPOST

> JwtResponse authWithMobileTokenUsingPOST(authRequest, opts)

Authenticate using verified Mobile Number and user data

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

let apiInstance = new HealthIdService.AuthenticationApi();
let authRequest = new HealthIdService.AuthWithMobileTxnAndUserData(); // AuthWithMobileTxnAndUserData | authRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.authWithMobileTokenUsingPOST(authRequest, opts, (error, data, response) => {
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
 **authRequest** | [**AuthWithMobileTxnAndUserData**](AuthWithMobileTxnAndUserData.md)| authRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**JwtResponse**](JwtResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## authenticateUserUsingPOST

> TxnResponse authenticateUserUsingPOST(authRequest, opts)

Authenticate request to generate Mobile OTP using Health ID number / Health ID

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

let apiInstance = new HealthIdService.AuthenticationApi();
let authRequest = new HealthIdService.AuthMobileOTPRequest(); // AuthMobileOTPRequest | authRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.authenticateUserUsingPOST(authRequest, opts, (error, data, response) => {
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
 **authRequest** | [**AuthMobileOTPRequest**](AuthMobileOTPRequest.md)| authRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TxnResponse**](TxnResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## authenticateWithPasswordUsingPOST

> JwtResponse authenticateWithPasswordUsingPOST(authenticationRequest, opts)

Authenticate using Health ID number / Health ID and password

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

let apiInstance = new HealthIdService.AuthenticationApi();
let authenticationRequest = new HealthIdService.JwtRequest(); // JwtRequest | authenticationRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.authenticateWithPasswordUsingPOST(authenticationRequest, opts, (error, data, response) => {
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
 **authenticationRequest** | [**JwtRequest**](JwtRequest.md)| authenticationRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**JwtResponse**](JwtResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## certUsingGET

> String certUsingGET(opts)

Auth token public key.

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

let apiInstance = new HealthIdService.AuthenticationApi();
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.certUsingGET(opts, (error, data, response) => {
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
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**String**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## confirmWithAadhaarBioUsingPOST

> JwtResponse confirmWithAadhaarBioUsingPOST(authenticationRequest, opts)

Authentication with Aadhaar Biometric based auth transaction.

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

let apiInstance = new HealthIdService.AuthenticationApi();
let authenticationRequest = new HealthIdService.AuthAccountAadhaarBioRequest(); // AuthAccountAadhaarBioRequest | authenticationRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.confirmWithAadhaarBioUsingPOST(authenticationRequest, opts, (error, data, response) => {
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
 **authenticationRequest** | [**AuthAccountAadhaarBioRequest**](AuthAccountAadhaarBioRequest.md)| authenticationRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**JwtResponse**](JwtResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## confirmWithAadhaarOtpUsingPOST

> JwtResponse confirmWithAadhaarOtpUsingPOST(authenticationRequest, opts)

Authentication with Aadhaar OTP based auth transaction.

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

let apiInstance = new HealthIdService.AuthenticationApi();
let authenticationRequest = new HealthIdService.AuthAccountAadhaarOTPRequest(); // AuthAccountAadhaarOTPRequest | authenticationRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.confirmWithAadhaarOtpUsingPOST(authenticationRequest, opts, (error, data, response) => {
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
 **authenticationRequest** | [**AuthAccountAadhaarOTPRequest**](AuthAccountAadhaarOTPRequest.md)| authenticationRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**JwtResponse**](JwtResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## confirmWithDemographicsUsingPOST

> String confirmWithDemographicsUsingPOST(authenticationRequest, opts)

Authenticate using demographic data of user.

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

let apiInstance = new HealthIdService.AuthenticationApi();
let authenticationRequest = new HealthIdService.AuthAccountWithDemographicsRequest(); // AuthAccountWithDemographicsRequest | authenticationRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.confirmWithDemographicsUsingPOST(authenticationRequest, opts, (error, data, response) => {
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
 **authenticationRequest** | [**AuthAccountWithDemographicsRequest**](AuthAccountWithDemographicsRequest.md)| authenticationRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**String**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## confirmWithMobileUsingPOST

> JwtResponse confirmWithMobileUsingPOST(authenticationRequest, opts)

Authentication with Mobile OTP based auth transaction.

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

let apiInstance = new HealthIdService.AuthenticationApi();
let authenticationRequest = new HealthIdService.AuthAccountMobileOTPRequest(); // AuthAccountMobileOTPRequest | authenticationRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.confirmWithMobileUsingPOST(authenticationRequest, opts, (error, data, response) => {
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
 **authenticationRequest** | [**AuthAccountMobileOTPRequest**](AuthAccountMobileOTPRequest.md)| authenticationRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**JwtResponse**](JwtResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## initiateAuthUsingPOST

> TxnResponse initiateAuthUsingPOST(authRequest, opts)

Initiate authentication process for given Health ID

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

let apiInstance = new HealthIdService.AuthenticationApi();
let authRequest = new HealthIdService.AuthInitRequest(); // AuthInitRequest | authRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.initiateAuthUsingPOST(authRequest, opts, (error, data, response) => {
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
 **authRequest** | [**AuthInitRequest**](AuthInitRequest.md)| authRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TxnResponse**](TxnResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## resendAuthMobileOTPUsingPOST

> Boolean resendAuthMobileOTPUsingPOST(resendOtpRequest, opts)

Resend Aadhaar/Mobile OTP for Authentication Transaction.

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

let apiInstance = new HealthIdService.AuthenticationApi();
let resendOtpRequest = new HealthIdService.ResendOTPRequest(); // ResendOTPRequest | resendOtpRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.resendAuthMobileOTPUsingPOST(resendOtpRequest, opts, (error, data, response) => {
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
 **resendOtpRequest** | [**ResendOTPRequest**](ResendOTPRequest.md)| resendOtpRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**Boolean**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

