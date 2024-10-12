# AuthorizedPartnerApiSpecification.DigiLockerSignUpAPIsApi

All URIs are relative to *https://betaapi.digitallocker.gov.in/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sIGNUPId**](DigiLockerSignUpAPIsApi.md#sIGNUPId) | **POST** /signup/2/demoauth | SIGN UP
[**verifyOTPId**](DigiLockerSignUpAPIsApi.md#verifyOTPId) | **POST** /signup/1/demoauthverify | Verify OTP



## sIGNUPId

> DemoAuthResponse sIGNUPId(opts)

SIGN UP

This API is used to validate Aadhaar details and verify the mobile number by generating an OTP. This API call, if successful, will be followed by verify OTP call by the partner application if the user is online or available to perform OTP validation as indicated in verification parameter

### Example

```javascript
import AuthorizedPartnerApiSpecification from 'authorized_partner_api_specification';
let defaultClient = AuthorizedPartnerApiSpecification.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauthsecurity
let oauthsecurity = defaultClient.authentications['oauthsecurity'];
oauthsecurity.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizedPartnerApiSpecification.DigiLockerSignUpAPIsApi();
let opts = {
  'clientid': "clientid_example", // String | Provide the client id that was created during the application registration process on Partners Portal.
  'consent': "consent_example", // String | The consent indicator from the user for performing demographic authentication using Aadhaar details. This Partner Application must capture the user consent for performing the Aadhaar demographic authentication. The possible values are ‘Y’ and ‘N’. The sign up request will be processed only when this indicator is ‘Y’.
  'demoauth': "demoauth_example", // String | The parameter indicates whether Aadhaar demographic authentication must be successful for creating DigiLocker account. The possible values are ‘Y’ and ‘N’. The value of ‘Y’ will perform Aadhaar demographic authentication and will return errors if any in response. The value of ‘N’ will also perform Aadhaar demographic authentication but will return any error in case of authentication failure. It will create a basic mobile based account for the user. Value ‘N’ should be used when the user account needs to be created in the absence of the user.
  'dob': 56, // Number | This is date of birth of the user as mentioned in Aadhaar in DDMMYYYY format.
  'gender': "gender_example", // String | This is gender of the user as mentioned in Aadhaar. The possible values are M, F, T for male, female and transgender respectively.
  'hmac': "/path/to/file", // File | Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
  'mobile': 56, // Number | This is the mobile number of the user. DigiLocker will check whether an account exists for this mobile number. Either uid or mobile is required to verify whether an account exists.
  'name': "name_example", // String | This is name of the user as mentioned in Aadhaar.
  'ts': "ts_example", // String | Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
  'uid': 56, // Number | This is the Aadhaar number of the user. DigiLocker will check whether an account exists for this Aadhaar number. Either uid or mobile is required to verify whether an account exists.
  'verification': "verification_example" // String | The parameter indicates whether the mobile number provided above should be validated by DigiLocker. If this parameter is ‘Y’, the DigiLocker sends an OTP to verify the mobile number. In this case the client application will call the second API to validate the OTP. The user will be signed on only after successful OTP validation. This flow should be used when the user account is created by user himself/herself or the user is present to provide the OTP. If this parameter is ‘N’, the user account will be created without OTP validation. The OTP validation will be performed when the user signs in for the first time in DigiLocker. This flow should be used when the user account needs to be created in the absence of the user.
};
apiInstance.sIGNUPId(opts, (error, data, response) => {
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
 **clientid** | **String**| Provide the client id that was created during the application registration process on Partners Portal. | [optional] 
 **consent** | **String**| The consent indicator from the user for performing demographic authentication using Aadhaar details. This Partner Application must capture the user consent for performing the Aadhaar demographic authentication. The possible values are ‘Y’ and ‘N’. The sign up request will be processed only when this indicator is ‘Y’. | [optional] 
 **demoauth** | **String**| The parameter indicates whether Aadhaar demographic authentication must be successful for creating DigiLocker account. The possible values are ‘Y’ and ‘N’. The value of ‘Y’ will perform Aadhaar demographic authentication and will return errors if any in response. The value of ‘N’ will also perform Aadhaar demographic authentication but will return any error in case of authentication failure. It will create a basic mobile based account for the user. Value ‘N’ should be used when the user account needs to be created in the absence of the user. | [optional] 
 **dob** | **Number**| This is date of birth of the user as mentioned in Aadhaar in DDMMYYYY format. | [optional] 
 **gender** | **String**| This is gender of the user as mentioned in Aadhaar. The possible values are M, F, T for male, female and transgender respectively. | [optional] 
 **hmac** | **File**| Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret. | [optional] 
 **mobile** | **Number**| This is the mobile number of the user. DigiLocker will check whether an account exists for this mobile number. Either uid or mobile is required to verify whether an account exists. | [optional] 
 **name** | **String**| This is name of the user as mentioned in Aadhaar. | [optional] 
 **ts** | **String**| Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes. | [optional] 
 **uid** | **Number**| This is the Aadhaar number of the user. DigiLocker will check whether an account exists for this Aadhaar number. Either uid or mobile is required to verify whether an account exists. | [optional] 
 **verification** | **String**| The parameter indicates whether the mobile number provided above should be validated by DigiLocker. If this parameter is ‘Y’, the DigiLocker sends an OTP to verify the mobile number. In this case the client application will call the second API to validate the OTP. The user will be signed on only after successful OTP validation. This flow should be used when the user account is created by user himself/herself or the user is present to provide the OTP. If this parameter is ‘N’, the user account will be created without OTP validation. The OTP validation will be performed when the user signs in for the first time in DigiLocker. This flow should be used when the user account needs to be created in the absence of the user. | [optional] 

### Return type

[**DemoAuthResponse**](DemoAuthResponse.md)

### Authorization

[oauthsecurity](../README.md#oauthsecurity)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## verifyOTPId

> DemoAuthVerifyResponse verifyOTPId(opts)

Verify OTP

This API is used to verify the OTP sent by DigiLocker during the sign up API call above.

### Example

```javascript
import AuthorizedPartnerApiSpecification from 'authorized_partner_api_specification';
let defaultClient = AuthorizedPartnerApiSpecification.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauthsecurity
let oauthsecurity = defaultClient.authentications['oauthsecurity'];
oauthsecurity.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizedPartnerApiSpecification.DigiLockerSignUpAPIsApi();
let opts = {
  'clientid': "clientid_example", // String | Provide the client id that was created during the application registration process on Partners Portal.
  'hmac': "/path/to/file", // File | Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
  'mobile': 56, // Number | This is the mobile number of the user. DigiLocker will check whether an account exists for this mobile number. Either uid or mobile is required to verify whether an account exists.
  'otp': 56, // Number | The OTP provided by the user.
  'ts': "ts_example" // String | Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
};
apiInstance.verifyOTPId(opts, (error, data, response) => {
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
 **clientid** | **String**| Provide the client id that was created during the application registration process on Partners Portal. | [optional] 
 **hmac** | **File**| Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret. | [optional] 
 **mobile** | **Number**| This is the mobile number of the user. DigiLocker will check whether an account exists for this mobile number. Either uid or mobile is required to verify whether an account exists. | [optional] 
 **otp** | **Number**| The OTP provided by the user. | [optional] 
 **ts** | **String**| Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes. | [optional] 

### Return type

[**DemoAuthVerifyResponse**](DemoAuthVerifyResponse.md)

### Authorization

[oauthsecurity](../README.md#oauthsecurity)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

