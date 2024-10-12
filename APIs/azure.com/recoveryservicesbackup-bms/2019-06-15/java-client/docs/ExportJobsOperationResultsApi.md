# ExportJobsOperationResultsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**exportJobsOperationResultsGet**](ExportJobsOperationResultsApi.md#exportJobsOperationResultsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupJobs/operationResults/{operationId} |  |


<a id="exportJobsOperationResultsGet"></a>
# **exportJobsOperationResultsGet**
> OperationResultInfoBaseResource exportJobsOperationResultsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, operationId)



Gets the operation result of operation triggered by Export Jobs API. If the operation is successful, then it also  contains URL of a Blob and a SAS key to access the same. The blob contains exported jobs in JSON serialized format.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportJobsOperationResultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExportJobsOperationResultsApi apiInstance = new ExportJobsOperationResultsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String operationId = "operationId_example"; // String | OperationID which represents the export job.
    try {
      OperationResultInfoBaseResource result = apiInstance.exportJobsOperationResultsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, operationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportJobsOperationResultsApi#exportJobsOperationResultsGet");
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
| **operationId** | **String**| OperationID which represents the export job. | |

### Return type

[**OperationResultInfoBaseResource**](OperationResultInfoBaseResource.md)

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

