# ManagedBackupShortTermRetentionPoliciesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**managedBackupShortTermRetentionPoliciesCreateOrUpdate**](ManagedBackupShortTermRetentionPoliciesApi.md#managedBackupShortTermRetentionPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}/backupShortTermRetentionPolicies/{policyName} |  |
| [**managedBackupShortTermRetentionPoliciesGet**](ManagedBackupShortTermRetentionPoliciesApi.md#managedBackupShortTermRetentionPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}/backupShortTermRetentionPolicies/{policyName} |  |
| [**managedBackupShortTermRetentionPoliciesListByDatabase**](ManagedBackupShortTermRetentionPoliciesApi.md#managedBackupShortTermRetentionPoliciesListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}/backupShortTermRetentionPolicies |  |
| [**managedBackupShortTermRetentionPoliciesUpdate**](ManagedBackupShortTermRetentionPoliciesApi.md#managedBackupShortTermRetentionPoliciesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}/backupShortTermRetentionPolicies/{policyName} |  |


<a id="managedBackupShortTermRetentionPoliciesCreateOrUpdate"></a>
# **managedBackupShortTermRetentionPoliciesCreateOrUpdate**
> ManagedBackupShortTermRetentionPolicy managedBackupShortTermRetentionPoliciesCreateOrUpdate(resourceGroupName, managedInstanceName, databaseName, policyName, subscriptionId, apiVersion, parameters)



Updates a managed database&#39;s short term retention policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedBackupShortTermRetentionPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ManagedBackupShortTermRetentionPoliciesApi apiInstance = new ManagedBackupShortTermRetentionPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String policyName = "default"; // String | The policy name. Should always be \"default\".
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    ManagedBackupShortTermRetentionPolicy parameters = new ManagedBackupShortTermRetentionPolicy(); // ManagedBackupShortTermRetentionPolicy | The short term retention policy info.
    try {
      ManagedBackupShortTermRetentionPolicy result = apiInstance.managedBackupShortTermRetentionPoliciesCreateOrUpdate(resourceGroupName, managedInstanceName, databaseName, policyName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedBackupShortTermRetentionPoliciesApi#managedBackupShortTermRetentionPoliciesCreateOrUpdate");
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
| **managedInstanceName** | **String**| The name of the managed instance. | |
| **databaseName** | **String**| The name of the database. | |
| **policyName** | **String**| The policy name. Should always be \&quot;default\&quot;. | [enum: default] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**ManagedBackupShortTermRetentionPolicy**](ManagedBackupShortTermRetentionPolicy.md)| The short term retention policy info. | |

### Return type

[**ManagedBackupShortTermRetentionPolicy**](ManagedBackupShortTermRetentionPolicy.md)

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
| **0** | *** Error Responses: ***   * 400 InvalidBackupRetentionDays - The retention days of {0} is not a valid configuration. Valid backup retention must be in 7-day increments (7, 14, 21, etc.)   * 400 InvalidRestorableDroppedDatabaseDeletionDate - The restorable dropped database deletion date given is invalid   * 400 InvalidRestorableDroppedDatabaseId - Invalid restorable dropped database identifier   * 400 InvalidParameterValue - An invalid value was given to a parameter.   * 400 InvalidBackupRetentionPeriod - The retention days of {0} is not a valid configuration. Valid backup retention in days must be between {1} and {2}   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found.   * 404 SourceDatabaseNotFound - The source database does not exist.   * 404 CannotFindObject - Cannot find the object because it does not exist or you do not have permissions   * 429 SubscriptionTooManyCreateUpdateRequests - Requests beyond max requests that can be processed by available resources.   * 429 SubscriptionTooManyRequests - Requests beyond max requests that can be processed by available resources.   * 503 TooManyRequests - Requests beyond max requests that can be processed by available resources.   * 504 RequestTimeout - Service request exceeded the allowed timeout. |  -  |

<a id="managedBackupShortTermRetentionPoliciesGet"></a>
# **managedBackupShortTermRetentionPoliciesGet**
> ManagedBackupShortTermRetentionPolicy managedBackupShortTermRetentionPoliciesGet(resourceGroupName, managedInstanceName, databaseName, policyName, subscriptionId, apiVersion)



Gets a managed database&#39;s short term retention policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedBackupShortTermRetentionPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ManagedBackupShortTermRetentionPoliciesApi apiInstance = new ManagedBackupShortTermRetentionPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String policyName = "default"; // String | The policy name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      ManagedBackupShortTermRetentionPolicy result = apiInstance.managedBackupShortTermRetentionPoliciesGet(resourceGroupName, managedInstanceName, databaseName, policyName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedBackupShortTermRetentionPoliciesApi#managedBackupShortTermRetentionPoliciesGet");
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
| **managedInstanceName** | **String**| The name of the managed instance. | |
| **databaseName** | **String**| The name of the database. | |
| **policyName** | **String**| The policy name. | [enum: default] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**ManagedBackupShortTermRetentionPolicy**](ManagedBackupShortTermRetentionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the policy. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidBackupRetentionDays - The retention days of {0} is not a valid configuration. Valid backup retention must be in 7-day increments (7, 14, 21, etc.)   * 400 InvalidRestorableDroppedDatabaseDeletionDate - The restorable dropped database deletion date given is invalid   * 400 InvalidRestorableDroppedDatabaseId - Invalid restorable dropped database identifier   * 400 InvalidParameterValue - An invalid value was given to a parameter.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found. |  -  |

<a id="managedBackupShortTermRetentionPoliciesListByDatabase"></a>
# **managedBackupShortTermRetentionPoliciesListByDatabase**
> ManagedBackupShortTermRetentionPolicyListResult managedBackupShortTermRetentionPoliciesListByDatabase(resourceGroupName, managedInstanceName, databaseName, subscriptionId, apiVersion)



Gets a managed database&#39;s short term retention policy list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedBackupShortTermRetentionPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ManagedBackupShortTermRetentionPoliciesApi apiInstance = new ManagedBackupShortTermRetentionPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      ManagedBackupShortTermRetentionPolicyListResult result = apiInstance.managedBackupShortTermRetentionPoliciesListByDatabase(resourceGroupName, managedInstanceName, databaseName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedBackupShortTermRetentionPoliciesApi#managedBackupShortTermRetentionPoliciesListByDatabase");
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
| **managedInstanceName** | **String**| The name of the managed instance. | |
| **databaseName** | **String**| The name of the database. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**ManagedBackupShortTermRetentionPolicyListResult**](ManagedBackupShortTermRetentionPolicyListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the policy. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidBackupRetentionDays - The retention days of {0} is not a valid configuration. Valid backup retention must be in 7-day increments (7, 14, 21, etc.)   * 400 InvalidRestorableDroppedDatabaseDeletionDate - The restorable dropped database deletion date given is invalid   * 400 InvalidRestorableDroppedDatabaseId - Invalid restorable dropped database identifier   * 400 InvalidParameterValue - An invalid value was given to a parameter.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found. |  -  |

<a id="managedBackupShortTermRetentionPoliciesUpdate"></a>
# **managedBackupShortTermRetentionPoliciesUpdate**
> ManagedBackupShortTermRetentionPolicy managedBackupShortTermRetentionPoliciesUpdate(resourceGroupName, managedInstanceName, databaseName, policyName, subscriptionId, apiVersion, parameters)



Updates a managed database&#39;s short term retention policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedBackupShortTermRetentionPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ManagedBackupShortTermRetentionPoliciesApi apiInstance = new ManagedBackupShortTermRetentionPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String policyName = "default"; // String | The policy name. Should always be \"default\".
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    ManagedBackupShortTermRetentionPolicy parameters = new ManagedBackupShortTermRetentionPolicy(); // ManagedBackupShortTermRetentionPolicy | The short term retention policy info.
    try {
      ManagedBackupShortTermRetentionPolicy result = apiInstance.managedBackupShortTermRetentionPoliciesUpdate(resourceGroupName, managedInstanceName, databaseName, policyName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedBackupShortTermRetentionPoliciesApi#managedBackupShortTermRetentionPoliciesUpdate");
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
| **managedInstanceName** | **String**| The name of the managed instance. | |
| **databaseName** | **String**| The name of the database. | |
| **policyName** | **String**| The policy name. Should always be \&quot;default\&quot;. | [enum: default] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**ManagedBackupShortTermRetentionPolicy**](ManagedBackupShortTermRetentionPolicy.md)| The short term retention policy info. | |

### Return type

[**ManagedBackupShortTermRetentionPolicy**](ManagedBackupShortTermRetentionPolicy.md)

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
| **0** | *** Error Responses: ***   * 400 InvalidBackupRetentionDays - The retention days of {0} is not a valid configuration. Valid backup retention must be in 7-day increments (7, 14, 21, etc.)   * 400 InvalidRestorableDroppedDatabaseDeletionDate - The restorable dropped database deletion date given is invalid   * 400 InvalidRestorableDroppedDatabaseId - Invalid restorable dropped database identifier   * 400 InvalidParameterValue - An invalid value was given to a parameter.   * 400 InvalidBackupRetentionPeriod - The retention days of {0} is not a valid configuration. Valid backup retention in days must be between {1} and {2}   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found.   * 404 SourceDatabaseNotFound - The source database does not exist.   * 404 CannotFindObject - Cannot find the object because it does not exist or you do not have permissions   * 429 SubscriptionTooManyCreateUpdateRequests - Requests beyond max requests that can be processed by available resources.   * 429 SubscriptionTooManyRequests - Requests beyond max requests that can be processed by available resources.   * 503 TooManyRequests - Requests beyond max requests that can be processed by available resources.   * 504 RequestTimeout - Service request exceeded the allowed timeout. |  -  |

