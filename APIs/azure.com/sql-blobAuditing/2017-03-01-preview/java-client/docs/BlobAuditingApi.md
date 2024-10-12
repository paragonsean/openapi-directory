# BlobAuditingApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**databaseBlobAuditingPoliciesCreateOrUpdate**](BlobAuditingApi.md#databaseBlobAuditingPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/auditingSettings/{blobAuditingPolicyName} |  |
| [**databaseBlobAuditingPoliciesGet**](BlobAuditingApi.md#databaseBlobAuditingPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/auditingSettings/{blobAuditingPolicyName} |  |
| [**databaseBlobAuditingPoliciesListByDatabase**](BlobAuditingApi.md#databaseBlobAuditingPoliciesListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/auditingSettings |  |
| [**extendedDatabaseBlobAuditingPoliciesCreateOrUpdate**](BlobAuditingApi.md#extendedDatabaseBlobAuditingPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/extendedAuditingSettings/{blobAuditingPolicyName} |  |
| [**extendedDatabaseBlobAuditingPoliciesGet**](BlobAuditingApi.md#extendedDatabaseBlobAuditingPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/extendedAuditingSettings/{blobAuditingPolicyName} |  |
| [**extendedServerBlobAuditingPoliciesCreateOrUpdate**](BlobAuditingApi.md#extendedServerBlobAuditingPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/extendedAuditingSettings/{blobAuditingPolicyName} |  |
| [**extendedServerBlobAuditingPoliciesGet**](BlobAuditingApi.md#extendedServerBlobAuditingPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/extendedAuditingSettings/{blobAuditingPolicyName} |  |
| [**serverBlobAuditingPoliciesCreateOrUpdate**](BlobAuditingApi.md#serverBlobAuditingPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/auditingSettings/{blobAuditingPolicyName} |  |
| [**serverBlobAuditingPoliciesGet**](BlobAuditingApi.md#serverBlobAuditingPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/auditingSettings/{blobAuditingPolicyName} |  |
| [**serverBlobAuditingPoliciesListByServer**](BlobAuditingApi.md#serverBlobAuditingPoliciesListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/auditingSettings |  |


<a id="databaseBlobAuditingPoliciesCreateOrUpdate"></a>
# **databaseBlobAuditingPoliciesCreateOrUpdate**
> DatabaseBlobAuditingPolicy databaseBlobAuditingPoliciesCreateOrUpdate(resourceGroupName, serverName, databaseName, blobAuditingPolicyName, subscriptionId, apiVersion, parameters)



Creates or updates a database&#39;s blob auditing policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobAuditingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BlobAuditingApi apiInstance = new BlobAuditingApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String blobAuditingPolicyName = "default"; // String | The name of the blob auditing policy.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    DatabaseBlobAuditingPolicy parameters = new DatabaseBlobAuditingPolicy(); // DatabaseBlobAuditingPolicy | The database blob auditing policy.
    try {
      DatabaseBlobAuditingPolicy result = apiInstance.databaseBlobAuditingPoliciesCreateOrUpdate(resourceGroupName, serverName, databaseName, blobAuditingPolicyName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobAuditingApi#databaseBlobAuditingPoliciesCreateOrUpdate");
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
| **blobAuditingPolicyName** | **String**| The name of the blob auditing policy. | [enum: default] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**DatabaseBlobAuditingPolicy**](DatabaseBlobAuditingPolicy.md)| The database blob auditing policy. | |

### Return type

[**DatabaseBlobAuditingPolicy**](DatabaseBlobAuditingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully set the database blob auditing policy. |  -  |
| **201** | Successfully created the database blob auditing policy. |  -  |
| **0** | *** Error Responses: ***   * 400 BlobAuditingIsNotSupportedOnResourceType - Blob Auditing is currently not supported for this resource type.   * 400 InvalidDatabaseBlobAuditingPolicyCreateRequest - The create database blob auditing policy request does not exist or has no properties object.   * 400 InvalidBlobAuditActionsAndGroups - Invalid audit actions or action groups.   * 400 DataSecurityInvalidUserSuppliedParameter - An invalid parameter value was provided by the client.   * 400 BlobAuditingInvalidStorageAccountName - The provided storage account is not valid or does not exist.   * 400 UpdateNotAllowedOnPausedDatabase - User attempted to perform an update on a paused database.   * 400 BlobAuditingInvalidStorageAccountCredentials - The provided storage account or access key is not valid.   * 400 BlobAuditingIsNotSupportedOnGeoDr - Blob auditing can be configured on primary databases only.   * 400 InvalidBlobAuditActionsAndGroupsForDW - Unsupported audit actions or action groups for DW.   * 400 BlobAuditingInsufficientStorageAccountPermissions - Insufficient read or write permissions on the provided storage account.   * 400 BlobAuditingStorageAccountIsDisabled - The provided storage account is disabled.   * 400 InvalidBlobAuditActions - Invalid audit action   * 404 SourceDatabaseNotFound - The source database does not exist.   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 500 DatabaseIsUnavailable - Loading failed. Please try again later. |  -  |

<a id="databaseBlobAuditingPoliciesGet"></a>
# **databaseBlobAuditingPoliciesGet**
> DatabaseBlobAuditingPolicy databaseBlobAuditingPoliciesGet(resourceGroupName, serverName, databaseName, blobAuditingPolicyName, subscriptionId, apiVersion)



Gets a database&#39;s blob auditing policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobAuditingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BlobAuditingApi apiInstance = new BlobAuditingApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String blobAuditingPolicyName = "default"; // String | The name of the blob auditing policy.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      DatabaseBlobAuditingPolicy result = apiInstance.databaseBlobAuditingPoliciesGet(resourceGroupName, serverName, databaseName, blobAuditingPolicyName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobAuditingApi#databaseBlobAuditingPoliciesGet");
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
| **blobAuditingPolicyName** | **String**| The name of the blob auditing policy. | [enum: default] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**DatabaseBlobAuditingPolicy**](DatabaseBlobAuditingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the database blob auditing policy. |  -  |
| **0** | *** Error Responses: ***   * 400 BlobAuditingIsNotSupportedOnResourceType - Blob Auditing is currently not supported for this resource type.   * 404 SourceDatabaseNotFound - The source database does not exist.   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 500 DatabaseIsUnavailable - Loading failed. Please try again later. |  -  |

<a id="databaseBlobAuditingPoliciesListByDatabase"></a>
# **databaseBlobAuditingPoliciesListByDatabase**
> DatabaseBlobAuditingPolicyListResult databaseBlobAuditingPoliciesListByDatabase(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion)



Lists auditing settings of a database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobAuditingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BlobAuditingApi apiInstance = new BlobAuditingApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      DatabaseBlobAuditingPolicyListResult result = apiInstance.databaseBlobAuditingPoliciesListByDatabase(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobAuditingApi#databaseBlobAuditingPoliciesListByDatabase");
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

[**DatabaseBlobAuditingPolicyListResult**](DatabaseBlobAuditingPolicyListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved database auditing settings. |  -  |
| **0** | *** Error Responses: ***   * 400 BlobAuditingIsNotSupportedOnResourceType - Blob Auditing is currently not supported for this resource type.   * 404 SourceDatabaseNotFound - The source database does not exist.   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 500 DatabaseIsUnavailable - Loading failed. Please try again later. |  -  |

<a id="extendedDatabaseBlobAuditingPoliciesCreateOrUpdate"></a>
# **extendedDatabaseBlobAuditingPoliciesCreateOrUpdate**
> ExtendedDatabaseBlobAuditingPolicy extendedDatabaseBlobAuditingPoliciesCreateOrUpdate(resourceGroupName, serverName, databaseName, blobAuditingPolicyName, subscriptionId, apiVersion, parameters)



Creates or updates an extended database&#39;s blob auditing policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobAuditingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BlobAuditingApi apiInstance = new BlobAuditingApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String blobAuditingPolicyName = "default"; // String | The name of the blob auditing policy.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    ExtendedDatabaseBlobAuditingPolicy parameters = new ExtendedDatabaseBlobAuditingPolicy(); // ExtendedDatabaseBlobAuditingPolicy | The extended database blob auditing policy.
    try {
      ExtendedDatabaseBlobAuditingPolicy result = apiInstance.extendedDatabaseBlobAuditingPoliciesCreateOrUpdate(resourceGroupName, serverName, databaseName, blobAuditingPolicyName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobAuditingApi#extendedDatabaseBlobAuditingPoliciesCreateOrUpdate");
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
| **blobAuditingPolicyName** | **String**| The name of the blob auditing policy. | [enum: default] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**ExtendedDatabaseBlobAuditingPolicy**](ExtendedDatabaseBlobAuditingPolicy.md)| The extended database blob auditing policy. | |

### Return type

[**ExtendedDatabaseBlobAuditingPolicy**](ExtendedDatabaseBlobAuditingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully set the extended database blob auditing policy. |  -  |
| **201** | Successfully created the extended database blob auditing policy. |  -  |
| **0** | *** Error Responses: ***   * 400 BlobAuditingIsNotSupportedOnResourceType - Blob Auditing is currently not supported for this resource type.   * 400 BlobAuditingPredicateExpressionSyntaxError - Invalid value of parameter &#39;predicateExpression&#39;.   * 400 InvalidDatabaseBlobAuditingPolicyCreateRequest - The create database blob auditing policy request does not exist or has no properties object.   * 400 InvalidBlobAuditActionsAndGroups - Invalid audit actions or action groups.   * 400 DataSecurityInvalidUserSuppliedParameter - An invalid parameter value was provided by the client.   * 400 BlobAuditingPredicateExpressionEmpty - Invalid parameter &#39;predicateExpression&#39;, value can not be empty.   * 400 BlobAuditingInvalidStorageAccountName - The provided storage account is not valid or does not exist.   * 400 UpdateNotAllowedOnPausedDatabase - User attempted to perform an update on a paused database.   * 400 BlobAuditingInvalidStorageAccountCredentials - The provided storage account or access key is not valid.   * 400 BlobAuditingIsNotSupportedOnGeoDr - Blob auditing can be configured on primary databases only.   * 400 InvalidBlobAuditActionsAndGroupsForDW - Unsupported audit actions or action groups for DW.   * 400 BlobAuditingInsufficientStorageAccountPermissions - Insufficient read or write permissions on the provided storage account.   * 400 BlobAuditingStorageAccountIsDisabled - The provided storage account is disabled.   * 400 InvalidBlobAuditActions - Invalid audit action   * 404 SourceDatabaseNotFound - The source database does not exist.   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 500 DatabaseIsUnavailable - Loading failed. Please try again later. |  -  |

<a id="extendedDatabaseBlobAuditingPoliciesGet"></a>
# **extendedDatabaseBlobAuditingPoliciesGet**
> ExtendedDatabaseBlobAuditingPolicy extendedDatabaseBlobAuditingPoliciesGet(resourceGroupName, serverName, databaseName, blobAuditingPolicyName, subscriptionId, apiVersion)



Gets an extended database&#39;s blob auditing policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobAuditingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BlobAuditingApi apiInstance = new BlobAuditingApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String blobAuditingPolicyName = "default"; // String | The name of the blob auditing policy.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      ExtendedDatabaseBlobAuditingPolicy result = apiInstance.extendedDatabaseBlobAuditingPoliciesGet(resourceGroupName, serverName, databaseName, blobAuditingPolicyName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobAuditingApi#extendedDatabaseBlobAuditingPoliciesGet");
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
| **blobAuditingPolicyName** | **String**| The name of the blob auditing policy. | [enum: default] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**ExtendedDatabaseBlobAuditingPolicy**](ExtendedDatabaseBlobAuditingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the extended database blob auditing policy. |  -  |
| **0** | *** Error Responses: ***   * 400 BlobAuditingIsNotSupportedOnResourceType - Blob Auditing is currently not supported for this resource type.   * 404 SourceDatabaseNotFound - The source database does not exist.   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 500 DatabaseIsUnavailable - Loading failed. Please try again later. |  -  |

<a id="extendedServerBlobAuditingPoliciesCreateOrUpdate"></a>
# **extendedServerBlobAuditingPoliciesCreateOrUpdate**
> ExtendedServerBlobAuditingPolicy extendedServerBlobAuditingPoliciesCreateOrUpdate(resourceGroupName, serverName, blobAuditingPolicyName, subscriptionId, apiVersion, parameters)



Creates or updates an extended server&#39;s blob auditing policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobAuditingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BlobAuditingApi apiInstance = new BlobAuditingApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String blobAuditingPolicyName = "default"; // String | The name of the blob auditing policy.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    ExtendedServerBlobAuditingPolicy parameters = new ExtendedServerBlobAuditingPolicy(); // ExtendedServerBlobAuditingPolicy | Properties of extended blob auditing policy
    try {
      ExtendedServerBlobAuditingPolicy result = apiInstance.extendedServerBlobAuditingPoliciesCreateOrUpdate(resourceGroupName, serverName, blobAuditingPolicyName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobAuditingApi#extendedServerBlobAuditingPoliciesCreateOrUpdate");
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
| **blobAuditingPolicyName** | **String**| The name of the blob auditing policy. | [enum: default] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**ExtendedServerBlobAuditingPolicy**](ExtendedServerBlobAuditingPolicy.md)| Properties of extended blob auditing policy | |

### Return type

[**ExtendedServerBlobAuditingPolicy**](ExtendedServerBlobAuditingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the extended auditing settings. |  -  |
| **202** | Updating the extended auditing settings is in progress. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidServerBlobAuditingPolicyCreateRequest - The create server blob auditing policy request does not exist or has no properties object.   * 400 InvalidBlobAuditActionsAndGroups - Invalid audit actions or action groups.   * 400 DataSecurityInvalidUserSuppliedParameter - An invalid parameter value was provided by the client.   * 400 BlobAuditingPredicateExpressionEmpty - Invalid parameter &#39;predicateExpression&#39;, value can not be empty.   * 400 InvalidBlobAuditActionsAndGroups - Invalid audit actions or action groups.   * 400 InvalidBlobAuditActions - Invalid audit action   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 409 ServerBlobAuditingPolicyInProgress - Set server blob auditing is already in progress. |  -  |

<a id="extendedServerBlobAuditingPoliciesGet"></a>
# **extendedServerBlobAuditingPoliciesGet**
> ExtendedServerBlobAuditingPolicy extendedServerBlobAuditingPoliciesGet(resourceGroupName, serverName, blobAuditingPolicyName, subscriptionId, apiVersion)



Gets an extended server&#39;s blob auditing policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobAuditingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BlobAuditingApi apiInstance = new BlobAuditingApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String blobAuditingPolicyName = "default"; // String | The name of the blob auditing policy.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      ExtendedServerBlobAuditingPolicy result = apiInstance.extendedServerBlobAuditingPoliciesGet(resourceGroupName, serverName, blobAuditingPolicyName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobAuditingApi#extendedServerBlobAuditingPoliciesGet");
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
| **blobAuditingPolicyName** | **String**| The name of the blob auditing policy. | [enum: default] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**ExtendedServerBlobAuditingPolicy**](ExtendedServerBlobAuditingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the extended server blob auditing policy. |  -  |
| **0** | *** Error Responses: ***   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription. |  -  |

<a id="serverBlobAuditingPoliciesCreateOrUpdate"></a>
# **serverBlobAuditingPoliciesCreateOrUpdate**
> ServerBlobAuditingPolicy serverBlobAuditingPoliciesCreateOrUpdate(resourceGroupName, serverName, blobAuditingPolicyName, subscriptionId, apiVersion, parameters)



Creates or updates a server&#39;s blob auditing policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobAuditingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BlobAuditingApi apiInstance = new BlobAuditingApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String blobAuditingPolicyName = "default"; // String | The name of the blob auditing policy.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    ServerBlobAuditingPolicy parameters = new ServerBlobAuditingPolicy(); // ServerBlobAuditingPolicy | Properties of blob auditing policy
    try {
      ServerBlobAuditingPolicy result = apiInstance.serverBlobAuditingPoliciesCreateOrUpdate(resourceGroupName, serverName, blobAuditingPolicyName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobAuditingApi#serverBlobAuditingPoliciesCreateOrUpdate");
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
| **blobAuditingPolicyName** | **String**| The name of the blob auditing policy. | [enum: default] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**ServerBlobAuditingPolicy**](ServerBlobAuditingPolicy.md)| Properties of blob auditing policy | |

### Return type

[**ServerBlobAuditingPolicy**](ServerBlobAuditingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the auditing settings. |  -  |
| **202** | Updating the auditing settings is in progress. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidServerBlobAuditingPolicyCreateRequest - The create server blob auditing policy request does not exist or has no properties object.   * 400 InvalidBlobAuditActionsAndGroups - Invalid audit actions or action groups.   * 400 DataSecurityInvalidUserSuppliedParameter - An invalid parameter value was provided by the client.   * 400 InvalidBlobAuditActionsAndGroups - Invalid audit actions or action groups.   * 400 InvalidBlobAuditActions - Invalid audit action   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 409 ServerBlobAuditingPolicyInProgress - Set server blob auditing is already in progress. |  -  |

<a id="serverBlobAuditingPoliciesGet"></a>
# **serverBlobAuditingPoliciesGet**
> ServerBlobAuditingPolicy serverBlobAuditingPoliciesGet(resourceGroupName, serverName, blobAuditingPolicyName, subscriptionId, apiVersion)



Gets a server&#39;s blob auditing policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobAuditingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BlobAuditingApi apiInstance = new BlobAuditingApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String blobAuditingPolicyName = "default"; // String | The name of the blob auditing policy.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      ServerBlobAuditingPolicy result = apiInstance.serverBlobAuditingPoliciesGet(resourceGroupName, serverName, blobAuditingPolicyName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobAuditingApi#serverBlobAuditingPoliciesGet");
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
| **blobAuditingPolicyName** | **String**| The name of the blob auditing policy. | [enum: default] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**ServerBlobAuditingPolicy**](ServerBlobAuditingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the server blob auditing policy. |  -  |
| **0** | *** Error Responses: ***   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription. |  -  |

<a id="serverBlobAuditingPoliciesListByServer"></a>
# **serverBlobAuditingPoliciesListByServer**
> ServerBlobAuditingPolicyListResult serverBlobAuditingPoliciesListByServer(resourceGroupName, serverName, subscriptionId, apiVersion)



Lists auditing settings of a server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobAuditingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BlobAuditingApi apiInstance = new BlobAuditingApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      ServerBlobAuditingPolicyListResult result = apiInstance.serverBlobAuditingPoliciesListByServer(resourceGroupName, serverName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobAuditingApi#serverBlobAuditingPoliciesListByServer");
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
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**ServerBlobAuditingPolicyListResult**](ServerBlobAuditingPolicyListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved server auditing settings. |  -  |
| **0** | *** Error Responses: ***   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription. |  -  |

