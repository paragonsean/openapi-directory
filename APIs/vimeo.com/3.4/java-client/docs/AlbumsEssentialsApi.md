# AlbumsEssentialsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAlbum**](AlbumsEssentialsApi.md#createAlbum) | **POST** /users/{user_id}/albums | Create an album |
| [**createAlbumAlt1**](AlbumsEssentialsApi.md#createAlbumAlt1) | **POST** /me/albums | Create an album |
| [**deleteAlbum**](AlbumsEssentialsApi.md#deleteAlbum) | **DELETE** /users/{user_id}/albums/{album_id} | Delete an album |
| [**deleteAlbumAlt1**](AlbumsEssentialsApi.md#deleteAlbumAlt1) | **DELETE** /me/albums/{album_id} | Delete an album |
| [**editAlbum**](AlbumsEssentialsApi.md#editAlbum) | **PATCH** /users/{user_id}/albums/{album_id} | Edit an album |
| [**editAlbumAlt1**](AlbumsEssentialsApi.md#editAlbumAlt1) | **PATCH** /me/albums/{album_id} | Edit an album |
| [**getAlbum**](AlbumsEssentialsApi.md#getAlbum) | **GET** /users/{user_id}/albums/{album_id} | Get a specific album |
| [**getAlbumAlt1**](AlbumsEssentialsApi.md#getAlbumAlt1) | **GET** /me/albums/{album_id} | Get a specific album |
| [**getAlbums**](AlbumsEssentialsApi.md#getAlbums) | **GET** /users/{user_id}/albums | Get all the albums that belong to a user |
| [**getAlbumsAlt1**](AlbumsEssentialsApi.md#getAlbumsAlt1) | **GET** /me/albums | Get all the albums that belong to a user |


<a id="createAlbum"></a>
# **createAlbum**
> Album createAlbum(userId, createAlbumAlt1Request)

Create an album

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsEssentialsApi;

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

    AlbumsEssentialsApi apiInstance = new AlbumsEssentialsApi(defaultClient);
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    CreateAlbumAlt1Request createAlbumAlt1Request = new CreateAlbumAlt1Request(); // CreateAlbumAlt1Request | 
    try {
      Album result = apiInstance.createAlbum(userId, createAlbumAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsEssentialsApi#createAlbum");
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
| **userId** | **BigDecimal**| The ID of the user. | |
| **createAlbumAlt1Request** | [**CreateAlbumAlt1Request**](CreateAlbumAlt1Request.md)|  | |

### Return type

[**Album**](Album.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.album+json
 - **Accept**: application/vnd.vimeo.album+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The album was created. |  -  |
| **400** | A parameter is invalid. |  -  |
| **403** | The supplied token doesn&#39;t have the proper scopes, or the authenticated user can&#39;t create an album. |  -  |

<a id="createAlbumAlt1"></a>
# **createAlbumAlt1**
> Album createAlbumAlt1(createAlbumAlt1Request)

Create an album

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsEssentialsApi;

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

    AlbumsEssentialsApi apiInstance = new AlbumsEssentialsApi(defaultClient);
    CreateAlbumAlt1Request createAlbumAlt1Request = new CreateAlbumAlt1Request(); // CreateAlbumAlt1Request | 
    try {
      Album result = apiInstance.createAlbumAlt1(createAlbumAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsEssentialsApi#createAlbumAlt1");
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
| **createAlbumAlt1Request** | [**CreateAlbumAlt1Request**](CreateAlbumAlt1Request.md)|  | |

### Return type

[**Album**](Album.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.album+json
 - **Accept**: application/vnd.vimeo.album+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The album was created. |  -  |
| **400** | A parameter is invalid. |  -  |
| **403** | The supplied token doesn&#39;t have the proper scopes, or the authenticated user can&#39;t create an album. |  -  |

<a id="deleteAlbum"></a>
# **deleteAlbum**
> deleteAlbum(albumId, userId)

Delete an album

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsEssentialsApi;

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

    AlbumsEssentialsApi apiInstance = new AlbumsEssentialsApi(defaultClient);
    BigDecimal albumId = new BigDecimal("3706071"); // BigDecimal | The ID of the album.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      apiInstance.deleteAlbum(albumId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsEssentialsApi#deleteAlbum");
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

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The album was deleted. |  -  |
| **403** | The supplied token doesn&#39;t have the proper scopes, or the authenticated user can&#39;t delete the album. |  -  |
| **404** | No such album exists. |  -  |

<a id="deleteAlbumAlt1"></a>
# **deleteAlbumAlt1**
> deleteAlbumAlt1(albumId)

Delete an album

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsEssentialsApi;

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

    AlbumsEssentialsApi apiInstance = new AlbumsEssentialsApi(defaultClient);
    BigDecimal albumId = new BigDecimal("3706071"); // BigDecimal | The ID of the album.
    try {
      apiInstance.deleteAlbumAlt1(albumId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsEssentialsApi#deleteAlbumAlt1");
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

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The album was deleted. |  -  |
| **403** | The supplied token doesn&#39;t have the proper scopes, or the authenticated user can&#39;t delete the album. |  -  |
| **404** | No such album exists. |  -  |

<a id="editAlbum"></a>
# **editAlbum**
> Album editAlbum(albumId, userId, editAlbumAlt1Request)

Edit an album

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsEssentialsApi;

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

    AlbumsEssentialsApi apiInstance = new AlbumsEssentialsApi(defaultClient);
    BigDecimal albumId = new BigDecimal("3706071"); // BigDecimal | The ID of the album.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    EditAlbumAlt1Request editAlbumAlt1Request = new EditAlbumAlt1Request(); // EditAlbumAlt1Request | 
    try {
      Album result = apiInstance.editAlbum(albumId, userId, editAlbumAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsEssentialsApi#editAlbum");
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
| **editAlbumAlt1Request** | [**EditAlbumAlt1Request**](EditAlbumAlt1Request.md)|  | [optional] |

### Return type

[**Album**](Album.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.album+json
 - **Accept**: application/vnd.vimeo.album+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The album was edited. |  -  |
| **400** | A parameter is invalid. |  -  |
| **403** | The authenticated user doesn&#39;t own the album, the supplied token doesn&#39;t have the proper scopes, or the authenticated user can&#39;t edit the album. |  -  |
| **404** | No such album exists. |  -  |

<a id="editAlbumAlt1"></a>
# **editAlbumAlt1**
> Album editAlbumAlt1(albumId, editAlbumAlt1Request)

Edit an album

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsEssentialsApi;

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

    AlbumsEssentialsApi apiInstance = new AlbumsEssentialsApi(defaultClient);
    BigDecimal albumId = new BigDecimal("3706071"); // BigDecimal | The ID of the album.
    EditAlbumAlt1Request editAlbumAlt1Request = new EditAlbumAlt1Request(); // EditAlbumAlt1Request | 
    try {
      Album result = apiInstance.editAlbumAlt1(albumId, editAlbumAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsEssentialsApi#editAlbumAlt1");
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
| **editAlbumAlt1Request** | [**EditAlbumAlt1Request**](EditAlbumAlt1Request.md)|  | [optional] |

### Return type

[**Album**](Album.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.album+json
 - **Accept**: application/vnd.vimeo.album+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The album was edited. |  -  |
| **400** | A parameter is invalid. |  -  |
| **403** | The authenticated user doesn&#39;t own the album, the supplied token doesn&#39;t have the proper scopes, or the authenticated user can&#39;t edit the album. |  -  |
| **404** | No such album exists. |  -  |

<a id="getAlbum"></a>
# **getAlbum**
> Album getAlbum(albumId, userId)

Get a specific album

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsEssentialsApi;

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

    AlbumsEssentialsApi apiInstance = new AlbumsEssentialsApi(defaultClient);
    BigDecimal albumId = new BigDecimal("3706071"); // BigDecimal | The ID of the album.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      Album result = apiInstance.getAlbum(albumId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsEssentialsApi#getAlbum");
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

[**Album**](Album.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.album+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The album was returned. |  -  |
| **404** | No such album exists. |  -  |

<a id="getAlbumAlt1"></a>
# **getAlbumAlt1**
> Album getAlbumAlt1(albumId)

Get a specific album

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsEssentialsApi;

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

    AlbumsEssentialsApi apiInstance = new AlbumsEssentialsApi(defaultClient);
    BigDecimal albumId = new BigDecimal("3706071"); // BigDecimal | The ID of the album.
    try {
      Album result = apiInstance.getAlbumAlt1(albumId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsEssentialsApi#getAlbumAlt1");
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

### Return type

[**Album**](Album.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.album+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The album was returned. |  -  |
| **404** | No such album exists. |  -  |

<a id="getAlbums"></a>
# **getAlbums**
> List&lt;Album&gt; getAlbums(userId, direction, page, perPage, query, sort)

Get all the albums that belong to a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsEssentialsApi;

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

    AlbumsEssentialsApi apiInstance = new AlbumsEssentialsApi(defaultClient);
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    String direction = "asc"; // String | The sort direction of the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String query = "Stop motion"; // String | The search query to use to filter the results.
    String sort = "alphabetical"; // String | The way to sort the results.
    try {
      List<Album> result = apiInstance.getAlbums(userId, direction, page, perPage, query, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsEssentialsApi#getAlbums");
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
| **userId** | **BigDecimal**| The ID of the user. | |
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **query** | **String**| The search query to use to filter the results. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: alphabetical, date, duration, videos] |

### Return type

[**List&lt;Album&gt;**](Album.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The albums were returned. |  -  |
| **400** | A parameter is invalid. |  -  |

<a id="getAlbumsAlt1"></a>
# **getAlbumsAlt1**
> List&lt;Album&gt; getAlbumsAlt1(direction, page, perPage, query, sort)

Get all the albums that belong to a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumsEssentialsApi;

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

    AlbumsEssentialsApi apiInstance = new AlbumsEssentialsApi(defaultClient);
    String direction = "asc"; // String | The sort direction of the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String query = "Stop motion"; // String | The search query to use to filter the results.
    String sort = "alphabetical"; // String | The way to sort the results.
    try {
      List<Album> result = apiInstance.getAlbumsAlt1(direction, page, perPage, query, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumsEssentialsApi#getAlbumsAlt1");
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
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **query** | **String**| The search query to use to filter the results. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: alphabetical, date, duration, videos] |

### Return type

[**List&lt;Album&gt;**](Album.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The albums were returned. |  -  |
| **400** | A parameter is invalid. |  -  |

