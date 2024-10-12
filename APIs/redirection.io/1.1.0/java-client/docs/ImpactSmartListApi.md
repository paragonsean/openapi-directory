# ImpactSmartListApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getImpactSmartListItem**](ImpactSmartListApi.md#getImpactSmartListItem) | **GET** /impact-smart-lists/{id} | Retrieves a ImpactSmartList resource. |
| [**postImpactSmartListCollection**](ImpactSmartListApi.md#postImpactSmartListCollection) | **POST** /impact-smart-lists | Creates a ImpactSmartList resource. |


<a id="getImpactSmartListItem"></a>
# **getImpactSmartListItem**
> ImpactSmartListRead getImpactSmartListItem(id)

Retrieves a ImpactSmartList resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImpactSmartListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ImpactSmartListApi apiInstance = new ImpactSmartListApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      ImpactSmartListRead result = apiInstance.getImpactSmartListItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImpactSmartListApi#getImpactSmartListItem");
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

[**ImpactSmartListRead**](ImpactSmartListRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ImpactSmartList resource response |  -  |
| **404** | Resource not found |  -  |

<a id="postImpactSmartListCollection"></a>
# **postImpactSmartListCollection**
> ImpactSmartListRead postImpactSmartListCollection(impactSmartList)

Creates a ImpactSmartList resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImpactSmartListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ImpactSmartListApi apiInstance = new ImpactSmartListApi(defaultClient);
    ImpactSmartListWrite impactSmartList = new ImpactSmartListWrite(); // ImpactSmartListWrite | The new ImpactSmartList resource
    try {
      ImpactSmartListRead result = apiInstance.postImpactSmartListCollection(impactSmartList);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImpactSmartListApi#postImpactSmartListCollection");
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
| **impactSmartList** | [**ImpactSmartListWrite**](ImpactSmartListWrite.md)| The new ImpactSmartList resource | [optional] |

### Return type

[**ImpactSmartListRead**](ImpactSmartListRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | ImpactSmartList resource created |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

