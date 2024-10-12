# GoalsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**goalsGetByIdPlanid**](GoalsApi.md#goalsGetByIdPlanid) | **GET** /api/Goals/{id} | Retrieve goals |
| [**goalsGetByPlanid**](GoalsApi.md#goalsGetByPlanid) | **GET** /api/Goals | Retrieve goals |


<a id="goalsGetByIdPlanid"></a>
# **goalsGetByIdPlanid**
> GoalModel goalsGetByIdPlanid(id, planId)

Retrieve goals

This operation retrieves a goal from the plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    GoalsApi apiInstance = new GoalsApi(defaultClient);
    Integer id = 56; // Integer | ID of goal to retrieve
    String planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
    try {
      GoalModel result = apiInstance.goalsGetByIdPlanid(id, planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GoalsApi#goalsGetByIdPlanid");
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
| **id** | **Integer**| ID of goal to retrieve | |
| **planId** | **String**| Id of the plan to retrieve data from (e.g. 1001-11-3). | |

### Return type

[**GoalModel**](GoalModel.md)

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

<a id="goalsGetByPlanid"></a>
# **goalsGetByPlanid**
> GoalsModel goalsGetByPlanid(planId)

Retrieve goals

This operation retrieves a list of all of the goals in the plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    GoalsApi apiInstance = new GoalsApi(defaultClient);
    String planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
    try {
      GoalsModel result = apiInstance.goalsGetByPlanid(planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GoalsApi#goalsGetByPlanid");
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

[**GoalsModel**](GoalsModel.md)

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

