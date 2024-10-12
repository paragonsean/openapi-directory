# BlobAuditingApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**databaseBlobAuditingPoliciesCreateOrUpdate**](BlobAuditingApi.md#databaseBlobAuditingPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/auditingSettings/{blobAuditingPolicyName} |  |
| [**databaseBlobAuditingPoliciesGet**](BlobAuditingApi.md#databaseBlobAuditingPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/auditingSettings/{blobAuditingPolicyName} |  |


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
    String databaseName = "databaseName_example"; // String | The name of the database for which the blob auditing policy will be defined.
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
| **databaseName** | **String**| The name of the database for which the blob auditing policy will be defined. | |
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
| **0** | *** Error Responses: ***   * 400 BlobAuditingIsNotSupportedOnResourceType - Blob Auditing is currently not supported for this resource type.   * 400 InvalidDatabaseBlobAuditingPolicyCreateRequest - The create database blob auditing policy request does not exist or has no properties object.   * 400 InvalidBlobAuditActionsAndGroups - Invalid audit actions or action groups.   * 400 DataSecurityInvalidUserSuppliedParameter - An invalid parameter value was provided by the client.   * 404 SourceDatabaseNotFound - The source database does not exist.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 500 DatabaseIsUnavailable - Loading failed. Please try again later.   * 500 UpsertBlobAuditingPolicyFailed - An error has occurred while saving Auditing settings, please try again later |  -  |

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
    String databaseName = "databaseName_example"; // String | The name of the database for which the blob audit policy is defined.
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
| **databaseName** | **String**| The name of the database for which the blob audit policy is defined. | |
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
| **0** | *** Error Responses: ***   * 400 BlobAuditingIsNotSupportedOnResourceType - Blob Auditing is currently not supported for this resource type.   * 400 InvalidDatabaseBlobAuditingPolicyCreateRequest - The create database blob auditing policy request does not exist or has no properties object.   * 400 InvalidBlobAuditActionsAndGroups - Invalid audit actions or action groups.   * 400 DataSecurityInvalidUserSuppliedParameter - An invalid parameter value was provided by the client.   * 404 SourceDatabaseNotFound - The source database does not exist.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 500 DatabaseIsUnavailable - Loading failed. Please try again later.   * 500 GetBlobAuditingPolicyFailed - Failed to get Auditing settings |  -  |

