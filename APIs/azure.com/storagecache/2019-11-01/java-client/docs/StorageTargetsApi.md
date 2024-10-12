# StorageTargetsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storageTargetsCreateOrUpdate**](StorageTargetsApi.md#storageTargetsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets/{storageTargetName} |  |
| [**storageTargetsDelete**](StorageTargetsApi.md#storageTargetsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets/{storageTargetName} |  |
| [**storageTargetsGet**](StorageTargetsApi.md#storageTargetsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets/{storageTargetName} |  |
| [**storageTargetsListByCache**](StorageTargetsApi.md#storageTargetsListByCache) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets |  |


<a id="storageTargetsCreateOrUpdate"></a>
# **storageTargetsCreateOrUpdate**
> StorageTarget storageTargetsCreateOrUpdate(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName, storagetarget)



Create or update a Storage Target. This operation is allowed at any time, but if the Cache is down or unhealthy, the actual creation/modification of the Storage Target may be delayed until the Cache is healthy again.

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
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String cacheName = "cacheName_example"; // String | Name of Cache.
    String storageTargetName = "storageTargetName_example"; // String | Name of the Storage Target.
    StorageTarget storagetarget = new StorageTarget(); // StorageTarget | Object containing the definition of a Storage Target.
    try {
      StorageTarget result = apiInstance.storageTargetsCreateOrUpdate(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName, storagetarget);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageTargetsApi#storageTargetsCreateOrUpdate");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **cacheName** | **String**| Name of Cache. | |
| **storageTargetName** | **String**| Name of the Storage Target. | |
| **storagetarget** | [**StorageTarget**](StorageTarget.md)| Object containing the definition of a Storage Target. | [optional] |

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
| **200** | Storage Target has been created or updated. |  -  |
| **201** | Storage Target creation or update has been initiated. Poll the new Storage Target&#39;s provisioningState property to monitor creation progress. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="storageTargetsDelete"></a>
# **storageTargetsDelete**
> Object storageTargetsDelete(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName)



Removes a Storage Target from a Cache. This operation is allowed at any time, but if the Cache is down or unhealthy, the actual removal of the Storage Target may be delayed until the Cache is healthy again. Note that if the Cache has data to flush to the Storage Target, the data will be flushed before the Storage Target will be deleted.

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
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String cacheName = "cacheName_example"; // String | Name of Cache.
    String storageTargetName = "storageTargetName_example"; // String | Name of Storage Target.
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **cacheName** | **String**| Name of Cache. | |
| **storageTargetName** | **String**| Name of Storage Target. | |

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
| **202** | Started the Storage Target&#39;s deletion. Poll the Cache&#39;s Storage Targets to monitor. |  -  |
| **204** | Storage Target deleted. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="storageTargetsGet"></a>
# **storageTargetsGet**
> StorageTarget storageTargetsGet(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName)



Returns a Storage Target from a Cache.

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
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String cacheName = "cacheName_example"; // String | Name of Cache.
    String storageTargetName = "storageTargetName_example"; // String | Name of the Storage Target.
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **cacheName** | **String**| Name of Cache. | |
| **storageTargetName** | **String**| Name of the Storage Target. | |

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



Returns a list of Storage Targets for the specified Cache.

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
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String cacheName = "cacheName_example"; // String | Name of Cache.
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **cacheName** | **String**| Name of Cache. | |

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
| **200** | Returns the list of Storage Targets defined by cacheName. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

