# RuleApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**agentLegacyComplexRuleCollection**](RuleApi.md#agentLegacyComplexRuleCollection) | **GET** /agent-rule-complexes | Retrieves the collection of Rule resources. |
| [**agentLegacyStraightRuleCollection**](RuleApi.md#agentLegacyStraightRuleCollection) | **GET** /agent-rule-straights | Retrieves the collection of Rule resources. |
| [**agentRuleCollection**](RuleApi.md#agentRuleCollection) | **GET** /agent-rules | Retrieves the collection of Rule resources. |
| [**exportRuleCollection**](RuleApi.md#exportRuleCollection) | **GET** /export-rules | Retrieves the collection of Rule resources. |
| [**getRuleCollection**](RuleApi.md#getRuleCollection) | **GET** /rules | Retrieves the collection of Rule resources. |
| [**getRuleItem**](RuleApi.md#getRuleItem) | **GET** /rules/{id} | Retrieves a Rule resource. |


<a id="agentLegacyComplexRuleCollection"></a>
# **agentLegacyComplexRuleCollection**
> List&lt;RuleRead&gt; agentLegacyComplexRuleCollection(projectId)

Retrieves the collection of Rule resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    RuleApi apiInstance = new RuleApi(defaultClient);
    String projectId = "projectId_example"; // String | 
    try {
      List<RuleRead> result = apiInstance.agentLegacyComplexRuleCollection(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RuleApi#agentLegacyComplexRuleCollection");
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

[**List&lt;RuleRead&gt;**](RuleRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rule collection response |  -  |

<a id="agentLegacyStraightRuleCollection"></a>
# **agentLegacyStraightRuleCollection**
> List&lt;RuleRead&gt; agentLegacyStraightRuleCollection(projectId)

Retrieves the collection of Rule resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    RuleApi apiInstance = new RuleApi(defaultClient);
    String projectId = "projectId_example"; // String | 
    try {
      List<RuleRead> result = apiInstance.agentLegacyStraightRuleCollection(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RuleApi#agentLegacyStraightRuleCollection");
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

[**List&lt;RuleRead&gt;**](RuleRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rule collection response |  -  |

<a id="agentRuleCollection"></a>
# **agentRuleCollection**
> List&lt;RuleRead&gt; agentRuleCollection(projectId)

Retrieves the collection of Rule resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    RuleApi apiInstance = new RuleApi(defaultClient);
    String projectId = "projectId_example"; // String | 
    try {
      List<RuleRead> result = apiInstance.agentRuleCollection(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RuleApi#agentRuleCollection");
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

[**List&lt;RuleRead&gt;**](RuleRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rule collection response |  -  |

<a id="exportRuleCollection"></a>
# **exportRuleCollection**
> List&lt;RuleRead&gt; exportRuleCollection(projectId, sortId, sortViewCount)

Retrieves the collection of Rule resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    RuleApi apiInstance = new RuleApi(defaultClient);
    String projectId = "projectId_example"; // String | 
    String sortId = "sortId_example"; // String | 
    String sortViewCount = "sortViewCount_example"; // String | 
    try {
      List<RuleRead> result = apiInstance.exportRuleCollection(projectId, sortId, sortViewCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RuleApi#exportRuleCollection");
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
| **sortId** | **String**|  | [optional] |
| **sortViewCount** | **String**|  | [optional] |

### Return type

[**List&lt;RuleRead&gt;**](RuleRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rule collection response |  -  |

<a id="getRuleCollection"></a>
# **getRuleCollection**
> List&lt;RuleRead&gt; getRuleCollection(projectId, sortId, sortViewCount, page)

Retrieves the collection of Rule resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    RuleApi apiInstance = new RuleApi(defaultClient);
    String projectId = "projectId_example"; // String | 
    String sortId = "sortId_example"; // String | 
    String sortViewCount = "sortViewCount_example"; // String | 
    Integer page = 56; // Integer | The collection page number
    try {
      List<RuleRead> result = apiInstance.getRuleCollection(projectId, sortId, sortViewCount, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RuleApi#getRuleCollection");
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
| **sortId** | **String**|  | [optional] |
| **sortViewCount** | **String**|  | [optional] |
| **page** | **Integer**| The collection page number | [optional] |

### Return type

[**List&lt;RuleRead&gt;**](RuleRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rule collection response |  -  |

<a id="getRuleItem"></a>
# **getRuleItem**
> RuleRead getRuleItem(id)

Retrieves a Rule resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RuleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    RuleApi apiInstance = new RuleApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      RuleRead result = apiInstance.getRuleItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RuleApi#getRuleItem");
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

[**RuleRead**](RuleRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rule resource response |  -  |
| **404** | Resource not found |  -  |

