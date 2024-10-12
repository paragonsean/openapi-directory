# GoalAdjustmentsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**goalAdjustmentsGetEducationByIdClientidPlanid**](GoalAdjustmentsApi.md#goalAdjustmentsGetEducationByIdClientidPlanid) | **GET** /api/GoalAdjustments/Education/{id}/Adjustments | Retrieve the adjustments |
| [**goalAdjustmentsGetGoalAdjustmentRestrictionsByClientidPlanid**](GoalAdjustmentsApi.md#goalAdjustmentsGetGoalAdjustmentRestrictionsByClientidPlanid) | **GET** /api/GoalAdjustments/Restrictions | Returns a list of goal adjustment restrictions. |
| [**goalAdjustmentsGetGoalSuccessRatesByClientidPlanid**](GoalAdjustmentsApi.md#goalAdjustmentsGetGoalSuccessRatesByClientidPlanid) | **GET** /api/GoalAdjustments/GoalSuccessRates | Returns a list of goals with their relevant success rates. |
| [**goalAdjustmentsGetMajorPurchaseByIdClientidPlanid**](GoalAdjustmentsApi.md#goalAdjustmentsGetMajorPurchaseByIdClientidPlanid) | **GET** /api/GoalAdjustments/MajorPurchase/{id}/Adjustments | Retrieve the adjustments |
| [**goalAdjustmentsGetRetirementByClientidPlanid**](GoalAdjustmentsApi.md#goalAdjustmentsGetRetirementByClientidPlanid) | **GET** /api/GoalAdjustments/Retirement/Adjustments | Retrieve the adjustments |
| [**goalAdjustmentsGetWhatAreMyOptionsByIdClientidPlanid**](GoalAdjustmentsApi.md#goalAdjustmentsGetWhatAreMyOptionsByIdClientidPlanid) | **GET** /api/GoalAdjustments/{id}/WhatAreMyOptions | Returns WAMO values for current goal |
| [**goalAdjustmentsPostEducationByIdGoaladjustmentsPlanid**](GoalAdjustmentsApi.md#goalAdjustmentsPostEducationByIdGoaladjustmentsPlanid) | **POST** /api/GoalAdjustments/Education/{id}/Calculations | Perform calculations |
| [**goalAdjustmentsPostMajorPurchaseByIdGoaladjustmentsPlanid**](GoalAdjustmentsApi.md#goalAdjustmentsPostMajorPurchaseByIdGoaladjustmentsPlanid) | **POST** /api/GoalAdjustments/MajorPurchase/{id}/Calculations | Perform calculations |
| [**goalAdjustmentsPostRetirementByGoaladjustmentsPlanid**](GoalAdjustmentsApi.md#goalAdjustmentsPostRetirementByGoaladjustmentsPlanid) | **POST** /api/GoalAdjustments/Retirement/Calculations | Perform calculations |


<a id="goalAdjustmentsGetEducationByIdClientidPlanid"></a>
# **goalAdjustmentsGetEducationByIdClientidPlanid**
> AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel goalAdjustmentsGetEducationByIdClientidPlanid(id, planId, clientId)

Retrieve the adjustments

This function retrieves a goal and the adjustments made to it

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GoalAdjustmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    GoalAdjustmentsApi apiInstance = new GoalAdjustmentsApi(defaultClient);
    Integer id = 56; // Integer | The id of the goal to retrieve adjustments for.
    String planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    String clientId = "clientId_example"; // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    try {
      AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel result = apiInstance.goalAdjustmentsGetEducationByIdClientidPlanid(id, planId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GoalAdjustmentsApi#goalAdjustmentsGetEducationByIdClientidPlanid");
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
| **id** | **Integer**| The id of the goal to retrieve adjustments for. | |
| **planId** | **String**| Id of the Plan to retrieve or update data for (e.g. 1001-11-3). | |
| **clientId** | **String**| Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions. | [optional] |

### Return type

[**AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel.md)

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
| **401** | Unauthorized for plan data access |  -  |
| **404** | Object not found |  -  |
| **503** | Unable to acquire a NaviPlan engine |  -  |

<a id="goalAdjustmentsGetGoalAdjustmentRestrictionsByClientidPlanid"></a>
# **goalAdjustmentsGetGoalAdjustmentRestrictionsByClientidPlanid**
> AdvicentNaviPlanRestApiGoalAdjustmentsModelsRestrictionsResultModel goalAdjustmentsGetGoalAdjustmentRestrictionsByClientidPlanid(planId, clientId)

Returns a list of goal adjustment restrictions.

This function returns a list of adjustment restrictions for all goals.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GoalAdjustmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    GoalAdjustmentsApi apiInstance = new GoalAdjustmentsApi(defaultClient);
    String planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    String clientId = "clientId_example"; // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    try {
      AdvicentNaviPlanRestApiGoalAdjustmentsModelsRestrictionsResultModel result = apiInstance.goalAdjustmentsGetGoalAdjustmentRestrictionsByClientidPlanid(planId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GoalAdjustmentsApi#goalAdjustmentsGetGoalAdjustmentRestrictionsByClientidPlanid");
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
| **planId** | **String**| Id of the Plan to retrieve or update data for (e.g. 1001-11-3). | |
| **clientId** | **String**| Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions. | [optional] |

### Return type

[**AdvicentNaviPlanRestApiGoalAdjustmentsModelsRestrictionsResultModel**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsRestrictionsResultModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Restrictions successfully retrieved. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized for plan data access |  -  |
| **404** | Object not found |  -  |
| **503** | Unable to acquire a NaviPlan engine |  -  |

<a id="goalAdjustmentsGetGoalSuccessRatesByClientidPlanid"></a>
# **goalAdjustmentsGetGoalSuccessRatesByClientidPlanid**
> AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateResultsModel goalAdjustmentsGetGoalSuccessRatesByClientidPlanid(planId, clientId)

Returns a list of goals with their relevant success rates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GoalAdjustmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    GoalAdjustmentsApi apiInstance = new GoalAdjustmentsApi(defaultClient);
    String planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    String clientId = "clientId_example"; // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    try {
      AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateResultsModel result = apiInstance.goalAdjustmentsGetGoalSuccessRatesByClientidPlanid(planId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GoalAdjustmentsApi#goalAdjustmentsGetGoalSuccessRatesByClientidPlanid");
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
| **planId** | **String**| Id of the Plan to retrieve or update data for (e.g. 1001-11-3). | |
| **clientId** | **String**| Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions. | [optional] |

### Return type

[**AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateResultsModel**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateResultsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Goal Success Rates successfully retrieved. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized for plan data access |  -  |
| **404** | Object not found |  -  |
| **503** | Unable to acquire a NaviPlan engine |  -  |

<a id="goalAdjustmentsGetMajorPurchaseByIdClientidPlanid"></a>
# **goalAdjustmentsGetMajorPurchaseByIdClientidPlanid**
> AdvicentNaviPlanRestApiGoalAdjustmentsModelsMajorPurchaseGoalAdjustmentsModel goalAdjustmentsGetMajorPurchaseByIdClientidPlanid(id, planId, clientId)

Retrieve the adjustments

This function retrieves a goal and the adjustments made to it

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GoalAdjustmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    GoalAdjustmentsApi apiInstance = new GoalAdjustmentsApi(defaultClient);
    Integer id = 56; // Integer | The id of the goal to retrieve adjustments for.
    String planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    String clientId = "clientId_example"; // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    try {
      AdvicentNaviPlanRestApiGoalAdjustmentsModelsMajorPurchaseGoalAdjustmentsModel result = apiInstance.goalAdjustmentsGetMajorPurchaseByIdClientidPlanid(id, planId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GoalAdjustmentsApi#goalAdjustmentsGetMajorPurchaseByIdClientidPlanid");
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
| **id** | **Integer**| The id of the goal to retrieve adjustments for. | |
| **planId** | **String**| Id of the Plan to retrieve or update data for (e.g. 1001-11-3). | |
| **clientId** | **String**| Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions. | [optional] |

### Return type

[**AdvicentNaviPlanRestApiGoalAdjustmentsModelsMajorPurchaseGoalAdjustmentsModel**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsMajorPurchaseGoalAdjustmentsModel.md)

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
| **401** | Unauthorized for plan data access |  -  |
| **404** | Object not found |  -  |
| **503** | Unable to acquire a NaviPlan engine |  -  |

<a id="goalAdjustmentsGetRetirementByClientidPlanid"></a>
# **goalAdjustmentsGetRetirementByClientidPlanid**
> AdvicentNaviPlanRestApiGoalAdjustmentsModelsRetirementGoalAdjustmentsModel goalAdjustmentsGetRetirementByClientidPlanid(planId, clientId)

Retrieve the adjustments

This function retrieves a goal and the adjustments made to it for a particular client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GoalAdjustmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    GoalAdjustmentsApi apiInstance = new GoalAdjustmentsApi(defaultClient);
    String planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    String clientId = "clientId_example"; // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    try {
      AdvicentNaviPlanRestApiGoalAdjustmentsModelsRetirementGoalAdjustmentsModel result = apiInstance.goalAdjustmentsGetRetirementByClientidPlanid(planId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GoalAdjustmentsApi#goalAdjustmentsGetRetirementByClientidPlanid");
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
| **planId** | **String**| Id of the Plan to retrieve or update data for (e.g. 1001-11-3). | |
| **clientId** | **String**| Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions. | [optional] |

### Return type

[**AdvicentNaviPlanRestApiGoalAdjustmentsModelsRetirementGoalAdjustmentsModel**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsRetirementGoalAdjustmentsModel.md)

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
| **401** | Unauthorized for plan data access |  -  |
| **404** | Object not found |  -  |
| **503** | Unable to acquire a NaviPlan engine |  -  |

<a id="goalAdjustmentsGetWhatAreMyOptionsByIdClientidPlanid"></a>
# **goalAdjustmentsGetWhatAreMyOptionsByIdClientidPlanid**
> AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel goalAdjustmentsGetWhatAreMyOptionsByIdClientidPlanid(id, planId, clientId)

Returns WAMO values for current goal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GoalAdjustmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    GoalAdjustmentsApi apiInstance = new GoalAdjustmentsApi(defaultClient);
    Integer id = 56; // Integer | The id of the goal to retrieve WAMO values for.
    String planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    String clientId = "clientId_example"; // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    try {
      AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel result = apiInstance.goalAdjustmentsGetWhatAreMyOptionsByIdClientidPlanid(id, planId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GoalAdjustmentsApi#goalAdjustmentsGetWhatAreMyOptionsByIdClientidPlanid");
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
| **id** | **Integer**| The id of the goal to retrieve WAMO values for. | |
| **planId** | **String**| Id of the Plan to retrieve or update data for (e.g. 1001-11-3). | |
| **clientId** | **String**| Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions. | [optional] |

### Return type

[**AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | What are my options results successfully retrieved. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized for plan data access |  -  |
| **404** | Object not found |  -  |
| **503** | Unable to acquire a NaviPlan engine |  -  |

<a id="goalAdjustmentsPostEducationByIdGoaladjustmentsPlanid"></a>
# **goalAdjustmentsPostEducationByIdGoaladjustmentsPlanid**
> AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments goalAdjustmentsPostEducationByIdGoaladjustmentsPlanid(id, planId, goalAdjustments)

Perform calculations

This function returns the posted object and the adjusted calculation values

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GoalAdjustmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    GoalAdjustmentsApi apiInstance = new GoalAdjustmentsApi(defaultClient);
    Integer id = 56; // Integer | The id of the goal to retrieve adjustments for.
    String planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments goalAdjustments = new AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments(); // AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments | The adjusted values for this goal
    try {
      AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments result = apiInstance.goalAdjustmentsPostEducationByIdGoaladjustmentsPlanid(id, planId, goalAdjustments);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GoalAdjustmentsApi#goalAdjustmentsPostEducationByIdGoaladjustmentsPlanid");
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
| **id** | **Integer**| The id of the goal to retrieve adjustments for. | |
| **planId** | **String**| Id of the Plan to retrieve or update data for (e.g. 1001-11-3). | |
| **goalAdjustments** | [**AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments.md)| The adjusted values for this goal | |

### Return type

[**AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized for plan data access |  -  |
| **404** | Object not found |  -  |
| **503** | Unable to acquire a NaviPlan engine |  -  |

<a id="goalAdjustmentsPostMajorPurchaseByIdGoaladjustmentsPlanid"></a>
# **goalAdjustmentsPostMajorPurchaseByIdGoaladjustmentsPlanid**
> AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfMajorPurchaseGoalAdjustments goalAdjustmentsPostMajorPurchaseByIdGoaladjustmentsPlanid(id, planId, goalAdjustments)

Perform calculations

This function returns the posted object and the adjusted calculation values

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GoalAdjustmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    GoalAdjustmentsApi apiInstance = new GoalAdjustmentsApi(defaultClient);
    Integer id = 56; // Integer | The id of the goal to retrieve adjustments for.
    String planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfMajorPurchaseGoalAdjustments goalAdjustments = new AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfMajorPurchaseGoalAdjustments(); // AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfMajorPurchaseGoalAdjustments | The adjusted values for this goal
    try {
      AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfMajorPurchaseGoalAdjustments result = apiInstance.goalAdjustmentsPostMajorPurchaseByIdGoaladjustmentsPlanid(id, planId, goalAdjustments);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GoalAdjustmentsApi#goalAdjustmentsPostMajorPurchaseByIdGoaladjustmentsPlanid");
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
| **id** | **Integer**| The id of the goal to retrieve adjustments for. | |
| **planId** | **String**| Id of the Plan to retrieve or update data for (e.g. 1001-11-3). | |
| **goalAdjustments** | [**AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfMajorPurchaseGoalAdjustments**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfMajorPurchaseGoalAdjustments.md)| The adjusted values for this goal | |

### Return type

[**AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfMajorPurchaseGoalAdjustments**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfMajorPurchaseGoalAdjustments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized for plan data access |  -  |
| **404** | Object not found |  -  |
| **503** | Unable to acquire a NaviPlan engine |  -  |

<a id="goalAdjustmentsPostRetirementByGoaladjustmentsPlanid"></a>
# **goalAdjustmentsPostRetirementByGoaladjustmentsPlanid**
> AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments goalAdjustmentsPostRetirementByGoaladjustmentsPlanid(planId, goalAdjustments)

Perform calculations

This function returns the posted object and the adjusted calculation values

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GoalAdjustmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    GoalAdjustmentsApi apiInstance = new GoalAdjustmentsApi(defaultClient);
    String planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments goalAdjustments = new AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments(); // AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments | The adjusted values for this goal
    try {
      AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments result = apiInstance.goalAdjustmentsPostRetirementByGoaladjustmentsPlanid(planId, goalAdjustments);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GoalAdjustmentsApi#goalAdjustmentsPostRetirementByGoaladjustmentsPlanid");
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
| **planId** | **String**| Id of the Plan to retrieve or update data for (e.g. 1001-11-3). | |
| **goalAdjustments** | [**AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments.md)| The adjusted values for this goal | |

### Return type

[**AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized for plan data access |  -  |
| **404** | Object not found |  -  |
| **503** | Unable to acquire a NaviPlan engine |  -  |

