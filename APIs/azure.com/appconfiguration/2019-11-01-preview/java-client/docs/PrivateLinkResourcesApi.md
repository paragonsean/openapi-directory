# PrivateLinkResourcesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**privateLinkResourcesGet**](PrivateLinkResourcesApi.md#privateLinkResourcesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/privateLinkResources/{groupName} |  |
| [**privateLinkResourcesListByConfigurationStore**](PrivateLinkResourcesApi.md#privateLinkResourcesListByConfigurationStore) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/privateLinkResources |  |


<a id="privateLinkResourcesGet"></a>
# **privateLinkResourcesGet**
> PrivateLinkResource privateLinkResourcesGet(subscriptionId, resourceGroupName, configStoreName, apiVersion, groupName)



Gets a private link resource that need to be created for a configuration store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateLinkResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateLinkResourcesApi apiInstance = new PrivateLinkResourcesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String configStoreName = "configStoreName_example"; // String | The name of the configuration store.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String groupName = "groupName_example"; // String | The name of the private link resource group.
    try {
      PrivateLinkResource result = apiInstance.privateLinkResourcesGet(subscriptionId, resourceGroupName, configStoreName, apiVersion, groupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateLinkResourcesApi#privateLinkResourcesGet");
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
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **configStoreName** | **String**| The name of the configuration store. | |
| **apiVersion** | **String**| The client API version. | |
| **groupName** | **String**| The name of the private link resource group. | |

### Return type

[**PrivateLinkResource**](PrivateLinkResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="privateLinkResourcesListByConfigurationStore"></a>
# **privateLinkResourcesListByConfigurationStore**
> PrivateLinkResourceListResult privateLinkResourcesListByConfigurationStore(subscriptionId, resourceGroupName, configStoreName, apiVersion)



Gets the private link resources that need to be created for a configuration store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateLinkResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateLinkResourcesApi apiInstance = new PrivateLinkResourcesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String configStoreName = "configStoreName_example"; // String | The name of the configuration store.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      PrivateLinkResourceListResult result = apiInstance.privateLinkResourcesListByConfigurationStore(subscriptionId, resourceGroupName, configStoreName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateLinkResourcesApi#privateLinkResourcesListByConfigurationStore");
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
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **configStoreName** | **String**| The name of the configuration store. | |
| **apiVersion** | **String**| The client API version. | |

### Return type

[**PrivateLinkResourceListResult**](PrivateLinkResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed |  -  |

