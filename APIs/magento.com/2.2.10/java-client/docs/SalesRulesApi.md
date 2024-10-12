# SalesRulesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesRuleRuleRepositoryV1SavePost**](SalesRulesApi.md#salesRuleRuleRepositoryV1SavePost) | **POST** /V1/salesRules | salesRules |


<a id="salesRuleRuleRepositoryV1SavePost"></a>
# **salesRuleRuleRepositoryV1SavePost**
> SalesRuleDataRuleInterface salesRuleRuleRepositoryV1SavePost(salesRuleRuleRepositoryV1SavePostRequest)

salesRules

Save sales rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    SalesRulesApi apiInstance = new SalesRulesApi(defaultClient);
    SalesRuleRuleRepositoryV1SavePostRequest salesRuleRuleRepositoryV1SavePostRequest = new SalesRuleRuleRepositoryV1SavePostRequest(); // SalesRuleRuleRepositoryV1SavePostRequest | 
    try {
      SalesRuleDataRuleInterface result = apiInstance.salesRuleRuleRepositoryV1SavePost(salesRuleRuleRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesRulesApi#salesRuleRuleRepositoryV1SavePost");
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

