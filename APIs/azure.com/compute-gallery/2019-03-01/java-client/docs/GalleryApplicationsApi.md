# GalleryApplicationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**galleryApplicationsCreateOrUpdate**](GalleryApplicationsApi.md#galleryApplicationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName} |  |
| [**galleryApplicationsDelete**](GalleryApplicationsApi.md#galleryApplicationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName} |  |
| [**galleryApplicationsGet**](GalleryApplicationsApi.md#galleryApplicationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName} |  |
| [**galleryApplicationsListByGallery**](GalleryApplicationsApi.md#galleryApplicationsListByGallery) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications |  |


<a id="galleryApplicationsCreateOrUpdate"></a>
# **galleryApplicationsCreateOrUpdate**
> GalleryApplication galleryApplicationsCreateOrUpdate(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, apiVersion, galleryApplication)



Create or update a gallery Application Definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryApplicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GalleryApplicationsApi apiInstance = new GalleryApplicationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String galleryName = "galleryName_example"; // String | The name of the Shared Application Gallery in which the Application Definition is to be created.
    String galleryApplicationName = "galleryApplicationName_example"; // String | The name of the gallery Application Definition to be created or updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    GalleryApplication galleryApplication = new GalleryApplication(); // GalleryApplication | Parameters supplied to the create or update gallery Application operation.
    try {
      GalleryApplication result = apiInstance.galleryApplicationsCreateOrUpdate(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, apiVersion, galleryApplication);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryApplicationsApi#galleryApplicationsCreateOrUpdate");
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
| **galleryName** | **String**| The name of the Shared Application Gallery in which the Application Definition is to be created. | |
| **galleryApplicationName** | **String**| The name of the gallery Application Definition to be created or updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters. | |
| **apiVersion** | **String**| Client Api Version. | |
| **galleryApplication** | [**GalleryApplication**](GalleryApplication.md)| Parameters supplied to the create or update gallery Application operation. | |

### Return type

[**GalleryApplication**](GalleryApplication.md)

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

<a id="galleryApplicationsDelete"></a>
# **galleryApplicationsDelete**
> galleryApplicationsDelete(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, apiVersion)



Delete a gallery Application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryApplicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GalleryApplicationsApi apiInstance = new GalleryApplicationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String galleryName = "galleryName_example"; // String | The name of the Shared Application Gallery in which the Application Definition is to be deleted.
    String galleryApplicationName = "galleryApplicationName_example"; // String | The name of the gallery Application Definition to be deleted.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      apiInstance.galleryApplicationsDelete(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryApplicationsApi#galleryApplicationsDelete");
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
| **galleryName** | **String**| The name of the Shared Application Gallery in which the Application Definition is to be deleted. | |
| **galleryApplicationName** | **String**| The name of the gallery Application Definition to be deleted. | |
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

<a id="galleryApplicationsGet"></a>
# **galleryApplicationsGet**
> GalleryApplication galleryApplicationsGet(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, apiVersion)



Retrieves information about a gallery Application Definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryApplicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GalleryApplicationsApi apiInstance = new GalleryApplicationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String galleryName = "galleryName_example"; // String | The name of the Shared Application Gallery from which the Application Definitions are to be retrieved.
    String galleryApplicationName = "galleryApplicationName_example"; // String | The name of the gallery Application Definition to be retrieved.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      GalleryApplication result = apiInstance.galleryApplicationsGet(subscriptionId, resourceGroupName, galleryName, galleryApplicationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryApplicationsApi#galleryApplicationsGet");
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
| **galleryName** | **String**| The name of the Shared Application Gallery from which the Application Definitions are to be retrieved. | |
| **galleryApplicationName** | **String**| The name of the gallery Application Definition to be retrieved. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**GalleryApplication**](GalleryApplication.md)

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

<a id="galleryApplicationsListByGallery"></a>
# **galleryApplicationsListByGallery**
> GalleryApplicationList galleryApplicationsListByGallery(subscriptionId, resourceGroupName, galleryName, apiVersion)



List gallery Application Definitions in a gallery.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryApplicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GalleryApplicationsApi apiInstance = new GalleryApplicationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String galleryName = "galleryName_example"; // String | The name of the Shared Application Gallery from which Application Definitions are to be listed.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      GalleryApplicationList result = apiInstance.galleryApplicationsListByGallery(subscriptionId, resourceGroupName, galleryName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryApplicationsApi#galleryApplicationsListByGallery");
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
| **galleryName** | **String**| The name of the Shared Application Gallery from which Application Definitions are to be listed. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**GalleryApplicationList**](GalleryApplicationList.md)

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

