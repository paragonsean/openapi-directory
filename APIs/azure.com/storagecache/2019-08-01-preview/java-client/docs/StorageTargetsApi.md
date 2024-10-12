# StorageTargetsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storageTargetsCreate**](StorageTargetsApi.md#storageTargetsCreate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets/{storageTargetName} |  |
| [**storageTargetsDelete**](StorageTargetsApi.md#storageTargetsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets/{storageTargetName} |  |
| [**storageTargetsGet**](StorageTargetsApi.md#storageTargetsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets/{storageTargetName} |  |
| [**storageTargetsListByCache**](StorageTargetsApi.md#storageTargetsListByCache) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets |  |
| [**storageTargetsUpdate**](StorageTargetsApi.md#storageTargetsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets/{storageTargetName} |  |


<a id="storageTargetsCreate"></a>
# **storageTargetsCreate**
> StorageTarget storageTargetsCreate(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName, storagetarget)



Create/update a storage target.  This operation is allowed at any time, but if the cache is down or unhealthy, the actual creation/modification of the storage target may be delayed until the cache is healthy again.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageTargetsApi apiInstance = new StorageTargetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String cacheName = "cacheName_example"; // String | Name of cache.
    String storageTargetName = "storageTargetName_example"; // String | Name of storage target.
    StorageTarget storagetarget = new StorageTarget(); // StorageTarget | Object containing the definition of a storage target.
    try {
      StorageTarget result = apiInstance.storageTargetsCreate(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName, storagetarget);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageTargetsApi#storageTargetsCreate");
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
| **storageTargetName** | **String**| Name of storage target. | |
| **storagetarget** | [**StorageTarget**](StorageTarget.md)| Object containing the definition of a storage target. | [optional] |

### Return type

[**StorageTarget**](StorageTarget.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Storage Target has been created. |  -  |
| **201** | Storage Target creation has been initiated.  Poll the new Storage Target&#39;s provisioningState property to monitor creation progress. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="storageTargetsDelete"></a>
# **storageTargetsDelete**
> Object storageTargetsDelete(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName)



Removes a storage target from a cache.  This operation is allowed at any time, but if the cache is down or unhealthy, the actual removal of the storage target may be delayed until the cache is healthy again.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageTargetsApi apiInstance = new StorageTargetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String cacheName = "cacheName_example"; // String | Name of cache.
    String storageTargetName = "storageTargetName_example"; // String | Name of storage target.
    try {
      Object result = apiInstance.storageTargetsDelete(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageTargetsApi#storageTargetsDelete");
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
| **storageTargetName** | **String**| Name of storage target. | |

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
| **200** | Storage target deleted. |  -  |
| **202** | Started the storage target&#39;s deletion. |  -  |
| **204** | Storage target deleted. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="storageTargetsGet"></a>
# **storageTargetsGet**
> StorageTarget storageTargetsGet(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName)



Returns a storage target from a cache.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageTargetsApi apiInstance = new StorageTargetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String cacheName = "cacheName_example"; // String | Name of cache.
    String storageTargetName = "storageTargetName_example"; // String | Name of storage target.
    try {
      StorageTarget result = apiInstance.storageTargetsGet(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageTargetsApi#storageTargetsGet");
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
| **storageTargetName** | **String**| Name of storage target. | |

### Return type

[**StorageTarget**](StorageTarget.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the Storage Target object corresponding to storageTargetName. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="storageTargetsListByCache"></a>
# **storageTargetsListByCache**
> StorageTargetsResult storageTargetsListByCache(resourceGroupName, apiVersion, subscriptionId, cacheName)



Returns the StorageTargets for this cache in the subscription and resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageTargetsApi apiInstance = new StorageTargetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String cacheName = "cacheName_example"; // String | Name of cache.
    try {
      StorageTargetsResult result = apiInstance.storageTargetsListByCache(resourceGroupName, apiVersion, subscriptionId, cacheName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageTargetsApi#storageTargetsListByCache");
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

[**StorageTargetsResult**](StorageTargetsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the list of storage targets defined by cacheId. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="storageTargetsUpdate"></a>
# **storageTargetsUpdate**
> StorageTarget storageTargetsUpdate(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName, storagetarget)



Update a storage target.  This operation is allowed at any time, but if the cache is down or unhealthy, the actual creation/modification of the storage target may be delayed until the cache is healthy again.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageTargetsApi apiInstance = new StorageTargetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String cacheName = "cacheName_example"; // String | Name of cache.
    String storageTargetName = "storageTargetName_example"; // String | Name of storage target.
    StorageTarget storagetarget = new StorageTarget(); // StorageTarget | Object containing the definition of a storage target.
    try {
      StorageTarget result = apiInstance.storageTargetsUpdate(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName, storagetarget);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageTargetsApi#storageTargetsUpdate");
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
| **storageTargetName** | **String**| Name of storage target. | |
| **storagetarget** | [**StorageTarget**](StorageTarget.md)| Object containing the definition of a storage target. | [optional] |

### Return type

[**StorageTarget**](StorageTarget.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Storage Target has been patched. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

