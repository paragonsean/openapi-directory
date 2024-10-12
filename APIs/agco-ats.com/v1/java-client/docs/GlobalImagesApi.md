# GlobalImagesApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**globalImagesDeleteFile**](GlobalImagesApi.md#globalImagesDeleteFile) | **DELETE** /api/v2/GlobalImages/{ID} | Mark a file as &#39;Removed&#39;. Disables download of the image and hides metadata from GET all method |
| [**globalImagesGetGlobalImage**](GlobalImagesApi.md#globalImagesGetGlobalImage) | **GET** /api/v2/GlobalImages/{ID} | Gets a GlobalImage&#39;s metadata. |
| [**globalImagesGetGlobalImageContents**](GlobalImagesApi.md#globalImagesGetGlobalImageContents) | **GET** /api/v2/GlobalImages/{ID}/ImageContents | Download the contents of a GlobalImage. The current State of the GlobalImage should be &#39;Available&#39;. |
| [**globalImagesGetGlobalImages**](GlobalImagesApi.md#globalImagesGetGlobalImages) | **GET** /api/v2/GlobalImages | Get a paged response of GlobalImage. |
| [**globalImagesPostGlobalImage**](GlobalImagesApi.md#globalImagesPostGlobalImage) | **POST** /api/v2/GlobalImages | Create the metadata for a GlobalImage before uploading. The State should be &#39;Created&#39;. |
| [**globalImagesPutGlobalImage**](GlobalImagesApi.md#globalImagesPutGlobalImage) | **PUT** /api/v2/GlobalImages/{ID} | Update the metadata for an image. |
| [**globalImagesPutGlobalImageContents**](GlobalImagesApi.md#globalImagesPutGlobalImageContents) | **PUT** /api/v2/GlobalImages/{ID}/ImageContents | Upload the contents of a GlobalImage. The current State of the File for the GlobalImage should be &#39;Created&#39;. |


<a id="globalImagesDeleteFile"></a>
# **globalImagesDeleteFile**
> globalImagesDeleteFile(ID)

Mark a file as &#39;Removed&#39;. Disables download of the image and hides metadata from GET all method

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    GlobalImagesApi apiInstance = new GlobalImagesApi(defaultClient);
    String ID = "ID_example"; // String | The GlobalImage's id.
    try {
      apiInstance.globalImagesDeleteFile(ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalImagesApi#globalImagesDeleteFile");
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
| **ID** | **String**| The GlobalImage&#39;s id. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="globalImagesGetGlobalImage"></a>
# **globalImagesGetGlobalImage**
> GlobalResourcesSharedModelsGlobalImage globalImagesGetGlobalImage(ID)

Gets a GlobalImage&#39;s metadata.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    GlobalImagesApi apiInstance = new GlobalImagesApi(defaultClient);
    String ID = "ID_example"; // String | The GlobalImage's id.
    try {
      GlobalResourcesSharedModelsGlobalImage result = apiInstance.globalImagesGetGlobalImage(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalImagesApi#globalImagesGetGlobalImage");
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
| **ID** | **String**| The GlobalImage&#39;s id. | |

### Return type

[**GlobalResourcesSharedModelsGlobalImage**](GlobalResourcesSharedModelsGlobalImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="globalImagesGetGlobalImageContents"></a>
# **globalImagesGetGlobalImageContents**
> Object globalImagesGetGlobalImageContents(ID, isFullImage)

Download the contents of a GlobalImage. The current State of the GlobalImage should be &#39;Available&#39;.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    GlobalImagesApi apiInstance = new GlobalImagesApi(defaultClient);
    String ID = "ID_example"; // String | The global image metadata id.
    Boolean isFullImage = true; // Boolean | Indicated whether to download the full image or the thumbnail. Defaults to 'true'.
    try {
      Object result = apiInstance.globalImagesGetGlobalImageContents(ID, isFullImage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalImagesApi#globalImagesGetGlobalImageContents");
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
| **ID** | **String**| The global image metadata id. | |
| **isFullImage** | **Boolean**| Indicated whether to download the full image or the thumbnail. Defaults to &#39;true&#39;. | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="globalImagesGetGlobalImages"></a>
# **globalImagesGetGlobalImages**
> APIIPagedResponseGlobalResourcesSharedModelsGlobalImage globalImagesGetGlobalImages(search, categoryId, publisher, includeDeleted, limit, offset)

Get a paged response of GlobalImage.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    GlobalImagesApi apiInstance = new GlobalImagesApi(defaultClient);
    String search = "search_example"; // String | Optional. Searches for matching global images with the matching Category Name, Publisher or Description
    String categoryId = "categoryId_example"; // String | 
    String publisher = "publisher_example"; // String | 
    Boolean includeDeleted = true; // Boolean | Indicates whether to include GlobalImages marked as removed.
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIIPagedResponseGlobalResourcesSharedModelsGlobalImage result = apiInstance.globalImagesGetGlobalImages(search, categoryId, publisher, includeDeleted, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalImagesApi#globalImagesGetGlobalImages");
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
| **search** | **String**| Optional. Searches for matching global images with the matching Category Name, Publisher or Description | [optional] |
| **categoryId** | **String**|  | [optional] |
| **publisher** | **String**|  | [optional] |
| **includeDeleted** | **Boolean**| Indicates whether to include GlobalImages marked as removed. | [optional] |
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIIPagedResponseGlobalResourcesSharedModelsGlobalImage**](APIIPagedResponseGlobalResourcesSharedModelsGlobalImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="globalImagesPostGlobalImage"></a>
# **globalImagesPostGlobalImage**
> String globalImagesPostGlobalImage(globalResourcesSharedModelsGlobalImage, overridePublisherOrDate)

Create the metadata for a GlobalImage before uploading. The State should be &#39;Created&#39;.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    GlobalImagesApi apiInstance = new GlobalImagesApi(defaultClient);
    GlobalResourcesSharedModelsGlobalImage globalResourcesSharedModelsGlobalImage = new GlobalResourcesSharedModelsGlobalImage(); // GlobalResourcesSharedModelsGlobalImage | The file's metadata.
    Boolean overridePublisherOrDate = true; // Boolean | Whether to set the publisher and date to the provided values.
    try {
      String result = apiInstance.globalImagesPostGlobalImage(globalResourcesSharedModelsGlobalImage, overridePublisherOrDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalImagesApi#globalImagesPostGlobalImage");
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
| **globalResourcesSharedModelsGlobalImage** | [**GlobalResourcesSharedModelsGlobalImage**](GlobalResourcesSharedModelsGlobalImage.md)| The file&#39;s metadata. | |
| **overridePublisherOrDate** | **Boolean**| Whether to set the publisher and date to the provided values. | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="globalImagesPutGlobalImage"></a>
# **globalImagesPutGlobalImage**
> globalImagesPutGlobalImage(ID, globalResourcesSharedModelsGlobalImage, overridePublisherOrDate)

Update the metadata for an image.

Update the metadata for an image. Size may not be modified by the client.                   Set status to &#39;Available&#39; to publish an image. Both the image and thumbnail must be uploaded.                  Set status to &#39;Created&#39; to reset an image&#39;s contents and re-upload.                   A file may only be &#39;Removed&#39; by the DELETE method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    GlobalImagesApi apiInstance = new GlobalImagesApi(defaultClient);
    String ID = "ID_example"; // String | The GlobalImage's id.
    GlobalResourcesSharedModelsGlobalImage globalResourcesSharedModelsGlobalImage = new GlobalResourcesSharedModelsGlobalImage(); // GlobalResourcesSharedModelsGlobalImage | The GlobalImage's metadata
    Boolean overridePublisherOrDate = true; // Boolean | Whether to set the publisher and date to the provided values.
    try {
      apiInstance.globalImagesPutGlobalImage(ID, globalResourcesSharedModelsGlobalImage, overridePublisherOrDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalImagesApi#globalImagesPutGlobalImage");
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
| **ID** | **String**| The GlobalImage&#39;s id. | |
| **globalResourcesSharedModelsGlobalImage** | [**GlobalResourcesSharedModelsGlobalImage**](GlobalResourcesSharedModelsGlobalImage.md)| The GlobalImage&#39;s metadata | |
| **overridePublisherOrDate** | **Boolean**| Whether to set the publisher and date to the provided values. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="globalImagesPutGlobalImageContents"></a>
# **globalImagesPutGlobalImageContents**
> Object globalImagesPutGlobalImageContents(ID, isFullImage)

Upload the contents of a GlobalImage. The current State of the File for the GlobalImage should be &#39;Created&#39;.

Both the image and thumbnail must be uploaded.                  Set isFullImage &#x3D; &#39;True&#39; for Full Image, isFullImage &#x3D; &#39;False&#39; for Thumbnail

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    GlobalImagesApi apiInstance = new GlobalImagesApi(defaultClient);
    String ID = "ID_example"; // String | The global image metadata id.
    Boolean isFullImage = true; // Boolean | Indicated whether this is the full image or the thumbnail. Defaults to 'true'.
    try {
      Object result = apiInstance.globalImagesPutGlobalImageContents(ID, isFullImage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalImagesApi#globalImagesPutGlobalImageContents");
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
| **ID** | **String**| The global image metadata id. | |
| **isFullImage** | **Boolean**| Indicated whether this is the full image or the thumbnail. Defaults to &#39;true&#39;. | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

