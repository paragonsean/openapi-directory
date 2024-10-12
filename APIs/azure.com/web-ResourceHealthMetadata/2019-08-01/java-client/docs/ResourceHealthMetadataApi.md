# ResourceHealthMetadataApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resourceHealthMetadataGetBySite**](ResourceHealthMetadataApi.md#resourceHealthMetadataGetBySite) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/resourceHealthMetadata/default | Gets the category of ResourceHealthMetadata to use for the given site |
| [**resourceHealthMetadataGetBySiteSlot**](ResourceHealthMetadataApi.md#resourceHealthMetadataGetBySiteSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/resourceHealthMetadata/default | Gets the category of ResourceHealthMetadata to use for the given site |
| [**resourceHealthMetadataList**](ResourceHealthMetadataApi.md#resourceHealthMetadataList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/resourceHealthMetadata | List all ResourceHealthMetadata for all sites in the subscription. |
| [**resourceHealthMetadataListByResourceGroup**](ResourceHealthMetadataApi.md#resourceHealthMetadataListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/resourceHealthMetadata | List all ResourceHealthMetadata for all sites in the resource group in the subscription. |
| [**resourceHealthMetadataListBySite**](ResourceHealthMetadataApi.md#resourceHealthMetadataListBySite) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/resourceHealthMetadata | Gets the category of ResourceHealthMetadata to use for the given site as a collection |
| [**resourceHealthMetadataListBySiteSlot**](ResourceHealthMetadataApi.md#resourceHealthMetadataListBySiteSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/resourceHealthMetadata | Gets the category of ResourceHealthMetadata to use for the given site as a collection |


<a id="resourceHealthMetadataGetBySite"></a>
# **resourceHealthMetadataGetBySite**
> ResourceHealthMetadata resourceHealthMetadataGetBySite(resourceGroupName, name, subscriptionId, apiVersion)

Gets the category of ResourceHealthMetadata to use for the given site

Description for Gets the category of ResourceHealthMetadata to use for the given site

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceHealthMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceHealthMetadataApi apiInstance = new ResourceHealthMetadataApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of web app
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ResourceHealthMetadata result = apiInstance.resourceHealthMetadataGetBySite(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceHealthMetadataApi#resourceHealthMetadataGetBySite");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of web app | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ResourceHealthMetadata**](ResourceHealthMetadata.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="resourceHealthMetadataGetBySiteSlot"></a>
# **resourceHealthMetadataGetBySiteSlot**
> ResourceHealthMetadata resourceHealthMetadataGetBySiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the category of ResourceHealthMetadata to use for the given site

Description for Gets the category of ResourceHealthMetadata to use for the given site

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceHealthMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceHealthMetadataApi apiInstance = new ResourceHealthMetadataApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of web app
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ResourceHealthMetadata result = apiInstance.resourceHealthMetadataGetBySiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceHealthMetadataApi#resourceHealthMetadataGetBySiteSlot");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of web app | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ResourceHealthMetadata**](ResourceHealthMetadata.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="resourceHealthMetadataList"></a>
# **resourceHealthMetadataList**
> ResourceHealthMetadataCollection resourceHealthMetadataList(subscriptionId, apiVersion)

List all ResourceHealthMetadata for all sites in the subscription.

Description for List all ResourceHealthMetadata for all sites in the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceHealthMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceHealthMetadataApi apiInstance = new ResourceHealthMetadataApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ResourceHealthMetadataCollection result = apiInstance.resourceHealthMetadataList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceHealthMetadataApi#resourceHealthMetadataList");
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
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ResourceHealthMetadataCollection**](ResourceHealthMetadataCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="resourceHealthMetadataListByResourceGroup"></a>
# **resourceHealthMetadataListByResourceGroup**
> ResourceHealthMetadataCollection resourceHealthMetadataListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)

List all ResourceHealthMetadata for all sites in the resource group in the subscription.

Description for List all ResourceHealthMetadata for all sites in the resource group in the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceHealthMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceHealthMetadataApi apiInstance = new ResourceHealthMetadataApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ResourceHealthMetadataCollection result = apiInstance.resourceHealthMetadataListByResourceGroup(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceHealthMetadataApi#resourceHealthMetadataListByResourceGroup");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ResourceHealthMetadataCollection**](ResourceHealthMetadataCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="resourceHealthMetadataListBySite"></a>
# **resourceHealthMetadataListBySite**
> ResourceHealthMetadataCollection resourceHealthMetadataListBySite(resourceGroupName, name, subscriptionId, apiVersion)

Gets the category of ResourceHealthMetadata to use for the given site as a collection

Description for Gets the category of ResourceHealthMetadata to use for the given site as a collection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceHealthMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceHealthMetadataApi apiInstance = new ResourceHealthMetadataApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of web app.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ResourceHealthMetadataCollection result = apiInstance.resourceHealthMetadataListBySite(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceHealthMetadataApi#resourceHealthMetadataListBySite");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of web app. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ResourceHealthMetadataCollection**](ResourceHealthMetadataCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="resourceHealthMetadataListBySiteSlot"></a>
# **resourceHealthMetadataListBySiteSlot**
> ResourceHealthMetadataCollection resourceHealthMetadataListBySiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the category of ResourceHealthMetadata to use for the given site as a collection

Description for Gets the category of ResourceHealthMetadata to use for the given site as a collection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceHealthMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceHealthMetadataApi apiInstance = new ResourceHealthMetadataApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of web app.
    String slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ResourceHealthMetadataCollection result = apiInstance.resourceHealthMetadataListBySiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceHealthMetadataApi#resourceHealthMetadataListBySiteSlot");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of web app. | |
| **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ResourceHealthMetadataCollection**](ResourceHealthMetadataCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

