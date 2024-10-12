# TauntApi

All URIs are relative to *https://api.fungenerators.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tauntCategoriesGet**](TauntApi.md#tauntCategoriesGet) | **GET** /taunt/categories |  |
| [**tauntGenerateGet**](TauntApi.md#tauntGenerateGet) | **GET** /taunt/generate |  |


<a id="tauntCategoriesGet"></a>
# **tauntCategoriesGet**
> tauntCategoriesGet(start, limit)



Get available taunt generation categories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TauntApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    TauntApi apiInstance = new TauntApi(defaultClient);
    Integer start = 56; // Integer | start
    Integer limit = 56; // Integer | limit
    try {
      apiInstance.tauntCategoriesGet(start, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling TauntApi#tauntCategoriesGet");
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

<a id="tauntGenerateGet"></a>
# **tauntGenerateGet**
> tauntGenerateGet(category, limit)



Generated taunts in the given category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TauntApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    TauntApi apiInstance = new TauntApi(defaultClient);
    String category = "category_example"; // String | Category to generator taunt from
    Integer limit = 56; // Integer | Limit. Controls number of taunts generated. Max of 5-10 based on the plan
    try {
      apiInstance.tauntGenerateGet(category, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling TauntApi#tauntGenerateGet");
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
| **category** | **String**| Category to generator taunt from | |
| **limit** | **Integer**| Limit. Controls number of taunts generated. Max of 5-10 based on the plan | [optional] |

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

