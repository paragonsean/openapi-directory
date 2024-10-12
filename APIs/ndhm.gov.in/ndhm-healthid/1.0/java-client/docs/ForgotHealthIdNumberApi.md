# ForgotHealthIdNumberApi

All URIs are relative to *https://healthidsbx.ndhm.gov.in/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**generateAadharOTPUsingPOST1**](ForgotHealthIdNumberApi.md#generateAadharOTPUsingPOST1) | **POST** /v1/forgot/healthId/aadhaar/generateOtp | Generate Aadhaar OTP on registrered mobile number |
| [**generateMobileOTPUsingPOST**](ForgotHealthIdNumberApi.md#generateMobileOTPUsingPOST) | **POST** /v1/forgot/healthId/mobile/generateOtp | Generate Mobile OTP to start registration |
| [**retrievalHealthIdByAadharUsingPOST**](ForgotHealthIdNumberApi.md#retrievalHealthIdByAadharUsingPOST) | **POST** /v1/forgot/healthId/aadhaar | Verify aadhar OTP sent as part of forgetHealth id. |
| [**retrievalHealthIdByMobileUsingPOST**](ForgotHealthIdNumberApi.md#retrievalHealthIdByMobileUsingPOST) | **POST** /v1/forgot/healthId/mobile | Verify Mobile OTP sent as  part of forgetHealth id. |


<a id="generateAadharOTPUsingPOST1"></a>
# **generateAadharOTPUsingPOST1**
> TxnResponse generateAadharOTPUsingPOST1(generateOtpRequest, acceptLanguage)

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
import org.openapitools.client.api.ForgotHealthIdNumberApi;

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

    ForgotHealthIdNumberApi apiInstance = new ForgotHealthIdNumberApi(defaultClient);
    AadharOtpGenerateRequestPayLoad generateOtpRequest = new AadharOtpGenerateRequestPayLoad(); // AadharOtpGenerateRequestPayLoad | generateOtpRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      TxnResponse result = apiInstance.generateAadharOTPUsingPOST1(generateOtpRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForgotHealthIdNumberApi#generateAadharOTPUsingPOST1");
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

<a id="generateMobileOTPUsingPOST"></a>
# **generateMobileOTPUsingPOST**
> TxnResponse generateMobileOTPUsingPOST(generateOtpRequest, acceptLanguage)

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
import org.openapitools.client.api.ForgotHealthIdNumberApi;

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

    ForgotHealthIdNumberApi apiInstance = new ForgotHealthIdNumberApi(defaultClient);
    GenerateMobileOTPRequest generateOtpRequest = new GenerateMobileOTPRequest(); // GenerateMobileOTPRequest | generateOtpRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      TxnResponse result = apiInstance.generateMobileOTPUsingPOST(generateOtpRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForgotHealthIdNumberApi#generateMobileOTPUsingPOST");
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

<a id="retrievalHealthIdByAadharUsingPOST"></a>
# **retrievalHealthIdByAadharUsingPOST**
> RetrieveHealthIdPayloadResponse retrievalHealthIdByAadharUsingPOST(authAccountAadhaarOTPRequest, acceptLanguage)

Verify aadhar OTP sent as part of forgetHealth id.

Verify aadhar OTP sent as part of forgetHealth id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForgotHealthIdNumberApi;

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

    ForgotHealthIdNumberApi apiInstance = new ForgotHealthIdNumberApi(defaultClient);
    AuthAccountAadhaarOTPRequest authAccountAadhaarOTPRequest = new AuthAccountAadhaarOTPRequest(); // AuthAccountAadhaarOTPRequest | authAccountAadhaarOTPRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      RetrieveHealthIdPayloadResponse result = apiInstance.retrievalHealthIdByAadharUsingPOST(authAccountAadhaarOTPRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForgotHealthIdNumberApi#retrievalHealthIdByAadharUsingPOST");
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
| **authAccountAadhaarOTPRequest** | [**AuthAccountAadhaarOTPRequest**](AuthAccountAadhaarOTPRequest.md)| authAccountAadhaarOTPRequest | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

[**RetrieveHealthIdPayloadResponse**](RetrieveHealthIdPayloadResponse.md)

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

<a id="retrievalHealthIdByMobileUsingPOST"></a>
# **retrievalHealthIdByMobileUsingPOST**
> RetrieveHealthIdPayloadResponse retrievalHealthIdByMobileUsingPOST(retriveHealthIdMobilePayLoad, acceptLanguage)

Verify Mobile OTP sent as  part of forgetHealth id.

Verify Mobile OTP sent as  part of forgetHealth id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForgotHealthIdNumberApi;

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

    ForgotHealthIdNumberApi apiInstance = new ForgotHealthIdNumberApi(defaultClient);
    RetriveHealthIdMobilePayLoad retriveHealthIdMobilePayLoad = new RetriveHealthIdMobilePayLoad(); // RetriveHealthIdMobilePayLoad | retriveHealthIdMobilePayLoad
    String acceptLanguage = "en-US"; // String | 
    try {
      RetrieveHealthIdPayloadResponse result = apiInstance.retrievalHealthIdByMobileUsingPOST(retriveHealthIdMobilePayLoad, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForgotHealthIdNumberApi#retrievalHealthIdByMobileUsingPOST");
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
| **retriveHealthIdMobilePayLoad** | [**RetriveHealthIdMobilePayLoad**](RetriveHealthIdMobilePayLoad.md)| retriveHealthIdMobilePayLoad | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

[**RetrieveHealthIdPayloadResponse**](RetrieveHealthIdPayloadResponse.md)

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

