# NamesApi

All URIs are relative to *https://api.fungenerators.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**nameCategoriesGet**](NamesApi.md#nameCategoriesGet) | **GET** /name/categories |  |
| [**nameGenerateGet**](NamesApi.md#nameGenerateGet) | **GET** /name/generate |  |


<a id="nameCategoriesGet"></a>
# **nameCategoriesGet**
> nameCategoriesGet(start, limit)



Get available name generation categories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    NamesApi apiInstance = new NamesApi(defaultClient);
    Integer start = 56; // Integer | start
    Integer limit = 56; // Integer | limit
    try {
      apiInstance.nameCategoriesGet(start, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamesApi#nameCategoriesGet");
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
| **start** | **Integer**| start | [optional] |
| **limit** | **Integer**| limit | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="nameGenerateGet"></a>
# **nameGenerateGet**
> nameGenerateGet(category, suggest, start, limit, variation)



Generated names in the given category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    NamesApi apiInstance = new NamesApi(defaultClient);
    String category = "category_example"; // String | Category to generator names from
    String suggest = "suggest_example"; // String | Suggestion string if supported by this category generator.
    Integer start = 56; // Integer | start. Controls pagination. Relevant only if suggestion is supported
    Integer limit = 56; // Integer | limit. Controls pagination limit. Relevant only if suggestion is supported
    String variation = "variation_example"; // String | Variation if supported ( male/female/any )
    try {
      apiInstance.nameGenerateGet(category, suggest, start, limit, variation);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamesApi#nameGenerateGet");
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
| **category** | **String**| Category to generator names from | |
| **suggest** | **String**| Suggestion string if supported by this category generator. | [optional] |
| **start** | **Integer**| start. Controls pagination. Relevant only if suggestion is supported | [optional] |
| **limit** | **Integer**| limit. Controls pagination limit. Relevant only if suggestion is supported | [optional] |
| **variation** | **String**| Variation if supported ( male/female/any ) | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

