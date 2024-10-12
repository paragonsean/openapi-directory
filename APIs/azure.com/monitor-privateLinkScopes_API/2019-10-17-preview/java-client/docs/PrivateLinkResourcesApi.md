# PrivateLinkResourcesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**privateLinkResourcesGet**](PrivateLinkResourcesApi.md#privateLinkResourcesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/privateLinkScopes/{scopeName}/privateLinkResources/{groupName} |  |
| [**privateLinkResourcesListByPrivateLinkScope**](PrivateLinkResourcesApi.md#privateLinkResourcesListByPrivateLinkScope) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/privateLinkScopes/{scopeName}/privateLinkResources |  |


<a id="privateLinkResourcesGet"></a>
# **privateLinkResourcesGet**
> PrivateLinkResource privateLinkResourcesGet(subscriptionId, resourceGroupName, apiVersion, scopeName, groupName)



Gets the private link resources that need to be created for a Azure Monitor PrivateLinkScope.

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
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String scopeName = "scopeName_example"; // String | Name of the Azure Monitor PrivateLinkScope that will contain the datasource
    String groupName = "groupName_example"; // String | The name of the private link resource.
    try {
      PrivateLinkResource result = apiInstance.privateLinkResourcesGet(subscriptionId, resourceGroupName, apiVersion, scopeName, groupName);
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **scopeName** | **String**| Name of the Azure Monitor PrivateLinkScope that will contain the datasource | |
| **groupName** | **String**| The name of the private link resource. | |

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
| **200** | Successfully retrieved a specified private link resource. |  -  |

<a id="privateLinkResourcesListByPrivateLinkScope"></a>
# **privateLinkResourcesListByPrivateLinkScope**
> PrivateLinkResourceListResult privateLinkResourcesListByPrivateLinkScope(subscriptionId, resourceGroupName, apiVersion, scopeName)



Gets the private link resources that need to be created for a Azure Monitor PrivateLinkScope.

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
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String scopeName = "scopeName_example"; // String | Name of the Azure Monitor PrivateLinkScope that will contain the datasource
    try {
      PrivateLinkResourceListResult result = apiInstance.privateLinkResourcesListByPrivateLinkScope(subscriptionId, resourceGroupName, apiVersion, scopeName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateLinkResourcesApi#privateLinkResourcesListByPrivateLinkScope");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **scopeName** | **String**| Name of the Azure Monitor PrivateLinkScope that will contain the datasource | |

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
| **200** | Successfully retrieved private link resources. |  -  |

