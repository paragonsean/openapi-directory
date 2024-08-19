# FailoverElasticPoolsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**elasticPoolsFailover**](FailoverElasticPoolsApi.md#elasticPoolsFailover) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools/{elasticPoolName}/failover |  |


<a id="elasticPoolsFailover"></a>
# **elasticPoolsFailover**
> elasticPoolsFailover(resourceGroupName, serverName, elasticPoolName, subscriptionId, apiVersion)



Failovers an elastic pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FailoverElasticPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    FailoverElasticPoolsApi apiInstance = new FailoverElasticPoolsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String elasticPoolName = "elasticPoolName_example"; // String | The name of the elastic pool to failover.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.elasticPoolsFailover(resourceGroupName, serverName, elasticPoolName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling FailoverElasticPoolsApi#elasticPoolsFailover");
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
| **serverName** | **String**| The name of the server. | |
| **elasticPoolName** | **String**| The name of the elastic pool to failover. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully completed elastic pool failover. |  -  |
| **202** | Elastic pool failover is in progress. |  -  |
| **0** | *** Error Responses: ***   * 400 ManagementServiceFeatureDisabled - User attempted to use a feature which is disabled.   * 400 ElasticPoolFailoverThrottled - There was a recent failover on the elastic pool.   * 400 ElasticPoolFailoverNotSupportedOnSKU - This type of customer initiated failover is not supported on the given SKU.   * 409 ManagementServiceDatabaseBusy - Database &#39;{0}&#39; is busy with another operation. Please try your operation later.   * 409 ElasticPoolNotInStateToFailover - The elastic pool or a database within the elastic pool is currently in a state such that failover cannot be issued. |  -  |

