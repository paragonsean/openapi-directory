# V1NifVerificationApi

All URIs are relative to *https://api.kompany.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**nifBasic**](V1NifVerificationApi.md#nifBasic) | **POST** /api/v1/nif-verification/basic-check/{country} | Verifies a NIF number |
| [**nifComprehensive**](V1NifVerificationApi.md#nifComprehensive) | **POST** /api/v1/nif-verification/comprehensive-check/{country} | Verifies a NIF number and retrieves company data |


<a id="nifBasic"></a>
# **nifBasic**
> NifBasic200Response nifBasic(country, nifNumber, companyAddress, companyName)

Verifies a NIF number

Performs a basic verification check of a given NIF tax number against NIF.com. Optional parameters may be added to improve calculation of confidence score.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1NifVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1NifVerificationApi apiInstance = new V1NifVerificationApi(defaultClient);
    String country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
    String nifNumber = "nifNumber_example"; // String | NIF number to validate
    String companyAddress = "companyAddress_example"; // String | company address lines
    String companyName = "companyName_example"; // String | Company name
    try {
      NifBasic200Response result = apiInstance.nifBasic(country, nifNumber, companyAddress, companyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1NifVerificationApi#nifBasic");
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
| **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | |
| **nifNumber** | **String**| NIF number to validate | |
| **companyAddress** | **String**| company address lines | [optional] |
| **companyName** | **String**| Company name | [optional] |

### Return type

[**NifBasic200Response**](NifBasic200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of a basic NIF verification |  -  |
| **0** |  |  -  |

<a id="nifComprehensive"></a>
# **nifComprehensive**
> NifComprehensive200Response nifComprehensive(country, nifNumber, companyAddress, companyName)

Verifies a NIF number and retrieves company data

Comprehensive verification of given portuguese NIF number against NIF.com. Optional parameters may help to build a better confidence score. Additional company data will be provided.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1NifVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1NifVerificationApi apiInstance = new V1NifVerificationApi(defaultClient);
    String country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
    String nifNumber = "nifNumber_example"; // String | NIF number to validate
    String companyAddress = "companyAddress_example"; // String | company address lines
    String companyName = "companyName_example"; // String | Company name
    try {
      NifComprehensive200Response result = apiInstance.nifComprehensive(country, nifNumber, companyAddress, companyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1NifVerificationApi#nifComprehensive");
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
| **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | |
| **nifNumber** | **String**| NIF number to validate | |
| **companyAddress** | **String**| company address lines | [optional] |
| **companyName** | **String**| Company name | [optional] |

### Return type

[**NifComprehensive200Response**](NifComprehensive200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of a comprehensive NIF verification |  -  |
| **0** |  |  -  |

