# PlaylistApi

All URIs are relative to *https://spinitron.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**playlistsGet**](PlaylistApi.md#playlistsGet) | **GET** /playlists | Returns playlists optionally filtered by {start} and/or {end} datetimes |
| [**playlistsIdGet**](PlaylistApi.md#playlistsIdGet) | **GET** /playlists/{id} | Get a Playlist by id |


<a id="playlistsGet"></a>
# **playlistsGet**
> PlaylistsGet200Response playlistsGet(start, end, showId, personaId, count, page, fields, expand)

Returns playlists optionally filtered by {start} and/or {end} datetimes

Get Playlists optionally filtered by a datetime range. Only past Playlists will be returned (with allowed tolerance equals 1 hour in future).  Ordered chronologically from newest to oldest. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaylistApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://spinitron.com/api");
    
    // Configure API key authorization: accessToken
    ApiKeyAuth accessToken = (ApiKeyAuth) defaultClient.getAuthentication("accessToken");
    accessToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //accessToken.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: httpBearer
    HttpBearerAuth httpBearer = (HttpBearerAuth) defaultClient.getAuthentication("httpBearer");
    httpBearer.setBearerToken("BEARER TOKEN");

    PlaylistApi apiInstance = new PlaylistApi(defaultClient);
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | The datetime starting from items must be returned. Maximum 1 hour in future. 
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | The ending datetime. Maximum 1 hour in future. 
    Integer showId = 56; // Integer | Filter by show
    Integer personaId = 56; // Integer | Filter by persona
    Integer count = 20; // Integer | Amount of items to return
    Integer page = 56; // Integer | Offset, used together with count
    List<String> fields = Arrays.asList(); // List<String> | Allows to select only needed fields
    List<String> expand = Arrays.asList(); // List<String> | Allows to select extra fields
    try {
      PlaylistsGet200Response result = apiInstance.playlistsGet(start, end, showId, personaId, count, page, fields, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaylistApi#playlistsGet");
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
| **start** | **OffsetDateTime**| The datetime starting from items must be returned. Maximum 1 hour in future.  | [optional] |
| **end** | **OffsetDateTime**| The ending datetime. Maximum 1 hour in future.  | [optional] |
| **showId** | **Integer**| Filter by show | [optional] |
| **personaId** | **Integer**| Filter by persona | [optional] |
| **count** | **Integer**| Amount of items to return | [optional] [default to 20] |
| **page** | **Integer**| Offset, used together with count | [optional] |
| **fields** | [**List&lt;String&gt;**](String.md)| Allows to select only needed fields | [optional] |
| **expand** | [**List&lt;String&gt;**](String.md)| Allows to select extra fields | [optional] |

### Return type

[**PlaylistsGet200Response**](PlaylistsGet200Response.md)

### Authorization

[accessToken](../README.md#accessToken), [httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The playlists |  -  |

<a id="playlistsIdGet"></a>
# **playlistsIdGet**
> Playlist playlistsIdGet(id, fields, expand)

Get a Playlist by id

The response object represents the playlist specified by {id}.  Status 404 is returned if a playlist with {id} does not exist or if it does but starts in the future (with allowed tolerance equals 1 hour in future). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaylistApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://spinitron.com/api");
    
    // Configure API key authorization: accessToken
    ApiKeyAuth accessToken = (ApiKeyAuth) defaultClient.getAuthentication("accessToken");
    accessToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //accessToken.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: httpBearer
    HttpBearerAuth httpBearer = (HttpBearerAuth) defaultClient.getAuthentication("httpBearer");
    httpBearer.setBearerToken("BEARER TOKEN");

    PlaylistApi apiInstance = new PlaylistApi(defaultClient);
    Integer id = 56; // Integer | 
    List<String> fields = Arrays.asList(); // List<String> | Allows to select only needed fields
    List<String> expand = Arrays.asList(); // List<String> | Allows to select extra fields
    try {
      Playlist result = apiInstance.playlistsIdGet(id, fields, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaylistApi#playlistsIdGet");
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
| **id** | **Integer**|  | |
| **fields** | [**List&lt;String&gt;**](String.md)| Allows to select only needed fields | [optional] |
| **expand** | [**List&lt;String&gt;**](String.md)| Allows to select extra fields | [optional] |

### Return type

[**Playlist**](Playlist.md)

### Authorization

[accessToken](../README.md#accessToken), [httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The playlist |  -  |
| **404** | Playlist not found or is in the future |  -  |

