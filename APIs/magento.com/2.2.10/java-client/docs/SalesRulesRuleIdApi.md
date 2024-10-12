# SalesRulesRuleIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesRuleRuleRepositoryV1DeleteByIdDelete**](SalesRulesRuleIdApi.md#salesRuleRuleRepositoryV1DeleteByIdDelete) | **DELETE** /V1/salesRules/{ruleId} | salesRules/{ruleId} |
| [**salesRuleRuleRepositoryV1GetByIdGet**](SalesRulesRuleIdApi.md#salesRuleRuleRepositoryV1GetByIdGet) | **GET** /V1/salesRules/{ruleId} | salesRules/{ruleId} |
| [**salesRuleRuleRepositoryV1SavePut**](SalesRulesRuleIdApi.md#salesRuleRuleRepositoryV1SavePut) | **PUT** /V1/salesRules/{ruleId} | salesRules/{ruleId} |


<a id="salesRuleRuleRepositoryV1DeleteByIdDelete"></a>
# **salesRuleRuleRepositoryV1DeleteByIdDelete**
> Boolean salesRuleRuleRepositoryV1DeleteByIdDelete(ruleId)

salesRules/{ruleId}

Delete rule by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesRulesRuleIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    SalesRulesRuleIdApi apiInstance = new SalesRulesRuleIdApi(defaultClient);
    Integer ruleId = 56; // Integer | 
    try {
      Boolean result = apiInstance.salesRuleRuleRepositoryV1DeleteByIdDelete(ruleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesRulesRuleIdApi#salesRuleRuleRepositoryV1DeleteByIdDelete");
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
| **ruleId** | **Integer**|  | |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

<a id="salesRuleRuleRepositoryV1GetByIdGet"></a>
# **salesRuleRuleRepositoryV1GetByIdGet**
> SalesRuleDataRuleInterface salesRuleRuleRepositoryV1GetByIdGet(ruleId)

salesRules/{ruleId}

Get rule by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesRulesRuleIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    SalesRulesRuleIdApi apiInstance = new SalesRulesRuleIdApi(defaultClient);
    Integer ruleId = 56; // Integer | 
    try {
      SalesRuleDataRuleInterface result = apiInstance.salesRuleRuleRepositoryV1GetByIdGet(ruleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesRulesRuleIdApi#salesRuleRuleRepositoryV1GetByIdGet");
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
| **ruleId** | **Integer**|  | |

### Return type

[**SalesRuleDataRuleInterface**](SalesRuleDataRuleInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

<a id="salesRuleRuleRepositoryV1SavePut"></a>
# **salesRuleRuleRepositoryV1SavePut**
> SalesRuleDataRuleInterface salesRuleRuleRepositoryV1SavePut(ruleId, salesRuleRuleRepositoryV1SavePostRequest)

salesRules/{ruleId}

Save sales rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesRulesRuleIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    SalesRulesRuleIdApi apiInstance = new SalesRulesRuleIdApi(defaultClient);
    String ruleId = "ruleId_example"; // String | 
    SalesRuleRuleRepositoryV1SavePostRequest salesRuleRuleRepositoryV1SavePostRequest = new SalesRuleRuleRepositoryV1SavePostRequest(); // SalesRuleRuleRepositoryV1SavePostRequest | 
    try {
      SalesRuleDataRuleInterface result = apiInstance.salesRuleRuleRepositoryV1SavePut(ruleId, salesRuleRuleRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesRulesRuleIdApi#salesRuleRuleRepositoryV1SavePut");
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
| **ruleId** | **String**|  | |
| **salesRuleRuleRepositoryV1SavePostRequest** | [**SalesRuleRuleRepositoryV1SavePostRequest**](SalesRuleRuleRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**SalesRuleDataRuleInterface**](SalesRuleDataRuleInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

