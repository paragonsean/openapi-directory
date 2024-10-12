# RestoresApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**restoresTrigger**](RestoresApi.md#restoresTrigger) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId}/restore |  |


<a id="restoresTrigger"></a>
# **restoresTrigger**
> restoresTrigger(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId, parameters)



Restores the specified backed up data. This is an asynchronous operation. To know the status of this API call, use  GetProtectedItemOperationResult API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RestoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RestoresApi apiInstance = new RestoresApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name associated with the backed up items.
    String containerName = "containerName_example"; // String | Container name associated with the backed up items.
    String protectedItemName = "protectedItemName_example"; // String | Backed up item to be restored.
    String recoveryPointId = "recoveryPointId_example"; // String | Recovery point ID which represents the backed up data to be restored.
    RestoreRequestResource parameters = new RestoreRequestResource(); // RestoreRequestResource | resource restore request
    try {
      apiInstance.restoresTrigger(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling RestoresApi#restoresTrigger");
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
| **protectedItemName** | **String**| Backed up item to be restored. | |
| **recoveryPointId** | **String**| Recovery point ID which represents the backed up data to be restored. | |
| **parameters** | [**RestoreRequestResource**](RestoreRequestResource.md)| resource restore request | |

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

