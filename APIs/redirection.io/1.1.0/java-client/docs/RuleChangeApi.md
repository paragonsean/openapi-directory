# RuleChangeApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteRuleChangeItem**](RuleChangeApi.md#deleteRuleChangeItem) | **DELETE** /rule-changes/{id} | Removes the RuleChange resource. |
| [**getRuleChangeCollection**](RuleChangeApi.md#getRuleChangeCollection) | **GET** /rule-changes | Retrieves the collection of RuleChange resources. |
| [**getRuleChangeItem**](RuleChangeApi.md#getRuleChangeItem) | **GET** /rule-changes/{id} | Retrieves a RuleChange resource. |
| [**postRuleChangeCollection**](RuleChangeApi.md#postRuleChangeCollection) | **POST** /rule-changes | Creates a RuleChange resource. |


<a id="deleteRuleChangeItem"></a>
# **deleteRuleChangeItem**
> deleteRuleChangeItem(id)

Removes the RuleChange resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RuleChangeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    RuleChangeApi apiInstance = new RuleChangeApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.deleteRuleChangeItem(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling RuleChangeApi#deleteRuleChangeItem");
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

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | RuleChange resource deleted |  -  |
| **404** | Resource not found |  -  |

<a id="getRuleChangeCollection"></a>
# **getRuleChangeCollection**
> List&lt;RuleChangeRead&gt; getRuleChangeCollection(versionId, page)

Retrieves the collection of RuleChange resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RuleChangeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    RuleChangeApi apiInstance = new RuleChangeApi(defaultClient);
    String versionId = "versionId_example"; // String | 
    Integer page = 56; // Integer | The collection page number
    try {
      List<RuleChangeRead> result = apiInstance.getRuleChangeCollection(versionId, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RuleChangeApi#getRuleChangeCollection");
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
| **versionId** | **String**|  | |
| **page** | **Integer**| The collection page number | [optional] |

### Return type

[**List&lt;RuleChangeRead&gt;**](RuleChangeRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | RuleChange collection response |  -  |

<a id="getRuleChangeItem"></a>
# **getRuleChangeItem**
> RuleChangeRead getRuleChangeItem(id)

Retrieves a RuleChange resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RuleChangeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    RuleChangeApi apiInstance = new RuleChangeApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      RuleChangeRead result = apiInstance.getRuleChangeItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RuleChangeApi#getRuleChangeItem");
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

[**RuleChangeRead**](RuleChangeRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | RuleChange resource response |  -  |
| **404** | Resource not found |  -  |

<a id="postRuleChangeCollection"></a>
# **postRuleChangeCollection**
> RuleChangeRead postRuleChangeCollection(ruleChange)

Creates a RuleChange resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RuleChangeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    RuleChangeApi apiInstance = new RuleChangeApi(defaultClient);
    RuleChangeWrite ruleChange = new RuleChangeWrite(); // RuleChangeWrite | The new RuleChange resource
    try {
      RuleChangeRead result = apiInstance.postRuleChangeCollection(ruleChange);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RuleChangeApi#postRuleChangeCollection");
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
| **ruleChange** | [**RuleChangeWrite**](RuleChangeWrite.md)| The new RuleChange resource | [optional] |

### Return type

[**RuleChangeRead**](RuleChangeRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | RuleChange resource created |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

