# AggregatedRecommendationApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**iotSecuritySolutionsAnalyticsRecommendationGet**](AggregatedRecommendationApi.md#iotSecuritySolutionsAnalyticsRecommendationGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default/aggregatedRecommendations/{aggregatedRecommendationName} |  |
| [**iotSecuritySolutionsAnalyticsRecommendationList**](AggregatedRecommendationApi.md#iotSecuritySolutionsAnalyticsRecommendationList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default/aggregatedRecommendations |  |


<a id="iotSecuritySolutionsAnalyticsRecommendationGet"></a>
# **iotSecuritySolutionsAnalyticsRecommendationGet**
> IoTSecurityAggregatedRecommendation iotSecuritySolutionsAnalyticsRecommendationGet(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedRecommendationName)



Use this method to get the aggregated security analytics recommendation of yours IoT Security solution. This aggregation is performed by recommendation name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AggregatedRecommendationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AggregatedRecommendationApi apiInstance = new AggregatedRecommendationApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String solutionName = "solutionName_example"; // String | The name of the IoT Security solution.
    String aggregatedRecommendationName = "aggregatedRecommendationName_example"; // String | Name of the recommendation aggregated for this query.
    try {
      IoTSecurityAggregatedRecommendation result = apiInstance.iotSecuritySolutionsAnalyticsRecommendationGet(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedRecommendationName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AggregatedRecommendationApi#iotSecuritySolutionsAnalyticsRecommendationGet");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **solutionName** | **String**| The name of the IoT Security solution. | |
| **aggregatedRecommendationName** | **String**| Name of the recommendation aggregated for this query. | |

### Return type

[**IoTSecurityAggregatedRecommendation**](IoTSecurityAggregatedRecommendation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="iotSecuritySolutionsAnalyticsRecommendationList"></a>
# **iotSecuritySolutionsAnalyticsRecommendationList**
> IoTSecurityAggregatedRecommendationList iotSecuritySolutionsAnalyticsRecommendationList(apiVersion, subscriptionId, resourceGroupName, solutionName, $top)



Use this method to get the list of aggregated security analytics recommendations of yours IoT Security solution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AggregatedRecommendationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AggregatedRecommendationApi apiInstance = new AggregatedRecommendationApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String solutionName = "solutionName_example"; // String | The name of the IoT Security solution.
    Integer $top = 56; // Integer | Number of results to retrieve.
    try {
      IoTSecurityAggregatedRecommendationList result = apiInstance.iotSecuritySolutionsAnalyticsRecommendationList(apiVersion, subscriptionId, resourceGroupName, solutionName, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AggregatedRecommendationApi#iotSecuritySolutionsAnalyticsRecommendationList");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **solutionName** | **String**| The name of the IoT Security solution. | |
| **$top** | **Integer**| Number of results to retrieve. | [optional] |

### Return type

[**IoTSecurityAggregatedRecommendationList**](IoTSecurityAggregatedRecommendationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

