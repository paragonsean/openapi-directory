# JobCancellationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jobCancellationsTrigger**](JobCancellationsApi.md#jobCancellationsTrigger) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupJobs/{jobName}/cancel |  |


<a id="jobCancellationsTrigger"></a>
# **jobCancellationsTrigger**
> jobCancellationsTrigger(apiVersion, vaultName, resourceGroupName, subscriptionId, jobName)



Cancels the job. This is an asynchronous operation. To know the status of the cancellation, call the GetCancelOperationResult API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobCancellationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobCancellationsApi apiInstance = new JobCancellationsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String jobName = "jobName_example"; // String | Name of the job to cancel.
    try {
      apiInstance.jobCancellationsTrigger(apiVersion, vaultName, resourceGroupName, subscriptionId, jobName);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobCancellationsApi#jobCancellationsTrigger");
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
| **jobName** | **String**| Name of the job to cancel. | |

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

