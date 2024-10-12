# FailoverDatabasesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**databasesFailover**](FailoverDatabasesApi.md#databasesFailover) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/failover |  |


<a id="databasesFailover"></a>
# **databasesFailover**
> databasesFailover(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion, replicaType)



Failovers a database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FailoverDatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    FailoverDatabasesApi apiInstance = new FailoverDatabasesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database to failover.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String replicaType = "Primary"; // String | The type of replica to be failed over.
    try {
      apiInstance.databasesFailover(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion, replicaType);
    } catch (ApiException e) {
      System.err.println("Exception when calling FailoverDatabasesApi#databasesFailover");
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
| **databaseName** | **String**| The name of the database to failover. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **replicaType** | **String**| The type of replica to be failed over. | [optional] [enum: Primary, ReadableSecondary] |

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
| **200** | Successfully completed database failover. |  -  |
| **202** | Database failover is in progress. |  -  |
| **0** | *** Error Responses: ***   * 400 ManagementServiceFeatureDisabled - User attempted to use a feature which is disabled.   * 400 DatabaseFailoverThrottled - There was a recent failover on the database or pool if database belongs in an elastic pool.   * 400 DatabaseFailoverNotSupportedOnSKU - This type of customer initiated failover is not supported on the given SKU.   * 409 ManagementServiceDatabaseBusy - Database &#39;{0}&#39; is busy with another operation. Please try your operation later.   * 409 DatabaseNotInStateToFailover - The database is currently in a state such that failover cannot be issued. |  -  |

