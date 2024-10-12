# ElasticPoolsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**elasticPoolsCreateOrUpdate**](ElasticPoolsApi.md#elasticPoolsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools/{elasticPoolName} |  |
| [**elasticPoolsDelete**](ElasticPoolsApi.md#elasticPoolsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools/{elasticPoolName} |  |
| [**elasticPoolsGet**](ElasticPoolsApi.md#elasticPoolsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools/{elasticPoolName} |  |
| [**elasticPoolsListByServer**](ElasticPoolsApi.md#elasticPoolsListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools |  |
| [**elasticPoolsUpdate**](ElasticPoolsApi.md#elasticPoolsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools/{elasticPoolName} |  |


<a id="elasticPoolsCreateOrUpdate"></a>
# **elasticPoolsCreateOrUpdate**
> ElasticPool elasticPoolsCreateOrUpdate(resourceGroupName, serverName, elasticPoolName, subscriptionId, apiVersion, parameters)



Creates or updates an elastic pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ElasticPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ElasticPoolsApi apiInstance = new ElasticPoolsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String elasticPoolName = "elasticPoolName_example"; // String | The name of the elastic pool.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    ElasticPool parameters = new ElasticPool(); // ElasticPool | The elastic pool parameters.
    try {
      ElasticPool result = apiInstance.elasticPoolsCreateOrUpdate(resourceGroupName, serverName, elasticPoolName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ElasticPoolsApi#elasticPoolsCreateOrUpdate");
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
| **elasticPoolName** | **String**| The name of the elastic pool. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**ElasticPool**](ElasticPool.md)| The elastic pool parameters. | |

### Return type

[**ElasticPool**](ElasticPool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated the elastic pool |  -  |
| **201** | Created the elastic pool |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 ElasticPoolStorageBelowLimitMB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ProvisioningDisabled - Displays error message from resources operation authorizer as is, without changes   * 400 ElasticPoolStorageNotAllowedMB - Attempting to set the elastic pool storage limit in mb which doesn&#39;t match the allowed values.   * 400 ElasticPoolStorageAboveLimitMB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ElasticPoolUpdateHkNotAllowed - The elastic pool cannot lower its service tier from Premium to Standard or Basic since one or more of its databases use memory-optimized objects.   * 400 ElasticPoolOverFileSpace - Insufficient file space in the elastic pool.   * 400 InvalidTier - The user specified an invalid tier.   * 400 ServerQuotaExceeded - Server cannot be added to a subscription because it will exceed quota.   * 400 ElasticPoolAlreadyExists - The server already contains an elastic pool with the specified name.   * 400 InvalidInputValueForEdition - Specified edition is not supported for elastic pool provisioning.   * 400 ElasticPoolDtuBelowLimit - The requested DTU value is too low for the requested elastic pool service tier.   * 400 ElasticPoolDtuAboveLimit - The requested DTU value is too high for the requested elastic pool service tier.   * 400 ElasticPoolDbDtuMaxBelowLimit - The requested per database DTU max is too low for the requested elastic pool service tier.   * 400 ElasticPoolDbDtuMaxAboveLimit - The requested per database DTU max is too high for the requested elastic pool service tier.   * 400 InvalidInputValueForDatabaseDtuMax - Attempting to set the DTU max per database for the Resource Pool which doesn&#39;t match the allowed values.   * 400 ElasticPoolDbDtuMinAboveLimit - The requested DTU min per database is too high for the requested service tier.   * 400 InvalidInputValueForDatabaseDtuMin - Attempting to set the DTU min per database for the Resource Pool which doesn&#39;t match the allowed values.   * 400 ElasticPoolStorageAboveLimitGB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ElasticPoolOverStorageUsage - Attempting to write data to a database when the storage limit of the elastic pool has been reached.   * 400 ElasticPoolsNotEnabled - Elastic pools have not been enabled in this region.   * 400 ElasticPoolNotEmpty - Request to delete an elastic pool that is not empty.   * 400 ElasticPoolStorageBelowLimitGB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ElasticPoolStorageNotAllowedGB - Attempting to set the elastic pool storage limit in gb which doesn&#39;t match the allowed values.   * 400 ElasticPoolDatabaseLimit - The elastic pool has reached its limit for number of databases.   * 400 ElasticPoolStorageDecreasePrecondition - There was an attempt to decrease the storage limit of the elastic pool below its storage usage.   * 400 ElasticPoolBusy - A management operation was attempted on an elastic pool which is busy.   * 400 InvalidInputValueDatabaseDtuMinLargerThanMax - Attempting to set the DTU min per database higher than the DTU max per database.   * 400 InvalidResourceRequestBody - The resource or resource properties in the request body is empty or invalid.   * 400 InvalidSkuName - Invalid SKU name.   * 400 MismatchedSkuNameAndCapacity - Mismatch between SKU name and capacity.   * 400 MismatchedSkuNameAndTier - Mismatch between SKU name and tier.   * 400 MismatchedSkuNameAndFamily - Mismatch between SKU name and family.   * 400 ElasticPoolStorageBelowLimitMB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ProvisioningDisabled - Displays error message from resources operation authorizer as is, without changes   * 400 ElasticPoolStorageNotAllowedMB - Attempting to set the elastic pool storage limit in mb which doesn&#39;t match the allowed values.   * 400 ElasticPoolStorageAboveLimitMB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ElasticPoolUpdateHkNotAllowed - The elastic pool cannot lower its service tier from Premium to Standard or Basic since one or more of its databases use memory-optimized objects.   * 400 ElasticPoolOverFileSpace - Insufficient file space in the elastic pool.   * 400 InvalidTier - The user specified an invalid tier.   * 400 ServerQuotaExceeded - Server cannot be added to a subscription because it will exceed quota.   * 400 ElasticPoolAlreadyExists - The server already contains an elastic pool with the specified name.   * 400 InvalidInputValueForEdition - Specified edition is not supported for elastic pool provisioning.   * 400 ElasticPoolDtuBelowLimit - The requested DTU value is too low for the requested elastic pool service tier.   * 400 ElasticPoolDtuAboveLimit - The requested DTU value is too high for the requested elastic pool service tier.   * 400 ElasticPoolDbDtuMaxBelowLimit - The requested per database DTU max is too low for the requested elastic pool service tier.   * 400 ElasticPoolDbDtuMaxAboveLimit - The requested per database DTU max is too high for the requested elastic pool service tier.   * 400 InvalidInputValueForDatabaseDtuMax - Attempting to set the DTU max per database for the Resource Pool which doesn&#39;t match the allowed values.   * 400 ElasticPoolDbDtuMinAboveLimit - The requested DTU min per database is too high for the requested service tier.   * 400 InvalidInputValueForDatabaseDtuMin - Attempting to set the DTU min per database for the Resource Pool which doesn&#39;t match the allowed values.   * 400 ElasticPoolStorageAboveLimitGB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ElasticPoolOverStorageUsage - Attempting to write data to a database when the storage limit of the elastic pool has been reached.   * 400 ElasticPoolsNotEnabled - Elastic pools have not been enabled in this region.   * 400 ElasticPoolNotEmpty - Request to delete an elastic pool that is not empty.   * 400 ElasticPoolStorageBelowLimitGB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ElasticPoolStorageNotAllowedGB - Attempting to set the elastic pool storage limit in gb which doesn&#39;t match the allowed values.   * 400 ElasticPoolDatabaseLimit - The elastic pool has reached its limit for number of databases.   * 400 ElasticPoolStorageDecreasePrecondition - There was an attempt to decrease the storage limit of the elastic pool below its storage usage.   * 400 ElasticPoolBusy - A management operation was attempted on an elastic pool which is busy.   * 400 InvalidInputValueDatabaseDtuMinLargerThanMax - Attempting to set the DTU min per database higher than the DTU max per database.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ElasticPoolNotFound - The specified elastic pool does not exist for the specified server.   * 404 OperationIdNotFound - The operation with Id does not exist.   * 404 ElasticPoolNotFound - The specified elastic pool does not exist for the specified server.   * 405 NotSupported - This functionality is not supported.   * 405 NotSupported - This functionality is not supported.   * 409 ServerDisabled - Server is disabled.   * 409 OperationCancelled - The operation has been cancelled by user.   * 409 OperationInterrupted - The operation on the resource could not be completed because it was interrupted by another operation on the same resource.   * 409 ServerDisabled - Server is disabled.   * 500 OperationTimedOut - The operation timed out and automatically rolled back. Please retry the operation.   * 503 ServiceTemporarilyUnavailable - Feature temporarily unavailable.   * 503 ServiceTemporarilyUnavailable - Feature temporarily unavailable. |  -  |

<a id="elasticPoolsDelete"></a>
# **elasticPoolsDelete**
> elasticPoolsDelete(resourceGroupName, serverName, elasticPoolName, subscriptionId, apiVersion)



Deletes an elastic pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ElasticPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ElasticPoolsApi apiInstance = new ElasticPoolsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String elasticPoolName = "elasticPoolName_example"; // String | The name of the elastic pool.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.elasticPoolsDelete(resourceGroupName, serverName, elasticPoolName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ElasticPoolsApi#elasticPoolsDelete");
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
| **elasticPoolName** | **String**| The name of the elastic pool. | |
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
| **200** | Deleted the elastic pool |  -  |
| **202** | Accepted |  -  |
| **204** | Elastic pool did not exist |  -  |
| **0** | *** Error Responses: ***   * 400 ElasticPoolStorageBelowLimitMB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ProvisioningDisabled - Displays error message from resources operation authorizer as is, without changes   * 400 ElasticPoolStorageNotAllowedMB - Attempting to set the elastic pool storage limit in mb which doesn&#39;t match the allowed values.   * 400 ElasticPoolStorageAboveLimitMB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ElasticPoolUpdateHkNotAllowed - The elastic pool cannot lower its service tier from Premium to Standard or Basic since one or more of its databases use memory-optimized objects.   * 400 ElasticPoolOverFileSpace - Insufficient file space in the elastic pool.   * 400 InvalidTier - The user specified an invalid tier.   * 400 ServerQuotaExceeded - Server cannot be added to a subscription because it will exceed quota.   * 400 ElasticPoolAlreadyExists - The server already contains an elastic pool with the specified name.   * 400 InvalidInputValueForEdition - Specified edition is not supported for elastic pool provisioning.   * 400 ElasticPoolDtuBelowLimit - The requested DTU value is too low for the requested elastic pool service tier.   * 400 ElasticPoolDtuAboveLimit - The requested DTU value is too high for the requested elastic pool service tier.   * 400 ElasticPoolDbDtuMaxBelowLimit - The requested per database DTU max is too low for the requested elastic pool service tier.   * 400 ElasticPoolDbDtuMaxAboveLimit - The requested per database DTU max is too high for the requested elastic pool service tier.   * 400 InvalidInputValueForDatabaseDtuMax - Attempting to set the DTU max per database for the Resource Pool which doesn&#39;t match the allowed values.   * 400 ElasticPoolDbDtuMinAboveLimit - The requested DTU min per database is too high for the requested service tier.   * 400 InvalidInputValueForDatabaseDtuMin - Attempting to set the DTU min per database for the Resource Pool which doesn&#39;t match the allowed values.   * 400 ElasticPoolStorageAboveLimitGB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ElasticPoolOverStorageUsage - Attempting to write data to a database when the storage limit of the elastic pool has been reached.   * 400 ElasticPoolsNotEnabled - Elastic pools have not been enabled in this region.   * 400 ElasticPoolNotEmpty - Request to delete an elastic pool that is not empty.   * 400 ElasticPoolStorageBelowLimitGB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ElasticPoolStorageNotAllowedGB - Attempting to set the elastic pool storage limit in gb which doesn&#39;t match the allowed values.   * 400 ElasticPoolDatabaseLimit - The elastic pool has reached its limit for number of databases.   * 400 ElasticPoolStorageDecreasePrecondition - There was an attempt to decrease the storage limit of the elastic pool below its storage usage.   * 400 ElasticPoolBusy - A management operation was attempted on an elastic pool which is busy.   * 400 InvalidInputValueDatabaseDtuMinLargerThanMax - Attempting to set the DTU min per database higher than the DTU max per database.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ElasticPoolNotFound - The specified elastic pool does not exist for the specified server.   * 404 OperationIdNotFound - The operation with Id does not exist.   * 405 NotSupported - This functionality is not supported.   * 409 ServerDisabled - Server is disabled.   * 409 OperationCancelled - The operation has been cancelled by user.   * 409 OperationInterrupted - The operation on the resource could not be completed because it was interrupted by another operation on the same resource.   * 500 OperationTimedOut - The operation timed out and automatically rolled back. Please retry the operation.   * 503 ServiceTemporarilyUnavailable - Feature temporarily unavailable. |  -  |

<a id="elasticPoolsGet"></a>
# **elasticPoolsGet**
> ElasticPool elasticPoolsGet(resourceGroupName, serverName, elasticPoolName, subscriptionId, apiVersion)



Gets an elastic pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ElasticPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ElasticPoolsApi apiInstance = new ElasticPoolsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String elasticPoolName = "elasticPoolName_example"; // String | The name of the elastic pool.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      ElasticPool result = apiInstance.elasticPoolsGet(resourceGroupName, serverName, elasticPoolName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ElasticPoolsApi#elasticPoolsGet");
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
| **elasticPoolName** | **String**| The name of the elastic pool. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**ElasticPool**](ElasticPool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Succeeded |  -  |
| **0** | *** Error Responses: ***   * 400 ElasticPoolStorageBelowLimitMB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ProvisioningDisabled - Displays error message from resources operation authorizer as is, without changes   * 400 ElasticPoolStorageNotAllowedMB - Attempting to set the elastic pool storage limit in mb which doesn&#39;t match the allowed values.   * 400 ElasticPoolStorageAboveLimitMB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ElasticPoolUpdateHkNotAllowed - The elastic pool cannot lower its service tier from Premium to Standard or Basic since one or more of its databases use memory-optimized objects.   * 400 ElasticPoolOverFileSpace - Insufficient file space in the elastic pool.   * 400 InvalidTier - The user specified an invalid tier.   * 400 ServerQuotaExceeded - Server cannot be added to a subscription because it will exceed quota.   * 400 ElasticPoolAlreadyExists - The server already contains an elastic pool with the specified name.   * 400 InvalidInputValueForEdition - Specified edition is not supported for elastic pool provisioning.   * 400 ElasticPoolDtuBelowLimit - The requested DTU value is too low for the requested elastic pool service tier.   * 400 ElasticPoolDtuAboveLimit - The requested DTU value is too high for the requested elastic pool service tier.   * 400 ElasticPoolDbDtuMaxBelowLimit - The requested per database DTU max is too low for the requested elastic pool service tier.   * 400 ElasticPoolDbDtuMaxAboveLimit - The requested per database DTU max is too high for the requested elastic pool service tier.   * 400 InvalidInputValueForDatabaseDtuMax - Attempting to set the DTU max per database for the Resource Pool which doesn&#39;t match the allowed values.   * 400 ElasticPoolDbDtuMinAboveLimit - The requested DTU min per database is too high for the requested service tier.   * 400 InvalidInputValueForDatabaseDtuMin - Attempting to set the DTU min per database for the Resource Pool which doesn&#39;t match the allowed values.   * 400 ElasticPoolStorageAboveLimitGB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ElasticPoolOverStorageUsage - Attempting to write data to a database when the storage limit of the elastic pool has been reached.   * 400 ElasticPoolsNotEnabled - Elastic pools have not been enabled in this region.   * 400 ElasticPoolNotEmpty - Request to delete an elastic pool that is not empty.   * 400 ElasticPoolStorageBelowLimitGB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ElasticPoolStorageNotAllowedGB - Attempting to set the elastic pool storage limit in gb which doesn&#39;t match the allowed values.   * 400 ElasticPoolDatabaseLimit - The elastic pool has reached its limit for number of databases.   * 400 ElasticPoolStorageDecreasePrecondition - There was an attempt to decrease the storage limit of the elastic pool below its storage usage.   * 400 ElasticPoolBusy - A management operation was attempted on an elastic pool which is busy.   * 400 InvalidInputValueDatabaseDtuMinLargerThanMax - Attempting to set the DTU min per database higher than the DTU max per database.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ElasticPoolNotFound - The specified elastic pool does not exist for the specified server.   * 404 OperationIdNotFound - The operation with Id does not exist.   * 404 ResourceNotFound - The requested resource was not found.   * 405 NotSupported - This functionality is not supported.   * 409 ServerDisabled - Server is disabled.   * 409 OperationCancelled - The operation has been cancelled by user.   * 409 OperationInterrupted - The operation on the resource could not be completed because it was interrupted by another operation on the same resource.   * 500 OperationTimedOut - The operation timed out and automatically rolled back. Please retry the operation.   * 503 ServiceTemporarilyUnavailable - Feature temporarily unavailable. |  -  |

<a id="elasticPoolsListByServer"></a>
# **elasticPoolsListByServer**
> ElasticPoolListResult elasticPoolsListByServer(resourceGroupName, serverName, subscriptionId, apiVersion, $skip)



Gets all elastic pools in a server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ElasticPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ElasticPoolsApi apiInstance = new ElasticPoolsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    Integer $skip = 56; // Integer | The number of elements in the collection to skip.
    try {
      ElasticPoolListResult result = apiInstance.elasticPoolsListByServer(resourceGroupName, serverName, subscriptionId, apiVersion, $skip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ElasticPoolsApi#elasticPoolsListByServer");
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
| **$skip** | **Integer**| The number of elements in the collection to skip. | [optional] |

### Return type

[**ElasticPoolListResult**](ElasticPoolListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Succeeded |  -  |
| **0** | *** Error Responses: ***   * 400 ElasticPoolStorageBelowLimitMB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ProvisioningDisabled - Displays error message from resources operation authorizer as is, without changes   * 400 ElasticPoolStorageNotAllowedMB - Attempting to set the elastic pool storage limit in mb which doesn&#39;t match the allowed values.   * 400 ElasticPoolStorageAboveLimitMB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ElasticPoolUpdateHkNotAllowed - The elastic pool cannot lower its service tier from Premium to Standard or Basic since one or more of its databases use memory-optimized objects.   * 400 ElasticPoolOverFileSpace - Insufficient file space in the elastic pool.   * 400 InvalidTier - The user specified an invalid tier.   * 400 ServerQuotaExceeded - Server cannot be added to a subscription because it will exceed quota.   * 400 ElasticPoolAlreadyExists - The server already contains an elastic pool with the specified name.   * 400 InvalidInputValueForEdition - Specified edition is not supported for elastic pool provisioning.   * 400 ElasticPoolDtuBelowLimit - The requested DTU value is too low for the requested elastic pool service tier.   * 400 ElasticPoolDtuAboveLimit - The requested DTU value is too high for the requested elastic pool service tier.   * 400 ElasticPoolDbDtuMaxBelowLimit - The requested per database DTU max is too low for the requested elastic pool service tier.   * 400 ElasticPoolDbDtuMaxAboveLimit - The requested per database DTU max is too high for the requested elastic pool service tier.   * 400 InvalidInputValueForDatabaseDtuMax - Attempting to set the DTU max per database for the Resource Pool which doesn&#39;t match the allowed values.   * 400 ElasticPoolDbDtuMinAboveLimit - The requested DTU min per database is too high for the requested service tier.   * 400 InvalidInputValueForDatabaseDtuMin - Attempting to set the DTU min per database for the Resource Pool which doesn&#39;t match the allowed values.   * 400 ElasticPoolStorageAboveLimitGB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ElasticPoolOverStorageUsage - Attempting to write data to a database when the storage limit of the elastic pool has been reached.   * 400 ElasticPoolsNotEnabled - Elastic pools have not been enabled in this region.   * 400 ElasticPoolNotEmpty - Request to delete an elastic pool that is not empty.   * 400 ElasticPoolStorageBelowLimitGB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ElasticPoolStorageNotAllowedGB - Attempting to set the elastic pool storage limit in gb which doesn&#39;t match the allowed values.   * 400 ElasticPoolDatabaseLimit - The elastic pool has reached its limit for number of databases.   * 400 ElasticPoolStorageDecreasePrecondition - There was an attempt to decrease the storage limit of the elastic pool below its storage usage.   * 400 ElasticPoolBusy - A management operation was attempted on an elastic pool which is busy.   * 400 InvalidInputValueDatabaseDtuMinLargerThanMax - Attempting to set the DTU min per database higher than the DTU max per database.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ElasticPoolNotFound - The specified elastic pool does not exist for the specified server.   * 404 OperationIdNotFound - The operation with Id does not exist.   * 405 NotSupported - This functionality is not supported.   * 409 ServerDisabled - Server is disabled.   * 409 OperationCancelled - The operation has been cancelled by user.   * 409 OperationInterrupted - The operation on the resource could not be completed because it was interrupted by another operation on the same resource.   * 500 OperationTimedOut - The operation timed out and automatically rolled back. Please retry the operation.   * 503 ServiceTemporarilyUnavailable - Feature temporarily unavailable. |  -  |

<a id="elasticPoolsUpdate"></a>
# **elasticPoolsUpdate**
> ElasticPool elasticPoolsUpdate(resourceGroupName, serverName, elasticPoolName, subscriptionId, apiVersion, parameters)



Updates an elastic pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ElasticPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ElasticPoolsApi apiInstance = new ElasticPoolsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String elasticPoolName = "elasticPoolName_example"; // String | The name of the elastic pool.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    ElasticPoolUpdate parameters = new ElasticPoolUpdate(); // ElasticPoolUpdate | The elastic pool update parameters.
    try {
      ElasticPool result = apiInstance.elasticPoolsUpdate(resourceGroupName, serverName, elasticPoolName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ElasticPoolsApi#elasticPoolsUpdate");
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
| **elasticPoolName** | **String**| The name of the elastic pool. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**ElasticPoolUpdate**](ElasticPoolUpdate.md)| The elastic pool update parameters. | |

### Return type

[**ElasticPool**](ElasticPool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated the elastic pool |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 ElasticPoolStorageBelowLimitMB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ProvisioningDisabled - Displays error message from resources operation authorizer as is, without changes   * 400 ElasticPoolStorageNotAllowedMB - Attempting to set the elastic pool storage limit in mb which doesn&#39;t match the allowed values.   * 400 ElasticPoolStorageAboveLimitMB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ElasticPoolUpdateHkNotAllowed - The elastic pool cannot lower its service tier from Premium to Standard or Basic since one or more of its databases use memory-optimized objects.   * 400 ElasticPoolOverFileSpace - Insufficient file space in the elastic pool.   * 400 InvalidTier - The user specified an invalid tier.   * 400 ServerQuotaExceeded - Server cannot be added to a subscription because it will exceed quota.   * 400 ElasticPoolAlreadyExists - The server already contains an elastic pool with the specified name.   * 400 InvalidInputValueForEdition - Specified edition is not supported for elastic pool provisioning.   * 400 ElasticPoolDtuBelowLimit - The requested DTU value is too low for the requested elastic pool service tier.   * 400 ElasticPoolDtuAboveLimit - The requested DTU value is too high for the requested elastic pool service tier.   * 400 ElasticPoolDbDtuMaxBelowLimit - The requested per database DTU max is too low for the requested elastic pool service tier.   * 400 ElasticPoolDbDtuMaxAboveLimit - The requested per database DTU max is too high for the requested elastic pool service tier.   * 400 InvalidInputValueForDatabaseDtuMax - Attempting to set the DTU max per database for the Resource Pool which doesn&#39;t match the allowed values.   * 400 ElasticPoolDbDtuMinAboveLimit - The requested DTU min per database is too high for the requested service tier.   * 400 InvalidInputValueForDatabaseDtuMin - Attempting to set the DTU min per database for the Resource Pool which doesn&#39;t match the allowed values.   * 400 ElasticPoolStorageAboveLimitGB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ElasticPoolOverStorageUsage - Attempting to write data to a database when the storage limit of the elastic pool has been reached.   * 400 ElasticPoolsNotEnabled - Elastic pools have not been enabled in this region.   * 400 ElasticPoolNotEmpty - Request to delete an elastic pool that is not empty.   * 400 ElasticPoolStorageBelowLimitGB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ElasticPoolStorageNotAllowedGB - Attempting to set the elastic pool storage limit in gb which doesn&#39;t match the allowed values.   * 400 ElasticPoolDatabaseLimit - The elastic pool has reached its limit for number of databases.   * 400 ElasticPoolStorageDecreasePrecondition - There was an attempt to decrease the storage limit of the elastic pool below its storage usage.   * 400 ElasticPoolBusy - A management operation was attempted on an elastic pool which is busy.   * 400 InvalidInputValueDatabaseDtuMinLargerThanMax - Attempting to set the DTU min per database higher than the DTU max per database.   * 400 InvalidResourceRequestBody - The resource or resource properties in the request body is empty or invalid.   * 400 InvalidSkuName - Invalid SKU name.   * 400 MismatchedSkuNameAndCapacity - Mismatch between SKU name and capacity.   * 400 MismatchedSkuNameAndTier - Mismatch between SKU name and tier.   * 400 MismatchedSkuNameAndFamily - Mismatch between SKU name and family.   * 400 ElasticPoolStorageBelowLimitMB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ProvisioningDisabled - Displays error message from resources operation authorizer as is, without changes   * 400 ElasticPoolStorageNotAllowedMB - Attempting to set the elastic pool storage limit in mb which doesn&#39;t match the allowed values.   * 400 ElasticPoolStorageAboveLimitMB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ElasticPoolUpdateHkNotAllowed - The elastic pool cannot lower its service tier from Premium to Standard or Basic since one or more of its databases use memory-optimized objects.   * 400 ElasticPoolOverFileSpace - Insufficient file space in the elastic pool.   * 400 InvalidTier - The user specified an invalid tier.   * 400 ServerQuotaExceeded - Server cannot be added to a subscription because it will exceed quota.   * 400 ElasticPoolAlreadyExists - The server already contains an elastic pool with the specified name.   * 400 InvalidInputValueForEdition - Specified edition is not supported for elastic pool provisioning.   * 400 ElasticPoolDtuBelowLimit - The requested DTU value is too low for the requested elastic pool service tier.   * 400 ElasticPoolDtuAboveLimit - The requested DTU value is too high for the requested elastic pool service tier.   * 400 ElasticPoolDbDtuMaxBelowLimit - The requested per database DTU max is too low for the requested elastic pool service tier.   * 400 ElasticPoolDbDtuMaxAboveLimit - The requested per database DTU max is too high for the requested elastic pool service tier.   * 400 InvalidInputValueForDatabaseDtuMax - Attempting to set the DTU max per database for the Resource Pool which doesn&#39;t match the allowed values.   * 400 ElasticPoolDbDtuMinAboveLimit - The requested DTU min per database is too high for the requested service tier.   * 400 InvalidInputValueForDatabaseDtuMin - Attempting to set the DTU min per database for the Resource Pool which doesn&#39;t match the allowed values.   * 400 ElasticPoolStorageAboveLimitGB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ElasticPoolOverStorageUsage - Attempting to write data to a database when the storage limit of the elastic pool has been reached.   * 400 ElasticPoolsNotEnabled - Elastic pools have not been enabled in this region.   * 400 ElasticPoolNotEmpty - Request to delete an elastic pool that is not empty.   * 400 ElasticPoolStorageBelowLimitGB - Attempting to set the elastic pool storage limit below the supported limit.   * 400 ElasticPoolStorageNotAllowedGB - Attempting to set the elastic pool storage limit in gb which doesn&#39;t match the allowed values.   * 400 ElasticPoolDatabaseLimit - The elastic pool has reached its limit for number of databases.   * 400 ElasticPoolStorageDecreasePrecondition - There was an attempt to decrease the storage limit of the elastic pool below its storage usage.   * 400 ElasticPoolBusy - A management operation was attempted on an elastic pool which is busy.   * 400 InvalidInputValueDatabaseDtuMinLargerThanMax - Attempting to set the DTU min per database higher than the DTU max per database.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ElasticPoolNotFound - The specified elastic pool does not exist for the specified server.   * 404 OperationIdNotFound - The operation with Id does not exist.   * 404 ElasticPoolNotFound - The specified elastic pool does not exist for the specified server.   * 405 NotSupported - This functionality is not supported.   * 405 NotSupported - This functionality is not supported.   * 409 ServerDisabled - Server is disabled.   * 409 OperationCancelled - The operation has been cancelled by user.   * 409 OperationInterrupted - The operation on the resource could not be completed because it was interrupted by another operation on the same resource.   * 409 ServerDisabled - Server is disabled.   * 500 OperationTimedOut - The operation timed out and automatically rolled back. Please retry the operation.   * 503 ServiceTemporarilyUnavailable - Feature temporarily unavailable.   * 503 ServiceTemporarilyUnavailable - Feature temporarily unavailable. |  -  |

