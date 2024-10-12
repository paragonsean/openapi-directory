# GalleryImagesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**galleryImagesCreateOrUpdate**](GalleryImagesApi.md#galleryImagesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName} |  |
| [**galleryImagesDelete**](GalleryImagesApi.md#galleryImagesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName} |  |
| [**galleryImagesGet**](GalleryImagesApi.md#galleryImagesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName} |  |
| [**galleryImagesListByGallery**](GalleryImagesApi.md#galleryImagesListByGallery) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images |  |


<a id="galleryImagesCreateOrUpdate"></a>
# **galleryImagesCreateOrUpdate**
> GalleryImage galleryImagesCreateOrUpdate(subscriptionId, resourceGroupName, galleryName, galleryImageName, apiVersion, galleryImage)



Create or update a gallery Image Definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GalleryImagesApi apiInstance = new GalleryImagesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String galleryName = "galleryName_example"; // String | The name of the Shared Image Gallery in which the Image Definition is to be created.
    String galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image Definition to be created or updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    GalleryImage galleryImage = new GalleryImage(); // GalleryImage | Parameters supplied to the create or update gallery image operation.
    try {
      GalleryImage result = apiInstance.galleryImagesCreateOrUpdate(subscriptionId, resourceGroupName, galleryName, galleryImageName, apiVersion, galleryImage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryImagesApi#galleryImagesCreateOrUpdate");
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
| **galleryName** | **String**| The name of the Shared Image Gallery in which the Image Definition is to be created. | |
| **galleryImageName** | **String**| The name of the gallery Image Definition to be created or updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters. | |
| **apiVersion** | **String**| Client Api Version. | |
| **galleryImage** | [**GalleryImage**](GalleryImage.md)| Parameters supplied to the create or update gallery image operation. | |

### Return type

[**GalleryImage**](GalleryImage.md)

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

<a id="galleryImagesDelete"></a>
# **galleryImagesDelete**
> galleryImagesDelete(subscriptionId, resourceGroupName, galleryName, galleryImageName, apiVersion)



Delete a gallery image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GalleryImagesApi apiInstance = new GalleryImagesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String galleryName = "galleryName_example"; // String | The name of the Shared Image Gallery in which the Image Definition is to be deleted.
    String galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image Definition to be deleted.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      apiInstance.galleryImagesDelete(subscriptionId, resourceGroupName, galleryName, galleryImageName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryImagesApi#galleryImagesDelete");
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
| **galleryName** | **String**| The name of the Shared Image Gallery in which the Image Definition is to be deleted. | |
| **galleryImageName** | **String**| The name of the gallery Image Definition to be deleted. | |
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

<a id="galleryImagesGet"></a>
# **galleryImagesGet**
> GalleryImage galleryImagesGet(subscriptionId, resourceGroupName, galleryName, galleryImageName, apiVersion)



Retrieves information about a gallery Image Definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GalleryImagesApi apiInstance = new GalleryImagesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String galleryName = "galleryName_example"; // String | The name of the Shared Image Gallery from which the Image Definitions are to be retrieved.
    String galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image Definition to be retrieved.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      GalleryImage result = apiInstance.galleryImagesGet(subscriptionId, resourceGroupName, galleryName, galleryImageName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryImagesApi#galleryImagesGet");
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
| **galleryName** | **String**| The name of the Shared Image Gallery from which the Image Definitions are to be retrieved. | |
| **galleryImageName** | **String**| The name of the gallery Image Definition to be retrieved. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**GalleryImage**](GalleryImage.md)

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

<a id="galleryImagesListByGallery"></a>
# **galleryImagesListByGallery**
> GalleryImageList galleryImagesListByGallery(subscriptionId, resourceGroupName, galleryName, apiVersion)



List gallery Image Definitions in a gallery.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GalleryImagesApi apiInstance = new GalleryImagesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String galleryName = "galleryName_example"; // String | The name of the Shared Image Gallery from which Image Definitions are to be listed.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      GalleryImageList result = apiInstance.galleryImagesListByGallery(subscriptionId, resourceGroupName, galleryName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryImagesApi#galleryImagesListByGallery");
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
| **galleryName** | **String**| The name of the Shared Image Gallery from which Image Definitions are to be listed. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**GalleryImageList**](GalleryImageList.md)

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

