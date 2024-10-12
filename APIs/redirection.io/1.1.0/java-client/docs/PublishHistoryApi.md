# PublishHistoryApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPublishHistoryCollection**](PublishHistoryApi.md#getPublishHistoryCollection) | **GET** /publish-histories | Retrieves the collection of PublishHistory resources. |
| [**getPublishHistoryItem**](PublishHistoryApi.md#getPublishHistoryItem) | **GET** /publish-histories/{id} | Retrieves a PublishHistory resource. |


<a id="getPublishHistoryCollection"></a>
# **getPublishHistoryCollection**
> List&lt;PublishHistoryRead&gt; getPublishHistoryCollection(projectId, createdAtBefore, createdAtStrictlyBefore, createdAtAfter, createdAtStrictlyAfter, page)

Retrieves the collection of PublishHistory resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublishHistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    PublishHistoryApi apiInstance = new PublishHistoryApi(defaultClient);
    String projectId = "projectId_example"; // String | 
    String createdAtBefore = "createdAtBefore_example"; // String | 
    String createdAtStrictlyBefore = "createdAtStrictlyBefore_example"; // String | 
    String createdAtAfter = "createdAtAfter_example"; // String | 
    String createdAtStrictlyAfter = "createdAtStrictlyAfter_example"; // String | 
    Integer page = 56; // Integer | The collection page number
    try {
      List<PublishHistoryRead> result = apiInstance.getPublishHistoryCollection(projectId, createdAtBefore, createdAtStrictlyBefore, createdAtAfter, createdAtStrictlyAfter, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublishHistoryApi#getPublishHistoryCollection");
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
| **projectId** | **String**|  | |
| **createdAtBefore** | **String**|  | [optional] |
| **createdAtStrictlyBefore** | **String**|  | [optional] |
| **createdAtAfter** | **String**|  | [optional] |
| **createdAtStrictlyAfter** | **String**|  | [optional] |
| **page** | **Integer**| The collection page number | [optional] |

### Return type

[**List&lt;PublishHistoryRead&gt;**](PublishHistoryRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | PublishHistory collection response |  -  |

<a id="getPublishHistoryItem"></a>
# **getPublishHistoryItem**
> PublishHistoryRead getPublishHistoryItem(id)

Retrieves a PublishHistory resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublishHistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    PublishHistoryApi apiInstance = new PublishHistoryApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      PublishHistoryRead result = apiInstance.getPublishHistoryItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublishHistoryApi#getPublishHistoryItem");
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

[**PublishHistoryRead**](PublishHistoryRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | PublishHistory resource response |  -  |
| **404** | Resource not found |  -  |

