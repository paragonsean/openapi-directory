# PortfolioAccountsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**portfolioAccountsGetByIdPlanid**](PortfolioAccountsApi.md#portfolioAccountsGetByIdPlanid) | **GET** /api/PortfolioAccounts/{id} | Retrieve a portfolio account |
| [**portfolioAccountsGetByPlanid**](PortfolioAccountsApi.md#portfolioAccountsGetByPlanid) | **GET** /api/PortfolioAccounts | Retrieve portfolio accounts |


<a id="portfolioAccountsGetByIdPlanid"></a>
# **portfolioAccountsGetByIdPlanid**
> PortfolioAccountModel portfolioAccountsGetByIdPlanid(id, planId)

Retrieve a portfolio account

This operation retrieves a portfolio account from the plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortfolioAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    PortfolioAccountsApi apiInstance = new PortfolioAccountsApi(defaultClient);
    Integer id = 56; // Integer | ID of portfolio account to retrieve
    String planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
    try {
      PortfolioAccountModel result = apiInstance.portfolioAccountsGetByIdPlanid(id, planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortfolioAccountsApi#portfolioAccountsGetByIdPlanid");
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
| **id** | **Integer**| ID of portfolio account to retrieve | |
| **planId** | **String**| Id of the plan to retrieve data from (e.g. 1001-11-3). | |

### Return type

[**PortfolioAccountModel**](PortfolioAccountModel.md)

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

<a id="portfolioAccountsGetByPlanid"></a>
# **portfolioAccountsGetByPlanid**
> PortfolioAccountsModel portfolioAccountsGetByPlanid(planId)

Retrieve portfolio accounts

This operation retrieves a list of all of the portfolio accounts in the plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortfolioAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    PortfolioAccountsApi apiInstance = new PortfolioAccountsApi(defaultClient);
    String planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
    try {
      PortfolioAccountsModel result = apiInstance.portfolioAccountsGetByPlanid(planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortfolioAccountsApi#portfolioAccountsGetByPlanid");
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

[**PortfolioAccountsModel**](PortfolioAccountsModel.md)

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

