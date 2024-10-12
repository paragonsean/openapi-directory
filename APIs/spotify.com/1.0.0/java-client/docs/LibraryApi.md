# LibraryApi

All URIs are relative to *https://api.spotify.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**changePlaylistDetails_0**](LibraryApi.md#changePlaylistDetails_0) | **PUT** /playlists/{playlist_id} | Change Playlist Details  |
| [**checkCurrentUserFollows_1**](LibraryApi.md#checkCurrentUserFollows_1) | **GET** /me/following/contains | Check If User Follows Artists or Users  |
| [**checkUsersSavedAlbums_0**](LibraryApi.md#checkUsersSavedAlbums_0) | **GET** /me/albums/contains | Check User&#39;s Saved Albums  |
| [**checkUsersSavedAudiobooks_0**](LibraryApi.md#checkUsersSavedAudiobooks_0) | **GET** /me/audiobooks/contains | Check User&#39;s Saved Audiobooks  |
| [**checkUsersSavedEpisodes_0**](LibraryApi.md#checkUsersSavedEpisodes_0) | **GET** /me/episodes/contains | Check User&#39;s Saved Episodes  |
| [**checkUsersSavedShows_0**](LibraryApi.md#checkUsersSavedShows_0) | **GET** /me/shows/contains | Check User&#39;s Saved Shows  |
| [**checkUsersSavedTracks_0**](LibraryApi.md#checkUsersSavedTracks_0) | **GET** /me/tracks/contains | Check User&#39;s Saved Tracks  |
| [**createPlaylist_0**](LibraryApi.md#createPlaylist_0) | **POST** /users/{user_id}/playlists | Create Playlist  |
| [**followArtistsUsers_1**](LibraryApi.md#followArtistsUsers_1) | **PUT** /me/following | Follow Artists or Users  |
| [**getAListOfCurrentUsersPlaylists_0**](LibraryApi.md#getAListOfCurrentUsersPlaylists_0) | **GET** /me/playlists | Get Current User&#39;s Playlists  |
| [**getFollowed_0**](LibraryApi.md#getFollowed_0) | **GET** /me/following | Get Followed Artists  |
| [**getUsersSavedAlbums_0**](LibraryApi.md#getUsersSavedAlbums_0) | **GET** /me/albums | Get User&#39;s Saved Albums  |
| [**getUsersSavedAudiobooks_0**](LibraryApi.md#getUsersSavedAudiobooks_0) | **GET** /me/audiobooks | Get User&#39;s Saved Audiobooks  |
| [**getUsersSavedEpisodes_0**](LibraryApi.md#getUsersSavedEpisodes_0) | **GET** /me/episodes | Get User&#39;s Saved Episodes  |
| [**getUsersSavedShows_0**](LibraryApi.md#getUsersSavedShows_0) | **GET** /me/shows | Get User&#39;s Saved Shows  |
| [**getUsersSavedTracks_0**](LibraryApi.md#getUsersSavedTracks_0) | **GET** /me/tracks | Get User&#39;s Saved Tracks  |
| [**getUsersTopArtistsAndTracks_1**](LibraryApi.md#getUsersTopArtistsAndTracks_1) | **GET** /me/top/{type} | Get User&#39;s Top Items  |
| [**removeAlbumsUser_0**](LibraryApi.md#removeAlbumsUser_0) | **DELETE** /me/albums | Remove Users&#39; Saved Albums  |
| [**removeAudiobooksUser_0**](LibraryApi.md#removeAudiobooksUser_0) | **DELETE** /me/audiobooks | Remove User&#39;s Saved Audiobooks  |
| [**removeEpisodesUser_0**](LibraryApi.md#removeEpisodesUser_0) | **DELETE** /me/episodes | Remove User&#39;s Saved Episodes  |
| [**removeShowsUser_0**](LibraryApi.md#removeShowsUser_0) | **DELETE** /me/shows | Remove User&#39;s Saved Shows  |
| [**removeTracksUser_0**](LibraryApi.md#removeTracksUser_0) | **DELETE** /me/tracks | Remove User&#39;s Saved Tracks  |
| [**saveAlbumsUser_0**](LibraryApi.md#saveAlbumsUser_0) | **PUT** /me/albums | Save Albums for Current User  |
| [**saveAudiobooksUser_0**](LibraryApi.md#saveAudiobooksUser_0) | **PUT** /me/audiobooks | Save Audiobooks for Current User  |
| [**saveEpisodesUser_0**](LibraryApi.md#saveEpisodesUser_0) | **PUT** /me/episodes | Save Episodes for Current User  |
| [**saveShowsUser_0**](LibraryApi.md#saveShowsUser_0) | **PUT** /me/shows | Save Shows for Current User  |
| [**saveTracksUser_0**](LibraryApi.md#saveTracksUser_0) | **PUT** /me/tracks | Save Tracks for Current User  |
| [**unfollowArtistsUsers_1**](LibraryApi.md#unfollowArtistsUsers_1) | **DELETE** /me/following | Unfollow Artists or Users  |


<a id="changePlaylistDetails_0"></a>
# **changePlaylistDetails_0**
> changePlaylistDetails_0(playlistId, changePlaylistDetailsRequest)

Change Playlist Details 

Change a playlist&#39;s name and public/private state. (The user must, of course, own the playlist.) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String playlistId = "3cEYpjA9oz9GiPac4AsH4n"; // String | 
    ChangePlaylistDetailsRequest changePlaylistDetailsRequest = new ChangePlaylistDetailsRequest(); // ChangePlaylistDetailsRequest | 
    try {
      apiInstance.changePlaylistDetails_0(playlistId, changePlaylistDetailsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#changePlaylistDetails_0");
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
| **playlistId** | **String**|  | |
| **changePlaylistDetailsRequest** | [**ChangePlaylistDetailsRequest**](ChangePlaylistDetailsRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Playlist updated |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="checkCurrentUserFollows_1"></a>
# **checkCurrentUserFollows_1**
> List&lt;Boolean&gt; checkCurrentUserFollows_1(type, ids)

Check If User Follows Artists or Users 

Check to see if the current user is following one or more artists or other Spotify users. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String type = "artist"; // String | 
    String ids = "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"; // String | 
    try {
      List<Boolean> result = apiInstance.checkCurrentUserFollows_1(type, ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#checkCurrentUserFollows_1");
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
| **type** | **String**|  | [enum: artist, user] |
| **ids** | **String**|  | |

### Return type

**List&lt;Boolean&gt;**

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array of booleans |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="checkUsersSavedAlbums_0"></a>
# **checkUsersSavedAlbums_0**
> List&lt;Boolean&gt; checkUsersSavedAlbums_0(ids)

Check User&#39;s Saved Albums 

Check if one or more albums is already saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String ids = "382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc"; // String | 
    try {
      List<Boolean> result = apiInstance.checkUsersSavedAlbums_0(ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#checkUsersSavedAlbums_0");
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
| **ids** | **String**|  | |

### Return type

**List&lt;Boolean&gt;**

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array of booleans |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="checkUsersSavedAudiobooks_0"></a>
# **checkUsersSavedAudiobooks_0**
> List&lt;Boolean&gt; checkUsersSavedAudiobooks_0(ids)

Check User&#39;s Saved Audiobooks 

Check if one or more audiobooks are already saved in the current Spotify user&#39;s library. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String ids = "18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe"; // String | 
    try {
      List<Boolean> result = apiInstance.checkUsersSavedAudiobooks_0(ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#checkUsersSavedAudiobooks_0");
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
| **ids** | **String**|  | |

### Return type

**List&lt;Boolean&gt;**

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array of booleans |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="checkUsersSavedEpisodes_0"></a>
# **checkUsersSavedEpisodes_0**
> List&lt;Boolean&gt; checkUsersSavedEpisodes_0(ids)

Check User&#39;s Saved Episodes 

Check if one or more episodes is already saved in the current Spotify user&#39;s &#39;Your Episodes&#39; library.&lt;br/&gt; This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer).. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String ids = "77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf"; // String | 
    try {
      List<Boolean> result = apiInstance.checkUsersSavedEpisodes_0(ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#checkUsersSavedEpisodes_0");
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
| **ids** | **String**|  | |

### Return type

**List&lt;Boolean&gt;**

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array of booleans |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="checkUsersSavedShows_0"></a>
# **checkUsersSavedShows_0**
> List&lt;Boolean&gt; checkUsersSavedShows_0(ids)

Check User&#39;s Saved Shows 

Check if one or more shows is already saved in the current Spotify user&#39;s library. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String ids = "5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ"; // String | 
    try {
      List<Boolean> result = apiInstance.checkUsersSavedShows_0(ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#checkUsersSavedShows_0");
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
| **ids** | **String**|  | |

### Return type

**List&lt;Boolean&gt;**

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array of booleans |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="checkUsersSavedTracks_0"></a>
# **checkUsersSavedTracks_0**
> List&lt;Boolean&gt; checkUsersSavedTracks_0(ids)

Check User&#39;s Saved Tracks 

Check if one or more tracks is already saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String ids = "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"; // String | 
    try {
      List<Boolean> result = apiInstance.checkUsersSavedTracks_0(ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#checkUsersSavedTracks_0");
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
| **ids** | **String**|  | |

### Return type

**List&lt;Boolean&gt;**

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array of booleans |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="createPlaylist_0"></a>
# **createPlaylist_0**
> PlaylistObject createPlaylist_0(userId, createPlaylistRequest)

Create Playlist 

Create a playlist for a Spotify user. (The playlist will be empty until you [add tracks](/documentation/web-api/reference/add-tracks-to-playlist).) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String userId = "smedjan"; // String | 
    CreatePlaylistRequest createPlaylistRequest = new CreatePlaylistRequest(); // CreatePlaylistRequest | 
    try {
      PlaylistObject result = apiInstance.createPlaylist_0(userId, createPlaylistRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#createPlaylist_0");
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
| **userId** | **String**|  | |
| **createPlaylistRequest** | [**CreatePlaylistRequest**](CreatePlaylistRequest.md)|  | [optional] |

### Return type

[**PlaylistObject**](PlaylistObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A playlist |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="followArtistsUsers_1"></a>
# **followArtistsUsers_1**
> followArtistsUsers_1(type, ids, followArtistsUsersRequest)

Follow Artists or Users 

Add the current user as a follower of one or more artists or other Spotify users. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String type = "artist"; // String | 
    String ids = "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"; // String | 
    FollowArtistsUsersRequest followArtistsUsersRequest = new FollowArtistsUsersRequest(); // FollowArtistsUsersRequest | 
    try {
      apiInstance.followArtistsUsers_1(type, ids, followArtistsUsersRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#followArtistsUsers_1");
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
| **type** | **String**|  | [enum: artist, user] |
| **ids** | **String**|  | |
| **followArtistsUsersRequest** | [**FollowArtistsUsersRequest**](FollowArtistsUsersRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Artist or user followed |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="getAListOfCurrentUsersPlaylists_0"></a>
# **getAListOfCurrentUsersPlaylists_0**
> PagingPlaylistObject getAListOfCurrentUsersPlaylists_0(limit, offset)

Get Current User&#39;s Playlists 

Get a list of the playlists owned or followed by the current Spotify user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    Integer limit = 20; // Integer | 
    Integer offset = 0; // Integer | 
    try {
      PagingPlaylistObject result = apiInstance.getAListOfCurrentUsersPlaylists_0(limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#getAListOfCurrentUsersPlaylists_0");
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
| **limit** | **Integer**|  | [optional] [default to 20] |
| **offset** | **Integer**|  | [optional] [default to 0] |

### Return type

[**PagingPlaylistObject**](PagingPlaylistObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paged set of playlists |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="getFollowed_0"></a>
# **getFollowed_0**
> GetFollowed200Response getFollowed_0(type, after, limit)

Get Followed Artists 

Get the current user&#39;s followed artists. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String type = "artist"; // String | 
    String after = "0I2XqVXqHScXjHhk6AYYRe"; // String | 
    Integer limit = 20; // Integer | 
    try {
      GetFollowed200Response result = apiInstance.getFollowed_0(type, after, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#getFollowed_0");
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
| **type** | **String**|  | [enum: artist] |
| **after** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 20] |

### Return type

[**GetFollowed200Response**](GetFollowed200Response.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paged set of artists |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="getUsersSavedAlbums_0"></a>
# **getUsersSavedAlbums_0**
> PagingSavedAlbumObject getUsersSavedAlbums_0(limit, offset, market)

Get User&#39;s Saved Albums 

Get a list of the albums saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    Integer limit = 20; // Integer | 
    Integer offset = 0; // Integer | 
    String market = "ES"; // String | 
    try {
      PagingSavedAlbumObject result = apiInstance.getUsersSavedAlbums_0(limit, offset, market);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#getUsersSavedAlbums_0");
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
| **limit** | **Integer**|  | [optional] [default to 20] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **market** | **String**|  | [optional] |

### Return type

[**PagingSavedAlbumObject**](PagingSavedAlbumObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pages of albums |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="getUsersSavedAudiobooks_0"></a>
# **getUsersSavedAudiobooks_0**
> PagingSimplifiedAudiobookObject getUsersSavedAudiobooks_0(limit, offset)

Get User&#39;s Saved Audiobooks 

Get a list of the audiobooks saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    Integer limit = 20; // Integer | 
    Integer offset = 0; // Integer | 
    try {
      PagingSimplifiedAudiobookObject result = apiInstance.getUsersSavedAudiobooks_0(limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#getUsersSavedAudiobooks_0");
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
| **limit** | **Integer**|  | [optional] [default to 20] |
| **offset** | **Integer**|  | [optional] [default to 0] |

### Return type

[**PagingSimplifiedAudiobookObject**](PagingSimplifiedAudiobookObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pages of audiobooks |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="getUsersSavedEpisodes_0"></a>
# **getUsersSavedEpisodes_0**
> PagingSavedEpisodeObject getUsersSavedEpisodes_0(market, limit, offset)

Get User&#39;s Saved Episodes 

Get a list of the episodes saved in the current Spotify user&#39;s library.&lt;br/&gt; This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String market = "ES"; // String | 
    Integer limit = 20; // Integer | 
    Integer offset = 0; // Integer | 
    try {
      PagingSavedEpisodeObject result = apiInstance.getUsersSavedEpisodes_0(market, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#getUsersSavedEpisodes_0");
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
| **market** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **offset** | **Integer**|  | [optional] [default to 0] |

### Return type

[**PagingSavedEpisodeObject**](PagingSavedEpisodeObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pages of episodes |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="getUsersSavedShows_0"></a>
# **getUsersSavedShows_0**
> PagingSavedShowObject getUsersSavedShows_0(limit, offset)

Get User&#39;s Saved Shows 

Get a list of shows saved in the current Spotify user&#39;s library. Optional parameters can be used to limit the number of shows returned. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    Integer limit = 20; // Integer | 
    Integer offset = 0; // Integer | 
    try {
      PagingSavedShowObject result = apiInstance.getUsersSavedShows_0(limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#getUsersSavedShows_0");
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
| **limit** | **Integer**|  | [optional] [default to 20] |
| **offset** | **Integer**|  | [optional] [default to 0] |

### Return type

[**PagingSavedShowObject**](PagingSavedShowObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pages of shows |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="getUsersSavedTracks_0"></a>
# **getUsersSavedTracks_0**
> PagingSavedTrackObject getUsersSavedTracks_0(market, limit, offset)

Get User&#39;s Saved Tracks 

Get a list of the songs saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String market = "ES"; // String | 
    Integer limit = 20; // Integer | 
    Integer offset = 0; // Integer | 
    try {
      PagingSavedTrackObject result = apiInstance.getUsersSavedTracks_0(market, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#getUsersSavedTracks_0");
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
| **market** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **offset** | **Integer**|  | [optional] [default to 0] |

### Return type

[**PagingSavedTrackObject**](PagingSavedTrackObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pages of tracks |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="getUsersTopArtistsAndTracks_1"></a>
# **getUsersTopArtistsAndTracks_1**
> GetUsersTopArtistsAndTracks200Response getUsersTopArtistsAndTracks_1(type, timeRange, limit, offset)

Get User&#39;s Top Items 

Get the current user&#39;s top artists or tracks based on calculated affinity. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String type = "artists"; // String | 
    String timeRange = "medium_term"; // String | 
    Integer limit = 20; // Integer | 
    Integer offset = 0; // Integer | 
    try {
      GetUsersTopArtistsAndTracks200Response result = apiInstance.getUsersTopArtistsAndTracks_1(type, timeRange, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#getUsersTopArtistsAndTracks_1");
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
| **type** | **String**|  | [enum: artists, tracks] |
| **timeRange** | **String**|  | [optional] [default to medium_term] |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **offset** | **Integer**|  | [optional] [default to 0] |

### Return type

[**GetUsersTopArtistsAndTracks200Response**](GetUsersTopArtistsAndTracks200Response.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pages of artists or tracks |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="removeAlbumsUser_0"></a>
# **removeAlbumsUser_0**
> removeAlbumsUser_0(ids, saveAlbumsUserRequest)

Remove Users&#39; Saved Albums 

Remove one or more albums from the current user&#39;s &#39;Your Music&#39; library. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String ids = "382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc"; // String | 
    SaveAlbumsUserRequest saveAlbumsUserRequest = new SaveAlbumsUserRequest(); // SaveAlbumsUserRequest | 
    try {
      apiInstance.removeAlbumsUser_0(ids, saveAlbumsUserRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#removeAlbumsUser_0");
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
| **ids** | **String**|  | |
| **saveAlbumsUserRequest** | [**SaveAlbumsUserRequest**](SaveAlbumsUserRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Album(s) have been removed from the library |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="removeAudiobooksUser_0"></a>
# **removeAudiobooksUser_0**
> removeAudiobooksUser_0(ids)

Remove User&#39;s Saved Audiobooks 

Remove one or more audiobooks from the Spotify user&#39;s library. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String ids = "18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe"; // String | 
    try {
      apiInstance.removeAudiobooksUser_0(ids);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#removeAudiobooksUser_0");
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
| **ids** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Audiobook(s) have been removed from the library |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="removeEpisodesUser_0"></a>
# **removeEpisodesUser_0**
> removeEpisodesUser_0(ids, removeEpisodesUserRequest)

Remove User&#39;s Saved Episodes 

Remove one or more episodes from the current user&#39;s library.&lt;br/&gt; This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String ids = "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"; // String | 
    RemoveEpisodesUserRequest removeEpisodesUserRequest = new RemoveEpisodesUserRequest(); // RemoveEpisodesUserRequest | 
    try {
      apiInstance.removeEpisodesUser_0(ids, removeEpisodesUserRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#removeEpisodesUser_0");
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
| **ids** | **String**|  | |
| **removeEpisodesUserRequest** | [**RemoveEpisodesUserRequest**](RemoveEpisodesUserRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Episode removed |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="removeShowsUser_0"></a>
# **removeShowsUser_0**
> removeShowsUser_0(ids, market)

Remove User&#39;s Saved Shows 

Delete one or more shows from current Spotify user&#39;s library. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String ids = "5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ"; // String | 
    String market = "ES"; // String | 
    try {
      apiInstance.removeShowsUser_0(ids, market);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#removeShowsUser_0");
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
| **ids** | **String**|  | |
| **market** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Show removed |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="removeTracksUser_0"></a>
# **removeTracksUser_0**
> removeTracksUser_0(ids, saveAlbumsUserRequest)

Remove User&#39;s Saved Tracks 

Remove one or more tracks from the current user&#39;s &#39;Your Music&#39; library. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String ids = "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"; // String | 
    SaveAlbumsUserRequest saveAlbumsUserRequest = new SaveAlbumsUserRequest(); // SaveAlbumsUserRequest | 
    try {
      apiInstance.removeTracksUser_0(ids, saveAlbumsUserRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#removeTracksUser_0");
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
| **ids** | **String**|  | |
| **saveAlbumsUserRequest** | [**SaveAlbumsUserRequest**](SaveAlbumsUserRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Track removed |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="saveAlbumsUser_0"></a>
# **saveAlbumsUser_0**
> saveAlbumsUser_0(ids, saveAlbumsUserRequest)

Save Albums for Current User 

Save one or more albums to the current user&#39;s &#39;Your Music&#39; library. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String ids = "382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc"; // String | 
    SaveAlbumsUserRequest saveAlbumsUserRequest = new SaveAlbumsUserRequest(); // SaveAlbumsUserRequest | 
    try {
      apiInstance.saveAlbumsUser_0(ids, saveAlbumsUserRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#saveAlbumsUser_0");
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
| **ids** | **String**|  | |
| **saveAlbumsUserRequest** | [**SaveAlbumsUserRequest**](SaveAlbumsUserRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The album is saved |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="saveAudiobooksUser_0"></a>
# **saveAudiobooksUser_0**
> saveAudiobooksUser_0(ids)

Save Audiobooks for Current User 

Save one or more audiobooks to the current Spotify user&#39;s library. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String ids = "18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe"; // String | 
    try {
      apiInstance.saveAudiobooksUser_0(ids);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#saveAudiobooksUser_0");
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
| **ids** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Audiobook(s) are saved to the library |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="saveEpisodesUser_0"></a>
# **saveEpisodesUser_0**
> saveEpisodesUser_0(ids, saveEpisodesUserRequest)

Save Episodes for Current User 

Save one or more episodes to the current user&#39;s library.&lt;br/&gt; This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String ids = "77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf"; // String | 
    SaveEpisodesUserRequest saveEpisodesUserRequest = new SaveEpisodesUserRequest(); // SaveEpisodesUserRequest | 
    try {
      apiInstance.saveEpisodesUser_0(ids, saveEpisodesUserRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#saveEpisodesUser_0");
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
| **ids** | **String**|  | |
| **saveEpisodesUserRequest** | [**SaveEpisodesUserRequest**](SaveEpisodesUserRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Episode saved |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="saveShowsUser_0"></a>
# **saveShowsUser_0**
> saveShowsUser_0(ids)

Save Shows for Current User 

Save one or more shows to current Spotify user&#39;s library. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String ids = "5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ"; // String | 
    try {
      apiInstance.saveShowsUser_0(ids);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#saveShowsUser_0");
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
| **ids** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Show saved |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="saveTracksUser_0"></a>
# **saveTracksUser_0**
> saveTracksUser_0(ids, saveTracksUserRequest)

Save Tracks for Current User 

Save one or more tracks to the current user&#39;s &#39;Your Music&#39; library. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String ids = "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"; // String | 
    SaveTracksUserRequest saveTracksUserRequest = new SaveTracksUserRequest(); // SaveTracksUserRequest | 
    try {
      apiInstance.saveTracksUser_0(ids, saveTracksUserRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#saveTracksUser_0");
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
| **ids** | **String**|  | |
| **saveTracksUserRequest** | [**SaveTracksUserRequest**](SaveTracksUserRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Track saved |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

<a id="unfollowArtistsUsers_1"></a>
# **unfollowArtistsUsers_1**
> unfollowArtistsUsers_1(type, ids, unfollowArtistsUsersRequest)

Unfollow Artists or Users 

Remove the current user as a follower of one or more artists or other Spotify users. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibraryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spotify.com/v1");
    
    // Configure OAuth2 access token for authorization: oauth_2_0
    OAuth oauth_2_0 = (OAuth) defaultClient.getAuthentication("oauth_2_0");
    oauth_2_0.setAccessToken("YOUR ACCESS TOKEN");

    LibraryApi apiInstance = new LibraryApi(defaultClient);
    String type = "artist"; // String | 
    String ids = "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"; // String | 
    UnfollowArtistsUsersRequest unfollowArtistsUsersRequest = new UnfollowArtistsUsersRequest(); // UnfollowArtistsUsersRequest | 
    try {
      apiInstance.unfollowArtistsUsers_1(type, ids, unfollowArtistsUsersRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibraryApi#unfollowArtistsUsers_1");
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
| **type** | **String**|  | [enum: artist, user] |
| **ids** | **String**|  | |
| **unfollowArtistsUsersRequest** | [**UnfollowArtistsUsersRequest**](UnfollowArtistsUsersRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Artist or user unfollowed |  -  |
| **401** | Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.  |  -  |
| **403** | Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won&#39;t help here.  |  -  |
| **429** | The app has exceeded its rate limits.  |  -  |

