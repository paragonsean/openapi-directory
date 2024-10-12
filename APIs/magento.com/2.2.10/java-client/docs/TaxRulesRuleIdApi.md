# TaxRulesRuleIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**taxTaxRuleRepositoryV1DeleteByIdDelete**](TaxRulesRuleIdApi.md#taxTaxRuleRepositoryV1DeleteByIdDelete) | **DELETE** /V1/taxRules/{ruleId} | taxRules/{ruleId} |
| [**taxTaxRuleRepositoryV1GetGet**](TaxRulesRuleIdApi.md#taxTaxRuleRepositoryV1GetGet) | **GET** /V1/taxRules/{ruleId} | taxRules/{ruleId} |


<a id="taxTaxRuleRepositoryV1DeleteByIdDelete"></a>
# **taxTaxRuleRepositoryV1DeleteByIdDelete**
> Boolean taxTaxRuleRepositoryV1DeleteByIdDelete(ruleId)

taxRules/{ruleId}

Delete TaxRule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxRulesRuleIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    TaxRulesRuleIdApi apiInstance = new TaxRulesRuleIdApi(defaultClient);
    Integer ruleId = 56; // Integer | 
    try {
      Boolean result = apiInstance.taxTaxRuleRepositoryV1DeleteByIdDelete(ruleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxRulesRuleIdApi#taxTaxRuleRepositoryV1DeleteByIdDelete");
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

<a id="taxTaxRuleRepositoryV1GetGet"></a>
# **taxTaxRuleRepositoryV1GetGet**
> TaxDataTaxRuleInterface taxTaxRuleRepositoryV1GetGet(ruleId)

taxRules/{ruleId}

Get TaxRule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxRulesRuleIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    TaxRulesRuleIdApi apiInstance = new TaxRulesRuleIdApi(defaultClient);
    Integer ruleId = 56; // Integer | 
    try {
      TaxDataTaxRuleInterface result = apiInstance.taxTaxRuleRepositoryV1GetGet(ruleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxRulesRuleIdApi#taxTaxRuleRepositoryV1GetGet");
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

[**TaxDataTaxRuleInterface**](TaxDataTaxRuleInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

