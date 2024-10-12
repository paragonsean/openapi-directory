# ProjectedGoalsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**projectedGoalsGetAssetsFundingGoalsByPlanid**](ProjectedGoalsApi.md#projectedGoalsGetAssetsFundingGoalsByPlanid) | **GET** /api/ProjectedGoals/AssetsFundingGoals | Retrieve assets funding goals over time |
| [**projectedGoalsGetNeedsVsAbilitiesByPlanid**](ProjectedGoalsApi.md#projectedGoalsGetNeedsVsAbilitiesByPlanid) | **GET** /api/ProjectedGoals/NeedsVsAbilities | Retrieve needs vs abilities data |


<a id="projectedGoalsGetAssetsFundingGoalsByPlanid"></a>
# **projectedGoalsGetAssetsFundingGoalsByPlanid**
> AssetsFundingGoalModel projectedGoalsGetAssetsFundingGoalsByPlanid(planId)

Retrieve assets funding goals over time

This operation retrieves the assets funding each goal throughout the plan years

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectedGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    ProjectedGoalsApi apiInstance = new ProjectedGoalsApi(defaultClient);
    String planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
    try {
      AssetsFundingGoalModel result = apiInstance.projectedGoalsGetAssetsFundingGoalsByPlanid(planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectedGoalsApi#projectedGoalsGetAssetsFundingGoalsByPlanid");
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

[**AssetsFundingGoalModel**](AssetsFundingGoalModel.md)

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

<a id="projectedGoalsGetNeedsVsAbilitiesByPlanid"></a>
# **projectedGoalsGetNeedsVsAbilitiesByPlanid**
> NeedsVsAbilitiesModel projectedGoalsGetNeedsVsAbilitiesByPlanid(planId)

Retrieve needs vs abilities data

This operation retrieves a needs and abilities data for all goals throughout                the plan years.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectedGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    ProjectedGoalsApi apiInstance = new ProjectedGoalsApi(defaultClient);
    String planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
    try {
      NeedsVsAbilitiesModel result = apiInstance.projectedGoalsGetNeedsVsAbilitiesByPlanid(planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectedGoalsApi#projectedGoalsGetNeedsVsAbilitiesByPlanid");
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

[**NeedsVsAbilitiesModel**](NeedsVsAbilitiesModel.md)

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

