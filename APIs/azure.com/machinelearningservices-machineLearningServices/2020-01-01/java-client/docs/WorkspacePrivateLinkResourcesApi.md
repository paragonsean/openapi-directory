# WorkspacePrivateLinkResourcesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**privateLinkResourcesListByWorkspace**](WorkspacePrivateLinkResourcesApi.md#privateLinkResourcesListByWorkspace) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/privateLinkResources |  |


<a id="privateLinkResourcesListByWorkspace"></a>
# **privateLinkResourcesListByWorkspace**
> PrivateLinkResourceListResult privateLinkResourcesListByWorkspace(subscriptionId, resourceGroupName, workspaceName, apiVersion)



Gets the private link resources that need to be created for a workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacePrivateLinkResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacePrivateLinkResourcesApi apiInstance = new WorkspacePrivateLinkResourcesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which workspace is located.
    String workspaceName = "workspaceName_example"; // String | Name of Azure Machine Learning workspace.
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    try {
      PrivateLinkResourceListResult result = apiInstance.privateLinkResourcesListByWorkspace(subscriptionId, resourceGroupName, workspaceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacePrivateLinkResourcesApi#privateLinkResourcesListByWorkspace");
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
| **subscriptionId** | **String**| Azure subscription identifier. | |
| **resourceGroupName** | **String**| Name of the resource group in which workspace is located. | |
| **workspaceName** | **String**| Name of Azure Machine Learning workspace. | |
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |

### Return type

[**PrivateLinkResourceListResult**](PrivateLinkResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved private link resources. |  -  |

