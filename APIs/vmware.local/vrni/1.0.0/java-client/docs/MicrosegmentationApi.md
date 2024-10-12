# MicrosegmentationApi

All URIs are relative to *http://vmware.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**exportNsxRecommendedRules**](MicrosegmentationApi.md#exportNsxRecommendedRules) | **POST** /micro-seg/recommended-rules/nsx | Export recommended rules for NSX-V |
| [**listRecommendedRules**](MicrosegmentationApi.md#listRecommendedRules) | **POST** /micro-seg/recommended-rules | Get logical recommended rules |


<a id="exportNsxRecommendedRules"></a>
# **exportNsxRecommendedRules**
> File exportNsxRecommendedRules(recommendedRulesRequest)

Export recommended rules for NSX-V

Export recommended firewall rules based on the flow data gathered by vRealize Network Insight in NSX-V compatible format

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MicrosegmentationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    MicrosegmentationApi apiInstance = new MicrosegmentationApi(defaultClient);
    RecommendedRulesRequest recommendedRulesRequest = new RecommendedRulesRequest(); // RecommendedRulesRequest | NSX Recommended Rules Request
    try {
      File result = apiInstance.exportNsxRecommendedRules(recommendedRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrosegmentationApi#exportNsxRecommendedRules");
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
| **recommendedRulesRequest** | [**RecommendedRulesRequest**](RecommendedRulesRequest.md)| NSX Recommended Rules Request | [optional] |

### Return type

[**File**](File.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="listRecommendedRules"></a>
# **listRecommendedRules**
> RecommendedRules listRecommendedRules(recommendedRulesRequest)

Get logical recommended rules

Get recommended firewall rules based on the flow data gathered by vRealize Network Insight. This API provides service to retrieve recommended rules based on flow traffic that is observed between two groups OR for a single group based on all the inbound and outboud traffic for that group. In case two groups are provided, both the groups should be of same type. Currently supported groups are Application, Tier, NSXSecurityGroup, EC2SecurityGroup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MicrosegmentationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    MicrosegmentationApi apiInstance = new MicrosegmentationApi(defaultClient);
    RecommendedRulesRequest recommendedRulesRequest = new RecommendedRulesRequest(); // RecommendedRulesRequest | Recommended Rules Request
    try {
      RecommendedRules result = apiInstance.listRecommendedRules(recommendedRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrosegmentationApi#listRecommendedRules");
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
| **recommendedRulesRequest** | [**RecommendedRulesRequest**](RecommendedRulesRequest.md)| Recommended Rules Request | [optional] |

### Return type

[**RecommendedRules**](RecommendedRules.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, results, time_range

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

