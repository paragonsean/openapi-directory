# ProtectionContainerOperationResultsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protectionContainerOperationResultsGet**](ProtectionContainerOperationResultsApi.md#protectionContainerOperationResultsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/operationResults/{operationId} |  |


<a id="protectionContainerOperationResultsGet"></a>
# **protectionContainerOperationResultsGet**
> ProtectionContainerResource protectionContainerOperationResultsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, operationId)



Fetches the result of any operation on the container.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtectionContainerOperationResultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProtectionContainerOperationResultsApi apiInstance = new ProtectionContainerOperationResultsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name associated with the container.
    String containerName = "containerName_example"; // String | Container name whose information should be fetched.
    String operationId = "operationId_example"; // String | Operation ID which represents the operation whose result needs to be fetched.
    try {
      ProtectionContainerResource result = apiInstance.protectionContainerOperationResultsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, operationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtectionContainerOperationResultsApi#protectionContainerOperationResultsGet");
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
| **fabricName** | **String**| Fabric name associated with the container. | |
| **containerName** | **String**| Container name whose information should be fetched. | |
| **operationId** | **String**| Operation ID which represents the operation whose result needs to be fetched. | |

### Return type

[**ProtectionContainerResource**](ProtectionContainerResource.md)

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

