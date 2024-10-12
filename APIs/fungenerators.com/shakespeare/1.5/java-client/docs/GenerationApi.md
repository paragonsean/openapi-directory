# GenerationApi

All URIs are relative to *http://api.fungenerators.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**shakespeareGenerateInsultGet**](GenerationApi.md#shakespeareGenerateInsultGet) | **GET** /shakespeare/generate/insult |  |
| [**shakespeareGenerateLoremIpsumGet**](GenerationApi.md#shakespeareGenerateLoremIpsumGet) | **GET** /shakespeare/generate/lorem-ipsum |  |
| [**shakespeareGenerateNameGet**](GenerationApi.md#shakespeareGenerateNameGet) | **GET** /shakespeare/generate/name |  |


<a id="shakespeareGenerateInsultGet"></a>
# **shakespeareGenerateInsultGet**
> shakespeareGenerateInsultGet(limit)



Generate random Shakespeare style insults.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GenerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    GenerationApi apiInstance = new GenerationApi(defaultClient);
    Integer limit = 56; // Integer | No of insults to generate
    try {
      apiInstance.shakespeareGenerateInsultGet(limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling GenerationApi#shakespeareGenerateInsultGet");
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
| **limit** | **Integer**| No of insults to generate | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="shakespeareGenerateLoremIpsumGet"></a>
# **shakespeareGenerateLoremIpsumGet**
> shakespeareGenerateLoremIpsumGet(type, limit)



Generate Shakespeare lorem ipsum.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GenerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    GenerationApi apiInstance = new GenerationApi(defaultClient);
    String type = "type_example"; // String | Type of element to generate `paragraphs/sentences/words`.
    Integer limit = 56; // Integer | No of elements to generate
    try {
      apiInstance.shakespeareGenerateLoremIpsumGet(type, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling GenerationApi#shakespeareGenerateLoremIpsumGet");
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
| **type** | **String**| Type of element to generate &#x60;paragraphs/sentences/words&#x60;. | [optional] |
| **limit** | **Integer**| No of elements to generate | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="shakespeareGenerateNameGet"></a>
# **shakespeareGenerateNameGet**
> shakespeareGenerateNameGet(variation, limit)



Generate random Shakespearen names.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GenerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    GenerationApi apiInstance = new GenerationApi(defaultClient);
    String variation = "variation_example"; // String | Variation to generate `male/female`.
    Integer limit = 56; // Integer | No of names to generate
    try {
      apiInstance.shakespeareGenerateNameGet(variation, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling GenerationApi#shakespeareGenerateNameGet");
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
| **variation** | **String**| Variation to generate &#x60;male/female&#x60;. | [optional] |
| **limit** | **Integer**| No of names to generate | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

