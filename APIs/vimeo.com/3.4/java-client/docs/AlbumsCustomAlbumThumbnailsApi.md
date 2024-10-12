# AlbumsCustomAlbumThumbnailsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAlbumCustomThumb**](AlbumsCustomAlbumThumbnailsApi.md#createAlbumCustomThumb) | **POST** /users/{user_id}/albums/{album_id}/custom_thumbnails | Add a custom uploaded thumbnail |
| [**deleteAlbumCustomThumbnail**](AlbumsCustomAlbumThumbnailsApi.md#deleteAlbumCustomThumbnail) | **DELETE** /users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id} | Remove a custom uploaded album thumbnail |
| [**getAlbumCustomThumbnail**](AlbumsCustomAlbumThumbnailsApi.md#getAlbumCustomThumbnail) | **GET** /users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id} | Get a specific custom uploaded album thumbnail |
| [**getAlbumCustomThumbs**](AlbumsCustomAlbumThumbnailsApi.md#getAlbumCustomThumbs) | **GET** /users/{user_id}/albums/{album_id}/custom_thumbnails | Get all the custom upload thumbnails of an album |
| [**replaceAlbumCustomThumb**](AlbumsCustomAlbumThumbnailsApi.md#replaceAlbumCustomThumb) | **PATCH** /users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id} | Replace a custom uploaded album thumbnail |


<a id="createAlbumCustomThumb"></a>
# **createAlbumCustomThumb**
> Picture createAlbumCustomThumb(albumId, userId)

Add a custom uploaded thumbnail

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsCustomAlbumThumbnailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlbumsCustomAlbumThumbnailsApi apiInstance = new AlbumsCustomAlbumThumbnailsApi(defaultClient);
    BigDecimal albumId = new BigDecimal("3706071"); // BigDecimal | The ID of the album.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      Picture result = apiInstance.createAlbumCustomThumb(albumId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsCustomAlbumThumbnailsApi#createAlbumCustomThumb");
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
| **albumId** | **BigDecimal**| The ID of the album. | |
| **userId** | **BigDecimal**| The ID of the user. | |

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.picture+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The custom thumbnail was added to the album. |  -  |
| **403** | The authenticated user can&#39;t modify this album. |  -  |
| **404** | No such album exists. |  -  |

<a id="deleteAlbumCustomThumbnail"></a>
# **deleteAlbumCustomThumbnail**
> deleteAlbumCustomThumbnail(albumId, thumbnailId, userId)

Remove a custom uploaded album thumbnail

This method removes a custom uploaded thumbnail from the specified album.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsCustomAlbumThumbnailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlbumsCustomAlbumThumbnailsApi apiInstance = new AlbumsCustomAlbumThumbnailsApi(defaultClient);
    BigDecimal albumId = new BigDecimal("3706071"); // BigDecimal | The ID of the album.
    BigDecimal thumbnailId = new BigDecimal("12345"); // BigDecimal | The ID of the custom thumbnail.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      apiInstance.deleteAlbumCustomThumbnail(albumId, thumbnailId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsCustomAlbumThumbnailsApi#deleteAlbumCustomThumbnail");
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
| **albumId** | **BigDecimal**| The ID of the album. | |
| **thumbnailId** | **BigDecimal**| The ID of the custom thumbnail. | |
| **userId** | **BigDecimal**| The ID of the user. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.picture+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The custom thumbnail was removed. |  -  |
| **403** | The authenticated user can&#39;t modify this album. |  -  |
| **404** | No such album exists, or it doesn&#39;t contain the specified custom thumbnail. |  -  |

<a id="getAlbumCustomThumbnail"></a>
# **getAlbumCustomThumbnail**
> Picture getAlbumCustomThumbnail(albumId, thumbnailId, userId)

Get a specific custom uploaded album thumbnail

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsCustomAlbumThumbnailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlbumsCustomAlbumThumbnailsApi apiInstance = new AlbumsCustomAlbumThumbnailsApi(defaultClient);
    BigDecimal albumId = new BigDecimal("3706071"); // BigDecimal | The ID of the album.
    BigDecimal thumbnailId = new BigDecimal("12345"); // BigDecimal | The ID of the custom thumbnail.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      Picture result = apiInstance.getAlbumCustomThumbnail(albumId, thumbnailId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsCustomAlbumThumbnailsApi#getAlbumCustomThumbnail");
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
| **albumId** | **BigDecimal**| The ID of the album. | |
| **thumbnailId** | **BigDecimal**| The ID of the custom thumbnail. | |
| **userId** | **BigDecimal**| The ID of the user. | |

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.picture+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The custom thumbnail was returned. |  -  |
| **403** | The authenticated user can&#39;t view this custom thumbnail. |  -  |
| **404** | No such album exists, or it doesn&#39;t contain the specified custom thumbnail. |  -  |

<a id="getAlbumCustomThumbs"></a>
# **getAlbumCustomThumbs**
> List&lt;Picture&gt; getAlbumCustomThumbs(albumId, userId, page, perPage)

Get all the custom upload thumbnails of an album

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsCustomAlbumThumbnailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlbumsCustomAlbumThumbnailsApi apiInstance = new AlbumsCustomAlbumThumbnailsApi(defaultClient);
    BigDecimal albumId = new BigDecimal("3706071"); // BigDecimal | The ID of the album.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    try {
      List<Picture> result = apiInstance.getAlbumCustomThumbs(albumId, userId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsCustomAlbumThumbnailsApi#getAlbumCustomThumbs");
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
| **albumId** | **BigDecimal**| The ID of the album. | |
| **userId** | **BigDecimal**| The ID of the user. | |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |

### Return type

[**List&lt;Picture&gt;**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.picture+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The custom uploaded thumbnails were returned. |  -  |
| **404** | No such album exists. |  -  |

<a id="replaceAlbumCustomThumb"></a>
# **replaceAlbumCustomThumb**
> Picture replaceAlbumCustomThumb(albumId, thumbnailId, userId, replaceAlbumCustomThumbRequest)

Replace a custom uploaded album thumbnail

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsCustomAlbumThumbnailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlbumsCustomAlbumThumbnailsApi apiInstance = new AlbumsCustomAlbumThumbnailsApi(defaultClient);
    BigDecimal albumId = new BigDecimal("3706071"); // BigDecimal | The ID of the album.
    BigDecimal thumbnailId = new BigDecimal("12345"); // BigDecimal | The ID of the custom thumbnail.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    ReplaceAlbumCustomThumbRequest replaceAlbumCustomThumbRequest = new ReplaceAlbumCustomThumbRequest(); // ReplaceAlbumCustomThumbRequest | 
    try {
      Picture result = apiInstance.replaceAlbumCustomThumb(albumId, thumbnailId, userId, replaceAlbumCustomThumbRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsCustomAlbumThumbnailsApi#replaceAlbumCustomThumb");
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
| **albumId** | **BigDecimal**| The ID of the album. | |
| **thumbnailId** | **BigDecimal**| The ID of the custom thumbnail. | |
| **userId** | **BigDecimal**| The ID of the user. | |
| **replaceAlbumCustomThumbRequest** | [**ReplaceAlbumCustomThumbRequest**](ReplaceAlbumCustomThumbRequest.md)|  | [optional] |

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.picture+json
 - **Accept**: application/vnd.vimeo.picture+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The custom thumbnail was replaced. |  -  |
| **403** | The authenticated user can&#39;t modify this album. |  -  |
| **404** | No such album exists, or it doesn&#39;t contain the specified custom thumbnail. |  -  |

