# KeyPhrasesApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**keyPhrases**](KeyPhrasesApi.md#keyPhrases) | **POST** /keyPhrases | The API returns a list of strings denoting the key talking points in the input text. |


<a id="keyPhrases"></a>
# **keyPhrases**
> KeyPhraseBatchResult keyPhrases(input)

The API returns a list of strings denoting the key talking points in the input text.

See the &lt;a href&#x3D;\&quot;https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/overview#supported-languages\&quot;&gt;Text Analytics Documentation&lt;/a&gt; for details about the languages that are supported by key phrase extraction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyPhrasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    KeyPhrasesApi apiInstance = new KeyPhrasesApi(defaultClient);
    MultiLanguageBatchInput input = new MultiLanguageBatchInput(); // MultiLanguageBatchInput | Collection of documents to analyze. Documents can now contain a language field to indicate the text language
    try {
      KeyPhraseBatchResult result = apiInstance.keyPhrases(input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyPhrasesApi#keyPhrases");
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
| **input** | [**MultiLanguageBatchInput**](MultiLanguageBatchInput.md)| Collection of documents to analyze. Documents can now contain a language field to indicate the text language | |

### Return type

[**KeyPhraseBatchResult**](KeyPhraseBatchResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response results in 0 or more key phrases identified in each valid document |  -  |
| **0** | Error Response |  -  |

