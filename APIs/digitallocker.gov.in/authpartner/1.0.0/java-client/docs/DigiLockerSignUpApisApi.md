# DigiLockerSignUpApisApi

All URIs are relative to *https://betaapi.digitallocker.gov.in/public*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sIGNUPId**](DigiLockerSignUpApisApi.md#sIGNUPId) | **POST** /signup/2/demoauth | SIGN UP |
| [**verifyOTPId**](DigiLockerSignUpApisApi.md#verifyOTPId) | **POST** /signup/1/demoauthverify | Verify OTP |


<a id="sIGNUPId"></a>
# **sIGNUPId**
> DemoAuthResponse sIGNUPId(clientid, consent, demoauth, dob, gender, hmac, mobile, name, ts, uid, verification)

SIGN UP

This API is used to validate Aadhaar details and verify the mobile number by generating an OTP. This API call, if successful, will be followed by verify OTP call by the partner application if the user is online or available to perform OTP validation as indicated in verification parameter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DigiLockerSignUpApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://betaapi.digitallocker.gov.in/public");
    
    // Configure OAuth2 access token for authorization: oauthsecurity
    OAuth oauthsecurity = (OAuth) defaultClient.getAuthentication("oauthsecurity");
    oauthsecurity.setAccessToken("YOUR ACCESS TOKEN");

    DigiLockerSignUpApisApi apiInstance = new DigiLockerSignUpApisApi(defaultClient);
    String clientid = "clientid_example"; // String | Provide the client id that was created during the application registration process on Partners Portal.
    String consent = "consent_example"; // String | The consent indicator from the user for performing demographic authentication using Aadhaar details. This Partner Application must capture the user consent for performing the Aadhaar demographic authentication. The possible values are ‘Y’ and ‘N’. The sign up request will be processed only when this indicator is ‘Y’.
    String demoauth = "demoauth_example"; // String | The parameter indicates whether Aadhaar demographic authentication must be successful for creating DigiLocker account. The possible values are ‘Y’ and ‘N’. The value of ‘Y’ will perform Aadhaar demographic authentication and will return errors if any in response. The value of ‘N’ will also perform Aadhaar demographic authentication but will return any error in case of authentication failure. It will create a basic mobile based account for the user. Value ‘N’ should be used when the user account needs to be created in the absence of the user.
    Integer dob = 56; // Integer | This is date of birth of the user as mentioned in Aadhaar in DDMMYYYY format.
    String gender = "M"; // String | This is gender of the user as mentioned in Aadhaar. The possible values are M, F, T for male, female and transgender respectively.
    File hmac = new File("/path/to/file"); // File | Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
    Integer mobile = 56; // Integer | This is the mobile number of the user. DigiLocker will check whether an account exists for this mobile number. Either uid or mobile is required to verify whether an account exists.
    String name = "name_example"; // String | This is name of the user as mentioned in Aadhaar.
    String ts = "ts_example"; // String | Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
    Integer uid = 56; // Integer | This is the Aadhaar number of the user. DigiLocker will check whether an account exists for this Aadhaar number. Either uid or mobile is required to verify whether an account exists.
    String verification = "verification_example"; // String | The parameter indicates whether the mobile number provided above should be validated by DigiLocker. If this parameter is ‘Y’, the DigiLocker sends an OTP to verify the mobile number. In this case the client application will call the second API to validate the OTP. The user will be signed on only after successful OTP validation. This flow should be used when the user account is created by user himself/herself or the user is present to provide the OTP. If this parameter is ‘N’, the user account will be created without OTP validation. The OTP validation will be performed when the user signs in for the first time in DigiLocker. This flow should be used when the user account needs to be created in the absence of the user.
    try {
      DemoAuthResponse result = apiInstance.sIGNUPId(clientid, consent, demoauth, dob, gender, hmac, mobile, name, ts, uid, verification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DigiLockerSignUpApisApi#sIGNUPId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **clientid** | **String**| Provide the client id that was created during the application registration process on Partners Portal. | [optional] |
| **consent** | **String**| The consent indicator from the user for performing demographic authentication using Aadhaar details. This Partner Application must capture the user consent for performing the Aadhaar demographic authentication. The possible values are ‘Y’ and ‘N’. The sign up request will be processed only when this indicator is ‘Y’. | [optional] |
| **demoauth** | **String**| The parameter indicates whether Aadhaar demographic authentication must be successful for creating DigiLocker account. The possible values are ‘Y’ and ‘N’. The value of ‘Y’ will perform Aadhaar demographic authentication and will return errors if any in response. The value of ‘N’ will also perform Aadhaar demographic authentication but will return any error in case of authentication failure. It will create a basic mobile based account for the user. Value ‘N’ should be used when the user account needs to be created in the absence of the user. | [optional] |
| **dob** | **Integer**| This is date of birth of the user as mentioned in Aadhaar in DDMMYYYY format. | [optional] |
| **gender** | **String**| This is gender of the user as mentioned in Aadhaar. The possible values are M, F, T for male, female and transgender respectively. | [optional] [enum: M, F, T] |
| **hmac** | **File**| Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret. | [optional] |
| **mobile** | **Integer**| This is the mobile number of the user. DigiLocker will check whether an account exists for this mobile number. Either uid or mobile is required to verify whether an account exists. | [optional] |
| **name** | **String**| This is name of the user as mentioned in Aadhaar. | [optional] |
| **ts** | **String**| Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes. | [optional] |
| **uid** | **Integer**| This is the Aadhaar number of the user. DigiLocker will check whether an account exists for this Aadhaar number. Either uid or mobile is required to verify whether an account exists. | [optional] |
| **verification** | **String**| The parameter indicates whether the mobile number provided above should be validated by DigiLocker. If this parameter is ‘Y’, the DigiLocker sends an OTP to verify the mobile number. In this case the client application will call the second API to validate the OTP. The user will be signed on only after successful OTP validation. This flow should be used when the user account is created by user himself/herself or the user is present to provide the OTP. If this parameter is ‘N’, the user account will be created without OTP validation. The OTP validation will be performed when the user signs in for the first time in DigiLocker. This flow should be used when the user account needs to be created in the absence of the user. | [optional] |

### Return type

[**DemoAuthResponse**](DemoAuthResponse.md)

### Authorization

[oauthsecurity](../README.md#oauthsecurity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized error |  -  |
| **500** | Internal Error |  -  |

<a id="verifyOTPId"></a>
# **verifyOTPId**
> DemoAuthVerifyResponse verifyOTPId(clientid, hmac, mobile, otp, ts)

Verify OTP

This API is used to verify the OTP sent by DigiLocker during the sign up API call above.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DigiLockerSignUpApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://betaapi.digitallocker.gov.in/public");
    
    // Configure OAuth2 access token for authorization: oauthsecurity
    OAuth oauthsecurity = (OAuth) defaultClient.getAuthentication("oauthsecurity");
    oauthsecurity.setAccessToken("YOUR ACCESS TOKEN");

    DigiLockerSignUpApisApi apiInstance = new DigiLockerSignUpApisApi(defaultClient);
    String clientid = "clientid_example"; // String | Provide the client id that was created during the application registration process on Partners Portal.
    File hmac = new File("/path/to/file"); // File | Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
    Integer mobile = 56; // Integer | This is the mobile number of the user. DigiLocker will check whether an account exists for this mobile number. Either uid or mobile is required to verify whether an account exists.
    Integer otp = 56; // Integer | The OTP provided by the user.
    String ts = "ts_example"; // String | Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
    try {
      DemoAuthVerifyResponse result = apiInstance.verifyOTPId(clientid, hmac, mobile, otp, ts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DigiLockerSignUpApisApi#verifyOTPId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **clientid** | **String**| Provide the client id that was created during the application registration process on Partners Portal. | [optional] |
| **hmac** | **File**| Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret. | [optional] |
| **mobile** | **Integer**| This is the mobile number of the user. DigiLocker will check whether an account exists for this mobile number. Either uid or mobile is required to verify whether an account exists. | [optional] |
| **otp** | **Integer**| The OTP provided by the user. | [optional] |
| **ts** | **String**| Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes. | [optional] |

### Return type

[**DemoAuthVerifyResponse**](DemoAuthVerifyResponse.md)

### Authorization

[oauthsecurity](../README.md#oauthsecurity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized error |  -  |
| **500** | Internal Error |  -  |

