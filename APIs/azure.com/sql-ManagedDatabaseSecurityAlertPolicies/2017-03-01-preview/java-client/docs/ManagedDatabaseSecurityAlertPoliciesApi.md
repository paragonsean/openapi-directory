# ManagedDatabaseSecurityAlertPoliciesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**managedDatabaseSecurityAlertPoliciesCreateOrUpdate**](ManagedDatabaseSecurityAlertPoliciesApi.md#managedDatabaseSecurityAlertPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}/securityAlertPolicies/{securityAlertPolicyName} |  |
| [**managedDatabaseSecurityAlertPoliciesGet**](ManagedDatabaseSecurityAlertPoliciesApi.md#managedDatabaseSecurityAlertPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}/securityAlertPolicies/{securityAlertPolicyName} |  |
| [**managedDatabaseSecurityAlertPoliciesListByDatabase**](ManagedDatabaseSecurityAlertPoliciesApi.md#managedDatabaseSecurityAlertPoliciesListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/databases/{databaseName}/securityAlertPolicies |  |


<a id="managedDatabaseSecurityAlertPoliciesCreateOrUpdate"></a>
# **managedDatabaseSecurityAlertPoliciesCreateOrUpdate**
> ManagedDatabaseSecurityAlertPolicy managedDatabaseSecurityAlertPoliciesCreateOrUpdate(resourceGroupName, managedInstanceName, databaseName, securityAlertPolicyName, subscriptionId, apiVersion, parameters)



Creates or updates a database&#39;s security alert policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedDatabaseSecurityAlertPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ManagedDatabaseSecurityAlertPoliciesApi apiInstance = new ManagedDatabaseSecurityAlertPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
    String databaseName = "databaseName_example"; // String | The name of the managed database for which the security alert policy is defined.
    String securityAlertPolicyName = "default"; // String | The name of the security alert policy.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    ManagedDatabaseSecurityAlertPolicy parameters = new ManagedDatabaseSecurityAlertPolicy(); // ManagedDatabaseSecurityAlertPolicy | The database security alert policy.
    try {
      ManagedDatabaseSecurityAlertPolicy result = apiInstance.managedDatabaseSecurityAlertPoliciesCreateOrUpdate(resourceGroupName, managedInstanceName, databaseName, securityAlertPolicyName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedDatabaseSecurityAlertPoliciesApi#managedDatabaseSecurityAlertPoliciesCreateOrUpdate");
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
| **databaseName** | **String**| The name of the managed database for which the security alert policy is defined. | |
| **securityAlertPolicyName** | **String**| The name of the security alert policy. | [enum: default] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**ManagedDatabaseSecurityAlertPolicy**](ManagedDatabaseSecurityAlertPolicy.md)| The database security alert policy. | |

### Return type

[**ManagedDatabaseSecurityAlertPolicy**](ManagedDatabaseSecurityAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully set the managed database security alert policy. |  -  |
| **201** | Successfully created the managed database security alert policy. |  -  |
| **0** | *** Error Responses: *** |  -  |

<a id="managedDatabaseSecurityAlertPoliciesGet"></a>
# **managedDatabaseSecurityAlertPoliciesGet**
> ManagedDatabaseSecurityAlertPolicy managedDatabaseSecurityAlertPoliciesGet(resourceGroupName, managedInstanceName, databaseName, securityAlertPolicyName, subscriptionId, apiVersion)



Gets a managed database&#39;s security alert policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedDatabaseSecurityAlertPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ManagedDatabaseSecurityAlertPoliciesApi apiInstance = new ManagedDatabaseSecurityAlertPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
    String databaseName = "databaseName_example"; // String | The name of the managed database for which the security alert policy is defined.
    String securityAlertPolicyName = "default"; // String | The name of the security alert policy.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      ManagedDatabaseSecurityAlertPolicy result = apiInstance.managedDatabaseSecurityAlertPoliciesGet(resourceGroupName, managedInstanceName, databaseName, securityAlertPolicyName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedDatabaseSecurityAlertPoliciesApi#managedDatabaseSecurityAlertPoliciesGet");
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
| **databaseName** | **String**| The name of the managed database for which the security alert policy is defined. | |
| **securityAlertPolicyName** | **String**| The name of the security alert policy. | [enum: default] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**ManagedDatabaseSecurityAlertPolicy**](ManagedDatabaseSecurityAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the managed database security alert policy. |  -  |
| **0** | *** Error Responses: ***   * 400 SecurityAlertPoliciesInvalidStorageAccountName - The provided storage account is not valid or does not exist.   * 400 SecurityAlertPoliciesInvalidStorageAccountCredentials - The provided storage account access key is not valid.   * 400 InvalidServerSecurityAlertPolicyCreateRequest - The create server Threat Detection security alert policy request does not exist or has no properties object.   * 400 DataSecurityInvalidUserSuppliedParameter - An invalid parameter value was provided by the client.   * 400 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 400 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 409 ServerSecurityAlertPolicyInProgress - Set server security alert policy is already in progress   * 409 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 500 DatabaseIsUnavailable - Loading failed. Please try again later.   * 500 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 500 GetServerSecurityAlertPolicyFailed - Failed to get Threat Detection settings |  -  |

<a id="managedDatabaseSecurityAlertPoliciesListByDatabase"></a>
# **managedDatabaseSecurityAlertPoliciesListByDatabase**
> ManagedDatabaseSecurityAlertPolicyListResult managedDatabaseSecurityAlertPoliciesListByDatabase(resourceGroupName, managedInstanceName, databaseName, subscriptionId, apiVersion)



Gets a list of managed database&#39;s security alert policies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedDatabaseSecurityAlertPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ManagedDatabaseSecurityAlertPoliciesApi apiInstance = new ManagedDatabaseSecurityAlertPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
    String databaseName = "databaseName_example"; // String | The name of the managed database for which the security alert policies are defined.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      ManagedDatabaseSecurityAlertPolicyListResult result = apiInstance.managedDatabaseSecurityAlertPoliciesListByDatabase(resourceGroupName, managedInstanceName, databaseName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedDatabaseSecurityAlertPoliciesApi#managedDatabaseSecurityAlertPoliciesListByDatabase");
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
| **databaseName** | **String**| The name of the managed database for which the security alert policies are defined. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**ManagedDatabaseSecurityAlertPolicyListResult**](ManagedDatabaseSecurityAlertPolicyListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the managed database security alert policies. |  -  |
| **0** | *** Error Responses: ***   * 400 SecurityAlertPoliciesInvalidStorageAccountName - The provided storage account is not valid or does not exist.   * 400 SecurityAlertPoliciesInvalidStorageAccountCredentials - The provided storage account access key is not valid.   * 400 InvalidServerSecurityAlertPolicyCreateRequest - The create server Threat Detection security alert policy request does not exist or has no properties object.   * 400 DataSecurityInvalidUserSuppliedParameter - An invalid parameter value was provided by the client.   * 400 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 400 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 409 ServerSecurityAlertPolicyInProgress - Set server security alert policy is already in progress   * 409 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 500 DatabaseIsUnavailable - Loading failed. Please try again later.   * 500 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 500 GetServerSecurityAlertPolicyFailed - Failed to get Threat Detection settings |  -  |

