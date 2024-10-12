# PromoteApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**scriptExecutionHistoryPromote**](PromoteApi.md#scriptExecutionHistoryPromote) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/scriptExecutionHistory/{scriptExecutionId}/promote |  |


<a id="scriptExecutionHistoryPromote"></a>
# **scriptExecutionHistoryPromote**
> scriptExecutionHistoryPromote(subscriptionId, resourceGroupName, clusterName, scriptExecutionId, apiVersion)



Promotes the specified ad-hoc script execution to a persisted script.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PromoteApi apiInstance = new PromoteApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster.
    String scriptExecutionId = "scriptExecutionId_example"; // String | The script execution Id
    String apiVersion = "apiVersion_example"; // String | The HDInsight client API Version.
    try {
      apiInstance.scriptExecutionHistoryPromote(subscriptionId, resourceGroupName, clusterName, scriptExecutionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromoteApi#scriptExecutionHistoryPromote");
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

null (empty response body)

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

