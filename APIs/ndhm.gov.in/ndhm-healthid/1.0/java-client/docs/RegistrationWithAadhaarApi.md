# RegistrationWithAadhaarApi

All URIs are relative to *https://healthidsbx.ndhm.gov.in/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAadhaarAccountUsingPOST**](RegistrationWithAadhaarApi.md#createAadhaarAccountUsingPOST) | **POST** /v1/registration/aadhaar/createHealthIdWithPreVerified | Create Health ID using pre-verified Aadhaar &amp; Mobile. |
| [**generateAadharOTPUsingPOST**](RegistrationWithAadhaarApi.md#generateAadharOTPUsingPOST) | **POST** /v1/registration/aadhaar/generateOtp | Generate Aadhaar OTP on registrered mobile number |
| [**generateMobileOTPForTxnUsingPOST**](RegistrationWithAadhaarApi.md#generateMobileOTPForTxnUsingPOST) | **POST** /v1/registration/aadhaar/generateMobileOTP | Generate Mobile OTP for verification. |
| [**getHealthIdNumbersByAadharUsingPOST**](RegistrationWithAadhaarApi.md#getHealthIdNumbersByAadharUsingPOST) | **POST** /v1/registration/aadhaar/search/aadhar | Search health id number using aadhar. |
| [**resendAadharOTPUsingPOST**](RegistrationWithAadhaarApi.md#resendAadharOTPUsingPOST) | **POST** /v1/registration/aadhaar/resendAadhaarOtp | Resend Aadhaar OTP on registrered mobile number to create Health ID. |
| [**verifyAadharBioUsingPOST**](RegistrationWithAadhaarApi.md#verifyAadharBioUsingPOST) | **POST** /v1/registration/aadhaar/verifyBio | Verify Aadhaar using biometrics. |
| [**verifyAadharOTPOnlyUsingPOST**](RegistrationWithAadhaarApi.md#verifyAadharOTPOnlyUsingPOST) | **POST** /v1/registration/aadhaar/verifyOTP | Verify Aadhaar OTP and continue for mobile verification. |
| [**verifyAadharOTPUsingPOST**](RegistrationWithAadhaarApi.md#verifyAadharOTPUsingPOST) | **POST** /v1/registration/aadhaar/createHealthIdWithAadhaarOtp | Verify Aadhaar OTP on registrered mobile number to create Health ID. |
| [**verifyMobileOTPForTxnUsingPOST**](RegistrationWithAadhaarApi.md#verifyMobileOTPForTxnUsingPOST) | **POST** /v1/registration/aadhaar/verifyMobileOTP | Verify Mobile OTP in an existing transaction. |


<a id="createAadhaarAccountUsingPOST"></a>
# **createAadhaarAccountUsingPOST**
> CreateAccountJwtResponse createAadhaarAccountUsingPOST(accountRequest, acceptLanguage)

Create Health ID using pre-verified Aadhaar &amp; Mobile.

Create Health ID using pre-verified Aadhaar &amp; Mobile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationWithAadhaarApi;

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

    RegistrationWithAadhaarApi apiInstance = new RegistrationWithAadhaarApi(defaultClient);
    CreateAccountWithPreVerifiedAadhaar accountRequest = new CreateAccountWithPreVerifiedAadhaar(); // CreateAccountWithPreVerifiedAadhaar | accountRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      CreateAccountJwtResponse result = apiInstance.createAadhaarAccountUsingPOST(accountRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationWithAadhaarApi#createAadhaarAccountUsingPOST");
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
| **accountRequest** | [**CreateAccountWithPreVerifiedAadhaar**](CreateAccountWithPreVerifiedAadhaar.md)| accountRequest | |
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

<a id="generateAadharOTPUsingPOST"></a>
# **generateAadharOTPUsingPOST**
> TxnResponse generateAadharOTPUsingPOST(generateOtpRequest, acceptLanguage)

Generate Aadhaar OTP on registrered mobile number

Generate Aadhaar OTP on registrered mobile number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationWithAadhaarApi;

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

    RegistrationWithAadhaarApi apiInstance = new RegistrationWithAadhaarApi(defaultClient);
    AadharOtpGenerateRequestPayLoad generateOtpRequest = new AadharOtpGenerateRequestPayLoad(); // AadharOtpGenerateRequestPayLoad | generateOtpRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      TxnResponse result = apiInstance.generateAadharOTPUsingPOST(generateOtpRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationWithAadhaarApi#generateAadharOTPUsingPOST");
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
| **generateOtpRequest** | [**AadharOtpGenerateRequestPayLoad**](AadharOtpGenerateRequestPayLoad.md)| generateOtpRequest | |
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

<a id="generateMobileOTPForTxnUsingPOST"></a>
# **generateMobileOTPForTxnUsingPOST**
> TxnResponse generateMobileOTPForTxnUsingPOST(request, acceptLanguage)

Generate Mobile OTP for verification.

Generate Mobile OTP to verify mobile number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationWithAadhaarApi;

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

    RegistrationWithAadhaarApi apiInstance = new RegistrationWithAadhaarApi(defaultClient);
    GenerateMobileOTPForTxnRequest request = new GenerateMobileOTPForTxnRequest(); // GenerateMobileOTPForTxnRequest | request
    String acceptLanguage = "en-US"; // String | 
    try {
      TxnResponse result = apiInstance.generateMobileOTPForTxnUsingPOST(request, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationWithAadhaarApi#generateMobileOTPForTxnUsingPOST");
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
| **request** | [**GenerateMobileOTPForTxnRequest**](GenerateMobileOTPForTxnRequest.md)| request | |
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

<a id="getHealthIdNumbersByAadharUsingPOST"></a>
# **getHealthIdNumbersByAadharUsingPOST**
> List&lt;Object&gt; getHealthIdNumbersByAadharUsingPOST(aadharNumberRequestPayload, acceptLanguage)

Search health id number using aadhar.

Search health id number using aadhar.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationWithAadhaarApi;

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

    RegistrationWithAadhaarApi apiInstance = new RegistrationWithAadhaarApi(defaultClient);
    AadharNumberRequestPayload aadharNumberRequestPayload = new AadharNumberRequestPayload(); // AadharNumberRequestPayload | aadharNumberRequestPayload
    String acceptLanguage = "en-US"; // String | 
    try {
      List<Object> result = apiInstance.getHealthIdNumbersByAadharUsingPOST(aadharNumberRequestPayload, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationWithAadhaarApi#getHealthIdNumbersByAadharUsingPOST");
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
| **aadharNumberRequestPayload** | [**AadharNumberRequestPayload**](AadharNumberRequestPayload.md)| aadharNumberRequestPayload | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

**List&lt;Object&gt;**

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

<a id="resendAadharOTPUsingPOST"></a>
# **resendAadharOTPUsingPOST**
> CreateAccountJwtResponse resendAadharOTPUsingPOST(request, acceptLanguage)

Resend Aadhaar OTP on registrered mobile number to create Health ID.

Resend Aadhar OTP on registrered mobile number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationWithAadhaarApi;

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

    RegistrationWithAadhaarApi apiInstance = new RegistrationWithAadhaarApi(defaultClient);
    ResendOTPRequest request = new ResendOTPRequest(); // ResendOTPRequest | request
    String acceptLanguage = "en-US"; // String | 
    try {
      CreateAccountJwtResponse result = apiInstance.resendAadharOTPUsingPOST(request, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationWithAadhaarApi#resendAadharOTPUsingPOST");
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
| **request** | [**ResendOTPRequest**](ResendOTPRequest.md)| request | |
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

<a id="verifyAadharBioUsingPOST"></a>
# **verifyAadharBioUsingPOST**
> TxnResponse verifyAadharBioUsingPOST(verifyAadharOtpRequest, acceptLanguage)

Verify Aadhaar using biometrics.

Verify Aadhaar using biometrics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationWithAadhaarApi;

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

    RegistrationWithAadhaarApi apiInstance = new RegistrationWithAadhaarApi(defaultClient);
    VerifyAadhaarWithBio verifyAadharOtpRequest = new VerifyAadhaarWithBio(); // VerifyAadhaarWithBio | verifyAadharOtpRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      TxnResponse result = apiInstance.verifyAadharBioUsingPOST(verifyAadharOtpRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationWithAadhaarApi#verifyAadharBioUsingPOST");
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
| **verifyAadharOtpRequest** | [**VerifyAadhaarWithBio**](VerifyAadhaarWithBio.md)| verifyAadharOtpRequest | |
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

<a id="verifyAadharOTPOnlyUsingPOST"></a>
# **verifyAadharOTPOnlyUsingPOST**
> TxnResponse verifyAadharOTPOnlyUsingPOST(verifyAadhaarOtp, acceptLanguage)

Verify Aadhaar OTP and continue for mobile verification.

Verify Aadhaar OTP received on registrered mobile number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationWithAadhaarApi;

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

    RegistrationWithAadhaarApi apiInstance = new RegistrationWithAadhaarApi(defaultClient);
    VerifyAadhaarOtp verifyAadhaarOtp = new VerifyAadhaarOtp(); // VerifyAadhaarOtp | verifyAadhaarOtp
    String acceptLanguage = "en-US"; // String | 
    try {
      TxnResponse result = apiInstance.verifyAadharOTPOnlyUsingPOST(verifyAadhaarOtp, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationWithAadhaarApi#verifyAadharOTPOnlyUsingPOST");
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
| **verifyAadhaarOtp** | [**VerifyAadhaarOtp**](VerifyAadhaarOtp.md)| verifyAadhaarOtp | |
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

<a id="verifyAadharOTPUsingPOST"></a>
# **verifyAadharOTPUsingPOST**
> CreateAccountJwtResponse verifyAadharOTPUsingPOST(verifyAadharOtpRequest, acceptLanguage)

Verify Aadhaar OTP on registrered mobile number to create Health ID.

Verify Aadhar OTP received on registrered mobile number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationWithAadhaarApi;

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

    RegistrationWithAadhaarApi apiInstance = new RegistrationWithAadhaarApi(defaultClient);
    CreateAccountWithAadhaarOtp verifyAadharOtpRequest = new CreateAccountWithAadhaarOtp(); // CreateAccountWithAadhaarOtp | verifyAadharOtpRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      CreateAccountJwtResponse result = apiInstance.verifyAadharOTPUsingPOST(verifyAadharOtpRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationWithAadhaarApi#verifyAadharOTPUsingPOST");
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
| **verifyAadharOtpRequest** | [**CreateAccountWithAadhaarOtp**](CreateAccountWithAadhaarOtp.md)| verifyAadharOtpRequest | |
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

<a id="verifyMobileOTPForTxnUsingPOST"></a>
# **verifyMobileOTPForTxnUsingPOST**
> TxnResponse verifyMobileOTPForTxnUsingPOST(request, acceptLanguage)

Verify Mobile OTP in an existing transaction.

Verify Mobile OTP in an existing transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationWithAadhaarApi;

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

    RegistrationWithAadhaarApi apiInstance = new RegistrationWithAadhaarApi(defaultClient);
    VerifyMobileRequest request = new VerifyMobileRequest(); // VerifyMobileRequest | request
    String acceptLanguage = "en-US"; // String | 
    try {
      TxnResponse result = apiInstance.verifyMobileOTPForTxnUsingPOST(request, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationWithAadhaarApi#verifyMobileOTPForTxnUsingPOST");
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
| **request** | [**VerifyMobileRequest**](VerifyMobileRequest.md)| request | |
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

