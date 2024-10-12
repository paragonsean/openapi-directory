# MusicArtistsBandsTracksAlbumArtCoverArtVideosApi

All URIs are relative to *https://api.hillbillysoftware.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**musiVideosGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musiVideosGet) | **GET** /Music/Videos/{AccessToken}/{ArtistID} | Lists all videos available for this Artist / Band |
| [**musicAlbumArtGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicAlbumArtGet) | **GET** /Music/Albums/Art/{AccessToken}/{AlbumID} | Returns Albumart for passed AlbumID |
| [**musicAlbumsGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicAlbumsGet) | **GET** /Music/Albums/{AccessToken}/{ArtistID} | Get albums from passed ArtistID |
| [**musicArtistExtendedGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicArtistExtendedGet) | **GET** /Music/Artist/Extended/{AccessToken}/{Name} | Provides extended information, which includes all known albums and music videos of artist / band |
| [**musicByMusicBrainzGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicByMusicBrainzGet) | **GET** /Music/Albums/MusicBrainzID/{AccessToken}/{MBID} | Get Artist / Band information on MusicBrainzID |
| [**musicCDCoversGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicCDCoversGet) | **GET** /Music/Albums/CoverArt/{AccessToken}/{MBID} | Gets CD art for passed MusicBrainzID |
| [**musicCoverArtByNameGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicCoverArtByNameGet) | **GET** /Music/Artist/Art/Name/{AccessToken}/{Name} | Retrieves artist / band Banner and logo based on artist or bandname |
| [**musicCoverArtGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicCoverArtGet) | **GET** /Music/Artist/Art/ID/{AccessToken}/{ArtistID} | Retrieves artist / band Banner and logo based on ArtistID |
| [**musicGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicGet) | **GET** /Music/Artist/{AccessToken}/{Name} | Get information about passed band name or artist |
| [**musicLyricsBySongGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicLyricsBySongGet) | **GET** /Music/Lyrics/BySong/{AccessToken}/{Song} | Get lyrics on song title |
| [**musicLyricsGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicLyricsGet) | **GET** /Music/Lyrics/ByName/{AccessToken}/{Name} | Get lyrics for band or artist (record set limited to 25) |
| [**musicLyricsbyAlbumIDGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicLyricsbyAlbumIDGet) | **GET** /Music/Lyrics/AlbumID/{AccessToken}/{AlbumID} | Returns all lyrics for requested AlbumID |
| [**musicTracksGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicTracksGet) | **GET** /Music/Tracks/{AccessToken}/{AlbumID} | Get all tracks from requested album |


<a id="musiVideosGet"></a>
# **musiVideosGet**
> List&lt;MusicVideo&gt; musiVideosGet(accessToken, artistID)

Lists all videos available for this Artist / Band

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    MusicArtistsBandsTracksAlbumArtCoverArtVideosApi apiInstance = new MusicArtistsBandsTracksAlbumArtCoverArtVideosApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String artistID = "artistID_example"; // String | 
    try {
      List<MusicVideo> result = apiInstance.musiVideosGet(accessToken, artistID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicArtistsBandsTracksAlbumArtCoverArtVideosApi#musiVideosGet");
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
| **accessToken** | **String**|  | |
| **artistID** | **String**|  | |

### Return type

[**List&lt;MusicVideo&gt;**](MusicVideo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lists all videos available for this Artist / Band |  -  |

<a id="musicAlbumArtGet"></a>
# **musicAlbumArtGet**
> AlbumArt musicAlbumArtGet(accessToken, albumID)

Returns Albumart for passed AlbumID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    MusicArtistsBandsTracksAlbumArtCoverArtVideosApi apiInstance = new MusicArtistsBandsTracksAlbumArtCoverArtVideosApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String albumID = "albumID_example"; // String | 
    try {
      AlbumArt result = apiInstance.musicAlbumArtGet(accessToken, albumID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicArtistsBandsTracksAlbumArtCoverArtVideosApi#musicAlbumArtGet");
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
| **accessToken** | **String**|  | |
| **albumID** | **String**|  | |

### Return type

[**AlbumArt**](AlbumArt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets album art for passed AlbumID |  -  |

<a id="musicAlbumsGet"></a>
# **musicAlbumsGet**
> List&lt;BandAlbums&gt; musicAlbumsGet(accessToken, artistID)

Get albums from passed ArtistID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    MusicArtistsBandsTracksAlbumArtCoverArtVideosApi apiInstance = new MusicArtistsBandsTracksAlbumArtCoverArtVideosApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String artistID = "artistID_example"; // String | ID of artist or band to retrieve albums from
    try {
      List<BandAlbums> result = apiInstance.musicAlbumsGet(accessToken, artistID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicArtistsBandsTracksAlbumArtCoverArtVideosApi#musicAlbumsGet");
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
| **accessToken** | **String**|  | |
| **artistID** | **String**| ID of artist or band to retrieve albums from | |

### Return type

[**List&lt;BandAlbums&gt;**](BandAlbums.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lists all albums from passed ArtistID |  -  |

<a id="musicArtistExtendedGet"></a>
# **musicArtistExtendedGet**
> List&lt;BandInfoExtended&gt; musicArtistExtendedGet(accessToken, name)

Provides extended information, which includes all known albums and music videos of artist / band

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    MusicArtistsBandsTracksAlbumArtCoverArtVideosApi apiInstance = new MusicArtistsBandsTracksAlbumArtCoverArtVideosApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String name = "name_example"; // String | 
    try {
      List<BandInfoExtended> result = apiInstance.musicArtistExtendedGet(accessToken, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicArtistsBandsTracksAlbumArtCoverArtVideosApi#musicArtistExtendedGet");
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
| **accessToken** | **String**|  | |
| **name** | **String**|  | |

### Return type

[**List&lt;BandInfoExtended&gt;**](BandInfoExtended.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Extended Information about band / artist |  -  |

<a id="musicByMusicBrainzGet"></a>
# **musicByMusicBrainzGet**
> List&lt;BandInfo&gt; musicByMusicBrainzGet(accessToken, MBID)

Get Artist / Band information on MusicBrainzID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    MusicArtistsBandsTracksAlbumArtCoverArtVideosApi apiInstance = new MusicArtistsBandsTracksAlbumArtCoverArtVideosApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String MBID = "MBID_example"; // String | MusicBrainzID
    try {
      List<BandInfo> result = apiInstance.musicByMusicBrainzGet(accessToken, MBID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicArtistsBandsTracksAlbumArtCoverArtVideosApi#musicByMusicBrainzGet");
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
| **accessToken** | **String**|  | |
| **MBID** | **String**| MusicBrainzID | |

### Return type

[**List&lt;BandInfo&gt;**](BandInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about band / artist based on MusicBrainzID |  -  |

<a id="musicCDCoversGet"></a>
# **musicCDCoversGet**
> List&lt;CDCoverArt&gt; musicCDCoversGet(accessToken, MBID)

Gets CD art for passed MusicBrainzID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    MusicArtistsBandsTracksAlbumArtCoverArtVideosApi apiInstance = new MusicArtistsBandsTracksAlbumArtCoverArtVideosApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String MBID = "MBID_example"; // String | MusicBrainzID
    try {
      List<CDCoverArt> result = apiInstance.musicCDCoversGet(accessToken, MBID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicArtistsBandsTracksAlbumArtCoverArtVideosApi#musicCDCoversGet");
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
| **accessToken** | **String**|  | |
| **MBID** | **String**| MusicBrainzID | |

### Return type

[**List&lt;CDCoverArt&gt;**](CDCoverArt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets CD Cover Art for album |  -  |

<a id="musicCoverArtByNameGet"></a>
# **musicCoverArtByNameGet**
> ArtistArt musicCoverArtByNameGet(accessToken, name)

Retrieves artist / band Banner and logo based on artist or bandname

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    MusicArtistsBandsTracksAlbumArtCoverArtVideosApi apiInstance = new MusicArtistsBandsTracksAlbumArtCoverArtVideosApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String name = "name_example"; // String | Name of artist or band
    try {
      ArtistArt result = apiInstance.musicCoverArtByNameGet(accessToken, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicArtistsBandsTracksAlbumArtCoverArtVideosApi#musicCoverArtByNameGet");
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
| **accessToken** | **String**|  | |
| **name** | **String**| Name of artist or band | |

### Return type

[**ArtistArt**](ArtistArt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets art for passed arist or bandname |  -  |

<a id="musicCoverArtGet"></a>
# **musicCoverArtGet**
> ArtistArt musicCoverArtGet(accessToken, artistID)

Retrieves artist / band Banner and logo based on ArtistID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    MusicArtistsBandsTracksAlbumArtCoverArtVideosApi apiInstance = new MusicArtistsBandsTracksAlbumArtCoverArtVideosApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String artistID = "artistID_example"; // String | ArtistID of artist or band
    try {
      ArtistArt result = apiInstance.musicCoverArtGet(accessToken, artistID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicArtistsBandsTracksAlbumArtCoverArtVideosApi#musicCoverArtGet");
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
| **accessToken** | **String**|  | |
| **artistID** | **String**| ArtistID of artist or band | |

### Return type

[**ArtistArt**](ArtistArt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets art for passed ArtistID |  -  |

<a id="musicGet"></a>
# **musicGet**
> List&lt;BandInfo&gt; musicGet(accessToken, name)

Get information about passed band name or artist

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    MusicArtistsBandsTracksAlbumArtCoverArtVideosApi apiInstance = new MusicArtistsBandsTracksAlbumArtCoverArtVideosApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String name = "name_example"; // String | Name (or part) of band or artist name
    try {
      List<BandInfo> result = apiInstance.musicGet(accessToken, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicArtistsBandsTracksAlbumArtCoverArtVideosApi#musicGet");
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
| **accessToken** | **String**|  | |
| **name** | **String**| Name (or part) of band or artist name | |

### Return type

[**List&lt;BandInfo&gt;**](BandInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about band / artist |  -  |

<a id="musicLyricsBySongGet"></a>
# **musicLyricsBySongGet**
> List&lt;Lyric&gt; musicLyricsBySongGet(accessToken, song)

Get lyrics on song title

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    MusicArtistsBandsTracksAlbumArtCoverArtVideosApi apiInstance = new MusicArtistsBandsTracksAlbumArtCoverArtVideosApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String song = "song_example"; // String | Name or part of song name
    try {
      List<Lyric> result = apiInstance.musicLyricsBySongGet(accessToken, song);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicArtistsBandsTracksAlbumArtCoverArtVideosApi#musicLyricsBySongGet");
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
| **accessToken** | **String**|  | |
| **song** | **String**| Name or part of song name | |

### Return type

[**List&lt;Lyric&gt;**](Lyric.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | lyric(s) for requested song |  -  |

<a id="musicLyricsGet"></a>
# **musicLyricsGet**
> List&lt;Lyric&gt; musicLyricsGet(accessToken, name)

Get lyrics for band or artist (record set limited to 25)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    MusicArtistsBandsTracksAlbumArtCoverArtVideosApi apiInstance = new MusicArtistsBandsTracksAlbumArtCoverArtVideosApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String name = "name_example"; // String | Name (or partial) of band or artist (record set limited to 25)
    try {
      List<Lyric> result = apiInstance.musicLyricsGet(accessToken, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicArtistsBandsTracksAlbumArtCoverArtVideosApi#musicLyricsGet");
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
| **accessToken** | **String**|  | |
| **name** | **String**| Name (or partial) of band or artist (record set limited to 25) | |

### Return type

[**List&lt;Lyric&gt;**](Lyric.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | lyric(s) for requested artist / band |  -  |

<a id="musicLyricsbyAlbumIDGet"></a>
# **musicLyricsbyAlbumIDGet**
> List&lt;Lyric&gt; musicLyricsbyAlbumIDGet(accessToken, albumID)

Returns all lyrics for requested AlbumID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    MusicArtistsBandsTracksAlbumArtCoverArtVideosApi apiInstance = new MusicArtistsBandsTracksAlbumArtCoverArtVideosApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String albumID = "albumID_example"; // String | 
    try {
      List<Lyric> result = apiInstance.musicLyricsbyAlbumIDGet(accessToken, albumID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicArtistsBandsTracksAlbumArtCoverArtVideosApi#musicLyricsbyAlbumIDGet");
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
| **accessToken** | **String**|  | |
| **albumID** | **String**|  | |

### Return type

[**List&lt;Lyric&gt;**](Lyric.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | lyric(s) for requested albumID |  -  |

<a id="musicTracksGet"></a>
# **musicTracksGet**
> List&lt;AlbumTracks&gt; musicTracksGet(accessToken, albumID)

Get all tracks from requested album

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    MusicArtistsBandsTracksAlbumArtCoverArtVideosApi apiInstance = new MusicArtistsBandsTracksAlbumArtCoverArtVideosApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String albumID = "albumID_example"; // String | AlbumID (can be retrieved via album endpoint)
    try {
      List<AlbumTracks> result = apiInstance.musicTracksGet(accessToken, albumID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicArtistsBandsTracksAlbumArtCoverArtVideosApi#musicTracksGet");
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
| **accessToken** | **String**|  | |
| **albumID** | **String**| AlbumID (can be retrieved via album endpoint) | |

### Return type

[**List&lt;AlbumTracks&gt;**](AlbumTracks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lists all tracks on album from passed AlbumID |  -  |

