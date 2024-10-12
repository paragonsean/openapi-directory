# ImpactRuleChangeApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getImpactRuleChangeItem**](ImpactRuleChangeApi.md#getImpactRuleChangeItem) | **GET** /impact-rule-changes/{id} | Retrieves a ImpactRuleChange resource. |
| [**postImpactRuleChangeCollection**](ImpactRuleChangeApi.md#postImpactRuleChangeCollection) | **POST** /impact-rule-changes | Creates a ImpactRuleChange resource. |


<a id="getImpactRuleChangeItem"></a>
# **getImpactRuleChangeItem**
> ImpactRuleChangeRead getImpactRuleChangeItem(id)

Retrieves a ImpactRuleChange resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImpactRuleChangeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ImpactRuleChangeApi apiInstance = new ImpactRuleChangeApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      ImpactRuleChangeRead result = apiInstance.getImpactRuleChangeItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImpactRuleChangeApi#getImpactRuleChangeItem");
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

[**ImpactRuleChangeRead**](ImpactRuleChangeRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ImpactRuleChange resource response |  -  |
| **404** | Resource not found |  -  |

<a id="postImpactRuleChangeCollection"></a>
# **postImpactRuleChangeCollection**
> ImpactRuleChangeRead postImpactRuleChangeCollection(impactRuleChange)

Creates a ImpactRuleChange resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImpactRuleChangeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ImpactRuleChangeApi apiInstance = new ImpactRuleChangeApi(defaultClient);
    ImpactRuleChangeWrite impactRuleChange = new ImpactRuleChangeWrite(); // ImpactRuleChangeWrite | The new ImpactRuleChange resource
    try {
      ImpactRuleChangeRead result = apiInstance.postImpactRuleChangeCollection(impactRuleChange);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImpactRuleChangeApi#postImpactRuleChangeCollection");
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
| **impactRuleChange** | [**ImpactRuleChangeWrite**](ImpactRuleChangeWrite.md)| The new ImpactRuleChange resource | [optional] |

### Return type

[**ImpactRuleChangeRead**](ImpactRuleChangeRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | ImpactRuleChange resource created |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

