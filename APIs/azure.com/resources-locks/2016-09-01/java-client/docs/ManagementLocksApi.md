# ManagementLocksApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**managementLocksCreateOrUpdateAtResourceGroupLevel**](ManagementLocksApi.md#managementLocksCreateOrUpdateAtResourceGroupLevel) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/locks/{lockName} | Creates or updates a management lock at the resource group level. |
| [**managementLocksCreateOrUpdateAtResourceLevel**](ManagementLocksApi.md#managementLocksCreateOrUpdateAtResourceLevel) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/locks/{lockName} | Creates or updates a management lock at the resource level or any level below the resource. |
| [**managementLocksCreateOrUpdateAtSubscriptionLevel**](ManagementLocksApi.md#managementLocksCreateOrUpdateAtSubscriptionLevel) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/locks/{lockName} | Creates or updates a management lock at the subscription level. |
| [**managementLocksCreateOrUpdateByScope**](ManagementLocksApi.md#managementLocksCreateOrUpdateByScope) | **PUT** /{scope}/providers/Microsoft.Authorization/locks/{lockName} |  |
| [**managementLocksDeleteAtResourceGroupLevel**](ManagementLocksApi.md#managementLocksDeleteAtResourceGroupLevel) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/locks/{lockName} | Deletes a management lock at the resource group level. |
| [**managementLocksDeleteAtResourceLevel**](ManagementLocksApi.md#managementLocksDeleteAtResourceLevel) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/locks/{lockName} | Deletes the management lock of a resource or any level below the resource. |
| [**managementLocksDeleteAtSubscriptionLevel**](ManagementLocksApi.md#managementLocksDeleteAtSubscriptionLevel) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/locks/{lockName} | Deletes the management lock at the subscription level. |
| [**managementLocksDeleteByScope**](ManagementLocksApi.md#managementLocksDeleteByScope) | **DELETE** /{scope}/providers/Microsoft.Authorization/locks/{lockName} |  |
| [**managementLocksGetAtResourceGroupLevel**](ManagementLocksApi.md#managementLocksGetAtResourceGroupLevel) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/locks/{lockName} |  |
| [**managementLocksGetAtResourceLevel**](ManagementLocksApi.md#managementLocksGetAtResourceLevel) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/locks/{lockName} |  |
| [**managementLocksGetAtSubscriptionLevel**](ManagementLocksApi.md#managementLocksGetAtSubscriptionLevel) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/locks/{lockName} |  |
| [**managementLocksGetByScope**](ManagementLocksApi.md#managementLocksGetByScope) | **GET** /{scope}/providers/Microsoft.Authorization/locks/{lockName} |  |
| [**managementLocksListAtResourceGroupLevel**](ManagementLocksApi.md#managementLocksListAtResourceGroupLevel) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/locks |  |
| [**managementLocksListAtResourceLevel**](ManagementLocksApi.md#managementLocksListAtResourceLevel) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/locks |  |
| [**managementLocksListAtSubscriptionLevel**](ManagementLocksApi.md#managementLocksListAtSubscriptionLevel) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/locks |  |
| [**managementLocksListByScope**](ManagementLocksApi.md#managementLocksListByScope) | **GET** /{scope}/providers/Microsoft.Authorization/locks |  |


<a id="managementLocksCreateOrUpdateAtResourceGroupLevel"></a>
# **managementLocksCreateOrUpdateAtResourceGroupLevel**
> ManagementLockObject managementLocksCreateOrUpdateAtResourceGroupLevel(resourceGroupName, lockName, apiVersion, subscriptionId, parameters)

Creates or updates a management lock at the resource group level.

When you apply a lock at a parent scope, all child resources inherit the same lock. To create management locks, you must have access to Microsoft.Authorization/_* or Microsoft.Authorization/locks/_* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementLocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementLocksApi apiInstance = new ManagementLocksApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to lock.
    String lockName = "lockName_example"; // String | The lock name. The lock name can be a maximum of 260 characters. It cannot contain <, > %, &, :, \\, ?, /, or any control characters.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    ManagementLockObject parameters = new ManagementLockObject(); // ManagementLockObject | The management lock parameters.
    try {
      ManagementLockObject result = apiInstance.managementLocksCreateOrUpdateAtResourceGroupLevel(resourceGroupName, lockName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementLocksApi#managementLocksCreateOrUpdateAtResourceGroupLevel");
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
| **resourceGroupName** | **String**| The name of the resource group to lock. | |
| **lockName** | **String**| The lock name. The lock name can be a maximum of 260 characters. It cannot contain &lt;, &gt; %, &amp;, :, \\, ?, /, or any control characters. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**ManagementLockObject**](ManagementLockObject.md)| The management lock parameters. | |

### Return type

[**ManagementLockObject**](ManagementLockObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the lock. |  -  |
| **201** | Created - Returns information about the lock. |  -  |

<a id="managementLocksCreateOrUpdateAtResourceLevel"></a>
# **managementLocksCreateOrUpdateAtResourceLevel**
> ManagementLockObject managementLocksCreateOrUpdateAtResourceLevel(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, lockName, apiVersion, subscriptionId, parameters)

Creates or updates a management lock at the resource level or any level below the resource.

When you apply a lock at a parent scope, all child resources inherit the same lock. To create management locks, you must have access to Microsoft.Authorization/_* or Microsoft.Authorization/locks/_* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementLocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementLocksApi apiInstance = new ManagementLocksApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the resource to lock. 
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The resource provider namespace of the resource to lock.
    String parentResourcePath = "parentResourcePath_example"; // String | The parent resource identity.
    String resourceType = "resourceType_example"; // String | The resource type of the resource to lock.
    String resourceName = "resourceName_example"; // String | The name of the resource to lock.
    String lockName = "lockName_example"; // String | The name of lock. The lock name can be a maximum of 260 characters. It cannot contain <, > %, &, :, \\, ?, /, or any control characters.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    ManagementLockObject parameters = new ManagementLockObject(); // ManagementLockObject | Parameters for creating or updating a  management lock.
    try {
      ManagementLockObject result = apiInstance.managementLocksCreateOrUpdateAtResourceLevel(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, lockName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementLocksApi#managementLocksCreateOrUpdateAtResourceLevel");
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
| **resourceGroupName** | **String**| The name of the resource group containing the resource to lock.  | |
| **resourceProviderNamespace** | **String**| The resource provider namespace of the resource to lock. | |
| **parentResourcePath** | **String**| The parent resource identity. | |
| **resourceType** | **String**| The resource type of the resource to lock. | |
| **resourceName** | **String**| The name of the resource to lock. | |
| **lockName** | **String**| The name of lock. The lock name can be a maximum of 260 characters. It cannot contain &lt;, &gt; %, &amp;, :, \\, ?, /, or any control characters. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**ManagementLockObject**](ManagementLockObject.md)| Parameters for creating or updating a  management lock. | |

### Return type

[**ManagementLockObject**](ManagementLockObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the lock. |  -  |
| **201** | Created - Returns information about the lock. |  -  |

<a id="managementLocksCreateOrUpdateAtSubscriptionLevel"></a>
# **managementLocksCreateOrUpdateAtSubscriptionLevel**
> ManagementLockObject managementLocksCreateOrUpdateAtSubscriptionLevel(lockName, apiVersion, subscriptionId, parameters)

Creates or updates a management lock at the subscription level.

When you apply a lock at a parent scope, all child resources inherit the same lock. To create management locks, you must have access to Microsoft.Authorization/_* or Microsoft.Authorization/locks/_* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementLocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementLocksApi apiInstance = new ManagementLocksApi(defaultClient);
    String lockName = "lockName_example"; // String | The name of lock. The lock name can be a maximum of 260 characters. It cannot contain <, > %, &, :, \\, ?, /, or any control characters.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    ManagementLockObject parameters = new ManagementLockObject(); // ManagementLockObject | The management lock parameters.
    try {
      ManagementLockObject result = apiInstance.managementLocksCreateOrUpdateAtSubscriptionLevel(lockName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementLocksApi#managementLocksCreateOrUpdateAtSubscriptionLevel");
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
| **lockName** | **String**| The name of lock. The lock name can be a maximum of 260 characters. It cannot contain &lt;, &gt; %, &amp;, :, \\, ?, /, or any control characters. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**ManagementLockObject**](ManagementLockObject.md)| The management lock parameters. | |

### Return type

[**ManagementLockObject**](ManagementLockObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the lock. |  -  |
| **201** | Created - Returns information about the lock. |  -  |

<a id="managementLocksCreateOrUpdateByScope"></a>
# **managementLocksCreateOrUpdateByScope**
> ManagementLockObject managementLocksCreateOrUpdateByScope(scope, lockName, apiVersion, parameters)



Create or update a management lock by scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementLocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementLocksApi apiInstance = new ManagementLocksApi(defaultClient);
    String scope = "scope_example"; // String | The scope for the lock. When providing a scope for the assignment, use '/subscriptions/{subscriptionId}' for subscriptions, '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}' for resource groups, and '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePathIfPresent}/{resourceType}/{resourceName}' for resources.
    String lockName = "lockName_example"; // String | The name of lock.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    ManagementLockObject parameters = new ManagementLockObject(); // ManagementLockObject | Create or update management lock parameters.
    try {
      ManagementLockObject result = apiInstance.managementLocksCreateOrUpdateByScope(scope, lockName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementLocksApi#managementLocksCreateOrUpdateByScope");
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
| **scope** | **String**| The scope for the lock. When providing a scope for the assignment, use &#39;/subscriptions/{subscriptionId}&#39; for subscriptions, &#39;/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}&#39; for resource groups, and &#39;/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePathIfPresent}/{resourceType}/{resourceName}&#39; for resources. | |
| **lockName** | **String**| The name of lock. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **parameters** | [**ManagementLockObject**](ManagementLockObject.md)| Create or update management lock parameters. | |

### Return type

[**ManagementLockObject**](ManagementLockObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |

<a id="managementLocksDeleteAtResourceGroupLevel"></a>
# **managementLocksDeleteAtResourceGroupLevel**
> managementLocksDeleteAtResourceGroupLevel(resourceGroupName, lockName, apiVersion, subscriptionId)

Deletes a management lock at the resource group level.

To delete management locks, you must have access to Microsoft.Authorization/_* or Microsoft.Authorization/locks/_* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementLocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementLocksApi apiInstance = new ManagementLocksApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the lock.
    String lockName = "lockName_example"; // String | The name of lock to delete.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      apiInstance.managementLocksDeleteAtResourceGroupLevel(resourceGroupName, lockName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementLocksApi#managementLocksDeleteAtResourceGroupLevel");
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
| **resourceGroupName** | **String**| The name of the resource group containing the lock. | |
| **lockName** | **String**| The name of lock to delete. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | NoContent |  -  |

<a id="managementLocksDeleteAtResourceLevel"></a>
# **managementLocksDeleteAtResourceLevel**
> managementLocksDeleteAtResourceLevel(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, lockName, apiVersion, subscriptionId)

Deletes the management lock of a resource or any level below the resource.

To delete management locks, you must have access to Microsoft.Authorization/_* or Microsoft.Authorization/locks/_* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementLocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementLocksApi apiInstance = new ManagementLocksApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the resource with the lock to delete. 
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The resource provider namespace of the resource with the lock to delete.
    String parentResourcePath = "parentResourcePath_example"; // String | The parent resource identity.
    String resourceType = "resourceType_example"; // String | The resource type of the resource with the lock to delete.
    String resourceName = "resourceName_example"; // String | The name of the resource with the lock to delete.
    String lockName = "lockName_example"; // String | The name of the lock to delete.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      apiInstance.managementLocksDeleteAtResourceLevel(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, lockName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementLocksApi#managementLocksDeleteAtResourceLevel");
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
| **resourceGroupName** | **String**| The name of the resource group containing the resource with the lock to delete.  | |
| **resourceProviderNamespace** | **String**| The resource provider namespace of the resource with the lock to delete. | |
| **parentResourcePath** | **String**| The parent resource identity. | |
| **resourceType** | **String**| The resource type of the resource with the lock to delete. | |
| **resourceName** | **String**| The name of the resource with the lock to delete. | |
| **lockName** | **String**| The name of the lock to delete. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | NoContent |  -  |

<a id="managementLocksDeleteAtSubscriptionLevel"></a>
# **managementLocksDeleteAtSubscriptionLevel**
> managementLocksDeleteAtSubscriptionLevel(lockName, apiVersion, subscriptionId)

Deletes the management lock at the subscription level.

To delete management locks, you must have access to Microsoft.Authorization/_* or Microsoft.Authorization/locks/_* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementLocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementLocksApi apiInstance = new ManagementLocksApi(defaultClient);
    String lockName = "lockName_example"; // String | The name of lock to delete.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      apiInstance.managementLocksDeleteAtSubscriptionLevel(lockName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementLocksApi#managementLocksDeleteAtSubscriptionLevel");
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
| **lockName** | **String**| The name of lock to delete. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | NoContent |  -  |

<a id="managementLocksDeleteByScope"></a>
# **managementLocksDeleteByScope**
> managementLocksDeleteByScope(scope, lockName, apiVersion)



Delete a management lock by scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementLocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementLocksApi apiInstance = new ManagementLocksApi(defaultClient);
    String scope = "scope_example"; // String | The scope for the lock. 
    String lockName = "lockName_example"; // String | The name of lock.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    try {
      apiInstance.managementLocksDeleteByScope(scope, lockName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementLocksApi#managementLocksDeleteByScope");
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
| **scope** | **String**| The scope for the lock.  | |
| **lockName** | **String**| The name of lock. | |
| **apiVersion** | **String**| The API version to use for the operation. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | NoContent |  -  |

<a id="managementLocksGetAtResourceGroupLevel"></a>
# **managementLocksGetAtResourceGroupLevel**
> ManagementLockObject managementLocksGetAtResourceGroupLevel(resourceGroupName, lockName, apiVersion, subscriptionId)



Gets a management lock at the resource group level.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementLocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementLocksApi apiInstance = new ManagementLocksApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the locked resource group.
    String lockName = "lockName_example"; // String | The name of the lock to get.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      ManagementLockObject result = apiInstance.managementLocksGetAtResourceGroupLevel(resourceGroupName, lockName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementLocksApi#managementLocksGetAtResourceGroupLevel");
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
| **resourceGroupName** | **String**| The name of the locked resource group. | |
| **lockName** | **String**| The name of the lock to get. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**ManagementLockObject**](ManagementLockObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the lock. |  -  |

<a id="managementLocksGetAtResourceLevel"></a>
# **managementLocksGetAtResourceLevel**
> ManagementLockObject managementLocksGetAtResourceLevel(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, lockName, apiVersion, subscriptionId)



Get the management lock of a resource or any level below resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementLocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementLocksApi apiInstance = new ManagementLocksApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. 
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
    String parentResourcePath = "parentResourcePath_example"; // String | An extra path parameter needed in some services, like SQL Databases.
    String resourceType = "resourceType_example"; // String | The type of the resource.
    String resourceName = "resourceName_example"; // String | The name of the resource.
    String lockName = "lockName_example"; // String | The name of lock.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      ManagementLockObject result = apiInstance.managementLocksGetAtResourceLevel(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, lockName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementLocksApi#managementLocksGetAtResourceLevel");
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
| **resourceGroupName** | **String**| The name of the resource group.  | |
| **resourceProviderNamespace** | **String**| The namespace of the resource provider. | |
| **parentResourcePath** | **String**| An extra path parameter needed in some services, like SQL Databases. | |
| **resourceType** | **String**| The type of the resource. | |
| **resourceName** | **String**| The name of the resource. | |
| **lockName** | **String**| The name of lock. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**ManagementLockObject**](ManagementLockObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="managementLocksGetAtSubscriptionLevel"></a>
# **managementLocksGetAtSubscriptionLevel**
> ManagementLockObject managementLocksGetAtSubscriptionLevel(lockName, apiVersion, subscriptionId)



Gets a management lock at the subscription level.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementLocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementLocksApi apiInstance = new ManagementLocksApi(defaultClient);
    String lockName = "lockName_example"; // String | The name of the lock to get.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      ManagementLockObject result = apiInstance.managementLocksGetAtSubscriptionLevel(lockName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementLocksApi#managementLocksGetAtSubscriptionLevel");
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
| **lockName** | **String**| The name of the lock to get. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**ManagementLockObject**](ManagementLockObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the lock. |  -  |

<a id="managementLocksGetByScope"></a>
# **managementLocksGetByScope**
> ManagementLockObject managementLocksGetByScope(scope, lockName, apiVersion)



Get a management lock by scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementLocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementLocksApi apiInstance = new ManagementLocksApi(defaultClient);
    String scope = "scope_example"; // String | The scope for the lock. 
    String lockName = "lockName_example"; // String | The name of lock.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    try {
      ManagementLockObject result = apiInstance.managementLocksGetByScope(scope, lockName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementLocksApi#managementLocksGetByScope");
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
| **scope** | **String**| The scope for the lock.  | |
| **lockName** | **String**| The name of lock. | |
| **apiVersion** | **String**| The API version to use for the operation. | |

### Return type

[**ManagementLockObject**](ManagementLockObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="managementLocksListAtResourceGroupLevel"></a>
# **managementLocksListAtResourceGroupLevel**
> ManagementLockListResult managementLocksListAtResourceGroupLevel(resourceGroupName, apiVersion, subscriptionId, $filter)



Gets all the management locks for a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementLocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementLocksApi apiInstance = new ManagementLocksApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the locks to get.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    try {
      ManagementLockListResult result = apiInstance.managementLocksListAtResourceGroupLevel(resourceGroupName, apiVersion, subscriptionId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementLocksApi#managementLocksListAtResourceGroupLevel");
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
| **resourceGroupName** | **String**| The name of the resource group containing the locks to get. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |

### Return type

[**ManagementLockListResult**](ManagementLockListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of resource locks. |  -  |

<a id="managementLocksListAtResourceLevel"></a>
# **managementLocksListAtResourceLevel**
> ManagementLockListResult managementLocksListAtResourceLevel(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, $filter)



Gets all the management locks for a resource or any level below resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementLocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementLocksApi apiInstance = new ManagementLocksApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the locked resource. The name is case insensitive.
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
    String parentResourcePath = "parentResourcePath_example"; // String | The parent resource identity.
    String resourceType = "resourceType_example"; // String | The resource type of the locked resource.
    String resourceName = "resourceName_example"; // String | The name of the locked resource.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    try {
      ManagementLockListResult result = apiInstance.managementLocksListAtResourceLevel(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementLocksApi#managementLocksListAtResourceLevel");
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
| **resourceGroupName** | **String**| The name of the resource group containing the locked resource. The name is case insensitive. | |
| **resourceProviderNamespace** | **String**| The namespace of the resource provider. | |
| **parentResourcePath** | **String**| The parent resource identity. | |
| **resourceType** | **String**| The resource type of the locked resource. | |
| **resourceName** | **String**| The name of the locked resource. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |

### Return type

[**ManagementLockListResult**](ManagementLockListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of resource locks. |  -  |

<a id="managementLocksListAtSubscriptionLevel"></a>
# **managementLocksListAtSubscriptionLevel**
> ManagementLockListResult managementLocksListAtSubscriptionLevel(apiVersion, subscriptionId, $filter)



Gets all the management locks for a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementLocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementLocksApi apiInstance = new ManagementLocksApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    try {
      ManagementLockListResult result = apiInstance.managementLocksListAtSubscriptionLevel(apiVersion, subscriptionId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementLocksApi#managementLocksListAtSubscriptionLevel");
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
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |

### Return type

[**ManagementLockListResult**](ManagementLockListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of resource locks. |  -  |

<a id="managementLocksListByScope"></a>
# **managementLocksListByScope**
> ManagementLockListResult managementLocksListByScope(scope, apiVersion, $filter)



Gets all the management locks for a scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementLocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementLocksApi apiInstance = new ManagementLocksApi(defaultClient);
    String scope = "scope_example"; // String | The scope for the lock. When providing a scope for the assignment, use '/subscriptions/{subscriptionId}' for subscriptions, '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}' for resource groups, and '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePathIfPresent}/{resourceType}/{resourceName}' for resources.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    try {
      ManagementLockListResult result = apiInstance.managementLocksListByScope(scope, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementLocksApi#managementLocksListByScope");
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
| **scope** | **String**| The scope for the lock. When providing a scope for the assignment, use &#39;/subscriptions/{subscriptionId}&#39; for subscriptions, &#39;/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}&#39; for resource groups, and &#39;/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePathIfPresent}/{resourceType}/{resourceName}&#39; for resources. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |

### Return type

[**ManagementLockListResult**](ManagementLockListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of resource locks. |  -  |

