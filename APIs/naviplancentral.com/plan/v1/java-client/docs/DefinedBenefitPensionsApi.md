# DefinedBenefitPensionsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**definedBenefitPensionsGetByIdPlanid**](DefinedBenefitPensionsApi.md#definedBenefitPensionsGetByIdPlanid) | **GET** /api/DefinedBenefitPensions/{id} | Retrieve a definedBenefitPension |
| [**definedBenefitPensionsGetByPlanid**](DefinedBenefitPensionsApi.md#definedBenefitPensionsGetByPlanid) | **GET** /api/DefinedBenefitPensions | Retrieve defined benefit pensions |


<a id="definedBenefitPensionsGetByIdPlanid"></a>
# **definedBenefitPensionsGetByIdPlanid**
> DefinedBenefitPensionModel definedBenefitPensionsGetByIdPlanid(id, planId)

Retrieve a definedBenefitPension

This operation retrieves a defined benefit pension from the plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefinedBenefitPensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    DefinedBenefitPensionsApi apiInstance = new DefinedBenefitPensionsApi(defaultClient);
    Integer id = 56; // Integer | ID of defined benefit pension to retrieve
    String planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
    try {
      DefinedBenefitPensionModel result = apiInstance.definedBenefitPensionsGetByIdPlanid(id, planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefinedBenefitPensionsApi#definedBenefitPensionsGetByIdPlanid");
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
| **id** | **Integer**| ID of defined benefit pension to retrieve | |
| **planId** | **String**| Id of the plan to retrieve data from (e.g. 1001-11-3). | |

### Return type

[**DefinedBenefitPensionModel**](DefinedBenefitPensionModel.md)

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

<a id="definedBenefitPensionsGetByPlanid"></a>
# **definedBenefitPensionsGetByPlanid**
> DefinedBenefitPensionsModel definedBenefitPensionsGetByPlanid(planId)

Retrieve defined benefit pensions

This operation retrieves a list of all of the defined benefit pensions in the plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefinedBenefitPensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    DefinedBenefitPensionsApi apiInstance = new DefinedBenefitPensionsApi(defaultClient);
    String planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
    try {
      DefinedBenefitPensionsModel result = apiInstance.definedBenefitPensionsGetByPlanid(planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefinedBenefitPensionsApi#definedBenefitPensionsGetByPlanid");
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

[**DefinedBenefitPensionsModel**](DefinedBenefitPensionsModel.md)

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

