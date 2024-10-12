# StoragePoolsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storagePoolsGet**](StoragePoolsApi.md#storagePoolsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/storageSubSystems/{storageSubSystem}/storagePools/{storagePool} |  |
| [**storagePoolsList**](StoragePoolsApi.md#storagePoolsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/storageSubSystems/{storageSubSystem}/storagePools |  |


<a id="storagePoolsGet"></a>
# **storagePoolsGet**
> StoragePool storagePoolsGet(subscriptionId, resourceGroupName, location, storageSubSystem, storagePool, apiVersion)



Return the requested a storage pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoragePoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StoragePoolsApi apiInstance = new StoragePoolsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String location = "location_example"; // String | Location of the resource.
    String storageSubSystem = "storageSubSystem_example"; // String | Name of the storage system.
    String storagePool = "storagePool_example"; // String | Storage pool name.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    try {
      StoragePool result = apiInstance.storagePoolsGet(subscriptionId, resourceGroupName, location, storageSubSystem, storagePool, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoragePoolsApi#storagePoolsGet");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group. | |
| **location** | **String**| Location of the resource. | |
| **storageSubSystem** | **String**| Name of the storage system. | |
| **storagePool** | **String**| Storage pool name. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |

### Return type

[**StoragePool**](StoragePool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | NOT FOUND |  -  |

<a id="storagePoolsList"></a>
# **storagePoolsList**
> StoragePoolList storagePoolsList(subscriptionId, resourceGroupName, location, storageSubSystem, apiVersion, $filter)



Returns a list of all storage pools for a location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoragePoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StoragePoolsApi apiInstance = new StoragePoolsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String location = "location_example"; // String | Location of the resource.
    String storageSubSystem = "storageSubSystem_example"; // String | Name of the storage system.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    String $filter = "$filter_example"; // String | OData filter parameter.
    try {
      StoragePoolList result = apiInstance.storagePoolsList(subscriptionId, resourceGroupName, location, storageSubSystem, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoragePoolsApi#storagePoolsList");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group. | |
| **location** | **String**| Location of the resource. | |
| **storageSubSystem** | **String**| Name of the storage system. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |
| **$filter** | **String**| OData filter parameter. | [optional] |

### Return type

[**StoragePoolList**](StoragePoolList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | NOT FOUND |  -  |

