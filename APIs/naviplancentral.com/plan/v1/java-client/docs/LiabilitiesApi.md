# LiabilitiesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**liabilitiesGetByIdPlanid**](LiabilitiesApi.md#liabilitiesGetByIdPlanid) | **GET** /api/Liabilities/{id} | Retrieve a liability |
| [**liabilitiesGetByPlanid**](LiabilitiesApi.md#liabilitiesGetByPlanid) | **GET** /api/Liabilities | Retrieve liabilities |


<a id="liabilitiesGetByIdPlanid"></a>
# **liabilitiesGetByIdPlanid**
> LiabilityModel liabilitiesGetByIdPlanid(id, planId)

Retrieve a liability

This operation retrieves a liability from the plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiabilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    LiabilitiesApi apiInstance = new LiabilitiesApi(defaultClient);
    Integer id = 56; // Integer | ID of liability to retrieve
    String planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
    try {
      LiabilityModel result = apiInstance.liabilitiesGetByIdPlanid(id, planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiabilitiesApi#liabilitiesGetByIdPlanid");
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
| **id** | **Integer**| ID of liability to retrieve | |
| **planId** | **String**| Id of the plan to retrieve data from (e.g. 1001-11-3). | |

### Return type

[**LiabilityModel**](LiabilityModel.md)

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

<a id="liabilitiesGetByPlanid"></a>
# **liabilitiesGetByPlanid**
> LiabilitiesModel liabilitiesGetByPlanid(planId)

Retrieve liabilities

This operation retrieves a list of all of the liabilities in the plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiabilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    LiabilitiesApi apiInstance = new LiabilitiesApi(defaultClient);
    String planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
    try {
      LiabilitiesModel result = apiInstance.liabilitiesGetByPlanid(planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiabilitiesApi#liabilitiesGetByPlanid");
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

[**LiabilitiesModel**](LiabilitiesModel.md)

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

