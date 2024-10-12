# UsagesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usagesListByInstancePool**](UsagesApi.md#usagesListByInstancePool) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/instancePools/{instancePoolName}/usages |  |


<a id="usagesListByInstancePool"></a>
# **usagesListByInstancePool**
> UsageListResult usagesListByInstancePool(resourceGroupName, instancePoolName, subscriptionId, apiVersion, expandChildren)



Gets all instance pool usage metrics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    UsagesApi apiInstance = new UsagesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String instancePoolName = "instancePoolName_example"; // String | The name of the instance pool to be retrieved.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    Boolean expandChildren = true; // Boolean | Optional request parameter to include managed instance usages within the instance pool.
    try {
      UsageListResult result = apiInstance.usagesListByInstancePool(resourceGroupName, instancePoolName, subscriptionId, apiVersion, expandChildren);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsagesApi#usagesListByInstancePool");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **instancePoolName** | **String**| The name of the instance pool to be retrieved. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **expandChildren** | **Boolean**| Optional request parameter to include managed instance usages within the instance pool. | [optional] |

### Return type

[**UsageListResult**](UsageListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the instance pool usages. |  -  |
| **0** | *** Error Responses: ***   * 400 InstancePoolWrongUsageName - Request for an instance pool&#39;s usage has an unsupported usage name   * 400 InstancePoolManagedInstanceInfoUnavailable - Information for managed instances inside this instance pool is not available   * 404 InstancePoolNotFound - An instance pool cannot be found |  -  |

