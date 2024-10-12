# StarwarsApi

All URIs are relative to *https://api.funtranslations.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**translateCheunhGet**](StarwarsApi.md#translateCheunhGet) | **GET** /translate/cheunh |  |
| [**translateGunganGet**](StarwarsApi.md#translateGunganGet) | **GET** /translate/gungan |  |
| [**translateHutteseGet**](StarwarsApi.md#translateHutteseGet) | **GET** /translate/huttese |  |
| [**translateMandalorianGet**](StarwarsApi.md#translateMandalorianGet) | **GET** /translate/mandalorian |  |
| [**translateSithGet**](StarwarsApi.md#translateSithGet) | **GET** /translate/sith |  |
| [**translateYodaGet**](StarwarsApi.md#translateYodaGet) | **GET** /translate/yoda |  |


<a id="translateCheunhGet"></a>
# **translateCheunhGet**
> translateCheunhGet(text)



Translate from English to Starwars cheunh.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StarwarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.funtranslations.com");
    
    // Configure API key authorization: X-Funtranslations-Api-Secret
    ApiKeyAuth X-Funtranslations-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Funtranslations-Api-Secret");
    X-Funtranslations-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Funtranslations-Api-Secret.setApiKeyPrefix("Token");

    StarwarsApi apiInstance = new StarwarsApi(defaultClient);
    String text = "text_example"; // String | Text to translate
    try {
      apiInstance.translateCheunhGet(text);
    } catch (ApiException e) {
      System.err.println("Exception when calling StarwarsApi#translateCheunhGet");
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

<a id="translateGunganGet"></a>
# **translateGunganGet**
> translateGunganGet(text)



Translate from English to Starwars Gungan Language.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StarwarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.funtranslations.com");
    
    // Configure API key authorization: X-Funtranslations-Api-Secret
    ApiKeyAuth X-Funtranslations-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Funtranslations-Api-Secret");
    X-Funtranslations-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Funtranslations-Api-Secret.setApiKeyPrefix("Token");

    StarwarsApi apiInstance = new StarwarsApi(defaultClient);
    String text = "text_example"; // String | Text to translate
    try {
      apiInstance.translateGunganGet(text);
    } catch (ApiException e) {
      System.err.println("Exception when calling StarwarsApi#translateGunganGet");
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

<a id="translateHutteseGet"></a>
# **translateHutteseGet**
> translateHutteseGet(text)



Translate from English to Starwars Huttese Language.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StarwarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.funtranslations.com");
    
    // Configure API key authorization: X-Funtranslations-Api-Secret
    ApiKeyAuth X-Funtranslations-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Funtranslations-Api-Secret");
    X-Funtranslations-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Funtranslations-Api-Secret.setApiKeyPrefix("Token");

    StarwarsApi apiInstance = new StarwarsApi(defaultClient);
    String text = "text_example"; // String | Text to translate
    try {
      apiInstance.translateHutteseGet(text);
    } catch (ApiException e) {
      System.err.println("Exception when calling StarwarsApi#translateHutteseGet");
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

<a id="translateMandalorianGet"></a>
# **translateMandalorianGet**
> translateMandalorianGet(text)



Translate from English to Starwars Mandalorian Language.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StarwarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.funtranslations.com");
    
    // Configure API key authorization: X-Funtranslations-Api-Secret
    ApiKeyAuth X-Funtranslations-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Funtranslations-Api-Secret");
    X-Funtranslations-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Funtranslations-Api-Secret.setApiKeyPrefix("Token");

    StarwarsApi apiInstance = new StarwarsApi(defaultClient);
    String text = "text_example"; // String | Text to translate
    try {
      apiInstance.translateMandalorianGet(text);
    } catch (ApiException e) {
      System.err.println("Exception when calling StarwarsApi#translateMandalorianGet");
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

<a id="translateSithGet"></a>
# **translateSithGet**
> translateSithGet(text)



Translate from English to Sith Speak.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StarwarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.funtranslations.com");
    
    // Configure API key authorization: X-Funtranslations-Api-Secret
    ApiKeyAuth X-Funtranslations-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Funtranslations-Api-Secret");
    X-Funtranslations-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Funtranslations-Api-Secret.setApiKeyPrefix("Token");

    StarwarsApi apiInstance = new StarwarsApi(defaultClient);
    String text = "text_example"; // String | Text to translate
    try {
      apiInstance.translateSithGet(text);
    } catch (ApiException e) {
      System.err.println("Exception when calling StarwarsApi#translateSithGet");
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

<a id="translateYodaGet"></a>
# **translateYodaGet**
> translateYodaGet(text)



Translate from English to Yoda Speak.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StarwarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.funtranslations.com");
    
    // Configure API key authorization: X-Funtranslations-Api-Secret
    ApiKeyAuth X-Funtranslations-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Funtranslations-Api-Secret");
    X-Funtranslations-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Funtranslations-Api-Secret.setApiKeyPrefix("Token");

    StarwarsApi apiInstance = new StarwarsApi(defaultClient);
    String text = "text_example"; // String | Text to translate
    try {
      apiInstance.translateYodaGet(text);
    } catch (ApiException e) {
      System.err.println("Exception when calling StarwarsApi#translateYodaGet");
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

