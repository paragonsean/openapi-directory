# ProjectedNetWorthApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**projectedNetWorthGetByIdPlanid**](ProjectedNetWorthApi.md#projectedNetWorthGetByIdPlanid) | **GET** /api/ProjectedNetWorth/{id} | Retrieve projected net worth by id |
| [**projectedNetWorthGetByPlanid**](ProjectedNetWorthApi.md#projectedNetWorthGetByPlanid) | **GET** /api/ProjectedNetWorth | Retrieve projected net worth |


<a id="projectedNetWorthGetByIdPlanid"></a>
# **projectedNetWorthGetByIdPlanid**
> NetWorthProjectionModel projectedNetWorthGetByIdPlanid(id, planId)

Retrieve projected net worth by id

This operation retrieves an object containing net worth information                 for a single specified year of the projected plan. These are EOY numbers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectedNetWorthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    ProjectedNetWorthApi apiInstance = new ProjectedNetWorthApi(defaultClient);
    Integer id = 56; // Integer | Index into the list of annual projections
    String planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
    try {
      NetWorthProjectionModel result = apiInstance.projectedNetWorthGetByIdPlanid(id, planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectedNetWorthApi#projectedNetWorthGetByIdPlanid");
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

[**NetWorthProjectionModel**](NetWorthProjectionModel.md)

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

<a id="projectedNetWorthGetByPlanid"></a>
# **projectedNetWorthGetByPlanid**
> NetWorthProjectionsModel projectedNetWorthGetByPlanid(planId)

Retrieve projected net worth

This operation retrieves an object containing net worth information                 for each year of the projected plan. These are EOY numbers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectedNetWorthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    ProjectedNetWorthApi apiInstance = new ProjectedNetWorthApi(defaultClient);
    String planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
    try {
      NetWorthProjectionsModel result = apiInstance.projectedNetWorthGetByPlanid(planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectedNetWorthApi#projectedNetWorthGetByPlanid");
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

[**NetWorthProjectionsModel**](NetWorthProjectionsModel.md)

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

