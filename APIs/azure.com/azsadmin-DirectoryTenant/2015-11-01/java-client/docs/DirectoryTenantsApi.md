# DirectoryTenantsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**directoryTenantsCreateOrUpdate**](DirectoryTenantsApi.md#directoryTenantsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Subscriptions.Admin/directoryTenants/{tenant} |  |
| [**directoryTenantsDelete**](DirectoryTenantsApi.md#directoryTenantsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Subscriptions.Admin/directoryTenants/{tenant} |  |
| [**directoryTenantsGet**](DirectoryTenantsApi.md#directoryTenantsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Subscriptions.Admin/directoryTenants/{tenant} |  |
| [**directoryTenantsList**](DirectoryTenantsApi.md#directoryTenantsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Subscriptions.Admin/directoryTenants |  |


<a id="directoryTenantsCreateOrUpdate"></a>
# **directoryTenantsCreateOrUpdate**
> DirectoryTenant directoryTenantsCreateOrUpdate(subscriptionId, resourceGroupName, tenant, apiVersion, newTenant)



Create or updates a directory tenant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoryTenantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DirectoryTenantsApi apiInstance = new DirectoryTenantsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group the resource is located under.
    String tenant = "tenant_example"; // String | Directory tenant name.
    String apiVersion = "2015-11-01"; // String | Client Api Version.
    DirectoryTenant newTenant = new DirectoryTenant(); // DirectoryTenant | New directory tenant properties.
    try {
      DirectoryTenant result = apiInstance.directoryTenantsCreateOrUpdate(subscriptionId, resourceGroupName, tenant, apiVersion, newTenant);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoryTenantsApi#directoryTenantsCreateOrUpdate");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The resource group the resource is located under. | |
| **tenant** | **String**| Directory tenant name. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2015-11-01] |
| **newTenant** | [**DirectoryTenant**](DirectoryTenant.md)| New directory tenant properties. | |

### Return type

[**DirectoryTenant**](DirectoryTenant.md)

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

<a id="directoryTenantsDelete"></a>
# **directoryTenantsDelete**
> directoryTenantsDelete(subscriptionId, resourceGroupName, tenant, apiVersion)



Delete a directory tenant under a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoryTenantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DirectoryTenantsApi apiInstance = new DirectoryTenantsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group the resource is located under.
    String tenant = "tenant_example"; // String | Directory tenant name.
    String apiVersion = "2015-11-01"; // String | Client Api Version.
    try {
      apiInstance.directoryTenantsDelete(subscriptionId, resourceGroupName, tenant, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoryTenantsApi#directoryTenantsDelete");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The resource group the resource is located under. | |
| **tenant** | **String**| Directory tenant name. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2015-11-01] |

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
| **204** | No Content |  -  |

<a id="directoryTenantsGet"></a>
# **directoryTenantsGet**
> DirectoryTenant directoryTenantsGet(subscriptionId, resourceGroupName, tenant, apiVersion)



Get a directory tenant by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoryTenantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DirectoryTenantsApi apiInstance = new DirectoryTenantsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group the resource is located under.
    String tenant = "tenant_example"; // String | Directory tenant name.
    String apiVersion = "2015-11-01"; // String | Client Api Version.
    try {
      DirectoryTenant result = apiInstance.directoryTenantsGet(subscriptionId, resourceGroupName, tenant, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoryTenantsApi#directoryTenantsGet");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The resource group the resource is located under. | |
| **tenant** | **String**| Directory tenant name. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2015-11-01] |

### Return type

[**DirectoryTenant**](DirectoryTenant.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="directoryTenantsList"></a>
# **directoryTenantsList**
> DirectoryTenantList directoryTenantsList(subscriptionId, resourceGroupName, apiVersion)



Lists all the directory tenants under the current subscription and given resource group name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoryTenantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DirectoryTenantsApi apiInstance = new DirectoryTenantsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group the resource is located under.
    String apiVersion = "2015-11-01"; // String | Client Api Version.
    try {
      DirectoryTenantList result = apiInstance.directoryTenantsList(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoryTenantsApi#directoryTenantsList");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The resource group the resource is located under. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2015-11-01] |

### Return type

[**DirectoryTenantList**](DirectoryTenantList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

