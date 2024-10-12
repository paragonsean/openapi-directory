# IoTSecuritySolutionAnalyticsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**iotSecuritySolutionAnalyticsGet**](IoTSecuritySolutionAnalyticsApi.md#iotSecuritySolutionAnalyticsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default |  |
| [**iotSecuritySolutionAnalyticsList**](IoTSecuritySolutionAnalyticsApi.md#iotSecuritySolutionAnalyticsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels |  |


<a id="iotSecuritySolutionAnalyticsGet"></a>
# **iotSecuritySolutionAnalyticsGet**
> IoTSecuritySolutionAnalyticsModel iotSecuritySolutionAnalyticsGet(apiVersion, subscriptionId, resourceGroupName, solutionName)



Use this method to get IoT Security Analytics metrics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IoTSecuritySolutionAnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IoTSecuritySolutionAnalyticsApi apiInstance = new IoTSecuritySolutionAnalyticsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String solutionName = "solutionName_example"; // String | The name of the IoT Security solution.
    try {
      IoTSecuritySolutionAnalyticsModel result = apiInstance.iotSecuritySolutionAnalyticsGet(apiVersion, subscriptionId, resourceGroupName, solutionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IoTSecuritySolutionAnalyticsApi#iotSecuritySolutionAnalyticsGet");
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

### Return type

[**IoTSecuritySolutionAnalyticsModel**](IoTSecuritySolutionAnalyticsModel.md)

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

<a id="iotSecuritySolutionAnalyticsList"></a>
# **iotSecuritySolutionAnalyticsList**
> IoTSecuritySolutionAnalyticsModelList iotSecuritySolutionAnalyticsList(apiVersion, subscriptionId, resourceGroupName, solutionName)



Use this method to get IoT security Analytics metrics in an array.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IoTSecuritySolutionAnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IoTSecuritySolutionAnalyticsApi apiInstance = new IoTSecuritySolutionAnalyticsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String solutionName = "solutionName_example"; // String | The name of the IoT Security solution.
    try {
      IoTSecuritySolutionAnalyticsModelList result = apiInstance.iotSecuritySolutionAnalyticsList(apiVersion, subscriptionId, resourceGroupName, solutionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IoTSecuritySolutionAnalyticsApi#iotSecuritySolutionAnalyticsList");
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

### Return type

[**IoTSecuritySolutionAnalyticsModelList**](IoTSecuritySolutionAnalyticsModelList.md)

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

