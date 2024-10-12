# LifestyleAssetsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lifestyleAssetsGetByIdPlanid**](LifestyleAssetsApi.md#lifestyleAssetsGetByIdPlanid) | **GET** /api/LifestyleAssets/{id} | Retrieve lifestyle assets |
| [**lifestyleAssetsGetByPlanid**](LifestyleAssetsApi.md#lifestyleAssetsGetByPlanid) | **GET** /api/LifestyleAssets | Retrieve lifestyle assets |


<a id="lifestyleAssetsGetByIdPlanid"></a>
# **lifestyleAssetsGetByIdPlanid**
> LifestyleAssetModel lifestyleAssetsGetByIdPlanid(id, planId)

Retrieve lifestyle assets

This operation retrieves a lifestyle asset from the plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifestyleAssetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    LifestyleAssetsApi apiInstance = new LifestyleAssetsApi(defaultClient);
    Integer id = 56; // Integer | ID of lifestyle asset to retrieve
    String planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
    try {
      LifestyleAssetModel result = apiInstance.lifestyleAssetsGetByIdPlanid(id, planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifestyleAssetsApi#lifestyleAssetsGetByIdPlanid");
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
| **id** | **Integer**| ID of lifestyle asset to retrieve | |
| **planId** | **String**| Id of the plan to retrieve data from (e.g. 1001-11-3). | |

### Return type

[**LifestyleAssetModel**](LifestyleAssetModel.md)

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

<a id="lifestyleAssetsGetByPlanid"></a>
# **lifestyleAssetsGetByPlanid**
> LifestyleAssetsModel lifestyleAssetsGetByPlanid(planId)

Retrieve lifestyle assets

This operation retrieves a list of all of the lifestyle assets in the plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifestyleAssetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    LifestyleAssetsApi apiInstance = new LifestyleAssetsApi(defaultClient);
    String planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
    try {
      LifestyleAssetsModel result = apiInstance.lifestyleAssetsGetByPlanid(planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifestyleAssetsApi#lifestyleAssetsGetByPlanid");
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

[**LifestyleAssetsModel**](LifestyleAssetsModel.md)

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

