# MatchingUrlApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMatchingUrlItem**](MatchingUrlApi.md#getMatchingUrlItem) | **GET** /matching-urls/{id} | Retrieves a MatchingUrl resource. |
| [**postMatchingUrlCollection**](MatchingUrlApi.md#postMatchingUrlCollection) | **POST** /matching-urls | Creates a MatchingUrl resource. |


<a id="getMatchingUrlItem"></a>
# **getMatchingUrlItem**
> MatchingUrlRead getMatchingUrlItem(id)

Retrieves a MatchingUrl resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MatchingUrlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    MatchingUrlApi apiInstance = new MatchingUrlApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      MatchingUrlRead result = apiInstance.getMatchingUrlItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MatchingUrlApi#getMatchingUrlItem");
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

[**MatchingUrlRead**](MatchingUrlRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | MatchingUrl resource response |  -  |
| **404** | Resource not found |  -  |

<a id="postMatchingUrlCollection"></a>
# **postMatchingUrlCollection**
> MatchingUrlRead postMatchingUrlCollection(matchingUrl)

Creates a MatchingUrl resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MatchingUrlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    MatchingUrlApi apiInstance = new MatchingUrlApi(defaultClient);
    MatchingUrlWrite matchingUrl = new MatchingUrlWrite(); // MatchingUrlWrite | The new MatchingUrl resource
    try {
      MatchingUrlRead result = apiInstance.postMatchingUrlCollection(matchingUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MatchingUrlApi#postMatchingUrlCollection");
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
| **matchingUrl** | [**MatchingUrlWrite**](MatchingUrlWrite.md)| The new MatchingUrl resource | [optional] |

### Return type

[**MatchingUrlRead**](MatchingUrlRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | MatchingUrl resource created |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

