# PricingRulesApi

All URIs are relative to *http://,*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ruleData**](PricingRulesApi.md#ruleData) | **GET** /api/rule/ruleData/1 | Rule Data |
| [**ruleDataLatest**](PricingRulesApi.md#ruleDataLatest) | **GET** /api/rule/ruleData/1/latest | Rule Data Latest |
| [**rules**](PricingRulesApi.md#rules) | **GET** /api/rule | Rules |


<a id="ruleData"></a>
# **ruleData**
> ruleData()

Rule Data

This resource lists all data that wa saved for pricing rules.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://,");

    PricingRulesApi apiInstance = new PricingRulesApi(defaultClient);
    String  = ""; // String | 
    try {
      apiInstance.ruleData();
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingRulesApi#ruleData");
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
| **** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ruleDataLatest"></a>
# **ruleDataLatest**
> ruleDataLatest()

Rule Data Latest

This resource lists only the latest data point that wa saved for a pricing rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://,");

    PricingRulesApi apiInstance = new PricingRulesApi(defaultClient);
    String  = ""; // String | 
    try {
      apiInstance.ruleDataLatest();
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingRulesApi#ruleDataLatest");
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
| **** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="rules"></a>
# **rules**
> rules()

Rules

This resource lists all pricing rules that are currently saved in you account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://,");

    PricingRulesApi apiInstance = new PricingRulesApi(defaultClient);
    String  = ""; // String | 
    try {
      apiInstance.rules();
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingRulesApi#rules");
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
| **** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

