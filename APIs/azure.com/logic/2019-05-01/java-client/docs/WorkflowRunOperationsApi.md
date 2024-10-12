# WorkflowRunOperationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workflowRunOperationsGet**](WorkflowRunOperationsApi.md#workflowRunOperationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/operations/{operationId} |  |


<a id="workflowRunOperationsGet"></a>
# **workflowRunOperationsGet**
> WorkflowRun workflowRunOperationsGet(subscriptionId, resourceGroupName, workflowName, runName, operationId, apiVersion)



Gets an operation for a run.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowRunOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowRunOperationsApi apiInstance = new WorkflowRunOperationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String runName = "runName_example"; // String | The workflow run name.
    String operationId = "operationId_example"; // String | The workflow operation id.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      WorkflowRun result = apiInstance.workflowRunOperationsGet(subscriptionId, resourceGroupName, workflowName, runName, operationId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowRunOperationsApi#workflowRunOperationsGet");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **workflowName** | **String**| The workflow name. | |
| **runName** | **String**| The workflow run name. | |
| **operationId** | **String**| The workflow operation id. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**WorkflowRun**](WorkflowRun.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

