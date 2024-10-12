# ImageManagementApi

All URIs are relative to *https://run.byvalue.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**imageDeleteImagesIdDelete**](ImageManagementApi.md#imageDeleteImagesIdDelete) | **DELETE** /images/{id} | Delete image |
| [**imageListAllImagesGet**](ImageManagementApi.md#imageListAllImagesGet) | **GET** /images | List all images |
| [**imageListImagesIdGet**](ImageManagementApi.md#imageListImagesIdGet) | **GET** /images/{id} | List image |
| [**imageUploadImagesPost**](ImageManagementApi.md#imageUploadImagesPost) | **POST** /images | Upload image |


<a id="imageDeleteImagesIdDelete"></a>
# **imageDeleteImagesIdDelete**
> imageDeleteImagesIdDelete(id)

Delete image

This endpoint allows you to delete images hosted in the LinQR storage.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://run.byvalue.org");
    
    // Configure API key authorization: RapidAPI
    ApiKeyAuth RapidAPI = (ApiKeyAuth) defaultClient.getAuthentication("RapidAPI");
    RapidAPI.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RapidAPI.setApiKeyPrefix("Token");

    ImageManagementApi apiInstance = new ImageManagementApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.imageDeleteImagesIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageManagementApi#imageDeleteImagesIdDelete");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[RapidAPI](../README.md#RapidAPI)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful Response |  -  |
| **404** | Not Found |  -  |
| **422** | Validation Error |  -  |
| **500** | Internal Server Error |  -  |

<a id="imageListAllImagesGet"></a>
# **imageListAllImagesGet**
> List&lt;ImageMetadata&gt; imageListAllImagesGet()

List all images

This endpoint allows you to list images hosted in the LinQR storage. If there are no images hosted, an empty array is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://run.byvalue.org");
    
    // Configure API key authorization: RapidAPI
    ApiKeyAuth RapidAPI = (ApiKeyAuth) defaultClient.getAuthentication("RapidAPI");
    RapidAPI.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RapidAPI.setApiKeyPrefix("Token");

    ImageManagementApi apiInstance = new ImageManagementApi(defaultClient);
    try {
      List<ImageMetadata> result = apiInstance.imageListAllImagesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageManagementApi#imageListAllImagesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;ImageMetadata&gt;**](ImageMetadata.md)

### Authorization

[RapidAPI](../README.md#RapidAPI)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **500** | Internal Server Error |  -  |

<a id="imageListImagesIdGet"></a>
# **imageListImagesIdGet**
> ImageMetadata imageListImagesIdGet(id)

List image

This endpoint allows you to list single image hosted in the LinQR storage.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://run.byvalue.org");
    
    // Configure API key authorization: RapidAPI
    ApiKeyAuth RapidAPI = (ApiKeyAuth) defaultClient.getAuthentication("RapidAPI");
    RapidAPI.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RapidAPI.setApiKeyPrefix("Token");

    ImageManagementApi apiInstance = new ImageManagementApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      ImageMetadata result = apiInstance.imageListImagesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageManagementApi#imageListImagesIdGet");
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
| **id** | **String**|  | |

### Return type

[**ImageMetadata**](ImageMetadata.md)

### Authorization

[RapidAPI](../README.md#RapidAPI)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **404** | Not Found |  -  |
| **422** | Validation Error |  -  |
| **500** | Internal Server Error |  -  |

<a id="imageUploadImagesPost"></a>
# **imageUploadImagesPost**
> ImageMetadata imageUploadImagesPost(image)

Upload image

This endpoint allows you to upload images to LinQR storage. In the response, metadata of the submitted image is sent, including the identifier used by other endpoints from the &#x60;Image management&#x60; group for image identification.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://run.byvalue.org");
    
    // Configure API key authorization: RapidAPI
    ApiKeyAuth RapidAPI = (ApiKeyAuth) defaultClient.getAuthentication("RapidAPI");
    RapidAPI.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RapidAPI.setApiKeyPrefix("Token");

    ImageManagementApi apiInstance = new ImageManagementApi(defaultClient);
    File image = new File("/path/to/file"); // File | Binary file to be uploaded into LinQR storage. Maximum single file size is 1MiB (1,048,576 bytes).
    try {
      ImageMetadata result = apiInstance.imageUploadImagesPost(image);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageManagementApi#imageUploadImagesPost");
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
| **image** | **File**| Binary file to be uploaded into LinQR storage. Maximum single file size is 1MiB (1,048,576 bytes). | |

### Return type

[**ImageMetadata**](ImageMetadata.md)

### Authorization

[RapidAPI](../README.md#RapidAPI)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |
| **500** | Internal Server Error |  -  |

