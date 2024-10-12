# PlanStatusesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**planStatusesGetByPlanid**](PlanStatusesApi.md#planStatusesGetByPlanid) | **GET** /api/PlanStatuses | Retrieve plan data statuses |


<a id="planStatusesGetByPlanid"></a>
# **planStatusesGetByPlanid**
> PlanStatusesModel planStatusesGetByPlanid(planId)

Retrieve plan data statuses

This operation retrieves the data statuses of the published plan if on demand updates              are enabled

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlanStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    PlanStatusesApi apiInstance = new PlanStatusesApi(defaultClient);
    String planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3)
    try {
      PlanStatusesModel result = apiInstance.planStatusesGetByPlanid(planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlanStatusesApi#planStatusesGetByPlanid");
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
| **planId** | **String**| Id of the plan to retrieve data from (e.g. 1001-11-3) | |

### Return type

[**PlanStatusesModel**](PlanStatusesModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized for plan status access |  -  |
| **404** | Object not found |  -  |

