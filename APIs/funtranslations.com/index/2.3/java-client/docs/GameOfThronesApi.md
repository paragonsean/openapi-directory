# GameOfThronesApi

All URIs are relative to *http://api.funtranslations.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**translateDothrakiGet**](GameOfThronesApi.md#translateDothrakiGet) | **GET** /translate/dothraki |  |
| [**translateValyrianGet**](GameOfThronesApi.md#translateValyrianGet) | **GET** /translate/valyrian |  |


<a id="translateDothrakiGet"></a>
# **translateDothrakiGet**
> translateDothrakiGet(text)



Translate from English to Dothraki.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GameOfThronesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.funtranslations.com");
    
    // Configure API key authorization: X-Funtranslations-Api-Secret
    ApiKeyAuth X-Funtranslations-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Funtranslations-Api-Secret");
    X-Funtranslations-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Funtranslations-Api-Secret.setApiKeyPrefix("Token");

    GameOfThronesApi apiInstance = new GameOfThronesApi(defaultClient);
    String text = "text_example"; // String | Text to translate
    try {
      apiInstance.translateDothrakiGet(text);
    } catch (ApiException e) {
      System.err.println("Exception when calling GameOfThronesApi#translateDothrakiGet");
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

<a id="translateValyrianGet"></a>
# **translateValyrianGet**
> translateValyrianGet(text)



Translate from English to Valyrian.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GameOfThronesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.funtranslations.com");
    
    // Configure API key authorization: X-Funtranslations-Api-Secret
    ApiKeyAuth X-Funtranslations-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Funtranslations-Api-Secret");
    X-Funtranslations-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Funtranslations-Api-Secret.setApiKeyPrefix("Token");

    GameOfThronesApi apiInstance = new GameOfThronesApi(defaultClient);
    String text = "text_example"; // String | Text to translate
    try {
      apiInstance.translateValyrianGet(text);
    } catch (ApiException e) {
      System.err.println("Exception when calling GameOfThronesApi#translateValyrianGet");
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

