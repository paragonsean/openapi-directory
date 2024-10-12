# GalleryApplicationVersionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**galleryApplicationVersionsCreateOrUpdate**](GalleryApplicationVersionsApi.md#galleryApplicationVersionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName} |  |
| [**galleryApplicationVersionsDelete**](GalleryApplicationVersionsApi.md#galleryApplicationVersionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName} |  |
| [**galleryApplicationVersionsGet**](GalleryApplicationVersionsApi.md#galleryApplicationVersionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName} |  |
| [**galleryApplicationVersionsListByGalleryApplication**](GalleryApplicationVersionsApi.md#galleryApplicationVersionsListByGalleryApplication) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions |  |
| [**galleryApplicationVersionsUpdate**](GalleryApplicationVersionsApi.md#galleryApplicationVersionsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName} |  |


<a id="galleryApplicationVersionsCreateOrUpdate"></a>
# **galleryApplicationVersionsCreateOrUpdate**
> GalleryApplicationVersion galleryApplicationVersionsCreateOrUpdate(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, galleryApplicationVersionName, apiVersion, galleryApplicationVersion)



Create or update a gallery Application Version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryApplicationVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GalleryApplicationVersionsApi apiInstance = new GalleryApplicationVersionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String galleryName = "galleryName_example"; // String | The name of the Shared Application Gallery in which the Application Definition resides.
    String galleryApplicationName = "galleryApplicationName_example"; // String | The name of the gallery Application Definition in which the Application Version is to be created.
    String galleryApplicationVersionName = "galleryApplicationVersionName_example"; // String | The name of the gallery Application Version to be created. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: <MajorVersion>.<MinorVersion>.<Patch>
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    GalleryApplicationVersion galleryApplicationVersion = new GalleryApplicationVersion(); // GalleryApplicationVersion | Parameters supplied to the create or update gallery Application Version operation.
    try {
      GalleryApplicationVersion result = apiInstance.galleryApplicationVersionsCreateOrUpdate(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, galleryApplicationVersionName, apiVersion, galleryApplicationVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryApplicationVersionsApi#galleryApplicationVersionsCreateOrUpdate");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **galleryName** | **String**| The name of the Shared Application Gallery in which the Application Definition resides. | |
| **galleryApplicationName** | **String**| The name of the gallery Application Definition in which the Application Version is to be created. | |
| **galleryApplicationVersionName** | **String**| The name of the gallery Application Version to be created. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: &lt;MajorVersion&gt;.&lt;MinorVersion&gt;.&lt;Patch&gt; | |
| **apiVersion** | **String**| Client Api Version. | |
| **galleryApplicationVersion** | [**GalleryApplicationVersion**](GalleryApplicationVersion.md)| Parameters supplied to the create or update gallery Application Version operation. | |

### Return type

[**GalleryApplicationVersion**](GalleryApplicationVersion.md)

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
| **202** | Accepted |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="galleryApplicationVersionsDelete"></a>
# **galleryApplicationVersionsDelete**
> galleryApplicationVersionsDelete(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, galleryApplicationVersionName, apiVersion)



Delete a gallery Application Version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryApplicationVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GalleryApplicationVersionsApi apiInstance = new GalleryApplicationVersionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String galleryName = "galleryName_example"; // String | The name of the Shared Application Gallery in which the Application Definition resides.
    String galleryApplicationName = "galleryApplicationName_example"; // String | The name of the gallery Application Definition in which the Application Version resides.
    String galleryApplicationVersionName = "galleryApplicationVersionName_example"; // String | The name of the gallery Application Version to be deleted.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      apiInstance.galleryApplicationVersionsDelete(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, galleryApplicationVersionName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryApplicationVersionsApi#galleryApplicationVersionsDelete");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **galleryName** | **String**| The name of the Shared Application Gallery in which the Application Definition resides. | |
| **galleryApplicationName** | **String**| The name of the gallery Application Definition in which the Application Version resides. | |
| **galleryApplicationVersionName** | **String**| The name of the gallery Application Version to be deleted. | |
| **apiVersion** | **String**| Client Api Version. | |

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
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="galleryApplicationVersionsGet"></a>
# **galleryApplicationVersionsGet**
> GalleryApplicationVersion galleryApplicationVersionsGet(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, galleryApplicationVersionName, apiVersion, $expand)



Retrieves information about a gallery Application Version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryApplicationVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GalleryApplicationVersionsApi apiInstance = new GalleryApplicationVersionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String galleryName = "galleryName_example"; // String | The name of the Shared Application Gallery in which the Application Definition resides.
    String galleryApplicationName = "galleryApplicationName_example"; // String | The name of the gallery Application Definition in which the Application Version resides.
    String galleryApplicationVersionName = "galleryApplicationVersionName_example"; // String | The name of the gallery Application Version to be retrieved.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $expand = "ReplicationStatus"; // String | The expand expression to apply on the operation.
    try {
      GalleryApplicationVersion result = apiInstance.galleryApplicationVersionsGet(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, galleryApplicationVersionName, apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryApplicationVersionsApi#galleryApplicationVersionsGet");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **galleryName** | **String**| The name of the Shared Application Gallery in which the Application Definition resides. | |
| **galleryApplicationName** | **String**| The name of the gallery Application Definition in which the Application Version resides. | |
| **galleryApplicationVersionName** | **String**| The name of the gallery Application Version to be retrieved. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$expand** | **String**| The expand expression to apply on the operation. | [optional] [enum: ReplicationStatus] |

### Return type

[**GalleryApplicationVersion**](GalleryApplicationVersion.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="galleryApplicationVersionsListByGalleryApplication"></a>
# **galleryApplicationVersionsListByGalleryApplication**
> GalleryApplicationVersionList galleryApplicationVersionsListByGalleryApplication(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, apiVersion)



List gallery Application Versions in a gallery Application Definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryApplicationVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GalleryApplicationVersionsApi apiInstance = new GalleryApplicationVersionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String galleryName = "galleryName_example"; // String | The name of the Shared Application Gallery in which the Application Definition resides.
    String galleryApplicationName = "galleryApplicationName_example"; // String | The name of the Shared Application Gallery Application Definition from which the Application Versions are to be listed.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      GalleryApplicationVersionList result = apiInstance.galleryApplicationVersionsListByGalleryApplication(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryApplicationVersionsApi#galleryApplicationVersionsListByGalleryApplication");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **galleryName** | **String**| The name of the Shared Application Gallery in which the Application Definition resides. | |
| **galleryApplicationName** | **String**| The name of the Shared Application Gallery Application Definition from which the Application Versions are to be listed. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**GalleryApplicationVersionList**](GalleryApplicationVersionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="galleryApplicationVersionsUpdate"></a>
# **galleryApplicationVersionsUpdate**
> GalleryApplicationVersion galleryApplicationVersionsUpdate(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, galleryApplicationVersionName, apiVersion, galleryApplicationVersion)



Update a gallery Application Version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryApplicationVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GalleryApplicationVersionsApi apiInstance = new GalleryApplicationVersionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String galleryName = "galleryName_example"; // String | The name of the Shared Application Gallery in which the Application Definition resides.
    String galleryApplicationName = "galleryApplicationName_example"; // String | The name of the gallery Application Definition in which the Application Version is to be updated.
    String galleryApplicationVersionName = "galleryApplicationVersionName_example"; // String | The name of the gallery Application Version to be updated. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: <MajorVersion>.<MinorVersion>.<Patch>
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    GalleryApplicationVersionUpdate galleryApplicationVersion = new GalleryApplicationVersionUpdate(); // GalleryApplicationVersionUpdate | Parameters supplied to the update gallery Application Version operation.
    try {
      GalleryApplicationVersion result = apiInstance.galleryApplicationVersionsUpdate(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, galleryApplicationVersionName, apiVersion, galleryApplicationVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryApplicationVersionsApi#galleryApplicationVersionsUpdate");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **galleryName** | **String**| The name of the Shared Application Gallery in which the Application Definition resides. | |
| **galleryApplicationName** | **String**| The name of the gallery Application Definition in which the Application Version is to be updated. | |
| **galleryApplicationVersionName** | **String**| The name of the gallery Application Version to be updated. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: &lt;MajorVersion&gt;.&lt;MinorVersion&gt;.&lt;Patch&gt; | |
| **apiVersion** | **String**| Client Api Version. | |
| **galleryApplicationVersion** | [**GalleryApplicationVersionUpdate**](GalleryApplicationVersionUpdate.md)| Parameters supplied to the update gallery Application Version operation. | |

### Return type

[**GalleryApplicationVersion**](GalleryApplicationVersion.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

