# WaitStatisticsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**waitStatisticsGet**](WaitStatisticsApi.md#waitStatisticsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/waitStatistics/{waitStatisticsId} |  |
| [**waitStatisticsListByServer**](WaitStatisticsApi.md#waitStatisticsListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/waitStatistics |  |


<a id="waitStatisticsGet"></a>
# **waitStatisticsGet**
> WaitStatistic waitStatisticsGet(apiVersion, subscriptionId, resourceGroupName, serverName, waitStatisticsId)



Retrieve wait statistics for specified identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WaitStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WaitStatisticsApi apiInstance = new WaitStatisticsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String serverName = "serverName_example"; // String | The name of the server.
    String waitStatisticsId = "waitStatisticsId_example"; // String | The Wait Statistic identifier.
    try {
      WaitStatistic result = apiInstance.waitStatisticsGet(apiVersion, subscriptionId, resourceGroupName, serverName, waitStatisticsId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WaitStatisticsApi#waitStatisticsGet");
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
| **waitStatisticsId** | **String**| The Wait Statistic identifier. | |

### Return type

[**WaitStatistic**](WaitStatistic.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="waitStatisticsListByServer"></a>
# **waitStatisticsListByServer**
> WaitStatisticsResultList waitStatisticsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName, parameters)



Retrieve wait statistics for specified aggregation window.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WaitStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WaitStatisticsApi apiInstance = new WaitStatisticsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String serverName = "serverName_example"; // String | The name of the server.
    WaitStatisticsInput parameters = new WaitStatisticsInput(); // WaitStatisticsInput | The required parameters for retrieving wait statistics.
    try {
      WaitStatisticsResultList result = apiInstance.waitStatisticsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WaitStatisticsApi#waitStatisticsListByServer");
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
| **parameters** | [**WaitStatisticsInput**](WaitStatisticsInput.md)| The required parameters for retrieving wait statistics. | |

### Return type

[**WaitStatisticsResultList**](WaitStatisticsResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

