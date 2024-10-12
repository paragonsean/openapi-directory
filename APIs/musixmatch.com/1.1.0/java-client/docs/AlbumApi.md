# AlbumApi

All URIs are relative to *https://api.musixmatch.com/ws/1.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**albumGetGet**](AlbumApi.md#albumGetGet) | **GET** /album.get |  |
| [**artistAlbumsGetGet**](AlbumApi.md#artistAlbumsGetGet) | **GET** /artist.albums.get |  |


<a id="albumGetGet"></a>
# **albumGetGet**
> AlbumGetGet200Response albumGetGet(albumId, format, paramCallback)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.musixmatch.com/ws/1.1");
    
    // Configure API key authorization: key
    ApiKeyAuth key = (ApiKeyAuth) defaultClient.getAuthentication("key");
    key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //key.setApiKeyPrefix("Token");

    AlbumApi apiInstance = new AlbumApi(defaultClient);
    String albumId = "albumId_example"; // String | The musiXmatch album id
    String format = "json"; // String | output format: json, jsonp, xml.
    String paramCallback = "paramCallback_example"; // String | jsonp callback
    try {
      AlbumGetGet200Response result = apiInstance.albumGetGet(albumId, format, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumApi#albumGetGet");
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
| **albumId** | **String**| The musiXmatch album id | |
| **format** | **String**| output format: json, jsonp, xml. | [optional] [default to json] |
| **paramCallback** | **String**| jsonp callback | [optional] |

### Return type

[**AlbumGetGet200Response**](AlbumGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful. |  -  |

<a id="artistAlbumsGetGet"></a>
# **artistAlbumsGetGet**
> ArtistAlbumsGetGet200Response artistAlbumsGetGet(artistId, format, paramCallback, sReleaseDate, gAlbumName, pageSize, page)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlbumApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.musixmatch.com/ws/1.1");
    
    // Configure API key authorization: key
    ApiKeyAuth key = (ApiKeyAuth) defaultClient.getAuthentication("key");
    key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //key.setApiKeyPrefix("Token");

    AlbumApi apiInstance = new AlbumApi(defaultClient);
    String artistId = "artistId_example"; // String | The musiXmatch artist id
    String format = "json"; // String | output format: json, jsonp, xml.
    String paramCallback = "paramCallback_example"; // String | jsonp callback
    String sReleaseDate = "sReleaseDate_example"; // String | Sort by release date (asc|desc)
    String gAlbumName = "gAlbumName_example"; // String | Group by Album Name
    BigDecimal pageSize = new BigDecimal(78); // BigDecimal | Define the page size for paginated results.Range is 1 to 100.
    BigDecimal page = new BigDecimal(78); // BigDecimal | Define the page number for paginated results
    try {
      ArtistAlbumsGetGet200Response result = apiInstance.artistAlbumsGetGet(artistId, format, paramCallback, sReleaseDate, gAlbumName, pageSize, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlbumApi#artistAlbumsGetGet");
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
| **artistId** | **String**| The musiXmatch artist id | |
| **format** | **String**| output format: json, jsonp, xml. | [optional] [default to json] |
| **paramCallback** | **String**| jsonp callback | [optional] |
| **sReleaseDate** | **String**| Sort by release date (asc|desc) | [optional] |
| **gAlbumName** | **String**| Group by Album Name | [optional] |
| **pageSize** | **BigDecimal**| Define the page size for paginated results.Range is 1 to 100. | [optional] |
| **page** | **BigDecimal**| Define the page number for paginated results | [optional] |

### Return type

[**ArtistAlbumsGetGet200Response**](ArtistAlbumsGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful. |  -  |

