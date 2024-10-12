# ManagementLocksApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**managementLocksCreateOrUpdateAtResourceGroupLevel**](ManagementLocksApi.md#managementLocksCreateOrUpdateAtResourceGroupLevel) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/locks/{lockName} |  |
| [**managementLocksCreateOrUpdateAtResourceLevel**](ManagementLocksApi.md#managementLocksCreateOrUpdateAtResourceLevel) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/locks/{lockName} |  |
| [**managementLocksCreateOrUpdateAtSubscriptionLevel**](ManagementLocksApi.md#managementLocksCreateOrUpdateAtSubscriptionLevel) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/locks/{lockName} |  |
| [**managementLocksDeleteAtResourceGroupLevel**](ManagementLocksApi.md#managementLocksDeleteAtResourceGroupLevel) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/locks/{lockName} |  |
| [**managementLocksDeleteAtResourceLevel**](ManagementLocksApi.md#managementLocksDeleteAtResourceLevel) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/locks/{lockName} |  |
| [**managementLocksDeleteAtSubscriptionLevel**](ManagementLocksApi.md#managementLocksDeleteAtSubscriptionLevel) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/locks/{lockName} |  |
| [**managementLocksGet**](ManagementLocksApi.md#managementLocksGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/locks/{lockName} |  |
| [**managementLocksGetAtResourceGroupLevel**](ManagementLocksApi.md#managementLocksGetAtResourceGroupLevel) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/locks/{lockName} |  |
| [**managementLocksListAtResourceGroupLevel**](ManagementLocksApi.md#managementLocksListAtResourceGroupLevel) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/locks |  |
| [**managementLocksListAtResourceLevel**](ManagementLocksApi.md#managementLocksListAtResourceLevel) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/locks |  |
| [**managementLocksListAtSubscriptionLevel**](ManagementLocksApi.md#managementLocksListAtSubscriptionLevel) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/locks |  |


<a id="managementLocksCreateOrUpdateAtResourceGroupLevel"></a>
# **managementLocksCreateOrUpdateAtResourceGroupLevel**
> ManagementLockObject managementLocksCreateOrUpdateAtResourceGroupLevel(resourceGroupName, lockName, apiVersion, subscriptionId, parameters)



Create or update a management lock at the resource group level.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String lockName = "lockName_example"; // String | The lock name.
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
| **resourceGroupName** | **String**| The resource group name. | |
| **lockName** | **String**| The lock name. | |
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
| **200** | OK |  -  |
| **201** | Created |  -  |

<a id="managementLocksCreateOrUpdateAtResourceLevel"></a>
# **managementLocksCreateOrUpdateAtResourceLevel**
> ManagementLockObject managementLocksCreateOrUpdateAtResourceLevel(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, lockName, apiVersion, subscriptionId, parameters)



Create or update a management lock at the resource level or any level below resource.

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
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | Resource identity.
    String parentResourcePath = "parentResourcePath_example"; // String | Resource identity.
    String resourceType = "resourceType_example"; // String | Resource identity.
    String resourceName = "resourceName_example"; // String | Resource identity.
    String lockName = "lockName_example"; // String | The name of lock.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    ManagementLockObject parameters = new ManagementLockObject(); // ManagementLockObject | Create or update management lock parameters.
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
| **resourceGroupName** | **String**| The name of the resource group.  | |
| **resourceProviderNamespace** | **String**| Resource identity. | |
| **parentResourcePath** | **String**| Resource identity. | |
| **resourceType** | **String**| Resource identity. | |
| **resourceName** | **String**| Resource identity. | |
| **lockName** | **String**| The name of lock. | |
| **apiVersion** | **String**| The API version to use for the operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
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

<a id="managementLocksCreateOrUpdateAtSubscriptionLevel"></a>
# **managementLocksCreateOrUpdateAtSubscriptionLevel**
> ManagementLockObject managementLocksCreateOrUpdateAtSubscriptionLevel(lockName, apiVersion, subscriptionId, parameters)



Create or update a management lock at the subscription level.

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
    String lockName = "lockName_example"; // String | The name of lock.
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
| **lockName** | **String**| The name of lock. | |
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
| **200** | OK |  -  |
| **201** | Created |  -  |

<a id="managementLocksDeleteAtResourceGroupLevel"></a>
# **managementLocksDeleteAtResourceGroupLevel**
> managementLocksDeleteAtResourceGroupLevel(resourceGroupName, lockName, apiVersion, subscriptionId)



Deletes the management lock of a resource group.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String lockName = "lockName_example"; // String | The name of lock.
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
| **resourceGroupName** | **String**| The resource group name. | |
| **lockName** | **String**| The name of lock. | |
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



Deletes the management lock of a resource or any level below resource.

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
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | Resource identity.
    String parentResourcePath = "parentResourcePath_example"; // String | Resource identity.
    String resourceType = "resourceType_example"; // String | Resource identity.
    String resourceName = "resourceName_example"; // String | Resource identity.
    String lockName = "lockName_example"; // String | The name of lock.
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
| **resourceGroupName** | **String**| The name of the resource group.  | |
| **resourceProviderNamespace** | **String**| Resource identity. | |
| **parentResourcePath** | **String**| Resource identity. | |
| **resourceType** | **String**| Resource identity. | |
| **resourceName** | **String**| Resource identity. | |
| **lockName** | **String**| The name of lock. | |
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



Deletes the management lock of a subscription.

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
    String lockName = "lockName_example"; // String | The name of lock.
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
| **lockName** | **String**| The name of lock. | |
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

<a id="managementLocksGet"></a>
# **managementLocksGet**
> ManagementLockObject managementLocksGet(lockName, apiVersion, subscriptionId)



Gets the management lock of a scope.

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
    String lockName = "lockName_example"; // String | Name of the management lock.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      ManagementLockObject result = apiInstance.managementLocksGet(lockName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementLocksApi#managementLocksGet");
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
| **lockName** | **String**| Name of the management lock. | |
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
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String lockName = "lockName_example"; // String | The lock name.
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
| **resourceGroupName** | **String**| The resource group name. | |
| **lockName** | **String**| The lock name. | |
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

<a id="managementLocksListAtResourceGroupLevel"></a>
# **managementLocksListAtResourceGroupLevel**
> ManagementLockListResult managementLocksListAtResourceGroupLevel(resourceGroupName, apiVersion, subscriptionId, $filter)



Gets all the management locks of a resource group.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
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
| **resourceGroupName** | **String**| Resource group name. | |
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
| **200** | OK |  -  |

<a id="managementLocksListAtResourceLevel"></a>
# **managementLocksListAtResourceLevel**
> ManagementLockListResult managementLocksListAtResourceLevel(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, $filter)



Gets all the management locks of a resource or any level below resource.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | Resource identity.
    String parentResourcePath = "parentResourcePath_example"; // String | Resource identity.
    String resourceType = "resourceType_example"; // String | Resource identity.
    String resourceName = "resourceName_example"; // String | Resource identity.
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **resourceProviderNamespace** | **String**| Resource identity. | |
| **parentResourcePath** | **String**| Resource identity. | |
| **resourceType** | **String**| Resource identity. | |
| **resourceName** | **String**| Resource identity. | |
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
| **200** | OK |  -  |

<a id="managementLocksListAtSubscriptionLevel"></a>
# **managementLocksListAtSubscriptionLevel**
> ManagementLockListResult managementLocksListAtSubscriptionLevel(apiVersion, subscriptionId, $filter)



Gets all the management locks of a subscription.

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
| **200** | OK |  -  |

