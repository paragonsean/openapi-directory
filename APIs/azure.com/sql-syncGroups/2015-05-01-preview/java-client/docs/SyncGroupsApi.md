# SyncGroupsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**syncGroupsCancelSync**](SyncGroupsApi.md#syncGroupsCancelSync) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName}/cancelSync |  |
| [**syncGroupsCreateOrUpdate**](SyncGroupsApi.md#syncGroupsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName} |  |
| [**syncGroupsDelete**](SyncGroupsApi.md#syncGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName} |  |
| [**syncGroupsGet**](SyncGroupsApi.md#syncGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName} |  |
| [**syncGroupsListByDatabase**](SyncGroupsApi.md#syncGroupsListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups |  |
| [**syncGroupsListHubSchemas**](SyncGroupsApi.md#syncGroupsListHubSchemas) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName}/hubSchemas |  |
| [**syncGroupsListLogs**](SyncGroupsApi.md#syncGroupsListLogs) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName}/logs |  |
| [**syncGroupsListSyncDatabaseIds**](SyncGroupsApi.md#syncGroupsListSyncDatabaseIds) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/syncDatabaseIds |  |
| [**syncGroupsRefreshHubSchema**](SyncGroupsApi.md#syncGroupsRefreshHubSchema) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName}/refreshHubSchema |  |
| [**syncGroupsTriggerSync**](SyncGroupsApi.md#syncGroupsTriggerSync) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName}/triggerSync |  |
| [**syncGroupsUpdate**](SyncGroupsApi.md#syncGroupsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName} |  |


<a id="syncGroupsCancelSync"></a>
# **syncGroupsCancelSync**
> syncGroupsCancelSync(resourceGroupName, serverName, databaseName, syncGroupName, subscriptionId, apiVersion)



Cancels a sync group synchronization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SyncGroupsApi apiInstance = new SyncGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
    String syncGroupName = "syncGroupName_example"; // String | The name of the sync group.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.syncGroupsCancelSync(resourceGroupName, serverName, databaseName, syncGroupName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncGroupsApi#syncGroupsCancelSync");
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
| **serverName** | **String**| The name of the server. | |
| **databaseName** | **String**| The name of the database on which the sync group is hosted. | |
| **syncGroupName** | **String**| The name of the sync group. | |
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
| **200** | Successfully cancel a sync group synchronization. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidSyncGroupCreateOrUpdateRequest - The create or update sync group request body is empty.   * 400 InvalidSyncMemberCreateOrUpdateRequest - The create or update sync member request body is empty.   * 400 InvalidSyncAgentCreateOrUpdateRequest - The create or update sync agent request body is empty.   * 400 InvalidDatabaseResourceId - Invalid database resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 InvalidSyncAgentResourceId - Invalid sync agent resource identifier.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 InvalidSyncGroup - Sync group is invalid.   * 400 InvalidSyncMetadataDatabase - Sync metadata database is invalid.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 409 CannotCreateSyncGroupDueToQuotaExceeded - Cannot create sync group due to quota exceeded. |  -  |

<a id="syncGroupsCreateOrUpdate"></a>
# **syncGroupsCreateOrUpdate**
> SyncGroup syncGroupsCreateOrUpdate(resourceGroupName, serverName, databaseName, syncGroupName, subscriptionId, apiVersion, parameters)



Creates or updates a sync group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SyncGroupsApi apiInstance = new SyncGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
    String syncGroupName = "syncGroupName_example"; // String | The name of the sync group.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    SyncGroup parameters = new SyncGroup(); // SyncGroup | The requested sync group resource state.
    try {
      SyncGroup result = apiInstance.syncGroupsCreateOrUpdate(resourceGroupName, serverName, databaseName, syncGroupName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncGroupsApi#syncGroupsCreateOrUpdate");
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
| **serverName** | **String**| The name of the server. | |
| **databaseName** | **String**| The name of the database on which the sync group is hosted. | |
| **syncGroupName** | **String**| The name of the sync group. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**SyncGroup**](SyncGroup.md)| The requested sync group resource state. | |

### Return type

[**SyncGroup**](SyncGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the sync group. |  -  |
| **201** | Successfully created the sync group. |  -  |
| **202** | Creating or updating the sync group is in progress. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidSyncGroupCreateOrUpdateRequest - The create or update sync group request body is empty.   * 400 InvalidSyncMemberCreateOrUpdateRequest - The create or update sync member request body is empty.   * 400 InvalidSyncAgentCreateOrUpdateRequest - The create or update sync agent request body is empty.   * 400 InvalidDatabaseResourceId - Invalid database resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 InvalidSyncAgentResourceId - Invalid sync agent resource identifier.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 InvalidSyncGroup - Sync group is invalid.   * 400 InvalidSyncMetadataDatabase - Sync metadata database is invalid.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 409 CannotCreateSyncGroupDueToQuotaExceeded - Cannot create sync group due to quota exceeded. |  -  |

<a id="syncGroupsDelete"></a>
# **syncGroupsDelete**
> syncGroupsDelete(resourceGroupName, serverName, databaseName, syncGroupName, subscriptionId, apiVersion)



Deletes a sync group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SyncGroupsApi apiInstance = new SyncGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
    String syncGroupName = "syncGroupName_example"; // String | The name of the sync group.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.syncGroupsDelete(resourceGroupName, serverName, databaseName, syncGroupName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncGroupsApi#syncGroupsDelete");
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
| **serverName** | **String**| The name of the server. | |
| **databaseName** | **String**| The name of the database on which the sync group is hosted. | |
| **syncGroupName** | **String**| The name of the sync group. | |
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
| **200** | Successfully deleted the sync group. |  -  |
| **202** | Deleting the sync group is in progress. |  -  |
| **204** | The specified sync group does not exist. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidSyncGroupCreateOrUpdateRequest - The create or update sync group request body is empty.   * 400 InvalidSyncMemberCreateOrUpdateRequest - The create or update sync member request body is empty.   * 400 InvalidSyncAgentCreateOrUpdateRequest - The create or update sync agent request body is empty.   * 400 InvalidDatabaseResourceId - Invalid database resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 InvalidSyncAgentResourceId - Invalid sync agent resource identifier.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 InvalidSyncGroup - Sync group is invalid.   * 400 InvalidSyncMetadataDatabase - Sync metadata database is invalid.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 409 CannotCreateSyncGroupDueToQuotaExceeded - Cannot create sync group due to quota exceeded. |  -  |

<a id="syncGroupsGet"></a>
# **syncGroupsGet**
> SyncGroup syncGroupsGet(resourceGroupName, serverName, databaseName, syncGroupName, subscriptionId, apiVersion)



Gets a sync group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SyncGroupsApi apiInstance = new SyncGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
    String syncGroupName = "syncGroupName_example"; // String | The name of the sync group.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      SyncGroup result = apiInstance.syncGroupsGet(resourceGroupName, serverName, databaseName, syncGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncGroupsApi#syncGroupsGet");
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
| **serverName** | **String**| The name of the server. | |
| **databaseName** | **String**| The name of the database on which the sync group is hosted. | |
| **syncGroupName** | **String**| The name of the sync group. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**SyncGroup**](SyncGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the specified sync group. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidSyncGroupCreateOrUpdateRequest - The create or update sync group request body is empty.   * 400 InvalidSyncMemberCreateOrUpdateRequest - The create or update sync member request body is empty.   * 400 InvalidSyncAgentCreateOrUpdateRequest - The create or update sync agent request body is empty.   * 400 InvalidDatabaseResourceId - Invalid database resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 InvalidSyncAgentResourceId - Invalid sync agent resource identifier.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 InvalidSyncGroup - Sync group is invalid.   * 400 InvalidSyncMetadataDatabase - Sync metadata database is invalid.   * 404 ResourceNotFound - The requested resource was not found.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 409 CannotCreateSyncGroupDueToQuotaExceeded - Cannot create sync group due to quota exceeded. |  -  |

<a id="syncGroupsListByDatabase"></a>
# **syncGroupsListByDatabase**
> SyncGroupListResult syncGroupsListByDatabase(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion)



Lists sync groups under a hub database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SyncGroupsApi apiInstance = new SyncGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      SyncGroupListResult result = apiInstance.syncGroupsListByDatabase(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncGroupsApi#syncGroupsListByDatabase");
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
| **serverName** | **String**| The name of the server. | |
| **databaseName** | **String**| The name of the database on which the sync group is hosted. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**SyncGroupListResult**](SyncGroupListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of sync groups. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidSyncGroupCreateOrUpdateRequest - The create or update sync group request body is empty.   * 400 InvalidSyncMemberCreateOrUpdateRequest - The create or update sync member request body is empty.   * 400 InvalidSyncAgentCreateOrUpdateRequest - The create or update sync agent request body is empty.   * 400 InvalidDatabaseResourceId - Invalid database resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 InvalidSyncAgentResourceId - Invalid sync agent resource identifier.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 InvalidSyncGroup - Sync group is invalid.   * 400 InvalidSyncMetadataDatabase - Sync metadata database is invalid.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 409 CannotCreateSyncGroupDueToQuotaExceeded - Cannot create sync group due to quota exceeded. |  -  |

<a id="syncGroupsListHubSchemas"></a>
# **syncGroupsListHubSchemas**
> SyncFullSchemaPropertiesListResult syncGroupsListHubSchemas(resourceGroupName, serverName, databaseName, syncGroupName, subscriptionId, apiVersion)



Gets a collection of hub database schemas.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SyncGroupsApi apiInstance = new SyncGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
    String syncGroupName = "syncGroupName_example"; // String | The name of the sync group.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      SyncFullSchemaPropertiesListResult result = apiInstance.syncGroupsListHubSchemas(resourceGroupName, serverName, databaseName, syncGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncGroupsApi#syncGroupsListHubSchemas");
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
| **serverName** | **String**| The name of the server. | |
| **databaseName** | **String**| The name of the database on which the sync group is hosted. | |
| **syncGroupName** | **String**| The name of the sync group. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**SyncFullSchemaPropertiesListResult**](SyncFullSchemaPropertiesListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully get a sync group hub database schema. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidSyncGroupCreateOrUpdateRequest - The create or update sync group request body is empty.   * 400 InvalidSyncMemberCreateOrUpdateRequest - The create or update sync member request body is empty.   * 400 InvalidSyncAgentCreateOrUpdateRequest - The create or update sync agent request body is empty.   * 400 InvalidDatabaseResourceId - Invalid database resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 InvalidSyncAgentResourceId - Invalid sync agent resource identifier.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 InvalidSyncGroup - Sync group is invalid.   * 400 InvalidSyncMetadataDatabase - Sync metadata database is invalid.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 409 CannotCreateSyncGroupDueToQuotaExceeded - Cannot create sync group due to quota exceeded. |  -  |

<a id="syncGroupsListLogs"></a>
# **syncGroupsListLogs**
> SyncGroupLogListResult syncGroupsListLogs(resourceGroupName, serverName, databaseName, syncGroupName, startTime, endTime, type, subscriptionId, apiVersion, continuationToken)



Gets a collection of sync group logs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SyncGroupsApi apiInstance = new SyncGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
    String syncGroupName = "syncGroupName_example"; // String | The name of the sync group.
    String startTime = "startTime_example"; // String | Get logs generated after this time.
    String endTime = "endTime_example"; // String | Get logs generated before this time.
    String type = "All"; // String | The types of logs to retrieve.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String continuationToken = "continuationToken_example"; // String | The continuation token for this operation.
    try {
      SyncGroupLogListResult result = apiInstance.syncGroupsListLogs(resourceGroupName, serverName, databaseName, syncGroupName, startTime, endTime, type, subscriptionId, apiVersion, continuationToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncGroupsApi#syncGroupsListLogs");
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
| **serverName** | **String**| The name of the server. | |
| **databaseName** | **String**| The name of the database on which the sync group is hosted. | |
| **syncGroupName** | **String**| The name of the sync group. | |
| **startTime** | **String**| Get logs generated after this time. | |
| **endTime** | **String**| Get logs generated before this time. | |
| **type** | **String**| The types of logs to retrieve. | [enum: All, Error, Warning, Success] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **continuationToken** | **String**| The continuation token for this operation. | [optional] |

### Return type

[**SyncGroupLogListResult**](SyncGroupLogListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved sync group logs. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidSyncGroupCreateOrUpdateRequest - The create or update sync group request body is empty.   * 400 InvalidSyncMemberCreateOrUpdateRequest - The create or update sync member request body is empty.   * 400 InvalidSyncAgentCreateOrUpdateRequest - The create or update sync agent request body is empty.   * 400 InvalidDatabaseResourceId - Invalid database resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 InvalidSyncAgentResourceId - Invalid sync agent resource identifier.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 InvalidSyncGroup - Sync group is invalid.   * 400 InvalidSyncMetadataDatabase - Sync metadata database is invalid.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 409 CannotCreateSyncGroupDueToQuotaExceeded - Cannot create sync group due to quota exceeded. |  -  |

<a id="syncGroupsListSyncDatabaseIds"></a>
# **syncGroupsListSyncDatabaseIds**
> SyncDatabaseIdListResult syncGroupsListSyncDatabaseIds(locationName, subscriptionId, apiVersion)



Gets a collection of sync database ids.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SyncGroupsApi apiInstance = new SyncGroupsApi(defaultClient);
    String locationName = "locationName_example"; // String | The name of the region where the resource is located.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      SyncDatabaseIdListResult result = apiInstance.syncGroupsListSyncDatabaseIds(locationName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncGroupsApi#syncGroupsListSyncDatabaseIds");
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
| **locationName** | **String**| The name of the region where the resource is located. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**SyncDatabaseIdListResult**](SyncDatabaseIdListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved collection of sync database ids. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidSyncGroupCreateOrUpdateRequest - The create or update sync group request body is empty.   * 400 InvalidSyncMemberCreateOrUpdateRequest - The create or update sync member request body is empty.   * 400 InvalidSyncAgentCreateOrUpdateRequest - The create or update sync agent request body is empty.   * 400 InvalidDatabaseResourceId - Invalid database resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 InvalidSyncAgentResourceId - Invalid sync agent resource identifier.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance. |  -  |

<a id="syncGroupsRefreshHubSchema"></a>
# **syncGroupsRefreshHubSchema**
> syncGroupsRefreshHubSchema(resourceGroupName, serverName, databaseName, syncGroupName, subscriptionId, apiVersion)



Refreshes a hub database schema.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SyncGroupsApi apiInstance = new SyncGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
    String syncGroupName = "syncGroupName_example"; // String | The name of the sync group.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.syncGroupsRefreshHubSchema(resourceGroupName, serverName, databaseName, syncGroupName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncGroupsApi#syncGroupsRefreshHubSchema");
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
| **serverName** | **String**| The name of the server. | |
| **databaseName** | **String**| The name of the database on which the sync group is hosted. | |
| **syncGroupName** | **String**| The name of the sync group. | |
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
| **200** | Successfully refreshed a sync hub schema. |  -  |
| **202** | The sync hub schema refresh operation is on going. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidSyncGroupCreateOrUpdateRequest - The create or update sync group request body is empty.   * 400 InvalidSyncMemberCreateOrUpdateRequest - The create or update sync member request body is empty.   * 400 InvalidSyncAgentCreateOrUpdateRequest - The create or update sync agent request body is empty.   * 400 InvalidDatabaseResourceId - Invalid database resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 InvalidSyncAgentResourceId - Invalid sync agent resource identifier.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 InvalidSyncGroup - Sync group is invalid.   * 400 InvalidSyncMetadataDatabase - Sync metadata database is invalid.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 409 CannotCreateSyncGroupDueToQuotaExceeded - Cannot create sync group due to quota exceeded. |  -  |

<a id="syncGroupsTriggerSync"></a>
# **syncGroupsTriggerSync**
> syncGroupsTriggerSync(resourceGroupName, serverName, databaseName, syncGroupName, subscriptionId, apiVersion)



Triggers a sync group synchronization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SyncGroupsApi apiInstance = new SyncGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
    String syncGroupName = "syncGroupName_example"; // String | The name of the sync group.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.syncGroupsTriggerSync(resourceGroupName, serverName, databaseName, syncGroupName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncGroupsApi#syncGroupsTriggerSync");
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
| **serverName** | **String**| The name of the server. | |
| **databaseName** | **String**| The name of the database on which the sync group is hosted. | |
| **syncGroupName** | **String**| The name of the sync group. | |
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
| **200** | Successfully triggered a sync group synchronization. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidSyncGroupCreateOrUpdateRequest - The create or update sync group request body is empty.   * 400 InvalidSyncMemberCreateOrUpdateRequest - The create or update sync member request body is empty.   * 400 InvalidSyncAgentCreateOrUpdateRequest - The create or update sync agent request body is empty.   * 400 InvalidDatabaseResourceId - Invalid database resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 InvalidSyncAgentResourceId - Invalid sync agent resource identifier.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 InvalidSyncGroup - Sync group is invalid.   * 400 InvalidSyncMetadataDatabase - Sync metadata database is invalid.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 409 CannotCreateSyncGroupDueToQuotaExceeded - Cannot create sync group due to quota exceeded. |  -  |

<a id="syncGroupsUpdate"></a>
# **syncGroupsUpdate**
> SyncGroup syncGroupsUpdate(resourceGroupName, serverName, databaseName, syncGroupName, subscriptionId, apiVersion, parameters)



Updates a sync group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SyncGroupsApi apiInstance = new SyncGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
    String syncGroupName = "syncGroupName_example"; // String | The name of the sync group.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    SyncGroup parameters = new SyncGroup(); // SyncGroup | The requested sync group resource state.
    try {
      SyncGroup result = apiInstance.syncGroupsUpdate(resourceGroupName, serverName, databaseName, syncGroupName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncGroupsApi#syncGroupsUpdate");
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
| **serverName** | **String**| The name of the server. | |
| **databaseName** | **String**| The name of the database on which the sync group is hosted. | |
| **syncGroupName** | **String**| The name of the sync group. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**SyncGroup**](SyncGroup.md)| The requested sync group resource state. | |

### Return type

[**SyncGroup**](SyncGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the sync group. |  -  |
| **202** | Updating the sync group is in progress. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidSyncGroupCreateOrUpdateRequest - The create or update sync group request body is empty.   * 400 InvalidSyncMemberCreateOrUpdateRequest - The create or update sync member request body is empty.   * 400 InvalidSyncAgentCreateOrUpdateRequest - The create or update sync agent request body is empty.   * 400 InvalidDatabaseResourceId - Invalid database resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 InvalidSyncAgentResourceId - Invalid sync agent resource identifier.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 InvalidSyncGroup - Sync group is invalid.   * 400 InvalidSyncMetadataDatabase - Sync metadata database is invalid.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 409 CannotCreateSyncGroupDueToQuotaExceeded - Cannot create sync group due to quota exceeded. |  -  |

