# ProtectedItemOperationStatusesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protectedItemOperationStatusesGet**](ProtectedItemOperationStatusesApi.md#protectedItemOperationStatusesGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/operationsStatus/{operationId} |  |


<a id="protectedItemOperationStatusesGet"></a>
# **protectedItemOperationStatusesGet**
> OperationStatus protectedItemOperationStatusesGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, operationId)



Gets the status of an operation such as triggering a backup or restore. The status can be: In progress, Completed, or Failed. You can refer to the OperationStatus enum for all the possible states of the operation. Some operations create jobs. This method returns the list of jobs associated with the operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtectedItemOperationStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProtectedItemOperationStatusesApi apiInstance = new ProtectedItemOperationStatusesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String fabricName = "fabricName_example"; // String | The fabric name associated with the backup item.
    String containerName = "containerName_example"; // String | The container name associated with the backup item.
    String protectedItemName = "protectedItemName_example"; // String | The name of backup item used in this GET operation.
    String operationId = "operationId_example"; // String | The OperationID used in this GET operation.
    try {
      OperationStatus result = apiInstance.protectedItemOperationStatusesGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, operationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtectedItemOperationStatusesApi#protectedItemOperationStatusesGet");
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
| **apiVersion** | **String**| Client API version. | |
| **vaultName** | **String**| The name of the Recovery Services vault. | |
| **resourceGroupName** | **String**| The name of the resource group associated with the Recovery Services vault. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **fabricName** | **String**| The fabric name associated with the backup item. | |
| **containerName** | **String**| The container name associated with the backup item. | |
| **protectedItemName** | **String**| The name of backup item used in this GET operation. | |
| **operationId** | **String**| The OperationID used in this GET operation. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |

