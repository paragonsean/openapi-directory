# RestorePointsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**restorePointsCreate**](RestorePointsApi.md#restorePointsCreate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/restorePoints |  |
| [**restorePointsDelete**](RestorePointsApi.md#restorePointsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/restorePoints/{restorePointName} |  |
| [**restorePointsGet**](RestorePointsApi.md#restorePointsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/restorePoints/{restorePointName} |  |
| [**restorePointsListByDatabase**](RestorePointsApi.md#restorePointsListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/restorePoints |  |


<a id="restorePointsCreate"></a>
# **restorePointsCreate**
> RestorePoint restorePointsCreate(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion, parameters)



Creates a restore point for a data warehouse.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RestorePointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    RestorePointsApi apiInstance = new RestorePointsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    CreateDatabaseRestorePointDefinition parameters = new CreateDatabaseRestorePointDefinition(); // CreateDatabaseRestorePointDefinition | The definition for creating the restore point of this database.
    try {
      RestorePoint result = apiInstance.restorePointsCreate(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RestorePointsApi#restorePointsCreate");
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
| **databaseName** | **String**| The name of the database. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**CreateDatabaseRestorePointDefinition**](CreateDatabaseRestorePointDefinition.md)| The definition for creating the restore point of this database. | |

### Return type

[**RestorePoint**](RestorePoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully created the restore point request. |  -  |
| **201** | Successfully created the restore point request. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 FeatureDisabledOnSelectedEdition - User attempted to use a feature which is disabled on current database edition.   * 400 BackupNotAllowedOnDeactivatedDatabase - Cannot create restore point on a deactivated database.   * 400 RestorePointLimitReached - A restore point cannot be created because database would exceed the allowed quota of restore points.   * 400 RestorePointAttemptToDeleteSystemBackup - Cannot delete system restore point.   * 404 DatabaseRestorePointNotFound - Can not find database restore point.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 408 DatabaseRestorePointTimedOut - Create database restore point failed. |  -  |

<a id="restorePointsDelete"></a>
# **restorePointsDelete**
> restorePointsDelete(resourceGroupName, serverName, databaseName, restorePointName, subscriptionId, apiVersion)



Deletes a restore point.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RestorePointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    RestorePointsApi apiInstance = new RestorePointsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String restorePointName = "restorePointName_example"; // String | The name of the restore point.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.restorePointsDelete(resourceGroupName, serverName, databaseName, restorePointName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling RestorePointsApi#restorePointsDelete");
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
| **databaseName** | **String**| The name of the database. | |
| **restorePointName** | **String**| The name of the restore point. | |
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
| **200** | Successfully deleted the restore point. |  -  |
| **0** | *** Error Responses: ***   * 400 FeatureDisabledOnSelectedEdition - User attempted to use a feature which is disabled on current database edition.   * 400 BackupNotAllowedOnDeactivatedDatabase - Cannot create restore point on a deactivated database.   * 400 RestorePointLimitReached - A restore point cannot be created because database would exceed the allowed quota of restore points.   * 400 RestorePointAttemptToDeleteSystemBackup - Cannot delete system restore point.   * 404 DatabaseRestorePointNotFound - Can not find database restore point.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 408 DatabaseRestorePointTimedOut - Create database restore point failed. |  -  |

<a id="restorePointsGet"></a>
# **restorePointsGet**
> RestorePoint restorePointsGet(resourceGroupName, serverName, databaseName, restorePointName, subscriptionId, apiVersion)



Gets a restore point.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RestorePointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    RestorePointsApi apiInstance = new RestorePointsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String restorePointName = "restorePointName_example"; // String | The name of the restore point.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      RestorePoint result = apiInstance.restorePointsGet(resourceGroupName, serverName, databaseName, restorePointName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RestorePointsApi#restorePointsGet");
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
| **databaseName** | **String**| The name of the database. | |
| **restorePointName** | **String**| The name of the restore point. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**RestorePoint**](RestorePoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully returned the restore point. |  -  |
| **0** | *** Error Responses: ***   * 400 FeatureDisabledOnSelectedEdition - User attempted to use a feature which is disabled on current database edition.   * 400 BackupNotAllowedOnDeactivatedDatabase - Cannot create restore point on a deactivated database.   * 400 RestorePointLimitReached - A restore point cannot be created because database would exceed the allowed quota of restore points.   * 400 RestorePointAttemptToDeleteSystemBackup - Cannot delete system restore point.   * 404 DatabaseRestorePointNotFound - Can not find database restore point.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 408 DatabaseRestorePointTimedOut - Create database restore point failed. |  -  |

<a id="restorePointsListByDatabase"></a>
# **restorePointsListByDatabase**
> RestorePointListResult restorePointsListByDatabase(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion)



Gets a list of database restore points.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RestorePointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    RestorePointsApi apiInstance = new RestorePointsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      RestorePointListResult result = apiInstance.restorePointsListByDatabase(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RestorePointsApi#restorePointsListByDatabase");
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
| **databaseName** | **String**| The name of the database. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**RestorePointListResult**](RestorePointListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully returned restore points. |  -  |
| **0** | *** Error Responses: ***   * 400 FeatureDisabledOnSelectedEdition - User attempted to use a feature which is disabled on current database edition.   * 400 BackupNotAllowedOnDeactivatedDatabase - Cannot create restore point on a deactivated database.   * 400 RestorePointLimitReached - A restore point cannot be created because database would exceed the allowed quota of restore points.   * 400 RestorePointAttemptToDeleteSystemBackup - Cannot delete system restore point.   * 404 DatabaseRestorePointNotFound - Can not find database restore point.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 408 DatabaseRestorePointTimedOut - Create database restore point failed. |  -  |

