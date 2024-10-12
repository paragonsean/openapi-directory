# ImagesApi

All URIs are relative to *https://api.linode.com/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createImage**](ImagesApi.md#createImage) | **POST** /images | Image Create |
| [**deleteImage**](ImagesApi.md#deleteImage) | **DELETE** /images/{imageId} | Image Delete |
| [**getImage**](ImagesApi.md#getImage) | **GET** /images/{imageId} | Image View |
| [**getImages**](ImagesApi.md#getImages) | **GET** /images | Images List |
| [**imagesUploadPost**](ImagesApi.md#imagesUploadPost) | **POST** /images/upload | Image Upload |
| [**updateImage**](ImagesApi.md#updateImage) | **PUT** /images/{imageId} | Image Update |


<a id="createImage"></a>
# **createImage**
> Image createImage(createImageRequest)

Image Create

Captures a private gold-master Image from a Linode Disk. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    CreateImageRequest createImageRequest = new CreateImageRequest(); // CreateImageRequest | Information about the Image to create.
    try {
      Image result = apiInstance.createImage(createImageRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#createImage");
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
| **createImageRequest** | [**CreateImageRequest**](CreateImageRequest.md)| Information about the Image to create. | [optional] |

### Return type

[**Image**](Image.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | New private Image created successfully. |  -  |
| **0** | Error |  -  |

<a id="deleteImage"></a>
# **deleteImage**
> Object deleteImage(imageId)

Image Delete

Deletes a private Image you have permission to &#x60;read_write&#x60;.   **Deleting an Image is a destructive action and cannot be undone.** 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageId = "imageId_example"; // String | ID of the Image to look up.
    try {
      Object result = apiInstance.deleteImage(imageId);
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
| **imageId** | **String**| ID of the Image to look up. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete successful |  -  |
| **0** | Error |  -  |

<a id="getImage"></a>
# **getImage**
> Image getImage(imageId)

Image View

Get information about a single Image.  * **Public** Images have IDs that begin with \&quot;linode/\&quot;. These distribution images are generally available to all users.  * **Private** Images have IDs that begin with \&quot;private/\&quot;. These Images are Account-specific and only accessible to Users with appropriate [Grants](/docs/api/account/#users-grants-view).  * To view a public Image, call this endpoint with or without authentication. To view a private Image, call this endpoint with authentication. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageId = "imageId_example"; // String | ID of the Image to look up.
    try {
      Image result = apiInstance.getImage(imageId);
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
| **imageId** | **String**| ID of the Image to look up. | |

### Return type

[**Image**](Image.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A single Image object. |  -  |
| **0** | Error |  -  |

<a id="getImages"></a>
# **getImages**
> GetImages200Response getImages(page, pageSize)

Images List

Returns a paginated list of Images.  * **Public** Images have IDs that begin with \&quot;linode/\&quot;. These distribution images are generally available to all users.  * **Private** Images have IDs that begin with \&quot;private/\&quot;. These Images are Account-specific and only accessible to Users with appropriate [Grants](/docs/api/account/#users-grants-view).  * To view only public Images, call this endpoint with or without authentication. To view private Images as well, call this endpoint with authentication. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetImages200Response result = apiInstance.getImages(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getImages");
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
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetImages200Response**](GetImages200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of Images. |  -  |
| **0** | Error |  -  |

<a id="imagesUploadPost"></a>
# **imagesUploadPost**
> ImagesUploadPost200Response imagesUploadPost(imagesUploadPostRequest)

Image Upload

Initiates an Image upload.  This endpoint creates a new private Image object and returns it along with the URL to which image data can be uploaded.  - Image data must be uploaded within 24 hours of creation or the upload will be cancelled and the image deleted.  - Image uploads should be made as an HTTP PUT request to the URL returned in the &#x60;upload_to&#x60; response parameter, with a &#x60;Content-type: application/octet-stream&#x60; header included in the request. For example:        curl -v \\         -H \&quot;Content-Type: application/octet-stream\&quot; \\         --upload-file example.img.gz \\         $UPLOAD_URL \\         --progress-bar \\         --output /dev/null  - Uploaded image data should be compressed in gzip (&#x60;.gz&#x60;) format. The uncompressed disk should be in raw disk image (&#x60;.img&#x60;) format. A maximum compressed file size of 5GB is supported for upload at this time.  **Note:** To initiate and complete an Image upload in a single step, see our guide on how to [Upload an Image](/docs/products/tools/images/guides/upload-an-image/) using Cloud Manager or the Linode CLI &#x60;image-upload&#x60; plugin. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    ImagesUploadPostRequest imagesUploadPostRequest = new ImagesUploadPostRequest(); // ImagesUploadPostRequest | The uploaded Image details.
    try {
      ImagesUploadPost200Response result = apiInstance.imagesUploadPost(imagesUploadPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesUploadPost");
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
| **imagesUploadPostRequest** | [**ImagesUploadPostRequest**](ImagesUploadPostRequest.md)| The uploaded Image details. | [optional] |

### Return type

[**ImagesUploadPost200Response**](ImagesUploadPost200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Image Upload object including the upload URL and Image object. |  -  |
| **0** | Error |  -  |

<a id="updateImage"></a>
# **updateImage**
> Image updateImage(imageId, image)

Image Update

Updates a private Image that you have permission to &#x60;read_write&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String imageId = "imageId_example"; // String | ID of the Image to look up.
    Image image = new Image(); // Image | The fields to update. 
    try {
      Image result = apiInstance.updateImage(imageId, image);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#updateImage");
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
| **imageId** | **String**| ID of the Image to look up. | |
| **image** | [**Image**](Image.md)| The fields to update.  | |

### Return type

[**Image**](Image.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated image. |  -  |
| **0** | Error |  -  |

