# WorkspacesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workspacesList**](WorkspacesApi.md#workspacesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBI/workspaceCollections/{workspaceCollectionName}/workspaces |  |


<a id="workspacesList"></a>
# **workspacesList**
> WorkspaceList workspacesList(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion)



Retrieves all existing Power BI workspaces in the specified workspace collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group
    String workspaceCollectionName = "workspaceCollectionName_example"; // String | Power BI Embedded Workspace Collection name
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      WorkspaceList result = apiInstance.workspacesList(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesList");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Azure resource group | |
| **workspaceCollectionName** | **String**| Power BI Embedded Workspace Collection name | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**WorkspaceList**](WorkspaceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get workspaces completed successfully |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

