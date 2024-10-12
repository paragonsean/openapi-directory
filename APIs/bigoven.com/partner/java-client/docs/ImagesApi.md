# ImagesApi

All URIs are relative to *https://api2.bigoven.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**imagesGet**](ImagesApi.md#imagesGet) | **GET** /recipe/{recipeId}/images | Get all the images for a recipe. DEPRECATED. Please use /recipe/{recipeId}/photos. |
| [**imagesGetPendingByUser**](ImagesApi.md#imagesGetPendingByUser) | **GET** /recipe/photos/pending | Gets the pending by user. |
| [**imagesGetRecipePhotos**](ImagesApi.md#imagesGetRecipePhotos) | **GET** /recipe/{recipeId}/photos | Get all the photos for a recipe |
| [**imagesGetScanImages**](ImagesApi.md#imagesGetScanImages) | **GET** /recipe/{recipeId}/scans | Gets a list of RecipeScan images for the recipe. There will be at most 3 per recipe. |
| [**imagesUploadRecipeImage**](ImagesApi.md#imagesUploadRecipeImage) | **POST** /recipe/{recipeId}/image | POST: /recipe/{recipeId}/image?lat&#x3D;42&amp;amp;lng&#x3D;21&amp;amp;caption&#x3D;this%20is%20my%20caption                              Note that caption, lng and lat are all optional, but must go on the request URI as params because this endpoint               needs a multipart/mime content header and will not parse JSON in the body along with it.                             Testing with Postman (validated 11/20/2015):               1) Remove the Content-Type header; add authentication information               2) On the request, click Body and choose \&quot;form-data\&quot;, then add a line item with \&quot;key\&quot; column set to \&quot;file\&quot; and on the right,               change the type of the input from Text to File.  Browse and choose a JPG. |
| [**imagesUploadUserAvatar**](ImagesApi.md#imagesUploadUserAvatar) | **POST** /image/avatar | POST: /image/avatar                             Testing with Postman (validated 11/20/2015):              1) Remove the Content-Type header; add authentication information              2) On the request, click Body and choose \&quot;form-data\&quot;, then add a line item with \&quot;key\&quot; column set to \&quot;file\&quot; and on the right,              change the type of the input from Text to File.  Browse and choose a JPG. |


<a id="imagesGet"></a>
# **imagesGet**
> List&lt;BigOvenModelAPIImage&gt; imagesGet(recipeId)

Get all the images for a recipe. DEPRECATED. Please use /recipe/{recipeId}/photos.

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
    defaultClient.setBasePath("https://api2.bigoven.com");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    Integer recipeId = 56; // Integer | Recipe ID (required)
    try {
      List<BigOvenModelAPIImage> result = apiInstance.imagesGet(recipeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesGet");
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
| **recipeId** | **Integer**| Recipe ID (required) | |

### Return type

[**List&lt;BigOvenModelAPIImage&gt;**](BigOvenModelAPIImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="imagesGetPendingByUser"></a>
# **imagesGetPendingByUser**
> API2ControllersWebAPIImagesControllerRecipePhotosResponse imagesGetPendingByUser()

Gets the pending by user.

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
    defaultClient.setBasePath("https://api2.bigoven.com");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    try {
      API2ControllersWebAPIImagesControllerRecipePhotosResponse result = apiInstance.imagesGetPendingByUser();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesGetPendingByUser");
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

[**API2ControllersWebAPIImagesControllerRecipePhotosResponse**](API2ControllersWebAPIImagesControllerRecipePhotosResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="imagesGetRecipePhotos"></a>
# **imagesGetRecipePhotos**
> API2ControllersWebAPIImagesControllerRecipePhotosResponse imagesGetRecipePhotos(recipeId, pg, rpp)

Get all the photos for a recipe

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
    defaultClient.setBasePath("https://api2.bigoven.com");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    Integer recipeId = 56; // Integer | Recipe ID (required)
    Integer pg = 56; // Integer | 
    Integer rpp = 56; // Integer | 
    try {
      API2ControllersWebAPIImagesControllerRecipePhotosResponse result = apiInstance.imagesGetRecipePhotos(recipeId, pg, rpp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesGetRecipePhotos");
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
| **recipeId** | **Integer**| Recipe ID (required) | |
| **pg** | **Integer**|  | [optional] |
| **rpp** | **Integer**|  | [optional] |

### Return type

[**API2ControllersWebAPIImagesControllerRecipePhotosResponse**](API2ControllersWebAPIImagesControllerRecipePhotosResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="imagesGetScanImages"></a>
# **imagesGetScanImages**
> List&lt;BigOvenModelAPIImage&gt; imagesGetScanImages(recipeId)

Gets a list of RecipeScan images for the recipe. There will be at most 3 per recipe.

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
    defaultClient.setBasePath("https://api2.bigoven.com");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    Integer recipeId = 56; // Integer | the recipe identifier (int)
    try {
      List<BigOvenModelAPIImage> result = apiInstance.imagesGetScanImages(recipeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesGetScanImages");
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
| **recipeId** | **Integer**| the recipe identifier (int) | |

### Return type

[**List&lt;BigOvenModelAPIImage&gt;**](BigOvenModelAPIImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="imagesUploadRecipeImage"></a>
# **imagesUploadRecipeImage**
> Object imagesUploadRecipeImage(recipeId, caption, lat, lng)

POST: /recipe/{recipeId}/image?lat&#x3D;42&amp;amp;lng&#x3D;21&amp;amp;caption&#x3D;this%20is%20my%20caption                              Note that caption, lng and lat are all optional, but must go on the request URI as params because this endpoint               needs a multipart/mime content header and will not parse JSON in the body along with it.                             Testing with Postman (validated 11/20/2015):               1) Remove the Content-Type header; add authentication information               2) On the request, click Body and choose \&quot;form-data\&quot;, then add a line item with \&quot;key\&quot; column set to \&quot;file\&quot; and on the right,               change the type of the input from Text to File.  Browse and choose a JPG.

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
    defaultClient.setBasePath("https://api2.bigoven.com");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String recipeId = "recipeId_example"; // String | 
    String caption = "caption_example"; // String | 
    Double lat = 3.4D; // Double | 
    Double lng = 3.4D; // Double | 
    try {
      Object result = apiInstance.imagesUploadRecipeImage(recipeId, caption, lat, lng);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesUploadRecipeImage");
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
| **recipeId** | **String**|  | |
| **caption** | **String**|  | [optional] |
| **lat** | **Double**|  | [optional] |
| **lng** | **Double**|  | [optional] |

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
| **200** | Success |  -  |
| **400** | if bad request (e.g., missing parameters) |  -  |
| **401** | if the user is unknown |  -  |
| **415** | if unsupported media type (e.g., bad JPG) |  -  |

<a id="imagesUploadUserAvatar"></a>
# **imagesUploadUserAvatar**
> Object imagesUploadUserAvatar()

POST: /image/avatar                             Testing with Postman (validated 11/20/2015):              1) Remove the Content-Type header; add authentication information              2) On the request, click Body and choose \&quot;form-data\&quot;, then add a line item with \&quot;key\&quot; column set to \&quot;file\&quot; and on the right,              change the type of the input from Text to File.  Browse and choose a JPG.

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
    defaultClient.setBasePath("https://api2.bigoven.com");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    try {
      Object result = apiInstance.imagesUploadUserAvatar();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagesUploadUserAvatar");
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

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | if bad request (e.g., missing parameters) |  -  |
| **401** | if the user is unknown |  -  |
| **415** | if unsupported media type (e.g., bad JPG) |  -  |

