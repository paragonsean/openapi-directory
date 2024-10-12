# ProtectionContainerRefreshOperationResultsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protectionContainerRefreshOperationResultsGet**](ProtectionContainerRefreshOperationResultsApi.md#protectionContainerRefreshOperationResultsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/operationResults/{operationId} |  |


<a id="protectionContainerRefreshOperationResultsGet"></a>
# **protectionContainerRefreshOperationResultsGet**
> protectionContainerRefreshOperationResultsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, operationId)



Provides the result of the refresh operation triggered by the BeginRefresh operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtectionContainerRefreshOperationResultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProtectionContainerRefreshOperationResultsApi apiInstance = new ProtectionContainerRefreshOperationResultsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String fabricName = "fabricName_example"; // String | The fabric name associated with the container.
    String operationId = "operationId_example"; // String | The operation ID used for this GET operation.
    try {
      apiInstance.protectionContainerRefreshOperationResultsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, operationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtectionContainerRefreshOperationResultsApi#protectionContainerRefreshOperationResultsGet");
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
| **fabricName** | **String**| The fabric name associated with the container. | |
| **operationId** | **String**| The operation ID used for this GET operation. | |

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
| **202** | Accepted. |  -  |
| **204** | No content. |  -  |

