# RecoveryPointsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**recoveryPointsGet**](RecoveryPointsApi.md#recoveryPointsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/recoveryPoints/{recoveryPointName} | Get a recovery point. |
| [**recoveryPointsListByReplicationProtectedItems**](RecoveryPointsApi.md#recoveryPointsListByReplicationProtectedItems) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/recoveryPoints | Get recovery points for a replication protected item. |


<a id="recoveryPointsGet"></a>
# **recoveryPointsGet**
> RecoveryPoint recoveryPointsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, recoveryPointName)

Get a recovery point.

Get the details of specified recovery point.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecoveryPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RecoveryPointsApi apiInstance = new RecoveryPointsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | The fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | The protection container name.
    String replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | The replication protected item's name.
    String recoveryPointName = "recoveryPointName_example"; // String | The recovery point name.
    try {
      RecoveryPoint result = apiInstance.recoveryPointsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, recoveryPointName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecoveryPointsApi#recoveryPointsGet");
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
| **resourceName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **fabricName** | **String**| The fabric name. | |
| **protectionContainerName** | **String**| The protection container name. | |
| **replicatedProtectedItemName** | **String**| The replication protected item&#39;s name. | |
| **recoveryPointName** | **String**| The recovery point name. | |

### Return type

[**RecoveryPoint**](RecoveryPoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recoveryPointsListByReplicationProtectedItems"></a>
# **recoveryPointsListByReplicationProtectedItems**
> RecoveryPointCollection recoveryPointsListByReplicationProtectedItems(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName)

Get recovery points for a replication protected item.

Lists the available recovery points for a replication protected item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecoveryPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RecoveryPointsApi apiInstance = new RecoveryPointsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | The fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | The protection container name.
    String replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | The replication protected item's name.
    try {
      RecoveryPointCollection result = apiInstance.recoveryPointsListByReplicationProtectedItems(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecoveryPointsApi#recoveryPointsListByReplicationProtectedItems");
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
| **resourceName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **fabricName** | **String**| The fabric name. | |
| **protectionContainerName** | **String**| The protection container name. | |
| **replicatedProtectedItemName** | **String**| The replication protected item&#39;s name. | |

### Return type

[**RecoveryPointCollection**](RecoveryPointCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

