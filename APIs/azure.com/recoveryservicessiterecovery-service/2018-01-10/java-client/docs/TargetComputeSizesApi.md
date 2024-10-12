# TargetComputeSizesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**targetComputeSizesListByReplicationProtectedItems**](TargetComputeSizesApi.md#targetComputeSizesListByReplicationProtectedItems) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/targetComputeSizes | Gets the list of target compute sizes for the replication protected item. |


<a id="targetComputeSizesListByReplicationProtectedItems"></a>
# **targetComputeSizesListByReplicationProtectedItems**
> TargetComputeSizeCollection targetComputeSizesListByReplicationProtectedItems(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName)

Gets the list of target compute sizes for the replication protected item.

Lists the available target compute sizes for a replication protected item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TargetComputeSizesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TargetComputeSizesApi apiInstance = new TargetComputeSizesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | protection container name.
    String replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
    try {
      TargetComputeSizeCollection result = apiInstance.targetComputeSizesListByReplicationProtectedItems(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TargetComputeSizesApi#targetComputeSizesListByReplicationProtectedItems");
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
| **apiVersion** | **String**| Client Api Version. | |
| **resourceName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **fabricName** | **String**| Fabric name. | |
| **protectionContainerName** | **String**| protection container name. | |
| **replicatedProtectedItemName** | **String**| Replication protected item name. | |

### Return type

[**TargetComputeSizeCollection**](TargetComputeSizeCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

