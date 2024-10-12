# StrategiesApi

All URIs are relative to *http://devui.magick.nu/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getStrategiesStrategyIdStrategyId**](StrategiesApi.md#getStrategiesStrategyIdStrategyId) | **GET** /strategies/strategyId/{strategyId} | Get Strategy by ID |
| [**getStrategiesTemplates**](StrategiesApi.md#getStrategiesTemplates) | **GET** /strategies/templates | Get all Template Strategies |


<a id="getStrategiesStrategyIdStrategyId"></a>
# **getStrategiesStrategyIdStrategyId**
> getStrategiesStrategyIdStrategyId(strategyId)

Get Strategy by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StrategiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://devui.magick.nu/rest");

    StrategiesApi apiInstance = new StrategiesApi(defaultClient);
    String strategyId = "strategyId_example"; // String | 
    try {
      apiInstance.getStrategiesStrategyIdStrategyId(strategyId);
    } catch (ApiException e) {
      System.err.println("Exception when calling StrategiesApi#getStrategiesStrategyIdStrategyId");
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
| **strategyId** | **String**|  | |

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
| **200** | No response was specified |  -  |

<a id="getStrategiesTemplates"></a>
# **getStrategiesTemplates**
> getStrategiesTemplates()

Get all Template Strategies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StrategiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://devui.magick.nu/rest");

    StrategiesApi apiInstance = new StrategiesApi(defaultClient);
    try {
      apiInstance.getStrategiesTemplates();
    } catch (ApiException e) {
      System.err.println("Exception when calling StrategiesApi#getStrategiesTemplates");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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
| **200** | No response was specified |  -  |

