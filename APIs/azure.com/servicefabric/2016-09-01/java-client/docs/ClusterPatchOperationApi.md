# ClusterPatchOperationApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**clustersUpdate**](ClusterPatchOperationApi.md#clustersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName} |  |


<a id="clustersUpdate"></a>
# **clustersUpdate**
> Cluster clustersUpdate(resourceGroupName, clusterName, apiVersion, subscriptionId, parameters)



Update cluster configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterPatchOperationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ClusterPatchOperationApi apiInstance = new ClusterPatchOperationApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the resource belongs or get created
    String clusterName = "clusterName_example"; // String | The name of the cluster resource
    String apiVersion = "apiVersion_example"; // String | The version of the ServiceFabric resource provider api
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
    ClusterUpdateParameters parameters = new ClusterUpdateParameters(); // ClusterUpdateParameters | The parameters which contains the property value and property name which used to update the cluster configuration
    try {
      Cluster result = apiInstance.clustersUpdate(resourceGroupName, clusterName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterPatchOperationApi#clustersUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group to which the resource belongs or get created | |
| **clusterName** | **String**| The name of the cluster resource | |
| **apiVersion** | **String**| The version of the ServiceFabric resource provider api | |
| **subscriptionId** | **String**| The customer subscription identifier | |
| **parameters** | [**ClusterUpdateParameters**](ClusterUpdateParameters.md)| The parameters which contains the property value and property name which used to update the cluster configuration | |

### Return type

[**Cluster**](Cluster.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Cluster updated successfully |  -  |
| **202** | Accepted - Update request accepted; the operation will complete asynchronously. |  -  |
| **0** | Error |  -  |

