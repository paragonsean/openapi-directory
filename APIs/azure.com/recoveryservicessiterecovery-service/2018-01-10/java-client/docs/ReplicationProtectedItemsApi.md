# ReplicationProtectedItemsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**replicationProtectedItemsApplyRecoveryPoint**](ReplicationProtectedItemsApi.md#replicationProtectedItemsApplyRecoveryPoint) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/applyRecoveryPoint | Change or apply recovery point. |
| [**replicationProtectedItemsCreate**](ReplicationProtectedItemsApi.md#replicationProtectedItemsCreate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName} | Enables protection. |
| [**replicationProtectedItemsDelete**](ReplicationProtectedItemsApi.md#replicationProtectedItemsDelete) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/remove | Disables protection. |
| [**replicationProtectedItemsFailoverCommit**](ReplicationProtectedItemsApi.md#replicationProtectedItemsFailoverCommit) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/failoverCommit | Execute commit failover |
| [**replicationProtectedItemsGet**](ReplicationProtectedItemsApi.md#replicationProtectedItemsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName} | Gets the details of a Replication protected item. |
| [**replicationProtectedItemsList**](ReplicationProtectedItemsApi.md#replicationProtectedItemsList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationProtectedItems | Gets the list of replication protected items. |
| [**replicationProtectedItemsListByReplicationProtectionContainers**](ReplicationProtectedItemsApi.md#replicationProtectedItemsListByReplicationProtectionContainers) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems | Gets the list of Replication protected items. |
| [**replicationProtectedItemsPlannedFailover**](ReplicationProtectedItemsApi.md#replicationProtectedItemsPlannedFailover) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/plannedFailover | Execute planned failover |
| [**replicationProtectedItemsPurge**](ReplicationProtectedItemsApi.md#replicationProtectedItemsPurge) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName} | Purges protection. |
| [**replicationProtectedItemsRepairReplication**](ReplicationProtectedItemsApi.md#replicationProtectedItemsRepairReplication) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/repairReplication | Resynchronize or repair replication. |
| [**replicationProtectedItemsReprotect**](ReplicationProtectedItemsApi.md#replicationProtectedItemsReprotect) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/reProtect | Execute Reverse Replication\\Reprotect |
| [**replicationProtectedItemsTestFailover**](ReplicationProtectedItemsApi.md#replicationProtectedItemsTestFailover) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/testFailover | Execute test failover |
| [**replicationProtectedItemsTestFailoverCleanup**](ReplicationProtectedItemsApi.md#replicationProtectedItemsTestFailoverCleanup) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/testFailoverCleanup | Execute test failover cleanup. |
| [**replicationProtectedItemsUnplannedFailover**](ReplicationProtectedItemsApi.md#replicationProtectedItemsUnplannedFailover) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/unplannedFailover | Execute unplanned failover |
| [**replicationProtectedItemsUpdate**](ReplicationProtectedItemsApi.md#replicationProtectedItemsUpdate) | **PATCH** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName} | Updates protection. |
| [**replicationProtectedItemsUpdateMobilityService**](ReplicationProtectedItemsApi.md#replicationProtectedItemsUpdateMobilityService) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicationProtectedItemName}/updateMobilityService | Update the mobility service on a protected item. |


<a id="replicationProtectedItemsApplyRecoveryPoint"></a>
# **replicationProtectedItemsApplyRecoveryPoint**
> ReplicationProtectedItem replicationProtectedItemsApplyRecoveryPoint(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, applyRecoveryPointInput)

Change or apply recovery point.

The operation to change the recovery point of a failed over replication protected item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectedItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectedItemsApi apiInstance = new ReplicationProtectedItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | The ARM fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | The protection container name.
    String replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | The replicated protected item's name.
    ApplyRecoveryPointInput applyRecoveryPointInput = new ApplyRecoveryPointInput(); // ApplyRecoveryPointInput | The ApplyRecoveryPointInput.
    try {
      ReplicationProtectedItem result = apiInstance.replicationProtectedItemsApplyRecoveryPoint(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, applyRecoveryPointInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectedItemsApi#replicationProtectedItemsApplyRecoveryPoint");
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
| **fabricName** | **String**| The ARM fabric name. | |
| **protectionContainerName** | **String**| The protection container name. | |
| **replicatedProtectedItemName** | **String**| The replicated protected item&#39;s name. | |
| **applyRecoveryPointInput** | [**ApplyRecoveryPointInput**](ApplyRecoveryPointInput.md)| The ApplyRecoveryPointInput. | |

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="replicationProtectedItemsCreate"></a>
# **replicationProtectedItemsCreate**
> ReplicationProtectedItem replicationProtectedItemsCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, input)

Enables protection.

The operation to create an ASR replication protected item (Enable replication).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectedItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectedItemsApi apiInstance = new ReplicationProtectedItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Name of the fabric.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | A name for the replication protected item.
    EnableProtectionInput input = new EnableProtectionInput(); // EnableProtectionInput | Enable Protection Input.
    try {
      ReplicationProtectedItem result = apiInstance.replicationProtectedItemsCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectedItemsApi#replicationProtectedItemsCreate");
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
| **fabricName** | **String**| Name of the fabric. | |
| **protectionContainerName** | **String**| Protection container name. | |
| **replicatedProtectedItemName** | **String**| A name for the replication protected item. | |
| **input** | [**EnableProtectionInput**](EnableProtectionInput.md)| Enable Protection Input. | |

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="replicationProtectedItemsDelete"></a>
# **replicationProtectedItemsDelete**
> replicationProtectedItemsDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, disableProtectionInput)

Disables protection.

The operation to disable replication on a replication protected item. This will also remove the item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectedItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectedItemsApi apiInstance = new ReplicationProtectedItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
    DisableProtectionInput disableProtectionInput = new DisableProtectionInput(); // DisableProtectionInput | Disable protection input.
    try {
      apiInstance.replicationProtectedItemsDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, disableProtectionInput);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectedItemsApi#replicationProtectedItemsDelete");
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
| **fabricName** | **String**| Fabric name. | |
| **protectionContainerName** | **String**| Protection container name. | |
| **replicatedProtectedItemName** | **String**| Replication protected item name. | |
| **disableProtectionInput** | [**DisableProtectionInput**](DisableProtectionInput.md)| Disable protection input. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |
| **204** | NoContent |  -  |

<a id="replicationProtectedItemsFailoverCommit"></a>
# **replicationProtectedItemsFailoverCommit**
> ReplicationProtectedItem replicationProtectedItemsFailoverCommit(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName)

Execute commit failover

Operation to commit the failover of the replication protected item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectedItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectedItemsApi apiInstance = new ReplicationProtectedItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Unique fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
    try {
      ReplicationProtectedItem result = apiInstance.replicationProtectedItemsFailoverCommit(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectedItemsApi#replicationProtectedItemsFailoverCommit");
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
| **fabricName** | **String**| Unique fabric name. | |
| **protectionContainerName** | **String**| Protection container name. | |
| **replicatedProtectedItemName** | **String**| Replication protected item name. | |

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="replicationProtectedItemsGet"></a>
# **replicationProtectedItemsGet**
> ReplicationProtectedItem replicationProtectedItemsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName)

Gets the details of a Replication protected item.

Gets the details of an ASR replication protected item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectedItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectedItemsApi apiInstance = new ReplicationProtectedItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric unique name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
    try {
      ReplicationProtectedItem result = apiInstance.replicationProtectedItemsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectedItemsApi#replicationProtectedItemsGet");
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
| **replicatedProtectedItemName** | **String**| Replication protected item name. | |

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationProtectedItemsList"></a>
# **replicationProtectedItemsList**
> ReplicationProtectedItemCollection replicationProtectedItemsList(apiVersion, resourceName, resourceGroupName, subscriptionId, skipToken, $filter)

Gets the list of replication protected items.

Gets the list of ASR replication protected items in the vault.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectedItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectedItemsApi apiInstance = new ReplicationProtectedItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String skipToken = "skipToken_example"; // String | The pagination token. Possible values: \"FabricId\" or \"FabricId_CloudId\" or null
    String $filter = "$filter_example"; // String | OData filter options.
    try {
      ReplicationProtectedItemCollection result = apiInstance.replicationProtectedItemsList(apiVersion, resourceName, resourceGroupName, subscriptionId, skipToken, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectedItemsApi#replicationProtectedItemsList");
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
| **skipToken** | **String**| The pagination token. Possible values: \&quot;FabricId\&quot; or \&quot;FabricId_CloudId\&quot; or null | [optional] |
| **$filter** | **String**| OData filter options. | [optional] |

### Return type

[**ReplicationProtectedItemCollection**](ReplicationProtectedItemCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationProtectedItemsListByReplicationProtectionContainers"></a>
# **replicationProtectedItemsListByReplicationProtectionContainers**
> ReplicationProtectedItemCollection replicationProtectedItemsListByReplicationProtectionContainers(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName)

Gets the list of Replication protected items.

Gets the list of ASR replication protected items in the protection container.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectedItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectedItemsApi apiInstance = new ReplicationProtectedItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    try {
      ReplicationProtectedItemCollection result = apiInstance.replicationProtectedItemsListByReplicationProtectionContainers(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectedItemsApi#replicationProtectedItemsListByReplicationProtectionContainers");
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
| **fabricName** | **String**| Fabric name. | |
| **protectionContainerName** | **String**| Protection container name. | |

### Return type

[**ReplicationProtectedItemCollection**](ReplicationProtectedItemCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationProtectedItemsPlannedFailover"></a>
# **replicationProtectedItemsPlannedFailover**
> ReplicationProtectedItem replicationProtectedItemsPlannedFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, failoverInput)

Execute planned failover

Operation to initiate a planned failover of the replication protected item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectedItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectedItemsApi apiInstance = new ReplicationProtectedItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Unique fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
    PlannedFailoverInput failoverInput = new PlannedFailoverInput(); // PlannedFailoverInput | Disable protection input.
    try {
      ReplicationProtectedItem result = apiInstance.replicationProtectedItemsPlannedFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, failoverInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectedItemsApi#replicationProtectedItemsPlannedFailover");
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
| **fabricName** | **String**| Unique fabric name. | |
| **protectionContainerName** | **String**| Protection container name. | |
| **replicatedProtectedItemName** | **String**| Replication protected item name. | |
| **failoverInput** | [**PlannedFailoverInput**](PlannedFailoverInput.md)| Disable protection input. | |

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="replicationProtectedItemsPurge"></a>
# **replicationProtectedItemsPurge**
> replicationProtectedItemsPurge(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName)

Purges protection.

The operation to delete or purge a replication protected item. This operation will force delete the replication protected item. Use the remove operation on replication protected item to perform a clean disable replication for the item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectedItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectedItemsApi apiInstance = new ReplicationProtectedItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
    try {
      apiInstance.replicationProtectedItemsPurge(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectedItemsApi#replicationProtectedItemsPurge");
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
| **fabricName** | **String**| Fabric name. | |
| **protectionContainerName** | **String**| Protection container name. | |
| **replicatedProtectedItemName** | **String**| Replication protected item name. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |
| **204** | NoContent |  -  |

<a id="replicationProtectedItemsRepairReplication"></a>
# **replicationProtectedItemsRepairReplication**
> ReplicationProtectedItem replicationProtectedItemsRepairReplication(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName)

Resynchronize or repair replication.

The operation to start resynchronize/repair replication for a replication protected item requiring resynchronization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectedItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectedItemsApi apiInstance = new ReplicationProtectedItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | The name of the fabric.
    String protectionContainerName = "protectionContainerName_example"; // String | The name of the container.
    String replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | The name of the replication protected item.
    try {
      ReplicationProtectedItem result = apiInstance.replicationProtectedItemsRepairReplication(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectedItemsApi#replicationProtectedItemsRepairReplication");
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
| **fabricName** | **String**| The name of the fabric. | |
| **protectionContainerName** | **String**| The name of the container. | |
| **replicatedProtectedItemName** | **String**| The name of the replication protected item. | |

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="replicationProtectedItemsReprotect"></a>
# **replicationProtectedItemsReprotect**
> ReplicationProtectedItem replicationProtectedItemsReprotect(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, rrInput)

Execute Reverse Replication\\Reprotect

Operation to reprotect or reverse replicate a failed over replication protected item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectedItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectedItemsApi apiInstance = new ReplicationProtectedItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Unique fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
    ReverseReplicationInput rrInput = new ReverseReplicationInput(); // ReverseReplicationInput | Disable protection input.
    try {
      ReplicationProtectedItem result = apiInstance.replicationProtectedItemsReprotect(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, rrInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectedItemsApi#replicationProtectedItemsReprotect");
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
| **fabricName** | **String**| Unique fabric name. | |
| **protectionContainerName** | **String**| Protection container name. | |
| **replicatedProtectedItemName** | **String**| Replication protected item name. | |
| **rrInput** | [**ReverseReplicationInput**](ReverseReplicationInput.md)| Disable protection input. | |

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="replicationProtectedItemsTestFailover"></a>
# **replicationProtectedItemsTestFailover**
> ReplicationProtectedItem replicationProtectedItemsTestFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, failoverInput)

Execute test failover

Operation to perform a test failover of the replication protected item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectedItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectedItemsApi apiInstance = new ReplicationProtectedItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Unique fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
    TestFailoverInput failoverInput = new TestFailoverInput(); // TestFailoverInput | Test failover input.
    try {
      ReplicationProtectedItem result = apiInstance.replicationProtectedItemsTestFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, failoverInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectedItemsApi#replicationProtectedItemsTestFailover");
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
| **fabricName** | **String**| Unique fabric name. | |
| **protectionContainerName** | **String**| Protection container name. | |
| **replicatedProtectedItemName** | **String**| Replication protected item name. | |
| **failoverInput** | [**TestFailoverInput**](TestFailoverInput.md)| Test failover input. | |

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="replicationProtectedItemsTestFailoverCleanup"></a>
# **replicationProtectedItemsTestFailoverCleanup**
> ReplicationProtectedItem replicationProtectedItemsTestFailoverCleanup(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, cleanupInput)

Execute test failover cleanup.

Operation to clean up the test failover of a replication protected item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectedItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectedItemsApi apiInstance = new ReplicationProtectedItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Unique fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
    TestFailoverCleanupInput cleanupInput = new TestFailoverCleanupInput(); // TestFailoverCleanupInput | Test failover cleanup input.
    try {
      ReplicationProtectedItem result = apiInstance.replicationProtectedItemsTestFailoverCleanup(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, cleanupInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectedItemsApi#replicationProtectedItemsTestFailoverCleanup");
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
| **fabricName** | **String**| Unique fabric name. | |
| **protectionContainerName** | **String**| Protection container name. | |
| **replicatedProtectedItemName** | **String**| Replication protected item name. | |
| **cleanupInput** | [**TestFailoverCleanupInput**](TestFailoverCleanupInput.md)| Test failover cleanup input. | |

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="replicationProtectedItemsUnplannedFailover"></a>
# **replicationProtectedItemsUnplannedFailover**
> ReplicationProtectedItem replicationProtectedItemsUnplannedFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, failoverInput)

Execute unplanned failover

Operation to initiate a failover of the replication protected item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectedItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectedItemsApi apiInstance = new ReplicationProtectedItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Unique fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
    UnplannedFailoverInput failoverInput = new UnplannedFailoverInput(); // UnplannedFailoverInput | Disable protection input.
    try {
      ReplicationProtectedItem result = apiInstance.replicationProtectedItemsUnplannedFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, failoverInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectedItemsApi#replicationProtectedItemsUnplannedFailover");
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
| **fabricName** | **String**| Unique fabric name. | |
| **protectionContainerName** | **String**| Protection container name. | |
| **replicatedProtectedItemName** | **String**| Replication protected item name. | |
| **failoverInput** | [**UnplannedFailoverInput**](UnplannedFailoverInput.md)| Disable protection input. | |

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="replicationProtectedItemsUpdate"></a>
# **replicationProtectedItemsUpdate**
> ReplicationProtectedItem replicationProtectedItemsUpdate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, updateProtectionInput)

Updates protection.

The operation to update the recovery settings of an ASR replication protected item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectedItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectedItemsApi apiInstance = new ReplicationProtectedItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
    UpdateReplicationProtectedItemInput updateProtectionInput = new UpdateReplicationProtectedItemInput(); // UpdateReplicationProtectedItemInput | Update protection input.
    try {
      ReplicationProtectedItem result = apiInstance.replicationProtectedItemsUpdate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, updateProtectionInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectedItemsApi#replicationProtectedItemsUpdate");
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
| **fabricName** | **String**| Fabric name. | |
| **protectionContainerName** | **String**| Protection container name. | |
| **replicatedProtectedItemName** | **String**| Replication protected item name. | |
| **updateProtectionInput** | [**UpdateReplicationProtectedItemInput**](UpdateReplicationProtectedItemInput.md)| Update protection input. | |

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="replicationProtectedItemsUpdateMobilityService"></a>
# **replicationProtectedItemsUpdateMobilityService**
> ReplicationProtectedItem replicationProtectedItemsUpdateMobilityService(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicationProtectedItemName, updateMobilityServiceRequest)

Update the mobility service on a protected item.

The operation to update(push update) the installed mobility service software on a replication protected item to the latest available version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationProtectedItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationProtectedItemsApi apiInstance = new ReplicationProtectedItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | The name of the fabric containing the protected item.
    String protectionContainerName = "protectionContainerName_example"; // String | The name of the container containing the protected item.
    String replicationProtectedItemName = "replicationProtectedItemName_example"; // String | The name of the protected item on which the agent is to be updated.
    UpdateMobilityServiceRequest updateMobilityServiceRequest = new UpdateMobilityServiceRequest(); // UpdateMobilityServiceRequest | Request to update the mobility service on the protected item.
    try {
      ReplicationProtectedItem result = apiInstance.replicationProtectedItemsUpdateMobilityService(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicationProtectedItemName, updateMobilityServiceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationProtectedItemsApi#replicationProtectedItemsUpdateMobilityService");
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
| **fabricName** | **String**| The name of the fabric containing the protected item. | |
| **protectionContainerName** | **String**| The name of the container containing the protected item. | |
| **replicationProtectedItemName** | **String**| The name of the protected item on which the agent is to be updated. | |
| **updateMobilityServiceRequest** | [**UpdateMobilityServiceRequest**](UpdateMobilityServiceRequest.md)| Request to update the mobility service on the protected item. | |

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

