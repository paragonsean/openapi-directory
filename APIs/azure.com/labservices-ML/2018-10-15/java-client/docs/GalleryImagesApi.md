# GalleryImagesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**galleryImagesCreateOrUpdate**](GalleryImagesApi.md#galleryImagesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/galleryimages/{galleryImageName} |  |
| [**galleryImagesDelete**](GalleryImagesApi.md#galleryImagesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/galleryimages/{galleryImageName} |  |
| [**galleryImagesGet**](GalleryImagesApi.md#galleryImagesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/galleryimages/{galleryImageName} |  |
| [**galleryImagesList**](GalleryImagesApi.md#galleryImagesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/galleryimages |  |
| [**galleryImagesUpdate**](GalleryImagesApi.md#galleryImagesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/galleryimages/{galleryImageName} |  |


<a id="galleryImagesCreateOrUpdate"></a>
# **galleryImagesCreateOrUpdate**
> GalleryImage galleryImagesCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, galleryImageName, apiVersion, galleryImage)



Create or replace an existing Gallery Image.

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
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image.
    String apiVersion = "2018-10-15"; // String | Client API version.
    GalleryImage galleryImage = new GalleryImage(); // GalleryImage | Represents an image from the Azure Marketplace
    try {
      GalleryImage result = apiInstance.galleryImagesCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, galleryImageName, apiVersion, galleryImage);
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **galleryImageName** | **String**| The name of the gallery Image. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **galleryImage** | [**GalleryImage**](GalleryImage.md)| Represents an image from the Azure Marketplace | |

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
| **0** | BadRequest |  -  |

<a id="galleryImagesDelete"></a>
# **galleryImagesDelete**
> galleryImagesDelete(subscriptionId, resourceGroupName, labAccountName, galleryImageName, apiVersion)



Delete gallery image.

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
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image.
    String apiVersion = "2018-10-15"; // String | Client API version.
    try {
      apiInstance.galleryImagesDelete(subscriptionId, resourceGroupName, labAccountName, galleryImageName, apiVersion);
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **galleryImageName** | **String**| The name of the gallery Image. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |

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
| **204** | No Content |  -  |
| **0** | BadRequest |  -  |

<a id="galleryImagesGet"></a>
# **galleryImagesGet**
> GalleryImage galleryImagesGet(subscriptionId, resourceGroupName, labAccountName, galleryImageName, apiVersion, $expand)



Get gallery image

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
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image.
    String apiVersion = "2018-10-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($select=author)'
    try {
      GalleryImage result = apiInstance.galleryImagesGet(subscriptionId, resourceGroupName, labAccountName, galleryImageName, apiVersion, $expand);
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **galleryImageName** | **String**| The name of the gallery Image. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;author)&#39; | [optional] |

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
| **0** | BadRequest |  -  |

<a id="galleryImagesList"></a>
# **galleryImagesList**
> ResponseWithContinuationGalleryImage galleryImagesList(subscriptionId, resourceGroupName, labAccountName, apiVersion, $expand, $filter, $top, $orderby)



List gallery images in a given lab account.

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
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String apiVersion = "2018-10-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($select=author)'
    String $filter = "$filter_example"; // String | The filter to apply to the operation.
    Integer $top = 56; // Integer | The maximum number of resources to return from the operation.
    String $orderby = "$orderby_example"; // String | The ordering expression for the results, using OData notation.
    try {
      ResponseWithContinuationGalleryImage result = apiInstance.galleryImagesList(subscriptionId, resourceGroupName, labAccountName, apiVersion, $expand, $filter, $top, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryImagesApi#galleryImagesList");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;author)&#39; | [optional] |
| **$filter** | **String**| The filter to apply to the operation. | [optional] |
| **$top** | **Integer**| The maximum number of resources to return from the operation. | [optional] |
| **$orderby** | **String**| The ordering expression for the results, using OData notation. | [optional] |

### Return type

[**ResponseWithContinuationGalleryImage**](ResponseWithContinuationGalleryImage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="galleryImagesUpdate"></a>
# **galleryImagesUpdate**
> GalleryImage galleryImagesUpdate(subscriptionId, resourceGroupName, labAccountName, galleryImageName, apiVersion, galleryImage)



Modify properties of gallery images.

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
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String galleryImageName = "galleryImageName_example"; // String | The name of the gallery Image.
    String apiVersion = "2018-10-15"; // String | Client API version.
    GalleryImageFragment galleryImage = new GalleryImageFragment(); // GalleryImageFragment | Represents an image from the Azure Marketplace
    try {
      GalleryImage result = apiInstance.galleryImagesUpdate(subscriptionId, resourceGroupName, labAccountName, galleryImageName, apiVersion, galleryImage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryImagesApi#galleryImagesUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **galleryImageName** | **String**| The name of the gallery Image. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **galleryImage** | [**GalleryImageFragment**](GalleryImageFragment.md)| Represents an image from the Azure Marketplace | |

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
| **0** | BadRequest |  -  |

