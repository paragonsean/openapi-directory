# DocumentClassificationApi

All URIs are relative to *http://api.datumbox.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adultContentDetection**](DocumentClassificationApi.md#adultContentDetection) | **POST** /1.0/AdultContentDetection.json | Classifies the Document as adult or noadult |
| [**commercialDetection**](DocumentClassificationApi.md#commercialDetection) | **POST** /1.0/CommercialDetection.json | Classifies the Document as commercial or nocommercial |
| [**educationalDetection**](DocumentClassificationApi.md#educationalDetection) | **POST** /1.0/EducationalDetection.json | Classifies the Document as educational or noeducational |
| [**genderDetection**](DocumentClassificationApi.md#genderDetection) | **POST** /1.0/GenderDetection.json | Gender Detection Service |
| [**languageDetection**](DocumentClassificationApi.md#languageDetection) | **POST** /1.0/LanguageDetection.json | Identifies the Language of the Document |
| [**readabilityAssessment**](DocumentClassificationApi.md#readabilityAssessment) | **POST** /1.0/ReadabilityAssessment.json | Evaluates the Readability of the Document |
| [**sentimentAnalysis**](DocumentClassificationApi.md#sentimentAnalysis) | **POST** /1.0/SentimentAnalysis.json | Identifies the Sentiment of the Document |
| [**spamDetection**](DocumentClassificationApi.md#spamDetection) | **POST** /1.0/SpamDetection.json | Classifies the Document as spam or nospam |
| [**subjectivityAnalysis**](DocumentClassificationApi.md#subjectivityAnalysis) | **POST** /1.0/SubjectivityAnalysis.json | Classifies Document as Subjective or Objective |
| [**topicClassification**](DocumentClassificationApi.md#topicClassification) | **POST** /1.0/TopicClassification.json | Identifies the Topic of the Document |
| [**twitterSentimentAnalysis**](DocumentClassificationApi.md#twitterSentimentAnalysis) | **POST** /1.0/TwitterSentimentAnalysis.json | Identifies the Sentiment of Twitter Messages |


<a id="adultContentDetection"></a>
# **adultContentDetection**
> adultContentDetection(apiKey, text)

Classifies the Document as adult or noadult

The Adult Content Detection function classifies the documents as adult or noadult based on their context. It can be used to detect whether a document contains content unsuitable for minors.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentClassificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.datumbox.com");

    DocumentClassificationApi apiInstance = new DocumentClassificationApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key
    String text = "text_example"; // String | The text that you want to analyze. It should not contain HTML tags.
    try {
      apiInstance.adultContentDetection(apiKey, text);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentClassificationApi#adultContentDetection");
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
| **apiKey** | **String**| Your API Key | |
| **text** | **String**| The text that you want to analyze. It should not contain HTML tags. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="commercialDetection"></a>
# **commercialDetection**
> commercialDetection(apiKey, text)

Classifies the Document as commercial or nocommercial

The Commercial Detection function labels the documents as commercial or non-commercial based on their keywords and expressions. It can be used to detect whether a website is commercial or not.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentClassificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.datumbox.com");

    DocumentClassificationApi apiInstance = new DocumentClassificationApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key
    String text = "text_example"; // String | The text that you want to analyze. It should not contain HTML tags.
    try {
      apiInstance.commercialDetection(apiKey, text);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentClassificationApi#commercialDetection");
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
| **apiKey** | **String**| Your API Key | |
| **text** | **String**| The text that you want to analyze. It should not contain HTML tags. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="educationalDetection"></a>
# **educationalDetection**
> educationalDetection(apiKey, text)

Classifies the Document as educational or noeducational

The Educational Detection function classifies the documents as educational or non-educational based on their context. It can be used to detect whether a website is educational or not.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentClassificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.datumbox.com");

    DocumentClassificationApi apiInstance = new DocumentClassificationApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key
    String text = "text_example"; // String | The text that you want to analyze. It should not contain HTML tags.
    try {
      apiInstance.educationalDetection(apiKey, text);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentClassificationApi#educationalDetection");
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
| **apiKey** | **String**| Your API Key | |
| **text** | **String**| The text that you want to analyze. It should not contain HTML tags. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="genderDetection"></a>
# **genderDetection**
> genderDetection(apiKey, text)

Gender Detection Service

The Gender Detection function identifies if a particular document is written-by or targets-to a man or a woman based on the context, the words and the idioms found in the text.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentClassificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.datumbox.com");

    DocumentClassificationApi apiInstance = new DocumentClassificationApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key
    String text = "text_example"; // String | The text that you want to analyze. It should not contain HTML tags.
    try {
      apiInstance.genderDetection(apiKey, text);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentClassificationApi#genderDetection");
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
| **apiKey** | **String**| Your API Key | |
| **text** | **String**| The text that you want to analyze. It should not contain HTML tags. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="languageDetection"></a>
# **languageDetection**
> languageDetection(apiKey, text)

Identifies the Language of the Document

The Language Detection function identifies the natural language of the given document based on its words and context. This classifier is able to detect 96 different languages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentClassificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.datumbox.com");

    DocumentClassificationApi apiInstance = new DocumentClassificationApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key
    String text = "text_example"; // String | The text that you want to analyze. It should not contain HTML tags.
    try {
      apiInstance.languageDetection(apiKey, text);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentClassificationApi#languageDetection");
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
| **apiKey** | **String**| Your API Key | |
| **text** | **String**| The text that you want to analyze. It should not contain HTML tags. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="readabilityAssessment"></a>
# **readabilityAssessment**
> readabilityAssessment(apiKey, text)

Evaluates the Readability of the Document

The Readability Assessment function determines the degree of readability of a document based on its terms and idioms. The texts are classified as basic, intermediate and advanced depending their difficulty.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentClassificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.datumbox.com");

    DocumentClassificationApi apiInstance = new DocumentClassificationApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key
    String text = "text_example"; // String | The text that you want to analyze. It should not contain HTML tags.
    try {
      apiInstance.readabilityAssessment(apiKey, text);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentClassificationApi#readabilityAssessment");
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
| **apiKey** | **String**| Your API Key | |
| **text** | **String**| The text that you want to analyze. It should not contain HTML tags. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="sentimentAnalysis"></a>
# **sentimentAnalysis**
> sentimentAnalysis(apiKey, text)

Identifies the Sentiment of the Document

The Sentiment Analysis function classifies documents as positive, negative or neutral (lack of sentiment) depending on whether they express a positive, negative or neutral opinion.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentClassificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.datumbox.com");

    DocumentClassificationApi apiInstance = new DocumentClassificationApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key
    String text = "text_example"; // String | The text that you want to analyze. It should not contain HTML tags.
    try {
      apiInstance.sentimentAnalysis(apiKey, text);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentClassificationApi#sentimentAnalysis");
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
| **apiKey** | **String**| Your API Key | |
| **text** | **String**| The text that you want to analyze. It should not contain HTML tags. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="spamDetection"></a>
# **spamDetection**
> spamDetection(apiKey, text)

Classifies the Document as spam or nospam

The Spam Detection function labels documents as spam or nospam by taking into account their context. It can be used to filter out spam emails and comments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentClassificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.datumbox.com");

    DocumentClassificationApi apiInstance = new DocumentClassificationApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key
    String text = "text_example"; // String | The text that you want to analyze. It should not contain HTML tags.
    try {
      apiInstance.spamDetection(apiKey, text);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentClassificationApi#spamDetection");
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
| **apiKey** | **String**| Your API Key | |
| **text** | **String**| The text that you want to analyze. It should not contain HTML tags. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="subjectivityAnalysis"></a>
# **subjectivityAnalysis**
> subjectivityAnalysis(apiKey, text)

Classifies Document as Subjective or Objective

The Subjectivity Analysis function categorizes documents as subjective or objective based on their writing style. Texts that express personal opinions are labeled as subjective and the others as objective.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentClassificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.datumbox.com");

    DocumentClassificationApi apiInstance = new DocumentClassificationApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key
    String text = "text_example"; // String | The text that you want to analyze. It should not contain HTML tags.
    try {
      apiInstance.subjectivityAnalysis(apiKey, text);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentClassificationApi#subjectivityAnalysis");
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
| **apiKey** | **String**| Your API Key | |
| **text** | **String**| The text that you want to analyze. It should not contain HTML tags. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="topicClassification"></a>
# **topicClassification**
> topicClassification(apiKey, text)

Identifies the Topic of the Document

The Topic Classification function assigns documents in 12 thematic categories based on their keywords, idioms and jargon. It can be used to identify the topic of the texts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentClassificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.datumbox.com");

    DocumentClassificationApi apiInstance = new DocumentClassificationApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key
    String text = "text_example"; // String | The text that you want to analyze. It should not contain HTML tags.
    try {
      apiInstance.topicClassification(apiKey, text);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentClassificationApi#topicClassification");
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
| **apiKey** | **String**| Your API Key | |
| **text** | **String**| The text that you want to analyze. It should not contain HTML tags. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="twitterSentimentAnalysis"></a>
# **twitterSentimentAnalysis**
> twitterSentimentAnalysis(apiKey, text)

Identifies the Sentiment of Twitter Messages

The Twitter Sentiment Analysis function allows you to perform Sentiment Analysis on Twitter. It classifies the tweets as positive, negative or neutral depending on their context.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentClassificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.datumbox.com");

    DocumentClassificationApi apiInstance = new DocumentClassificationApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key
    String text = "text_example"; // String | The text of the tweet that we evaluate.
    try {
      apiInstance.twitterSentimentAnalysis(apiKey, text);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentClassificationApi#twitterSentimentAnalysis");
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
| **apiKey** | **String**| Your API Key | |
| **text** | **String**| The text of the tweet that we evaluate. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

