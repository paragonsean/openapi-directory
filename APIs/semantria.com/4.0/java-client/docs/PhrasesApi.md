# PhrasesApi

All URIs are relative to *https://api.semantria.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addPhrases**](PhrasesApi.md#addPhrases) | **POST** /phrases.{content_type} | Add sentiment-bearing phrases |
| [**deletePhrases**](PhrasesApi.md#deletePhrases) | **DELETE** /phrases.{content_type} | Remove sentiment-bearing phrases |
| [**getPhrases**](PhrasesApi.md#getPhrases) | **GET** /phrases.{content_type} | Retrieve sentiment-bearing phrases |
| [**updatePhrases**](PhrasesApi.md#updatePhrases) | **PUT** /phrases.{content_type} | Updates sentiment-bearing phrases |


<a id="addPhrases"></a>
# **addPhrases**
> List&lt;PhraseResponseVersion&gt; addPhrases(contentType, sentimentPhrases, configId)

Add sentiment-bearing phrases

This method adds sentiment-bearing phrases on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PhrasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    PhrasesApi apiInstance = new PhrasesApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    Object sentimentPhrases = null; // Object | List of parametrized JSON or XML objects.
    String configId = "configId_example"; // String | Identifier of configuration phrases linked to.
    try {
      List<PhraseResponseVersion> result = apiInstance.addPhrases(contentType, sentimentPhrases, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PhrasesApi#addPhrases");
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
| **contentType** | **String**|  | |
| **sentimentPhrases** | **Object**| List of parametrized JSON or XML objects. | |
| **configId** | **String**| Identifier of configuration phrases linked to. | [optional] |

### Return type

[**List&lt;PhraseResponseVersion&gt;**](PhraseResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **202** | Client request accepted and queued. |  -  |
| **400** | Incoming request body is incorrect. Server responds with details. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **406** | Number of allowed sentiment-bearing phrases per configuration achieved. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="deletePhrases"></a>
# **deletePhrases**
> deletePhrases(contentType, sentimentPhraseIDs, configId)

Remove sentiment-bearing phrases

This method removes certain sentiment-bearing phrases by their names on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PhrasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    PhrasesApi apiInstance = new PhrasesApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    List<String> sentimentPhraseIDs = Arrays.asList(); // List<String> | List of sentiment-bearing phrase identifiers.
    String configId = "configId_example"; // String | Identifier of configuration phrases linked to.
    try {
      apiInstance.deletePhrases(contentType, sentimentPhraseIDs, configId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PhrasesApi#deletePhrases");
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
| **contentType** | **String**|  | |
| **sentimentPhraseIDs** | [**List&lt;String&gt;**](String.md)| List of sentiment-bearing phrase identifiers. | |
| **configId** | **String**| Identifier of configuration phrases linked to. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **202** | Client request accepted and queued. |  -  |
| **400** | Incoming request body is incorrect. Server responds with details. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **403** | Forbidden. Server responds if client tries to remove primary configuration. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="getPhrases"></a>
# **getPhrases**
> List&lt;PhraseResponseVersion&gt; getPhrases(contentType, configId)

Retrieve sentiment-bearing phrases

This method retrieves list of sentiment-bearing phrases available on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PhrasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    PhrasesApi apiInstance = new PhrasesApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    String configId = "configId_example"; // String | Identifier of configuration phrases linked to.
    try {
      List<PhraseResponseVersion> result = apiInstance.getPhrases(contentType, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PhrasesApi#getPhrases");
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
| **contentType** | **String**|  | |
| **configId** | **String**| Identifier of configuration phrases linked to. | [optional] |

### Return type

[**List&lt;PhraseResponseVersion&gt;**](PhraseResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Client request accepted and queued. Server responds with the sentiment-bearing phrases list. |  -  |
| **202** | Client request accepted and no sentiment-bearing phrases found. Server responds with empty body. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="updatePhrases"></a>
# **updatePhrases**
> List&lt;PhraseResponseVersion&gt; updatePhrases(contentType, sentimentPhrases, configId)

Updates sentiment-bearing phrases

This method updates sentiment-bearing phrases by unique IDs on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PhrasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    PhrasesApi apiInstance = new PhrasesApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    Object sentimentPhrases = null; // Object | List of parametrized JSON or XML objects.
    String configId = "configId_example"; // String | Identifier of configuration phrases linked to.
    try {
      List<PhraseResponseVersion> result = apiInstance.updatePhrases(contentType, sentimentPhrases, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PhrasesApi#updatePhrases");
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
| **contentType** | **String**|  | |
| **sentimentPhrases** | **Object**| List of parametrized JSON or XML objects. | |
| **configId** | **String**| Identifier of configuration phrases linked to. | [optional] |

### Return type

[**List&lt;PhraseResponseVersion&gt;**](PhraseResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **202** | Client request accepted and queued. |  -  |
| **400** | Incoming request body is incorrect. Server responds with details. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **406** | Number of allowed sentiment-bearing phrases per configuration achieved. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

