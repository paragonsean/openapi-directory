# ProjectedAnnualSummaryApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**projectedAnnualSummaryGetByIdPlanid**](ProjectedAnnualSummaryApi.md#projectedAnnualSummaryGetByIdPlanid) | **GET** /api/ProjectedAnnualSummary/{id} | Retrieve projected annual summary by id |
| [**projectedAnnualSummaryGetByPlanid**](ProjectedAnnualSummaryApi.md#projectedAnnualSummaryGetByPlanid) | **GET** /api/ProjectedAnnualSummary | Retrieve projected annual summaries |


<a id="projectedAnnualSummaryGetByIdPlanid"></a>
# **projectedAnnualSummaryGetByIdPlanid**
> ProjectedAnnualSummaryModel projectedAnnualSummaryGetByIdPlanid(id, planId)

Retrieve projected annual summary by id

This operation retrieves an object containing annual summary information                 for a single specified year of the projected plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectedAnnualSummaryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    ProjectedAnnualSummaryApi apiInstance = new ProjectedAnnualSummaryApi(defaultClient);
    Integer id = 56; // Integer | Index into the list of annual projections
    String planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
    try {
      ProjectedAnnualSummaryModel result = apiInstance.projectedAnnualSummaryGetByIdPlanid(id, planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectedAnnualSummaryApi#projectedAnnualSummaryGetByIdPlanid");
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

[**ProjectedAnnualSummaryModel**](ProjectedAnnualSummaryModel.md)

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

<a id="projectedAnnualSummaryGetByPlanid"></a>
# **projectedAnnualSummaryGetByPlanid**
> ProjectedAnnualSummariesModel projectedAnnualSummaryGetByPlanid(planId)

Retrieve projected annual summaries

This operation retrieves an object containing annual summary information                 for each year of the projected plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectedAnnualSummaryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    ProjectedAnnualSummaryApi apiInstance = new ProjectedAnnualSummaryApi(defaultClient);
    String planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
    try {
      ProjectedAnnualSummariesModel result = apiInstance.projectedAnnualSummaryGetByPlanid(planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectedAnnualSummaryApi#projectedAnnualSummaryGetByPlanid");
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

[**ProjectedAnnualSummariesModel**](ProjectedAnnualSummariesModel.md)

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

