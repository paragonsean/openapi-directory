# BackupsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**backupsTrigger**](BackupsApi.md#backupsTrigger) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/backup |  |


<a id="backupsTrigger"></a>
# **backupsTrigger**
> backupsTrigger(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, parameters)



Triggers backup for specified backed up item. This is an asynchronous operation. To know the status of the  operation, call GetProtectedItemOperationResult API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BackupsApi apiInstance = new BackupsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name associated with the backup item.
    String containerName = "containerName_example"; // String | Container name associated with the backup item.
    String protectedItemName = "protectedItemName_example"; // String | Backup item for which backup needs to be triggered.
    BackupRequestResource parameters = new BackupRequestResource(); // BackupRequestResource | resource backup request
    try {
      apiInstance.backupsTrigger(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupsApi#backupsTrigger");
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
| **fabricName** | **String**| Fabric name associated with the backup item. | |
| **containerName** | **String**| Container name associated with the backup item. | |
| **protectedItemName** | **String**| Backup item for which backup needs to be triggered. | |
| **parameters** | [**BackupRequestResource**](BackupRequestResource.md)| resource backup request | |

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

