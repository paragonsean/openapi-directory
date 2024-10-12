# ImportApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getImportCollection**](ImportApi.md#getImportCollection) | **GET** /imports | Retrieves the collection of Import resources. |
| [**getImportItem**](ImportApi.md#getImportItem) | **GET** /imports/{id} | Retrieves a Import resource. |
| [**postImportCollection**](ImportApi.md#postImportCollection) | **POST** /imports | Creates a Import resource. |


<a id="getImportCollection"></a>
# **getImportCollection**
> List&lt;ImportRead&gt; getImportCollection(projectId, page)

Retrieves the collection of Import resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ImportApi apiInstance = new ImportApi(defaultClient);
    String projectId = "projectId_example"; // String | 
    Integer page = 56; // Integer | The collection page number
    try {
      List<ImportRead> result = apiInstance.getImportCollection(projectId, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportApi#getImportCollection");
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
| **page** | **Integer**| The collection page number | [optional] |

### Return type

[**List&lt;ImportRead&gt;**](ImportRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Import collection response |  -  |

<a id="getImportItem"></a>
# **getImportItem**
> ImportRead getImportItem(id)

Retrieves a Import resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ImportApi apiInstance = new ImportApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      ImportRead result = apiInstance.getImportItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportApi#getImportItem");
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

[**ImportRead**](ImportRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Import resource response |  -  |
| **404** | Resource not found |  -  |

<a id="postImportCollection"></a>
# **postImportCollection**
> ImportRead postImportCollection(_import)

Creates a Import resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ImportApi apiInstance = new ImportApi(defaultClient);
    ImportWrite _import = new ImportWrite(); // ImportWrite | The new Import resource
    try {
      ImportRead result = apiInstance.postImportCollection(_import);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportApi#postImportCollection");
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
| **_import** | [**ImportWrite**](ImportWrite.md)| The new Import resource | [optional] |

### Return type

[**ImportRead**](ImportRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Import resource created |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

