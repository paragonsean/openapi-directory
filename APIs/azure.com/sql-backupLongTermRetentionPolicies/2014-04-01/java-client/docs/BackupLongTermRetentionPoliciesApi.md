# BackupLongTermRetentionPoliciesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**backupLongTermRetentionPoliciesCreateOrUpdate**](BackupLongTermRetentionPoliciesApi.md#backupLongTermRetentionPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/backupLongTermRetentionPolicies/{backupLongTermRetentionPolicyName} |  |
| [**backupLongTermRetentionPoliciesGet**](BackupLongTermRetentionPoliciesApi.md#backupLongTermRetentionPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/backupLongTermRetentionPolicies/{backupLongTermRetentionPolicyName} |  |
| [**backupLongTermRetentionPoliciesListByDatabase**](BackupLongTermRetentionPoliciesApi.md#backupLongTermRetentionPoliciesListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/backupLongTermRetentionPolicies |  |


<a id="backupLongTermRetentionPoliciesCreateOrUpdate"></a>
# **backupLongTermRetentionPoliciesCreateOrUpdate**
> BackupLongTermRetentionPolicy backupLongTermRetentionPoliciesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, backupLongTermRetentionPolicyName, parameters)



Creates or updates a database backup long term retention policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupLongTermRetentionPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BackupLongTermRetentionPoliciesApi apiInstance = new BackupLongTermRetentionPoliciesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database
    String backupLongTermRetentionPolicyName = "Default"; // String | The name of the backup long term retention policy
    BackupLongTermRetentionPolicy parameters = new BackupLongTermRetentionPolicy(); // BackupLongTermRetentionPolicy | The required parameters to update a backup long term retention policy
    try {
      BackupLongTermRetentionPolicy result = apiInstance.backupLongTermRetentionPoliciesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, backupLongTermRetentionPolicyName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupLongTermRetentionPoliciesApi#backupLongTermRetentionPoliciesCreateOrUpdate");
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
| **databaseName** | **String**| The name of the database | |
| **backupLongTermRetentionPolicyName** | **String**| The name of the backup long term retention policy | [enum: Default] |
| **parameters** | [**BackupLongTermRetentionPolicy**](BackupLongTermRetentionPolicy.md)| The required parameters to update a backup long term retention policy | |

### Return type

[**BackupLongTermRetentionPolicy**](BackupLongTermRetentionPolicy.md)

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

<a id="backupLongTermRetentionPoliciesGet"></a>
# **backupLongTermRetentionPoliciesGet**
> BackupLongTermRetentionPolicy backupLongTermRetentionPoliciesGet(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, backupLongTermRetentionPolicyName)



Returns a database backup long term retention policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupLongTermRetentionPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BackupLongTermRetentionPoliciesApi apiInstance = new BackupLongTermRetentionPoliciesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String backupLongTermRetentionPolicyName = "Default"; // String | The name of the backup long term retention policy
    try {
      BackupLongTermRetentionPolicy result = apiInstance.backupLongTermRetentionPoliciesGet(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, backupLongTermRetentionPolicyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupLongTermRetentionPoliciesApi#backupLongTermRetentionPoliciesGet");
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
| **databaseName** | **String**| The name of the database. | |
| **backupLongTermRetentionPolicyName** | **String**| The name of the backup long term retention policy | [enum: Default] |

### Return type

[**BackupLongTermRetentionPolicy**](BackupLongTermRetentionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="backupLongTermRetentionPoliciesListByDatabase"></a>
# **backupLongTermRetentionPoliciesListByDatabase**
> BackupLongTermRetentionPolicyListResult backupLongTermRetentionPoliciesListByDatabase(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName)



Returns a database backup long term retention policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupLongTermRetentionPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BackupLongTermRetentionPoliciesApi apiInstance = new BackupLongTermRetentionPoliciesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    try {
      BackupLongTermRetentionPolicyListResult result = apiInstance.backupLongTermRetentionPoliciesListByDatabase(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupLongTermRetentionPoliciesApi#backupLongTermRetentionPoliciesListByDatabase");
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
| **databaseName** | **String**| The name of the database. | |

### Return type

[**BackupLongTermRetentionPolicyListResult**](BackupLongTermRetentionPolicyListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

