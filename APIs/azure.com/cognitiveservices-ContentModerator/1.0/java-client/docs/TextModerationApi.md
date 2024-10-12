# TextModerationApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**textModerationDetectLanguage**](TextModerationApi.md#textModerationDetectLanguage) | **POST** /contentmoderator/moderate/v1.0/ProcessText/DetectLanguage |  |
| [**textModerationScreenText**](TextModerationApi.md#textModerationScreenText) | **POST** /contentmoderator/moderate/v1.0/ProcessText/Screen/ | Detect profanity and match against custom and shared blacklists |


<a id="textModerationDetectLanguage"></a>
# **textModerationDetectLanguage**
> DetectedLanguage textModerationDetectLanguage(contentType, textContent)



This operation will detect the language of given input content. Returns the &lt;a href&#x3D;\&quot;http://www-01.sil.org/iso639-3/codes.asp\&quot;&gt;ISO 639-3 code&lt;/a&gt; for the predominant language comprising the submitted text. Over 110 languages supported.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    TextModerationApi apiInstance = new TextModerationApi(defaultClient);
    String contentType = "text/plain"; // String | The content type.
    Object textContent = null; // Object | Content to screen.
    try {
      DetectedLanguage result = apiInstance.textModerationDetectLanguage(contentType, textContent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextModerationApi#textModerationDetectLanguage");
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
| **contentType** | **String**| The content type. | [enum: text/plain, text/html, text/xml, text/markdown] |
| **textContent** | **Object**| Content to screen. | |

### Return type

[**DetectedLanguage**](DetectedLanguage.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: text/plain, text/html, text/xml, text/markdown
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The detected language result. |  -  |
| **0** | Error response. |  -  |

<a id="textModerationScreenText"></a>
# **textModerationScreenText**
> Screen textModerationScreenText(contentType, textContent, language, autocorrect, PII, listId, classify)

Detect profanity and match against custom and shared blacklists

Detects profanity in more than 100 languages and match against custom and shared blacklists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    TextModerationApi apiInstance = new TextModerationApi(defaultClient);
    String contentType = "text/plain"; // String | The content type.
    Object textContent = null; // Object | Content to screen.
    String language = "language_example"; // String | Language of the text.
    Boolean autocorrect = false; // Boolean | Autocorrect text.
    Boolean PII = false; // Boolean | Detect personal identifiable information.
    String listId = "listId_example"; // String | The list Id.
    Boolean classify = false; // Boolean | Classify input.
    try {
      Screen result = apiInstance.textModerationScreenText(contentType, textContent, language, autocorrect, PII, listId, classify);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextModerationApi#textModerationScreenText");
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
| **contentType** | **String**| The content type. | [enum: text/plain, text/html, text/xml, text/markdown] |
| **textContent** | **Object**| Content to screen. | |
| **language** | **String**| Language of the text. | [optional] |
| **autocorrect** | **Boolean**| Autocorrect text. | [optional] [default to false] |
| **PII** | **Boolean**| Detect personal identifiable information. | [optional] [default to false] |
| **listId** | **String**| The list Id. | [optional] |
| **classify** | **Boolean**| Classify input. | [optional] [default to false] |

### Return type

[**Screen**](Screen.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: text/plain, text/html, text/xml, text/markdown
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |
| **0** | Error response. |  -  |

