# V1EinVerificationApi

All URIs are relative to *https://api.kompany.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**einVerificationBasic**](V1EinVerificationApi.md#einVerificationBasic) | **GET** /api/v1/ein-verification/basic-check | Verifies an EIN number |
| [**einVerificationComprehensive**](V1EinVerificationApi.md#einVerificationComprehensive) | **GET** /api/v1/ein-verification/comprehensive-check | Verifies EIN number and retrieves company data |
| [**einVerificationLookup**](V1EinVerificationApi.md#einVerificationLookup) | **GET** /api/v1/ein-verification/lookup | Retrieves a list of EIN numbers |


<a id="einVerificationBasic"></a>
# **einVerificationBasic**
> EinVerificationBasic200Response einVerificationBasic(ein)

Verifies an EIN number

Performs a basic verification check of a given EIN tax number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1EinVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1EinVerificationApi apiInstance = new V1EinVerificationApi(defaultClient);
    String ein = "ein_example"; // String | Nine letter EIN number with or without hyphens
    try {
      EinVerificationBasic200Response result = apiInstance.einVerificationBasic(ein);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1EinVerificationApi#einVerificationBasic");
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
| **ein** | **String**| Nine letter EIN number with or without hyphens | |

### Return type

[**EinVerificationBasic200Response**](EinVerificationBasic200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of a basic EIN number verification |  -  |
| **0** |  |  -  |

<a id="einVerificationComprehensive"></a>
# **einVerificationComprehensive**
> EinVerificationComprehensive200Response einVerificationComprehensive(ein)

Verifies EIN number and retrieves company data

Comprehensive verification of a given EIN number. Additionally to the basic verification it will lookup company details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1EinVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1EinVerificationApi apiInstance = new V1EinVerificationApi(defaultClient);
    String ein = "ein_example"; // String | Nine letter EIN number with or without hyphens
    try {
      EinVerificationComprehensive200Response result = apiInstance.einVerificationComprehensive(ein);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1EinVerificationApi#einVerificationComprehensive");
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
| **ein** | **String**| Nine letter EIN number with or without hyphens | |

### Return type

[**EinVerificationComprehensive200Response**](EinVerificationComprehensive200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of a comprehensive EIN number verification |  -  |
| **0** |  |  -  |

<a id="einVerificationLookup"></a>
# **einVerificationLookup**
> EinVerificationLookup200Response einVerificationLookup(name, state, zip, tight)

Retrieves a list of EIN numbers

Lookup EIN number for a company by its company name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1EinVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1EinVerificationApi apiInstance = new V1EinVerificationApi(defaultClient);
    String name = "name_example"; // String | Business name of the company
    String state = "state_example"; // String | Optional state parameter to improve results. (Two letter code for example CA or US-CA for California)
    String zip = "zip_example"; // String | Optional zip code parameter to improve results. (Zip is preferred over state)
    Boolean tight = true; // Boolean | Optional parameter to do tight matching. (Only the best match will be returned rather then the top 5)
    try {
      EinVerificationLookup200Response result = apiInstance.einVerificationLookup(name, state, zip, tight);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1EinVerificationApi#einVerificationLookup");
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
| **name** | **String**| Business name of the company | |
| **state** | **String**| Optional state parameter to improve results. (Two letter code for example CA or US-CA for California) | [optional] |
| **zip** | **String**| Optional zip code parameter to improve results. (Zip is preferred over state) | [optional] |
| **tight** | **Boolean**| Optional parameter to do tight matching. (Only the best match will be returned rather then the top 5) | [optional] |

### Return type

[**EinVerificationLookup200Response**](EinVerificationLookup200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of a EIN reverse lookup |  -  |
| **0** |  |  -  |

