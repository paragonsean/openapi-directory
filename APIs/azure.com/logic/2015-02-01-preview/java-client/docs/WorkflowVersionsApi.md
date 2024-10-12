# WorkflowVersionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workflowVersionsGet**](WorkflowVersionsApi.md#workflowVersionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/versions/{versionId} |  |


<a id="workflowVersionsGet"></a>
# **workflowVersionsGet**
> WorkflowVersion workflowVersionsGet(subscriptionId, resourceGroupName, workflowName, versionId, apiVersion)



Gets a workflow version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowVersionsApi apiInstance = new WorkflowVersionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String versionId = "versionId_example"; // String | The workflow versionId.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      WorkflowVersion result = apiInstance.workflowVersionsGet(subscriptionId, resourceGroupName, workflowName, versionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowVersionsApi#workflowVersionsGet");
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
| **versionId** | **String**| The workflow versionId. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**WorkflowVersion**](WorkflowVersion.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

