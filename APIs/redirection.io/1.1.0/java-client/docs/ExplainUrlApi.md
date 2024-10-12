# ExplainUrlApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getExplainUrlItem**](ExplainUrlApi.md#getExplainUrlItem) | **GET** /explain-urls/{id} | Retrieves a ExplainUrl resource. |
| [**postExplainUrlCollection**](ExplainUrlApi.md#postExplainUrlCollection) | **POST** /explain-urls | Creates a ExplainUrl resource. |


<a id="getExplainUrlItem"></a>
# **getExplainUrlItem**
> ExplainUrl getExplainUrlItem(id)

Retrieves a ExplainUrl resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExplainUrlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ExplainUrlApi apiInstance = new ExplainUrlApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      ExplainUrl result = apiInstance.getExplainUrlItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExplainUrlApi#getExplainUrlItem");
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
| **id** | **String**|  | |

### Return type

[**ExplainUrl**](ExplainUrl.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ExplainUrl resource response |  -  |
| **404** | Resource not found |  -  |

<a id="postExplainUrlCollection"></a>
# **postExplainUrlCollection**
> ExplainUrl postExplainUrlCollection(explainUrl)

Creates a ExplainUrl resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExplainUrlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ExplainUrlApi apiInstance = new ExplainUrlApi(defaultClient);
    ExplainUrlWrite explainUrl = new ExplainUrlWrite(); // ExplainUrlWrite | The new ExplainUrl resource
    try {
      ExplainUrl result = apiInstance.postExplainUrlCollection(explainUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExplainUrlApi#postExplainUrlCollection");
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
| **explainUrl** | [**ExplainUrlWrite**](ExplainUrlWrite.md)| The new ExplainUrl resource | [optional] |

### Return type

[**ExplainUrl**](ExplainUrl.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | ExplainUrl resource created |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

