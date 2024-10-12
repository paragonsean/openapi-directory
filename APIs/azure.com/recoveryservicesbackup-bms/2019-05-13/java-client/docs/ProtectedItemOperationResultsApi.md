# ProtectedItemOperationResultsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protectedItemOperationResultsGet**](ProtectedItemOperationResultsApi.md#protectedItemOperationResultsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/operationResults/{operationId} |  |


<a id="protectedItemOperationResultsGet"></a>
# **protectedItemOperationResultsGet**
> ProtectedItemResource protectedItemOperationResultsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, operationId)



Fetches the result of any operation on the backup item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtectedItemOperationResultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProtectedItemOperationResultsApi apiInstance = new ProtectedItemOperationResultsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name associated with the backup item.
    String containerName = "containerName_example"; // String | Container name associated with the backup item.
    String protectedItemName = "protectedItemName_example"; // String | Backup item name whose details are to be fetched.
    String operationId = "operationId_example"; // String | OperationID which represents the operation whose result needs to be fetched.
    try {
      ProtectedItemResource result = apiInstance.protectedItemOperationResultsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, operationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtectedItemOperationResultsApi#protectedItemOperationResultsGet");
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
| **protectedItemName** | **String**| Backup item name whose details are to be fetched. | |
| **operationId** | **String**| OperationID which represents the operation whose result needs to be fetched. | |

### Return type

[**ProtectedItemResource**](ProtectedItemResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **204** | NoContent |  -  |

