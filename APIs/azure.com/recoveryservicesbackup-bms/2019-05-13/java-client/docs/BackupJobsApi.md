# BackupJobsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**backupJobsList**](BackupJobsApi.md#backupJobsList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupJobs |  |


<a id="backupJobsList"></a>
# **backupJobsList**
> JobResourceList backupJobsList(apiVersion, vaultName, resourceGroupName, subscriptionId, $filter, $skipToken)



Provides a pageable list of jobs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupJobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BackupJobsApi apiInstance = new BackupJobsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String $filter = "$filter_example"; // String | OData filter options.
    String $skipToken = "$skipToken_example"; // String | skipToken Filter.
    try {
      JobResourceList result = apiInstance.backupJobsList(apiVersion, vaultName, resourceGroupName, subscriptionId, $filter, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupJobsApi#backupJobsList");
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
| **$filter** | **String**| OData filter options. | [optional] |
| **$skipToken** | **String**| skipToken Filter. | [optional] |

### Return type

[**JobResourceList**](JobResourceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

