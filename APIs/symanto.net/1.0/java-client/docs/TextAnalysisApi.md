# TextAnalysisApi

All URIs are relative to *https://api.symanto.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**communication**](TextAnalysisApi.md#communication) | **POST** /communication | Communication &amp; Tonality |
| [**ekmanEmotion**](TextAnalysisApi.md#ekmanEmotion) | **POST** /ekman-emotion | Emotion Analysis |
| [**emotion**](TextAnalysisApi.md#emotion) | **POST** /emotion | Emotion Analysis |
| [**languageDetection**](TextAnalysisApi.md#languageDetection) | **POST** /language-detection | Language Detection |
| [**personality**](TextAnalysisApi.md#personality) | **POST** /personality | Personality Traits |
| [**sentiment**](TextAnalysisApi.md#sentiment) | **POST** /sentiment | Sentiment Analysis |
| [**topicSentiment**](TextAnalysisApi.md#topicSentiment) | **POST** /topic-sentiment | Extracts topics and sentiments and relates them. |


<a id="communication"></a>
# **communication**
> List&lt;PostPredicted&gt; communication(all, post)

Communication &amp; Tonality

Identify the purpose and writing style of a written text.  Supported Languages: [&#x60;ar&#x60;, &#x60;de&#x60;, &#x60;en&#x60;, &#x60;es&#x60;, &#x60;fr&#x60;, &#x60;it&#x60;, &#x60;nl&#x60;, &#x60;pt&#x60;, &#x60;ru&#x60;, &#x60;tr&#x60;, &#x60;zh&#x60;]  Returned labels: * action-seeking * fact-oriented * information-seeking * self-revealing

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextAnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.symanto.net");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    TextAnalysisApi apiInstance = new TextAnalysisApi(defaultClient);
    Boolean all = false; // Boolean | 
    List<Post> post = Arrays.asList(); // List<Post> | 
    try {
      List<PostPredicted> result = apiInstance.communication(all, post);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextAnalysisApi#communication");
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
| **all** | **Boolean**|  | [optional] [default to false] |
| **post** | [**List&lt;Post&gt;**](Post.md)|  | [optional] |

### Return type

[**List&lt;PostPredicted&gt;**](PostPredicted.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="ekmanEmotion"></a>
# **ekmanEmotion**
> List&lt;PostPredicted&gt; ekmanEmotion(all, post)

Emotion Analysis

Detect the emotions of the text based on Ekman.  Supported Langauges: [&#x60;en&#x60;, &#x60;de&#x60;, &#x60;es&#x60;]  Returned labels: * anger * disgust * fear * joy * sadness * surprise * no-emotion

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextAnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.symanto.net");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    TextAnalysisApi apiInstance = new TextAnalysisApi(defaultClient);
    Boolean all = false; // Boolean | 
    List<Post> post = Arrays.asList(); // List<Post> | 
    try {
      List<PostPredicted> result = apiInstance.ekmanEmotion(all, post);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextAnalysisApi#ekmanEmotion");
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
| **all** | **Boolean**|  | [optional] [default to false] |
| **post** | [**List&lt;Post&gt;**](Post.md)|  | [optional] |

### Return type

[**List&lt;PostPredicted&gt;**](PostPredicted.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="emotion"></a>
# **emotion**
> List&lt;PostPredicted&gt; emotion(all, post)

Emotion Analysis

Detect the emotions of the text.  Supported Langauges: [&#x60;en&#x60;, &#x60;de&#x60;, &#x60;es&#x60;]  Returned labels: * anger * joy * love * sadness * surprise * uncategorized

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextAnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.symanto.net");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    TextAnalysisApi apiInstance = new TextAnalysisApi(defaultClient);
    Boolean all = false; // Boolean | 
    List<Post> post = Arrays.asList(); // List<Post> | 
    try {
      List<PostPredicted> result = apiInstance.emotion(all, post);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextAnalysisApi#emotion");
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
| **all** | **Boolean**|  | [optional] [default to false] |
| **post** | [**List&lt;Post&gt;**](Post.md)|  | [optional] |

### Return type

[**List&lt;PostPredicted&gt;**](PostPredicted.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="languageDetection"></a>
# **languageDetection**
> List&lt;LanguagePredicted&gt; languageDetection(languageDetection)

Language Detection

Identifies what language a text is written in. Only languages that our API supports can be analyzed.  Returned labels: * language_code of the detected language

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextAnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.symanto.net");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    TextAnalysisApi apiInstance = new TextAnalysisApi(defaultClient);
    List<LanguageDetection> languageDetection = Arrays.asList(); // List<LanguageDetection> | 
    try {
      List<LanguagePredicted> result = apiInstance.languageDetection(languageDetection);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextAnalysisApi#languageDetection");
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
| **languageDetection** | [**List&lt;LanguageDetection&gt;**](LanguageDetection.md)|  | [optional] |

### Return type

[**List&lt;LanguagePredicted&gt;**](LanguagePredicted.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="personality"></a>
# **personality**
> List&lt;PostPredicted&gt; personality(all, post)

Personality Traits

Predict the personality trait of author of any written text.  Supported Languages: [&#x60;ar&#x60;, &#x60;de&#x60;, &#x60;en&#x60;, &#x60;es&#x60;, &#x60;fr&#x60;, &#x60;it&#x60;, &#x60;nl&#x60;, &#x60;pt&#x60;, &#x60;ru&#x60;, &#x60;tr&#x60;, &#x60;zh&#x60;]  Returned labels:  * emotional * rational

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextAnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.symanto.net");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    TextAnalysisApi apiInstance = new TextAnalysisApi(defaultClient);
    Boolean all = false; // Boolean | 
    List<Post> post = Arrays.asList(); // List<Post> | 
    try {
      List<PostPredicted> result = apiInstance.personality(all, post);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextAnalysisApi#personality");
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
| **all** | **Boolean**|  | [optional] [default to false] |
| **post** | [**List&lt;Post&gt;**](Post.md)|  | [optional] |

### Return type

[**List&lt;PostPredicted&gt;**](PostPredicted.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="sentiment"></a>
# **sentiment**
> List&lt;PostPredicted&gt; sentiment(all, post)

Sentiment Analysis

Evaluate the overall tonality of the text.  Supported Languages: [&#x60;en&#x60;, &#x60;de&#x60;, &#x60;es&#x60;]  Returned labels: * positive * negative

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextAnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.symanto.net");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    TextAnalysisApi apiInstance = new TextAnalysisApi(defaultClient);
    Boolean all = false; // Boolean | 
    List<Post> post = Arrays.asList(); // List<Post> | 
    try {
      List<PostPredicted> result = apiInstance.sentiment(all, post);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextAnalysisApi#sentiment");
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
| **all** | **Boolean**|  | [optional] [default to false] |
| **post** | [**List&lt;Post&gt;**](Post.md)|  | [optional] |

### Return type

[**List&lt;PostPredicted&gt;**](PostPredicted.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="topicSentiment"></a>
# **topicSentiment**
> List&lt;TopicSentimentOutput&gt; topicSentiment(domain, post)

Extracts topics and sentiments and relates them.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextAnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.symanto.net");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    TextAnalysisApi apiInstance = new TextAnalysisApi(defaultClient);
    String domain = "Ecom"; // String | Provide analysis domain for better extraction (optional)
    List<Post> post = Arrays.asList(); // List<Post> | 
    try {
      List<TopicSentimentOutput> result = apiInstance.topicSentiment(domain, post);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextAnalysisApi#topicSentiment");
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
| **domain** | **String**| Provide analysis domain for better extraction (optional) | [optional] [enum: Ecom, Employee, Hotel, Restaurant] |
| **post** | [**List&lt;Post&gt;**](Post.md)|  | [optional] |

### Return type

[**List&lt;TopicSentimentOutput&gt;**](TopicSentimentOutput.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

