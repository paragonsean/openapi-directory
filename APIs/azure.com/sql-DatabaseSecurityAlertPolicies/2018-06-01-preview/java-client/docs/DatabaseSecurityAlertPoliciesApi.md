# DatabaseSecurityAlertPoliciesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**databaseSecurityAlertPoliciesCreateOrUpdate**](DatabaseSecurityAlertPoliciesApi.md#databaseSecurityAlertPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/securityAlertPolicies/{securityAlertPolicyName} |  |
| [**databaseSecurityAlertPoliciesGet**](DatabaseSecurityAlertPoliciesApi.md#databaseSecurityAlertPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/securityAlertPolicies/{securityAlertPolicyName} |  |
| [**databaseSecurityAlertPoliciesListByDatabase**](DatabaseSecurityAlertPoliciesApi.md#databaseSecurityAlertPoliciesListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/securityAlertPolicies |  |


<a id="databaseSecurityAlertPoliciesCreateOrUpdate"></a>
# **databaseSecurityAlertPoliciesCreateOrUpdate**
> DatabaseSecurityAlertPolicy databaseSecurityAlertPoliciesCreateOrUpdate(resourceGroupName, serverName, databaseName, securityAlertPolicyName, subscriptionId, apiVersion, parameters)



Creates or updates a database&#39;s security alert policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseSecurityAlertPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DatabaseSecurityAlertPoliciesApi apiInstance = new DatabaseSecurityAlertPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the  server.
    String databaseName = "databaseName_example"; // String | The name of the  database for which the security alert policy is defined.
    String securityAlertPolicyName = "default"; // String | The name of the security alert policy.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    DatabaseSecurityAlertPolicy parameters = new DatabaseSecurityAlertPolicy(); // DatabaseSecurityAlertPolicy | The database security alert policy.
    try {
      DatabaseSecurityAlertPolicy result = apiInstance.databaseSecurityAlertPoliciesCreateOrUpdate(resourceGroupName, serverName, databaseName, securityAlertPolicyName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseSecurityAlertPoliciesApi#databaseSecurityAlertPoliciesCreateOrUpdate");
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
| **serverName** | **String**| The name of the  server. | |
| **databaseName** | **String**| The name of the  database for which the security alert policy is defined. | |
| **securityAlertPolicyName** | **String**| The name of the security alert policy. | [enum: default] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**DatabaseSecurityAlertPolicy**](DatabaseSecurityAlertPolicy.md)| The database security alert policy. | |

### Return type

[**DatabaseSecurityAlertPolicy**](DatabaseSecurityAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully set the  database security alert policy. |  -  |
| **201** | Successfully created the  database security alert policy. |  -  |
| **0** | *** Error Responses: ***   * 400 SecurityAlertPoliciesInvalidStorageAccountName - The provided storage account is not valid or does not exist.   * 400 SecurityAlertPoliciesInvalidStorageAccountCredentials - The provided storage account access key is not valid.   * 400 InvalidDatabaseSecurityAlertPolicyCreateRequest - The create database Threat Detection security alert policy request does not exist or has no properties object.   * 400 DataSecurityInvalidUserSuppliedParameter - An invalid parameter value was provided by the client.   * 400 UpsertDatabaseSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 400 UpsertDatabaseSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 404 UpsertDatabaseSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 409 DatabaseSecurityAlertPolicyInProgress - Set database security alert policy is already in progress   * 409 UpsertDatabaseSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 500 DatabaseIsUnavailable - Loading failed. Please try again later.   * 500 UpsertDatabaseSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 500 GetDatabaseSecurityAlertPolicyFailed - Failed to get Threat Detection settings |  -  |

<a id="databaseSecurityAlertPoliciesGet"></a>
# **databaseSecurityAlertPoliciesGet**
> DatabaseSecurityAlertPolicy databaseSecurityAlertPoliciesGet(resourceGroupName, serverName, databaseName, securityAlertPolicyName, subscriptionId, apiVersion)



Gets a  database&#39;s security alert policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseSecurityAlertPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DatabaseSecurityAlertPoliciesApi apiInstance = new DatabaseSecurityAlertPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the  server.
    String databaseName = "databaseName_example"; // String | The name of the  database for which the security alert policy is defined.
    String securityAlertPolicyName = "default"; // String | The name of the security alert policy.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      DatabaseSecurityAlertPolicy result = apiInstance.databaseSecurityAlertPoliciesGet(resourceGroupName, serverName, databaseName, securityAlertPolicyName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseSecurityAlertPoliciesApi#databaseSecurityAlertPoliciesGet");
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
| **serverName** | **String**| The name of the  server. | |
| **databaseName** | **String**| The name of the  database for which the security alert policy is defined. | |
| **securityAlertPolicyName** | **String**| The name of the security alert policy. | [enum: default] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**DatabaseSecurityAlertPolicy**](DatabaseSecurityAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the  database security alert policy. |  -  |
| **0** | *** Error Responses: ***   * 400 SecurityAlertPoliciesInvalidStorageAccountName - The provided storage account is not valid or does not exist.   * 400 SecurityAlertPoliciesInvalidStorageAccountCredentials - The provided storage account access key is not valid.   * 400 InvalidDatabaseSecurityAlertPolicyCreateRequest - The create database Threat Detection security alert policy request does not exist or has no properties object.   * 400 DataSecurityInvalidUserSuppliedParameter - An invalid parameter value was provided by the client.   * 400 UpsertDatabaseSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 400 UpsertDatabaseSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 404 UpsertDatabaseSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 409 DatabaseSecurityAlertPolicyInProgress - Set database security alert policy is already in progress   * 409 UpsertDatabaseSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 500 DatabaseIsUnavailable - Loading failed. Please try again later.   * 500 UpsertDatabaseSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 500 GetDatabaseSecurityAlertPolicyFailed - Failed to get Threat Detection settings |  -  |

<a id="databaseSecurityAlertPoliciesListByDatabase"></a>
# **databaseSecurityAlertPoliciesListByDatabase**
> DatabaseSecurityAlertListResult databaseSecurityAlertPoliciesListByDatabase(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion)



Gets a list of database&#39;s security alert policies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseSecurityAlertPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DatabaseSecurityAlertPoliciesApi apiInstance = new DatabaseSecurityAlertPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the  server.
    String databaseName = "databaseName_example"; // String | The name of the  database for which the security alert policy is defined.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      DatabaseSecurityAlertListResult result = apiInstance.databaseSecurityAlertPoliciesListByDatabase(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseSecurityAlertPoliciesApi#databaseSecurityAlertPoliciesListByDatabase");
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
| **serverName** | **String**| The name of the  server. | |
| **databaseName** | **String**| The name of the  database for which the security alert policy is defined. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**DatabaseSecurityAlertListResult**](DatabaseSecurityAlertListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the  database security alert policy. |  -  |
| **0** | *** Error Responses: ***   * 400 SecurityAlertPoliciesInvalidStorageAccountName - The provided storage account is not valid or does not exist.   * 400 SecurityAlertPoliciesInvalidStorageAccountCredentials - The provided storage account access key is not valid.   * 400 InvalidDatabaseSecurityAlertPolicyCreateRequest - The create database Threat Detection security alert policy request does not exist or has no properties object.   * 400 DataSecurityInvalidUserSuppliedParameter - An invalid parameter value was provided by the client.   * 400 UpsertDatabaseSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 400 UpsertDatabaseSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 404 UpsertDatabaseSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 409 DatabaseSecurityAlertPolicyInProgress - Set database security alert policy is already in progress   * 409 UpsertDatabaseSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 500 DatabaseIsUnavailable - Loading failed. Please try again later.   * 500 UpsertDatabaseSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 500 GetDatabaseSecurityAlertPolicyFailed - Failed to get Threat Detection settings |  -  |

