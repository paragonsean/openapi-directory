# HealthFacilityApi

All URIs are relative to *https://healthidsbx.ndhm.gov.in/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authenticateHealthFacilityUsingPOST**](HealthFacilityApi.md#authenticateHealthFacilityUsingPOST) | **POST** /v1/health/facility/authenticate | Generate token for heath facility id. |
| [**changePasswordUsingPOST**](HealthFacilityApi.md#changePasswordUsingPOST) | **POST** /v1/health/facility/change/password | Change password for heath facility id. |
| [**createAadhaarAccountUsingPOST1**](HealthFacilityApi.md#createAadhaarAccountUsingPOST1) | **POST** /v1/health/facility/createHealthIdWithPreVerified | Generate Health ID card SVG |
| [**generateFacilityOTPUsingPOST**](HealthFacilityApi.md#generateFacilityOTPUsingPOST) | **POST** /v1/health/facility/generateOtp | Generate health hacility OTP on registrered mobile number |
| [**generatePasswordUsingPOST**](HealthFacilityApi.md#generatePasswordUsingPOST) | **POST** /v1/health/facility/generate/password | Generates password for heath facility id. |
| [**generateSvgCardUsingGET1**](HealthFacilityApi.md#generateSvgCardUsingGET1) | **GET** /v1/health/facility/getSvgCard | generateSvgCard |
| [**resetPasswordUsingPOST**](HealthFacilityApi.md#resetPasswordUsingPOST) | **POST** /v1/health/facility/reset/password | Reset password for heath facility id. |


<a id="authenticateHealthFacilityUsingPOST"></a>
# **authenticateHealthFacilityUsingPOST**
> String authenticateHealthFacilityUsingPOST(healthFacilityAuthenticationRequest, acceptLanguage)

Generate token for heath facility id.

Generate token for heath facility id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthFacilityApi;

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

    HealthFacilityApi apiInstance = new HealthFacilityApi(defaultClient);
    HealthFacilityAuthenticationRequest healthFacilityAuthenticationRequest = new HealthFacilityAuthenticationRequest(); // HealthFacilityAuthenticationRequest | healthFacilityAuthenticationRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      String result = apiInstance.authenticateHealthFacilityUsingPOST(healthFacilityAuthenticationRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthFacilityApi#authenticateHealthFacilityUsingPOST");
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
| **healthFacilityAuthenticationRequest** | [**HealthFacilityAuthenticationRequest**](HealthFacilityAuthenticationRequest.md)| healthFacilityAuthenticationRequest | |
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

<a id="changePasswordUsingPOST"></a>
# **changePasswordUsingPOST**
> String changePasswordUsingPOST(healthFacilityPasswordRequest, acceptLanguage)

Change password for heath facility id.

Change password for heath facility id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthFacilityApi;

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

    HealthFacilityApi apiInstance = new HealthFacilityApi(defaultClient);
    HealthFacilityChangedPasswordRequest healthFacilityPasswordRequest = new HealthFacilityChangedPasswordRequest(); // HealthFacilityChangedPasswordRequest | healthFacilityPasswordRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      String result = apiInstance.changePasswordUsingPOST(healthFacilityPasswordRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthFacilityApi#changePasswordUsingPOST");
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
| **healthFacilityPasswordRequest** | [**HealthFacilityChangedPasswordRequest**](HealthFacilityChangedPasswordRequest.md)| healthFacilityPasswordRequest | |
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

<a id="createAadhaarAccountUsingPOST1"></a>
# **createAadhaarAccountUsingPOST1**
> CreateAccountJwtResponse createAadhaarAccountUsingPOST1(accountRequest, acceptLanguage)

Generate Health ID card SVG

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthFacilityApi;

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

    HealthFacilityApi apiInstance = new HealthFacilityApi(defaultClient);
    CreateAccountWithPreVerifiedAadhaar accountRequest = new CreateAccountWithPreVerifiedAadhaar(); // CreateAccountWithPreVerifiedAadhaar | accountRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      CreateAccountJwtResponse result = apiInstance.createAadhaarAccountUsingPOST1(accountRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthFacilityApi#createAadhaarAccountUsingPOST1");
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

<a id="generateFacilityOTPUsingPOST"></a>
# **generateFacilityOTPUsingPOST**
> TxnResponse generateFacilityOTPUsingPOST(xToken, generateOtpRequest, acceptLanguage)

Generate health hacility OTP on registrered mobile number

Generate health facility OTP on registrered mobile number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthFacilityApi;

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

    HealthFacilityApi apiInstance = new HealthFacilityApi(defaultClient);
    String xToken = "Bearer XToken"; // String | Auth Token
    AadharOtpGenerateRequestPayLoad generateOtpRequest = new AadharOtpGenerateRequestPayLoad(); // AadharOtpGenerateRequestPayLoad | generateOtpRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      TxnResponse result = apiInstance.generateFacilityOTPUsingPOST(xToken, generateOtpRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthFacilityApi#generateFacilityOTPUsingPOST");
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
| **xToken** | **String**| Auth Token | |
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

<a id="generatePasswordUsingPOST"></a>
# **generatePasswordUsingPOST**
> String generatePasswordUsingPOST(healthFacilityPasswordRequest, acceptLanguage)

Generates password for heath facility id.

Generates password for heath facility id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthFacilityApi;

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

    HealthFacilityApi apiInstance = new HealthFacilityApi(defaultClient);
    HealthFacilityPasswordRequest healthFacilityPasswordRequest = new HealthFacilityPasswordRequest(); // HealthFacilityPasswordRequest | healthFacilityPasswordRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      String result = apiInstance.generatePasswordUsingPOST(healthFacilityPasswordRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthFacilityApi#generatePasswordUsingPOST");
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
| **healthFacilityPasswordRequest** | [**HealthFacilityPasswordRequest**](HealthFacilityPasswordRequest.md)| healthFacilityPasswordRequest | |
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

<a id="generateSvgCardUsingGET1"></a>
# **generateSvgCardUsingGET1**
> byte[] generateSvgCardUsingGET1(healthID, xToken, acceptLanguage)

generateSvgCard

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthFacilityApi;

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

    HealthFacilityApi apiInstance = new HealthFacilityApi(defaultClient);
    String healthID = "demo@ndhm"; // String | Your health id
    String xToken = "Bearer X-Token"; // String | Auth Token
    String acceptLanguage = "en-US"; // String | 
    try {
      byte[] result = apiInstance.generateSvgCardUsingGET1(healthID, xToken, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthFacilityApi#generateSvgCardUsingGET1");
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
| **healthID** | **String**| Your health id | |
| **xToken** | **String**| Auth Token | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

**byte[]**

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

<a id="resetPasswordUsingPOST"></a>
# **resetPasswordUsingPOST**
> String resetPasswordUsingPOST(healthFacilityPasswordRequest, acceptLanguage)

Reset password for heath facility id.

Reset password for heath facility id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthFacilityApi;

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

    HealthFacilityApi apiInstance = new HealthFacilityApi(defaultClient);
    HealthFacilityPasswordRequest healthFacilityPasswordRequest = new HealthFacilityPasswordRequest(); // HealthFacilityPasswordRequest | healthFacilityPasswordRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      String result = apiInstance.resetPasswordUsingPOST(healthFacilityPasswordRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthFacilityApi#resetPasswordUsingPOST");
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
| **healthFacilityPasswordRequest** | [**HealthFacilityPasswordRequest**](HealthFacilityPasswordRequest.md)| healthFacilityPasswordRequest | |
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

