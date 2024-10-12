# ScriptExecutionHistoryApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**scriptActionsGetExecutionDetail**](ScriptExecutionHistoryApi.md#scriptActionsGetExecutionDetail) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/scriptExecutionHistory/{scriptExecutionId} |  |
| [**scriptExecutionHistoryListByCluster**](ScriptExecutionHistoryApi.md#scriptExecutionHistoryListByCluster) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/scriptExecutionHistory |  |


<a id="scriptActionsGetExecutionDetail"></a>
# **scriptActionsGetExecutionDetail**
> ScriptActionsGetExecutionDetail200Response scriptActionsGetExecutionDetail(subscriptionId, resourceGroupName, clusterName, scriptExecutionId, apiVersion)



Gets the script execution detail for the given script execution ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptExecutionHistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ScriptExecutionHistoryApi apiInstance = new ScriptExecutionHistoryApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster.
    String scriptExecutionId = "scriptExecutionId_example"; // String | The script execution Id
    String apiVersion = "apiVersion_example"; // String | The HDInsight client API Version.
    try {
      ScriptActionsGetExecutionDetail200Response result = apiInstance.scriptActionsGetExecutionDetail(subscriptionId, resourceGroupName, clusterName, scriptExecutionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptExecutionHistoryApi#scriptActionsGetExecutionDetail");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **clusterName** | **String**| The name of the cluster. | |
| **scriptExecutionId** | **String**| The script execution Id | |
| **apiVersion** | **String**| The HDInsight client API Version. | |

### Return type

[**ScriptActionsGetExecutionDetail200Response**](ScriptActionsGetExecutionDetail200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="scriptExecutionHistoryListByCluster"></a>
# **scriptExecutionHistoryListByCluster**
> ScriptActionExecutionHistoryList scriptExecutionHistoryListByCluster(subscriptionId, resourceGroupName, clusterName, apiVersion)



Lists all scripts&#39; execution history for the specified cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptExecutionHistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ScriptExecutionHistoryApi apiInstance = new ScriptExecutionHistoryApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster.
    String apiVersion = "apiVersion_example"; // String | The HDInsight client API Version.
    try {
      ScriptActionExecutionHistoryList result = apiInstance.scriptExecutionHistoryListByCluster(subscriptionId, resourceGroupName, clusterName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptExecutionHistoryApi#scriptExecutionHistoryListByCluster");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **clusterName** | **String**| The name of the cluster. | |
| **apiVersion** | **String**| The HDInsight client API Version. | |

### Return type

[**ScriptActionExecutionHistoryList**](ScriptActionExecutionHistoryList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

