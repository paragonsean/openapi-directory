# SentencesApi

All URIs are relative to *https://randomlovecraft.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSentences**](SentencesApi.md#getSentences) | **GET** /sentences | A random sentence |
| [**getSentencesFromBook**](SentencesApi.md#getSentencesFromBook) | **GET** /books/{id}/sentences | Random sentences from a specific book |
| [**getSpecificSentence**](SentencesApi.md#getSpecificSentence) | **GET** /sentences/{id} | A specific sentence |


<a id="getSentences"></a>
# **getSentences**
> GetSentencesFromBook200Response getSentences(limit)

A random sentence



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SentencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://randomlovecraft.com/api");

    SentencesApi apiInstance = new SentencesApi(defaultClient);
    Integer limit = 1; // Integer | 
    try {
      GetSentencesFromBook200Response result = apiInstance.getSentences(limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SentencesApi#getSentences");
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
| **limit** | **Integer**|  | [optional] [default to 1] |

### Return type

[**GetSentencesFromBook200Response**](GetSentencesFromBook200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getSentencesFromBook"></a>
# **getSentencesFromBook**
> GetSentencesFromBook200Response getSentencesFromBook(id, limit)

Random sentences from a specific book



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SentencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://randomlovecraft.com/api");

    SentencesApi apiInstance = new SentencesApi(defaultClient);
    String id = "id_example"; // String | Book ID
    Integer limit = 1; // Integer | 
    try {
      GetSentencesFromBook200Response result = apiInstance.getSentencesFromBook(id, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SentencesApi#getSentencesFromBook");
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
| **id** | **String**| Book ID | |
| **limit** | **Integer**|  | [optional] [default to 1] |

### Return type

[**GetSentencesFromBook200Response**](GetSentencesFromBook200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getSpecificSentence"></a>
# **getSpecificSentence**
> GetSpecificSentence200Response getSpecificSentence(id)

A specific sentence



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SentencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://randomlovecraft.com/api");

    SentencesApi apiInstance = new SentencesApi(defaultClient);
    String id = "id_example"; // String | Sentence ID
    try {
      GetSpecificSentence200Response result = apiInstance.getSpecificSentence(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SentencesApi#getSpecificSentence");
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
| **id** | **String**| Sentence ID | |

### Return type

[**GetSpecificSentence200Response**](GetSpecificSentence200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

