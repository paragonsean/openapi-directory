# AuthenticationApi

All URIs are relative to *https://healthidsbx.ndhm.gov.in/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authAccountPasswordRequestUsingPOST**](AuthenticationApi.md#authAccountPasswordRequestUsingPOST) | **POST** /v1/auth/confirmWithPassword | Authentication with PASSWORD based auth transaction. |
| [**authWithMobileTokenUsingPOST**](AuthenticationApi.md#authWithMobileTokenUsingPOST) | **POST** /v1/auth/authWithMobileToken | Authenticate using verified Mobile Number and user data |
| [**authenticateUserUsingPOST**](AuthenticationApi.md#authenticateUserUsingPOST) | **POST** /v1/auth/authWithMobile | Authenticate request to generate Mobile OTP using Health ID number / Health ID |
| [**authenticateWithPasswordUsingPOST**](AuthenticationApi.md#authenticateWithPasswordUsingPOST) | **POST** /v1/auth/authPassword | Authenticate using Health ID number / Health ID and password |
| [**certUsingGET**](AuthenticationApi.md#certUsingGET) | **GET** /v1/auth/cert | Auth token public key. |
| [**confirmWithAadhaarBioUsingPOST**](AuthenticationApi.md#confirmWithAadhaarBioUsingPOST) | **POST** /v1/auth/confirmWithAadhaarBio | Authentication with Aadhaar Biometric based auth transaction. |
| [**confirmWithAadhaarOtpUsingPOST**](AuthenticationApi.md#confirmWithAadhaarOtpUsingPOST) | **POST** /v1/auth/confirmWithAadhaarOtp | Authentication with Aadhaar OTP based auth transaction. |
| [**confirmWithDemographicsUsingPOST**](AuthenticationApi.md#confirmWithDemographicsUsingPOST) | **POST** /v1/auth/confirmWithDemographics | Authenticate using demographic data of user. |
| [**confirmWithMobileUsingPOST**](AuthenticationApi.md#confirmWithMobileUsingPOST) | **POST** /v1/auth/confirmWithMobileOTP | Authentication with Mobile OTP based auth transaction. |
| [**initiateAuthUsingPOST**](AuthenticationApi.md#initiateAuthUsingPOST) | **POST** /v1/auth/init | Initiate authentication process for given Health ID |
| [**resendAuthMobileOTPUsingPOST**](AuthenticationApi.md#resendAuthMobileOTPUsingPOST) | **POST** /v1/auth/resendAuthOTP | Resend Aadhaar/Mobile OTP for Authentication Transaction. |


<a id="authAccountPasswordRequestUsingPOST"></a>
# **authAccountPasswordRequestUsingPOST**
> JwtResponse authAccountPasswordRequestUsingPOST(authenticationRequest, acceptLanguage)

Authentication with PASSWORD based auth transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

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

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    AuthWithPasswordRequest authenticationRequest = new AuthWithPasswordRequest(); // AuthWithPasswordRequest | authenticationRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      JwtResponse result = apiInstance.authAccountPasswordRequestUsingPOST(authenticationRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authAccountPasswordRequestUsingPOST");
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
| **authenticationRequest** | [**AuthWithPasswordRequest**](AuthWithPasswordRequest.md)| authenticationRequest | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

[**JwtResponse**](JwtResponse.md)

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

<a id="authWithMobileTokenUsingPOST"></a>
# **authWithMobileTokenUsingPOST**
> JwtResponse authWithMobileTokenUsingPOST(authRequest, acceptLanguage)

Authenticate using verified Mobile Number and user data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

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

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    AuthWithMobileTxnAndUserData authRequest = new AuthWithMobileTxnAndUserData(); // AuthWithMobileTxnAndUserData | authRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      JwtResponse result = apiInstance.authWithMobileTokenUsingPOST(authRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authWithMobileTokenUsingPOST");
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
| **authRequest** | [**AuthWithMobileTxnAndUserData**](AuthWithMobileTxnAndUserData.md)| authRequest | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

[**JwtResponse**](JwtResponse.md)

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

<a id="authenticateUserUsingPOST"></a>
# **authenticateUserUsingPOST**
> TxnResponse authenticateUserUsingPOST(authRequest, acceptLanguage)

Authenticate request to generate Mobile OTP using Health ID number / Health ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

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

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    AuthMobileOTPRequest authRequest = new AuthMobileOTPRequest(); // AuthMobileOTPRequest | authRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      TxnResponse result = apiInstance.authenticateUserUsingPOST(authRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authenticateUserUsingPOST");
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
| **authRequest** | [**AuthMobileOTPRequest**](AuthMobileOTPRequest.md)| authRequest | |
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

<a id="authenticateWithPasswordUsingPOST"></a>
# **authenticateWithPasswordUsingPOST**
> JwtResponse authenticateWithPasswordUsingPOST(authenticationRequest, acceptLanguage)

Authenticate using Health ID number / Health ID and password

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

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

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    JwtRequest authenticationRequest = new JwtRequest(); // JwtRequest | authenticationRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      JwtResponse result = apiInstance.authenticateWithPasswordUsingPOST(authenticationRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authenticateWithPasswordUsingPOST");
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
| **authenticationRequest** | [**JwtRequest**](JwtRequest.md)| authenticationRequest | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

[**JwtResponse**](JwtResponse.md)

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

<a id="certUsingGET"></a>
# **certUsingGET**
> String certUsingGET(acceptLanguage)

Auth token public key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

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

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    String acceptLanguage = "en-US"; // String | 
    try {
      String result = apiInstance.certUsingGET(acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#certUsingGET");
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
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

**String**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="confirmWithAadhaarBioUsingPOST"></a>
# **confirmWithAadhaarBioUsingPOST**
> JwtResponse confirmWithAadhaarBioUsingPOST(authenticationRequest, acceptLanguage)

Authentication with Aadhaar Biometric based auth transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

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

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    AuthAccountAadhaarBioRequest authenticationRequest = new AuthAccountAadhaarBioRequest(); // AuthAccountAadhaarBioRequest | authenticationRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      JwtResponse result = apiInstance.confirmWithAadhaarBioUsingPOST(authenticationRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#confirmWithAadhaarBioUsingPOST");
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
| **authenticationRequest** | [**AuthAccountAadhaarBioRequest**](AuthAccountAadhaarBioRequest.md)| authenticationRequest | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

[**JwtResponse**](JwtResponse.md)

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

<a id="confirmWithAadhaarOtpUsingPOST"></a>
# **confirmWithAadhaarOtpUsingPOST**
> JwtResponse confirmWithAadhaarOtpUsingPOST(authenticationRequest, acceptLanguage)

Authentication with Aadhaar OTP based auth transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

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

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    AuthAccountAadhaarOTPRequest authenticationRequest = new AuthAccountAadhaarOTPRequest(); // AuthAccountAadhaarOTPRequest | authenticationRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      JwtResponse result = apiInstance.confirmWithAadhaarOtpUsingPOST(authenticationRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#confirmWithAadhaarOtpUsingPOST");
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
| **authenticationRequest** | [**AuthAccountAadhaarOTPRequest**](AuthAccountAadhaarOTPRequest.md)| authenticationRequest | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

[**JwtResponse**](JwtResponse.md)

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

<a id="confirmWithDemographicsUsingPOST"></a>
# **confirmWithDemographicsUsingPOST**
> String confirmWithDemographicsUsingPOST(authenticationRequest, acceptLanguage)

Authenticate using demographic data of user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

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

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    AuthAccountWithDemographicsRequest authenticationRequest = new AuthAccountWithDemographicsRequest(); // AuthAccountWithDemographicsRequest | authenticationRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      String result = apiInstance.confirmWithDemographicsUsingPOST(authenticationRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#confirmWithDemographicsUsingPOST");
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
| **authenticationRequest** | [**AuthAccountWithDemographicsRequest**](AuthAccountWithDemographicsRequest.md)| authenticationRequest | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

**String**

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

<a id="confirmWithMobileUsingPOST"></a>
# **confirmWithMobileUsingPOST**
> JwtResponse confirmWithMobileUsingPOST(authenticationRequest, acceptLanguage)

Authentication with Mobile OTP based auth transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

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

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    AuthAccountMobileOTPRequest authenticationRequest = new AuthAccountMobileOTPRequest(); // AuthAccountMobileOTPRequest | authenticationRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      JwtResponse result = apiInstance.confirmWithMobileUsingPOST(authenticationRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#confirmWithMobileUsingPOST");
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
| **authenticationRequest** | [**AuthAccountMobileOTPRequest**](AuthAccountMobileOTPRequest.md)| authenticationRequest | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

[**JwtResponse**](JwtResponse.md)

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

<a id="initiateAuthUsingPOST"></a>
# **initiateAuthUsingPOST**
> TxnResponse initiateAuthUsingPOST(authRequest, acceptLanguage)

Initiate authentication process for given Health ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

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

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    AuthInitRequest authRequest = new AuthInitRequest(); // AuthInitRequest | authRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      TxnResponse result = apiInstance.initiateAuthUsingPOST(authRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#initiateAuthUsingPOST");
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
| **authRequest** | [**AuthInitRequest**](AuthInitRequest.md)| authRequest | |
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

<a id="resendAuthMobileOTPUsingPOST"></a>
# **resendAuthMobileOTPUsingPOST**
> Boolean resendAuthMobileOTPUsingPOST(resendOtpRequest, acceptLanguage)

Resend Aadhaar/Mobile OTP for Authentication Transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

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

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    ResendOTPRequest resendOtpRequest = new ResendOTPRequest(); // ResendOTPRequest | resendOtpRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      Boolean result = apiInstance.resendAuthMobileOTPUsingPOST(resendOtpRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#resendAuthMobileOTPUsingPOST");
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
| **resendOtpRequest** | [**ResendOTPRequest**](ResendOTPRequest.md)| resendOtpRequest | |
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

