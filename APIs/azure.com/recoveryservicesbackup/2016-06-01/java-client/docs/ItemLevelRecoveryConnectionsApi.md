# ItemLevelRecoveryConnectionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**itemLevelRecoveryConnectionsProvision**](ItemLevelRecoveryConnectionsApi.md#itemLevelRecoveryConnectionsProvision) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId}/provisionInstantItemRecovery |  |
| [**itemLevelRecoveryConnectionsRevoke**](ItemLevelRecoveryConnectionsApi.md#itemLevelRecoveryConnectionsRevoke) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId}/revokeInstantItemRecovery |  |


<a id="itemLevelRecoveryConnectionsProvision"></a>
# **itemLevelRecoveryConnectionsProvision**
> itemLevelRecoveryConnectionsProvision(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId, resourceILRRequest)



Provisions a script which invokes an iSCSI connection to the backup data. Executing this script opens File Explorer which displays the recoverable files and folders. This is an asynchronous operation. To get the provisioning status, call GetProtectedItemOperationResult API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItemLevelRecoveryConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ItemLevelRecoveryConnectionsApi apiInstance = new ItemLevelRecoveryConnectionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String fabricName = "fabricName_example"; // String | The fabric name associated with the backup items.
    String containerName = "containerName_example"; // String | The container name associated with the backup items.
    String protectedItemName = "protectedItemName_example"; // String | The name of the backup item whose files or folders are to be restored.
    String recoveryPointId = "recoveryPointId_example"; // String | The recovery point ID for backup data. The iSCSI connection will be provisioned for this backup data.
    ILRRequestResource resourceILRRequest = new ILRRequestResource(); // ILRRequestResource | The resource Item Level Recovery (ILR) request.
    try {
      apiInstance.itemLevelRecoveryConnectionsProvision(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId, resourceILRRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItemLevelRecoveryConnectionsApi#itemLevelRecoveryConnectionsProvision");
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
| **fabricName** | **String**| The fabric name associated with the backup items. | |
| **containerName** | **String**| The container name associated with the backup items. | |
| **protectedItemName** | **String**| The name of the backup item whose files or folders are to be restored. | |
| **recoveryPointId** | **String**| The recovery point ID for backup data. The iSCSI connection will be provisioned for this backup data. | |
| **resourceILRRequest** | [**ILRRequestResource**](ILRRequestResource.md)| The resource Item Level Recovery (ILR) request. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted. |  -  |

<a id="itemLevelRecoveryConnectionsRevoke"></a>
# **itemLevelRecoveryConnectionsRevoke**
> itemLevelRecoveryConnectionsRevoke(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId)



Revokes an iSCSI connection which can be used to download a script. Executing this script opens a file explorer displaying all recoverable files and folders. This is an asynchronous operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItemLevelRecoveryConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ItemLevelRecoveryConnectionsApi apiInstance = new ItemLevelRecoveryConnectionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String fabricName = "fabricName_example"; // String | The fabric name associated with the backup items. The value allowed is Azure.
    String containerName = "containerName_example"; // String | The container name associated with the backup items.
    String protectedItemName = "protectedItemName_example"; // String | The name of the backup items whose files or folders will be restored.
    String recoveryPointId = "recoveryPointId_example"; // String | The string that identifies the recovery point. The iSCSI connection will be revoked for this protected data.
    try {
      apiInstance.itemLevelRecoveryConnectionsRevoke(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItemLevelRecoveryConnectionsApi#itemLevelRecoveryConnectionsRevoke");
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
| **fabricName** | **String**| The fabric name associated with the backup items. The value allowed is Azure. | |
| **containerName** | **String**| The container name associated with the backup items. | |
| **protectedItemName** | **String**| The name of the backup items whose files or folders will be restored. | |
| **recoveryPointId** | **String**| The string that identifies the recovery point. The iSCSI connection will be revoked for this protected data. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The revocation was accepted. |  -  |

