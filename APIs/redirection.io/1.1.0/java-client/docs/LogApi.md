# LogApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLogCollection**](LogApi.md#getLogCollection) | **GET** /logs | Retrieves the collection of Log resources. |
| [**getLogItem**](LogApi.md#getLogItem) | **GET** /logs/{id} | Retrieves a Log resource. |


<a id="getLogCollection"></a>
# **getLogCollection**
> List&lt;LogRead&gt; getLogCollection(page, projectId, createdAt, source, target, statusCode, referrer, userAgent, userAgentType, simplifiedUserAgent, ruleId, instanceName, excludeUrls, excludeEmptyReferrer, createdAtGt, createdAtGte, createdAtLt, createdAtLte, statusCodeGt, statusCodeGte, statusCodeLt, statusCodeLte)

Retrieves the collection of Log resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    LogApi apiInstance = new LogApi(defaultClient);
    Integer page = 56; // Integer | The collection page number
    String projectId = "projectId_example"; // String | 
    String createdAt = "createdAt_example"; // String | 
    String source = "source_example"; // String | 
    String target = "target_example"; // String | 
    String statusCode = "statusCode_example"; // String | 
    String referrer = "referrer_example"; // String | 
    String userAgent = "userAgent_example"; // String | 
    String userAgentType = "userAgentType_example"; // String | 
    String simplifiedUserAgent = "simplifiedUserAgent_example"; // String | 
    String ruleId = "ruleId_example"; // String | 
    String instanceName = "instanceName_example"; // String | 
    String excludeUrls = "excludeUrls_example"; // String | 
    String excludeEmptyReferrer = "excludeEmptyReferrer_example"; // String | 
    String createdAtGt = "createdAtGt_example"; // String | 
    String createdAtGte = "createdAtGte_example"; // String | 
    String createdAtLt = "createdAtLt_example"; // String | 
    String createdAtLte = "createdAtLte_example"; // String | 
    String statusCodeGt = "statusCodeGt_example"; // String | 
    String statusCodeGte = "statusCodeGte_example"; // String | 
    String statusCodeLt = "statusCodeLt_example"; // String | 
    String statusCodeLte = "statusCodeLte_example"; // String | 
    try {
      List<LogRead> result = apiInstance.getLogCollection(page, projectId, createdAt, source, target, statusCode, referrer, userAgent, userAgentType, simplifiedUserAgent, ruleId, instanceName, excludeUrls, excludeEmptyReferrer, createdAtGt, createdAtGte, createdAtLt, createdAtLte, statusCodeGt, statusCodeGte, statusCodeLt, statusCodeLte);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogApi#getLogCollection");
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
| **page** | **Integer**| The collection page number | [optional] |
| **projectId** | **String**|  | [optional] |
| **createdAt** | **String**|  | [optional] |
| **source** | **String**|  | [optional] |
| **target** | **String**|  | [optional] |
| **statusCode** | **String**|  | [optional] |
| **referrer** | **String**|  | [optional] |
| **userAgent** | **String**|  | [optional] |
| **userAgentType** | **String**|  | [optional] |
| **simplifiedUserAgent** | **String**|  | [optional] |
| **ruleId** | **String**|  | [optional] |
| **instanceName** | **String**|  | [optional] |
| **excludeUrls** | **String**|  | [optional] |
| **excludeEmptyReferrer** | **String**|  | [optional] |
| **createdAtGt** | **String**|  | [optional] |
| **createdAtGte** | **String**|  | [optional] |
| **createdAtLt** | **String**|  | [optional] |
| **createdAtLte** | **String**|  | [optional] |
| **statusCodeGt** | **String**|  | [optional] |
| **statusCodeGte** | **String**|  | [optional] |
| **statusCodeLt** | **String**|  | [optional] |
| **statusCodeLte** | **String**|  | [optional] |

### Return type

[**List&lt;LogRead&gt;**](LogRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Log collection response |  -  |

<a id="getLogItem"></a>
# **getLogItem**
> LogRead getLogItem(id)

Retrieves a Log resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    LogApi apiInstance = new LogApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      LogRead result = apiInstance.getLogItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogApi#getLogItem");
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

[**LogRead**](LogRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Log resource response |  -  |
| **404** | Resource not found |  -  |

