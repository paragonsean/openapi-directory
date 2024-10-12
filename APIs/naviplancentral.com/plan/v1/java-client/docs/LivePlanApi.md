# LivePlanApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**livePlanGetAccountsByClientidPlanid**](LivePlanApi.md#livePlanGetAccountsByClientidPlanid) | **GET** /api/LivePlan/NetWorth/Accounts | Retrieves accounts for a given plan |
| [**livePlanGetGoalFundingListByClientidPlanid**](LivePlanApi.md#livePlanGetGoalFundingListByClientidPlanid) | **GET** /api/LivePlan/Goals/Funding | Retrieve a list of funding accounts |
| [**livePlanGetGoalsByClientidPlanid**](LivePlanApi.md#livePlanGetGoalsByClientidPlanid) | **GET** /api/LivePlan/Goals | Retrieves all goals from the live plan |
| [**livePlanGetLiabilitiesByClientidPlanid**](LivePlanApi.md#livePlanGetLiabilitiesByClientidPlanid) | **GET** /api/LivePlan/NetWorth/Liabilities | Retrieves liabilities for a given plan |
| [**livePlanGetLifestyleAssetsByClientidPlanid**](LivePlanApi.md#livePlanGetLifestyleAssetsByClientidPlanid) | **GET** /api/LivePlan/NetWorth/LifestyleAssets | Retrieves lifestyle assets for a given plan |
| [**livePlanGetProjectedNeedsVsAbilitiesByIdClientidPlanid**](LivePlanApi.md#livePlanGetProjectedNeedsVsAbilitiesByIdClientidPlanid) | **GET** /api/LivePlan/Projections/{id}/NeedsVsAbilities | Retrieves needs vs abilities projections |
| [**livePlanGetProjectedNetWorthByClientidPlanid**](LivePlanApi.md#livePlanGetProjectedNetWorthByClientidPlanid) | **GET** /api/LivePlan/Projections/NetWorth | Retrieves net worth projections |
| [**livePlanGetRealEstateAssetsByClientidPlanid**](LivePlanApi.md#livePlanGetRealEstateAssetsByClientidPlanid) | **GET** /api/LivePlan/NetWorth/RealEstate | Retrieves real estate accounts for a given plan |
| [**livePlanGetWhatAreMyOptionsByIdClientidPlanid**](LivePlanApi.md#livePlanGetWhatAreMyOptionsByIdClientidPlanid) | **GET** /api/LivePlan/Goals/{id}/WhatAreMyOptions | Retrieve WAMO values for a given goal |


<a id="livePlanGetAccountsByClientidPlanid"></a>
# **livePlanGetAccountsByClientidPlanid**
> AdvicentNaviPlanRestApiNetWorthModelsAccountBaseModel livePlanGetAccountsByClientidPlanid(planId, clientId)

Retrieves accounts for a given plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LivePlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    LivePlanApi apiInstance = new LivePlanApi(defaultClient);
    String planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    String clientId = "clientId_example"; // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    try {
      AdvicentNaviPlanRestApiNetWorthModelsAccountBaseModel result = apiInstance.livePlanGetAccountsByClientidPlanid(planId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LivePlanApi#livePlanGetAccountsByClientidPlanid");
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

[**AdvicentNaviPlanRestApiNetWorthModelsAccountBaseModel**](AdvicentNaviPlanRestApiNetWorthModelsAccountBaseModel.md)

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

<a id="livePlanGetGoalFundingListByClientidPlanid"></a>
# **livePlanGetGoalFundingListByClientidPlanid**
> AdvicentNaviPlanRestApiGoalsModelsGoalFundingListModel livePlanGetGoalFundingListByClientidPlanid(planId, clientId)

Retrieve a list of funding accounts

This function retrieves a list of funding accounts for the goals in the plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LivePlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    LivePlanApi apiInstance = new LivePlanApi(defaultClient);
    String planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    String clientId = "clientId_example"; // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    try {
      AdvicentNaviPlanRestApiGoalsModelsGoalFundingListModel result = apiInstance.livePlanGetGoalFundingListByClientidPlanid(planId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LivePlanApi#livePlanGetGoalFundingListByClientidPlanid");
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

[**AdvicentNaviPlanRestApiGoalsModelsGoalFundingListModel**](AdvicentNaviPlanRestApiGoalsModelsGoalFundingListModel.md)

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

<a id="livePlanGetGoalsByClientidPlanid"></a>
# **livePlanGetGoalsByClientidPlanid**
> AdvicentNaviPlanRestApiGoalsModelsLiveGoalBaseModel livePlanGetGoalsByClientidPlanid(planId, clientId)

Retrieves all goals from the live plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LivePlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    LivePlanApi apiInstance = new LivePlanApi(defaultClient);
    String planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    String clientId = "clientId_example"; // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    try {
      AdvicentNaviPlanRestApiGoalsModelsLiveGoalBaseModel result = apiInstance.livePlanGetGoalsByClientidPlanid(planId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LivePlanApi#livePlanGetGoalsByClientidPlanid");
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

[**AdvicentNaviPlanRestApiGoalsModelsLiveGoalBaseModel**](AdvicentNaviPlanRestApiGoalsModelsLiveGoalBaseModel.md)

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

<a id="livePlanGetLiabilitiesByClientidPlanid"></a>
# **livePlanGetLiabilitiesByClientidPlanid**
> AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel livePlanGetLiabilitiesByClientidPlanid(planId, clientId)

Retrieves liabilities for a given plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LivePlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    LivePlanApi apiInstance = new LivePlanApi(defaultClient);
    String planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    String clientId = "clientId_example"; // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    try {
      AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel result = apiInstance.livePlanGetLiabilitiesByClientidPlanid(planId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LivePlanApi#livePlanGetLiabilitiesByClientidPlanid");
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

[**AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel**](AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel.md)

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

<a id="livePlanGetLifestyleAssetsByClientidPlanid"></a>
# **livePlanGetLifestyleAssetsByClientidPlanid**
> AdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetBaseModel livePlanGetLifestyleAssetsByClientidPlanid(planId, clientId)

Retrieves lifestyle assets for a given plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LivePlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    LivePlanApi apiInstance = new LivePlanApi(defaultClient);
    String planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    String clientId = "clientId_example"; // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    try {
      AdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetBaseModel result = apiInstance.livePlanGetLifestyleAssetsByClientidPlanid(planId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LivePlanApi#livePlanGetLifestyleAssetsByClientidPlanid");
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

[**AdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetBaseModel**](AdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetBaseModel.md)

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

<a id="livePlanGetProjectedNeedsVsAbilitiesByIdClientidPlanid"></a>
# **livePlanGetProjectedNeedsVsAbilitiesByIdClientidPlanid**
> AdvicentNaviPlanRestApiProjectionsModelsNeedsVsAbilitiesProjectionsModel livePlanGetProjectedNeedsVsAbilitiesByIdClientidPlanid(id, planId, clientId)

Retrieves needs vs abilities projections

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LivePlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    LivePlanApi apiInstance = new LivePlanApi(defaultClient);
    Integer id = 56; // Integer | 
    String planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    String clientId = "clientId_example"; // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    try {
      AdvicentNaviPlanRestApiProjectionsModelsNeedsVsAbilitiesProjectionsModel result = apiInstance.livePlanGetProjectedNeedsVsAbilitiesByIdClientidPlanid(id, planId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LivePlanApi#livePlanGetProjectedNeedsVsAbilitiesByIdClientidPlanid");
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
| **id** | **Integer**|  | |
| **planId** | **String**| Id of the Plan to retrieve or update data for (e.g. 1001-11-3). | |
| **clientId** | **String**| Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions. | [optional] |

### Return type

[**AdvicentNaviPlanRestApiProjectionsModelsNeedsVsAbilitiesProjectionsModel**](AdvicentNaviPlanRestApiProjectionsModelsNeedsVsAbilitiesProjectionsModel.md)

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

<a id="livePlanGetProjectedNetWorthByClientidPlanid"></a>
# **livePlanGetProjectedNetWorthByClientidPlanid**
> AdvicentNaviPlanRestApiProjectionsModelsNetWorthProjectionsModel livePlanGetProjectedNetWorthByClientidPlanid(planId, clientId)

Retrieves net worth projections

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LivePlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    LivePlanApi apiInstance = new LivePlanApi(defaultClient);
    String planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    String clientId = "clientId_example"; // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    try {
      AdvicentNaviPlanRestApiProjectionsModelsNetWorthProjectionsModel result = apiInstance.livePlanGetProjectedNetWorthByClientidPlanid(planId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LivePlanApi#livePlanGetProjectedNetWorthByClientidPlanid");
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

[**AdvicentNaviPlanRestApiProjectionsModelsNetWorthProjectionsModel**](AdvicentNaviPlanRestApiProjectionsModelsNetWorthProjectionsModel.md)

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

<a id="livePlanGetRealEstateAssetsByClientidPlanid"></a>
# **livePlanGetRealEstateAssetsByClientidPlanid**
> AdvicentNaviPlanRestApiNetWorthModelsRealEstateBaseModel livePlanGetRealEstateAssetsByClientidPlanid(planId, clientId)

Retrieves real estate accounts for a given plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LivePlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    LivePlanApi apiInstance = new LivePlanApi(defaultClient);
    String planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    String clientId = "clientId_example"; // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    try {
      AdvicentNaviPlanRestApiNetWorthModelsRealEstateBaseModel result = apiInstance.livePlanGetRealEstateAssetsByClientidPlanid(planId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LivePlanApi#livePlanGetRealEstateAssetsByClientidPlanid");
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

[**AdvicentNaviPlanRestApiNetWorthModelsRealEstateBaseModel**](AdvicentNaviPlanRestApiNetWorthModelsRealEstateBaseModel.md)

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

<a id="livePlanGetWhatAreMyOptionsByIdClientidPlanid"></a>
# **livePlanGetWhatAreMyOptionsByIdClientidPlanid**
> AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel livePlanGetWhatAreMyOptionsByIdClientidPlanid(id, planId, clientId)

Retrieve WAMO values for a given goal

This function retrieves the WAMO values for the specified goal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LivePlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    LivePlanApi apiInstance = new LivePlanApi(defaultClient);
    Integer id = 56; // Integer | The id of the goal
    String planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
    String clientId = "clientId_example"; // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
    try {
      AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel result = apiInstance.livePlanGetWhatAreMyOptionsByIdClientidPlanid(id, planId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LivePlanApi#livePlanGetWhatAreMyOptionsByIdClientidPlanid");
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
| **id** | **Integer**| The id of the goal | |
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
| **200** | Success |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized for plan data access |  -  |
| **404** | Object not found |  -  |
| **503** | Unable to acquire a NaviPlan engine |  -  |

