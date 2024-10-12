# TopQueryStatisticsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**topQueryStatisticsGet**](TopQueryStatisticsApi.md#topQueryStatisticsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMariaDB/servers/{serverName}/topQueryStatistics/{queryStatisticId} |  |
| [**topQueryStatisticsListByServer**](TopQueryStatisticsApi.md#topQueryStatisticsListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMariaDB/servers/{serverName}/topQueryStatistics |  |


<a id="topQueryStatisticsGet"></a>
# **topQueryStatisticsGet**
> QueryStatistic topQueryStatisticsGet(apiVersion, subscriptionId, resourceGroupName, serverName, queryStatisticId)



Retrieve the query statistic for specified identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopQueryStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TopQueryStatisticsApi apiInstance = new TopQueryStatisticsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String serverName = "serverName_example"; // String | The name of the server.
    String queryStatisticId = "queryStatisticId_example"; // String | The Query Statistic identifier.
    try {
      QueryStatistic result = apiInstance.topQueryStatisticsGet(apiVersion, subscriptionId, resourceGroupName, serverName, queryStatisticId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopQueryStatisticsApi#topQueryStatisticsGet");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **serverName** | **String**| The name of the server. | |
| **queryStatisticId** | **String**| The Query Statistic identifier. | |

### Return type

[**QueryStatistic**](QueryStatistic.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="topQueryStatisticsListByServer"></a>
# **topQueryStatisticsListByServer**
> TopQueryStatisticsResultList topQueryStatisticsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName, parameters)



Retrieve the Query-Store top queries for specified metric and aggregation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopQueryStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TopQueryStatisticsApi apiInstance = new TopQueryStatisticsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String serverName = "serverName_example"; // String | The name of the server.
    TopQueryStatisticsInput parameters = new TopQueryStatisticsInput(); // TopQueryStatisticsInput | The required parameters for retrieving top query statistics.
    try {
      TopQueryStatisticsResultList result = apiInstance.topQueryStatisticsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopQueryStatisticsApi#topQueryStatisticsListByServer");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **serverName** | **String**| The name of the server. | |
| **parameters** | [**TopQueryStatisticsInput**](TopQueryStatisticsInput.md)| The required parameters for retrieving top query statistics. | |

### Return type

[**TopQueryStatisticsResultList**](TopQueryStatisticsResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

