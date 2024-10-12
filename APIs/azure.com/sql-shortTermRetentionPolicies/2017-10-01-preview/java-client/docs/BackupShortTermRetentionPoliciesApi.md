# BackupShortTermRetentionPoliciesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**backupShortTermRetentionPoliciesCreateOrUpdate**](BackupShortTermRetentionPoliciesApi.md#backupShortTermRetentionPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/backupShortTermRetentionPolicies/{policyName} |  |
| [**backupShortTermRetentionPoliciesGet**](BackupShortTermRetentionPoliciesApi.md#backupShortTermRetentionPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/backupShortTermRetentionPolicies/{policyName} |  |
| [**backupShortTermRetentionPoliciesListByDatabase**](BackupShortTermRetentionPoliciesApi.md#backupShortTermRetentionPoliciesListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/backupShortTermRetentionPolicies |  |
| [**backupShortTermRetentionPoliciesUpdate**](BackupShortTermRetentionPoliciesApi.md#backupShortTermRetentionPoliciesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/backupShortTermRetentionPolicies/{policyName} |  |


<a id="backupShortTermRetentionPoliciesCreateOrUpdate"></a>
# **backupShortTermRetentionPoliciesCreateOrUpdate**
> BackupShortTermRetentionPolicy backupShortTermRetentionPoliciesCreateOrUpdate(resourceGroupName, serverName, databaseName, policyName, subscriptionId, apiVersion, parameters)



Updates a database&#39;s short term retention policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupShortTermRetentionPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BackupShortTermRetentionPoliciesApi apiInstance = new BackupShortTermRetentionPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String policyName = "default"; // String | The policy name. Should always be \"default\".
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    BackupShortTermRetentionPolicy parameters = new BackupShortTermRetentionPolicy(); // BackupShortTermRetentionPolicy | The short term retention policy info.
    try {
      BackupShortTermRetentionPolicy result = apiInstance.backupShortTermRetentionPoliciesCreateOrUpdate(resourceGroupName, serverName, databaseName, policyName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupShortTermRetentionPoliciesApi#backupShortTermRetentionPoliciesCreateOrUpdate");
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
| **policyName** | **String**| The policy name. Should always be \&quot;default\&quot;. | [enum: default] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**BackupShortTermRetentionPolicy**](BackupShortTermRetentionPolicy.md)| The short term retention policy info. | |

### Return type

[**BackupShortTermRetentionPolicy**](BackupShortTermRetentionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the policy. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidBackupRetentionDays - The retention days of {0} is not a valid configuration. Valid backup retention must be in 7-day increments (7, 14, 21, etc.)   * 400 InvalidParameterValue - An invalid value was given to a parameter.   * 400 InvalidBackupRetentionPeriod - The retention days of {0} is not a valid configuration. Valid backup retention in days must be between {1} and {2}   * 400 UpdateShortTermRetentionFeatureNotSupportedForEdition - This feature is not available for the selected database&#39;s edition {0}.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found.   * 404 CannotFindObject - Cannot find the object because it does not exist or you do not have permissions   * 404 SourceDatabaseNotFound - The source database does not exist.   * 429 SubscriptionTooManyCreateUpdateRequests - Requests beyond max requests that can be processed by available resources.   * 429 SubscriptionTooManyRequests - Requests beyond max requests that can be processed by available resources.   * 503 TooManyRequests - Requests beyond max requests that can be processed by available resources.   * 504 RequestTimeout - Service request exceeded the allowed timeout. |  -  |

<a id="backupShortTermRetentionPoliciesGet"></a>
# **backupShortTermRetentionPoliciesGet**
> BackupShortTermRetentionPolicy backupShortTermRetentionPoliciesGet(resourceGroupName, serverName, databaseName, policyName, subscriptionId, apiVersion)



Gets a database&#39;s short term retention policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupShortTermRetentionPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BackupShortTermRetentionPoliciesApi apiInstance = new BackupShortTermRetentionPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String policyName = "default"; // String | The policy name. Should always be \"default\".
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      BackupShortTermRetentionPolicy result = apiInstance.backupShortTermRetentionPoliciesGet(resourceGroupName, serverName, databaseName, policyName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupShortTermRetentionPoliciesApi#backupShortTermRetentionPoliciesGet");
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
| **policyName** | **String**| The policy name. Should always be \&quot;default\&quot;. | [enum: default] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**BackupShortTermRetentionPolicy**](BackupShortTermRetentionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the policy. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidBackupRetentionDays - The retention days of {0} is not a valid configuration. Valid backup retention must be in 7-day increments (7, 14, 21, etc.)   * 400 InvalidParameterValue - An invalid value was given to a parameter.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found. |  -  |

<a id="backupShortTermRetentionPoliciesListByDatabase"></a>
# **backupShortTermRetentionPoliciesListByDatabase**
> BackupShortTermRetentionPolicyListResult backupShortTermRetentionPoliciesListByDatabase(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion)



Gets a database&#39;s short term retention policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupShortTermRetentionPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BackupShortTermRetentionPoliciesApi apiInstance = new BackupShortTermRetentionPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      BackupShortTermRetentionPolicyListResult result = apiInstance.backupShortTermRetentionPoliciesListByDatabase(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupShortTermRetentionPoliciesApi#backupShortTermRetentionPoliciesListByDatabase");
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

[**BackupShortTermRetentionPolicyListResult**](BackupShortTermRetentionPolicyListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the policy. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidBackupRetentionDays - The retention days of {0} is not a valid configuration. Valid backup retention must be in 7-day increments (7, 14, 21, etc.)   * 400 InvalidParameterValue - An invalid value was given to a parameter.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found. |  -  |

<a id="backupShortTermRetentionPoliciesUpdate"></a>
# **backupShortTermRetentionPoliciesUpdate**
> BackupShortTermRetentionPolicy backupShortTermRetentionPoliciesUpdate(resourceGroupName, serverName, databaseName, policyName, subscriptionId, apiVersion, parameters)



Updates a database&#39;s short term retention policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupShortTermRetentionPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BackupShortTermRetentionPoliciesApi apiInstance = new BackupShortTermRetentionPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String policyName = "default"; // String | The policy name. Should always be \"default\".
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    BackupShortTermRetentionPolicy parameters = new BackupShortTermRetentionPolicy(); // BackupShortTermRetentionPolicy | The short term retention policy info.
    try {
      BackupShortTermRetentionPolicy result = apiInstance.backupShortTermRetentionPoliciesUpdate(resourceGroupName, serverName, databaseName, policyName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupShortTermRetentionPoliciesApi#backupShortTermRetentionPoliciesUpdate");
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
| **policyName** | **String**| The policy name. Should always be \&quot;default\&quot;. | [enum: default] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**BackupShortTermRetentionPolicy**](BackupShortTermRetentionPolicy.md)| The short term retention policy info. | |

### Return type

[**BackupShortTermRetentionPolicy**](BackupShortTermRetentionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the policy. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidBackupRetentionDays - The retention days of {0} is not a valid configuration. Valid backup retention must be in 7-day increments (7, 14, 21, etc.)   * 400 InvalidParameterValue - An invalid value was given to a parameter.   * 400 InvalidBackupRetentionPeriod - The retention days of {0} is not a valid configuration. Valid backup retention in days must be between {1} and {2}   * 400 UpdateShortTermRetentionFeatureNotSupportedForEdition - This feature is not available for the selected database&#39;s edition {0}.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found.   * 404 CannotFindObject - Cannot find the object because it does not exist or you do not have permissions   * 404 SourceDatabaseNotFound - The source database does not exist.   * 429 SubscriptionTooManyCreateUpdateRequests - Requests beyond max requests that can be processed by available resources.   * 429 SubscriptionTooManyRequests - Requests beyond max requests that can be processed by available resources.   * 503 TooManyRequests - Requests beyond max requests that can be processed by available resources.   * 504 RequestTimeout - Service request exceeded the allowed timeout. |  -  |

