# DefaultApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**entitiesLinking**](DefaultApi.md#entitiesLinking) | **POST** /entities/linking | Linked entities from a well-known knowledge base |
| [**entitiesRecognitionGeneral**](DefaultApi.md#entitiesRecognitionGeneral) | **POST** /entities/recognition/general | Named Entity Recognition |
| [**entitiesRecognitionPii**](DefaultApi.md#entitiesRecognitionPii) | **POST** /entities/recognition/pii | Entities containing personal information |
| [**keyPhrases**](DefaultApi.md#keyPhrases) | **POST** /keyPhrases | Key Phrases |
| [**languages**](DefaultApi.md#languages) | **POST** /languages | Detect Language |
| [**sentiment**](DefaultApi.md#sentiment) | **POST** /sentiment | Sentiment |


<a id="entitiesLinking"></a>
# **entitiesLinking**
> EntityLinkingResult entitiesLinking(input, modelVersion, showStats)

Linked entities from a well-known knowledge base

The API returns a list of recognized entities with links to a well-known knowledge base. See the &lt;a href&#x3D;\&quot;https://aka.ms/talangs\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    MultiLanguageBatchInput input = new MultiLanguageBatchInput(); // MultiLanguageBatchInput | Collection of documents to analyze.
    String modelVersion = "modelVersion_example"; // String | (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version. 
    Boolean showStats = true; // Boolean | (Optional) if set to true, response will contain input and document level statistics.
    try {
      EntityLinkingResult result = apiInstance.entitiesLinking(input, modelVersion, showStats);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#entitiesLinking");
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
| **input** | [**MultiLanguageBatchInput**](MultiLanguageBatchInput.md)| Collection of documents to analyze. | |
| **modelVersion** | **String**| (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version.  | [optional] |
| **showStats** | **Boolean**| (Optional) if set to true, response will contain input and document level statistics. | [optional] |

### Return type

[**EntityLinkingResult**](EntityLinkingResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful call results in a list of recognized entities with links to a well-known knowledge base returned for each valid document |  -  |
| **0** | Error Response |  -  |

<a id="entitiesRecognitionGeneral"></a>
# **entitiesRecognitionGeneral**
> EntitiesResult entitiesRecognitionGeneral(input, modelVersion, showStats)

Named Entity Recognition

The API returns a list of general named entities in a given document. For the list of supported entity types, check &lt;a href&#x3D;\&quot;https://aka.ms/taner\&quot;&gt;Supported Entity Types in Text Analytics API&lt;/a&gt;. See the &lt;a href&#x3D;\&quot;https://aka.ms/talangs\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    MultiLanguageBatchInput input = new MultiLanguageBatchInput(); // MultiLanguageBatchInput | Collection of documents to analyze.
    String modelVersion = "modelVersion_example"; // String | (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version. 
    Boolean showStats = true; // Boolean | (Optional) if set to true, response will contain input and document level statistics.
    try {
      EntitiesResult result = apiInstance.entitiesRecognitionGeneral(input, modelVersion, showStats);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#entitiesRecognitionGeneral");
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
| **input** | [**MultiLanguageBatchInput**](MultiLanguageBatchInput.md)| Collection of documents to analyze. | |
| **modelVersion** | **String**| (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version.  | [optional] |
| **showStats** | **Boolean**| (Optional) if set to true, response will contain input and document level statistics. | [optional] |

### Return type

[**EntitiesResult**](EntitiesResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful call results in a list of recognized entities returned for each valid document. |  -  |
| **0** | Error Response |  -  |

<a id="entitiesRecognitionPii"></a>
# **entitiesRecognitionPii**
> EntitiesResult entitiesRecognitionPii(input, modelVersion, showStats)

Entities containing personal information

The API returns a list of entities with personal information (\\\&quot;SSN\\\&quot;, \\\&quot;Bank Account\\\&quot; etc) in the document. For the list of supported entity types, check &lt;a href&#x3D;\&quot;https://aka.ms/tanerpii\&quot;&gt;Supported Entity Types in Text Analytics API&lt;/a&gt;. See the &lt;a href&#x3D;\&quot;https://aka.ms/talangs\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    MultiLanguageBatchInput input = new MultiLanguageBatchInput(); // MultiLanguageBatchInput | Collection of documents to analyze.
    String modelVersion = "modelVersion_example"; // String | (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version. 
    Boolean showStats = true; // Boolean | (Optional) if set to true, response will contain input and document level statistics.
    try {
      EntitiesResult result = apiInstance.entitiesRecognitionPii(input, modelVersion, showStats);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#entitiesRecognitionPii");
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
| **input** | [**MultiLanguageBatchInput**](MultiLanguageBatchInput.md)| Collection of documents to analyze. | |
| **modelVersion** | **String**| (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version.  | [optional] |
| **showStats** | **Boolean**| (Optional) if set to true, response will contain input and document level statistics. | [optional] |

### Return type

[**EntitiesResult**](EntitiesResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful call results in a list of entities containing personal information returned for each valid document |  -  |
| **0** | Error Response |  -  |

<a id="keyPhrases"></a>
# **keyPhrases**
> KeyPhraseResult keyPhrases(input, modelVersion, showStats)

Key Phrases

The API returns a list of strings denoting the key phrases in the input text. See the &lt;a href&#x3D;\&quot;https://aka.ms/talangs\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    MultiLanguageBatchInput input = new MultiLanguageBatchInput(); // MultiLanguageBatchInput | Collection of documents to analyze. Documents can now contain a language field to indicate the text language
    String modelVersion = "modelVersion_example"; // String | (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version. 
    Boolean showStats = true; // Boolean | (Optional) if set to true, response will contain input and document level statistics.
    try {
      KeyPhraseResult result = apiInstance.keyPhrases(input, modelVersion, showStats);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#keyPhrases");
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
| **modelVersion** | **String**| (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version.  | [optional] |
| **showStats** | **Boolean**| (Optional) if set to true, response will contain input and document level statistics. | [optional] |

### Return type

[**KeyPhraseResult**](KeyPhraseResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response results in 0 or more key phrases identified in each valid document |  -  |
| **0** | Error Response |  -  |

<a id="languages"></a>
# **languages**
> LanguageResult languages(input, modelVersion, showStats)

Detect Language

The API returns the detected language and a numeric score between 0 and 1. Scores close to 1 indicate 100% certainty that the identified language is true. See the &lt;a href&#x3D;\&quot;https://aka.ms/talangs\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    LanguageBatchInput input = new LanguageBatchInput(); // LanguageBatchInput | Collection of documents to analyze.
    String modelVersion = "modelVersion_example"; // String | (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version. 
    Boolean showStats = true; // Boolean | (Optional) if set to true, response will contain input and document level statistics.
    try {
      LanguageResult result = apiInstance.languages(input, modelVersion, showStats);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#languages");
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
| **input** | [**LanguageBatchInput**](LanguageBatchInput.md)| Collection of documents to analyze. | |
| **modelVersion** | **String**| (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version.  | [optional] |
| **showStats** | **Boolean**| (Optional) if set to true, response will contain input and document level statistics. | [optional] |

### Return type

[**LanguageResult**](LanguageResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful call results in the detected language with the highest probability for each valid document |  -  |
| **0** | Error Response |  -  |

<a id="sentiment"></a>
# **sentiment**
> SentimentResponse sentiment(input, modelVersion, showStats)

Sentiment

The API returns a sentiment prediction, as well as sentiment scores for each sentiment class (Positive, Negative, and Neutral) for the document and each sentence within it. See the &lt;a href&#x3D;\&quot;https://aka.ms/talangs\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    MultiLanguageBatchInput input = new MultiLanguageBatchInput(); // MultiLanguageBatchInput | Collection of documents to analyze.
    String modelVersion = "modelVersion_example"; // String | (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version. 
    Boolean showStats = true; // Boolean | (Optional) if set to true, response will contain input and document level statistics.
    try {
      SentimentResponse result = apiInstance.sentiment(input, modelVersion, showStats);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sentiment");
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
| **input** | [**MultiLanguageBatchInput**](MultiLanguageBatchInput.md)| Collection of documents to analyze. | |
| **modelVersion** | **String**| (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version.  | [optional] |
| **showStats** | **Boolean**| (Optional) if set to true, response will contain input and document level statistics. | [optional] |

### Return type

[**SentimentResponse**](SentimentResponse.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful call results in a document sentiment prediction, as well as sentiment scores for each sentiment class (Positive, Negative, and Neutral) |  -  |
| **0** | Error Response |  -  |

