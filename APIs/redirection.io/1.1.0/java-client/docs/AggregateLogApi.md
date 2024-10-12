# AggregateLogApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAggregateLogCollection**](AggregateLogApi.md#getAggregateLogCollection) | **GET** /aggregate-logs | Retrieves the collection of AggregateLog resources. |
| [**getAggregateLogItem**](AggregateLogApi.md#getAggregateLogItem) | **GET** /aggregate-logs/{id} | Retrieves a AggregateLog resource. |


<a id="getAggregateLogCollection"></a>
# **getAggregateLogCollection**
> List&lt;AggregateLogRead&gt; getAggregateLogCollection(page, projectId, createdAt, source, target, statusCode, referrer, userAgent, userAgentType, simplifiedUserAgent, ruleId, instanceName, excludeUrls, excludeEmptyReferrer, createdAtGt, createdAtGte, createdAtLt, createdAtLte, statusCodeGt, statusCodeGte, statusCodeLt, statusCodeLte)

Retrieves the collection of AggregateLog resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AggregateLogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    AggregateLogApi apiInstance = new AggregateLogApi(defaultClient);
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
      List<AggregateLogRead> result = apiInstance.getAggregateLogCollection(page, projectId, createdAt, source, target, statusCode, referrer, userAgent, userAgentType, simplifiedUserAgent, ruleId, instanceName, excludeUrls, excludeEmptyReferrer, createdAtGt, createdAtGte, createdAtLt, createdAtLte, statusCodeGt, statusCodeGte, statusCodeLt, statusCodeLte);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AggregateLogApi#getAggregateLogCollection");
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

[**List&lt;AggregateLogRead&gt;**](AggregateLogRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | AggregateLog collection response |  -  |

<a id="getAggregateLogItem"></a>
# **getAggregateLogItem**
> AggregateLogRead getAggregateLogItem(id)

Retrieves a AggregateLog resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AggregateLogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    AggregateLogApi apiInstance = new AggregateLogApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      AggregateLogRead result = apiInstance.getAggregateLogItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AggregateLogApi#getAggregateLogItem");
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

[**AggregateLogRead**](AggregateLogRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | AggregateLog resource response |  -  |
| **404** | Resource not found |  -  |

