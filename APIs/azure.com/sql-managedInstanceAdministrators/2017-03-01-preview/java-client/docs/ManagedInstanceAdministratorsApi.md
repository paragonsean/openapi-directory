# ManagedInstanceAdministratorsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**managedInstanceAdministratorsCreateOrUpdate**](ManagedInstanceAdministratorsApi.md#managedInstanceAdministratorsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/administrators/{administratorName} |  |
| [**managedInstanceAdministratorsDelete**](ManagedInstanceAdministratorsApi.md#managedInstanceAdministratorsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/administrators/{administratorName} |  |
| [**managedInstanceAdministratorsGet**](ManagedInstanceAdministratorsApi.md#managedInstanceAdministratorsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/administrators/{administratorName} |  |
| [**managedInstanceAdministratorsListByInstance**](ManagedInstanceAdministratorsApi.md#managedInstanceAdministratorsListByInstance) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/administrators |  |


<a id="managedInstanceAdministratorsCreateOrUpdate"></a>
# **managedInstanceAdministratorsCreateOrUpdate**
> ManagedInstanceAdministrator managedInstanceAdministratorsCreateOrUpdate(resourceGroupName, managedInstanceName, administratorName, subscriptionId, apiVersion, parameters)



Creates or updates a managed instance administrator.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedInstanceAdministratorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ManagedInstanceAdministratorsApi apiInstance = new ManagedInstanceAdministratorsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
    String administratorName = "ActiveDirectory"; // String | The requested administrator name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    ManagedInstanceAdministrator parameters = new ManagedInstanceAdministrator(); // ManagedInstanceAdministrator | The requested administrator parameters.
    try {
      ManagedInstanceAdministrator result = apiInstance.managedInstanceAdministratorsCreateOrUpdate(resourceGroupName, managedInstanceName, administratorName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedInstanceAdministratorsApi#managedInstanceAdministratorsCreateOrUpdate");
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
| **administratorName** | **String**| The requested administrator name. | [enum: ActiveDirectory] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**ManagedInstanceAdministrator**](ManagedInstanceAdministrator.md)| The requested administrator parameters. | |

### Return type

[**ManagedInstanceAdministrator**](ManagedInstanceAdministrator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the managed instance administrator. |  -  |
| **201** | Successfully created the managed instance administrator. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 SubscriptionNotFound - The requested subscription was not found.   * 400 InvalidManagedServerAdministratorType - Invalid administrator type specified in properties.   * 400 InvalidResourceRequestBody - The resource or resource properties in the request body is empty or invalid.   * 400 InvalidParameterValue - An invalid value was given to a parameter.   * 400 InvalidLoginName - The provided login name is invalid.   * 400 PrincipalNotFoundInTenant - AzureAD Lookup returned no results for this name.   * 400 ManagedInstanceIsBusy - Managed Instance is busy with another request.   * 400 InvalidPrincipalType - This principal type is not supported in Windows Azure SQL Database.   * 400 TenantNotFoundInActiveDirectory - Tenant is not available in active directory.   * 400 InvalidUsername - Supplied user name contains invalid characters.   * 404 ServerNotInSubscription - Specified server does not exist on the specified subscription.   * 404 ManagedInstanceNotInSubscriptionResourceGroup - Specified managed instance does not exist in the specified resource group and subscription.   * 404 OperationIdNotFound - The operation with Id does not exist.   * 404 ResourceNotFound - The requested resource was not found.   * 409 OperationCancelled - The operation has been cancelled by user.   * 409 OperationInterrupted - The operation on the resource could not be completed because it was interrupted by another operation on the same resource.   * 429 SubscriptionTooManyCreateUpdateRequests - Requests beyond max requests that can be processed by available resources.   * 429 SubscriptionTooManyRequests - Requests beyond max requests that can be processed by available resources.   * 500 OperationTimedOut - The operation timed out and automatically rolled back. Please retry the operation.   * 500 ActiveDirectoryLookupTimedOut - The operation could not be completed at this time. Please try again later.   * 503 TooManyRequests - Requests beyond max requests that can be processed by available resources.   * 504 RequestTimeout - Service request exceeded the allowed timeout. |  -  |

<a id="managedInstanceAdministratorsDelete"></a>
# **managedInstanceAdministratorsDelete**
> managedInstanceAdministratorsDelete(resourceGroupName, managedInstanceName, administratorName, subscriptionId, apiVersion)



Deletes a managed instance administrator.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedInstanceAdministratorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ManagedInstanceAdministratorsApi apiInstance = new ManagedInstanceAdministratorsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
    String administratorName = "ActiveDirectory"; // String | The administrator name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.managedInstanceAdministratorsDelete(resourceGroupName, managedInstanceName, administratorName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedInstanceAdministratorsApi#managedInstanceAdministratorsDelete");
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
| **administratorName** | **String**| The administrator name. | [enum: ActiveDirectory] |
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
| **200** | Successfully deleted the managed instance administrator. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 SubscriptionNotFound - The requested subscription was not found.   * 400 InvalidManagedServerAdministratorType - Invalid administrator type specified in properties.   * 400 InvalidResourceRequestBody - The resource or resource properties in the request body is empty or invalid.   * 400 InvalidParameterValue - An invalid value was given to a parameter.   * 400 InvalidLoginName - The provided login name is invalid.   * 400 PrincipalNotFoundInTenant - AzureAD Lookup returned no results for this name.   * 400 ManagedInstanceIsBusy - Managed Instance is busy with another request.   * 400 InvalidPrincipalType - This principal type is not supported in Windows Azure SQL Database.   * 400 TenantNotFoundInActiveDirectory - Tenant is not available in active directory.   * 400 InvalidUsername - Supplied user name contains invalid characters.   * 404 ServerNotInSubscription - Specified server does not exist on the specified subscription.   * 404 ManagedInstanceNotInSubscriptionResourceGroup - Specified managed instance does not exist in the specified resource group and subscription.   * 404 OperationIdNotFound - The operation with Id does not exist.   * 404 ResourceNotFound - The requested resource was not found.   * 409 OperationCancelled - The operation has been cancelled by user.   * 409 OperationInterrupted - The operation on the resource could not be completed because it was interrupted by another operation on the same resource.   * 429 SubscriptionTooManyCreateUpdateRequests - Requests beyond max requests that can be processed by available resources.   * 429 SubscriptionTooManyRequests - Requests beyond max requests that can be processed by available resources.   * 500 OperationTimedOut - The operation timed out and automatically rolled back. Please retry the operation.   * 500 ActiveDirectoryLookupTimedOut - The operation could not be completed at this time. Please try again later.   * 503 TooManyRequests - Requests beyond max requests that can be processed by available resources.   * 504 RequestTimeout - Service request exceeded the allowed timeout. |  -  |

<a id="managedInstanceAdministratorsGet"></a>
# **managedInstanceAdministratorsGet**
> ManagedInstanceAdministrator managedInstanceAdministratorsGet(resourceGroupName, managedInstanceName, administratorName, subscriptionId, apiVersion)



Gets a managed instance administrator.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedInstanceAdministratorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ManagedInstanceAdministratorsApi apiInstance = new ManagedInstanceAdministratorsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
    String administratorName = "ActiveDirectory"; // String | The administrator name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      ManagedInstanceAdministrator result = apiInstance.managedInstanceAdministratorsGet(resourceGroupName, managedInstanceName, administratorName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedInstanceAdministratorsApi#managedInstanceAdministratorsGet");
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
| **administratorName** | **String**| The administrator name. | [enum: ActiveDirectory] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**ManagedInstanceAdministrator**](ManagedInstanceAdministrator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the specified managed instance administrator. |  -  |
| **0** | *** Error Responses: ***   * 400 SubscriptionNotFound - The requested subscription was not found.   * 400 InvalidManagedServerAdministratorType - Invalid administrator type specified in properties.   * 400 InvalidResourceRequestBody - The resource or resource properties in the request body is empty or invalid.   * 404 ServerNotInSubscription - Specified server does not exist on the specified subscription.   * 404 ManagedInstanceNotInSubscriptionResourceGroup - Specified managed instance does not exist in the specified resource group and subscription.   * 404 ResourceNotFound - The requested resource was not found.   * 429 SubscriptionTooManyCreateUpdateRequests - Requests beyond max requests that can be processed by available resources.   * 429 SubscriptionTooManyRequests - Requests beyond max requests that can be processed by available resources.   * 503 TooManyRequests - Requests beyond max requests that can be processed by available resources.   * 504 RequestTimeout - Service request exceeded the allowed timeout. |  -  |

<a id="managedInstanceAdministratorsListByInstance"></a>
# **managedInstanceAdministratorsListByInstance**
> ManagedInstanceAdministratorListResult managedInstanceAdministratorsListByInstance(resourceGroupName, managedInstanceName, subscriptionId, apiVersion)



Gets a list of managed instance administrators.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedInstanceAdministratorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ManagedInstanceAdministratorsApi apiInstance = new ManagedInstanceAdministratorsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      ManagedInstanceAdministratorListResult result = apiInstance.managedInstanceAdministratorsListByInstance(resourceGroupName, managedInstanceName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedInstanceAdministratorsApi#managedInstanceAdministratorsListByInstance");
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
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**ManagedInstanceAdministratorListResult**](ManagedInstanceAdministratorListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of managed instance administrators. |  -  |
| **0** | *** Error Responses: ***   * 400 SubscriptionNotFound - The requested subscription was not found.   * 404 ServerNotInSubscription - Specified server does not exist on the specified subscription.   * 404 ManagedInstanceNotInSubscriptionResourceGroup - Specified managed instance does not exist in the specified resource group and subscription.   * 404 ResourceNotFound - The requested resource was not found.   * 429 SubscriptionTooManyCreateUpdateRequests - Requests beyond max requests that can be processed by available resources.   * 429 SubscriptionTooManyRequests - Requests beyond max requests that can be processed by available resources.   * 503 TooManyRequests - Requests beyond max requests that can be processed by available resources.   * 504 RequestTimeout - Service request exceeded the allowed timeout. |  -  |

