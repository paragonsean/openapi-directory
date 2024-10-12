# HealthIdService.IntegratedProgramsApi

All URIs are relative to *https://healthidsbx.ndhm.gov.in/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createHealthIdByDemoAuthUsingPOST**](IntegratedProgramsApi.md#createHealthIdByDemoAuthUsingPOST) | **POST** /v1/hid/benefit/createHealthId/demo/auth | Create health id using Aadhaar Demo Auth.
[**createHealthIdByMobileUsingPOST**](IntegratedProgramsApi.md#createHealthIdByMobileUsingPOST) | **POST** /v1/hid/benefit/mobile/createHealthId | Create health id using mobile Authentication.
[**delinkHidBenefitUsingPOST**](IntegratedProgramsApi.md#delinkHidBenefitUsingPOST) | **POST** /v1/hid/benefit/delink | De-Linked with hid.
[**findByAadharUsingPOST**](IntegratedProgramsApi.md#findByAadharUsingPOST) | **POST** /v1/hid/benefit/search/aadhaar | Search health id number using aadhar or aadhar token.
[**findByHealthIdUsingPOST**](IntegratedProgramsApi.md#findByHealthIdUsingPOST) | **POST** /v1/hid/benefit/search/healthIdNumber | Search benefit using health id number.
[**generateAadharOTPUsingPOST2**](IntegratedProgramsApi.md#generateAadharOTPUsingPOST2) | **POST** /v1/hid/benefit/aadhaar/generateOtp | Generate Aadhaar OTP on registrered mobile number
[**generateMobileOtpUsingPOST**](IntegratedProgramsApi.md#generateMobileOtpUsingPOST) | **POST** /v1/hid/benefit/mobile/generateOtp | Generate mobile OTP on registrered mobile number
[**linkHidBenefitUsingPOST**](IntegratedProgramsApi.md#linkHidBenefitUsingPOST) | **POST** /v1/hid/benefit/link | Linked with hid.
[**notifyBenefitUsingPOST**](IntegratedProgramsApi.md#notifyBenefitUsingPOST) | **POST** /v1/hid/benefit/notify/benefit | Create health id using notify Benefit.
[**updateAccountInformationUsingPOST1**](IntegratedProgramsApi.md#updateAccountInformationUsingPOST1) | **POST** /v1/hid/benefit/update/profile | Update account information
[**updateMobileInformationUsingPOST**](IntegratedProgramsApi.md#updateMobileInformationUsingPOST) | **POST** /v1/hid/benefit/update/mobile | Update mobile number for account.
[**updateStatusUsingPOST**](IntegratedProgramsApi.md#updateStatusUsingPOST) | **POST** /v1/hid/benefit/update/status | Update health id status .
[**verifyAadharOtpUsingPOST**](IntegratedProgramsApi.md#verifyAadharOtpUsingPOST) | **POST** /v1/hid/benefit/aadhaar/verifyAadharOtp | Create health id using Aadhaar Number Otp.
[**verifyBioUsingPOST**](IntegratedProgramsApi.md#verifyBioUsingPOST) | **POST** /v1/hid/benefit/aadhaar/verifyBio | Create health id using Biometric Authentication.



## createHealthIdByDemoAuthUsingPOST

> HidBenefitRequestPayload createHealthIdByDemoAuthUsingPOST(createHIdDemoAuthRequest, opts)

Create health id using Aadhaar Demo Auth.

Create health id using Aadhaar Demo Auth.

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

let apiInstance = new HealthIdService.IntegratedProgramsApi();
let createHIdDemoAuthRequest = new HealthIdService.CreateHIdDemoAuthRequest(); // CreateHIdDemoAuthRequest | createHIdDemoAuthRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.createHealthIdByDemoAuthUsingPOST(createHIdDemoAuthRequest, opts, (error, data, response) => {
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
 **createHIdDemoAuthRequest** | [**CreateHIdDemoAuthRequest**](CreateHIdDemoAuthRequest.md)| createHIdDemoAuthRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**HidBenefitRequestPayload**](HidBenefitRequestPayload.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## createHealthIdByMobileUsingPOST

> TxnResponse createHealthIdByMobileUsingPOST(createHidMobileRequest, opts)

Create health id using mobile Authentication.

Create health id using mobile Authentication.

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

let apiInstance = new HealthIdService.IntegratedProgramsApi();
let createHidMobileRequest = new HealthIdService.CreateHidMobileRequest(); // CreateHidMobileRequest | createHidMobileRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.createHealthIdByMobileUsingPOST(createHidMobileRequest, opts, (error, data, response) => {
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
 **createHidMobileRequest** | [**CreateHidMobileRequest**](CreateHidMobileRequest.md)| createHidMobileRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**TxnResponse**](TxnResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## delinkHidBenefitUsingPOST

> HidBenefitLinkedResponsePayload delinkHidBenefitUsingPOST(hidBenefitLinkedRequestPayload, opts)

De-Linked with hid.

De-Linked with hid.

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

let apiInstance = new HealthIdService.IntegratedProgramsApi();
let hidBenefitLinkedRequestPayload = new HealthIdService.HidBenefitDelinkRequestPayload(); // HidBenefitDelinkRequestPayload | hidBenefitLinkedRequestPayload
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.delinkHidBenefitUsingPOST(hidBenefitLinkedRequestPayload, opts, (error, data, response) => {
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
 **hidBenefitLinkedRequestPayload** | [**HidBenefitDelinkRequestPayload**](HidBenefitDelinkRequestPayload.md)| hidBenefitLinkedRequestPayload | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**HidBenefitLinkedResponsePayload**](HidBenefitLinkedResponsePayload.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## findByAadharUsingPOST

> [Object] findByAadharUsingPOST(aadharNumberRequestPayload, opts)

Search health id number using aadhar or aadhar token.

Search health id number using aadhar or aadhar token.

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

let apiInstance = new HealthIdService.IntegratedProgramsApi();
let aadharNumberRequestPayload = new HealthIdService.AadharNumberRequestPayload(); // AadharNumberRequestPayload | aadharNumberRequestPayload
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.findByAadharUsingPOST(aadharNumberRequestPayload, opts, (error, data, response) => {
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


## findByHealthIdUsingPOST

> [HidBenefitSearchResponsePayload] findByHealthIdUsingPOST(searchRequest, opts)

Search benefit using health id number.

Search benefit using health id number

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

let apiInstance = new HealthIdService.IntegratedProgramsApi();
let searchRequest = new HealthIdService.HidBenefitNameSearchRequest(); // HidBenefitNameSearchRequest | searchRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.findByHealthIdUsingPOST(searchRequest, opts, (error, data, response) => {
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
 **searchRequest** | [**HidBenefitNameSearchRequest**](HidBenefitNameSearchRequest.md)| searchRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**[HidBenefitSearchResponsePayload]**](HidBenefitSearchResponsePayload.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## generateAadharOTPUsingPOST2

> TxnResponse generateAadharOTPUsingPOST2(generateOtpRequest, opts)

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

let apiInstance = new HealthIdService.IntegratedProgramsApi();
let generateOtpRequest = new HealthIdService.AadharOtpGenerateRequestPayLoad(); // AadharOtpGenerateRequestPayLoad | generateOtpRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.generateAadharOTPUsingPOST2(generateOtpRequest, opts, (error, data, response) => {
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


## generateMobileOtpUsingPOST

> TxnResponse generateMobileOtpUsingPOST(generateOtpRequest, opts)

Generate mobile OTP on registrered mobile number

Generate mobile OTP on registrered mobile number

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

let apiInstance = new HealthIdService.IntegratedProgramsApi();
let generateOtpRequest = new HealthIdService.GenerateMobileOTPRequest(); // GenerateMobileOTPRequest | generateOtpRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.generateMobileOtpUsingPOST(generateOtpRequest, opts, (error, data, response) => {
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


## linkHidBenefitUsingPOST

> HidBenefitLinkedResponsePayload linkHidBenefitUsingPOST(hidBenefitLinkedRequestPayload, opts)

Linked with hid.

Linked with hid.

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

let apiInstance = new HealthIdService.IntegratedProgramsApi();
let hidBenefitLinkedRequestPayload = new HealthIdService.HidBenefitLinkedRequestPayload(); // HidBenefitLinkedRequestPayload | hidBenefitLinkedRequestPayload
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.linkHidBenefitUsingPOST(hidBenefitLinkedRequestPayload, opts, (error, data, response) => {
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
 **hidBenefitLinkedRequestPayload** | [**HidBenefitLinkedRequestPayload**](HidBenefitLinkedRequestPayload.md)| hidBenefitLinkedRequestPayload | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**HidBenefitLinkedResponsePayload**](HidBenefitLinkedResponsePayload.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## notifyBenefitUsingPOST

> HidBenefitRequestPayload notifyBenefitUsingPOST(createHidNotifyBenefitRequest, opts)

Create health id using notify Benefit.

Create health id using notify Benefit.

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

let apiInstance = new HealthIdService.IntegratedProgramsApi();
let createHidNotifyBenefitRequest = new HealthIdService.CreateHidNotifyBenefitRequest(); // CreateHidNotifyBenefitRequest | createHidNotifyBenefitRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.notifyBenefitUsingPOST(createHidNotifyBenefitRequest, opts, (error, data, response) => {
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
 **createHidNotifyBenefitRequest** | [**CreateHidNotifyBenefitRequest**](CreateHidNotifyBenefitRequest.md)| createHidNotifyBenefitRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**HidBenefitRequestPayload**](HidBenefitRequestPayload.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## updateAccountInformationUsingPOST1

> UserDTO updateAccountInformationUsingPOST1(request, opts)

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

let apiInstance = new HealthIdService.IntegratedProgramsApi();
let request = new HealthIdService.HidUpdateAccountRequest(); // HidUpdateAccountRequest | request
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.updateAccountInformationUsingPOST1(request, opts, (error, data, response) => {
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
 **request** | [**HidUpdateAccountRequest**](HidUpdateAccountRequest.md)| request | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**UserDTO**](UserDTO.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## updateMobileInformationUsingPOST

> UserDTO updateMobileInformationUsingPOST(request, opts)

Update mobile number for account.

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

let apiInstance = new HealthIdService.IntegratedProgramsApi();
let request = new HealthIdService.HidUpdateMobiletRequest(); // HidUpdateMobiletRequest | request
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.updateMobileInformationUsingPOST(request, opts, (error, data, response) => {
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
 **request** | [**HidUpdateMobiletRequest**](HidUpdateMobiletRequest.md)| request | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**UserDTO**](UserDTO.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## updateStatusUsingPOST

> Boolean updateStatusUsingPOST(generateOtpRequest, opts)

Update health id status .

Update health id status.

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

let apiInstance = new HealthIdService.IntegratedProgramsApi();
let generateOtpRequest = new HealthIdService.HidStatusRequestPayload(); // HidStatusRequestPayload | generateOtpRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.updateStatusUsingPOST(generateOtpRequest, opts, (error, data, response) => {
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
 **generateOtpRequest** | [**HidStatusRequestPayload**](HidStatusRequestPayload.md)| generateOtpRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

**Boolean**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## verifyAadharOtpUsingPOST

> HidBenefitRequestPayload verifyAadharOtpUsingPOST(createHealthIdOptRequest, opts)

Create health id using Aadhaar Number Otp.

Create health id using Aadhaar number opt

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

let apiInstance = new HealthIdService.IntegratedProgramsApi();
let createHealthIdOptRequest = new HealthIdService.CreateHealthIdOptRequest(); // CreateHealthIdOptRequest | createHealthIdOptRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.verifyAadharOtpUsingPOST(createHealthIdOptRequest, opts, (error, data, response) => {
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
 **createHealthIdOptRequest** | [**CreateHealthIdOptRequest**](CreateHealthIdOptRequest.md)| createHealthIdOptRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**HidBenefitRequestPayload**](HidBenefitRequestPayload.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## verifyBioUsingPOST

> HidBenefitRequestPayload verifyBioUsingPOST(createHidBiometricRequest, opts)

Create health id using Biometric Authentication.

Create health id using Biometric Authentication.

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

let apiInstance = new HealthIdService.IntegratedProgramsApi();
let createHidBiometricRequest = new HealthIdService.CreateHidBiometricRequest(); // CreateHidBiometricRequest | createHidBiometricRequest
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.verifyBioUsingPOST(createHidBiometricRequest, opts, (error, data, response) => {
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
 **createHidBiometricRequest** | [**CreateHidBiometricRequest**](CreateHidBiometricRequest.md)| createHidBiometricRequest | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**HidBenefitRequestPayload**](HidBenefitRequestPayload.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

