# LongTermRetentionBackupsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**longTermRetentionBackupsDelete**](LongTermRetentionBackupsApi.md#longTermRetentionBackupsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionServers/{longTermRetentionServerName}/longTermRetentionDatabases/{longTermRetentionDatabaseName}/longTermRetentionBackups/{backupName} |  |
| [**longTermRetentionBackupsDeleteByResourceGroup**](LongTermRetentionBackupsApi.md#longTermRetentionBackupsDeleteByResourceGroup) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionServers/{longTermRetentionServerName}/longTermRetentionDatabases/{longTermRetentionDatabaseName}/longTermRetentionBackups/{backupName} |  |
| [**longTermRetentionBackupsGet**](LongTermRetentionBackupsApi.md#longTermRetentionBackupsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionServers/{longTermRetentionServerName}/longTermRetentionDatabases/{longTermRetentionDatabaseName}/longTermRetentionBackups/{backupName} |  |
| [**longTermRetentionBackupsGetByResourceGroup**](LongTermRetentionBackupsApi.md#longTermRetentionBackupsGetByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionServers/{longTermRetentionServerName}/longTermRetentionDatabases/{longTermRetentionDatabaseName}/longTermRetentionBackups/{backupName} |  |
| [**longTermRetentionBackupsListByDatabase**](LongTermRetentionBackupsApi.md#longTermRetentionBackupsListByDatabase) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionServers/{longTermRetentionServerName}/longTermRetentionDatabases/{longTermRetentionDatabaseName}/longTermRetentionBackups |  |
| [**longTermRetentionBackupsListByLocation**](LongTermRetentionBackupsApi.md#longTermRetentionBackupsListByLocation) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionBackups |  |
| [**longTermRetentionBackupsListByResourceGroupDatabase**](LongTermRetentionBackupsApi.md#longTermRetentionBackupsListByResourceGroupDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionServers/{longTermRetentionServerName}/longTermRetentionDatabases/{longTermRetentionDatabaseName}/longTermRetentionBackups |  |
| [**longTermRetentionBackupsListByResourceGroupLocation**](LongTermRetentionBackupsApi.md#longTermRetentionBackupsListByResourceGroupLocation) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionBackups |  |
| [**longTermRetentionBackupsListByResourceGroupServer**](LongTermRetentionBackupsApi.md#longTermRetentionBackupsListByResourceGroupServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionServers/{longTermRetentionServerName}/longTermRetentionBackups |  |
| [**longTermRetentionBackupsListByServer**](LongTermRetentionBackupsApi.md#longTermRetentionBackupsListByServer) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/longTermRetentionServers/{longTermRetentionServerName}/longTermRetentionBackups |  |


<a id="longTermRetentionBackupsDelete"></a>
# **longTermRetentionBackupsDelete**
> longTermRetentionBackupsDelete(locationName, longTermRetentionServerName, longTermRetentionDatabaseName, backupName, subscriptionId, apiVersion)



Deletes a long term retention backup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongTermRetentionBackupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LongTermRetentionBackupsApi apiInstance = new LongTermRetentionBackupsApi(defaultClient);
    String locationName = "locationName_example"; // String | The location of the database
    String longTermRetentionServerName = "longTermRetentionServerName_example"; // String | The name of the server
    String longTermRetentionDatabaseName = "longTermRetentionDatabaseName_example"; // String | The name of the database
    String backupName = "backupName_example"; // String | The backup name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.longTermRetentionBackupsDelete(locationName, longTermRetentionServerName, longTermRetentionDatabaseName, backupName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongTermRetentionBackupsApi#longTermRetentionBackupsDelete");
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
| **locationName** | **String**| The location of the database | |
| **longTermRetentionServerName** | **String**| The name of the server | |
| **longTermRetentionDatabaseName** | **String**| The name of the database | |
| **backupName** | **String**| The backup name. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted the backup. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidLongTermRetentionBackupId - Invalid long term retention backup identifier.   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

<a id="longTermRetentionBackupsDeleteByResourceGroup"></a>
# **longTermRetentionBackupsDeleteByResourceGroup**
> longTermRetentionBackupsDeleteByResourceGroup(resourceGroupName, locationName, longTermRetentionServerName, longTermRetentionDatabaseName, backupName, subscriptionId, apiVersion)



Deletes a long term retention backup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongTermRetentionBackupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LongTermRetentionBackupsApi apiInstance = new LongTermRetentionBackupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String locationName = "locationName_example"; // String | The location of the database
    String longTermRetentionServerName = "longTermRetentionServerName_example"; // String | The name of the server
    String longTermRetentionDatabaseName = "longTermRetentionDatabaseName_example"; // String | The name of the database
    String backupName = "backupName_example"; // String | The backup name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.longTermRetentionBackupsDeleteByResourceGroup(resourceGroupName, locationName, longTermRetentionServerName, longTermRetentionDatabaseName, backupName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongTermRetentionBackupsApi#longTermRetentionBackupsDeleteByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **locationName** | **String**| The location of the database | |
| **longTermRetentionServerName** | **String**| The name of the server | |
| **longTermRetentionDatabaseName** | **String**| The name of the database | |
| **backupName** | **String**| The backup name. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted the backup. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidLongTermRetentionBackupId - Invalid long term retention backup identifier.   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

<a id="longTermRetentionBackupsGet"></a>
# **longTermRetentionBackupsGet**
> LongTermRetentionBackup longTermRetentionBackupsGet(locationName, longTermRetentionServerName, longTermRetentionDatabaseName, backupName, subscriptionId, apiVersion)



Gets a long term retention backup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongTermRetentionBackupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LongTermRetentionBackupsApi apiInstance = new LongTermRetentionBackupsApi(defaultClient);
    String locationName = "locationName_example"; // String | The location of the database.
    String longTermRetentionServerName = "longTermRetentionServerName_example"; // String | The name of the server
    String longTermRetentionDatabaseName = "longTermRetentionDatabaseName_example"; // String | The name of the database
    String backupName = "backupName_example"; // String | The backup name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      LongTermRetentionBackup result = apiInstance.longTermRetentionBackupsGet(locationName, longTermRetentionServerName, longTermRetentionDatabaseName, backupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongTermRetentionBackupsApi#longTermRetentionBackupsGet");
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
| **locationName** | **String**| The location of the database. | |
| **longTermRetentionServerName** | **String**| The name of the server | |
| **longTermRetentionDatabaseName** | **String**| The name of the database | |
| **backupName** | **String**| The backup name. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**LongTermRetentionBackup**](LongTermRetentionBackup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the backup. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidLongTermRetentionBackupId - Invalid long term retention backup identifier.   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found. |  -  |

<a id="longTermRetentionBackupsGetByResourceGroup"></a>
# **longTermRetentionBackupsGetByResourceGroup**
> LongTermRetentionBackup longTermRetentionBackupsGetByResourceGroup(resourceGroupName, locationName, longTermRetentionServerName, longTermRetentionDatabaseName, backupName, subscriptionId, apiVersion)



Gets a long term retention backup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongTermRetentionBackupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LongTermRetentionBackupsApi apiInstance = new LongTermRetentionBackupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String locationName = "locationName_example"; // String | The location of the database.
    String longTermRetentionServerName = "longTermRetentionServerName_example"; // String | The name of the server
    String longTermRetentionDatabaseName = "longTermRetentionDatabaseName_example"; // String | The name of the database
    String backupName = "backupName_example"; // String | The backup name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      LongTermRetentionBackup result = apiInstance.longTermRetentionBackupsGetByResourceGroup(resourceGroupName, locationName, longTermRetentionServerName, longTermRetentionDatabaseName, backupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongTermRetentionBackupsApi#longTermRetentionBackupsGetByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **locationName** | **String**| The location of the database. | |
| **longTermRetentionServerName** | **String**| The name of the server | |
| **longTermRetentionDatabaseName** | **String**| The name of the database | |
| **backupName** | **String**| The backup name. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**LongTermRetentionBackup**](LongTermRetentionBackup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the backup. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidLongTermRetentionBackupId - Invalid long term retention backup identifier.   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found. |  -  |

<a id="longTermRetentionBackupsListByDatabase"></a>
# **longTermRetentionBackupsListByDatabase**
> LongTermRetentionBackupListResult longTermRetentionBackupsListByDatabase(locationName, longTermRetentionServerName, longTermRetentionDatabaseName, subscriptionId, apiVersion, onlyLatestPerDatabase, databaseState)



Lists all long term retention backups for a database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongTermRetentionBackupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LongTermRetentionBackupsApi apiInstance = new LongTermRetentionBackupsApi(defaultClient);
    String locationName = "locationName_example"; // String | The location of the database
    String longTermRetentionServerName = "longTermRetentionServerName_example"; // String | The name of the server
    String longTermRetentionDatabaseName = "longTermRetentionDatabaseName_example"; // String | The name of the database
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    Boolean onlyLatestPerDatabase = true; // Boolean | Whether or not to only get the latest backup for each database.
    String databaseState = "All"; // String | Whether to query against just live databases, just deleted databases, or all databases.
    try {
      LongTermRetentionBackupListResult result = apiInstance.longTermRetentionBackupsListByDatabase(locationName, longTermRetentionServerName, longTermRetentionDatabaseName, subscriptionId, apiVersion, onlyLatestPerDatabase, databaseState);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongTermRetentionBackupsApi#longTermRetentionBackupsListByDatabase");
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
| **locationName** | **String**| The location of the database | |
| **longTermRetentionServerName** | **String**| The name of the server | |
| **longTermRetentionDatabaseName** | **String**| The name of the database | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **onlyLatestPerDatabase** | **Boolean**| Whether or not to only get the latest backup for each database. | [optional] |
| **databaseState** | **String**| Whether to query against just live databases, just deleted databases, or all databases. | [optional] [enum: All, Live, Deleted] |

### Return type

[**LongTermRetentionBackupListResult**](LongTermRetentionBackupListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of backups. |  -  |
| **0** | *** Error Responses: ***   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

<a id="longTermRetentionBackupsListByLocation"></a>
# **longTermRetentionBackupsListByLocation**
> LongTermRetentionBackupListResult longTermRetentionBackupsListByLocation(locationName, subscriptionId, apiVersion, onlyLatestPerDatabase, databaseState)



Lists the long term retention backups for a given location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongTermRetentionBackupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LongTermRetentionBackupsApi apiInstance = new LongTermRetentionBackupsApi(defaultClient);
    String locationName = "locationName_example"; // String | The location of the database
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    Boolean onlyLatestPerDatabase = true; // Boolean | Whether or not to only get the latest backup for each database.
    String databaseState = "All"; // String | Whether to query against just live databases, just deleted databases, or all databases.
    try {
      LongTermRetentionBackupListResult result = apiInstance.longTermRetentionBackupsListByLocation(locationName, subscriptionId, apiVersion, onlyLatestPerDatabase, databaseState);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongTermRetentionBackupsApi#longTermRetentionBackupsListByLocation");
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
| **locationName** | **String**| The location of the database | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **onlyLatestPerDatabase** | **Boolean**| Whether or not to only get the latest backup for each database. | [optional] |
| **databaseState** | **String**| Whether to query against just live databases, just deleted databases, or all databases. | [optional] [enum: All, Live, Deleted] |

### Return type

[**LongTermRetentionBackupListResult**](LongTermRetentionBackupListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of backups. |  -  |
| **0** | *** Error Responses: ***   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

<a id="longTermRetentionBackupsListByResourceGroupDatabase"></a>
# **longTermRetentionBackupsListByResourceGroupDatabase**
> LongTermRetentionBackupListResult longTermRetentionBackupsListByResourceGroupDatabase(resourceGroupName, locationName, longTermRetentionServerName, longTermRetentionDatabaseName, subscriptionId, apiVersion, onlyLatestPerDatabase, databaseState)



Lists all long term retention backups for a database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongTermRetentionBackupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LongTermRetentionBackupsApi apiInstance = new LongTermRetentionBackupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String locationName = "locationName_example"; // String | The location of the database
    String longTermRetentionServerName = "longTermRetentionServerName_example"; // String | The name of the server
    String longTermRetentionDatabaseName = "longTermRetentionDatabaseName_example"; // String | The name of the database
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    Boolean onlyLatestPerDatabase = true; // Boolean | Whether or not to only get the latest backup for each database.
    String databaseState = "All"; // String | Whether to query against just live databases, just deleted databases, or all databases.
    try {
      LongTermRetentionBackupListResult result = apiInstance.longTermRetentionBackupsListByResourceGroupDatabase(resourceGroupName, locationName, longTermRetentionServerName, longTermRetentionDatabaseName, subscriptionId, apiVersion, onlyLatestPerDatabase, databaseState);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongTermRetentionBackupsApi#longTermRetentionBackupsListByResourceGroupDatabase");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **locationName** | **String**| The location of the database | |
| **longTermRetentionServerName** | **String**| The name of the server | |
| **longTermRetentionDatabaseName** | **String**| The name of the database | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **onlyLatestPerDatabase** | **Boolean**| Whether or not to only get the latest backup for each database. | [optional] |
| **databaseState** | **String**| Whether to query against just live databases, just deleted databases, or all databases. | [optional] [enum: All, Live, Deleted] |

### Return type

[**LongTermRetentionBackupListResult**](LongTermRetentionBackupListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of backups. |  -  |
| **0** | *** Error Responses: ***   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

<a id="longTermRetentionBackupsListByResourceGroupLocation"></a>
# **longTermRetentionBackupsListByResourceGroupLocation**
> LongTermRetentionBackupListResult longTermRetentionBackupsListByResourceGroupLocation(resourceGroupName, locationName, subscriptionId, apiVersion, onlyLatestPerDatabase, databaseState)



Lists the long term retention backups for a given location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongTermRetentionBackupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LongTermRetentionBackupsApi apiInstance = new LongTermRetentionBackupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String locationName = "locationName_example"; // String | The location of the database
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    Boolean onlyLatestPerDatabase = true; // Boolean | Whether or not to only get the latest backup for each database.
    String databaseState = "All"; // String | Whether to query against just live databases, just deleted databases, or all databases.
    try {
      LongTermRetentionBackupListResult result = apiInstance.longTermRetentionBackupsListByResourceGroupLocation(resourceGroupName, locationName, subscriptionId, apiVersion, onlyLatestPerDatabase, databaseState);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongTermRetentionBackupsApi#longTermRetentionBackupsListByResourceGroupLocation");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **locationName** | **String**| The location of the database | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **onlyLatestPerDatabase** | **Boolean**| Whether or not to only get the latest backup for each database. | [optional] |
| **databaseState** | **String**| Whether to query against just live databases, just deleted databases, or all databases. | [optional] [enum: All, Live, Deleted] |

### Return type

[**LongTermRetentionBackupListResult**](LongTermRetentionBackupListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of backups. |  -  |
| **0** | *** Error Responses: ***   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

<a id="longTermRetentionBackupsListByResourceGroupServer"></a>
# **longTermRetentionBackupsListByResourceGroupServer**
> LongTermRetentionBackupListResult longTermRetentionBackupsListByResourceGroupServer(resourceGroupName, locationName, longTermRetentionServerName, subscriptionId, apiVersion, onlyLatestPerDatabase, databaseState)



Lists the long term retention backups for a given server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongTermRetentionBackupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LongTermRetentionBackupsApi apiInstance = new LongTermRetentionBackupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String locationName = "locationName_example"; // String | The location of the database
    String longTermRetentionServerName = "longTermRetentionServerName_example"; // String | The name of the server
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    Boolean onlyLatestPerDatabase = true; // Boolean | Whether or not to only get the latest backup for each database.
    String databaseState = "All"; // String | Whether to query against just live databases, just deleted databases, or all databases.
    try {
      LongTermRetentionBackupListResult result = apiInstance.longTermRetentionBackupsListByResourceGroupServer(resourceGroupName, locationName, longTermRetentionServerName, subscriptionId, apiVersion, onlyLatestPerDatabase, databaseState);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongTermRetentionBackupsApi#longTermRetentionBackupsListByResourceGroupServer");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **locationName** | **String**| The location of the database | |
| **longTermRetentionServerName** | **String**| The name of the server | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **onlyLatestPerDatabase** | **Boolean**| Whether or not to only get the latest backup for each database. | [optional] |
| **databaseState** | **String**| Whether to query against just live databases, just deleted databases, or all databases. | [optional] [enum: All, Live, Deleted] |

### Return type

[**LongTermRetentionBackupListResult**](LongTermRetentionBackupListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of backups. |  -  |
| **0** | *** Error Responses: ***   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

<a id="longTermRetentionBackupsListByServer"></a>
# **longTermRetentionBackupsListByServer**
> LongTermRetentionBackupListResult longTermRetentionBackupsListByServer(locationName, longTermRetentionServerName, subscriptionId, apiVersion, onlyLatestPerDatabase, databaseState)



Lists the long term retention backups for a given server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongTermRetentionBackupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LongTermRetentionBackupsApi apiInstance = new LongTermRetentionBackupsApi(defaultClient);
    String locationName = "locationName_example"; // String | The location of the database
    String longTermRetentionServerName = "longTermRetentionServerName_example"; // String | The name of the server
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    Boolean onlyLatestPerDatabase = true; // Boolean | Whether or not to only get the latest backup for each database.
    String databaseState = "All"; // String | Whether to query against just live databases, just deleted databases, or all databases.
    try {
      LongTermRetentionBackupListResult result = apiInstance.longTermRetentionBackupsListByServer(locationName, longTermRetentionServerName, subscriptionId, apiVersion, onlyLatestPerDatabase, databaseState);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongTermRetentionBackupsApi#longTermRetentionBackupsListByServer");
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
| **locationName** | **String**| The location of the database | |
| **longTermRetentionServerName** | **String**| The name of the server | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **onlyLatestPerDatabase** | **Boolean**| Whether or not to only get the latest backup for each database. | [optional] |
| **databaseState** | **String**| Whether to query against just live databases, just deleted databases, or all databases. | [optional] [enum: All, Live, Deleted] |

### Return type

[**LongTermRetentionBackupListResult**](LongTermRetentionBackupListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of backups. |  -  |
| **0** | *** Error Responses: ***   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

