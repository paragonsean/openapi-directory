# ResourcePoolsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resourcePoolsGet**](ResourcePoolsApi.md#resourcePoolsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/privateClouds/{pcName}/resourcePools/{resourcePoolName} | Implements get of resource pool |
| [**resourcePoolsList**](ResourcePoolsApi.md#resourcePoolsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/privateClouds/{pcName}/resourcePools | Implements get of resource pools list |


<a id="resourcePoolsGet"></a>
# **resourcePoolsGet**
> ResourcePool resourcePoolsGet(subscriptionId, apiVersion, regionId, pcName, resourcePoolName)

Implements get of resource pool

Returns resource pool templates by its name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcePoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourcePoolsApi apiInstance = new ResourcePoolsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String regionId = "regionId_example"; // String | The region Id (westus, eastus)
    String pcName = "pcName_example"; // String | The private cloud name
    String resourcePoolName = "resourcePoolName_example"; // String | resource pool id (vsphereId)
    try {
      ResourcePool result = apiInstance.resourcePoolsGet(subscriptionId, apiVersion, regionId, pcName, resourcePoolName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcePoolsApi#resourcePoolsGet");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **apiVersion** | **String**| Client API version. | |
| **regionId** | **String**| The region Id (westus, eastus) | |
| **pcName** | **String**| The private cloud name | |
| **resourcePoolName** | **String**| resource pool id (vsphereId) | |

### Return type

[**ResourcePool**](ResourcePool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | General Error |  -  |

<a id="resourcePoolsList"></a>
# **resourcePoolsList**
> ResourcePoolsListResponse resourcePoolsList(subscriptionId, regionId, pcName, apiVersion)

Implements get of resource pools list

Returns list of resource pools in region for private cloud

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcePoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourcePoolsApi apiInstance = new ResourcePoolsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String regionId = "regionId_example"; // String | The region Id (westus, eastus)
    String pcName = "pcName_example"; // String | The private cloud name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      ResourcePoolsListResponse result = apiInstance.resourcePoolsList(subscriptionId, regionId, pcName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcePoolsApi#resourcePoolsList");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **regionId** | **String**| The region Id (westus, eastus) | |
| **pcName** | **String**| The private cloud name | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**ResourcePoolsListResponse**](ResourcePoolsListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | General Error |  -  |

