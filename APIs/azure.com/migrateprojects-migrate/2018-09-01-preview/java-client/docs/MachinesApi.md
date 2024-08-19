# MachinesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**machinesEnumerateMachines**](MachinesApi.md#machinesEnumerateMachines) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/machines | Gets a list of machines in the migrate project. |
| [**machinesGetMachine**](MachinesApi.md#machinesGetMachine) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/machines/{machineName} | Gets a machine in the migrate project. |


<a id="machinesEnumerateMachines"></a>
# **machinesEnumerateMachines**
> MachineCollection machinesEnumerateMachines(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, continuationToken, pageSize)

Gets a list of machines in the migrate project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MachinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MachinesApi apiInstance = new MachinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
    String migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2018-09-01-preview"; // String | Standard request header. Used by service to identify API version used by client.
    String continuationToken = "continuationToken_example"; // String | The continuation token.
    Integer pageSize = 56; // Integer | The number of items to be returned in a single page. This value is honored only if it is less than the 100.
    try {
      MachineCollection result = apiInstance.machinesEnumerateMachines(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, continuationToken, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MachinesApi#machinesEnumerateMachines");
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
| **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | |
| **migrateProjectName** | **String**| Name of the Azure Migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-09-01-preview] |
| **continuationToken** | **String**| The continuation token. | [optional] |
| **pageSize** | **Integer**| The number of items to be returned in a single page. This value is honored only if it is less than the 100. | [optional] |

### Return type

[**MachineCollection**](MachineCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="machinesGetMachine"></a>
# **machinesGetMachine**
> Machine machinesGetMachine(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, machineName)

Gets a machine in the migrate project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MachinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MachinesApi apiInstance = new MachinesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
    String migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2018-09-01-preview"; // String | Standard request header. Used by service to identify API version used by client.
    String machineName = "machineName_example"; // String | Unique name of a machine in Azure migration hub.
    try {
      Machine result = apiInstance.machinesGetMachine(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, machineName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MachinesApi#machinesGetMachine");
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
| **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | |
| **migrateProjectName** | **String**| Name of the Azure Migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-09-01-preview] |
| **machineName** | **String**| Unique name of a machine in Azure migration hub. | |

### Return type

[**Machine**](Machine.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

