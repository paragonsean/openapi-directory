# ReplicationMigrationItemsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**replicationMigrationItemsCreate**](ReplicationMigrationItemsApi.md#replicationMigrationItemsCreate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationMigrationItems/{migrationItemName} | Enables migration. |
| [**replicationMigrationItemsDelete**](ReplicationMigrationItemsApi.md#replicationMigrationItemsDelete) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationMigrationItems/{migrationItemName} | Delete the migration item. |
| [**replicationMigrationItemsGet**](ReplicationMigrationItemsApi.md#replicationMigrationItemsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationMigrationItems/{migrationItemName} | Gets the details of a migration item. |
| [**replicationMigrationItemsList**](ReplicationMigrationItemsApi.md#replicationMigrationItemsList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationMigrationItems | Gets the list of migration items in the vault. |
| [**replicationMigrationItemsListByReplicationProtectionContainers**](ReplicationMigrationItemsApi.md#replicationMigrationItemsListByReplicationProtectionContainers) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationMigrationItems | Gets the list of migration items in the protection container. |
| [**replicationMigrationItemsMigrate**](ReplicationMigrationItemsApi.md#replicationMigrationItemsMigrate) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationMigrationItems/{migrationItemName}/migrate | Migrate item. |
| [**replicationMigrationItemsTestMigrate**](ReplicationMigrationItemsApi.md#replicationMigrationItemsTestMigrate) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationMigrationItems/{migrationItemName}/testMigrate | Test migrate item. |
| [**replicationMigrationItemsTestMigrateCleanup**](ReplicationMigrationItemsApi.md#replicationMigrationItemsTestMigrateCleanup) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationMigrationItems/{migrationItemName}/testMigrateCleanup | Test migrate cleanup. |
| [**replicationMigrationItemsUpdate**](ReplicationMigrationItemsApi.md#replicationMigrationItemsUpdate) | **PATCH** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationMigrationItems/{migrationItemName} | Updates migration item. |


<a id="replicationMigrationItemsCreate"></a>
# **replicationMigrationItemsCreate**
> MigrationItem replicationMigrationItemsCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, migrationItemName, input)

Enables migration.

The operation to create an ASR migration item (enable migration).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationMigrationItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationMigrationItemsApi apiInstance = new ReplicationMigrationItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String migrationItemName = "migrationItemName_example"; // String | Migration item name.
    EnableMigrationInput input = new EnableMigrationInput(); // EnableMigrationInput | Enable migration input.
    try {
      MigrationItem result = apiInstance.replicationMigrationItemsCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, migrationItemName, input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationMigrationItemsApi#replicationMigrationItemsCreate");
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
| **migrationItemName** | **String**| Migration item name. | |
| **input** | [**EnableMigrationInput**](EnableMigrationInput.md)| Enable migration input. | |

### Return type

[**MigrationItem**](MigrationItem.md)

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

<a id="replicationMigrationItemsDelete"></a>
# **replicationMigrationItemsDelete**
> replicationMigrationItemsDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, migrationItemName, deleteOption)

Delete the migration item.

The operation to delete an ASR migration item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationMigrationItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationMigrationItemsApi apiInstance = new ReplicationMigrationItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String migrationItemName = "migrationItemName_example"; // String | Migration item name.
    String deleteOption = "deleteOption_example"; // String | The delete option.
    try {
      apiInstance.replicationMigrationItemsDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, migrationItemName, deleteOption);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationMigrationItemsApi#replicationMigrationItemsDelete");
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
| **migrationItemName** | **String**| Migration item name. | |
| **deleteOption** | **String**| The delete option. | [optional] |

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

<a id="replicationMigrationItemsGet"></a>
# **replicationMigrationItemsGet**
> MigrationItem replicationMigrationItemsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, migrationItemName)

Gets the details of a migration item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationMigrationItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationMigrationItemsApi apiInstance = new ReplicationMigrationItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric unique name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String migrationItemName = "migrationItemName_example"; // String | Migration item name.
    try {
      MigrationItem result = apiInstance.replicationMigrationItemsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, migrationItemName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationMigrationItemsApi#replicationMigrationItemsGet");
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

[**MigrationItem**](MigrationItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationMigrationItemsList"></a>
# **replicationMigrationItemsList**
> MigrationItemCollection replicationMigrationItemsList(apiVersion, resourceName, resourceGroupName, subscriptionId, skipToken, $filter)

Gets the list of migration items in the vault.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationMigrationItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationMigrationItemsApi apiInstance = new ReplicationMigrationItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String skipToken = "skipToken_example"; // String | The pagination token.
    String $filter = "$filter_example"; // String | OData filter options.
    try {
      MigrationItemCollection result = apiInstance.replicationMigrationItemsList(apiVersion, resourceName, resourceGroupName, subscriptionId, skipToken, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationMigrationItemsApi#replicationMigrationItemsList");
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
| **skipToken** | **String**| The pagination token. | [optional] |
| **$filter** | **String**| OData filter options. | [optional] |

### Return type

[**MigrationItemCollection**](MigrationItemCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationMigrationItemsListByReplicationProtectionContainers"></a>
# **replicationMigrationItemsListByReplicationProtectionContainers**
> MigrationItemCollection replicationMigrationItemsListByReplicationProtectionContainers(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName)

Gets the list of migration items in the protection container.

Gets the list of ASR migration items in the protection container.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationMigrationItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationMigrationItemsApi apiInstance = new ReplicationMigrationItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    try {
      MigrationItemCollection result = apiInstance.replicationMigrationItemsListByReplicationProtectionContainers(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationMigrationItemsApi#replicationMigrationItemsListByReplicationProtectionContainers");
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

[**MigrationItemCollection**](MigrationItemCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationMigrationItemsMigrate"></a>
# **replicationMigrationItemsMigrate**
> MigrationItem replicationMigrationItemsMigrate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, migrationItemName, migrateInput)

Migrate item.

The operation to initiate migration of the item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationMigrationItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationMigrationItemsApi apiInstance = new ReplicationMigrationItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String migrationItemName = "migrationItemName_example"; // String | Migration item name.
    MigrateInput migrateInput = new MigrateInput(); // MigrateInput | Migrate input.
    try {
      MigrationItem result = apiInstance.replicationMigrationItemsMigrate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, migrationItemName, migrateInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationMigrationItemsApi#replicationMigrationItemsMigrate");
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
| **migrationItemName** | **String**| Migration item name. | |
| **migrateInput** | [**MigrateInput**](MigrateInput.md)| Migrate input. | |

### Return type

[**MigrationItem**](MigrationItem.md)

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

<a id="replicationMigrationItemsTestMigrate"></a>
# **replicationMigrationItemsTestMigrate**
> MigrationItem replicationMigrationItemsTestMigrate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, migrationItemName, testMigrateInput)

Test migrate item.

The operation to initiate test migration of the item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationMigrationItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationMigrationItemsApi apiInstance = new ReplicationMigrationItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String migrationItemName = "migrationItemName_example"; // String | Migration item name.
    TestMigrateInput testMigrateInput = new TestMigrateInput(); // TestMigrateInput | Test migrate input.
    try {
      MigrationItem result = apiInstance.replicationMigrationItemsTestMigrate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, migrationItemName, testMigrateInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationMigrationItemsApi#replicationMigrationItemsTestMigrate");
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
| **migrationItemName** | **String**| Migration item name. | |
| **testMigrateInput** | [**TestMigrateInput**](TestMigrateInput.md)| Test migrate input. | |

### Return type

[**MigrationItem**](MigrationItem.md)

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

<a id="replicationMigrationItemsTestMigrateCleanup"></a>
# **replicationMigrationItemsTestMigrateCleanup**
> MigrationItem replicationMigrationItemsTestMigrateCleanup(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, migrationItemName, testMigrateCleanupInput)

Test migrate cleanup.

The operation to initiate test migrate cleanup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationMigrationItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationMigrationItemsApi apiInstance = new ReplicationMigrationItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String migrationItemName = "migrationItemName_example"; // String | Migration item name.
    TestMigrateCleanupInput testMigrateCleanupInput = new TestMigrateCleanupInput(); // TestMigrateCleanupInput | Test migrate cleanup input.
    try {
      MigrationItem result = apiInstance.replicationMigrationItemsTestMigrateCleanup(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, migrationItemName, testMigrateCleanupInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationMigrationItemsApi#replicationMigrationItemsTestMigrateCleanup");
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
| **migrationItemName** | **String**| Migration item name. | |
| **testMigrateCleanupInput** | [**TestMigrateCleanupInput**](TestMigrateCleanupInput.md)| Test migrate cleanup input. | |

### Return type

[**MigrationItem**](MigrationItem.md)

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

<a id="replicationMigrationItemsUpdate"></a>
# **replicationMigrationItemsUpdate**
> MigrationItem replicationMigrationItemsUpdate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, migrationItemName, input)

Updates migration item.

The operation to update the recovery settings of an ASR migration item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationMigrationItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationMigrationItemsApi apiInstance = new ReplicationMigrationItemsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String fabricName = "fabricName_example"; // String | Fabric name.
    String protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
    String migrationItemName = "migrationItemName_example"; // String | Migration item name.
    UpdateMigrationItemInput input = new UpdateMigrationItemInput(); // UpdateMigrationItemInput | Update migration item input.
    try {
      MigrationItem result = apiInstance.replicationMigrationItemsUpdate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, migrationItemName, input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationMigrationItemsApi#replicationMigrationItemsUpdate");
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
| **migrationItemName** | **String**| Migration item name. | |
| **input** | [**UpdateMigrationItemInput**](UpdateMigrationItemInput.md)| Update migration item input. | |

### Return type

[**MigrationItem**](MigrationItem.md)

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

