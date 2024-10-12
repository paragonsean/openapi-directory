# ImagesApi

All URIs are relative to *http://slicebox.local/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**imagesDeletePost**](ImagesApi.md#imagesDeletePost) | **POST** /images/delete |  |
| [**imagesExportGet**](ImagesApi.md#imagesExportGet) | **GET** /images/export |  |
| [**imagesExportPost**](ImagesApi.md#imagesExportPost) | **POST** /images/export |  |
| [**imagesIdAnonymizePut_0**](ImagesApi.md#imagesIdAnonymizePut_0) | **PUT** /images/{id}/anonymize |  |
| [**imagesIdAnonymizedPost_0**](ImagesApi.md#imagesIdAnonymizedPost_0) | **POST** /images/{id}/anonymized |  |
| [**imagesIdAttributesGet**](ImagesApi.md#imagesIdAttributesGet) | **GET** /images/{id}/attributes |  |
| [**imagesIdDelete**](ImagesApi.md#imagesIdDelete) | **DELETE** /images/{id} |  |
| [**imagesIdGet**](ImagesApi.md#imagesIdGet) | **GET** /images/{id} |  |
| [**imagesIdImageinformationGet**](ImagesApi.md#imagesIdImageinformationGet) | **GET** /images/{id}/imageinformation |  |
| [**imagesIdModifyPut**](ImagesApi.md#imagesIdModifyPut) | **PUT** /images/{id}/modify |  |
| [**imagesIdPngGet**](ImagesApi.md#imagesIdPngGet) | **GET** /images/{id}/png |  |
| [**imagesJpegPost**](ImagesApi.md#imagesJpegPost) | **POST** /images/jpeg |  |
| [**imagesPost**](ImagesApi.md#imagesPost) | **POST** /images |  |


<a id="imagesDeletePost"></a>
# **imagesDeletePost**
> imagesDeletePost(imageIDs)



bulk delete a sequence of images according to the supplied image IDs. This is the same as a sequence of DELETE requests to /images/{id}

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
    defaultClient.setBasePath("http://slicebox.local/api");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    List<Long> imageIDs = Arrays.asList(); // List<Long> | IDs of images to delete
    try {
      apiInstance.imagesDeletePost(imageIDs);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesDeletePost");
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
| **imageIDs** | [**List&lt;Long&gt;**](Long.md)| IDs of images to delete | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Images deleted |  -  |

<a id="imagesExportGet"></a>
# **imagesExportGet**
> imagesExportGet(id)



download the export set with the supplied export set ID as a zip archive

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
    defaultClient.setBasePath("http://slicebox.local/api");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    Long id = 56L; // Long | ID of export set to download
    try {
      apiInstance.imagesExportGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesExportGet");
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
| **id** | **Long**| ID of export set to download | |

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
| **200** | zip archive of images |  -  |

<a id="imagesExportPost"></a>
# **imagesExportPost**
> ExportSetId imagesExportPost(imageIds)



create an export set, a group of image IDs of images to export. The export set will contain the selected images. The export set is available for download 12 hours before it is automatically deleted.

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
    defaultClient.setBasePath("http://slicebox.local/api");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    List<Long> imageIds = Arrays.asList(); // List<Long> | ids of images to export
    try {
      ExportSetId result = apiInstance.imagesExportPost(imageIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesExportPost");
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
| **imageIds** | [**List&lt;Long&gt;**](Long.md)| ids of images to export | |

### Return type

[**ExportSetId**](ExportSetId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ID of created export set. To be used with the associated GET method for downloading. |  -  |
| **201** | if the supplied list of image ids is empty or no if images could be found |  -  |

<a id="imagesIdAnonymizePut_0"></a>
# **imagesIdAnonymizePut_0**
> Image imagesIdAnonymizePut_0(id, tagValues)



delete the selected image and replace it with an anonymized version

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
    defaultClient.setBasePath("http://slicebox.local/api");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    Long id = 56L; // Long | ID of image to anonymize
    AnonymizationData tagValues = new AnonymizationData(); // AnonymizationData | specification of values for anonymous DICOM attributes
    try {
      Image result = apiInstance.imagesIdAnonymizePut_0(id, tagValues);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesIdAnonymizePut_0");
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
| **id** | **Long**| ID of image to anonymize | |
| **tagValues** | [**AnonymizationData**](AnonymizationData.md)| specification of values for anonymous DICOM attributes | |

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the newly created anonymous image |  -  |
| **404** | image or corresponding dataset not found |  -  |

<a id="imagesIdAnonymizedPost_0"></a>
# **imagesIdAnonymizedPost_0**
> imagesIdAnonymizedPost_0(id, tagValues)



get an anonymized version of the image with the supplied ID

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
    defaultClient.setBasePath("http://slicebox.local/api");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    Long id = 56L; // Long | ID of image for which to get anonymized dataset
    AnonymizationData tagValues = new AnonymizationData(); // AnonymizationData | specification of values for anonymous DICOM attributes
    try {
      apiInstance.imagesIdAnonymizedPost_0(id, tagValues);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesIdAnonymizedPost_0");
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
| **id** | **Long**| ID of image for which to get anonymized dataset | |
| **tagValues** | [**AnonymizationData**](AnonymizationData.md)| specification of values for anonymous DICOM attributes | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | binary data of anonymized dataset |  -  |
| **404** | if no image was found for the supplied image ID |  -  |

<a id="imagesIdAttributesGet"></a>
# **imagesIdAttributesGet**
> List&lt;ImageAttribute&gt; imagesIdAttributesGet(id)



list all DICOM attributes of the dataset corresponding to the supplied image ID

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
    defaultClient.setBasePath("http://slicebox.local/api");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    Long id = 56L; // Long | ID of image
    try {
      List<ImageAttribute> result = apiInstance.imagesIdAttributesGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesIdAttributesGet");
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
| **id** | **Long**| ID of image | |

### Return type

[**List&lt;ImageAttribute&gt;**](ImageAttribute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of DICOM attributes |  -  |
| **404** | if no image was found for the supplied image ID |  -  |

<a id="imagesIdDelete"></a>
# **imagesIdDelete**
> imagesIdDelete(id)



Delete the image with the supplied ID

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
    defaultClient.setBasePath("http://slicebox.local/api");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    Long id = 56L; // Long | ID of image
    try {
      apiInstance.imagesIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesIdDelete");
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
| **id** | **Long**| ID of image | |

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
| **204** | image deleted |  -  |

<a id="imagesIdGet"></a>
# **imagesIdGet**
> imagesIdGet(id)



fetch dataset corresponding to the supplied image ID

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
    defaultClient.setBasePath("http://slicebox.local/api");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    Long id = 56L; // Long | ID of image
    try {
      apiInstance.imagesIdGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesIdGet");
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
| **id** | **Long**| ID of image | |

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
| **200** | binary data of dataset |  -  |
| **404** | if no image was found for the supplied image ID |  -  |

<a id="imagesIdImageinformationGet"></a>
# **imagesIdImageinformationGet**
> ImageInformation imagesIdImageinformationGet(id)



get basic information about the pixel data of an image

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
    defaultClient.setBasePath("http://slicebox.local/api");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    Long id = 56L; // Long | ID of image
    try {
      ImageInformation result = apiInstance.imagesIdImageinformationGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesIdImageinformationGet");
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
| **id** | **Long**| ID of image | |

### Return type

[**ImageInformation**](ImageInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | basic information about the pixeldata of an image |  -  |
| **404** | if no image was found for the supplied image ID |  -  |

<a id="imagesIdModifyPut"></a>
# **imagesIdModifyPut**
> imagesIdModifyPut(id, tagPathValueMappings)



modify and/or insert image attributes according to the input tagpath-value mappings

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
    defaultClient.setBasePath("http://slicebox.local/api");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    Long id = 56L; // Long | ID of image to modify
    List<TagMapping> tagPathValueMappings = Arrays.asList(); // List<TagMapping> | specification of tag paths and corresponding values to insert or modify
    try {
      apiInstance.imagesIdModifyPut(id, tagPathValueMappings);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesIdModifyPut");
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
| **id** | **Long**| ID of image to modify | |
| **tagPathValueMappings** | [**List&lt;TagMapping&gt;**](TagMapping.md)| specification of tag paths and corresponding values to insert or modify | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | image attributes successfully modified |  -  |

<a id="imagesIdPngGet"></a>
# **imagesIdPngGet**
> imagesIdPngGet(id, framenumber, windowmin, windowmax, imageheight)



get a PNG image representation of the image corresponding to the supplied ID

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
    defaultClient.setBasePath("http://slicebox.local/api");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    Long id = 56L; // Long | ID of image
    Integer framenumber = 1; // Integer | frame/slice to show
    Integer windowmin = 0; // Integer | intensity window minimum value. If not specified or set to zero, windowing will be selected from relevant DICOM attributes
    Integer windowmax = 0; // Integer | intensity window maximum value. If not specified or set to zero, windowing will be selected from relevant DICOM attributes
    Integer imageheight = 0; // Integer | height of PNG image. If not specified or set to zero, the image height will equal that of the data
    try {
      apiInstance.imagesIdPngGet(id, framenumber, windowmin, windowmax, imageheight);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesIdPngGet");
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
| **id** | **Long**| ID of image | |
| **framenumber** | **Integer**| frame/slice to show | [optional] [default to 1] |
| **windowmin** | **Integer**| intensity window minimum value. If not specified or set to zero, windowing will be selected from relevant DICOM attributes | [optional] [default to 0] |
| **windowmax** | **Integer**| intensity window maximum value. If not specified or set to zero, windowing will be selected from relevant DICOM attributes | [optional] [default to 0] |
| **imageheight** | **Integer**| height of PNG image. If not specified or set to zero, the image height will equal that of the data | [optional] [default to 0] |

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
| **200** | image data |  -  |
| **404** | if no image was found for the supplied image ID |  -  |
| **501** | if the system is not capable of creating an image representation of the data |  -  |

<a id="imagesJpegPost"></a>
# **imagesJpegPost**
> Image imagesJpegPost(studyid, jpegBytes, description)



add a JPEG image to slicebox. The image data will be wrapped in a DICOM file and added as a new series belonging to the study with the supplied ID

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
    defaultClient.setBasePath("http://slicebox.local/api");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    Long studyid = 56L; // Long | ID of study to add new series to
    Object jpegBytes = null; // Object | The jpeg image data
    String description = "description_example"; // String | DICOM series description of the resulting secondary capture series
    try {
      Image result = apiInstance.imagesJpegPost(studyid, jpegBytes, description);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesJpegPost");
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
| **studyid** | **Long**| ID of study to add new series to | |
| **jpegBytes** | **Object**| The jpeg image data | |
| **description** | **String**| DICOM series description of the resulting secondary capture series | [optional] |

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | meta data for added dataset on the image level of the DICOM hierarchy |  -  |

<a id="imagesPost"></a>
# **imagesPost**
> Image imagesPost(imagesPostRequest)



add a DICOM dataset to slicebox

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
    defaultClient.setBasePath("http://slicebox.local/api");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    ImagesPostRequest imagesPostRequest = new ImagesPostRequest(); // ImagesPostRequest | 
    try {
      Image result = apiInstance.imagesPost(imagesPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesPost");
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
| **imagesPostRequest** | [**ImagesPostRequest**](ImagesPostRequest.md)|  | |

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | meta data for added dataset on the image level of the DICOM hierarchy. Status code 200 signifies that this image was already present in the slicebox database. |  -  |
| **201** | meta data for added dataset on the image level of the DICOM hierarchy |  -  |

