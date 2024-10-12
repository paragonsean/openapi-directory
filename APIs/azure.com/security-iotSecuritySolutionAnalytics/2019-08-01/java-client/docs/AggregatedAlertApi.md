# AggregatedAlertApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**iotSecuritySolutionsAnalyticsAggregatedAlertDismiss**](AggregatedAlertApi.md#iotSecuritySolutionsAnalyticsAggregatedAlertDismiss) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default/aggregatedAlerts/{aggregatedAlertName}/dismiss |  |
| [**iotSecuritySolutionsAnalyticsAggregatedAlertGet**](AggregatedAlertApi.md#iotSecuritySolutionsAnalyticsAggregatedAlertGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default/aggregatedAlerts/{aggregatedAlertName} |  |
| [**iotSecuritySolutionsAnalyticsAggregatedAlertList**](AggregatedAlertApi.md#iotSecuritySolutionsAnalyticsAggregatedAlertList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default/aggregatedAlerts |  |


<a id="iotSecuritySolutionsAnalyticsAggregatedAlertDismiss"></a>
# **iotSecuritySolutionsAnalyticsAggregatedAlertDismiss**
> iotSecuritySolutionsAnalyticsAggregatedAlertDismiss(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedAlertName)



Use this method to dismiss an aggregated IoT Security Solution Alert.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AggregatedAlertApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AggregatedAlertApi apiInstance = new AggregatedAlertApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String solutionName = "solutionName_example"; // String | The name of the IoT Security solution.
    String aggregatedAlertName = "aggregatedAlertName_example"; // String | Identifier of the aggregated alert.
    try {
      apiInstance.iotSecuritySolutionsAnalyticsAggregatedAlertDismiss(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedAlertName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AggregatedAlertApi#iotSecuritySolutionsAnalyticsAggregatedAlertDismiss");
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
| **aggregatedAlertName** | **String**| Identifier of the aggregated alert. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This aggregate alert is permanently dismissed. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="iotSecuritySolutionsAnalyticsAggregatedAlertGet"></a>
# **iotSecuritySolutionsAnalyticsAggregatedAlertGet**
> IoTSecurityAggregatedAlert iotSecuritySolutionsAnalyticsAggregatedAlertGet(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedAlertName)



Use this method to get a single the aggregated alert of yours IoT Security solution. This aggregation is performed by alert name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AggregatedAlertApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AggregatedAlertApi apiInstance = new AggregatedAlertApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String solutionName = "solutionName_example"; // String | The name of the IoT Security solution.
    String aggregatedAlertName = "aggregatedAlertName_example"; // String | Identifier of the aggregated alert.
    try {
      IoTSecurityAggregatedAlert result = apiInstance.iotSecuritySolutionsAnalyticsAggregatedAlertGet(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedAlertName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AggregatedAlertApi#iotSecuritySolutionsAnalyticsAggregatedAlertGet");
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
| **aggregatedAlertName** | **String**| Identifier of the aggregated alert. | |

### Return type

[**IoTSecurityAggregatedAlert**](IoTSecurityAggregatedAlert.md)

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

<a id="iotSecuritySolutionsAnalyticsAggregatedAlertList"></a>
# **iotSecuritySolutionsAnalyticsAggregatedAlertList**
> IoTSecurityAggregatedAlertList iotSecuritySolutionsAnalyticsAggregatedAlertList(apiVersion, subscriptionId, resourceGroupName, solutionName, $top)



Use this method to get the aggregated alert list of yours IoT Security solution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AggregatedAlertApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AggregatedAlertApi apiInstance = new AggregatedAlertApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String solutionName = "solutionName_example"; // String | The name of the IoT Security solution.
    Integer $top = 56; // Integer | Number of results to retrieve.
    try {
      IoTSecurityAggregatedAlertList result = apiInstance.iotSecuritySolutionsAnalyticsAggregatedAlertList(apiVersion, subscriptionId, resourceGroupName, solutionName, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AggregatedAlertApi#iotSecuritySolutionsAnalyticsAggregatedAlertList");
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

[**IoTSecurityAggregatedAlertList**](IoTSecurityAggregatedAlertList.md)

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

