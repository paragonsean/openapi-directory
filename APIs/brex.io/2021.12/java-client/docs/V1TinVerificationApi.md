# V1TinVerificationApi

All URIs are relative to *https://api.kompany.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tinVerificationBasicCheck**](V1TinVerificationApi.md#tinVerificationBasicCheck) | **GET** /api/v1/tin-verification/basic-check | Verifies a TIN number |
| [**tinVerificationComprehensiveCheck**](V1TinVerificationApi.md#tinVerificationComprehensiveCheck) | **GET** /api/v1/tin-verification/comprehensive-check | EIN Name Lookup with TIN number and retrieves company data |
| [**tinVerificationNameLookup**](V1TinVerificationApi.md#tinVerificationNameLookup) | **GET** /api/v1/tin-verification/name-lookup | EIN Name Lookup with TIN number |


<a id="tinVerificationBasicCheck"></a>
# **tinVerificationBasicCheck**
> TinVerificationBasicCheck200Response tinVerificationBasicCheck(tin, name)

Verifies a TIN number

Performs a basic verification check of a given TIN number and name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1TinVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1TinVerificationApi apiInstance = new V1TinVerificationApi(defaultClient);
    String tin = "tin_example"; // String | Nine letter TIN number with or without hyphens
    String name = "name_example"; // String | Company Name
    try {
      TinVerificationBasicCheck200Response result = apiInstance.tinVerificationBasicCheck(tin, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1TinVerificationApi#tinVerificationBasicCheck");
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
| **tin** | **String**| Nine letter TIN number with or without hyphens | |
| **name** | **String**| Company Name | |

### Return type

[**TinVerificationBasicCheck200Response**](TinVerificationBasicCheck200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of a basic TIN number check with company name |  -  |
| **0** |  |  -  |

<a id="tinVerificationComprehensiveCheck"></a>
# **tinVerificationComprehensiveCheck**
> TinVerificationComprehensiveCheck200Response tinVerificationComprehensiveCheck(tin, name, threshold)

EIN Name Lookup with TIN number and retrieves company data

Performs an EIN name match using provided TIN Number. Additionally to the name lookup it will lookup company details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1TinVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1TinVerificationApi apiInstance = new V1TinVerificationApi(defaultClient);
    String tin = "tin_example"; // String | Nine letter TIN number with or without hyphens
    String name = "name_example"; // String | Company Name
    Long threshold = 56L; // Long | The percentage of minimum similarity threshold for company matching (optional, default: 70%)
    try {
      TinVerificationComprehensiveCheck200Response result = apiInstance.tinVerificationComprehensiveCheck(tin, name, threshold);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1TinVerificationApi#tinVerificationComprehensiveCheck");
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
| **tin** | **String**| Nine letter TIN number with or without hyphens | |
| **name** | **String**| Company Name | |
| **threshold** | **Long**| The percentage of minimum similarity threshold for company matching (optional, default: 70%) | [optional] |

### Return type

[**TinVerificationComprehensiveCheck200Response**](TinVerificationComprehensiveCheck200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of a basic TIN number check with company name and the list of matched companies |  -  |
| **0** |  |  -  |

<a id="tinVerificationNameLookup"></a>
# **tinVerificationNameLookup**
> TinVerificationNameLookup200Response tinVerificationNameLookup(tin)

EIN Name Lookup with TIN number

Performs an EIN name match using provided TIN Number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1TinVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1TinVerificationApi apiInstance = new V1TinVerificationApi(defaultClient);
    String tin = "tin_example"; // String | Nine letter TIN number with or without hyphens
    try {
      TinVerificationNameLookup200Response result = apiInstance.tinVerificationNameLookup(tin);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1TinVerificationApi#tinVerificationNameLookup");
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
| **tin** | **String**| Nine letter TIN number with or without hyphens | |

### Return type

[**TinVerificationNameLookup200Response**](TinVerificationNameLookup200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of a EIN name lookup with TIN number |  -  |
| **0** |  |  -  |

