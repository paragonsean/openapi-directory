# HealthIdService.ProfileApi

All URIs are relative to *https://healthidsbx.ndhm.gov.in/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changePasswordViaAadharUsingPOST**](ProfileApi.md#changePasswordViaAadharUsingPOST) | **POST** /v1/account/change/passwd/byAadhaar | Change password via Aadhar for heath id.
[**changePasswordViaMobileUsingPOST**](ProfileApi.md#changePasswordViaMobileUsingPOST) | **POST** /v1/account/change/passwd/byMobile | Change password via mobile for heath id.
[**changePasswordViaUsingPOST**](ProfileApi.md#changePasswordViaUsingPOST) | **POST** /v1/account/change/password | Change password via password for heath id.
[**deleteAccountUsingDELETE**](ProfileApi.md#deleteAccountUsingDELETE) | **DELETE** /v1/account/profile | Delete account
[**generateAadharOTPUsingGET**](ProfileApi.md#generateAadharOTPUsingGET) | **GET** /v1/account/change/passwd/generateAadhaarOTP | Generate Aadhaar OTP on registrered mobile number.
[**generateCardUsingGET**](ProfileApi.md#generateCardUsingGET) | **GET** /v1/account/getCard | Generate Health ID card in PDF format
[**generateMobileOTPUsingGET**](ProfileApi.md#generateMobileOTPUsingGET) | **GET** /v1/account/change/passwd/generateMobileOTP | Generate Mobile OTP to start registration.
[**generatePngCardUsingGET**](ProfileApi.md#generatePngCardUsingGET) | **GET** /v1/account/getPngCard | Generate Health ID card PNG
[**generateSvgCardUsingGET**](ProfileApi.md#generateSvgCardUsingGET) | **GET** /v1/account/getSvgCard | Generate Health ID card SVG
[**generatereKycAadharOTPUsingPOST**](ProfileApi.md#generatereKycAadharOTPUsingPOST) | **POST** /v1/account/aadhaar/generateOTP | Generate Aadhaar OTP on registrered for link account with aadhar number
[**getAccountInformationUsingGET**](ProfileApi.md#getAccountInformationUsingGET) | **GET** /v1/account/profile | Get account information.
[**getBenefitsUsingGET**](ProfileApi.md#getBenefitsUsingGET) | **GET** /v1/account/benefits | Get List of Benefits associated with HealthID.
[**getQrCodeUsingGET**](ProfileApi.md#getQrCodeUsingGET) | **GET** /v1/account/qrCode | Get Quick Response code in PNG format for this account.
[**updateAccountInformationUsingPOST**](ProfileApi.md#updateAccountInformationUsingPOST) | **POST** /v1/account/profile | Update account information
[**validateTokenUsingPOST**](ProfileApi.md#validateTokenUsingPOST) | **POST** /v1/account/token | Validate auth token
[**verifyAadharOTPOnlyUsingPOST1**](ProfileApi.md#verifyAadharOTPOnlyUsingPOST1) | **POST** /v1/account/aadhaar/verifyOTP | Verify Aadhaar OTP to complete KYC/re-KYC verification.



## changePasswordViaAadharUsingPOST

> String changePasswordViaAadharUsingPOST(xToken, hidOtpRequestPaylaod, opts)

Change password via Aadhar for heath id.

Change password via Aadhar for heath id.

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

let apiInstance = new HealthIdService.ProfileApi();
let xToken = "Bearer X-Token"; // String | Auth Token
let hidOtpRequestPaylaod = new HealthIdService.HidOtpRequestPaylaod(); // HidOtpRequestPaylaod | hidOtpRequestPaylaod
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.changePasswordViaAadharUsingPOST(xToken, hidOtpRequestPaylaod, opts, (error, data, response) => {
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
 **hidOtpRequestPaylaod** | [**HidOtpRequestPaylaod**](HidOtpRequestPaylaod.md)| hidOtpRequestPaylaod | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**String**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## changePasswordViaMobileUsingPOST

> String changePasswordViaMobileUsingPOST(xToken, hidOtpRequestPaylaod, opts)

Change password via mobile for heath id.

Change password via mobile for heath id.

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

let apiInstance = new HealthIdService.ProfileApi();
let xToken = "Bearer X-Token"; // String | Auth Token
let hidOtpRequestPaylaod = new HealthIdService.HidOtpRequestPaylaod(); // HidOtpRequestPaylaod | hidOtpRequestPaylaod
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.changePasswordViaMobileUsingPOST(xToken, hidOtpRequestPaylaod, opts, (error, data, response) => {
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
 **hidOtpRequestPaylaod** | [**HidOtpRequestPaylaod**](HidOtpRequestPaylaod.md)| hidOtpRequestPaylaod | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**String**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## changePasswordViaUsingPOST

> String changePasswordViaUsingPOST(xToken, healthFacilityPasswordRequest, opts)

Change password via password for heath id.

Change password via password for heath id.

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

let apiInstance = new HealthIdService.ProfileApi();
let xToken = "Bearer X-Token"; // String | Auth Token
let healthFacilityPasswordRequest = new HealthIdService.HidChangePasswordRequestPayload(); // HidChangePasswordRequestPayload | healthFacilityPasswordRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.changePasswordViaUsingPOST(xToken, healthFacilityPasswordRequest, opts, (error, data, response) => {
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
 **healthFacilityPasswordRequest** | [**HidChangePasswordRequestPayload**](HidChangePasswordRequestPayload.md)| healthFacilityPasswordRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**String**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## deleteAccountUsingDELETE

> Boolean deleteAccountUsingDELETE(xToken, opts)

Delete account

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

let apiInstance = new HealthIdService.ProfileApi();
let xToken = "Bearer X-Token"; // String | Auth Token
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.deleteAccountUsingDELETE(xToken, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**Boolean**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## generateAadharOTPUsingGET

> String generateAadharOTPUsingGET(xToken, opts)

Generate Aadhaar OTP on registrered mobile number.

Generate Aadhaar OTP on registrered mobile number.

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

let apiInstance = new HealthIdService.ProfileApi();
let xToken = "Bearer X-Token"; // String | Auth Token
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.generateAadharOTPUsingGET(xToken, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**String**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## generateCardUsingGET

> UserDTO generateCardUsingGET(xToken, opts)

Generate Health ID card in PDF format

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

let apiInstance = new HealthIdService.ProfileApi();
let xToken = "Bearer X-Token"; // String | Auth Token
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.generateCardUsingGET(xToken, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**UserDTO**](UserDTO.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## generateMobileOTPUsingGET

> String generateMobileOTPUsingGET(xToken, opts)

Generate Mobile OTP to start registration.

Generate Mobile OTP to start registration.

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

let apiInstance = new HealthIdService.ProfileApi();
let xToken = "Bearer X-Token"; // String | Auth Token
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.generateMobileOTPUsingGET(xToken, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**String**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## generatePngCardUsingGET

> UserDTO generatePngCardUsingGET(xToken, opts)

Generate Health ID card PNG

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

let apiInstance = new HealthIdService.ProfileApi();
let xToken = "Bearer X-Token"; // String | Auth Token
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.generatePngCardUsingGET(xToken, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**UserDTO**](UserDTO.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## generateSvgCardUsingGET

> UserDTO generateSvgCardUsingGET(xToken, opts)

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

let apiInstance = new HealthIdService.ProfileApi();
let xToken = "Bearer X-Token"; // String | Auth Token
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.generateSvgCardUsingGET(xToken, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**UserDTO**](UserDTO.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## generatereKycAadharOTPUsingPOST

> TxnResponse generatereKycAadharOTPUsingPOST(xToken, opts)

Generate Aadhaar OTP on registrered for link account with aadhar number

Generate Aadhaar OTP on registrered for link account with aadhar number

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

let apiInstance = new HealthIdService.ProfileApi();
let xToken = "Bearer X-Token"; // String | Auth Token
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.generatereKycAadharOTPUsingPOST(xToken, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TxnResponse**](TxnResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getAccountInformationUsingGET

> UserDTO getAccountInformationUsingGET(xToken, opts)

Get account information.

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

let apiInstance = new HealthIdService.ProfileApi();
let xToken = "Bearer XToken"; // String | Auth Token
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.getAccountInformationUsingGET(xToken, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**UserDTO**](UserDTO.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getBenefitsUsingGET

> UserDTO getBenefitsUsingGET(xToken, opts)

Get List of Benefits associated with HealthID.

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

let apiInstance = new HealthIdService.ProfileApi();
let xToken = "Bearer XToken"; // String | Auth Token
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.getBenefitsUsingGET(xToken, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**UserDTO**](UserDTO.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getQrCodeUsingGET

> Blob getQrCodeUsingGET(xToken, opts)

Get Quick Response code in PNG format for this account.

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

let apiInstance = new HealthIdService.ProfileApi();
let xToken = "Bearer XToken"; // String | Auth Token
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.getQrCodeUsingGET(xToken, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**Blob**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, image/png


## updateAccountInformationUsingPOST

> UserDTO updateAccountInformationUsingPOST(xToken, request, opts)

Update account information

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

let apiInstance = new HealthIdService.ProfileApi();
let xToken = "Bearer X-Token"; // String | Auth Token
let request = new HealthIdService.UpdateAccountRequest(); // UpdateAccountRequest | request
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.updateAccountInformationUsingPOST(xToken, request, opts, (error, data, response) => {
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
 **request** | [**UpdateAccountRequest**](UpdateAccountRequest.md)| request | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**UserDTO**](UserDTO.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## validateTokenUsingPOST

> Boolean validateTokenUsingPOST(request, opts)

Validate auth token

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

let apiInstance = new HealthIdService.ProfileApi();
let request = new HealthIdService.ValidateTokenRequest(); // ValidateTokenRequest | request
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.validateTokenUsingPOST(request, opts, (error, data, response) => {
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
 **request** | [**ValidateTokenRequest**](ValidateTokenRequest.md)| request | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**Boolean**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## verifyAadharOTPOnlyUsingPOST1

> Boolean verifyAadharOTPOnlyUsingPOST1(xToken, verifyAadhaarOtp, opts)

Verify Aadhaar OTP to complete KYC/re-KYC verification.

Verify Aadhaar OTP to complete KYC/re-KYC verification

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

let apiInstance = new HealthIdService.ProfileApi();
let xToken = "Bearer X-Token"; // String | Auth Token
let verifyAadhaarOtp = new HealthIdService.VerifyAadhaarOtp(); // VerifyAadhaarOtp | verifyAadhaarOtp
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.verifyAadharOTPOnlyUsingPOST1(xToken, verifyAadhaarOtp, opts, (error, data, response) => {
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
 **verifyAadhaarOtp** | [**VerifyAadhaarOtp**](VerifyAadhaarOtp.md)| verifyAadhaarOtp | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**Boolean**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

