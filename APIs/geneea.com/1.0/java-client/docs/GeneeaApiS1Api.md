# GeneeaApiS1Api

All URIs are relative to *https://api.geneea.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**correctionGet**](GeneeaApiS1Api.md#correctionGet) | **GET** /s1/correction | Performs text correction (diacritization) on the given document |
| [**correctionPost**](GeneeaApiS1Api.md#correctionPost) | **POST** /s1/correction | Performs text correction (diacritization) on the given document |
| [**entitiesGet**](GeneeaApiS1Api.md#entitiesGet) | **GET** /s1/entities | Performs named-entity recognition on the given document |
| [**entitiesPost**](GeneeaApiS1Api.md#entitiesPost) | **POST** /s1/entities | Performs named-entity recognition on the given document |
| [**lemmatizeGet**](GeneeaApiS1Api.md#lemmatizeGet) | **GET** /s1/lemmatize | Performs lemmatization on the given document |
| [**lemmatizePost**](GeneeaApiS1Api.md#lemmatizePost) | **POST** /s1/lemmatize | Performs lemmatization on the given document |
| [**sentimentGet**](GeneeaApiS1Api.md#sentimentGet) | **GET** /s1/sentiment | Performs sentiment analysis on the given document |
| [**sentimentPost**](GeneeaApiS1Api.md#sentimentPost) | **POST** /s1/sentiment | Performs sentiment analysis on the given document |
| [**topicGet**](GeneeaApiS1Api.md#topicGet) | **GET** /s1/topic | Performs topic detection on the given document |
| [**topicPost**](GeneeaApiS1Api.md#topicPost) | **POST** /s1/topic | Performs topic detection on the given document |


<a id="correctionGet"></a>
# **correctionGet**
> Object correctionGet(id, text, url, extractor, language, returnTextInfo)

Performs text correction (diacritization) on the given document

&lt;br/&gt;&lt;strong&gt;Possible options:&lt;/strong&gt;&lt;p class&#x3D;\&quot;markdown\&quot;&gt;An optional parameter &lt;code&gt;diacritize&lt;/code&gt; with values &lt;code&gt;yes&lt;/code&gt;, &lt;code&gt;no&lt;/code&gt; or &lt;code&gt;auto&lt;/code&gt; indicate whether the text diacritization will be performed. The default value is &lt;code&gt;auto&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneeaApiS1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.geneea.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    GeneeaApiS1Api apiInstance = new GeneeaApiS1Api(defaultClient);
    String id = "id_example"; // String | document ID
    String text = "text_example"; // String | raw document text
    String url = "url_example"; // String | document URL
    String extractor = "default"; // String | document extractor
    String language = "language_example"; // String | document language
    Boolean returnTextInfo = true; // Boolean | 
    try {
      Object result = apiInstance.correctionGet(id, text, url, extractor, language, returnTextInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneeaApiS1Api#correctionGet");
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
| **id** | **String**| document ID | [optional] |
| **text** | **String**| raw document text | [optional] |
| **url** | **String**| document URL | [optional] |
| **extractor** | **String**| document extractor | [optional] [enum: default, article, keep-everything] |
| **language** | **String**| document language | [optional] |
| **returnTextInfo** | **Boolean**|  | [optional] |

### Return type

**Object**

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="correctionPost"></a>
# **correctionPost**
> Object correctionPost(body)

Performs text correction (diacritization) on the given document

&lt;strong&gt;Notes:&lt;/strong&gt;&lt;br/&gt;Valid JSON cannot contain newline characters. These have to be escaped. (See also &lt;a href&#x3D;\&quot;https://geneea.atlassian.net/wiki/display/IPD/The+Interpretor+API+Public+Documentation#TheInterpretorAPIPublicDocumentation-Interactiveonlinedocumentation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Interpretor documentation&lt;/a&gt;)&lt;br/&gt;Fields &lt;code&gt;text&lt;/code&gt; and &lt;code&gt;url&lt;/code&gt; are mutually exclusive.&lt;br/&gt;&lt;strong&gt;Examples:&lt;/strong&gt;&lt;pre&gt;&lt;code&gt;{\&quot;text\&quot;: \&quot;Hello world!\&quot;}&lt;/code&gt;&lt;/pre&gt;&lt;pre&gt;&lt;code&gt;{\&quot;url\&quot;: \&quot;https://en.wikipedia.org/wiki/Pyrrhuloxia\&quot;}&lt;/code&gt;&lt;/pre&gt;&lt;br/&gt;&lt;strong&gt;Possible options:&lt;/strong&gt;&lt;p class&#x3D;\&quot;markdown\&quot;&gt;An optional parameter &lt;code&gt;diacritize&lt;/code&gt; with values &lt;code&gt;yes&lt;/code&gt;, &lt;code&gt;no&lt;/code&gt; or &lt;code&gt;auto&lt;/code&gt; indicate whether the text diacritization will be performed. The default value is &lt;code&gt;auto&lt;/code&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneeaApiS1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.geneea.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    GeneeaApiS1Api apiInstance = new GeneeaApiS1Api(defaultClient);
    Request body = new Request(); // Request | request
    try {
      Object result = apiInstance.correctionPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneeaApiS1Api#correctionPost");
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
| **body** | [**Request**](Request.md)| request | [optional] |

### Return type

**Object**

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Description was not specified |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="entitiesGet"></a>
# **entitiesGet**
> EntitiesResponse entitiesGet(id, text, url, extractor, language, returnTextInfo)

Performs named-entity recognition on the given document

entitiesGet

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneeaApiS1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.geneea.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    GeneeaApiS1Api apiInstance = new GeneeaApiS1Api(defaultClient);
    String id = "id_example"; // String | document ID
    String text = "text_example"; // String | raw document text
    String url = "url_example"; // String | document URL
    String extractor = "default"; // String | document extractor
    String language = "language_example"; // String | document language
    Boolean returnTextInfo = true; // Boolean | 
    try {
      EntitiesResponse result = apiInstance.entitiesGet(id, text, url, extractor, language, returnTextInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneeaApiS1Api#entitiesGet");
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
| **id** | **String**| document ID | [optional] |
| **text** | **String**| raw document text | [optional] |
| **url** | **String**| document URL | [optional] |
| **extractor** | **String**| document extractor | [optional] [enum: default, article, keep-everything] |
| **language** | **String**| document language | [optional] |
| **returnTextInfo** | **Boolean**|  | [optional] |

### Return type

[**EntitiesResponse**](EntitiesResponse.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="entitiesPost"></a>
# **entitiesPost**
> EntitiesResponse entitiesPost(body)

Performs named-entity recognition on the given document

&lt;strong&gt;Notes:&lt;/strong&gt;&lt;br/&gt;Valid JSON cannot contain newline characters. These have to be escaped. (See also &lt;a href&#x3D;\&quot;https://geneea.atlassian.net/wiki/display/IPD/The+Interpretor+API+Public+Documentation#TheInterpretorAPIPublicDocumentation-Interactiveonlinedocumentation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Interpretor documentation&lt;/a&gt;)&lt;br/&gt;Fields &lt;code&gt;text&lt;/code&gt; and &lt;code&gt;url&lt;/code&gt; are mutually exclusive.&lt;br/&gt;&lt;strong&gt;Examples:&lt;/strong&gt;&lt;pre&gt;&lt;code&gt;{\&quot;text\&quot;: \&quot;Hello world!\&quot;}&lt;/code&gt;&lt;/pre&gt;&lt;pre&gt;&lt;code&gt;{\&quot;url\&quot;: \&quot;https://en.wikipedia.org/wiki/Pyrrhuloxia\&quot;}&lt;/code&gt;&lt;/pre&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneeaApiS1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.geneea.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    GeneeaApiS1Api apiInstance = new GeneeaApiS1Api(defaultClient);
    Request body = new Request(); // Request | request
    try {
      EntitiesResponse result = apiInstance.entitiesPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneeaApiS1Api#entitiesPost");
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
| **body** | [**Request**](Request.md)| request | [optional] |

### Return type

[**EntitiesResponse**](EntitiesResponse.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Description was not specified |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="lemmatizeGet"></a>
# **lemmatizeGet**
> LemmatizeResponse lemmatizeGet(id, text, url, extractor, language, returnTextInfo)

Performs lemmatization on the given document

lemmatizeGet

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneeaApiS1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.geneea.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    GeneeaApiS1Api apiInstance = new GeneeaApiS1Api(defaultClient);
    String id = "id_example"; // String | document ID
    String text = "text_example"; // String | raw document text
    String url = "url_example"; // String | document URL
    String extractor = "default"; // String | document extractor
    String language = "language_example"; // String | document language
    Boolean returnTextInfo = true; // Boolean | 
    try {
      LemmatizeResponse result = apiInstance.lemmatizeGet(id, text, url, extractor, language, returnTextInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneeaApiS1Api#lemmatizeGet");
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
| **id** | **String**| document ID | [optional] |
| **text** | **String**| raw document text | [optional] |
| **url** | **String**| document URL | [optional] |
| **extractor** | **String**| document extractor | [optional] [enum: default, article, keep-everything] |
| **language** | **String**| document language | [optional] |
| **returnTextInfo** | **Boolean**|  | [optional] |

### Return type

[**LemmatizeResponse**](LemmatizeResponse.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="lemmatizePost"></a>
# **lemmatizePost**
> LemmatizeResponse lemmatizePost(body)

Performs lemmatization on the given document

&lt;strong&gt;Notes:&lt;/strong&gt;&lt;br/&gt;Valid JSON cannot contain newline characters. These have to be escaped. (See also &lt;a href&#x3D;\&quot;https://geneea.atlassian.net/wiki/display/IPD/The+Interpretor+API+Public+Documentation#TheInterpretorAPIPublicDocumentation-Interactiveonlinedocumentation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Interpretor documentation&lt;/a&gt;)&lt;br/&gt;Fields &lt;code&gt;text&lt;/code&gt; and &lt;code&gt;url&lt;/code&gt; are mutually exclusive.&lt;br/&gt;&lt;strong&gt;Examples:&lt;/strong&gt;&lt;pre&gt;&lt;code&gt;{\&quot;text\&quot;: \&quot;Hello world!\&quot;}&lt;/code&gt;&lt;/pre&gt;&lt;pre&gt;&lt;code&gt;{\&quot;url\&quot;: \&quot;https://en.wikipedia.org/wiki/Pyrrhuloxia\&quot;}&lt;/code&gt;&lt;/pre&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneeaApiS1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.geneea.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    GeneeaApiS1Api apiInstance = new GeneeaApiS1Api(defaultClient);
    Request body = new Request(); // Request | request
    try {
      LemmatizeResponse result = apiInstance.lemmatizePost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneeaApiS1Api#lemmatizePost");
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
| **body** | [**Request**](Request.md)| request | [optional] |

### Return type

[**LemmatizeResponse**](LemmatizeResponse.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Description was not specified |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="sentimentGet"></a>
# **sentimentGet**
> SentimentResponse sentimentGet(id, text, url, extractor, language, returnTextInfo)

Performs sentiment analysis on the given document

sentimentGet

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneeaApiS1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.geneea.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    GeneeaApiS1Api apiInstance = new GeneeaApiS1Api(defaultClient);
    String id = "id_example"; // String | document ID
    String text = "text_example"; // String | raw document text
    String url = "url_example"; // String | document URL
    String extractor = "default"; // String | document extractor
    String language = "language_example"; // String | document language
    Boolean returnTextInfo = true; // Boolean | 
    try {
      SentimentResponse result = apiInstance.sentimentGet(id, text, url, extractor, language, returnTextInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneeaApiS1Api#sentimentGet");
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
| **id** | **String**| document ID | [optional] |
| **text** | **String**| raw document text | [optional] |
| **url** | **String**| document URL | [optional] |
| **extractor** | **String**| document extractor | [optional] [enum: default, article, keep-everything] |
| **language** | **String**| document language | [optional] |
| **returnTextInfo** | **Boolean**|  | [optional] |

### Return type

[**SentimentResponse**](SentimentResponse.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="sentimentPost"></a>
# **sentimentPost**
> SentimentResponse sentimentPost(body)

Performs sentiment analysis on the given document

&lt;strong&gt;Notes:&lt;/strong&gt;&lt;br/&gt;Valid JSON cannot contain newline characters. These have to be escaped. (See also &lt;a href&#x3D;\&quot;https://geneea.atlassian.net/wiki/display/IPD/The+Interpretor+API+Public+Documentation#TheInterpretorAPIPublicDocumentation-Interactiveonlinedocumentation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Interpretor documentation&lt;/a&gt;)&lt;br/&gt;Fields &lt;code&gt;text&lt;/code&gt; and &lt;code&gt;url&lt;/code&gt; are mutually exclusive.&lt;br/&gt;&lt;strong&gt;Examples:&lt;/strong&gt;&lt;pre&gt;&lt;code&gt;{\&quot;text\&quot;: \&quot;Hello world!\&quot;}&lt;/code&gt;&lt;/pre&gt;&lt;pre&gt;&lt;code&gt;{\&quot;url\&quot;: \&quot;https://en.wikipedia.org/wiki/Pyrrhuloxia\&quot;}&lt;/code&gt;&lt;/pre&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneeaApiS1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.geneea.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    GeneeaApiS1Api apiInstance = new GeneeaApiS1Api(defaultClient);
    Request body = new Request(); // Request | request
    try {
      SentimentResponse result = apiInstance.sentimentPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneeaApiS1Api#sentimentPost");
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
| **body** | [**Request**](Request.md)| request | [optional] |

### Return type

[**SentimentResponse**](SentimentResponse.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Description was not specified |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="topicGet"></a>
# **topicGet**
> TopicResponse topicGet(id, text, url, extractor, language, returnTextInfo)

Performs topic detection on the given document

topicGet

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneeaApiS1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.geneea.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    GeneeaApiS1Api apiInstance = new GeneeaApiS1Api(defaultClient);
    String id = "id_example"; // String | document ID
    String text = "text_example"; // String | raw document text
    String url = "url_example"; // String | document URL
    String extractor = "default"; // String | document extractor
    String language = "language_example"; // String | document language
    Boolean returnTextInfo = true; // Boolean | 
    try {
      TopicResponse result = apiInstance.topicGet(id, text, url, extractor, language, returnTextInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneeaApiS1Api#topicGet");
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
| **id** | **String**| document ID | [optional] |
| **text** | **String**| raw document text | [optional] |
| **url** | **String**| document URL | [optional] |
| **extractor** | **String**| document extractor | [optional] [enum: default, article, keep-everything] |
| **language** | **String**| document language | [optional] |
| **returnTextInfo** | **Boolean**|  | [optional] |

### Return type

[**TopicResponse**](TopicResponse.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="topicPost"></a>
# **topicPost**
> TopicResponse topicPost(body)

Performs topic detection on the given document

&lt;strong&gt;Notes:&lt;/strong&gt;&lt;br/&gt;Valid JSON cannot contain newline characters. These have to be escaped. (See also &lt;a href&#x3D;\&quot;https://geneea.atlassian.net/wiki/display/IPD/The+Interpretor+API+Public+Documentation#TheInterpretorAPIPublicDocumentation-Interactiveonlinedocumentation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Interpretor documentation&lt;/a&gt;)&lt;br/&gt;Fields &lt;code&gt;text&lt;/code&gt; and &lt;code&gt;url&lt;/code&gt; are mutually exclusive.&lt;br/&gt;&lt;strong&gt;Examples:&lt;/strong&gt;&lt;pre&gt;&lt;code&gt;{\&quot;text\&quot;: \&quot;Hello world!\&quot;}&lt;/code&gt;&lt;/pre&gt;&lt;pre&gt;&lt;code&gt;{\&quot;url\&quot;: \&quot;https://en.wikipedia.org/wiki/Pyrrhuloxia\&quot;}&lt;/code&gt;&lt;/pre&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneeaApiS1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.geneea.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    GeneeaApiS1Api apiInstance = new GeneeaApiS1Api(defaultClient);
    Request body = new Request(); // Request | request
    try {
      TopicResponse result = apiInstance.topicPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneeaApiS1Api#topicPost");
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
| **body** | [**Request**](Request.md)| request | [optional] |

### Return type

[**TopicResponse**](TopicResponse.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Description was not specified |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

