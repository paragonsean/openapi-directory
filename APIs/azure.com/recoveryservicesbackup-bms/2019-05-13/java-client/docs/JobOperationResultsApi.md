# JobOperationResultsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jobOperationResultsGet**](JobOperationResultsApi.md#jobOperationResultsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupJobs/{jobName}/operationResults/{operationId} |  |


<a id="jobOperationResultsGet"></a>
# **jobOperationResultsGet**
> jobOperationResultsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, jobName, operationId)



Fetches the result of any operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobOperationResultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobOperationResultsApi apiInstance = new JobOperationResultsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String jobName = "jobName_example"; // String | Job name whose operation result has to be fetched.
    String operationId = "operationId_example"; // String | OperationID which represents the operation whose result has to be fetched.
    try {
      apiInstance.jobOperationResultsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, jobName, operationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobOperationResultsApi#jobOperationResultsGet");
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
| **jobName** | **String**| Job name whose operation result has to be fetched. | |
| **operationId** | **String**| OperationID which represents the operation whose result has to be fetched. | |

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
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **204** | NoContent |  -  |

