# MusicApi

All URIs are relative to *https://rms.api.bbc.co.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deletePersonalisedMusicFavouritesByTypeById**](MusicApi.md#deletePersonalisedMusicFavouritesByTypeById) | **DELETE** /my/music/favourites/{type}/{id} | Favourite Track or Clip |
| [**deletePersonalisedMusicFollowsByTypeById**](MusicApi.md#deletePersonalisedMusicFollowsByTypeById) | **DELETE** /my/music/follows/{type}/{id} | Followed Network, Category, Artist, Playlist and Genre |
| [**getMusicPopularArtistById**](MusicApi.md#getMusicPopularArtistById) | **GET** /music/popular/artists/{id} | Single Artist Popularity |
| [**getMusicPopularArtists**](MusicApi.md#getMusicPopularArtists) | **GET** /music/popular/artists | Popular Artists |
| [**getMusicPopularPlaylistById**](MusicApi.md#getMusicPopularPlaylistById) | **GET** /music/popular/playlists/{id} | Single Playlist Popularity |
| [**getMusicPopularPlaylists**](MusicApi.md#getMusicPopularPlaylists) | **GET** /music/popular/playlists | Popular Playlists |
| [**getMusicPopularTrackById**](MusicApi.md#getMusicPopularTrackById) | **GET** /music/popular/tracks/{id} | Single Track Popularity |
| [**getMusicPopularTracks**](MusicApi.md#getMusicPopularTracks) | **GET** /music/popular/tracks | Popular Tracks |
| [**getPersonalisedMusicFavourites**](MusicApi.md#getPersonalisedMusicFavourites) | **GET** /my/music/favourites | Favourite Tracks or Clips |
| [**getPersonalisedMusicFavouritesByType**](MusicApi.md#getPersonalisedMusicFavouritesByType) | **GET** /my/music/favourites/{type} | Favourite Tracks or Clips by Type |
| [**getPersonalisedMusicFavouritesByTypeById**](MusicApi.md#getPersonalisedMusicFavouritesByTypeById) | **GET** /my/music/favourites/{type}/{id} | Favourite Track or Clip |
| [**getPersonalisedMusicFollows**](MusicApi.md#getPersonalisedMusicFollows) | **GET** /my/music/follows | Followed Networks, Categories, Artists, Playlists and Genres |
| [**getPersonalisedMusicFollowsByType**](MusicApi.md#getPersonalisedMusicFollowsByType) | **GET** /my/music/follows/{type} | Followed Networks, Categories, Artists, Playlists and Genres by Type |
| [**getPersonalisedMusicFollowsByTypeById**](MusicApi.md#getPersonalisedMusicFollowsByTypeById) | **GET** /my/music/follows/{type}/{id} | Followed Network, Category, Artist, Playlist and Genre |
| [**postPersonalisedMusicFavouritesBatch**](MusicApi.md#postPersonalisedMusicFavouritesBatch) | **POST** /my/music/favourites | Favourite Tracks or Clips |
| [**postPersonalisedMusicFavouritesByTypeById**](MusicApi.md#postPersonalisedMusicFavouritesByTypeById) | **POST** /my/music/favourites/{type}/{id} | Favourite Track or Clip |
| [**postPersonalisedMusicFollowsBatch**](MusicApi.md#postPersonalisedMusicFollowsBatch) | **POST** /my/music/follows | Followed Networks, Categories, Artists, Playlists and Genres |
| [**postPersonalisedMusicFollowsByTypeById**](MusicApi.md#postPersonalisedMusicFollowsByTypeById) | **POST** /my/music/follows/{type}/{id} | Followed Network, Category, Artist, Playlist and Genre |
| [**putPersonalisedMusicFavouritesBatch**](MusicApi.md#putPersonalisedMusicFavouritesBatch) | **PUT** /my/music/favourites | Favourite Tracks or Clips |
| [**putPersonalisedMusicFavouritesByTypeById**](MusicApi.md#putPersonalisedMusicFavouritesByTypeById) | **PUT** /my/music/favourites/{type}/{id} | Favourite Track or Clip |
| [**putPersonalisedMusicFollowsBatch**](MusicApi.md#putPersonalisedMusicFollowsBatch) | **PUT** /my/music/follows | Followed Networks, Categories, Artists, Playlists and Genres |
| [**putPersonalisedMusicFollowsByTypeById**](MusicApi.md#putPersonalisedMusicFollowsByTypeById) | **PUT** /my/music/follows/{type}/{id} | Followed Network, Category, Artist, Playlist and Genre |


<a id="deletePersonalisedMusicFavouritesByTypeById"></a>
# **deletePersonalisedMusicFavouritesByTypeById**
> PersonalisedMusicSuccess deletePersonalisedMusicFavouritesByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id)

Favourite Track or Clip

Delete track or clip from a BBC Music user favourites. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicApi apiInstance = new MusicApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String type = "clips"; // String | Supported Music favourite types: Clips or Tracks
    String id = "id_example"; // String | Clip PID or Track ID
    try {
      PersonalisedMusicSuccess result = apiInstance.deletePersonalisedMusicFavouritesByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicApi#deletePersonalisedMusicFavouritesByTypeById");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **type** | **String**| Supported Music favourite types: Clips or Tracks | [enum: clips, tracks] |
| **id** | **String**| Clip PID or Track ID | |

### Return type

[**PersonalisedMusicSuccess**](PersonalisedMusicSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="deletePersonalisedMusicFollowsByTypeById"></a>
# **deletePersonalisedMusicFollowsByTypeById**
> PersonalisedMusicSuccess deletePersonalisedMusicFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, musicData, musicContext, musicWithinUk)

Followed Network, Category, Artist, Playlist and Genre

Remove a single network, category, artist, playlist, network, genre or service entity is in a users follows 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicApi apiInstance = new MusicApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String type = "playlists"; // String | Supported Music follows types: Playlists, Services, Genres & Artists
    String id = "id_example"; // String | Playlists, Services, Networks, Genres, Categories or Artists ID
    Boolean musicData = true; // Boolean | Omits music data from the response, defaults to true
    String musicContext = "events"; // String | Specify context to be passed to Music API
    Boolean musicWithinUk = true; // Boolean | Specify location to be passed to Music API
    try {
      PersonalisedMusicSuccess result = apiInstance.deletePersonalisedMusicFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, musicData, musicContext, musicWithinUk);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicApi#deletePersonalisedMusicFollowsByTypeById");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **type** | **String**| Supported Music follows types: Playlists, Services, Genres &amp; Artists | [enum: playlists, services, networks, genres, categories, artists] |
| **id** | **String**| Playlists, Services, Networks, Genres, Categories or Artists ID | |
| **musicData** | **Boolean**| Omits music data from the response, defaults to true | [optional] |
| **musicContext** | **String**| Specify context to be passed to Music API | [optional] [enum: events, ivote, music, musicplaylist, programmes, radio, unknown] |
| **musicWithinUk** | **Boolean**| Specify location to be passed to Music API | [optional] |

### Return type

[**PersonalisedMusicSuccess**](PersonalisedMusicSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getMusicPopularArtistById"></a>
# **getMusicPopularArtistById**
> MusicPopularityArtists getMusicPopularArtistById(xAPIKey, id, since, until, decomposed)

Single Artist Popularity

Popularity Artist By Id 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicApi apiInstance = new MusicApi(defaultClient);
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String id = "id_example"; // String | MusicBrainz Id - Used to get single resource score
    String since = "since_example"; // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now
    String until = "until_example"; // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given 'since' and 'until' date params
    Boolean decomposed = true; // Boolean | In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is >= 31 days
    try {
      MusicPopularityArtists result = apiInstance.getMusicPopularArtistById(xAPIKey, id, since, until, decomposed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicApi#getMusicPopularArtistById");
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
| **xAPIKey** | **String**| API_KEY | |
| **id** | **String**| MusicBrainz Id - Used to get single resource score | |
| **since** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now | [optional] |
| **until** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given &#39;since&#39; and &#39;until&#39; date params | [optional] |
| **decomposed** | **Boolean**| In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is &gt;&#x3D; 31 days | [optional] |

### Return type

[**MusicPopularityArtists**](MusicPopularityArtists.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getMusicPopularArtists"></a>
# **getMusicPopularArtists**
> MusicPopularityArtists getMusicPopularArtists(xAPIKey, since, until, decomposed, offset, limit)

Popular Artists

List of Most Popular artists from BBC Music. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicApi apiInstance = new MusicApi(defaultClient);
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String since = "since_example"; // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now
    String until = "until_example"; // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given 'since' and 'until' date params
    Boolean decomposed = true; // Boolean | In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is >= 31 days
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    try {
      MusicPopularityArtists result = apiInstance.getMusicPopularArtists(xAPIKey, since, until, decomposed, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicApi#getMusicPopularArtists");
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
| **xAPIKey** | **String**| API_KEY | |
| **since** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now | [optional] |
| **until** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given &#39;since&#39; and &#39;until&#39; date params | [optional] |
| **decomposed** | **Boolean**| In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is &gt;&#x3D; 31 days | [optional] |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |

### Return type

[**MusicPopularityArtists**](MusicPopularityArtists.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getMusicPopularPlaylistById"></a>
# **getMusicPopularPlaylistById**
> MusicPopularityPlaylists getMusicPopularPlaylistById(xAPIKey, id, since, until, decomposed)

Single Playlist Popularity

Popular playlist by Id 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicApi apiInstance = new MusicApi(defaultClient);
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String id = "id_example"; // String | BBC Music Playlist Id - Used to get single resource score
    String since = "since_example"; // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now
    String until = "until_example"; // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given 'since' and 'until' date params
    Boolean decomposed = true; // Boolean | In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is >= 31 days
    try {
      MusicPopularityPlaylists result = apiInstance.getMusicPopularPlaylistById(xAPIKey, id, since, until, decomposed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicApi#getMusicPopularPlaylistById");
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
| **xAPIKey** | **String**| API_KEY | |
| **id** | **String**| BBC Music Playlist Id - Used to get single resource score | |
| **since** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now | [optional] |
| **until** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given &#39;since&#39; and &#39;until&#39; date params | [optional] |
| **decomposed** | **Boolean**| In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is &gt;&#x3D; 31 days | [optional] |

### Return type

[**MusicPopularityPlaylists**](MusicPopularityPlaylists.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getMusicPopularPlaylists"></a>
# **getMusicPopularPlaylists**
> MusicPopularityPlaylists getMusicPopularPlaylists(xAPIKey, since, until, decomposed, offset, limit)

Popular Playlists

List of Most Popular playlists from BBC Music. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicApi apiInstance = new MusicApi(defaultClient);
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String since = "since_example"; // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now
    String until = "until_example"; // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given 'since' and 'until' date params
    Boolean decomposed = true; // Boolean | In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is >= 31 days
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    try {
      MusicPopularityPlaylists result = apiInstance.getMusicPopularPlaylists(xAPIKey, since, until, decomposed, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicApi#getMusicPopularPlaylists");
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
| **xAPIKey** | **String**| API_KEY | |
| **since** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now | [optional] |
| **until** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given &#39;since&#39; and &#39;until&#39; date params | [optional] |
| **decomposed** | **Boolean**| In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is &gt;&#x3D; 31 days | [optional] |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |

### Return type

[**MusicPopularityPlaylists**](MusicPopularityPlaylists.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getMusicPopularTrackById"></a>
# **getMusicPopularTrackById**
> MusicPopularityTracks getMusicPopularTrackById(xAPIKey, id, since, until, network, programme, artist, decomposed)

Single Track Popularity

Popular Track for BBC Music 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicApi apiInstance = new MusicApi(defaultClient);
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String id = "id_example"; // String | BBC Music Track Id - Used to get single resource score
    String since = "since_example"; // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now
    String until = "until_example"; // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given 'since' and 'until' date params
    String network = "network_example"; // String | Return items with given Network ID
    String programme = "programme_example"; // String | Items with given Programme Pid
    String artist = "artist_example"; // String | MusicBrainz artist ID
    Boolean decomposed = true; // Boolean | In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is >= 31 days
    try {
      MusicPopularityTracks result = apiInstance.getMusicPopularTrackById(xAPIKey, id, since, until, network, programme, artist, decomposed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicApi#getMusicPopularTrackById");
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
| **xAPIKey** | **String**| API_KEY | |
| **id** | **String**| BBC Music Track Id - Used to get single resource score | |
| **since** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now | [optional] |
| **until** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given &#39;since&#39; and &#39;until&#39; date params | [optional] |
| **network** | **String**| Return items with given Network ID | [optional] |
| **programme** | **String**| Items with given Programme Pid | [optional] |
| **artist** | **String**| MusicBrainz artist ID | [optional] |
| **decomposed** | **Boolean**| In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is &gt;&#x3D; 31 days | [optional] |

### Return type

[**MusicPopularityTracks**](MusicPopularityTracks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getMusicPopularTracks"></a>
# **getMusicPopularTracks**
> MusicPopularityTracks getMusicPopularTracks(xAPIKey, since, until, network, programme, artist, decomposed, offset, limit)

Popular Tracks

List of popular tracks for BBC Music. Filter by time, network, artist, playlist or programme. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicApi apiInstance = new MusicApi(defaultClient);
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String since = "since_example"; // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now
    String until = "until_example"; // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given 'since' and 'until' date params
    String network = "network_example"; // String | Return items with given Network ID
    String programme = "programme_example"; // String | Items with given Programme Pid
    String artist = "artist_example"; // String | MusicBrainz artist ID
    Boolean decomposed = true; // Boolean | In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is >= 31 days
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    try {
      MusicPopularityTracks result = apiInstance.getMusicPopularTracks(xAPIKey, since, until, network, programme, artist, decomposed, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicApi#getMusicPopularTracks");
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
| **xAPIKey** | **String**| API_KEY | |
| **since** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now | [optional] |
| **until** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given &#39;since&#39; and &#39;until&#39; date params | [optional] |
| **network** | **String**| Return items with given Network ID | [optional] |
| **programme** | **String**| Items with given Programme Pid | [optional] |
| **artist** | **String**| MusicBrainz artist ID | [optional] |
| **decomposed** | **Boolean**| In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is &gt;&#x3D; 31 days | [optional] |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |

### Return type

[**MusicPopularityTracks**](MusicPopularityTracks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getPersonalisedMusicFavourites"></a>
# **getPersonalisedMusicFavourites**
> PersonalisedMusicResponse getPersonalisedMusicFavourites(authorization, xAuthenticationProvider, xAPIKey, offset, limit, action, musicData)

Favourite Tracks or Clips

List of favourited tracks and clips for a given user for BBC Music. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicApi apiInstance = new MusicApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    String action = "favourited"; // String | Filters activities based on the type of action
    Boolean musicData = true; // Boolean | Omits music data from the response, defaults to true
    try {
      PersonalisedMusicResponse result = apiInstance.getPersonalisedMusicFavourites(authorization, xAuthenticationProvider, xAPIKey, offset, limit, action, musicData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicApi#getPersonalisedMusicFavourites");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |
| **action** | **String**| Filters activities based on the type of action | [optional] [enum: favourited, unfavourited] |
| **musicData** | **Boolean**| Omits music data from the response, defaults to true | [optional] |

### Return type

[**PersonalisedMusicResponse**](PersonalisedMusicResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getPersonalisedMusicFavouritesByType"></a>
# **getPersonalisedMusicFavouritesByType**
> PersonalisedMusicResponse getPersonalisedMusicFavouritesByType(authorization, xAuthenticationProvider, xAPIKey, type, action, offset, limit)

Favourite Tracks or Clips by Type

List of favourited tracks or clips for a given user for BBC Music. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicApi apiInstance = new MusicApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String type = "clips"; // String | Supported Music favourite types: Clips or Tracks
    String action = "favourited"; // String | Filters activities based on the type of action
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    try {
      PersonalisedMusicResponse result = apiInstance.getPersonalisedMusicFavouritesByType(authorization, xAuthenticationProvider, xAPIKey, type, action, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicApi#getPersonalisedMusicFavouritesByType");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **type** | **String**| Supported Music favourite types: Clips or Tracks | [enum: clips, tracks] |
| **action** | **String**| Filters activities based on the type of action | [optional] [enum: favourited, unfavourited] |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |

### Return type

[**PersonalisedMusicResponse**](PersonalisedMusicResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getPersonalisedMusicFavouritesByTypeById"></a>
# **getPersonalisedMusicFavouritesByTypeById**
> PersonalisedMusicResponse getPersonalisedMusicFavouritesByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id)

Favourite Track or Clip

Check to see if a single track or clip entity is in a users favourites - determines UX of add button. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicApi apiInstance = new MusicApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String type = "clips"; // String | Supported Music favourite types: Clips or Tracks
    String id = "id_example"; // String | Clip PID or Track ID
    try {
      PersonalisedMusicResponse result = apiInstance.getPersonalisedMusicFavouritesByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicApi#getPersonalisedMusicFavouritesByTypeById");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **type** | **String**| Supported Music favourite types: Clips or Tracks | [enum: clips, tracks] |
| **id** | **String**| Clip PID or Track ID | |

### Return type

[**PersonalisedMusicResponse**](PersonalisedMusicResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getPersonalisedMusicFollows"></a>
# **getPersonalisedMusicFollows**
> PersonalisedMusicResponse getPersonalisedMusicFollows(authorization, xAuthenticationProvider, xAPIKey, action, musicData, musicContext, musicWithinUk, offset, limit)

Followed Networks, Categories, Artists, Playlists and Genres

List of followed networks, categories, artists, playlists and genres for a given user for BBC Music. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicApi apiInstance = new MusicApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String action = "followed"; // String | Filters activities based on the type of action
    Boolean musicData = true; // Boolean | Omits music data from the response, defaults to true
    String musicContext = "events"; // String | Specify context to be passed to Music API
    Boolean musicWithinUk = true; // Boolean | Specify location to be passed to Music API
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    try {
      PersonalisedMusicResponse result = apiInstance.getPersonalisedMusicFollows(authorization, xAuthenticationProvider, xAPIKey, action, musicData, musicContext, musicWithinUk, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicApi#getPersonalisedMusicFollows");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **action** | **String**| Filters activities based on the type of action | [optional] [enum: followed, unfollowed] |
| **musicData** | **Boolean**| Omits music data from the response, defaults to true | [optional] |
| **musicContext** | **String**| Specify context to be passed to Music API | [optional] [enum: events, ivote, music, musicplaylist, programmes, radio, unknown] |
| **musicWithinUk** | **Boolean**| Specify location to be passed to Music API | [optional] |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |

### Return type

[**PersonalisedMusicResponse**](PersonalisedMusicResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getPersonalisedMusicFollowsByType"></a>
# **getPersonalisedMusicFollowsByType**
> PersonalisedMusicResponse getPersonalisedMusicFollowsByType(authorization, xAuthenticationProvider, xAPIKey, type, action, musicData, musicContext, musicWithinUk, offset, limit)

Followed Networks, Categories, Artists, Playlists and Genres by Type

List of followed networks, categories, artists, playlists, networks, genres, categories or services for a given BBC Music user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicApi apiInstance = new MusicApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String type = "playlists"; // String | Supported Music follows types: Playlists, Services, Genres & Artists
    String action = "followed"; // String | Filters activities based on the type of action
    Boolean musicData = true; // Boolean | Omits music data from the response, defaults to true
    String musicContext = "events"; // String | Specify context to be passed to Music API
    Boolean musicWithinUk = true; // Boolean | Specify location to be passed to Music API
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    try {
      PersonalisedMusicResponse result = apiInstance.getPersonalisedMusicFollowsByType(authorization, xAuthenticationProvider, xAPIKey, type, action, musicData, musicContext, musicWithinUk, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicApi#getPersonalisedMusicFollowsByType");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **type** | **String**| Supported Music follows types: Playlists, Services, Genres &amp; Artists | [enum: playlists, services, networks, genres, categories, artists] |
| **action** | **String**| Filters activities based on the type of action | [optional] [enum: followed, unfollowed] |
| **musicData** | **Boolean**| Omits music data from the response, defaults to true | [optional] |
| **musicContext** | **String**| Specify context to be passed to Music API | [optional] [enum: events, ivote, music, musicplaylist, programmes, radio, unknown] |
| **musicWithinUk** | **Boolean**| Specify location to be passed to Music API | [optional] |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |

### Return type

[**PersonalisedMusicResponse**](PersonalisedMusicResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getPersonalisedMusicFollowsByTypeById"></a>
# **getPersonalisedMusicFollowsByTypeById**
> PersonalisedMusicResponse getPersonalisedMusicFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, musicData, musicContext, musicWithinUk)

Followed Network, Category, Artist, Playlist and Genre

Check to see if a single network, category, artist, playlist, network, genre or service entity is in a users follows - determines UX of add button. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicApi apiInstance = new MusicApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String type = "playlists"; // String | Supported Music follows types: Playlists, Services, Genres & Artists
    String id = "id_example"; // String | Playlists, Services, Networks, Genres, Categories or Artists ID
    Boolean musicData = true; // Boolean | Omits music data from the response, defaults to true
    String musicContext = "events"; // String | Specify context to be passed to Music API
    Boolean musicWithinUk = true; // Boolean | Specify location to be passed to Music API
    try {
      PersonalisedMusicResponse result = apiInstance.getPersonalisedMusicFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, musicData, musicContext, musicWithinUk);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicApi#getPersonalisedMusicFollowsByTypeById");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **type** | **String**| Supported Music follows types: Playlists, Services, Genres &amp; Artists | [enum: playlists, services, networks, genres, categories, artists] |
| **id** | **String**| Playlists, Services, Networks, Genres, Categories or Artists ID | |
| **musicData** | **Boolean**| Omits music data from the response, defaults to true | [optional] |
| **musicContext** | **String**| Specify context to be passed to Music API | [optional] [enum: events, ivote, music, musicplaylist, programmes, radio, unknown] |
| **musicWithinUk** | **Boolean**| Specify location to be passed to Music API | [optional] |

### Return type

[**PersonalisedMusicResponse**](PersonalisedMusicResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="postPersonalisedMusicFavouritesBatch"></a>
# **postPersonalisedMusicFavouritesBatch**
> PersonalisedMusicResponse postPersonalisedMusicFavouritesBatch(authorization, xAuthenticationProvider, xAPIKey, body)

Favourite Tracks or Clips

Add multiple tracks and/or clips to a BBC Music user&#39;s favourites.  N.B. Any HTML tags submitted in metadata will be removed 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicApi apiInstance = new MusicApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    List<PersonalisedMusicBatchRequest> body = Arrays.asList(); // List<PersonalisedMusicBatchRequest> | Action favourited or unfavourited
    try {
      PersonalisedMusicResponse result = apiInstance.postPersonalisedMusicFavouritesBatch(authorization, xAuthenticationProvider, xAPIKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicApi#postPersonalisedMusicFavouritesBatch");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **body** | [**List&lt;PersonalisedMusicBatchRequest&gt;**](PersonalisedMusicBatchRequest.md)| Action favourited or unfavourited | |

### Return type

[**PersonalisedMusicResponse**](PersonalisedMusicResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="postPersonalisedMusicFavouritesByTypeById"></a>
# **postPersonalisedMusicFavouritesByTypeById**
> PersonalisedMusicResponse postPersonalisedMusicFavouritesByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, body)

Favourite Track or Clip

Add track or clip to a BBC Music user favourites.  N.B. Any HTML tags submitted in metadata will be removed 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicApi apiInstance = new MusicApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String type = "clips"; // String | Supported Music favourite types: Clips or Tracks
    String id = "id_example"; // String | Clip PID or Track ID
    PersonalisedMusicRequest body = new PersonalisedMusicRequest(); // PersonalisedMusicRequest | Action favourited or unfavourited
    try {
      PersonalisedMusicResponse result = apiInstance.postPersonalisedMusicFavouritesByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicApi#postPersonalisedMusicFavouritesByTypeById");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **type** | **String**| Supported Music favourite types: Clips or Tracks | [enum: clips, tracks] |
| **id** | **String**| Clip PID or Track ID | |
| **body** | [**PersonalisedMusicRequest**](PersonalisedMusicRequest.md)| Action favourited or unfavourited | |

### Return type

[**PersonalisedMusicResponse**](PersonalisedMusicResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="postPersonalisedMusicFollowsBatch"></a>
# **postPersonalisedMusicFollowsBatch**
> PersonalisedMusicSuccess postPersonalisedMusicFollowsBatch(authorization, xAuthenticationProvider, xAPIKey, body, action, musicData, musicContext, musicWithinUk)

Followed Networks, Categories, Artists, Playlists and Genres

Add networks, categories, artists, playlists, networks, genres or services in a users follows  N.B. Any HTML tags submitted in metadata will be removed 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicApi apiInstance = new MusicApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    List<PersonalisedMusicBatchRequest> body = Arrays.asList(); // List<PersonalisedMusicBatchRequest> | Action followed or unfollowed
    String action = "followed"; // String | Filters activities based on the type of action
    Boolean musicData = true; // Boolean | Omits music data from the response, defaults to true
    String musicContext = "events"; // String | Specify context to be passed to Music API
    Boolean musicWithinUk = true; // Boolean | Specify location to be passed to Music API
    try {
      PersonalisedMusicSuccess result = apiInstance.postPersonalisedMusicFollowsBatch(authorization, xAuthenticationProvider, xAPIKey, body, action, musicData, musicContext, musicWithinUk);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicApi#postPersonalisedMusicFollowsBatch");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **body** | [**List&lt;PersonalisedMusicBatchRequest&gt;**](PersonalisedMusicBatchRequest.md)| Action followed or unfollowed | |
| **action** | **String**| Filters activities based on the type of action | [optional] [enum: followed, unfollowed] |
| **musicData** | **Boolean**| Omits music data from the response, defaults to true | [optional] |
| **musicContext** | **String**| Specify context to be passed to Music API | [optional] [enum: events, ivote, music, musicplaylist, programmes, radio, unknown] |
| **musicWithinUk** | **Boolean**| Specify location to be passed to Music API | [optional] |

### Return type

[**PersonalisedMusicSuccess**](PersonalisedMusicSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="postPersonalisedMusicFollowsByTypeById"></a>
# **postPersonalisedMusicFollowsByTypeById**
> PersonalisedMusicSuccess postPersonalisedMusicFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, body, musicData, musicContext, musicWithinUk)

Followed Network, Category, Artist, Playlist and Genre

Add a single network, category, artist, playlist, network, genre or service entity is in a users follows  N.B. Any HTML tags submitted in metadata will be removed 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicApi apiInstance = new MusicApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String type = "playlists"; // String | Supported Music follows types: Playlists, Services, Genres & Artists
    String id = "id_example"; // String | Playlists, Services, Networks, Genres, Categories or Artists ID
    PersonalisedMusicRequest body = new PersonalisedMusicRequest(); // PersonalisedMusicRequest | Action followed or unfollowed
    Boolean musicData = true; // Boolean | Omits music data from the response, defaults to true
    String musicContext = "events"; // String | Specify context to be passed to Music API
    Boolean musicWithinUk = true; // Boolean | Specify location to be passed to Music API
    try {
      PersonalisedMusicSuccess result = apiInstance.postPersonalisedMusicFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, body, musicData, musicContext, musicWithinUk);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicApi#postPersonalisedMusicFollowsByTypeById");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **type** | **String**| Supported Music follows types: Playlists, Services, Genres &amp; Artists | [enum: playlists, services, networks, genres, categories, artists] |
| **id** | **String**| Playlists, Services, Networks, Genres, Categories or Artists ID | |
| **body** | [**PersonalisedMusicRequest**](PersonalisedMusicRequest.md)| Action followed or unfollowed | |
| **musicData** | **Boolean**| Omits music data from the response, defaults to true | [optional] |
| **musicContext** | **String**| Specify context to be passed to Music API | [optional] [enum: events, ivote, music, musicplaylist, programmes, radio, unknown] |
| **musicWithinUk** | **Boolean**| Specify location to be passed to Music API | [optional] |

### Return type

[**PersonalisedMusicSuccess**](PersonalisedMusicSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="putPersonalisedMusicFavouritesBatch"></a>
# **putPersonalisedMusicFavouritesBatch**
> PersonalisedMusicSuccess putPersonalisedMusicFavouritesBatch(authorization, xAuthenticationProvider, xAPIKey, body)

Favourite Tracks or Clips

Update tracks or clips from a BBC Music user favourites.  N.B. Any HTML tags submitted in metadata will be removed 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicApi apiInstance = new MusicApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    List<PersonalisedMusicBatchRequest> body = Arrays.asList(); // List<PersonalisedMusicBatchRequest> | Action favourited or unfavourited
    try {
      PersonalisedMusicSuccess result = apiInstance.putPersonalisedMusicFavouritesBatch(authorization, xAuthenticationProvider, xAPIKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicApi#putPersonalisedMusicFavouritesBatch");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **body** | [**List&lt;PersonalisedMusicBatchRequest&gt;**](PersonalisedMusicBatchRequest.md)| Action favourited or unfavourited | |

### Return type

[**PersonalisedMusicSuccess**](PersonalisedMusicSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="putPersonalisedMusicFavouritesByTypeById"></a>
# **putPersonalisedMusicFavouritesByTypeById**
> PersonalisedMusicSuccess putPersonalisedMusicFavouritesByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, body)

Favourite Track or Clip

Update tracks or clips from a BBC Music user favourites.  N.B. Any HTML tags submitted in metadata will be removed 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicApi apiInstance = new MusicApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String type = "clips"; // String | Supported Music favourite types: Clips or Tracks
    String id = "id_example"; // String | Clip PID or Track ID
    PersonalisedMusicRequest body = new PersonalisedMusicRequest(); // PersonalisedMusicRequest | Action favourited or unfavourited
    try {
      PersonalisedMusicSuccess result = apiInstance.putPersonalisedMusicFavouritesByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicApi#putPersonalisedMusicFavouritesByTypeById");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **type** | **String**| Supported Music favourite types: Clips or Tracks | [enum: clips, tracks] |
| **id** | **String**| Clip PID or Track ID | |
| **body** | [**PersonalisedMusicRequest**](PersonalisedMusicRequest.md)| Action favourited or unfavourited | |

### Return type

[**PersonalisedMusicSuccess**](PersonalisedMusicSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="putPersonalisedMusicFollowsBatch"></a>
# **putPersonalisedMusicFollowsBatch**
> PersonalisedMusicSuccess putPersonalisedMusicFollowsBatch(authorization, xAuthenticationProvider, xAPIKey, body, action, musicData, musicContext, musicWithinUk)

Followed Networks, Categories, Artists, Playlists and Genres

Update networks, categories, artists, playlists, networks, genres or services in a users follows  N.B. Any HTML tags submitted in metadata will be removed 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicApi apiInstance = new MusicApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    List<PersonalisedMusicBatchRequest> body = Arrays.asList(); // List<PersonalisedMusicBatchRequest> | Action followed or unfollowed
    String action = "followed"; // String | Filters activities based on the type of action
    Boolean musicData = true; // Boolean | Omits music data from the response, defaults to true
    String musicContext = "events"; // String | Specify context to be passed to Music API
    Boolean musicWithinUk = true; // Boolean | Specify location to be passed to Music API
    try {
      PersonalisedMusicSuccess result = apiInstance.putPersonalisedMusicFollowsBatch(authorization, xAuthenticationProvider, xAPIKey, body, action, musicData, musicContext, musicWithinUk);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicApi#putPersonalisedMusicFollowsBatch");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **body** | [**List&lt;PersonalisedMusicBatchRequest&gt;**](PersonalisedMusicBatchRequest.md)| Action followed or unfollowed | |
| **action** | **String**| Filters activities based on the type of action | [optional] [enum: followed, unfollowed] |
| **musicData** | **Boolean**| Omits music data from the response, defaults to true | [optional] |
| **musicContext** | **String**| Specify context to be passed to Music API | [optional] [enum: events, ivote, music, musicplaylist, programmes, radio, unknown] |
| **musicWithinUk** | **Boolean**| Specify location to be passed to Music API | [optional] |

### Return type

[**PersonalisedMusicSuccess**](PersonalisedMusicSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="putPersonalisedMusicFollowsByTypeById"></a>
# **putPersonalisedMusicFollowsByTypeById**
> PersonalisedMusicSuccess putPersonalisedMusicFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, body, musicData, musicContext, musicWithinUk)

Followed Network, Category, Artist, Playlist and Genre

Update a single network, category, artist, playlist, network, genre or service entity is in a users follows  N.B. Any HTML tags submitted in metadata will be removed 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    MusicApi apiInstance = new MusicApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAuthenticationProvider = "idv5"; // String | Authentication type
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String type = "playlists"; // String | Supported Music follows types: Playlists, Services, Genres & Artists
    String id = "id_example"; // String | Playlists, Services, Networks, Genres, Categories or Artists ID
    PersonalisedMusicRequest body = new PersonalisedMusicRequest(); // PersonalisedMusicRequest | Action followed or unfollowed
    Boolean musicData = true; // Boolean | Omits music data from the response, defaults to true
    String musicContext = "events"; // String | Specify context to be passed to Music API
    Boolean musicWithinUk = true; // Boolean | Specify location to be passed to Music API
    try {
      PersonalisedMusicSuccess result = apiInstance.putPersonalisedMusicFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, body, musicData, musicContext, musicWithinUk);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MusicApi#putPersonalisedMusicFollowsByTypeById");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAuthenticationProvider** | **String**| Authentication type | [default to idv5] |
| **xAPIKey** | **String**| API_KEY | |
| **type** | **String**| Supported Music follows types: Playlists, Services, Genres &amp; Artists | [enum: playlists, services, networks, genres, categories, artists] |
| **id** | **String**| Playlists, Services, Networks, Genres, Categories or Artists ID | |
| **body** | [**PersonalisedMusicRequest**](PersonalisedMusicRequest.md)| Action followed or unfollowed | |
| **musicData** | **Boolean**| Omits music data from the response, defaults to true | [optional] |
| **musicContext** | **String**| Specify context to be passed to Music API | [optional] [enum: events, ivote, music, musicplaylist, programmes, radio, unknown] |
| **musicWithinUk** | **Boolean**| Specify location to be passed to Music API | [optional] |

### Return type

[**PersonalisedMusicSuccess**](PersonalisedMusicSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

