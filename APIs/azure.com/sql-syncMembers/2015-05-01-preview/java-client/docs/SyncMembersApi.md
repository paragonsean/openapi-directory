# SyncMembersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**syncMembersCreateOrUpdate**](SyncMembersApi.md#syncMembersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName}/syncMembers/{syncMemberName} |  |
| [**syncMembersDelete**](SyncMembersApi.md#syncMembersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName}/syncMembers/{syncMemberName} |  |
| [**syncMembersGet**](SyncMembersApi.md#syncMembersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName}/syncMembers/{syncMemberName} |  |
| [**syncMembersListBySyncGroup**](SyncMembersApi.md#syncMembersListBySyncGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName}/syncMembers |  |
| [**syncMembersListMemberSchemas**](SyncMembersApi.md#syncMembersListMemberSchemas) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName}/syncMembers/{syncMemberName}/schemas |  |
| [**syncMembersRefreshMemberSchema**](SyncMembersApi.md#syncMembersRefreshMemberSchema) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName}/syncMembers/{syncMemberName}/refreshSchema |  |
| [**syncMembersUpdate**](SyncMembersApi.md#syncMembersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName}/syncMembers/{syncMemberName} |  |


<a id="syncMembersCreateOrUpdate"></a>
# **syncMembersCreateOrUpdate**
> SyncMember syncMembersCreateOrUpdate(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion, parameters)



Creates or updates a sync member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SyncMembersApi apiInstance = new SyncMembersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
    String syncGroupName = "syncGroupName_example"; // String | The name of the sync group on which the sync member is hosted.
    String syncMemberName = "syncMemberName_example"; // String | The name of the sync member.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    SyncMember parameters = new SyncMember(); // SyncMember | The requested sync member resource state.
    try {
      SyncMember result = apiInstance.syncMembersCreateOrUpdate(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncMembersApi#syncMembersCreateOrUpdate");
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
| **syncGroupName** | **String**| The name of the sync group on which the sync member is hosted. | |
| **syncMemberName** | **String**| The name of the sync member. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**SyncMember**](SyncMember.md)| The requested sync member resource state. | |

### Return type

[**SyncMember**](SyncMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the sync member. |  -  |
| **201** | Successfully created the sync member. |  -  |
| **202** | Creating or updating the sync member is in progress. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidSyncGroupCreateOrUpdateRequest - The create or update sync group request body is empty.   * 400 InvalidSyncMemberCreateOrUpdateRequest - The create or update sync member request body is empty.   * 400 InvalidSyncAgentCreateOrUpdateRequest - The create or update sync agent request body is empty.   * 400 InvalidDatabaseResourceId - Invalid database resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 InvalidSyncAgentResourceId - Invalid sync agent resource identifier.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 InvalidSyncGroup - Sync group is invalid.   * 400 InvalidSyncMember - Sync member is invalid.   * 400 InvalidSyncAgent - Sync agent is invalid.   * 400 InvalidSyncMetadataDatabase - Sync metadata database is invalid.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 409 CannotCreateSyncMemberDueToQuotaExceeded - Cannot create sync member due to quota exceeded. |  -  |

<a id="syncMembersDelete"></a>
# **syncMembersDelete**
> syncMembersDelete(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion)



Deletes a sync member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SyncMembersApi apiInstance = new SyncMembersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
    String syncGroupName = "syncGroupName_example"; // String | The name of the sync group on which the sync member is hosted.
    String syncMemberName = "syncMemberName_example"; // String | The name of the sync member.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.syncMembersDelete(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncMembersApi#syncMembersDelete");
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
| **syncGroupName** | **String**| The name of the sync group on which the sync member is hosted. | |
| **syncMemberName** | **String**| The name of the sync member. | |
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
| **200** | Successfully deleted the sync member. |  -  |
| **202** | Deleting the sync member is in progress. |  -  |
| **204** | The specified sync member does not exist. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidSyncGroupCreateOrUpdateRequest - The create or update sync group request body is empty.   * 400 InvalidSyncMemberCreateOrUpdateRequest - The create or update sync member request body is empty.   * 400 InvalidSyncAgentCreateOrUpdateRequest - The create or update sync agent request body is empty.   * 400 InvalidDatabaseResourceId - Invalid database resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 InvalidSyncAgentResourceId - Invalid sync agent resource identifier.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 InvalidSyncGroup - Sync group is invalid.   * 400 InvalidSyncMember - Sync member is invalid.   * 400 InvalidSyncAgent - Sync agent is invalid.   * 400 InvalidSyncMetadataDatabase - Sync metadata database is invalid.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 409 CannotCreateSyncMemberDueToQuotaExceeded - Cannot create sync member due to quota exceeded. |  -  |

<a id="syncMembersGet"></a>
# **syncMembersGet**
> SyncMember syncMembersGet(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion)



Gets a sync member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SyncMembersApi apiInstance = new SyncMembersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
    String syncGroupName = "syncGroupName_example"; // String | The name of the sync group on which the sync member is hosted.
    String syncMemberName = "syncMemberName_example"; // String | The name of the sync member.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      SyncMember result = apiInstance.syncMembersGet(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncMembersApi#syncMembersGet");
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
| **syncGroupName** | **String**| The name of the sync group on which the sync member is hosted. | |
| **syncMemberName** | **String**| The name of the sync member. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**SyncMember**](SyncMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the specified sync member. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidSyncGroupCreateOrUpdateRequest - The create or update sync group request body is empty.   * 400 InvalidSyncMemberCreateOrUpdateRequest - The create or update sync member request body is empty.   * 400 InvalidSyncAgentCreateOrUpdateRequest - The create or update sync agent request body is empty.   * 400 InvalidDatabaseResourceId - Invalid database resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 InvalidSyncAgentResourceId - Invalid sync agent resource identifier.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 InvalidSyncGroup - Sync group is invalid.   * 400 InvalidSyncMember - Sync member is invalid.   * 400 InvalidSyncAgent - Sync agent is invalid.   * 400 InvalidSyncMetadataDatabase - Sync metadata database is invalid.   * 404 ResourceNotFound - The requested resource was not found.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 409 CannotCreateSyncMemberDueToQuotaExceeded - Cannot create sync member due to quota exceeded. |  -  |

<a id="syncMembersListBySyncGroup"></a>
# **syncMembersListBySyncGroup**
> SyncMemberListResult syncMembersListBySyncGroup(resourceGroupName, serverName, databaseName, syncGroupName, subscriptionId, apiVersion)



Lists sync members in the given sync group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SyncMembersApi apiInstance = new SyncMembersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
    String syncGroupName = "syncGroupName_example"; // String | The name of the sync group.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      SyncMemberListResult result = apiInstance.syncMembersListBySyncGroup(resourceGroupName, serverName, databaseName, syncGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncMembersApi#syncMembersListBySyncGroup");
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

[**SyncMemberListResult**](SyncMemberListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of sync members. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidSyncGroupCreateOrUpdateRequest - The create or update sync group request body is empty.   * 400 InvalidSyncMemberCreateOrUpdateRequest - The create or update sync member request body is empty.   * 400 InvalidSyncAgentCreateOrUpdateRequest - The create or update sync agent request body is empty.   * 400 InvalidDatabaseResourceId - Invalid database resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 InvalidSyncAgentResourceId - Invalid sync agent resource identifier.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 InvalidSyncGroup - Sync group is invalid.   * 400 InvalidSyncMember - Sync member is invalid.   * 400 InvalidSyncAgent - Sync agent is invalid.   * 400 InvalidSyncMetadataDatabase - Sync metadata database is invalid.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 409 CannotCreateSyncMemberDueToQuotaExceeded - Cannot create sync member due to quota exceeded. |  -  |

<a id="syncMembersListMemberSchemas"></a>
# **syncMembersListMemberSchemas**
> SyncFullSchemaPropertiesListResult syncMembersListMemberSchemas(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion)



Gets a sync member database schema.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SyncMembersApi apiInstance = new SyncMembersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
    String syncGroupName = "syncGroupName_example"; // String | The name of the sync group on which the sync member is hosted.
    String syncMemberName = "syncMemberName_example"; // String | The name of the sync member.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      SyncFullSchemaPropertiesListResult result = apiInstance.syncMembersListMemberSchemas(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncMembersApi#syncMembersListMemberSchemas");
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
| **syncGroupName** | **String**| The name of the sync group on which the sync member is hosted. | |
| **syncMemberName** | **String**| The name of the sync member. | |
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
| **200** | Successfully get a sync member schema. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidSyncGroupCreateOrUpdateRequest - The create or update sync group request body is empty.   * 400 InvalidSyncMemberCreateOrUpdateRequest - The create or update sync member request body is empty.   * 400 InvalidSyncAgentCreateOrUpdateRequest - The create or update sync agent request body is empty.   * 400 InvalidDatabaseResourceId - Invalid database resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 InvalidSyncAgentResourceId - Invalid sync agent resource identifier.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 InvalidSyncGroup - Sync group is invalid.   * 400 InvalidSyncMember - Sync member is invalid.   * 400 InvalidSyncAgent - Sync agent is invalid.   * 400 InvalidSyncMetadataDatabase - Sync metadata database is invalid.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 409 CannotCreateSyncMemberDueToQuotaExceeded - Cannot create sync member due to quota exceeded. |  -  |

<a id="syncMembersRefreshMemberSchema"></a>
# **syncMembersRefreshMemberSchema**
> syncMembersRefreshMemberSchema(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion)



Refreshes a sync member database schema.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SyncMembersApi apiInstance = new SyncMembersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
    String syncGroupName = "syncGroupName_example"; // String | The name of the sync group on which the sync member is hosted.
    String syncMemberName = "syncMemberName_example"; // String | The name of the sync member.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.syncMembersRefreshMemberSchema(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncMembersApi#syncMembersRefreshMemberSchema");
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
| **syncGroupName** | **String**| The name of the sync group on which the sync member is hosted. | |
| **syncMemberName** | **String**| The name of the sync member. | |
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
| **200** | Successfully refreshed a sync member schema. |  -  |
| **202** | The sync member schema refresh operation is on going. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidSyncGroupCreateOrUpdateRequest - The create or update sync group request body is empty.   * 400 InvalidSyncMemberCreateOrUpdateRequest - The create or update sync member request body is empty.   * 400 InvalidSyncAgentCreateOrUpdateRequest - The create or update sync agent request body is empty.   * 400 InvalidDatabaseResourceId - Invalid database resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 InvalidSyncAgentResourceId - Invalid sync agent resource identifier.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 InvalidSyncGroup - Sync group is invalid.   * 400 InvalidSyncMember - Sync member is invalid.   * 400 InvalidSyncAgent - Sync agent is invalid.   * 400 InvalidSyncMetadataDatabase - Sync metadata database is invalid.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 409 CannotCreateSyncMemberDueToQuotaExceeded - Cannot create sync member due to quota exceeded. |  -  |

<a id="syncMembersUpdate"></a>
# **syncMembersUpdate**
> SyncMember syncMembersUpdate(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion, parameters)



Updates an existing sync member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SyncMembersApi apiInstance = new SyncMembersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
    String syncGroupName = "syncGroupName_example"; // String | The name of the sync group on which the sync member is hosted.
    String syncMemberName = "syncMemberName_example"; // String | The name of the sync member.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    SyncMember parameters = new SyncMember(); // SyncMember | The requested sync member resource state.
    try {
      SyncMember result = apiInstance.syncMembersUpdate(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncMembersApi#syncMembersUpdate");
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
| **syncGroupName** | **String**| The name of the sync group on which the sync member is hosted. | |
| **syncMemberName** | **String**| The name of the sync member. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**SyncMember**](SyncMember.md)| The requested sync member resource state. | |

### Return type

[**SyncMember**](SyncMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the sync member. |  -  |
| **202** | Updating the sync member is in progress. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidSyncGroupCreateOrUpdateRequest - The create or update sync group request body is empty.   * 400 InvalidSyncMemberCreateOrUpdateRequest - The create or update sync member request body is empty.   * 400 InvalidSyncAgentCreateOrUpdateRequest - The create or update sync agent request body is empty.   * 400 InvalidDatabaseResourceId - Invalid database resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 InvalidSyncAgentResourceId - Invalid sync agent resource identifier.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 InvalidSyncGroup - Sync group is invalid.   * 400 InvalidSyncMember - Sync member is invalid.   * 400 InvalidSyncAgent - Sync agent is invalid.   * 400 InvalidSyncMetadataDatabase - Sync metadata database is invalid.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 409 CannotCreateSyncMemberDueToQuotaExceeded - Cannot create sync member due to quota exceeded. |  -  |

