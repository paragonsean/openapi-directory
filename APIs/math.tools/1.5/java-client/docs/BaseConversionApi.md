# BaseConversionApi

All URIs are relative to *https://api.math.tools*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**numbersBaseBinaryGet**](BaseConversionApi.md#numbersBaseBinaryGet) | **GET** /numbers/base/binary |  |
| [**numbersBaseGet**](BaseConversionApi.md#numbersBaseGet) | **GET** /numbers/base |  |
| [**numbersBaseHexGet**](BaseConversionApi.md#numbersBaseHexGet) | **GET** /numbers/base/hex |  |
| [**numbersBaseOctalGet**](BaseConversionApi.md#numbersBaseOctalGet) | **GET** /numbers/base/octal |  |


<a id="numbersBaseBinaryGet"></a>
# **numbersBaseBinaryGet**
> numbersBaseBinaryGet(number, from)



Convert a given number to binary

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BaseConversionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.math.tools");
    
    // Configure API key authorization: X-Mathtools-Api-Secret
    ApiKeyAuth X-Mathtools-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Mathtools-Api-Secret");
    X-Mathtools-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Mathtools-Api-Secret.setApiKeyPrefix("Token");

    BaseConversionApi apiInstance = new BaseConversionApi(defaultClient);
    Integer number = 56; // Integer | Number to convert to binary
    Integer from = 56; // Integer | Base of the supplied number (Optional base 10 assumed by default)
    try {
      apiInstance.numbersBaseBinaryGet(number, from);
    } catch (ApiException e) {
      System.err.println("Exception when calling BaseConversionApi#numbersBaseBinaryGet");
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
| **number** | **Integer**| Number to convert to binary | |
| **from** | **Integer**| Base of the supplied number (Optional base 10 assumed by default) | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 success response |  -  |
| **401** | 401 Unauthorized response |  -  |

<a id="numbersBaseGet"></a>
# **numbersBaseGet**
> numbersBaseGet(number, to, from)



Convert a given number from one base to another base

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BaseConversionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.math.tools");
    
    // Configure API key authorization: X-Mathtools-Api-Secret
    ApiKeyAuth X-Mathtools-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Mathtools-Api-Secret");
    X-Mathtools-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Mathtools-Api-Secret.setApiKeyPrefix("Token");

    BaseConversionApi apiInstance = new BaseConversionApi(defaultClient);
    Integer number = 56; // Integer | Number to convert to the target base
    Integer to = 56; // Integer | Target base to convert to
    Integer from = 56; // Integer | Base of the supplied number (Optional base 10 assumed by default)
    try {
      apiInstance.numbersBaseGet(number, to, from);
    } catch (ApiException e) {
      System.err.println("Exception when calling BaseConversionApi#numbersBaseGet");
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
| **number** | **Integer**| Number to convert to the target base | |
| **to** | **Integer**| Target base to convert to | |
| **from** | **Integer**| Base of the supplied number (Optional base 10 assumed by default) | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 success response |  -  |
| **401** | 401 Unauthorized response |  -  |

<a id="numbersBaseHexGet"></a>
# **numbersBaseHexGet**
> numbersBaseHexGet(number, from)



Convert a given number to hexadecimal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BaseConversionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.math.tools");
    
    // Configure API key authorization: X-Mathtools-Api-Secret
    ApiKeyAuth X-Mathtools-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Mathtools-Api-Secret");
    X-Mathtools-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Mathtools-Api-Secret.setApiKeyPrefix("Token");

    BaseConversionApi apiInstance = new BaseConversionApi(defaultClient);
    Integer number = 56; // Integer | Number to convert to hex
    Integer from = 56; // Integer | Base of the supplied number (Optional base 10 assumed by default)
    try {
      apiInstance.numbersBaseHexGet(number, from);
    } catch (ApiException e) {
      System.err.println("Exception when calling BaseConversionApi#numbersBaseHexGet");
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
| **number** | **Integer**| Number to convert to hex | |
| **from** | **Integer**| Base of the supplied number (Optional base 10 assumed by default) | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 success response |  -  |
| **401** | 401 Unauthorized response |  -  |

<a id="numbersBaseOctalGet"></a>
# **numbersBaseOctalGet**
> numbersBaseOctalGet(number, from)



Convert a given number to octal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BaseConversionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.math.tools");
    
    // Configure API key authorization: X-Mathtools-Api-Secret
    ApiKeyAuth X-Mathtools-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Mathtools-Api-Secret");
    X-Mathtools-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Mathtools-Api-Secret.setApiKeyPrefix("Token");

    BaseConversionApi apiInstance = new BaseConversionApi(defaultClient);
    Integer number = 56; // Integer | Number to convert to octal
    Integer from = 56; // Integer | Base of the supplied number (Optional base 10 assumed by default)
    try {
      apiInstance.numbersBaseOctalGet(number, from);
    } catch (ApiException e) {
      System.err.println("Exception when calling BaseConversionApi#numbersBaseOctalGet");
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
| **number** | **Integer**| Number to convert to octal | |
| **from** | **Integer**| Base of the supplied number (Optional base 10 assumed by default) | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Mathtools-Api-Secret](../README.md#X-Mathtools-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 success response |  -  |
| **401** | 401 Unauthorized response |  -  |

