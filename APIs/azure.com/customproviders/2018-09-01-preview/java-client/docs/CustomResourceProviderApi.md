# CustomResourceProviderApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customResourceProviderCreateOrUpdate**](CustomResourceProviderApi.md#customResourceProviderCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName} |  |
| [**customResourceProviderDelete**](CustomResourceProviderApi.md#customResourceProviderDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName} |  |
| [**customResourceProviderGet**](CustomResourceProviderApi.md#customResourceProviderGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName} |  |
| [**customResourceProviderListByResourceGroup**](CustomResourceProviderApi.md#customResourceProviderListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders |  |
| [**customResourceProviderListBySubscription**](CustomResourceProviderApi.md#customResourceProviderListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CustomProviders/resourceProviders |  |
| [**customResourceProviderUpdate**](CustomResourceProviderApi.md#customResourceProviderUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName} |  |


<a id="customResourceProviderCreateOrUpdate"></a>
# **customResourceProviderCreateOrUpdate**
> CustomRPManifest customResourceProviderCreateOrUpdate(subscriptionId, resourceGroupName, resourceProviderName, apiVersion, resourceProvider)



Creates or updates the custom resource provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomResourceProviderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomResourceProviderApi apiInstance = new CustomResourceProviderApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String resourceProviderName = "resourceProviderName_example"; // String | The name of the resource provider.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    CustomRPManifest resourceProvider = new CustomRPManifest(); // CustomRPManifest | The parameters required to create or update a custom resource provider definition.
    try {
      CustomRPManifest result = apiInstance.customResourceProviderCreateOrUpdate(subscriptionId, resourceGroupName, resourceProviderName, apiVersion, resourceProvider);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomResourceProviderApi#customResourceProviderCreateOrUpdate");
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
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **resourceProviderName** | **String**| The name of the resource provider. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **resourceProvider** | [**CustomRPManifest**](CustomRPManifest.md)| The parameters required to create or update a custom resource provider definition. | |

### Return type

[**CustomRPManifest**](CustomRPManifest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. Resource already exists and the changes have been accepted |  -  |
| **201** | Created response definition. Resource has been created |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="customResourceProviderDelete"></a>
# **customResourceProviderDelete**
> customResourceProviderDelete(subscriptionId, resourceGroupName, resourceProviderName, apiVersion)



Deletes the custom resource provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomResourceProviderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomResourceProviderApi apiInstance = new CustomResourceProviderApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String resourceProviderName = "resourceProviderName_example"; // String | The name of the resource provider.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    try {
      apiInstance.customResourceProviderDelete(subscriptionId, resourceGroupName, resourceProviderName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomResourceProviderApi#customResourceProviderDelete");
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
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **resourceProviderName** | **String**| The name of the resource provider. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK resource deleted |  -  |
| **202** | OK resource delete has been accepted. |  -  |
| **204** | OK resource was not found. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="customResourceProviderGet"></a>
# **customResourceProviderGet**
> CustomRPManifest customResourceProviderGet(subscriptionId, resourceGroupName, resourceProviderName, apiVersion)



Gets the custom resource provider manifest.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomResourceProviderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomResourceProviderApi apiInstance = new CustomResourceProviderApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String resourceProviderName = "resourceProviderName_example"; // String | The name of the resource provider.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    try {
      CustomRPManifest result = apiInstance.customResourceProviderGet(subscriptionId, resourceGroupName, resourceProviderName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomResourceProviderApi#customResourceProviderGet");
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
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **resourceProviderName** | **String**| The name of the resource provider. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |

### Return type

[**CustomRPManifest**](CustomRPManifest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition with the existing resource. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="customResourceProviderListByResourceGroup"></a>
# **customResourceProviderListByResourceGroup**
> ListByCustomRPManifest customResourceProviderListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Gets all the custom resource providers within a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomResourceProviderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomResourceProviderApi apiInstance = new CustomResourceProviderApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    try {
      ListByCustomRPManifest result = apiInstance.customResourceProviderListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomResourceProviderApi#customResourceProviderListByResourceGroup");
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
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |

### Return type

[**ListByCustomRPManifest**](ListByCustomRPManifest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of custom resource providers. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="customResourceProviderListBySubscription"></a>
# **customResourceProviderListBySubscription**
> ListByCustomRPManifest customResourceProviderListBySubscription(subscriptionId, apiVersion)



Gets all the custom resource providers within a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomResourceProviderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomResourceProviderApi apiInstance = new CustomResourceProviderApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    try {
      ListByCustomRPManifest result = apiInstance.customResourceProviderListBySubscription(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomResourceProviderApi#customResourceProviderListBySubscription");
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
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |

### Return type

[**ListByCustomRPManifest**](ListByCustomRPManifest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of custom resource providers. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="customResourceProviderUpdate"></a>
# **customResourceProviderUpdate**
> CustomRPManifest customResourceProviderUpdate(subscriptionId, resourceGroupName, resourceProviderName, apiVersion, patchableResource)



Updates an existing custom resource provider. The only value that can be updated via PATCH currently is the tags.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomResourceProviderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomResourceProviderApi apiInstance = new CustomResourceProviderApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String resourceProviderName = "resourceProviderName_example"; // String | The name of the resource provider.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    ResourceProvidersUpdate patchableResource = new ResourceProvidersUpdate(); // ResourceProvidersUpdate | The updatable fields of a custom resource provider.
    try {
      CustomRPManifest result = apiInstance.customResourceProviderUpdate(subscriptionId, resourceGroupName, resourceProviderName, apiVersion, patchableResource);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomResourceProviderApi#customResourceProviderUpdate");
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
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **resourceProviderName** | **String**| The name of the resource provider. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **patchableResource** | [**ResourceProvidersUpdate**](ResourceProvidersUpdate.md)| The updatable fields of a custom resource provider. | |

### Return type

[**CustomRPManifest**](CustomRPManifest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response. The resource has been updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

