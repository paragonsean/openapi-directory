# RuleSetVersionApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**clearRuleSetVersionItem**](RuleSetVersionApi.md#clearRuleSetVersionItem) | **POST** /rule-set-versions/{id}/clear | Clear a version |
| [**getRuleSetVersionCollection**](RuleSetVersionApi.md#getRuleSetVersionCollection) | **GET** /rule-set-versions | Retrieves the collection of RuleSetVersion resources. |
| [**getRuleSetVersionItem**](RuleSetVersionApi.md#getRuleSetVersionItem) | **GET** /rule-set-versions/{id} | Retrieves a RuleSetVersion resource. |
| [**publishRuleSetVersionItem**](RuleSetVersionApi.md#publishRuleSetVersionItem) | **POST** /rule-set-versions/{id}/publish | Publish a version |


<a id="clearRuleSetVersionItem"></a>
# **clearRuleSetVersionItem**
> RuleSetVersionRead clearRuleSetVersionItem(id, ruleSetVersion)

Clear a version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RuleSetVersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    RuleSetVersionApi apiInstance = new RuleSetVersionApi(defaultClient);
    String id = "id_example"; // String | The id of the version
    RuleSetVersion ruleSetVersion = new RuleSetVersion(); // RuleSetVersion | The new RuleSetVersion resource
    try {
      RuleSetVersionRead result = apiInstance.clearRuleSetVersionItem(id, ruleSetVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RuleSetVersionApi#clearRuleSetVersionItem");
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
| **id** | **String**| The id of the version | |
| **ruleSetVersion** | [**RuleSetVersion**](RuleSetVersion.md)| The new RuleSetVersion resource | |

### Return type

[**RuleSetVersionRead**](RuleSetVersionRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | RuleSetVersion resource created |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

<a id="getRuleSetVersionCollection"></a>
# **getRuleSetVersionCollection**
> List&lt;RuleSetVersionRead&gt; getRuleSetVersionCollection(projectId, sortCreatedAt, page)

Retrieves the collection of RuleSetVersion resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RuleSetVersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    RuleSetVersionApi apiInstance = new RuleSetVersionApi(defaultClient);
    String projectId = "projectId_example"; // String | 
    String sortCreatedAt = "sortCreatedAt_example"; // String | 
    Integer page = 56; // Integer | The collection page number
    try {
      List<RuleSetVersionRead> result = apiInstance.getRuleSetVersionCollection(projectId, sortCreatedAt, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RuleSetVersionApi#getRuleSetVersionCollection");
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
| **sortCreatedAt** | **String**|  | [optional] |
| **page** | **Integer**| The collection page number | [optional] |

### Return type

[**List&lt;RuleSetVersionRead&gt;**](RuleSetVersionRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | RuleSetVersion collection response |  -  |

<a id="getRuleSetVersionItem"></a>
# **getRuleSetVersionItem**
> RuleSetVersionRead getRuleSetVersionItem(id)

Retrieves a RuleSetVersion resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RuleSetVersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    RuleSetVersionApi apiInstance = new RuleSetVersionApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      RuleSetVersionRead result = apiInstance.getRuleSetVersionItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RuleSetVersionApi#getRuleSetVersionItem");
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

[**RuleSetVersionRead**](RuleSetVersionRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | RuleSetVersion resource response |  -  |
| **404** | Resource not found |  -  |

<a id="publishRuleSetVersionItem"></a>
# **publishRuleSetVersionItem**
> RuleSetVersionRead publishRuleSetVersionItem(id, ruleSetVersion)

Publish a version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RuleSetVersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    RuleSetVersionApi apiInstance = new RuleSetVersionApi(defaultClient);
    String id = "id_example"; // String | The id of the version
    RuleSetVersion ruleSetVersion = new RuleSetVersion(); // RuleSetVersion | The new RuleSetVersion resource
    try {
      RuleSetVersionRead result = apiInstance.publishRuleSetVersionItem(id, ruleSetVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RuleSetVersionApi#publishRuleSetVersionItem");
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
| **id** | **String**| The id of the version | |
| **ruleSetVersion** | [**RuleSetVersion**](RuleSetVersion.md)| The new RuleSetVersion resource | |

### Return type

[**RuleSetVersionRead**](RuleSetVersionRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | RuleSetVersion resource created |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

