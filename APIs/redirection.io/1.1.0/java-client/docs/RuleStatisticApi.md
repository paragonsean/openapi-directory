# RuleStatisticApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRuleStatisticCollection**](RuleStatisticApi.md#getRuleStatisticCollection) | **GET** /rule-statistics | Retrieves the collection of RuleStatistic resources. |
| [**getRuleStatisticItem**](RuleStatisticApi.md#getRuleStatisticItem) | **GET** /rule-statistics/{id} | Retrieves a RuleStatistic resource. |


<a id="getRuleStatisticCollection"></a>
# **getRuleStatisticCollection**
> List&lt;RuleStatistic&gt; getRuleStatisticCollection(projectId)

Retrieves the collection of RuleStatistic resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RuleStatisticApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    RuleStatisticApi apiInstance = new RuleStatisticApi(defaultClient);
    String projectId = "projectId_example"; // String | 
    try {
      List<RuleStatistic> result = apiInstance.getRuleStatisticCollection(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RuleStatisticApi#getRuleStatisticCollection");
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

### Return type

[**List&lt;RuleStatistic&gt;**](RuleStatistic.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | RuleStatistic collection response |  -  |

<a id="getRuleStatisticItem"></a>
# **getRuleStatisticItem**
> RuleStatistic getRuleStatisticItem(id)

Retrieves a RuleStatistic resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RuleStatisticApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    RuleStatisticApi apiInstance = new RuleStatisticApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      RuleStatistic result = apiInstance.getRuleStatisticItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RuleStatisticApi#getRuleStatisticItem");
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

[**RuleStatistic**](RuleStatistic.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | RuleStatistic resource response |  -  |
| **404** | Resource not found |  -  |

