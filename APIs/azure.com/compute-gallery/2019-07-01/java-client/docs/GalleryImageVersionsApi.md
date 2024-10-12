# GalleryImageVersionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**galleryImageVersionsCreateOrUpdate**](GalleryImageVersionsApi.md#galleryImageVersionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName}/versions/{galleryImageVersionName} |  |
| [**galleryImageVersionsDelete**](GalleryImageVersionsApi.md#galleryImageVersionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName}/versions/{galleryImageVersionName} |  |
| [**galleryImageVersionsGet**](GalleryImageVersionsApi.md#galleryImageVersionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName}/versions/{galleryImageVersionName} |  |
| [**galleryImageVersionsListByGalleryImage**](GalleryImageVersionsApi.md#galleryImageVersionsListByGalleryImage) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName}/versions |  |
| [**galleryImageVersionsUpdate**](GalleryImageVersionsApi.md#galleryImageVersionsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName}/versions/{galleryImageVersionName} |  |


<a id="galleryImageVersionsCreateOrUpdate"></a>
# **galleryImageVersionsCreateOrUpdate**
> GalleryImageVersion galleryImageVersionsCreateOrUpdate(subscriptionId, resourceGroupName, galleryName, galleryImageName, galleryImageVersionName, apiVersion, galleryImageVersion)



Create or update a gallery Image Version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryImageVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GalleryImageVersionsApi apiInstance = new GalleryImageVersionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String galleryName = "galleryName_example"; // String | The name of the Shared Image Gallery in which the Image Definition resides.
    String galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image Definition in which the Image Version is to be created.
    String galleryImageVersionName = "galleryImageVersionName_example"; // String | The name of the gallery Image Version to be created. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: <MajorVersion>.<MinorVersion>.<Patch>
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    GalleryImageVersion galleryImageVersion = new GalleryImageVersion(); // GalleryImageVersion | Parameters supplied to the create or update gallery Image Version operation.
    try {
      GalleryImageVersion result = apiInstance.galleryImageVersionsCreateOrUpdate(subscriptionId, resourceGroupName, galleryName, galleryImageName, galleryImageVersionName, apiVersion, galleryImageVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryImageVersionsApi#galleryImageVersionsCreateOrUpdate");
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
| **galleryName** | **String**| The name of the Shared Image Gallery in which the Image Definition resides. | |
| **galleryImageName** | **String**| The name of the gallery Image Definition in which the Image Version is to be created. | |
| **galleryImageVersionName** | **String**| The name of the gallery Image Version to be created. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: &lt;MajorVersion&gt;.&lt;MinorVersion&gt;.&lt;Patch&gt; | |
| **apiVersion** | **String**| Client Api Version. | |
| **galleryImageVersion** | [**GalleryImageVersion**](GalleryImageVersion.md)| Parameters supplied to the create or update gallery Image Version operation. | |

### Return type

[**GalleryImageVersion**](GalleryImageVersion.md)

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

<a id="galleryImageVersionsDelete"></a>
# **galleryImageVersionsDelete**
> galleryImageVersionsDelete(subscriptionId, resourceGroupName, galleryName, galleryImageName, galleryImageVersionName, apiVersion)



Delete a gallery Image Version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryImageVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GalleryImageVersionsApi apiInstance = new GalleryImageVersionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String galleryName = "galleryName_example"; // String | The name of the Shared Image Gallery in which the Image Definition resides.
    String galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image Definition in which the Image Version resides.
    String galleryImageVersionName = "galleryImageVersionName_example"; // String | The name of the gallery Image Version to be deleted.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      apiInstance.galleryImageVersionsDelete(subscriptionId, resourceGroupName, galleryName, galleryImageName, galleryImageVersionName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryImageVersionsApi#galleryImageVersionsDelete");
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
| **galleryName** | **String**| The name of the Shared Image Gallery in which the Image Definition resides. | |
| **galleryImageName** | **String**| The name of the gallery Image Definition in which the Image Version resides. | |
| **galleryImageVersionName** | **String**| The name of the gallery Image Version to be deleted. | |
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

<a id="galleryImageVersionsGet"></a>
# **galleryImageVersionsGet**
> GalleryImageVersion galleryImageVersionsGet(subscriptionId, resourceGroupName, galleryName, galleryImageName, galleryImageVersionName, apiVersion, $expand)



Retrieves information about a gallery Image Version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryImageVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GalleryImageVersionsApi apiInstance = new GalleryImageVersionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String galleryName = "galleryName_example"; // String | The name of the Shared Image Gallery in which the Image Definition resides.
    String galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image Definition in which the Image Version resides.
    String galleryImageVersionName = "galleryImageVersionName_example"; // String | The name of the gallery Image Version to be retrieved.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $expand = "ReplicationStatus"; // String | The expand expression to apply on the operation.
    try {
      GalleryImageVersion result = apiInstance.galleryImageVersionsGet(subscriptionId, resourceGroupName, galleryName, galleryImageName, galleryImageVersionName, apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryImageVersionsApi#galleryImageVersionsGet");
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
| **galleryName** | **String**| The name of the Shared Image Gallery in which the Image Definition resides. | |
| **galleryImageName** | **String**| The name of the gallery Image Definition in which the Image Version resides. | |
| **galleryImageVersionName** | **String**| The name of the gallery Image Version to be retrieved. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$expand** | **String**| The expand expression to apply on the operation. | [optional] [enum: ReplicationStatus] |

### Return type

[**GalleryImageVersion**](GalleryImageVersion.md)

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

<a id="galleryImageVersionsListByGalleryImage"></a>
# **galleryImageVersionsListByGalleryImage**
> GalleryImageVersionList galleryImageVersionsListByGalleryImage(subscriptionId, resourceGroupName, galleryName, galleryImageName, apiVersion)



List gallery Image Versions in a gallery Image Definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryImageVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GalleryImageVersionsApi apiInstance = new GalleryImageVersionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String galleryName = "galleryName_example"; // String | The name of the Shared Image Gallery in which the Image Definition resides.
    String galleryImageName = "galleryImageName_example"; // String | The name of the Shared Image Gallery Image Definition from which the Image Versions are to be listed.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      GalleryImageVersionList result = apiInstance.galleryImageVersionsListByGalleryImage(subscriptionId, resourceGroupName, galleryName, galleryImageName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryImageVersionsApi#galleryImageVersionsListByGalleryImage");
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
| **galleryName** | **String**| The name of the Shared Image Gallery in which the Image Definition resides. | |
| **galleryImageName** | **String**| The name of the Shared Image Gallery Image Definition from which the Image Versions are to be listed. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**GalleryImageVersionList**](GalleryImageVersionList.md)

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

<a id="galleryImageVersionsUpdate"></a>
# **galleryImageVersionsUpdate**
> GalleryImageVersion galleryImageVersionsUpdate(subscriptionId, resourceGroupName, galleryName, galleryImageName, galleryImageVersionName, apiVersion, galleryImageVersion)



Update a gallery Image Version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryImageVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GalleryImageVersionsApi apiInstance = new GalleryImageVersionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String galleryName = "galleryName_example"; // String | The name of the Shared Image Gallery in which the Image Definition resides.
    String galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image Definition in which the Image Version is to be updated.
    String galleryImageVersionName = "galleryImageVersionName_example"; // String | The name of the gallery Image Version to be updated. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: <MajorVersion>.<MinorVersion>.<Patch>
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    GalleryImageVersionUpdate galleryImageVersion = new GalleryImageVersionUpdate(); // GalleryImageVersionUpdate | Parameters supplied to the update gallery Image Version operation.
    try {
      GalleryImageVersion result = apiInstance.galleryImageVersionsUpdate(subscriptionId, resourceGroupName, galleryName, galleryImageName, galleryImageVersionName, apiVersion, galleryImageVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryImageVersionsApi#galleryImageVersionsUpdate");
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
| **galleryName** | **String**| The name of the Shared Image Gallery in which the Image Definition resides. | |
| **galleryImageName** | **String**| The name of the gallery Image Definition in which the Image Version is to be updated. | |
| **galleryImageVersionName** | **String**| The name of the gallery Image Version to be updated. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: &lt;MajorVersion&gt;.&lt;MinorVersion&gt;.&lt;Patch&gt; | |
| **apiVersion** | **String**| Client Api Version. | |
| **galleryImageVersion** | [**GalleryImageVersionUpdate**](GalleryImageVersionUpdate.md)| Parameters supplied to the update gallery Image Version operation. | |

### Return type

[**GalleryImageVersion**](GalleryImageVersion.md)

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

