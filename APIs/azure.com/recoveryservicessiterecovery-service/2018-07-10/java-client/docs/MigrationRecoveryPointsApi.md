# MigrationRecoveryPointsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**migrationRecoveryPointsGet**](MigrationRecoveryPointsApi.md#migrationRecoveryPointsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationMigrationItems/{migrationItemName}/migrationRecoveryPoints/{migrationRecoveryPointName} | Gets a recovery point for a migration item. |
| [**migrationRecoveryPointsListByReplicationMigrationItems**](MigrationRecoveryPointsApi.md#migrationRecoveryPointsListByReplicationMigrationItems) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationMigrationItems/{migrationItemName}/migrationRecoveryPoints | Gets the recovery points for a migration item. |


<a id="migrationRecoveryPointsGet"></a>
# **migrationRecoveryPointsGet**
> MigrationRecoveryPoint migrationRecoveryPointsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, migrationItemName, migrationRecoveryPointName)

Gets a recovery point for a migration item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MigrationRecoveryPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MigrationRecoveryPointsApi apiInstance = new MigrationRecoveryPointsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric unique name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String migrationItemName = "migrationItemName_example"; // String | Migration item name.
    String migrationRecoveryPointName = "migrationRecoveryPointName_example"; // String | The migration recovery point name.
    try {
      MigrationRecoveryPoint result = apiInstance.migrationRecoveryPointsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, migrationItemName, migrationRecoveryPointName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MigrationRecoveryPointsApi#migrationRecoveryPointsGet");
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
| **fabricName** | **String**| Fabric unique name. | |
| **protectionContainerName** | **String**| Protection container name. | |
| **migrationItemName** | **String**| Migration item name. | |
| **migrationRecoveryPointName** | **String**| The migration recovery point name. | |

### Return type

[**MigrationRecoveryPoint**](MigrationRecoveryPoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="migrationRecoveryPointsListByReplicationMigrationItems"></a>
# **migrationRecoveryPointsListByReplicationMigrationItems**
> MigrationRecoveryPointCollection migrationRecoveryPointsListByReplicationMigrationItems(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, migrationItemName)

Gets the recovery points for a migration item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MigrationRecoveryPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MigrationRecoveryPointsApi apiInstance = new MigrationRecoveryPointsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric unique name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String migrationItemName = "migrationItemName_example"; // String | Migration item name.
    try {
      MigrationRecoveryPointCollection result = apiInstance.migrationRecoveryPointsListByReplicationMigrationItems(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, migrationItemName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MigrationRecoveryPointsApi#migrationRecoveryPointsListByReplicationMigrationItems");
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
| **fabricName** | **String**| Fabric unique name. | |
| **protectionContainerName** | **String**| Protection container name. | |
| **migrationItemName** | **String**| Migration item name. | |

### Return type

[**MigrationRecoveryPointCollection**](MigrationRecoveryPointCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

