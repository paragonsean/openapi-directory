# ElasticPoolsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**elasticPoolActivitiesListByElasticPool**](ElasticPoolsApi.md#elasticPoolActivitiesListByElasticPool) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools/{elasticPoolName}/elasticPoolActivity |  |
| [**elasticPoolDatabaseActivitiesListByElasticPool**](ElasticPoolsApi.md#elasticPoolDatabaseActivitiesListByElasticPool) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools/{elasticPoolName}/elasticPoolDatabaseActivity |  |


<a id="elasticPoolActivitiesListByElasticPool"></a>
# **elasticPoolActivitiesListByElasticPool**
> ElasticPoolActivityListResult elasticPoolActivitiesListByElasticPool(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName)



Returns elastic pool activities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ElasticPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ElasticPoolsApi apiInstance = new ElasticPoolsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String elasticPoolName = "elasticPoolName_example"; // String | The name of the elastic pool for which to get the current activity.
    try {
      ElasticPoolActivityListResult result = apiInstance.elasticPoolActivitiesListByElasticPool(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ElasticPoolsApi#elasticPoolActivitiesListByElasticPool");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **elasticPoolName** | **String**| The name of the elastic pool for which to get the current activity. | |

### Return type

[**ElasticPoolActivityListResult**](ElasticPoolActivityListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="elasticPoolDatabaseActivitiesListByElasticPool"></a>
# **elasticPoolDatabaseActivitiesListByElasticPool**
> ElasticPoolDatabaseActivityListResult elasticPoolDatabaseActivitiesListByElasticPool(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName)



Returns activity on databases inside of an elastic pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ElasticPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ElasticPoolsApi apiInstance = new ElasticPoolsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String elasticPoolName = "elasticPoolName_example"; // String | The name of the elastic pool.
    try {
      ElasticPoolDatabaseActivityListResult result = apiInstance.elasticPoolDatabaseActivitiesListByElasticPool(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ElasticPoolsApi#elasticPoolDatabaseActivitiesListByElasticPool");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **elasticPoolName** | **String**| The name of the elastic pool. | |

### Return type

[**ElasticPoolDatabaseActivityListResult**](ElasticPoolDatabaseActivityListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

