# ImagesApi

All URIs are relative to *https://hub.docker.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNamespacesRepositoriesImages**](ImagesApi.md#getNamespacesRepositoriesImages) | **GET** /v2/namespaces/{namespace}/repositories/{repository}/images | Get details of repository&#39;s images |
| [**getNamespacesRepositoriesImagesSummary**](ImagesApi.md#getNamespacesRepositoriesImagesSummary) | **GET** /v2/namespaces/{namespace}/repositories/{repository}/images-summary | Get summary of repository&#39;s images |
| [**getNamespacesRepositoriesImagesTags**](ImagesApi.md#getNamespacesRepositoriesImagesTags) | **GET** /v2/namespaces/{namespace}/repositories/{repository}/images/{digest}/tags | Get image&#39;s tags |
| [**postNamespacesDeleteImages**](ImagesApi.md#postNamespacesDeleteImages) | **POST** /v2/namespaces/{namespace}/delete-images | Delete images |


<a id="getNamespacesRepositoriesImages"></a>
# **getNamespacesRepositoriesImages**
> GetNamespaceRepositoryImagesResponse getNamespacesRepositoriesImages(namespace, repository, status, currentlyTagged, ordering, activeFrom, page, pageSize)

Get details of repository&#39;s images

Gets details on the images in a repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String namespace = "namespace_example"; // String | Namespace of the repository.
    String repository = "repository_example"; // String | Name of the repository.
    String status = "active"; // String | Filters to only show images of this status.
    Boolean currentlyTagged = true; // Boolean | Filters to only show images with: - `true`: at least 1 current tag. - `false`: no current tags. 
    String ordering = "last_activity"; // String | Orders the results by this property.  Prefixing with `-` sorts by descending order. 
    String activeFrom = "activeFrom_example"; // String | Sets the time from which an image must have been pushed or pulled to be counted as active.  Defaults to 1 month before the current time. 
    Integer page = 56; // Integer | Page number to get. Defaults to 1.
    Integer pageSize = 56; // Integer | Number of images to get per page. Defaults to 10. Max of 100.
    try {
      GetNamespaceRepositoryImagesResponse result = apiInstance.getNamespacesRepositoriesImages(namespace, repository, status, currentlyTagged, ordering, activeFrom, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getNamespacesRepositoriesImages");
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
| **namespace** | **String**| Namespace of the repository. | |
| **repository** | **String**| Name of the repository. | |
| **status** | **String**| Filters to only show images of this status. | [optional] [enum: active, inactive] |
| **currentlyTagged** | **Boolean**| Filters to only show images with: - &#x60;true&#x60;: at least 1 current tag. - &#x60;false&#x60;: no current tags.  | [optional] |
| **ordering** | **String**| Orders the results by this property.  Prefixing with &#x60;-&#x60; sorts by descending order.  | [optional] [enum: last_activity, -last_activity, digest, -digest] |
| **activeFrom** | **String**| Sets the time from which an image must have been pushed or pulled to be counted as active.  Defaults to 1 month before the current time.  | [optional] |
| **page** | **Integer**| Page number to get. Defaults to 1. | [optional] |
| **pageSize** | **Integer**| Number of images to get per page. Defaults to 10. Max of 100. | [optional] |

### Return type

[**GetNamespaceRepositoryImagesResponse**](GetNamespaceRepositoryImagesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized - user does not have read access to the namespace. |  -  |
| **403** | Forbidden - this API is only available to users on Pro or Team plans. |  -  |

<a id="getNamespacesRepositoriesImagesSummary"></a>
# **getNamespacesRepositoriesImagesSummary**
> GetNamespaceRepositoryImagesSummaryResponse getNamespacesRepositoriesImagesSummary(namespace, repository, activeFrom)

Get summary of repository&#39;s images

Gets the number of images in a repository and the number of images counted as active and inactive. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String namespace = "namespace_example"; // String | Namespace of the repository.
    String repository = "repository_example"; // String | Name of the repository.
    String activeFrom = "activeFrom_example"; // String | Sets the time from which an image must have been pushed or pulled to be counted as active.  Defaults to 1 month before the current time. 
    try {
      GetNamespaceRepositoryImagesSummaryResponse result = apiInstance.getNamespacesRepositoriesImagesSummary(namespace, repository, activeFrom);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getNamespacesRepositoriesImagesSummary");
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
| **namespace** | **String**| Namespace of the repository. | |
| **repository** | **String**| Name of the repository. | |
| **activeFrom** | **String**| Sets the time from which an image must have been pushed or pulled to be counted as active.  Defaults to 1 month before the current time.  | [optional] |

### Return type

[**GetNamespaceRepositoryImagesSummaryResponse**](GetNamespaceRepositoryImagesSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized - user does not have read access to the namespace |  -  |

<a id="getNamespacesRepositoriesImagesTags"></a>
# **getNamespacesRepositoriesImagesTags**
> GetNamespaceRepositoryImagesTagsResponse getNamespacesRepositoriesImagesTags(namespace, repository, digest, page, pageSize)

Get image&#39;s tags

Gets current and historical tags for an image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String namespace = "namespace_example"; // String | Namespace of the repository.
    String repository = "repository_example"; // String | Name of the repository.
    String digest = "digest_example"; // String | Digest of the image.
    Integer page = 56; // Integer | Page number to get. Defaults to 1.
    Integer pageSize = 56; // Integer | Number of images to get per page. Defaults to 10. Max of 100.
    try {
      GetNamespaceRepositoryImagesTagsResponse result = apiInstance.getNamespacesRepositoriesImagesTags(namespace, repository, digest, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getNamespacesRepositoriesImagesTags");
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
| **namespace** | **String**| Namespace of the repository. | |
| **repository** | **String**| Name of the repository. | |
| **digest** | **String**| Digest of the image. | |
| **page** | **Integer**| Page number to get. Defaults to 1. | [optional] |
| **pageSize** | **Integer**| Number of images to get per page. Defaults to 10. Max of 100. | [optional] |

### Return type

[**GetNamespaceRepositoryImagesTagsResponse**](GetNamespaceRepositoryImagesTagsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized - user does not have read access to the namespace |  -  |
| **403** | Forbidden - this API is only available to users on Pro or Team plans |  -  |

<a id="postNamespacesDeleteImages"></a>
# **postNamespacesDeleteImages**
> PostNamespacesDeleteImagesResponseSuccess postNamespacesDeleteImages(namespace, postNamespacesDeleteImagesRequest)

Delete images

Deletes one or more images within a namespace. This is currently limited to a single  repository.  If you attempt to delete images that are marked as active or are currently tagged, the deletion does not happen and it displays the warnings. To continue with the deletion, you must ignore these warnings by putting them in the &#x60;ignore_warnings&#x60; property.  Deleting a currently tagged image deletes the tag from the repository.  You cannot ignore errors. It is not possible to directly delete children of multi-arch images. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String namespace = "namespace_example"; // String | Namespace of the repository.
    PostNamespacesDeleteImagesRequest postNamespacesDeleteImagesRequest = new PostNamespacesDeleteImagesRequest(); // PostNamespacesDeleteImagesRequest | Delete request.
    try {
      PostNamespacesDeleteImagesResponseSuccess result = apiInstance.postNamespacesDeleteImages(namespace, postNamespacesDeleteImagesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#postNamespacesDeleteImages");
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
| **namespace** | **String**| Namespace of the repository. | |
| **postNamespacesDeleteImagesRequest** | [**PostNamespacesDeleteImagesRequest**](PostNamespacesDeleteImagesRequest.md)| Delete request. | |

### Return type

[**PostNamespacesDeleteImagesResponseSuccess**](PostNamespacesDeleteImagesResponseSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deletion completed |  -  |
| **400** | Deletion not possible |  -  |
| **403** | Forbidden - this API is only available to users on Pro or Team plans |  -  |

