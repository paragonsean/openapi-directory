# RestrictedStocksApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**restrictedStocksGetByIdPlanid**](RestrictedStocksApi.md#restrictedStocksGetByIdPlanid) | **GET** /api/RestrictedStocks/{id} | Retrieve a restricted stock |
| [**restrictedStocksGetByPlanid**](RestrictedStocksApi.md#restrictedStocksGetByPlanid) | **GET** /api/RestrictedStocks | Retrieve restricted stocks |


<a id="restrictedStocksGetByIdPlanid"></a>
# **restrictedStocksGetByIdPlanid**
> RestrictedStockModel restrictedStocksGetByIdPlanid(id, planId)

Retrieve a restricted stock

This operation retrieves a restricted stock from the plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RestrictedStocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    RestrictedStocksApi apiInstance = new RestrictedStocksApi(defaultClient);
    Integer id = 56; // Integer | ID of restricted stock to retrieve
    String planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
    try {
      RestrictedStockModel result = apiInstance.restrictedStocksGetByIdPlanid(id, planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RestrictedStocksApi#restrictedStocksGetByIdPlanid");
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
| **id** | **Integer**| ID of restricted stock to retrieve | |
| **planId** | **String**| Id of the plan to retrieve data from (e.g. 1001-11-3). | |

### Return type

[**RestrictedStockModel**](RestrictedStockModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **202** | Plan migration is processing |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized for plan data access |  -  |
| **404** | Object not found |  -  |

<a id="restrictedStocksGetByPlanid"></a>
# **restrictedStocksGetByPlanid**
> RestrictedStocksModel restrictedStocksGetByPlanid(planId)

Retrieve restricted stocks

This operation retrieves a list of all of the restricted stocks in the plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RestrictedStocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    RestrictedStocksApi apiInstance = new RestrictedStocksApi(defaultClient);
    String planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
    try {
      RestrictedStocksModel result = apiInstance.restrictedStocksGetByPlanid(planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RestrictedStocksApi#restrictedStocksGetByPlanid");
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
| **planId** | **String**| Id of the plan to retrieve data from (e.g. 1001-11-3). | |

### Return type

[**RestrictedStocksModel**](RestrictedStocksModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **202** | Plan migration is processing |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized for plan data access |  -  |
| **404** | Object not found |  -  |

