# AlbumsCustomAlbumLogosApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAlbumLogo**](AlbumsCustomAlbumLogosApi.md#createAlbumLogo) | **POST** /users/{user_id}/albums/{album_id}/logos | Add a custom album logo |
| [**deleteAlbumLogo**](AlbumsCustomAlbumLogosApi.md#deleteAlbumLogo) | **DELETE** /users/{user_id}/albums/{album_id}/logos/{logo_id} | Remove a custom album logo |
| [**getAlbumLogo**](AlbumsCustomAlbumLogosApi.md#getAlbumLogo) | **GET** /users/{user_id}/albums/{album_id}/logos/{logo_id} | Get a specific custom album logo |
| [**getAlbumLogos**](AlbumsCustomAlbumLogosApi.md#getAlbumLogos) | **GET** /users/{user_id}/albums/{album_id}/logos | Get all the custom logos of an album |
| [**replaceAlbumLogo**](AlbumsCustomAlbumLogosApi.md#replaceAlbumLogo) | **PATCH** /users/{user_id}/albums/{album_id}/logos/{logo_id} | Replace a custom album logo |


<a id="createAlbumLogo"></a>
# **createAlbumLogo**
> Picture createAlbumLogo(albumId, userId)

Add a custom album logo

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsCustomAlbumLogosApi;

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

    AlbumsCustomAlbumLogosApi apiInstance = new AlbumsCustomAlbumLogosApi(defaultClient);
    BigDecimal albumId = new BigDecimal("3706071"); // BigDecimal | The ID of the album.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      Picture result = apiInstance.createAlbumLogo(albumId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsCustomAlbumLogosApi#createAlbumLogo");
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
| **201** | The logo was added to the album. |  -  |
| **403** | The authenticated user can&#39;t modify this album. |  -  |
| **404** | No such album exists. |  -  |

<a id="deleteAlbumLogo"></a>
# **deleteAlbumLogo**
> deleteAlbumLogo(albumId, logoId, userId)

Remove a custom album logo

This method removes a custom logo from the specified album.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsCustomAlbumLogosApi;

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

    AlbumsCustomAlbumLogosApi apiInstance = new AlbumsCustomAlbumLogosApi(defaultClient);
    BigDecimal albumId = new BigDecimal("3706071"); // BigDecimal | The ID of the album.
    BigDecimal logoId = new BigDecimal("12345"); // BigDecimal | The ID of the custom logo.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      apiInstance.deleteAlbumLogo(albumId, logoId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsCustomAlbumLogosApi#deleteAlbumLogo");
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
| **logoId** | **BigDecimal**| The ID of the custom logo. | |
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
| **204** | The custom logo was removed. |  -  |
| **403** | The authenticated user can&#39;t modify this album. |  -  |
| **404** | No such album exists, or it doesn&#39;t contain the specified custom logo. |  -  |

<a id="getAlbumLogo"></a>
# **getAlbumLogo**
> Picture getAlbumLogo(albumId, logoId, userId)

Get a specific custom album logo

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsCustomAlbumLogosApi;

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

    AlbumsCustomAlbumLogosApi apiInstance = new AlbumsCustomAlbumLogosApi(defaultClient);
    BigDecimal albumId = new BigDecimal("3706071"); // BigDecimal | The ID of the album.
    BigDecimal logoId = new BigDecimal("12345"); // BigDecimal | The ID of the custom logo.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      Picture result = apiInstance.getAlbumLogo(albumId, logoId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsCustomAlbumLogosApi#getAlbumLogo");
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
| **logoId** | **BigDecimal**| The ID of the custom logo. | |
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
| **200** | The custom logo was returned. |  -  |
| **403** | The authenticated user can&#39;t view this custom logo. |  -  |
| **404** | No such album exists, or it doesn&#39;t contain the specified custom logo. |  -  |

<a id="getAlbumLogos"></a>
# **getAlbumLogos**
> List&lt;Picture&gt; getAlbumLogos(albumId, userId, page, perPage)

Get all the custom logos of an album

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsCustomAlbumLogosApi;

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

    AlbumsCustomAlbumLogosApi apiInstance = new AlbumsCustomAlbumLogosApi(defaultClient);
    BigDecimal albumId = new BigDecimal("3706071"); // BigDecimal | The ID of the album.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    try {
      List<Picture> result = apiInstance.getAlbumLogos(albumId, userId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsCustomAlbumLogosApi#getAlbumLogos");
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
| **200** | The custom logos were returned. |  -  |
| **404** | No such album exists. |  -  |

<a id="replaceAlbumLogo"></a>
# **replaceAlbumLogo**
> Picture replaceAlbumLogo(albumId, logoId, userId, replaceAlbumLogoRequest)

Replace a custom album logo

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsCustomAlbumLogosApi;

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

    AlbumsCustomAlbumLogosApi apiInstance = new AlbumsCustomAlbumLogosApi(defaultClient);
    BigDecimal albumId = new BigDecimal("3706071"); // BigDecimal | The ID of the album.
    BigDecimal logoId = new BigDecimal("12345"); // BigDecimal | The ID of the custom logo.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    ReplaceAlbumLogoRequest replaceAlbumLogoRequest = new ReplaceAlbumLogoRequest(); // ReplaceAlbumLogoRequest | 
    try {
      Picture result = apiInstance.replaceAlbumLogo(albumId, logoId, userId, replaceAlbumLogoRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsCustomAlbumLogosApi#replaceAlbumLogo");
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
| **logoId** | **BigDecimal**| The ID of the custom logo. | |
| **userId** | **BigDecimal**| The ID of the user. | |
| **replaceAlbumLogoRequest** | [**ReplaceAlbumLogoRequest**](ReplaceAlbumLogoRequest.md)|  | [optional] |

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
| **200** | The custom logo was replaced. |  -  |
| **403** | The authenticated user can&#39;t modify this album. |  -  |
| **404** | No such album exists, or it doesn&#39;t contain the specified custom logo. |  -  |

