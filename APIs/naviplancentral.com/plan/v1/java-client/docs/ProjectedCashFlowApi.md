# ProjectedCashFlowApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**projectedCashFlowGetByIdPlanid**](ProjectedCashFlowApi.md#projectedCashFlowGetByIdPlanid) | **GET** /api/ProjectedCashFlow/{id} | Retrieve projected cash flow by id |
| [**projectedCashFlowGetByPlanid**](ProjectedCashFlowApi.md#projectedCashFlowGetByPlanid) | **GET** /api/ProjectedCashFlow | Retrieve projected cash flow |


<a id="projectedCashFlowGetByIdPlanid"></a>
# **projectedCashFlowGetByIdPlanid**
> CashFlowProjectionModel projectedCashFlowGetByIdPlanid(id, planId)

Retrieve projected cash flow by id

This operation retrieves an object containing cash flow information                 for a single specified year of the projected plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectedCashFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    ProjectedCashFlowApi apiInstance = new ProjectedCashFlowApi(defaultClient);
    Integer id = 56; // Integer | Index into the list of annual projections
    String planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
    try {
      CashFlowProjectionModel result = apiInstance.projectedCashFlowGetByIdPlanid(id, planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectedCashFlowApi#projectedCashFlowGetByIdPlanid");
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
| **id** | **Integer**| Index into the list of annual projections | |
| **planId** | **String**| Id of the plan to retrieve data from (e.g. 1001-11-3). | |

### Return type

[**CashFlowProjectionModel**](CashFlowProjectionModel.md)

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

<a id="projectedCashFlowGetByPlanid"></a>
# **projectedCashFlowGetByPlanid**
> CashFlowProjectionsModel projectedCashFlowGetByPlanid(planId)

Retrieve projected cash flow

This operation retrieves an object containing cash flow information                 for each year of the projected plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectedCashFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    ProjectedCashFlowApi apiInstance = new ProjectedCashFlowApi(defaultClient);
    String planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
    try {
      CashFlowProjectionsModel result = apiInstance.projectedCashFlowGetByPlanid(planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectedCashFlowApi#projectedCashFlowGetByPlanid");
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

[**CashFlowProjectionsModel**](CashFlowProjectionsModel.md)

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

