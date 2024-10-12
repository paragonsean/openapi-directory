# IntegratedProgramsApi

All URIs are relative to *https://healthidsbx.ndhm.gov.in/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createHealthIdByDemoAuthUsingPOST**](IntegratedProgramsApi.md#createHealthIdByDemoAuthUsingPOST) | **POST** /v1/hid/benefit/createHealthId/demo/auth | Create health id using Aadhaar Demo Auth. |
| [**createHealthIdByMobileUsingPOST**](IntegratedProgramsApi.md#createHealthIdByMobileUsingPOST) | **POST** /v1/hid/benefit/mobile/createHealthId | Create health id using mobile Authentication. |
| [**delinkHidBenefitUsingPOST**](IntegratedProgramsApi.md#delinkHidBenefitUsingPOST) | **POST** /v1/hid/benefit/delink | De-Linked with hid. |
| [**findByAadharUsingPOST**](IntegratedProgramsApi.md#findByAadharUsingPOST) | **POST** /v1/hid/benefit/search/aadhaar | Search health id number using aadhar or aadhar token. |
| [**findByHealthIdUsingPOST**](IntegratedProgramsApi.md#findByHealthIdUsingPOST) | **POST** /v1/hid/benefit/search/healthIdNumber | Search benefit using health id number. |
| [**generateAadharOTPUsingPOST2**](IntegratedProgramsApi.md#generateAadharOTPUsingPOST2) | **POST** /v1/hid/benefit/aadhaar/generateOtp | Generate Aadhaar OTP on registrered mobile number |
| [**generateMobileOtpUsingPOST**](IntegratedProgramsApi.md#generateMobileOtpUsingPOST) | **POST** /v1/hid/benefit/mobile/generateOtp | Generate mobile OTP on registrered mobile number |
| [**linkHidBenefitUsingPOST**](IntegratedProgramsApi.md#linkHidBenefitUsingPOST) | **POST** /v1/hid/benefit/link | Linked with hid. |
| [**notifyBenefitUsingPOST**](IntegratedProgramsApi.md#notifyBenefitUsingPOST) | **POST** /v1/hid/benefit/notify/benefit | Create health id using notify Benefit. |
| [**updateAccountInformationUsingPOST1**](IntegratedProgramsApi.md#updateAccountInformationUsingPOST1) | **POST** /v1/hid/benefit/update/profile | Update account information |
| [**updateMobileInformationUsingPOST**](IntegratedProgramsApi.md#updateMobileInformationUsingPOST) | **POST** /v1/hid/benefit/update/mobile | Update mobile number for account. |
| [**updateStatusUsingPOST**](IntegratedProgramsApi.md#updateStatusUsingPOST) | **POST** /v1/hid/benefit/update/status | Update health id status . |
| [**verifyAadharOtpUsingPOST**](IntegratedProgramsApi.md#verifyAadharOtpUsingPOST) | **POST** /v1/hid/benefit/aadhaar/verifyAadharOtp | Create health id using Aadhaar Number Otp. |
| [**verifyBioUsingPOST**](IntegratedProgramsApi.md#verifyBioUsingPOST) | **POST** /v1/hid/benefit/aadhaar/verifyBio | Create health id using Biometric Authentication. |


<a id="createHealthIdByDemoAuthUsingPOST"></a>
# **createHealthIdByDemoAuthUsingPOST**
> HidBenefitRequestPayload createHealthIdByDemoAuthUsingPOST(createHIdDemoAuthRequest, acceptLanguage)

Create health id using Aadhaar Demo Auth.

Create health id using Aadhaar Demo Auth.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegratedProgramsApi;

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

    IntegratedProgramsApi apiInstance = new IntegratedProgramsApi(defaultClient);
    CreateHIdDemoAuthRequest createHIdDemoAuthRequest = new CreateHIdDemoAuthRequest(); // CreateHIdDemoAuthRequest | createHIdDemoAuthRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      HidBenefitRequestPayload result = apiInstance.createHealthIdByDemoAuthUsingPOST(createHIdDemoAuthRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegratedProgramsApi#createHealthIdByDemoAuthUsingPOST");
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
| **createHIdDemoAuthRequest** | [**CreateHIdDemoAuthRequest**](CreateHIdDemoAuthRequest.md)| createHIdDemoAuthRequest | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

[**HidBenefitRequestPayload**](HidBenefitRequestPayload.md)

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

<a id="createHealthIdByMobileUsingPOST"></a>
# **createHealthIdByMobileUsingPOST**
> TxnResponse createHealthIdByMobileUsingPOST(createHidMobileRequest, acceptLanguage)

Create health id using mobile Authentication.

Create health id using mobile Authentication.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegratedProgramsApi;

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

    IntegratedProgramsApi apiInstance = new IntegratedProgramsApi(defaultClient);
    CreateHidMobileRequest createHidMobileRequest = new CreateHidMobileRequest(); // CreateHidMobileRequest | createHidMobileRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      TxnResponse result = apiInstance.createHealthIdByMobileUsingPOST(createHidMobileRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegratedProgramsApi#createHealthIdByMobileUsingPOST");
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
| **createHidMobileRequest** | [**CreateHidMobileRequest**](CreateHidMobileRequest.md)| createHidMobileRequest | |
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

<a id="delinkHidBenefitUsingPOST"></a>
# **delinkHidBenefitUsingPOST**
> HidBenefitLinkedResponsePayload delinkHidBenefitUsingPOST(hidBenefitLinkedRequestPayload, acceptLanguage)

De-Linked with hid.

De-Linked with hid.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegratedProgramsApi;

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

    IntegratedProgramsApi apiInstance = new IntegratedProgramsApi(defaultClient);
    HidBenefitDelinkRequestPayload hidBenefitLinkedRequestPayload = new HidBenefitDelinkRequestPayload(); // HidBenefitDelinkRequestPayload | hidBenefitLinkedRequestPayload
    String acceptLanguage = "en-US"; // String | 
    try {
      HidBenefitLinkedResponsePayload result = apiInstance.delinkHidBenefitUsingPOST(hidBenefitLinkedRequestPayload, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegratedProgramsApi#delinkHidBenefitUsingPOST");
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
| **hidBenefitLinkedRequestPayload** | [**HidBenefitDelinkRequestPayload**](HidBenefitDelinkRequestPayload.md)| hidBenefitLinkedRequestPayload | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

[**HidBenefitLinkedResponsePayload**](HidBenefitLinkedResponsePayload.md)

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

<a id="findByAadharUsingPOST"></a>
# **findByAadharUsingPOST**
> List&lt;Object&gt; findByAadharUsingPOST(aadharNumberRequestPayload, acceptLanguage)

Search health id number using aadhar or aadhar token.

Search health id number using aadhar or aadhar token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegratedProgramsApi;

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

    IntegratedProgramsApi apiInstance = new IntegratedProgramsApi(defaultClient);
    AadharNumberRequestPayload aadharNumberRequestPayload = new AadharNumberRequestPayload(); // AadharNumberRequestPayload | aadharNumberRequestPayload
    String acceptLanguage = "en-US"; // String | 
    try {
      List<Object> result = apiInstance.findByAadharUsingPOST(aadharNumberRequestPayload, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegratedProgramsApi#findByAadharUsingPOST");
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

<a id="findByHealthIdUsingPOST"></a>
# **findByHealthIdUsingPOST**
> List&lt;HidBenefitSearchResponsePayload&gt; findByHealthIdUsingPOST(searchRequest, acceptLanguage)

Search benefit using health id number.

Search benefit using health id number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegratedProgramsApi;

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

    IntegratedProgramsApi apiInstance = new IntegratedProgramsApi(defaultClient);
    HidBenefitNameSearchRequest searchRequest = new HidBenefitNameSearchRequest(); // HidBenefitNameSearchRequest | searchRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      List<HidBenefitSearchResponsePayload> result = apiInstance.findByHealthIdUsingPOST(searchRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegratedProgramsApi#findByHealthIdUsingPOST");
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
| **searchRequest** | [**HidBenefitNameSearchRequest**](HidBenefitNameSearchRequest.md)| searchRequest | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

[**List&lt;HidBenefitSearchResponsePayload&gt;**](HidBenefitSearchResponsePayload.md)

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

<a id="generateAadharOTPUsingPOST2"></a>
# **generateAadharOTPUsingPOST2**
> TxnResponse generateAadharOTPUsingPOST2(generateOtpRequest, acceptLanguage)

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
import org.openapitools.client.api.IntegratedProgramsApi;

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

    IntegratedProgramsApi apiInstance = new IntegratedProgramsApi(defaultClient);
    AadharOtpGenerateRequestPayLoad generateOtpRequest = new AadharOtpGenerateRequestPayLoad(); // AadharOtpGenerateRequestPayLoad | generateOtpRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      TxnResponse result = apiInstance.generateAadharOTPUsingPOST2(generateOtpRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegratedProgramsApi#generateAadharOTPUsingPOST2");
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

<a id="generateMobileOtpUsingPOST"></a>
# **generateMobileOtpUsingPOST**
> TxnResponse generateMobileOtpUsingPOST(generateOtpRequest, acceptLanguage)

Generate mobile OTP on registrered mobile number

Generate mobile OTP on registrered mobile number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegratedProgramsApi;

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

    IntegratedProgramsApi apiInstance = new IntegratedProgramsApi(defaultClient);
    GenerateMobileOTPRequest generateOtpRequest = new GenerateMobileOTPRequest(); // GenerateMobileOTPRequest | generateOtpRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      TxnResponse result = apiInstance.generateMobileOtpUsingPOST(generateOtpRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegratedProgramsApi#generateMobileOtpUsingPOST");
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

<a id="linkHidBenefitUsingPOST"></a>
# **linkHidBenefitUsingPOST**
> HidBenefitLinkedResponsePayload linkHidBenefitUsingPOST(hidBenefitLinkedRequestPayload, acceptLanguage)

Linked with hid.

Linked with hid.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegratedProgramsApi;

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

    IntegratedProgramsApi apiInstance = new IntegratedProgramsApi(defaultClient);
    HidBenefitLinkedRequestPayload hidBenefitLinkedRequestPayload = new HidBenefitLinkedRequestPayload(); // HidBenefitLinkedRequestPayload | hidBenefitLinkedRequestPayload
    String acceptLanguage = "en-US"; // String | 
    try {
      HidBenefitLinkedResponsePayload result = apiInstance.linkHidBenefitUsingPOST(hidBenefitLinkedRequestPayload, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegratedProgramsApi#linkHidBenefitUsingPOST");
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
| **hidBenefitLinkedRequestPayload** | [**HidBenefitLinkedRequestPayload**](HidBenefitLinkedRequestPayload.md)| hidBenefitLinkedRequestPayload | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

[**HidBenefitLinkedResponsePayload**](HidBenefitLinkedResponsePayload.md)

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

<a id="notifyBenefitUsingPOST"></a>
# **notifyBenefitUsingPOST**
> HidBenefitRequestPayload notifyBenefitUsingPOST(createHidNotifyBenefitRequest, acceptLanguage)

Create health id using notify Benefit.

Create health id using notify Benefit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegratedProgramsApi;

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

    IntegratedProgramsApi apiInstance = new IntegratedProgramsApi(defaultClient);
    CreateHidNotifyBenefitRequest createHidNotifyBenefitRequest = new CreateHidNotifyBenefitRequest(); // CreateHidNotifyBenefitRequest | createHidNotifyBenefitRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      HidBenefitRequestPayload result = apiInstance.notifyBenefitUsingPOST(createHidNotifyBenefitRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegratedProgramsApi#notifyBenefitUsingPOST");
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
| **createHidNotifyBenefitRequest** | [**CreateHidNotifyBenefitRequest**](CreateHidNotifyBenefitRequest.md)| createHidNotifyBenefitRequest | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

[**HidBenefitRequestPayload**](HidBenefitRequestPayload.md)

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

<a id="updateAccountInformationUsingPOST1"></a>
# **updateAccountInformationUsingPOST1**
> UserDTO updateAccountInformationUsingPOST1(request, acceptLanguage)

Update account information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegratedProgramsApi;

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

    IntegratedProgramsApi apiInstance = new IntegratedProgramsApi(defaultClient);
    HidUpdateAccountRequest request = new HidUpdateAccountRequest(); // HidUpdateAccountRequest | request
    String acceptLanguage = "en-US"; // String | 
    try {
      UserDTO result = apiInstance.updateAccountInformationUsingPOST1(request, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegratedProgramsApi#updateAccountInformationUsingPOST1");
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
| **request** | [**HidUpdateAccountRequest**](HidUpdateAccountRequest.md)| request | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

[**UserDTO**](UserDTO.md)

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

<a id="updateMobileInformationUsingPOST"></a>
# **updateMobileInformationUsingPOST**
> UserDTO updateMobileInformationUsingPOST(request, acceptLanguage)

Update mobile number for account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegratedProgramsApi;

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

    IntegratedProgramsApi apiInstance = new IntegratedProgramsApi(defaultClient);
    HidUpdateMobiletRequest request = new HidUpdateMobiletRequest(); // HidUpdateMobiletRequest | request
    String acceptLanguage = "en-US"; // String | 
    try {
      UserDTO result = apiInstance.updateMobileInformationUsingPOST(request, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegratedProgramsApi#updateMobileInformationUsingPOST");
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
| **request** | [**HidUpdateMobiletRequest**](HidUpdateMobiletRequest.md)| request | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

[**UserDTO**](UserDTO.md)

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

<a id="updateStatusUsingPOST"></a>
# **updateStatusUsingPOST**
> Boolean updateStatusUsingPOST(generateOtpRequest, acceptLanguage)

Update health id status .

Update health id status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegratedProgramsApi;

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

    IntegratedProgramsApi apiInstance = new IntegratedProgramsApi(defaultClient);
    HidStatusRequestPayload generateOtpRequest = new HidStatusRequestPayload(); // HidStatusRequestPayload | generateOtpRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      Boolean result = apiInstance.updateStatusUsingPOST(generateOtpRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegratedProgramsApi#updateStatusUsingPOST");
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
| **generateOtpRequest** | [**HidStatusRequestPayload**](HidStatusRequestPayload.md)| generateOtpRequest | |
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

<a id="verifyAadharOtpUsingPOST"></a>
# **verifyAadharOtpUsingPOST**
> HidBenefitRequestPayload verifyAadharOtpUsingPOST(createHealthIdOptRequest, acceptLanguage)

Create health id using Aadhaar Number Otp.

Create health id using Aadhaar number opt

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegratedProgramsApi;

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

    IntegratedProgramsApi apiInstance = new IntegratedProgramsApi(defaultClient);
    CreateHealthIdOptRequest createHealthIdOptRequest = new CreateHealthIdOptRequest(); // CreateHealthIdOptRequest | createHealthIdOptRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      HidBenefitRequestPayload result = apiInstance.verifyAadharOtpUsingPOST(createHealthIdOptRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegratedProgramsApi#verifyAadharOtpUsingPOST");
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
| **createHealthIdOptRequest** | [**CreateHealthIdOptRequest**](CreateHealthIdOptRequest.md)| createHealthIdOptRequest | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

[**HidBenefitRequestPayload**](HidBenefitRequestPayload.md)

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

<a id="verifyBioUsingPOST"></a>
# **verifyBioUsingPOST**
> HidBenefitRequestPayload verifyBioUsingPOST(createHidBiometricRequest, acceptLanguage)

Create health id using Biometric Authentication.

Create health id using Biometric Authentication.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegratedProgramsApi;

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

    IntegratedProgramsApi apiInstance = new IntegratedProgramsApi(defaultClient);
    CreateHidBiometricRequest createHidBiometricRequest = new CreateHidBiometricRequest(); // CreateHidBiometricRequest | createHidBiometricRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      HidBenefitRequestPayload result = apiInstance.verifyBioUsingPOST(createHidBiometricRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegratedProgramsApi#verifyBioUsingPOST");
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
| **createHidBiometricRequest** | [**CreateHidBiometricRequest**](CreateHidBiometricRequest.md)| createHidBiometricRequest | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

[**HidBenefitRequestPayload**](HidBenefitRequestPayload.md)

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

