# ItemLevelRecoveryConnectionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**itemLevelRecoveryConnectionsProvision**](ItemLevelRecoveryConnectionsApi.md#itemLevelRecoveryConnectionsProvision) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId}/provisionInstantItemRecovery |  |
| [**itemLevelRecoveryConnectionsRevoke**](ItemLevelRecoveryConnectionsApi.md#itemLevelRecoveryConnectionsRevoke) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId}/revokeInstantItemRecovery |  |


<a id="itemLevelRecoveryConnectionsProvision"></a>
# **itemLevelRecoveryConnectionsProvision**
> itemLevelRecoveryConnectionsProvision(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId, parameters)



Provisions a script which invokes an iSCSI connection to the backup data. Executing this script opens a file  explorer displaying all the recoverable files and folders. This is an asynchronous operation. To know the status of  provisioning, call GetProtectedItemOperationResult API.

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
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name associated with the backed up items.
    String containerName = "containerName_example"; // String | Container name associated with the backed up items.
    String protectedItemName = "protectedItemName_example"; // String | Backed up item name whose files/folders are to be restored.
    String recoveryPointId = "recoveryPointId_example"; // String | Recovery point ID which represents backed up data. iSCSI connection will be provisioned  for this backed up data.
    ILRRequestResource parameters = new ILRRequestResource(); // ILRRequestResource | resource ILR request
    try {
      apiInstance.itemLevelRecoveryConnectionsProvision(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId, parameters);
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
| **apiVersion** | **String**| Client Api Version. | |
| **vaultName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **fabricName** | **String**| Fabric name associated with the backed up items. | |
| **containerName** | **String**| Container name associated with the backed up items. | |
| **protectedItemName** | **String**| Backed up item name whose files/folders are to be restored. | |
| **recoveryPointId** | **String**| Recovery point ID which represents backed up data. iSCSI connection will be provisioned  for this backed up data. | |
| **parameters** | [**ILRRequestResource**](ILRRequestResource.md)| resource ILR request | |

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
| **202** | Accepted |  -  |

<a id="itemLevelRecoveryConnectionsRevoke"></a>
# **itemLevelRecoveryConnectionsRevoke**
> itemLevelRecoveryConnectionsRevoke(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId)



Revokes an iSCSI connection which can be used to download a script. Executing this script opens a file explorer  displaying all recoverable files and folders. This is an asynchronous operation.

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
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name associated with the backed up items.
    String containerName = "containerName_example"; // String | Container name associated with the backed up items.
    String protectedItemName = "protectedItemName_example"; // String | Backed up item name whose files/folders are to be restored.
    String recoveryPointId = "recoveryPointId_example"; // String | Recovery point ID which represents backed up data. iSCSI connection will be revoked for  this backed up data.
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
| **apiVersion** | **String**| Client Api Version. | |
| **vaultName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **fabricName** | **String**| Fabric name associated with the backed up items. | |
| **containerName** | **String**| Container name associated with the backed up items. | |
| **protectedItemName** | **String**| Backed up item name whose files/folders are to be restored. | |
| **recoveryPointId** | **String**| Recovery point ID which represents backed up data. iSCSI connection will be revoked for  this backed up data. | |

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
| **202** | Accepted |  -  |

