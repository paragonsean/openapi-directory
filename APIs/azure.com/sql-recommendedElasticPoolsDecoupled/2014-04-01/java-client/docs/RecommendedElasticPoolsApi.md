# RecommendedElasticPoolsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**recommendedElasticPoolsGet**](RecommendedElasticPoolsApi.md#recommendedElasticPoolsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/recommendedElasticPools/{recommendedElasticPoolName} |  |
| [**recommendedElasticPoolsListByServer**](RecommendedElasticPoolsApi.md#recommendedElasticPoolsListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/recommendedElasticPools |  |
| [**recommendedElasticPoolsListMetrics**](RecommendedElasticPoolsApi.md#recommendedElasticPoolsListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/recommendedElasticPools/{recommendedElasticPoolName}/metrics |  |


<a id="recommendedElasticPoolsGet"></a>
# **recommendedElasticPoolsGet**
> RecommendedElasticPool recommendedElasticPoolsGet(apiVersion, subscriptionId, resourceGroupName, serverName, recommendedElasticPoolName)



Gets a recommended elastic pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecommendedElasticPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    RecommendedElasticPoolsApi apiInstance = new RecommendedElasticPoolsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String recommendedElasticPoolName = "recommendedElasticPoolName_example"; // String | The name of the recommended elastic pool to be retrieved.
    try {
      RecommendedElasticPool result = apiInstance.recommendedElasticPoolsGet(apiVersion, subscriptionId, resourceGroupName, serverName, recommendedElasticPoolName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendedElasticPoolsApi#recommendedElasticPoolsGet");
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
| **recommendedElasticPoolName** | **String**| The name of the recommended elastic pool to be retrieved. | |

### Return type

[**RecommendedElasticPool**](RecommendedElasticPool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recommendedElasticPoolsListByServer"></a>
# **recommendedElasticPoolsListByServer**
> RecommendedElasticPoolListResult recommendedElasticPoolsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName)



Returns recommended elastic pools.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecommendedElasticPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    RecommendedElasticPoolsApi apiInstance = new RecommendedElasticPoolsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    try {
      RecommendedElasticPoolListResult result = apiInstance.recommendedElasticPoolsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendedElasticPoolsApi#recommendedElasticPoolsListByServer");
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

### Return type

[**RecommendedElasticPoolListResult**](RecommendedElasticPoolListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recommendedElasticPoolsListMetrics"></a>
# **recommendedElasticPoolsListMetrics**
> RecommendedElasticPoolListMetricsResult recommendedElasticPoolsListMetrics(apiVersion, subscriptionId, resourceGroupName, serverName, recommendedElasticPoolName)



Returns recommended elastic pool metrics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecommendedElasticPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    RecommendedElasticPoolsApi apiInstance = new RecommendedElasticPoolsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String recommendedElasticPoolName = "recommendedElasticPoolName_example"; // String | The name of the recommended elastic pool to be retrieved.
    try {
      RecommendedElasticPoolListMetricsResult result = apiInstance.recommendedElasticPoolsListMetrics(apiVersion, subscriptionId, resourceGroupName, serverName, recommendedElasticPoolName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendedElasticPoolsApi#recommendedElasticPoolsListMetrics");
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
| **recommendedElasticPoolName** | **String**| The name of the recommended elastic pool to be retrieved. | |

### Return type

[**RecommendedElasticPoolListMetricsResult**](RecommendedElasticPoolListMetricsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

