# TaxRulesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**taxTaxRuleRepositoryV1SavePost**](TaxRulesApi.md#taxTaxRuleRepositoryV1SavePost) | **POST** /V1/taxRules | taxRules |
| [**taxTaxRuleRepositoryV1SavePut**](TaxRulesApi.md#taxTaxRuleRepositoryV1SavePut) | **PUT** /V1/taxRules | taxRules |


<a id="taxTaxRuleRepositoryV1SavePost"></a>
# **taxTaxRuleRepositoryV1SavePost**
> TaxDataTaxRuleInterface taxTaxRuleRepositoryV1SavePost(taxTaxRuleRepositoryV1SavePutRequest)

taxRules

Save TaxRule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    TaxRulesApi apiInstance = new TaxRulesApi(defaultClient);
    TaxTaxRuleRepositoryV1SavePutRequest taxTaxRuleRepositoryV1SavePutRequest = new TaxTaxRuleRepositoryV1SavePutRequest(); // TaxTaxRuleRepositoryV1SavePutRequest | 
    try {
      TaxDataTaxRuleInterface result = apiInstance.taxTaxRuleRepositoryV1SavePost(taxTaxRuleRepositoryV1SavePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxRulesApi#taxTaxRuleRepositoryV1SavePost");
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
| **taxTaxRuleRepositoryV1SavePutRequest** | [**TaxTaxRuleRepositoryV1SavePutRequest**](TaxTaxRuleRepositoryV1SavePutRequest.md)|  | [optional] |

### Return type

[**TaxDataTaxRuleInterface**](TaxDataTaxRuleInterface.md)

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

<a id="taxTaxRuleRepositoryV1SavePut"></a>
# **taxTaxRuleRepositoryV1SavePut**
> TaxDataTaxRuleInterface taxTaxRuleRepositoryV1SavePut(taxTaxRuleRepositoryV1SavePutRequest)

taxRules

Save TaxRule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    TaxRulesApi apiInstance = new TaxRulesApi(defaultClient);
    TaxTaxRuleRepositoryV1SavePutRequest taxTaxRuleRepositoryV1SavePutRequest = new TaxTaxRuleRepositoryV1SavePutRequest(); // TaxTaxRuleRepositoryV1SavePutRequest | 
    try {
      TaxDataTaxRuleInterface result = apiInstance.taxTaxRuleRepositoryV1SavePut(taxTaxRuleRepositoryV1SavePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxRulesApi#taxTaxRuleRepositoryV1SavePut");
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
| **taxTaxRuleRepositoryV1SavePutRequest** | [**TaxTaxRuleRepositoryV1SavePutRequest**](TaxTaxRuleRepositoryV1SavePutRequest.md)|  | [optional] |

### Return type

[**TaxDataTaxRuleInterface**](TaxDataTaxRuleInterface.md)

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

