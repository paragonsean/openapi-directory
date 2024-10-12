# ImagesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addImage**](ImagesApi.md#addImage) | **POST** /images | Submit a new image for analysis by the engine |
| [**deleteImage**](ImagesApi.md#deleteImage) | **DELETE** /images/{imageDigest} | Delete an image analysis |
| [**deleteImageByImageId**](ImagesApi.md#deleteImageByImageId) | **DELETE** /images/by_id/{imageId} | Delete image by docker imageId |
| [**deleteImagesAsync**](ImagesApi.md#deleteImagesAsync) | **DELETE** /images | Bulk mark images for deletion |
| [**getImage**](ImagesApi.md#getImage) | **GET** /images/{imageDigest} | Get image metadata |
| [**getImageByImageId**](ImagesApi.md#getImageByImageId) | **GET** /images/by_id/{imageId} | Lookup image by docker imageId |
| [**getImageContentByType**](ImagesApi.md#getImageContentByType) | **GET** /images/{imageDigest}/content/{ctype} | Get the content of an image by type |
| [**getImageContentByTypeFiles**](ImagesApi.md#getImageContentByTypeFiles) | **GET** /images/{imageDigest}/content/files | Get the content of an image by type files |
| [**getImageContentByTypeImageId**](ImagesApi.md#getImageContentByTypeImageId) | **GET** /images/by_id/{imageId}/content/{ctype} | Get the content of an image by type |
| [**getImageContentByTypeImageIdFiles**](ImagesApi.md#getImageContentByTypeImageIdFiles) | **GET** /images/by_id/{imageId}/content/files | Get the content of an image by type files |
| [**getImageContentByTypeImageIdJavapackage**](ImagesApi.md#getImageContentByTypeImageIdJavapackage) | **GET** /images/by_id/{imageId}/content/java | Get the content of an image by type java |
| [**getImageContentByTypeJavapackage**](ImagesApi.md#getImageContentByTypeJavapackage) | **GET** /images/{imageDigest}/content/java | Get the content of an image by type java |
| [**getImageContentByTypeMalware**](ImagesApi.md#getImageContentByTypeMalware) | **GET** /images/{imageDigest}/content/malware | Get the content of an image by type malware |
| [**getImageMetadataByType**](ImagesApi.md#getImageMetadataByType) | **GET** /images/{imageDigest}/metadata/{mtype} | Get the metadata of an image by type |
| [**getImagePolicyCheck**](ImagesApi.md#getImagePolicyCheck) | **GET** /images/{imageDigest}/check | Check policy evaluation status for image |
| [**getImagePolicyCheckByImageId**](ImagesApi.md#getImagePolicyCheckByImageId) | **GET** /images/by_id/{imageId}/check | Check policy evaluation status for image |
| [**getImageSbomNative**](ImagesApi.md#getImageSbomNative) | **GET** /images/{imageDigest}/sboms/native | Get image sbom in the native Anchore format |
| [**getImageVulnerabilitiesByType**](ImagesApi.md#getImageVulnerabilitiesByType) | **GET** /images/{imageDigest}/vuln/{vtype} | Get vulnerabilities by type |
| [**getImageVulnerabilitiesByTypeImageId**](ImagesApi.md#getImageVulnerabilitiesByTypeImageId) | **GET** /images/by_id/{imageId}/vuln/{vtype} | Get vulnerabilities by type |
| [**getImageVulnerabilityTypes**](ImagesApi.md#getImageVulnerabilityTypes) | **GET** /images/{imageDigest}/vuln | Get vulnerability types |
| [**getImageVulnerabilityTypesByImageId**](ImagesApi.md#getImageVulnerabilityTypesByImageId) | **GET** /images/by_id/{imageId}/vuln | Get vulnerability types |
| [**listImageContent**](ImagesApi.md#listImageContent) | **GET** /images/{imageDigest}/content | List image content types |
| [**listImageContentByImageid**](ImagesApi.md#listImageContentByImageid) | **GET** /images/by_id/{imageId}/content | List image content types |
| [**listImageMetadata**](ImagesApi.md#listImageMetadata) | **GET** /images/{imageDigest}/metadata | List image metadata types |
| [**listImages**](ImagesApi.md#listImages) | **GET** /images | List all visible images |


<a id="addImage"></a>
# **addImage**
> List&lt;AnchoreImage&gt; addImage(imageAnalysisRequest, force, autosubscribe, xAnchoreAccount)

Submit a new image for analysis by the engine

Creates a new analysis task that is executed asynchronously

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    ImageAnalysisRequest imageAnalysisRequest = new ImageAnalysisRequest(); // ImageAnalysisRequest | 
    Boolean force = true; // Boolean | Override any existing entry in the system
    Boolean autosubscribe = true; // Boolean | Instruct engine to automatically begin watching the added tag for updates from registry
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<AnchoreImage> result = apiInstance.addImage(imageAnalysisRequest, force, autosubscribe, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#addImage");
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
| **imageAnalysisRequest** | [**ImageAnalysisRequest**](ImageAnalysisRequest.md)|  | |
| **force** | **Boolean**| Override any existing entry in the system | [optional] |
| **autosubscribe** | **Boolean**| Instruct engine to automatically begin watching the added tag for updates from registry | [optional] |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**List&lt;AnchoreImage&gt;**](AnchoreImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully added image to analysis queue |  -  |
| **500** | Internal Error |  -  |

<a id="deleteImage"></a>
# **deleteImage**
> DeleteImageResponse deleteImage(imageDigest, force, xAnchoreAccount)

Delete an image analysis

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageDigest = "imageDigest_example"; // String | 
    Boolean force = true; // Boolean | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      DeleteImageResponse result = apiInstance.deleteImage(imageDigest, force, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#deleteImage");
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
| **imageDigest** | **String**|  | |
| **force** | **Boolean**|  | [optional] |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**DeleteImageResponse**](DeleteImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Image deletion success |  -  |

<a id="deleteImageByImageId"></a>
# **deleteImageByImageId**
> DeleteImageResponse deleteImageByImageId(imageId, force, xAnchoreAccount)

Delete image by docker imageId

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageId = "imageId_example"; // String | 
    Boolean force = true; // Boolean | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      DeleteImageResponse result = apiInstance.deleteImageByImageId(imageId, force, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#deleteImageByImageId");
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
| **imageId** | **String**|  | |
| **force** | **Boolean**|  | [optional] |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**DeleteImageResponse**](DeleteImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Image deletion success |  -  |
| **500** | Internal error |  -  |

<a id="deleteImagesAsync"></a>
# **deleteImagesAsync**
> List&lt;DeleteImageResponse&gt; deleteImagesAsync(imageDigests, force, xAnchoreAccount)

Bulk mark images for deletion

Delete analysis for image digests in the list asynchronously

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    List<String> imageDigests = Arrays.asList(); // List<String> | 
    Boolean force = true; // Boolean | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<DeleteImageResponse> result = apiInstance.deleteImagesAsync(imageDigests, force, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#deleteImagesAsync");
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
| **imageDigests** | [**List&lt;String&gt;**](String.md)|  | |
| **force** | **Boolean**|  | [optional] |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**List&lt;DeleteImageResponse&gt;**](DeleteImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **500** | Internal Error |  -  |

<a id="getImage"></a>
# **getImage**
> List&lt;AnchoreImage&gt; getImage(imageDigest, xAnchoreAccount)

Get image metadata

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageDigest = "imageDigest_example"; // String | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<AnchoreImage> result = apiInstance.getImage(imageDigest, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImage");
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
| **imageDigest** | **String**|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**List&lt;AnchoreImage&gt;**](AnchoreImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Image lookup success |  -  |
| **500** | Internal error |  -  |

<a id="getImageByImageId"></a>
# **getImageByImageId**
> List&lt;AnchoreImage&gt; getImageByImageId(imageId, xAnchoreAccount)

Lookup image by docker imageId

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageId = "imageId_example"; // String | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<AnchoreImage> result = apiInstance.getImageByImageId(imageId, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImageByImageId");
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
| **imageId** | **String**|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**List&lt;AnchoreImage&gt;**](AnchoreImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Image lookup success |  -  |
| **500** | Internal error |  -  |

<a id="getImageContentByType"></a>
# **getImageContentByType**
> ContentPackageResponse getImageContentByType(imageDigest, ctype, xAnchoreAccount)

Get the content of an image by type

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageDigest = "imageDigest_example"; // String | 
    String ctype = "ctype_example"; // String | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      ContentPackageResponse result = apiInstance.getImageContentByType(imageDigest, ctype, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImageContentByType");
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
| **imageDigest** | **String**|  | |
| **ctype** | **String**|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**ContentPackageResponse**](ContentPackageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Content of specified type from the image |  -  |
| **500** | Internal error |  -  |

<a id="getImageContentByTypeFiles"></a>
# **getImageContentByTypeFiles**
> ContentFilesResponse getImageContentByTypeFiles(imageDigest, xAnchoreAccount)

Get the content of an image by type files

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageDigest = "imageDigest_example"; // String | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      ContentFilesResponse result = apiInstance.getImageContentByTypeFiles(imageDigest, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImageContentByTypeFiles");
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
| **imageDigest** | **String**|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**ContentFilesResponse**](ContentFilesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Content of specified type from the image |  -  |
| **500** | Internal error |  -  |

<a id="getImageContentByTypeImageId"></a>
# **getImageContentByTypeImageId**
> ContentPackageResponse getImageContentByTypeImageId(imageId, ctype, xAnchoreAccount)

Get the content of an image by type

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageId = "imageId_example"; // String | 
    String ctype = "ctype_example"; // String | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      ContentPackageResponse result = apiInstance.getImageContentByTypeImageId(imageId, ctype, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImageContentByTypeImageId");
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
| **imageId** | **String**|  | |
| **ctype** | **String**|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**ContentPackageResponse**](ContentPackageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Content of specified type from the image |  -  |
| **500** | Internal error |  -  |

<a id="getImageContentByTypeImageIdFiles"></a>
# **getImageContentByTypeImageIdFiles**
> ContentFilesResponse getImageContentByTypeImageIdFiles(imageId, xAnchoreAccount)

Get the content of an image by type files

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageId = "imageId_example"; // String | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      ContentFilesResponse result = apiInstance.getImageContentByTypeImageIdFiles(imageId, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImageContentByTypeImageIdFiles");
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
| **imageId** | **String**|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**ContentFilesResponse**](ContentFilesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Content of specified type from the image |  -  |
| **500** | Internal error |  -  |

<a id="getImageContentByTypeImageIdJavapackage"></a>
# **getImageContentByTypeImageIdJavapackage**
> ContentJAVAPackageResponse getImageContentByTypeImageIdJavapackage(imageId, xAnchoreAccount)

Get the content of an image by type java

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageId = "imageId_example"; // String | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      ContentJAVAPackageResponse result = apiInstance.getImageContentByTypeImageIdJavapackage(imageId, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImageContentByTypeImageIdJavapackage");
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
| **imageId** | **String**|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**ContentJAVAPackageResponse**](ContentJAVAPackageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Content of specified type from the image |  -  |
| **500** | Internal error |  -  |

<a id="getImageContentByTypeJavapackage"></a>
# **getImageContentByTypeJavapackage**
> ContentJAVAPackageResponse getImageContentByTypeJavapackage(imageDigest, xAnchoreAccount)

Get the content of an image by type java

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageDigest = "imageDigest_example"; // String | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      ContentJAVAPackageResponse result = apiInstance.getImageContentByTypeJavapackage(imageDigest, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImageContentByTypeJavapackage");
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
| **imageDigest** | **String**|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**ContentJAVAPackageResponse**](ContentJAVAPackageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Content of specified type from the image |  -  |
| **500** | Internal error |  -  |

<a id="getImageContentByTypeMalware"></a>
# **getImageContentByTypeMalware**
> ContentMalwareResponse getImageContentByTypeMalware(imageDigest, xAnchoreAccount)

Get the content of an image by type malware

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageDigest = "imageDigest_example"; // String | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      ContentMalwareResponse result = apiInstance.getImageContentByTypeMalware(imageDigest, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImageContentByTypeMalware");
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
| **imageDigest** | **String**|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**ContentMalwareResponse**](ContentMalwareResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Content of specified type from the image |  -  |
| **500** | Internal error |  -  |

<a id="getImageMetadataByType"></a>
# **getImageMetadataByType**
> MetadataResponse getImageMetadataByType(imageDigest, mtype, xAnchoreAccount)

Get the metadata of an image by type

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageDigest = "imageDigest_example"; // String | 
    String mtype = "mtype_example"; // String | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      MetadataResponse result = apiInstance.getImageMetadataByType(imageDigest, mtype, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImageMetadataByType");
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
| **imageDigest** | **String**|  | |
| **mtype** | **String**|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**MetadataResponse**](MetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metadata of specified type from the image |  -  |
| **500** | Internal error |  -  |

<a id="getImagePolicyCheck"></a>
# **getImagePolicyCheck**
> List&lt;Object&gt; getImagePolicyCheck(imageDigest, tag, policyId, detail, history, interactive, xAnchoreAccount)

Check policy evaluation status for image

Get the policy evaluation for the given image

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageDigest = "imageDigest_example"; // String | 
    String tag = "tag_example"; // String | 
    String policyId = "policyId_example"; // String | 
    Boolean detail = true; // Boolean | 
    Boolean history = true; // Boolean | 
    Boolean interactive = true; // Boolean | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<Object> result = apiInstance.getImagePolicyCheck(imageDigest, tag, policyId, detail, history, interactive, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImagePolicyCheck");
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
| **imageDigest** | **String**|  | |
| **tag** | **String**|  | |
| **policyId** | **String**|  | [optional] |
| **detail** | **Boolean**|  | [optional] |
| **history** | **Boolean**|  | [optional] |
| **interactive** | **Boolean**|  | [optional] |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

**List&lt;Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Policy evaluation success |  -  |
| **500** | Internal Error |  -  |

<a id="getImagePolicyCheckByImageId"></a>
# **getImagePolicyCheckByImageId**
> List&lt;Object&gt; getImagePolicyCheckByImageId(imageId, tag, policyId, detail, history, xAnchoreAccount)

Check policy evaluation status for image

Get the policy evaluation for the given image

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageId = "imageId_example"; // String | 
    String tag = "tag_example"; // String | 
    String policyId = "policyId_example"; // String | 
    Boolean detail = true; // Boolean | 
    Boolean history = true; // Boolean | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<Object> result = apiInstance.getImagePolicyCheckByImageId(imageId, tag, policyId, detail, history, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImagePolicyCheckByImageId");
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
| **imageId** | **String**|  | |
| **tag** | **String**|  | |
| **policyId** | **String**|  | [optional] |
| **detail** | **Boolean**|  | [optional] |
| **history** | **Boolean**|  | [optional] |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

**List&lt;Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Policy evaluation success |  -  |
| **500** | Internal Error |  -  |

<a id="getImageSbomNative"></a>
# **getImageSbomNative**
> File getImageSbomNative(imageDigest, xAnchoreAccount)

Get image sbom in the native Anchore format

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageDigest = "imageDigest_example"; // String | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      File result = apiInstance.getImageSbomNative(imageDigest, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImageSbomNative");
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
| **imageDigest** | **String**|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/gzip

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Image lookup success |  -  |
| **500** | Internal error |  -  |

<a id="getImageVulnerabilitiesByType"></a>
# **getImageVulnerabilitiesByType**
> VulnerabilityResponse getImageVulnerabilitiesByType(imageDigest, vtype, forceRefresh, vendorOnly, xAnchoreAccount)

Get vulnerabilities by type

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageDigest = "imageDigest_example"; // String | 
    String vtype = "vtype_example"; // String | 
    Boolean forceRefresh = true; // Boolean | 
    Boolean vendorOnly = true; // Boolean | Filter results to include only vulnerabilities that are not marked as invalid by upstream OS vendor data. When set to true, it will filter out all vulnerabilities where `will_not_fix` is False. If false all vulnerabilities are returned regardless of `will_not_fix`
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      VulnerabilityResponse result = apiInstance.getImageVulnerabilitiesByType(imageDigest, vtype, forceRefresh, vendorOnly, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImageVulnerabilitiesByType");
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
| **imageDigest** | **String**|  | |
| **vtype** | **String**|  | |
| **forceRefresh** | **Boolean**|  | [optional] |
| **vendorOnly** | **Boolean**| Filter results to include only vulnerabilities that are not marked as invalid by upstream OS vendor data. When set to true, it will filter out all vulnerabilities where &#x60;will_not_fix&#x60; is False. If false all vulnerabilities are returned regardless of &#x60;will_not_fix&#x60; | [optional] |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**VulnerabilityResponse**](VulnerabilityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Vulnerability listing for the image |  -  |
| **500** | Internal Error |  -  |

<a id="getImageVulnerabilitiesByTypeImageId"></a>
# **getImageVulnerabilitiesByTypeImageId**
> VulnerabilityResponse getImageVulnerabilitiesByTypeImageId(imageId, vtype, xAnchoreAccount)

Get vulnerabilities by type

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageId = "imageId_example"; // String | 
    String vtype = "vtype_example"; // String | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      VulnerabilityResponse result = apiInstance.getImageVulnerabilitiesByTypeImageId(imageId, vtype, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImageVulnerabilitiesByTypeImageId");
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
| **imageId** | **String**|  | |
| **vtype** | **String**|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**VulnerabilityResponse**](VulnerabilityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Vulnerability listing for the image |  -  |
| **500** | Internal Error |  -  |

<a id="getImageVulnerabilityTypes"></a>
# **getImageVulnerabilityTypes**
> List&lt;String&gt; getImageVulnerabilityTypes(imageDigest, xAnchoreAccount)

Get vulnerability types

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageDigest = "imageDigest_example"; // String | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<String> result = apiInstance.getImageVulnerabilityTypes(imageDigest, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImageVulnerabilityTypes");
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
| **imageDigest** | **String**|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Vulnerability listing for the image |  -  |
| **500** | Internal Error |  -  |

<a id="getImageVulnerabilityTypesByImageId"></a>
# **getImageVulnerabilityTypesByImageId**
> List&lt;String&gt; getImageVulnerabilityTypesByImageId(imageId, xAnchoreAccount)

Get vulnerability types

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageId = "imageId_example"; // String | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<String> result = apiInstance.getImageVulnerabilityTypesByImageId(imageId, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImageVulnerabilityTypesByImageId");
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
| **imageId** | **String**|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Vulnerability listing for the image |  -  |
| **500** | Internal Error |  -  |

<a id="listImageContent"></a>
# **listImageContent**
> List&lt;String&gt; listImageContent(imageDigest, xAnchoreAccount)

List image content types

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageDigest = "imageDigest_example"; // String | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<String> result = apiInstance.listImageContent(imageDigest, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#listImageContent");
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
| **imageDigest** | **String**|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Content listing for the image |  -  |
| **500** | Internal Error |  -  |

<a id="listImageContentByImageid"></a>
# **listImageContentByImageid**
> List&lt;String&gt; listImageContentByImageid(imageId, xAnchoreAccount)

List image content types

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageId = "imageId_example"; // String | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<String> result = apiInstance.listImageContentByImageid(imageId, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#listImageContentByImageid");
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
| **imageId** | **String**|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Content of specified type from the image |  -  |
| **500** | Internal error |  -  |

<a id="listImageMetadata"></a>
# **listImageMetadata**
> List&lt;String&gt; listImageMetadata(imageDigest, xAnchoreAccount)

List image metadata types

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageDigest = "imageDigest_example"; // String | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<String> result = apiInstance.listImageMetadata(imageDigest, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#listImageMetadata");
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
| **imageDigest** | **String**|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metadata listing for the image |  -  |
| **500** | Internal Error |  -  |

<a id="listImages"></a>
# **listImages**
> List&lt;AnchoreImage&gt; listImages(history, fulltag, imageStatus, analysisStatus, xAnchoreAccount)

List all visible images

List all images visible to the user

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
    defaultClient.setBasePath("http://localhost");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    Boolean history = true; // Boolean | Include image history in the response
    String fulltag = "fulltag_example"; // String | Full docker-pull string to filter results by (e.g. docker.io/library/nginx:latest, or myhost.com:5000/testimages:v1.1.1)
    String imageStatus = "all"; // String | Filter by image_status value on the record. Default if omitted is 'active'.
    String analysisStatus = "not_analyzed"; // String | Filter by analysis_status value on the record.
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<AnchoreImage> result = apiInstance.listImages(history, fulltag, imageStatus, analysisStatus, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#listImages");
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
| **history** | **Boolean**| Include image history in the response | [optional] |
| **fulltag** | **String**| Full docker-pull string to filter results by (e.g. docker.io/library/nginx:latest, or myhost.com:5000/testimages:v1.1.1) | [optional] |
| **imageStatus** | **String**| Filter by image_status value on the record. Default if omitted is &#39;active&#39;. | [optional] [default to active] [enum: all, active, deleting] |
| **analysisStatus** | **String**| Filter by analysis_status value on the record. | [optional] [enum: not_analyzed, analyzed, analyzing, analysis_failed] |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**List&lt;AnchoreImage&gt;**](AnchoreImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **500** | Internal Error |  -  |

