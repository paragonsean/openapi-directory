# V1SystemApi

All URIs are relative to *https://api.kompany.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**healthCheck**](V1SystemApi.md#healthCheck) | **GET** /api/v1/system/health | Returns the health information for the official business registers based on usage. |
| [**systemCountries**](V1SystemApi.md#systemCountries) | **GET** /api/v1/system/countries | Returns a list of countries |
| [**systemPricelist**](V1SystemApi.md#systemPricelist) | **GET** /api/v1/system/pricelist | Returns a list of products with prices |


<a id="healthCheck"></a>
# **healthCheck**
> List&lt;HealthCheck200ResponseInner&gt; healthCheck()

Returns the health information for the official business registers based on usage.

Returns the health information for the official business registers based on usage.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1SystemApi apiInstance = new V1SystemApi(defaultClient);
    try {
      List<HealthCheck200ResponseInner> result = apiInstance.healthCheck();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1SystemApi#healthCheck");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;HealthCheck200ResponseInner&gt;**](HealthCheck200ResponseInner.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of the commercial registers and their health data |  -  |
| **0** |  |  -  |

<a id="systemCountries"></a>
# **systemCountries**
> List&lt;SystemCountries200ResponseInner&gt; systemCountries()

Returns a list of countries

Retrieve the list of all currently enabled countries

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1SystemApi apiInstance = new V1SystemApi(defaultClient);
    try {
      List<SystemCountries200ResponseInner> result = apiInstance.systemCountries();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1SystemApi#systemCountries");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;SystemCountries200ResponseInner&gt;**](SystemCountries200ResponseInner.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of countries |  -  |
| **0** | Detailed information about the error |  -  |

<a id="systemPricelist"></a>
# **systemPricelist**
> List&lt;SystemPricelist200ResponseInner&gt; systemPricelist()

Returns a list of products with prices

Retrieve pricing rules for your subscription plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1SystemApi apiInstance = new V1SystemApi(defaultClient);
    try {
      List<SystemPricelist200ResponseInner> result = apiInstance.systemPricelist();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1SystemApi#systemPricelist");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;SystemPricelist200ResponseInner&gt;**](SystemPricelist200ResponseInner.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of pricing rules |  -  |
| **0** |  |  -  |

