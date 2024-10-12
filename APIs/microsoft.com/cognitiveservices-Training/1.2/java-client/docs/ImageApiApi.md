# ImageApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createImagesFromData**](ImageApiApi.md#createImagesFromData) | **POST** /projects/{projectId}/images | Add the provided images to the set of training images |
| [**createImagesFromFiles**](ImageApiApi.md#createImagesFromFiles) | **POST** /projects/{projectId}/images/files | Add the provided batch of images to the set of training images |
| [**createImagesFromPredictions**](ImageApiApi.md#createImagesFromPredictions) | **POST** /projects/{projectId}/images/predictions | Add the specified predicted images to the set of training images |
| [**createImagesFromUrls**](ImageApiApi.md#createImagesFromUrls) | **POST** /projects/{projectId}/images/urls | Add the provided images urls to the set of training images |
| [**deleteImageTags**](ImageApiApi.md#deleteImageTags) | **DELETE** /projects/{projectId}/images/tags | Remove a set of tags from a set of images |
| [**deleteImages**](ImageApiApi.md#deleteImages) | **DELETE** /projects/{projectId}/images | Delete images from the set of training images |
| [**getTaggedImages**](ImageApiApi.md#getTaggedImages) | **GET** /projects/{projectId}/images/tagged | Get tagged images for a given project iteration |
| [**getUntaggedImages**](ImageApiApi.md#getUntaggedImages) | **GET** /projects/{projectId}/images/untagged | Get untagged images for a given project iteration |
| [**postImageTags**](ImageApiApi.md#postImageTags) | **POST** /projects/{projectId}/images/tags | Associate a set of images with a set of tags |


<a id="createImagesFromData"></a>
# **createImagesFromData**
> ImageCreateSummary createImagesFromData(projectId, trainingKey, imageData, tagIds)

Add the provided images to the set of training images

This API accepts body content as multipart/form-data and application/octet-stream. When using multipart  multiple image files can be sent at once, with a maximum of 64 files

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    ImageApiApi apiInstance = new ImageApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id
    String trainingKey = "{API Key}"; // String | 
    File imageData = new File("/path/to/file"); // File | 
    List<String> tagIds = Arrays.asList(); // List<String> | The tags ids with which to tag each image. Limited to 20
    try {
      ImageCreateSummary result = apiInstance.createImagesFromData(projectId, trainingKey, imageData, tagIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageApiApi#createImagesFromData");
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
| **projectId** | **UUID**| The project id | |
| **trainingKey** | **String**|  | |
| **imageData** | **File**|  | |
| **tagIds** | [**List&lt;String&gt;**](String.md)| The tags ids with which to tag each image. Limited to 20 | [optional] |

### Return type

[**ImageCreateSummary**](ImageCreateSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="createImagesFromFiles"></a>
# **createImagesFromFiles**
> ImageCreateSummary createImagesFromFiles(projectId, trainingKey, imageFileCreateBatch)

Add the provided batch of images to the set of training images

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    ImageApiApi apiInstance = new ImageApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id
    String trainingKey = "{API Key}"; // String | 
    ImageFileCreateBatch imageFileCreateBatch = new ImageFileCreateBatch(); // ImageFileCreateBatch | The batch of image files to add. Limited to 64 images and 20 tags per batch
    try {
      ImageCreateSummary result = apiInstance.createImagesFromFiles(projectId, trainingKey, imageFileCreateBatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageApiApi#createImagesFromFiles");
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
| **projectId** | **UUID**| The project id | |
| **trainingKey** | **String**|  | |
| **imageFileCreateBatch** | [**ImageFileCreateBatch**](ImageFileCreateBatch.md)| The batch of image files to add. Limited to 64 images and 20 tags per batch | |

### Return type

[**ImageCreateSummary**](ImageCreateSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="createImagesFromPredictions"></a>
# **createImagesFromPredictions**
> ImageCreateSummary createImagesFromPredictions(projectId, trainingKey, imageIdCreateBatch)

Add the specified predicted images to the set of training images

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    ImageApiApi apiInstance = new ImageApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id
    String trainingKey = "{API Key}"; // String | 
    ImageIdCreateBatch imageIdCreateBatch = new ImageIdCreateBatch(); // ImageIdCreateBatch | Image and tag ids. Limited to 64 images and 20 tags per batch
    try {
      ImageCreateSummary result = apiInstance.createImagesFromPredictions(projectId, trainingKey, imageIdCreateBatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageApiApi#createImagesFromPredictions");
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
| **projectId** | **UUID**| The project id | |
| **trainingKey** | **String**|  | |
| **imageIdCreateBatch** | [**ImageIdCreateBatch**](ImageIdCreateBatch.md)| Image and tag ids. Limited to 64 images and 20 tags per batch | |

### Return type

[**ImageCreateSummary**](ImageCreateSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="createImagesFromUrls"></a>
# **createImagesFromUrls**
> ImageCreateSummary createImagesFromUrls(projectId, trainingKey, imageUrlCreateBatch)

Add the provided images urls to the set of training images

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    ImageApiApi apiInstance = new ImageApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id
    String trainingKey = "{API Key}"; // String | 
    ImageUrlCreateBatch imageUrlCreateBatch = new ImageUrlCreateBatch(); // ImageUrlCreateBatch | Image urls and tag ids. Limited to 64 images and 20 tags per batch
    try {
      ImageCreateSummary result = apiInstance.createImagesFromUrls(projectId, trainingKey, imageUrlCreateBatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageApiApi#createImagesFromUrls");
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
| **projectId** | **UUID**| The project id | |
| **trainingKey** | **String**|  | |
| **imageUrlCreateBatch** | [**ImageUrlCreateBatch**](ImageUrlCreateBatch.md)| Image urls and tag ids. Limited to 64 images and 20 tags per batch | |

### Return type

[**ImageCreateSummary**](ImageCreateSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="deleteImageTags"></a>
# **deleteImageTags**
> deleteImageTags(projectId, imageIds, tagIds, trainingKey)

Remove a set of tags from a set of images

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    ImageApiApi apiInstance = new ImageApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id
    List<String> imageIds = Arrays.asList(); // List<String> | Image ids. Limited to 64 images
    List<String> tagIds = Arrays.asList(); // List<String> | Tags to be deleted from the specified images. Limited to 20 tags
    String trainingKey = "{API Key}"; // String | 
    try {
      apiInstance.deleteImageTags(projectId, imageIds, tagIds, trainingKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageApiApi#deleteImageTags");
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
| **projectId** | **UUID**| The project id | |
| **imageIds** | [**List&lt;String&gt;**](String.md)| Image ids. Limited to 64 images | |
| **tagIds** | [**List&lt;String&gt;**](String.md)| Tags to be deleted from the specified images. Limited to 20 tags | |
| **trainingKey** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="deleteImages"></a>
# **deleteImages**
> deleteImages(projectId, imageIds, trainingKey)

Delete images from the set of training images

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    ImageApiApi apiInstance = new ImageApiApi(defaultClient);
    UUID projectId = UUID.fromString("64b822c5-8082-4b36-a426-27225f4aa18c"); // UUID | The project id
    List<String> imageIds = Arrays.asList(); // List<String> | Ids of the images to be deleted. Limited to 256 images per batch
    String trainingKey = "{API Key}"; // String | 
    try {
      apiInstance.deleteImages(projectId, imageIds, trainingKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageApiApi#deleteImages");
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
| **projectId** | **UUID**| The project id | |
| **imageIds** | [**List&lt;String&gt;**](String.md)| Ids of the images to be deleted. Limited to 256 images per batch | |
| **trainingKey** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="getTaggedImages"></a>
# **getTaggedImages**
> List&lt;Image&gt; getTaggedImages(projectId, trainingKey, iterationId, tagIds, orderBy, take, skip)

Get tagged images for a given project iteration

This API supports batching and range selection. By default it will only return first 50 images matching images.  Use the {take} and {skip} parameters to control how many images to return in a given batch.  The filtering is on an and/or relationship. For example, if the provided tag ids are for the \&quot;Dog\&quot; and  \&quot;Cat\&quot; tags, then only images tagged with Dog and/or Cat will be returned

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    ImageApiApi apiInstance = new ImageApiApi(defaultClient);
    UUID projectId = UUID.fromString("bc3f7dad-5544-468c-8573-3ef04d55463e"); // UUID | The project id
    String trainingKey = "{API Key}"; // String | 
    UUID iterationId = UUID.fromString("cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12"); // UUID | The iteration id. Defaults to workspace
    List<String> tagIds = Arrays.asList(); // List<String> | An list of tags ids to filter the images. Defaults to all tagged images when null. Limited to 20
    String orderBy = "Newest"; // String | The ordering. Defaults to newest
    Integer take = 50; // Integer | Maximum number of images to return. Defaults to 50, limited to 256
    Integer skip = 0; // Integer | Number of images to skip before beginning the image batch. Defaults to 0
    try {
      List<Image> result = apiInstance.getTaggedImages(projectId, trainingKey, iterationId, tagIds, orderBy, take, skip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageApiApi#getTaggedImages");
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
| **projectId** | **UUID**| The project id | |
| **trainingKey** | **String**|  | |
| **iterationId** | **UUID**| The iteration id. Defaults to workspace | [optional] |
| **tagIds** | [**List&lt;String&gt;**](String.md)| An list of tags ids to filter the images. Defaults to all tagged images when null. Limited to 20 | [optional] |
| **orderBy** | **String**| The ordering. Defaults to newest | [optional] [enum: Newest, Oldest] |
| **take** | **Integer**| Maximum number of images to return. Defaults to 50, limited to 256 | [optional] [default to 50] |
| **skip** | **Integer**| Number of images to skip before beginning the image batch. Defaults to 0 | [optional] [default to 0] |

### Return type

[**List&lt;Image&gt;**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getUntaggedImages"></a>
# **getUntaggedImages**
> List&lt;Image&gt; getUntaggedImages(projectId, trainingKey, iterationId, orderBy, take, skip)

Get untagged images for a given project iteration

This API supports batching and range selection. By default it will only return first 50 images matching images.  Use the {take} and {skip} parameters to control how many images to return in a given batch.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    ImageApiApi apiInstance = new ImageApiApi(defaultClient);
    UUID projectId = UUID.fromString("bc3f7dad-5544-468c-8573-3ef04d55463e"); // UUID | The project id
    String trainingKey = "{API Key}"; // String | 
    UUID iterationId = UUID.fromString("cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12"); // UUID | The iteration id. Defaults to workspace
    String orderBy = "Newest"; // String | The ordering. Defaults to newest
    Integer take = 50; // Integer | Maximum number of images to return. Defaults to 50, limited to 256
    Integer skip = 0; // Integer | Number of images to skip before beginning the image batch. Defaults to 0
    try {
      List<Image> result = apiInstance.getUntaggedImages(projectId, trainingKey, iterationId, orderBy, take, skip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageApiApi#getUntaggedImages");
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
| **projectId** | **UUID**| The project id | |
| **trainingKey** | **String**|  | |
| **iterationId** | **UUID**| The iteration id. Defaults to workspace | [optional] |
| **orderBy** | **String**| The ordering. Defaults to newest | [optional] [enum: Newest, Oldest] |
| **take** | **Integer**| Maximum number of images to return. Defaults to 50, limited to 256 | [optional] [default to 50] |
| **skip** | **Integer**| Number of images to skip before beginning the image batch. Defaults to 0 | [optional] [default to 0] |

### Return type

[**List&lt;Image&gt;**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="postImageTags"></a>
# **postImageTags**
> ImageTagCreateSummary postImageTags(projectId, trainingKey, imageTagCreateBatch)

Associate a set of images with a set of tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    ImageApiApi apiInstance = new ImageApiApi(defaultClient);
    UUID projectId = UUID.fromString("bc3f7dad-5544-468c-8573-3ef04d55463e"); // UUID | The project id
    String trainingKey = "{API Key}"; // String | 
    ImageTagCreateBatch imageTagCreateBatch = new ImageTagCreateBatch(); // ImageTagCreateBatch | Batch of image tags. Limited to 128 tags per batch
    try {
      ImageTagCreateSummary result = apiInstance.postImageTags(projectId, trainingKey, imageTagCreateBatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageApiApi#postImageTags");
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
| **projectId** | **UUID**| The project id | |
| **trainingKey** | **String**|  | |
| **imageTagCreateBatch** | [**ImageTagCreateBatch**](ImageTagCreateBatch.md)| Batch of image tags. Limited to 128 tags per batch | |

### Return type

[**ImageTagCreateSummary**](ImageTagCreateSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

