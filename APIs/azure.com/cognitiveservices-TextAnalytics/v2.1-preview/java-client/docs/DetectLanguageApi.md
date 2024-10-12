# DetectLanguageApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**detectLanguage**](DetectLanguageApi.md#detectLanguage) | **POST** /languages | The API returns the detected language and a numeric score between 0 and 1. |


<a id="detectLanguage"></a>
# **detectLanguage**
> LanguageBatchResult detectLanguage(input)

The API returns the detected language and a numeric score between 0 and 1.

Scores close to 1 indicate 100% certainty that the identified language is true. A total of 120 languages are supported.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DetectLanguageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DetectLanguageApi apiInstance = new DetectLanguageApi(defaultClient);
    BatchInput input = new BatchInput(); // BatchInput | Collection of documents to analyze.
    try {
      LanguageBatchResult result = apiInstance.detectLanguage(input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DetectLanguageApi#detectLanguage");
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
| **input** | [**BatchInput**](BatchInput.md)| Collection of documents to analyze. | |

### Return type

[**LanguageBatchResult**](LanguageBatchResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful call results in the detected language with the highest probability for each valid document |  -  |
| **0** | Error Response |  -  |

