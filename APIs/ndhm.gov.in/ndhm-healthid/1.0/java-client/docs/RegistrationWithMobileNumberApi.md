# RegistrationWithMobileNumberApi

All URIs are relative to *https://healthidsbx.ndhm.gov.in/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**generateMobileOTPUsingPOST1**](RegistrationWithMobileNumberApi.md#generateMobileOTPUsingPOST1) | **POST** /v1/registration/mobile/generateOtp | Generate Mobile OTP to start registration |
| [**resentOtpUsingPOST**](RegistrationWithMobileNumberApi.md#resentOtpUsingPOST) | **POST** /v1/registration/mobile/resendOtp | Resend Mobile OTP for Health ID registration |
| [**verifyMobileOTPUsingPOST**](RegistrationWithMobileNumberApi.md#verifyMobileOTPUsingPOST) | **POST** /v1/registration/mobile/verifyOtp | Verify Mobile OTP sent as part of registration transaction. |
| [**verifyUserViaMobileUsingPOST**](RegistrationWithMobileNumberApi.md#verifyUserViaMobileUsingPOST) | **POST** /v1/registration/mobile/createHealthId | Create Health ID with verified mobile token |


<a id="generateMobileOTPUsingPOST1"></a>
# **generateMobileOTPUsingPOST1**
> TxnResponse generateMobileOTPUsingPOST1(generateOtpRequest, acceptLanguage)

Generate Mobile OTP to start registration

Generate Mobile OTP to start registration transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationWithMobileNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://healthidsbx.ndhm.gov.in/api");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    // Configure API key authorization: X-HIP-ID
    ApiKeyAuth X-HIP-ID = (ApiKeyAuth) defaultClient.getAuthentication("X-HIP-ID");
    X-HIP-ID.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-HIP-ID.setApiKeyPrefix("Token");

    RegistrationWithMobileNumberApi apiInstance = new RegistrationWithMobileNumberApi(defaultClient);
    GenerateMobileOTPRequest generateOtpRequest = new GenerateMobileOTPRequest(); // GenerateMobileOTPRequest | generateOtpRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      TxnResponse result = apiInstance.generateMobileOTPUsingPOST1(generateOtpRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationWithMobileNumberApi#generateMobileOTPUsingPOST1");
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
| **generateOtpRequest** | [**GenerateMobileOTPRequest**](GenerateMobileOTPRequest.md)| generateOtpRequest | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

[**TxnResponse**](TxnResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="resentOtpUsingPOST"></a>
# **resentOtpUsingPOST**
> Boolean resentOtpUsingPOST(resendRequest, acceptLanguage)

Resend Mobile OTP for Health ID registration

Resend Mobile OTP in an existing transaction in case previous OTP is not received.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationWithMobileNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://healthidsbx.ndhm.gov.in/api");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    // Configure API key authorization: X-HIP-ID
    ApiKeyAuth X-HIP-ID = (ApiKeyAuth) defaultClient.getAuthentication("X-HIP-ID");
    X-HIP-ID.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-HIP-ID.setApiKeyPrefix("Token");

    RegistrationWithMobileNumberApi apiInstance = new RegistrationWithMobileNumberApi(defaultClient);
    ResendOTPRequest resendRequest = new ResendOTPRequest(); // ResendOTPRequest | resendRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      Boolean result = apiInstance.resentOtpUsingPOST(resendRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationWithMobileNumberApi#resentOtpUsingPOST");
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
| **resendRequest** | [**ResendOTPRequest**](ResendOTPRequest.md)| resendRequest | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

**Boolean**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="verifyMobileOTPUsingPOST"></a>
# **verifyMobileOTPUsingPOST**
> MobileVerificationToken verifyMobileOTPUsingPOST(verifyOtpRequest, acceptLanguage)

Verify Mobile OTP sent as part of registration transaction.

Verify Mobile OTP in current registration transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationWithMobileNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://healthidsbx.ndhm.gov.in/api");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    // Configure API key authorization: X-HIP-ID
    ApiKeyAuth X-HIP-ID = (ApiKeyAuth) defaultClient.getAuthentication("X-HIP-ID");
    X-HIP-ID.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-HIP-ID.setApiKeyPrefix("Token");

    RegistrationWithMobileNumberApi apiInstance = new RegistrationWithMobileNumberApi(defaultClient);
    VerifyMobileRequest verifyOtpRequest = new VerifyMobileRequest(); // VerifyMobileRequest | verifyOtpRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      MobileVerificationToken result = apiInstance.verifyMobileOTPUsingPOST(verifyOtpRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationWithMobileNumberApi#verifyMobileOTPUsingPOST");
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
| **verifyOtpRequest** | [**VerifyMobileRequest**](VerifyMobileRequest.md)| verifyOtpRequest | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

[**MobileVerificationToken**](MobileVerificationToken.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="verifyUserViaMobileUsingPOST"></a>
# **verifyUserViaMobileUsingPOST**
> CreateAccountJwtResponse verifyUserViaMobileUsingPOST(createAccountRequest, acceptLanguage)

Create Health ID with verified mobile token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationWithMobileNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://healthidsbx.ndhm.gov.in/api");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    // Configure API key authorization: X-HIP-ID
    ApiKeyAuth X-HIP-ID = (ApiKeyAuth) defaultClient.getAuthentication("X-HIP-ID");
    X-HIP-ID.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-HIP-ID.setApiKeyPrefix("Token");

    RegistrationWithMobileNumberApi apiInstance = new RegistrationWithMobileNumberApi(defaultClient);
    CreateAccountByVerifiedMobileRequest createAccountRequest = new CreateAccountByVerifiedMobileRequest(); // CreateAccountByVerifiedMobileRequest | createAccountRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      CreateAccountJwtResponse result = apiInstance.verifyUserViaMobileUsingPOST(createAccountRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationWithMobileNumberApi#verifyUserViaMobileUsingPOST");
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
| **createAccountRequest** | [**CreateAccountByVerifiedMobileRequest**](CreateAccountByVerifiedMobileRequest.md)| createAccountRequest | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

[**CreateAccountJwtResponse**](CreateAccountJwtResponse.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

