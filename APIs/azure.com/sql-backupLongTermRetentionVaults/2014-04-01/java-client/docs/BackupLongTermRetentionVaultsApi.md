# BackupLongTermRetentionVaultsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**backupLongTermRetentionVaultsCreateOrUpdate**](BackupLongTermRetentionVaultsApi.md#backupLongTermRetentionVaultsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/backupLongTermRetentionVaults/{backupLongTermRetentionVaultName} |  |
| [**backupLongTermRetentionVaultsGet**](BackupLongTermRetentionVaultsApi.md#backupLongTermRetentionVaultsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/backupLongTermRetentionVaults/{backupLongTermRetentionVaultName} |  |
| [**backupLongTermRetentionVaultsListByServer**](BackupLongTermRetentionVaultsApi.md#backupLongTermRetentionVaultsListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/backupLongTermRetentionVaults |  |


<a id="backupLongTermRetentionVaultsCreateOrUpdate"></a>
# **backupLongTermRetentionVaultsCreateOrUpdate**
> BackupLongTermRetentionVault backupLongTermRetentionVaultsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, backupLongTermRetentionVaultName, parameters)



Updates a server backup long term retention vault

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupLongTermRetentionVaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BackupLongTermRetentionVaultsApi apiInstance = new BackupLongTermRetentionVaultsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String backupLongTermRetentionVaultName = "RegisteredVault"; // String | The name of the backup long term retention vault
    BackupLongTermRetentionVault parameters = new BackupLongTermRetentionVault(); // BackupLongTermRetentionVault | The required parameters to update a backup long term retention vault
    try {
      BackupLongTermRetentionVault result = apiInstance.backupLongTermRetentionVaultsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, backupLongTermRetentionVaultName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupLongTermRetentionVaultsApi#backupLongTermRetentionVaultsCreateOrUpdate");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **backupLongTermRetentionVaultName** | **String**| The name of the backup long term retention vault | [enum: RegisteredVault] |
| **parameters** | [**BackupLongTermRetentionVault**](BackupLongTermRetentionVault.md)| The required parameters to update a backup long term retention vault | |

### Return type

[**BackupLongTermRetentionVault**](BackupLongTermRetentionVault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **202** | Accepted |  -  |

<a id="backupLongTermRetentionVaultsGet"></a>
# **backupLongTermRetentionVaultsGet**
> BackupLongTermRetentionVault backupLongTermRetentionVaultsGet(apiVersion, subscriptionId, resourceGroupName, serverName, backupLongTermRetentionVaultName)



Gets a server backup long term retention vault

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupLongTermRetentionVaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BackupLongTermRetentionVaultsApi apiInstance = new BackupLongTermRetentionVaultsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String backupLongTermRetentionVaultName = "RegisteredVault"; // String | The name of the Azure SQL Server backup LongTermRetention vault
    try {
      BackupLongTermRetentionVault result = apiInstance.backupLongTermRetentionVaultsGet(apiVersion, subscriptionId, resourceGroupName, serverName, backupLongTermRetentionVaultName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupLongTermRetentionVaultsApi#backupLongTermRetentionVaultsGet");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **backupLongTermRetentionVaultName** | **String**| The name of the Azure SQL Server backup LongTermRetention vault | [enum: RegisteredVault] |

### Return type

[**BackupLongTermRetentionVault**](BackupLongTermRetentionVault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="backupLongTermRetentionVaultsListByServer"></a>
# **backupLongTermRetentionVaultsListByServer**
> BackupLongTermRetentionVaultListResult backupLongTermRetentionVaultsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName)



Gets server backup long term retention vaults in a server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupLongTermRetentionVaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BackupLongTermRetentionVaultsApi apiInstance = new BackupLongTermRetentionVaultsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    try {
      BackupLongTermRetentionVaultListResult result = apiInstance.backupLongTermRetentionVaultsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupLongTermRetentionVaultsApi#backupLongTermRetentionVaultsListByServer");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |

### Return type

[**BackupLongTermRetentionVaultListResult**](BackupLongTermRetentionVaultListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

