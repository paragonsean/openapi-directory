# DialectApi

All URIs are relative to *http://api.funtranslations.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**translateBrooklynGet**](DialectApi.md#translateBrooklynGet) | **GET** /translate/brooklyn |  |
| [**translateCockneyGet**](DialectApi.md#translateCockneyGet) | **GET** /translate/cockney |  |
| [**translateJiveGet**](DialectApi.md#translateJiveGet) | **GET** /translate/jive |  |
| [**translateValspeakGet**](DialectApi.md#translateValspeakGet) | **GET** /translate/valspeak |  |


<a id="translateBrooklynGet"></a>
# **translateBrooklynGet**
> translateBrooklynGet(text)



Translate from English to Brooklyn Speak.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DialectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.funtranslations.com");
    
    // Configure API key authorization: X-Funtranslations-Api-Secret
    ApiKeyAuth X-Funtranslations-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Funtranslations-Api-Secret");
    X-Funtranslations-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Funtranslations-Api-Secret.setApiKeyPrefix("Token");

    DialectApi apiInstance = new DialectApi(defaultClient);
    String text = "text_example"; // String | Text to translate
    try {
      apiInstance.translateBrooklynGet(text);
    } catch (ApiException e) {
      System.err.println("Exception when calling DialectApi#translateBrooklynGet");
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
| **text** | **String**| Text to translate | |

### Return type

null (empty response body)

### Authorization

[X-Funtranslations-Api-Secret](../README.md#X-Funtranslations-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="translateCockneyGet"></a>
# **translateCockneyGet**
> translateCockneyGet(text)



Translate from English to Cockney Speak.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DialectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.funtranslations.com");
    
    // Configure API key authorization: X-Funtranslations-Api-Secret
    ApiKeyAuth X-Funtranslations-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Funtranslations-Api-Secret");
    X-Funtranslations-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Funtranslations-Api-Secret.setApiKeyPrefix("Token");

    DialectApi apiInstance = new DialectApi(defaultClient);
    String text = "text_example"; // String | Text to translate
    try {
      apiInstance.translateCockneyGet(text);
    } catch (ApiException e) {
      System.err.println("Exception when calling DialectApi#translateCockneyGet");
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
| **text** | **String**| Text to translate | |

### Return type

null (empty response body)

### Authorization

[X-Funtranslations-Api-Secret](../README.md#X-Funtranslations-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="translateJiveGet"></a>
# **translateJiveGet**
> translateJiveGet(text)



Translate from normal English to Jive Speak.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DialectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.funtranslations.com");
    
    // Configure API key authorization: X-Funtranslations-Api-Secret
    ApiKeyAuth X-Funtranslations-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Funtranslations-Api-Secret");
    X-Funtranslations-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Funtranslations-Api-Secret.setApiKeyPrefix("Token");

    DialectApi apiInstance = new DialectApi(defaultClient);
    String text = "text_example"; // String | Text to translate
    try {
      apiInstance.translateJiveGet(text);
    } catch (ApiException e) {
      System.err.println("Exception when calling DialectApi#translateJiveGet");
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
| **text** | **String**| Text to translate | |

### Return type

null (empty response body)

### Authorization

[X-Funtranslations-Api-Secret](../README.md#X-Funtranslations-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="translateValspeakGet"></a>
# **translateValspeakGet**
> translateValspeakGet(text)



Translate from English to Valley Speak.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DialectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.funtranslations.com");
    
    // Configure API key authorization: X-Funtranslations-Api-Secret
    ApiKeyAuth X-Funtranslations-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Funtranslations-Api-Secret");
    X-Funtranslations-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Funtranslations-Api-Secret.setApiKeyPrefix("Token");

    DialectApi apiInstance = new DialectApi(defaultClient);
    String text = "text_example"; // String | Text to translate
    try {
      apiInstance.translateValspeakGet(text);
    } catch (ApiException e) {
      System.err.println("Exception when calling DialectApi#translateValspeakGet");
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
| **text** | **String**| Text to translate | |

### Return type

null (empty response body)

### Authorization

[X-Funtranslations-Api-Secret](../README.md#X-Funtranslations-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

