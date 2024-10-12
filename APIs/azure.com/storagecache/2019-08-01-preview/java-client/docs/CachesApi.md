# CachesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cachesCreate**](CachesApi.md#cachesCreate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName} |  |
| [**cachesDelete**](CachesApi.md#cachesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName} |  |
| [**cachesFlush**](CachesApi.md#cachesFlush) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/flush |  |
| [**cachesGet**](CachesApi.md#cachesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName} |  |
| [**cachesList**](CachesApi.md#cachesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.StorageCache/caches |  |
| [**cachesListByResourceGroup**](CachesApi.md#cachesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches |  |
| [**cachesStart**](CachesApi.md#cachesStart) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/start |  |
| [**cachesStop**](CachesApi.md#cachesStop) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/stop |  |
| [**cachesUpdate**](CachesApi.md#cachesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName} |  |
| [**cachesUpgradeFirmware**](CachesApi.md#cachesUpgradeFirmware) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/upgrade |  |


<a id="cachesCreate"></a>
# **cachesCreate**
> Cache cachesCreate(resourceGroupName, apiVersion, subscriptionId, cacheName, cache)



Create/update a Cache instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CachesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CachesApi apiInstance = new CachesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String cacheName = "cacheName_example"; // String | Name of cache.
    Cache cache = new Cache(); // Cache | Object containing the user selectable properties of the new cache.  If read-only properties are included, they must match the existing values of those properties.
    try {
      Cache result = apiInstance.cachesCreate(resourceGroupName, apiVersion, subscriptionId, cacheName, cache);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CachesApi#cachesCreate");
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
| **resourceGroupName** | **String**| Target resource group. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **cacheName** | **String**| Name of cache. | |
| **cache** | [**Cache**](Cache.md)| Object containing the user selectable properties of the new cache.  If read-only properties are included, they must match the existing values of those properties. | [optional] |

### Return type

[**Cache**](Cache.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Cache created or already exists. |  -  |
| **201** | Cache creation has been initiated.  Poll the new Cache&#39;s provisioningState property to monitor creation progress. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="cachesDelete"></a>
# **cachesDelete**
> Object cachesDelete(resourceGroupName, cacheName, apiVersion, subscriptionId)



Schedules a Cache for deletion.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CachesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CachesApi apiInstance = new CachesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
    String cacheName = "cacheName_example"; // String | Name of cache.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      Object result = apiInstance.cachesDelete(resourceGroupName, cacheName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CachesApi#cachesDelete");
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
| **resourceGroupName** | **String**| Target resource group. | |
| **cacheName** | **String**| Name of cache. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Cache deleted. |  -  |
| **202** | Started the Cache&#39;s transition to Deleted state. |  -  |
| **204** | Cache deleted. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="cachesFlush"></a>
# **cachesFlush**
> Object cachesFlush(resourceGroupName, apiVersion, subscriptionId, cacheName)



Tells a cache to write all dirty data to the StorageTarget(s).  During the flush, clients will see errors returned until the flush is complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CachesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CachesApi apiInstance = new CachesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String cacheName = "cacheName_example"; // String | Name of cache.
    try {
      Object result = apiInstance.cachesFlush(resourceGroupName, apiVersion, subscriptionId, cacheName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CachesApi#cachesFlush");
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
| **resourceGroupName** | **String**| Target resource group. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **cacheName** | **String**| Name of cache. | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All cache data is clean. |  -  |
| **202** | Cache has started flushing. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="cachesGet"></a>
# **cachesGet**
> Cache cachesGet(resourceGroupName, cacheName, apiVersion, subscriptionId)



Returns a Cache.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CachesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CachesApi apiInstance = new CachesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
    String cacheName = "cacheName_example"; // String | Name of cache.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      Cache result = apiInstance.cachesGet(resourceGroupName, cacheName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CachesApi#cachesGet");
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
| **resourceGroupName** | **String**| Target resource group. | |
| **cacheName** | **String**| Name of cache. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**Cache**](Cache.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the Cache object corresponding to cacheId. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="cachesList"></a>
# **cachesList**
> CachesListResult cachesList(apiVersion, subscriptionId)



Returns all Caches the user has access to under a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CachesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CachesApi apiInstance = new CachesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      CachesListResult result = apiInstance.cachesList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CachesApi#cachesList");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**CachesListResult**](CachesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Cache objects.  Note that entity references might replace complete Cache objects, as described in http://docs.oasis-open.org/odata/odata-json-format/v4.01/cs01/odata-json-format-v4.01-cs01.html#sec_EntityReference |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="cachesListByResourceGroup"></a>
# **cachesListByResourceGroup**
> CachesListResult cachesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Returns all Caches the user has access to under a resource group and subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CachesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CachesApi apiInstance = new CachesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      CachesListResult result = apiInstance.cachesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CachesApi#cachesListByResourceGroup");
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
| **resourceGroupName** | **String**| Target resource group. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**CachesListResult**](CachesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Cache objects.  Note that entity references might replace complete Cache objects, as described in http://docs.oasis-open.org/odata/odata-json-format/v4.01/cs01/odata-json-format-v4.01-cs01.html#sec_EntityReference |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="cachesStart"></a>
# **cachesStart**
> Object cachesStart(resourceGroupName, apiVersion, subscriptionId, cacheName)



Tells a Stopped state cache to transition to Active state.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CachesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CachesApi apiInstance = new CachesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String cacheName = "cacheName_example"; // String | Name of cache.
    try {
      Object result = apiInstance.cachesStart(resourceGroupName, apiVersion, subscriptionId, cacheName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CachesApi#cachesStart");
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
| **resourceGroupName** | **String**| Target resource group. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **cacheName** | **String**| Name of cache. | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Cache is Active. |  -  |
| **202** | Cache has started the transition to Active. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="cachesStop"></a>
# **cachesStop**
> Object cachesStop(resourceGroupName, apiVersion, subscriptionId, cacheName)



Tells an Active cache to transition to Stopped state.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CachesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CachesApi apiInstance = new CachesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String cacheName = "cacheName_example"; // String | Name of cache.
    try {
      Object result = apiInstance.cachesStop(resourceGroupName, apiVersion, subscriptionId, cacheName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CachesApi#cachesStop");
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
| **resourceGroupName** | **String**| Target resource group. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **cacheName** | **String**| Name of cache. | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Cache is stopped. |  -  |
| **202** | Cache has started the transition to Stopped. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="cachesUpdate"></a>
# **cachesUpdate**
> Cache cachesUpdate(resourceGroupName, apiVersion, subscriptionId, cacheName, cache)



Update a Cache instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CachesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CachesApi apiInstance = new CachesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String cacheName = "cacheName_example"; // String | Name of cache.
    Cache cache = new Cache(); // Cache | Object containing the user selectable properties of the new cache.  If read-only properties are included, they must match the existing values of those properties.
    try {
      Cache result = apiInstance.cachesUpdate(resourceGroupName, apiVersion, subscriptionId, cacheName, cache);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CachesApi#cachesUpdate");
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
| **resourceGroupName** | **String**| Target resource group. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **cacheName** | **String**| Name of cache. | |
| **cache** | [**Cache**](Cache.md)| Object containing the user selectable properties of the new cache.  If read-only properties are included, they must match the existing values of those properties. | [optional] |

### Return type

[**Cache**](Cache.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Patched the Cache. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="cachesUpgradeFirmware"></a>
# **cachesUpgradeFirmware**
> Object cachesUpgradeFirmware(resourceGroupName, apiVersion, subscriptionId, cacheName)



Tells a cache to upgrade its firmware.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CachesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CachesApi apiInstance = new CachesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String cacheName = "cacheName_example"; // String | Name of cache.
    try {
      Object result = apiInstance.cachesUpgradeFirmware(resourceGroupName, apiVersion, subscriptionId, cacheName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CachesApi#cachesUpgradeFirmware");
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
| **resourceGroupName** | **String**| Target resource group. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **cacheName** | **String**| Name of cache. | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Cache firmware is up to date. |  -  |
| **202** | Cache has started the upgrade. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

