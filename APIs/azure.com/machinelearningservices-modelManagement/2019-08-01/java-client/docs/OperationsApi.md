# OperationsApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**operationsGet**](OperationsApi.md#operationsGet) | **GET** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/operations/{id} | Get the status of an async operation. |


<a id="operationsGet"></a>
# **operationsGet**
> AsyncOperationStatus operationsGet(subscriptionId, resourceGroup, workspace, id)

Get the status of an async operation.

Get the status of an async operation by operation id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OperationsApi apiInstance = new OperationsApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
    String workspace = "workspace_example"; // String | The name of the workspace.
    String id = "id_example"; // String | The operation id.
    try {
      AsyncOperationStatus result = apiInstance.operationsGet(subscriptionId, resourceGroup, workspace, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationsApi#operationsGet");
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
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroup** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspace** | **String**| The name of the workspace. | |
| **id** | **String**| The operation id. | |

### Return type

[**AsyncOperationStatus**](AsyncOperationStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error response describing why the operation failed. |  -  |

