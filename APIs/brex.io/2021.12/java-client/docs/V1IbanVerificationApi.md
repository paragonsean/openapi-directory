# V1IbanVerificationApi

All URIs are relative to *https://api.kompany.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ibanBasic**](V1IbanVerificationApi.md#ibanBasic) | **POST** /api/v1/iban-verification/check-iban | Checks validity of an IBAN number |
| [**ibanComprehensive**](V1IbanVerificationApi.md#ibanComprehensive) | **POST** /api/v1/iban-verification/comprehensive-check-iban | Checks validity of an IBAN number |


<a id="ibanBasic"></a>
# **ibanBasic**
> IbanBasic200Response ibanBasic(ibanNumber)

Checks validity of an IBAN number

Basic verification of an IBAN number validating its structure

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1IbanVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1IbanVerificationApi apiInstance = new V1IbanVerificationApi(defaultClient);
    String ibanNumber = "ibanNumber_example"; // String | IBAN number to validate
    try {
      IbanBasic200Response result = apiInstance.ibanBasic(ibanNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1IbanVerificationApi#ibanBasic");
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
| **ibanNumber** | **String**| IBAN number to validate | |

### Return type

[**IbanBasic200Response**](IbanBasic200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Denotes validity of checked IBAN |  -  |
| **0** |  |  -  |

<a id="ibanComprehensive"></a>
# **ibanComprehensive**
> Object ibanComprehensive(ibanNumber)

Checks validity of an IBAN number

Comprehensive verification of IBAN number using a service provider for verification

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1IbanVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1IbanVerificationApi apiInstance = new V1IbanVerificationApi(defaultClient);
    String ibanNumber = "ibanNumber_example"; // String | IBAN number to validate
    try {
      Object result = apiInstance.ibanComprehensive(ibanNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1IbanVerificationApi#ibanComprehensive");
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
| **ibanNumber** | **String**| IBAN number to validate | |

### Return type

**Object**

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Denotes validity of checked IBAN and provides comprehensive information |  -  |
| **0** |  |  -  |

