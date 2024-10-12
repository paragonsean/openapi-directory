# NumberSystemsConversionApi

All URIs are relative to *https://api.math.tools*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**numbersNumeralChineseGet**](NumberSystemsConversionApi.md#numbersNumeralChineseGet) | **GET** /numbers/numeral/chinese |  |
| [**numbersNumeralEgyptianGet**](NumberSystemsConversionApi.md#numbersNumeralEgyptianGet) | **GET** /numbers/numeral/egyptian |  |
| [**numbersNumeralRomanGet**](NumberSystemsConversionApi.md#numbersNumeralRomanGet) | **GET** /numbers/numeral/roman |  |


<a id="numbersNumeralChineseGet"></a>
# **numbersNumeralChineseGet**
> numbersNumeralChineseGet(number)



Convert base 10 representation of a given number to chinese numeral.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumberSystemsConversionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.math.tools");
    
    // Configure API key authorization: X-Mathtools-Api-Secret
    ApiKeyAuth X-Mathtools-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Mathtools-Api-Secret");
    X-Mathtools-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Mathtools-Api-Secret.setApiKeyPrefix("Token");

    NumberSystemsConversionApi apiInstance = new NumberSystemsConversionApi(defaultClient);
    Integer number = 56; // Integer | Number to convert
    try {
      apiInstance.numbersNumeralChineseGet(number);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumberSystemsConversionApi#numbersNumeralChineseGet");
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
| **number** | **Integer**| Number to convert | [optional] |

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
| **200** | 200 Success response |  -  |
| **401** | 401 Unauthorized response |  -  |

<a id="numbersNumeralEgyptianGet"></a>
# **numbersNumeralEgyptianGet**
> numbersNumeralEgyptianGet(number)



Convert base 10 representation of a given number to egyptian numeral.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumberSystemsConversionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.math.tools");
    
    // Configure API key authorization: X-Mathtools-Api-Secret
    ApiKeyAuth X-Mathtools-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Mathtools-Api-Secret");
    X-Mathtools-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Mathtools-Api-Secret.setApiKeyPrefix("Token");

    NumberSystemsConversionApi apiInstance = new NumberSystemsConversionApi(defaultClient);
    Integer number = 56; // Integer | Number to convert
    try {
      apiInstance.numbersNumeralEgyptianGet(number);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumberSystemsConversionApi#numbersNumeralEgyptianGet");
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
| **number** | **Integer**| Number to convert | [optional] |

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
| **200** | 200 Success response |  -  |
| **401** | 401 Unauthorized response |  -  |

<a id="numbersNumeralRomanGet"></a>
# **numbersNumeralRomanGet**
> numbersNumeralRomanGet(number)



Convert base 10 representation of a given number to roman numeral.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumberSystemsConversionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.math.tools");
    
    // Configure API key authorization: X-Mathtools-Api-Secret
    ApiKeyAuth X-Mathtools-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Mathtools-Api-Secret");
    X-Mathtools-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Mathtools-Api-Secret.setApiKeyPrefix("Token");

    NumberSystemsConversionApi apiInstance = new NumberSystemsConversionApi(defaultClient);
    Integer number = 56; // Integer | Number to convert
    try {
      apiInstance.numbersNumeralRomanGet(number);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumberSystemsConversionApi#numbersNumeralRomanGet");
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
| **number** | **Integer**| Number to convert | [optional] |

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
| **200** | 200 Success response |  -  |
| **401** | 401 Unauthorized response |  -  |

