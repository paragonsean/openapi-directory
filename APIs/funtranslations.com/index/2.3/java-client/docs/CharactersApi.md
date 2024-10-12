# CharactersApi

All URIs are relative to *http://api.funtranslations.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**translateChefGet**](CharactersApi.md#translateChefGet) | **GET** /translate/chef |  |
| [**translateDolanGet**](CharactersApi.md#translateDolanGet) | **GET** /translate/dolan |  |
| [**translateFerblatinGet**](CharactersApi.md#translateFerblatinGet) | **GET** /translate/ferblatin |  |
| [**translateFuddGet**](CharactersApi.md#translateFuddGet) | **GET** /translate/fudd |  |
| [**translateMinionGet**](CharactersApi.md#translateMinionGet) | **GET** /translate/minion |  |
| [**translatePirateGet**](CharactersApi.md#translatePirateGet) | **GET** /translate/pirate |  |


<a id="translateChefGet"></a>
# **translateChefGet**
> translateChefGet(text)



Translate from English to Swedish Chef speak.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CharactersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.funtranslations.com");
    
    // Configure API key authorization: X-Funtranslations-Api-Secret
    ApiKeyAuth X-Funtranslations-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Funtranslations-Api-Secret");
    X-Funtranslations-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Funtranslations-Api-Secret.setApiKeyPrefix("Token");

    CharactersApi apiInstance = new CharactersApi(defaultClient);
    String text = "text_example"; // String | Text to translate
    try {
      apiInstance.translateChefGet(text);
    } catch (ApiException e) {
      System.err.println("Exception when calling CharactersApi#translateChefGet");
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

<a id="translateDolanGet"></a>
# **translateDolanGet**
> translateDolanGet(text)



Translate from English to Dolan Speak.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CharactersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.funtranslations.com");
    
    // Configure API key authorization: X-Funtranslations-Api-Secret
    ApiKeyAuth X-Funtranslations-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Funtranslations-Api-Secret");
    X-Funtranslations-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Funtranslations-Api-Secret.setApiKeyPrefix("Token");

    CharactersApi apiInstance = new CharactersApi(defaultClient);
    String text = "text_example"; // String | Text to translate
    try {
      apiInstance.translateDolanGet(text);
    } catch (ApiException e) {
      System.err.println("Exception when calling CharactersApi#translateDolanGet");
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

<a id="translateFerblatinGet"></a>
# **translateFerblatinGet**
> translateFerblatinGet(text)



Translate from English to Ferb Latin.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CharactersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.funtranslations.com");
    
    // Configure API key authorization: X-Funtranslations-Api-Secret
    ApiKeyAuth X-Funtranslations-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Funtranslations-Api-Secret");
    X-Funtranslations-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Funtranslations-Api-Secret.setApiKeyPrefix("Token");

    CharactersApi apiInstance = new CharactersApi(defaultClient);
    String text = "text_example"; // String | Text to translate
    try {
      apiInstance.translateFerblatinGet(text);
    } catch (ApiException e) {
      System.err.println("Exception when calling CharactersApi#translateFerblatinGet");
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

<a id="translateFuddGet"></a>
# **translateFuddGet**
> translateFuddGet(text)



Translate from English to Fudd Speak.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CharactersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.funtranslations.com");
    
    // Configure API key authorization: X-Funtranslations-Api-Secret
    ApiKeyAuth X-Funtranslations-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Funtranslations-Api-Secret");
    X-Funtranslations-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Funtranslations-Api-Secret.setApiKeyPrefix("Token");

    CharactersApi apiInstance = new CharactersApi(defaultClient);
    String text = "text_example"; // String | Text to translate
    try {
      apiInstance.translateFuddGet(text);
    } catch (ApiException e) {
      System.err.println("Exception when calling CharactersApi#translateFuddGet");
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

<a id="translateMinionGet"></a>
# **translateMinionGet**
> translateMinionGet(text)



Translate from English to Minion Speak.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CharactersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.funtranslations.com");
    
    // Configure API key authorization: X-Funtranslations-Api-Secret
    ApiKeyAuth X-Funtranslations-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Funtranslations-Api-Secret");
    X-Funtranslations-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Funtranslations-Api-Secret.setApiKeyPrefix("Token");

    CharactersApi apiInstance = new CharactersApi(defaultClient);
    String text = "text_example"; // String | Text to translate
    try {
      apiInstance.translateMinionGet(text);
    } catch (ApiException e) {
      System.err.println("Exception when calling CharactersApi#translateMinionGet");
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

<a id="translatePirateGet"></a>
# **translatePirateGet**
> translatePirateGet(text)



Translate from English to Pirate Speak.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CharactersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.funtranslations.com");
    
    // Configure API key authorization: X-Funtranslations-Api-Secret
    ApiKeyAuth X-Funtranslations-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Funtranslations-Api-Secret");
    X-Funtranslations-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Funtranslations-Api-Secret.setApiKeyPrefix("Token");

    CharactersApi apiInstance = new CharactersApi(defaultClient);
    String text = "text_example"; // String | Text to translate
    try {
      apiInstance.translatePirateGet(text);
    } catch (ApiException e) {
      System.err.println("Exception when calling CharactersApi#translatePirateGet");
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

