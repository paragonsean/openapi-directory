# AggregatedCostApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**aggregatedCostGetByManagementGroup**](AggregatedCostApi.md#aggregatedCostGetByManagementGroup) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Consumption/aggregatedcost |  |
| [**aggregatedCostGetForBillingPeriodByManagementGroup**](AggregatedCostApi.md#aggregatedCostGetForBillingPeriodByManagementGroup) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}/Microsoft.Consumption/aggregatedcost |  |


<a id="aggregatedCostGetByManagementGroup"></a>
# **aggregatedCostGetByManagementGroup**
> ManagementGroupAggregatedCostResult aggregatedCostGetByManagementGroup(managementGroupId, apiVersion)



Provides the aggregate cost of a management group and all child management groups by current billing period.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AggregatedCostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AggregatedCostApi apiInstance = new AggregatedCostApi(defaultClient);
    String managementGroupId = "managementGroupId_example"; // String | Azure Management Group ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-06-30.
    try {
      ManagementGroupAggregatedCostResult result = apiInstance.aggregatedCostGetByManagementGroup(managementGroupId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AggregatedCostApi#aggregatedCostGetByManagementGroup");
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
| **managementGroupId** | **String**| Azure Management Group ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-06-30. | |

### Return type

[**ManagementGroupAggregatedCostResult**](ManagementGroupAggregatedCostResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="aggregatedCostGetForBillingPeriodByManagementGroup"></a>
# **aggregatedCostGetForBillingPeriodByManagementGroup**
> ManagementGroupAggregatedCostResult aggregatedCostGetForBillingPeriodByManagementGroup(managementGroupId, billingPeriodName, apiVersion)



Provides the aggregate cost of a management group and all child management groups by specified billing period

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AggregatedCostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AggregatedCostApi apiInstance = new AggregatedCostApi(defaultClient);
    String managementGroupId = "managementGroupId_example"; // String | Azure Management Group ID.
    String billingPeriodName = "billingPeriodName_example"; // String | Billing Period Name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-06-30.
    try {
      ManagementGroupAggregatedCostResult result = apiInstance.aggregatedCostGetForBillingPeriodByManagementGroup(managementGroupId, billingPeriodName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AggregatedCostApi#aggregatedCostGetForBillingPeriodByManagementGroup");
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
| **managementGroupId** | **String**| Azure Management Group ID. | |
| **billingPeriodName** | **String**| Billing Period Name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-06-30. | |

### Return type

[**ManagementGroupAggregatedCostResult**](ManagementGroupAggregatedCostResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

