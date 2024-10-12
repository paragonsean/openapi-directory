# SyncApi

All URIs are relative to *https://api.trakt.tv*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addItemsToCollection**](SyncApi.md#addItemsToCollection) | **POST** /sync/collection | Add items to collection |
| [**addItemsToPersonalRecommendations**](SyncApi.md#addItemsToPersonalRecommendations) | **POST** /sync/recommendations | Add items to personal recommendations |
| [**addItemsToWatchedHistory**](SyncApi.md#addItemsToWatchedHistory) | **POST** /sync/history | Add items to watched history |
| [**addItemsToWatchlist**](SyncApi.md#addItemsToWatchlist) | **POST** /sync/watchlist | Add items to watchlist |
| [**addNewRatings**](SyncApi.md#addNewRatings) | **POST** /sync/ratings | Add new ratings |
| [**getCollection**](SyncApi.md#getCollection) | **GET** /sync/collection/{type} | Get collection |
| [**getLastActivity**](SyncApi.md#getLastActivity) | **GET** /sync/last_activities | Get last activity |
| [**getPersonalRecommendations**](SyncApi.md#getPersonalRecommendations) | **GET** /sync/recommendations/{type}/{sort} | Get personal recommendations |
| [**getPlaybackProgress**](SyncApi.md#getPlaybackProgress) | **GET** /sync/playback/{type} | Get playback progress |
| [**getRatings**](SyncApi.md#getRatings) | **GET** /sync/ratings/{type}/{rating} | Get ratings |
| [**getWatched**](SyncApi.md#getWatched) | **GET** /sync/watched/{type} | Get watched |
| [**getWatchedHistory**](SyncApi.md#getWatchedHistory) | **GET** /sync/history/{type}/{id} | Get watched history |
| [**getWatchlist**](SyncApi.md#getWatchlist) | **GET** /sync/watchlist/{type}/{sort} | Get watchlist |
| [**removeAPlaybackItem**](SyncApi.md#removeAPlaybackItem) | **DELETE** /sync/playback/{id} | Remove a playback item |
| [**removeItemsFromCollection**](SyncApi.md#removeItemsFromCollection) | **POST** /sync/collection/remove | Remove items from collection |
| [**removeItemsFromHistory**](SyncApi.md#removeItemsFromHistory) | **POST** /sync/history/remove | Remove items from history |
| [**removeItemsFromPersonalRecommendations**](SyncApi.md#removeItemsFromPersonalRecommendations) | **POST** /sync/recommendations/remove | Remove items from personal recommendations |
| [**removeItemsFromWatchlist**](SyncApi.md#removeItemsFromWatchlist) | **POST** /sync/watchlist/remove | Remove items from watchlist |
| [**removeRatings**](SyncApi.md#removeRatings) | **POST** /sync/ratings/remove | Remove ratings |
| [**reorderPersonallyRecommendedItems**](SyncApi.md#reorderPersonallyRecommendedItems) | **POST** /sync/recommendations/reorder | Reorder personally recommended items |
| [**reorderWatchlistItems**](SyncApi.md#reorderWatchlistItems) | **POST** /sync/watchlist/reorder | Reorder watchlist items |


<a id="addItemsToCollection"></a>
# **addItemsToCollection**
> addItemsToCollection(traktApiVersion, traktApiKey, addItemsToCollectionRequest)

Add items to collection

#### &amp;#128274; OAuth Required  Add items to a user&#39;s collection. Accepts shows, seasons, episodes and movies. If only a show is passed, all episodes for the show will be collected. If seasons are specified, all episodes in those seasons will be collected.  Send a &#x60;collected_at&#x60; UTC datetime to mark items as collected in the past. You can also send additional metadata about the media itself to have a very accurate collection. Showcase what is available to watch from your epic HD DVD collection down to your downloaded iTunes movies.  **Note:** You can resend items already in your collection and they will be updated with any new values. This includes the &#x60;collected_at&#x60; and any other metadata.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;episodes&#x60; | array | Array of &#x60;episode&#x60; objects. |  #### Media Object POST Data  | Key | Type | Value | |---|---|---| | item &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | object | &#x60;movie&#x60;, &#x60;show&#x60;, or &#x60;episode&#x60; object. | | &#x60;collected_at&#x60; | datetime | UTC datetime when the item was collected. Set to &#x60;released&#x60; to automatically use the inital release date + runtime *(episodes only)*). | | &#x60;media_type&#x60; | string | Set to &#x60;digital&#x60;, &#x60;bluray&#x60;, &#x60;hddvd&#x60;, &#x60;dvd&#x60;, &#x60;vcd&#x60;, &#x60;vhs&#x60;, &#x60;betamax&#x60;, or &#x60;laserdisc&#x60;. | | &#x60;resolution&#x60; | string | Set to &#x60;uhd_4k&#x60;, &#x60;hd_1080p&#x60;, &#x60;hd_1080i&#x60;, &#x60;hd_720p&#x60;, &#x60;sd_480p&#x60;, &#x60;sd_480i&#x60;, &#x60;sd_576p&#x60;, or &#x60;sd_576i&#x60;. | | &#x60;hdr&#x60; | string | Set to &#x60;dolby_vision&#x60;, &#x60;hdr10&#x60;, &#x60;hdr10_plus&#x60;, or &#x60;hlg&#x60;. | | &#x60;audio&#x60; | string | Set to &#x60;dolby_digital&#x60;, &#x60;dolby_digital_plus&#x60;, &#x60;dolby_digital_plus_atmos&#x60;, &#x60;dolby_truehd&#x60;, &#x60;dolby_atmos&#x60; *(Dolby TrueHD Atmos)*, &#x60;dolby_prologic&#x60;, &#x60;dts&#x60;, &#x60;dts_ma&#x60;, &#x60;dts_hr&#x60;, &#x60;dts_x&#x60;, &#x60;auro_3d&#x60;, &#x60;mp3&#x60;, &#x60;mp2&#x60;, &#x60;aac&#x60;, &#x60;lpcm&#x60;, &#x60;ogg&#x60; *(Ogg Vorbis)*, &#x60;ogg_opus&#x60;, &#x60;wma&#x60;, or &#x60;flac&#x60;. | | &#x60;audio_channels&#x60; | string | Set to &#x60;1.0&#x60;, &#x60;2.0&#x60;, &#x60;2.1&#x60;, &#x60;3.0&#x60;, &#x60;3.1&#x60;, &#x60;4.0&#x60;, &#x60;4.1&#x60;, &#x60;5.0&#x60;, &#x60;5.1&#x60;, &#x60;5.1.2&#x60;, &#x60;5.1.4&#x60;, &#x60;6.1&#x60;, &#x60;7.1&#x60;, &#x60;7.1.2&#x60;, &#x60;7.1.4&#x60;, &#x60;9.1&#x60;, or &#x60;10.1&#x60; | | &#x60;3d&#x60; | boolean | Set &#x60;true&#x60; if in 3D. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SyncApi apiInstance = new SyncApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    AddItemsToCollectionRequest addItemsToCollectionRequest = new AddItemsToCollectionRequest(); // AddItemsToCollectionRequest | 
    try {
      apiInstance.addItemsToCollection(traktApiVersion, traktApiKey, addItemsToCollectionRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncApi#addItemsToCollection");
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
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **addItemsToCollectionRequest** | [**AddItemsToCollectionRequest**](AddItemsToCollectionRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="addItemsToPersonalRecommendations"></a>
# **addItemsToPersonalRecommendations**
> addItemsToPersonalRecommendations(traktApiVersion, traktApiKey, addItemsToPersonalRecommendationsRequest)

Add items to personal recommendations

#### &amp;#128274; OAuth Required &amp;#128513; Emojis  If the user only had 50 movies and TV shows to bring with them on a desert island, what would they be? These recommendations are used to enchance Trakt&#39;s social recommendation algorithm. Apps should encourage user&#39;s to build their personal recommendations so the algorithm keeps getting better.  #### Notes  Each recommendation can optionally accept a &#x60;notes&#x60; *(255 maximum characters)* field explaining why the user recommended the item.  #### Limits  If the user has recommended 50 items already, a &#x60;420&#x60; HTTP error code is returned. This limit applies to all users.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SyncApi apiInstance = new SyncApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    AddItemsToPersonalRecommendationsRequest addItemsToPersonalRecommendationsRequest = new AddItemsToPersonalRecommendationsRequest(); // AddItemsToPersonalRecommendationsRequest | 
    try {
      apiInstance.addItemsToPersonalRecommendations(traktApiVersion, traktApiKey, addItemsToPersonalRecommendationsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncApi#addItemsToPersonalRecommendations");
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
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **addItemsToPersonalRecommendationsRequest** | [**AddItemsToPersonalRecommendationsRequest**](AddItemsToPersonalRecommendationsRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="addItemsToWatchedHistory"></a>
# **addItemsToWatchedHistory**
> addItemsToWatchedHistory(traktApiVersion, traktApiKey, addItemsToWatchedHistoryRequest)

Add items to watched history

#### &amp;#128274; OAuth Required  Add items to a user&#39;s watch history. Accepts shows, seasons, episodes and movies. If only a show is passed, all episodes for the show will be added. If seasons are specified, only episodes in those seasons will be added.  Send a &#x60;watched_at&#x60; UTC datetime to mark items as watched in the past. This is useful for syncing past watches from a media center.  **Note:** Please be careful with sending duplicate data. We don&#39;t verify the &#x60;item&#x60; + &#x60;watched_at&#x60; to ensure it&#39;s unique, it is up to your app to veify this and not send duplicate plays.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;episodes&#x60; | array | Array of &#x60;episode&#x60; objects. |  #### Media Object POST Data  | Key | Type | Value | |---|---|---| | item &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | object | &#x60;movie&#x60;, &#x60;show&#x60;, or &#x60;episode&#x60; object. | | &#x60;watched_at&#x60; | datetime | UTC datetime when the item was watched. Set to &#x60;released&#x60; to automatically use the initial release date + runtime *(episodes only)*. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SyncApi apiInstance = new SyncApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    AddItemsToWatchedHistoryRequest addItemsToWatchedHistoryRequest = new AddItemsToWatchedHistoryRequest(); // AddItemsToWatchedHistoryRequest | 
    try {
      apiInstance.addItemsToWatchedHistory(traktApiVersion, traktApiKey, addItemsToWatchedHistoryRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncApi#addItemsToWatchedHistory");
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
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **addItemsToWatchedHistoryRequest** | [**AddItemsToWatchedHistoryRequest**](AddItemsToWatchedHistoryRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="addItemsToWatchlist"></a>
# **addItemsToWatchlist**
> addItemsToWatchlist(traktApiVersion, traktApiKey, addItemsToWatchlistRequest)

Add items to watchlist

#### &amp;#128274; OAuth Required &amp;#128513; Emojis 🔥 VIP Enhanced  Add one of more items to a user&#39;s watchlist. Accepts shows, seasons, episodes and movies. If only a show is passed, only the show itself will be added. If seasons are specified, all of those seasons will be added.  #### Notes  Each watchlist item can optionally accept a &#x60;notes&#x60; *(255 maximum characters)* field with custom text. The user must be a [**Trakt VIP**](https://trakt.tv/vip) to send &#x60;notes&#x60;.  #### Limits  If the user&#39;s watchlist limit is exceeded, a &#x60;420&#x60; HTTP error code is returned. Use the [**_/users/settings**](/reference/users/settings) method to get all limits for a user account. In most cases, upgrading to [**Trakt VIP**](https://trakt.tv/vip) will increase the limits.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;episodes&#x60; | array | Array of &#x60;episode&#x60; objects. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SyncApi apiInstance = new SyncApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    AddItemsToWatchlistRequest addItemsToWatchlistRequest = new AddItemsToWatchlistRequest(); // AddItemsToWatchlistRequest | 
    try {
      apiInstance.addItemsToWatchlist(traktApiVersion, traktApiKey, addItemsToWatchlistRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncApi#addItemsToWatchlist");
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
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **addItemsToWatchlistRequest** | [**AddItemsToWatchlistRequest**](AddItemsToWatchlistRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **420** |  |  * X-Account-Limit -  <br>  * X-Upgrade-URL -  <br>  * X-VIP-User -  <br>  |

<a id="addNewRatings"></a>
# **addNewRatings**
> addNewRatings(traktApiVersion, traktApiKey, addNewRatingsRequest)

Add new ratings

#### &amp;#128274; OAuth Required  Rate one or more items. Accepts shows, seasons, episodes and movies. If only a show is passed, only the show itself will be rated. If seasons are specified, all of those seasons will be rated.  Send a &#x60;rated_at&#x60; UTC datetime to mark items as rated in the past. This is useful for syncing ratings from a media center.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;episodes&#x60; | array | Array of &#x60;episode&#x60; objects. |  #### Media Object POST Data  | Key | Type | Value | |---|---|---| | item &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | object | &#x60;movie&#x60;, &#x60;show&#x60;, &#x60;season&#x60;, or &#x60;episode&#x60; object. | | &#x60;rating&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | integer | Between 1 and 10. | | &#x60;rated_at&#x60; | datetime | UTC datetime when the item was rated. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SyncApi apiInstance = new SyncApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    AddNewRatingsRequest addNewRatingsRequest = new AddNewRatingsRequest(); // AddNewRatingsRequest | 
    try {
      apiInstance.addNewRatings(traktApiVersion, traktApiKey, addNewRatingsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncApi#addNewRatings");
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
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **addNewRatingsRequest** | [**AddNewRatingsRequest**](AddNewRatingsRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="getCollection"></a>
# **getCollection**
> getCollection(type, traktApiVersion, traktApiKey)

Get collection

#### &amp;#128274; OAuth Required &amp;#10024; Extended Info  Get all collected items in a user&#39;s collection. A collected item indicates availability to watch digitally or on physical media.  Each &#x60;movie&#x60; object contains &#x60;collected_at&#x60; and &#x60;updated_at&#x60; timestamps. Since users can set custom dates when they collected movies, it is possible for &#x60;collected_at&#x60; to be in the past. We also include &#x60;updated_at&#x60; to help sync Trakt data with your app. Cache this timestamp locally and only re-process the movie if you see a newer timestamp.  Each &#x60;show&#x60; object contains &#x60;last_collected_at&#x60; and &#x60;last_updated_at&#x60; timestamps. Since users can set custom dates when they collected episodes, it is possible for &#x60;last_collected_at&#x60; to be in the past. We also include &#x60;last_updated_at&#x60; to help sync Trakt data with your app. Cache this timestamp locally and only re-process the show if you see a newer timestamp.  If you add &#x60;?extended&#x3D;metadata&#x60; to the URL, it will return the additional &#x60;media_type&#x60;, &#x60;resolution&#x60;, &#x60;hdr&#x60;, &#x60;audio&#x60;, &#x60;audio_channels&#x60; and &#39;3d&#39; metadata. It will use &#x60;null&#x60; if the metadata isn&#39;t set for an item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SyncApi apiInstance = new SyncApi(defaultClient);
    String type = "movies"; // String | 
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getCollection(type, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncApi#getCollection");
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
| **type** | **String**|  | [enum: movies, shows] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | &#x60;&#x60;&#x60; /sync/collection/shows?extended&#x3D;metadata &#x60;&#x60;&#x60; |  -  |

<a id="getLastActivity"></a>
# **getLastActivity**
> getLastActivity(traktApiVersion, traktApiKey)

Get last activity

#### &amp;#128274; OAuth Required  This method is a useful first step in the syncing process. We recommended caching these dates locally, then you can compare to know exactly what data has changed recently. This can greatly optimize your syncs so you don&#39;t pull down a ton of data only to see nothing has actually changed.  #### Account  &#x60;settings_at&#x60; is set when the OAuth user updates any of their Trakt settings on the website. &#x60;followed_at&#x60; is set when another Trakt user follows or unfollows the OAuth user. &#x60;following_at&#x60; is set when the OAuth user follows or unfollows another Trakt user. &#x60;pending_at&#x60; is set when the OAuth user follows a private account, which requires their approval. &#x60;requested_at&#x60; is set when the OAuth user has a private account and someone requests to follow them.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SyncApi apiInstance = new SyncApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getLastActivity(traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncApi#getLastActivity");
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
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getPersonalRecommendations"></a>
# **getPersonalRecommendations**
> getPersonalRecommendations(type, sort, traktApiVersion, traktApiKey)

Get personal recommendations

#### &amp;#128274; OAuth Required &amp;#128196; Pagination Optional &amp;#10024; Extended Info &amp;#128513; Emojis  If the user only had 50 movies and TV shows to bring with them on a desert island, what would they be? These recommendations are used to enchance Trakt&#39;s social recommendation algorithm. Apps should encourage user&#39;s to build their personal recommendations so the algorithm keeps getting better.  #### Notes  Each recommendation contains a &#x60;notes&#x60; field explaining why the user recommended the item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SyncApi apiInstance = new SyncApi(defaultClient);
    String type = "movies"; // String | Filter for a specific item type
    String sort = "rank"; // String | How to sort (only if type is also sent)
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getPersonalRecommendations(type, sort, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncApi#getPersonalRecommendations");
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
| **type** | **String**| Filter for a specific item type | [enum: movies, shows] |
| **sort** | **String**| How to sort (only if type is also sent) | [enum: rank, added, released, title] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | &#x60;&#x60;&#x60; /sync/recommendations/shows &#x60;&#x60;&#x60; |  * X-Sort-By -  <br>  * X-Sort-How -  <br>  |

<a id="getPlaybackProgress"></a>
# **getPlaybackProgress**
> getPlaybackProgress(type, startAt, endAt, traktApiVersion, traktApiKey)

Get playback progress

#### &amp;#128274; OAuth Required &amp;#128196; Pagination Optional  Whenever a scrobble is paused, the playback progress is saved. Use this progress to sync up playback across different media centers or apps. For example, you can start watching a movie in a media center, stop it, then resume on your tablet from the same spot. Each item will have the &#x60;progress&#x60; percentage between 0 and 100.  You can optionally specify a &#x60;type&#x60; to only get &#x60;movies&#x60; or &#x60;episodes&#x60;.  By default, all results will be returned. Pagination is optional and can be used for something like an \&quot;on deck\&quot; feature, or if you only need a limited data set.  **Note:** We only save playback progress for the last 6 months.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SyncApi apiInstance = new SyncApi(defaultClient);
    String type = "movies"; // String | 
    String startAt = "2016-06-01T00:00:00.000Z"; // String | Starting date.
    String endAt = "2016-07-01T23:59:59.000Z"; // String | Ending date.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getPlaybackProgress(type, startAt, endAt, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncApi#getPlaybackProgress");
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
| **type** | **String**|  | [enum: movies, episodes] |
| **startAt** | **String**| Starting date. | [optional] |
| **endAt** | **String**| Ending date. | [optional] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getRatings"></a>
# **getRatings**
> getRatings(type, rating, traktApiVersion, traktApiKey)

Get ratings

#### &amp;#128274; OAuth Required &amp;#128196; Pagination Optional &amp;#10024; Extended Info  Get a user&#39;s ratings filtered by &#x60;type&#x60;. You can optionally filter for a specific &#x60;rating&#x60; between 1 and 10. Send a comma separated string for &#x60;rating&#x60; if you need multiple ratings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SyncApi apiInstance = new SyncApi(defaultClient);
    String type = "movies"; // String | 
    Integer rating = 1; // Integer | Filter for a specific rating.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getRatings(type, rating, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncApi#getRatings");
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
| **type** | **String**|  | [enum: movies, shows, seasons, episodes, all] |
| **rating** | **Integer**| Filter for a specific rating. | [enum: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | &#x60;&#x60;&#x60; /sync/ratings/episodes &#x60;&#x60;&#x60; |  -  |

<a id="getWatched"></a>
# **getWatched**
> getWatched(type, traktApiVersion, traktApiKey)

Get watched

#### &amp;#128274; OAuth Required &amp;#10024; Extended Info  Returns all movies or shows a user has watched sorted by most plays.  If &#x60;type&#x60; is set to _shows_ and you add &#x60;?extended&#x3D;noseasons&#x60; to the URL, it won&#39;t return season or episode info.  Each &#x60;movie&#x60; and &#x60;show&#x60; object contains &#x60;last_watched_at&#x60; and &#x60;last_updated_at&#x60; timestamps. Since users can set custom dates when they watched movies and episodes, it is possible for &#x60;last_watched_at&#x60; to be in the past. We also include &#x60;last_updated_at&#x60; to help sync Trakt data with your app. Cache this timestamp locally and only re-process the movies and shows if you see a newer timestamp.  Each &#x60;show&#x60; object contains a &#x60;reset_at&#x60; timestamp. If not &#x60;null&#x60;, this is when the user started re-watching the show. Your app can adjust the progress by ignoring episodes with a &#x60;last_watched_at&#x60; prior to the &#x60;reset_at&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SyncApi apiInstance = new SyncApi(defaultClient);
    String type = "movies"; // String | 
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getWatched(type, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncApi#getWatched");
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
| **type** | **String**|  | [enum: movies, shows] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | &#x60;&#x60;&#x60; /sync/watched/shows?extended&#x3D;noseasons &#x60;&#x60;&#x60; |  -  |

<a id="getWatchedHistory"></a>
# **getWatchedHistory**
> getWatchedHistory(type, id, startAt, endAt, traktApiVersion, traktApiKey)

Get watched history

#### &amp;#128274; OAuth Required &amp;#128196; Pagination &amp;#10024; Extended Info  Returns movies and episodes that a user has watched, sorted by most recent. You can optionally limit the &#x60;type&#x60; to &#x60;movies&#x60; or &#x60;episodes&#x60;. The &#x60;id&#x60; _(64-bit integer)_ in each history item uniquely identifies the event and can be used to remove individual events by using the [**_/sync/history/remove**](#reference/sync/remove-from-history/get-watched-history) method. The &#x60;action&#x60; will be set to &#x60;scrobble&#x60;, &#x60;checkin&#x60;, or &#x60;watch&#x60;.  Specify a &#x60;type&#x60; and trakt &#x60;id&#x60; to limit the history for just that item. If the &#x60;id&#x60; is valid, but there is no history, an empty array will be returned.  | Example URL | Returns watches for... | |---|---| | &#x60;/history/movies/12601&#x60; | TRON: Legacy | | &#x60;/history/shows/1388&#x60; | All episodes of Breaking Bad | | &#x60;/history/seasons/3950&#x60; | All episodes of Breaking Bad: Season 1 | | &#x60;/history/episodes/73482&#x60; | Only episode 1 for Breaking Bad: Season 1 |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SyncApi apiInstance = new SyncApi(defaultClient);
    String type = "movies"; // String | 
    Integer id = 123; // Integer | Trakt ID for a specific item.
    String startAt = "2016-06-01T00:00:00.000Z"; // String | Starting date.
    String endAt = "2016-07-01T23:59:59.000Z"; // String | Ending date.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getWatchedHistory(type, id, startAt, endAt, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncApi#getWatchedHistory");
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
| **type** | **String**|  | [enum: movies, shows, seasons, episodes] |
| **id** | **Integer**| Trakt ID for a specific item. | |
| **startAt** | **String**| Starting date. | [optional] |
| **endAt** | **String**| Ending date. | [optional] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | &#x60;&#x60;&#x60; /sync/history/episodes &#x60;&#x60;&#x60; |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  |

<a id="getWatchlist"></a>
# **getWatchlist**
> getWatchlist(type, sort, traktApiVersion, traktApiKey)

Get watchlist

#### &amp;#128274; OAuth Required &amp;#128196; Pagination Optional &amp;#10024; Extended Info &amp;#128513; Emojis  Returns all items in a user&#39;s watchlist filtered by type.  #### Notes  Each watchlist item contains a &#x60;notes&#x60; field with text entered by the user.  #### Sorting Headers  By default, all list items are sorted by &#x60;rank&#x60; &#x60;asc&#x60;. We send &#x60;X-Applied-Sort-By&#x60; and &#x60;X-Applied-Sort-How&#x60; headers to indicate how the results are actually being sorted.  We also send &#x60;X-Sort-By&#x60; and &#x60;X-Sort-How&#x60; headers which indicate the user&#39;s sort preference. Use these to to custom sort the watchlist _**in your app**_ for more advanced sort abilities we can&#39;t do in the API. Values for &#x60;X-Sort-By&#x60; include &#x60;rank&#x60;, &#x60;added&#x60;, &#x60;title&#x60;, &#x60;released&#x60;, &#x60;runtime&#x60;, &#x60;popularity&#x60;, &#x60;percentage&#x60;, and &#x60;votes&#x60;. Values for &#x60;X-Sort-How&#x60; include &#x60;asc&#x60; and &#x60;desc&#x60;.  #### Auto Removal  When an item is watched, it will be automatically removed from the watchlist. For shows and seasons, watching 1 episode will remove the entire show or season.  _**The watchlist should not be used as a list of what the user is actively watching.**_  Use a combination of the [**_/sync/watched**](/reference/sync/get-watched) and [**_/shows/:id/progress**](/reference/shows/watched-progress) methods to get what the user is actively watching.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SyncApi apiInstance = new SyncApi(defaultClient);
    String type = "movies"; // String | Filter for a specific item type
    String sort = "rank"; // String | How to sort (only if type is also sent)
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getWatchlist(type, sort, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncApi#getWatchlist");
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
| **type** | **String**| Filter for a specific item type | [enum: movies, shows, seasons, episodes] |
| **sort** | **String**| How to sort (only if type is also sent) | [enum: rank, added, released, title] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | &#x60;&#x60;&#x60; /sync/watchlist/episodes &#x60;&#x60;&#x60; |  * X-Sort-By -  <br>  * X-Sort-How -  <br>  |

<a id="removeAPlaybackItem"></a>
# **removeAPlaybackItem**
> removeAPlaybackItem(id, traktApiVersion, traktApiKey)

Remove a playback item

#### &amp;#128274; OAuth Required  Remove a playback item from a user&#39;s playback progress list. A &#x60;404&#x60; will be returned if the &#x60;id&#x60; is invalid.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SyncApi apiInstance = new SyncApi(defaultClient);
    Integer id = 13; // Integer | playback ID
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.removeAPlaybackItem(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncApi#removeAPlaybackItem");
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
| **id** | **Integer**| playback ID | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="removeItemsFromCollection"></a>
# **removeItemsFromCollection**
> removeItemsFromCollection(traktApiVersion, traktApiKey, removeItemsFromCollectionRequest)

Remove items from collection

#### &amp;#128274; OAuth Required  Remove one or more items from a user&#39;s collection.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;episodes&#x60; | array | Array of &#x60;episode&#x60; objects. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SyncApi apiInstance = new SyncApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    RemoveItemsFromCollectionRequest removeItemsFromCollectionRequest = new RemoveItemsFromCollectionRequest(); // RemoveItemsFromCollectionRequest | 
    try {
      apiInstance.removeItemsFromCollection(traktApiVersion, traktApiKey, removeItemsFromCollectionRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncApi#removeItemsFromCollection");
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
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **removeItemsFromCollectionRequest** | [**RemoveItemsFromCollectionRequest**](RemoveItemsFromCollectionRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="removeItemsFromHistory"></a>
# **removeItemsFromHistory**
> removeItemsFromHistory(traktApiVersion, traktApiKey, removeItemsFromHistoryRequest)

Remove items from history

#### &amp;#128274; OAuth Required  Remove items from a user&#39;s watch history including all watches, scrobbles, and checkins. Accepts shows, seasons, episodes and movies. If only a show is passed, all episodes for the show will be removed. If seasons are specified, only episodes in those seasons will be removed.  You can also send a list of raw history &#x60;ids&#x60; _(64-bit integers)_ to delete single plays from the watched history. The [**_/sync/history**](#reference/sync/get-history) method will return an individual &#x60;id&#x60; _(64-bit integer)_ for each history item.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;episodes&#x60; | array | Array of &#x60;episode&#x60; objects. | | &#x60;ids&#x60; | array | Array of history ids. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SyncApi apiInstance = new SyncApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    RemoveItemsFromHistoryRequest removeItemsFromHistoryRequest = new RemoveItemsFromHistoryRequest(); // RemoveItemsFromHistoryRequest | 
    try {
      apiInstance.removeItemsFromHistory(traktApiVersion, traktApiKey, removeItemsFromHistoryRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncApi#removeItemsFromHistory");
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
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **removeItemsFromHistoryRequest** | [**RemoveItemsFromHistoryRequest**](RemoveItemsFromHistoryRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="removeItemsFromPersonalRecommendations"></a>
# **removeItemsFromPersonalRecommendations**
> removeItemsFromPersonalRecommendations(traktApiVersion, traktApiKey, removeItemsFromPersonalRecommendationsRequest)

Remove items from personal recommendations

#### &amp;#128274; OAuth Required  Remove items from a user&#39;s personal recommendations. These recommendations are used to enchance Trakt&#39;s social recommendation algorithm. Apps should encourage user&#39;s to build their personal recommendations so the algorithm keeps getting better.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SyncApi apiInstance = new SyncApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    RemoveItemsFromPersonalRecommendationsRequest removeItemsFromPersonalRecommendationsRequest = new RemoveItemsFromPersonalRecommendationsRequest(); // RemoveItemsFromPersonalRecommendationsRequest | 
    try {
      apiInstance.removeItemsFromPersonalRecommendations(traktApiVersion, traktApiKey, removeItemsFromPersonalRecommendationsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncApi#removeItemsFromPersonalRecommendations");
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
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **removeItemsFromPersonalRecommendationsRequest** | [**RemoveItemsFromPersonalRecommendationsRequest**](RemoveItemsFromPersonalRecommendationsRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="removeItemsFromWatchlist"></a>
# **removeItemsFromWatchlist**
> removeItemsFromWatchlist(traktApiVersion, traktApiKey, removeItemsFromCollectionRequest)

Remove items from watchlist

#### &amp;#128274; OAuth Required  Remove one or more items from a user&#39;s watchlist.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;episodes&#x60; | array | Array of &#x60;episode&#x60; objects. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SyncApi apiInstance = new SyncApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    RemoveItemsFromCollectionRequest removeItemsFromCollectionRequest = new RemoveItemsFromCollectionRequest(); // RemoveItemsFromCollectionRequest | 
    try {
      apiInstance.removeItemsFromWatchlist(traktApiVersion, traktApiKey, removeItemsFromCollectionRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncApi#removeItemsFromWatchlist");
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
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **removeItemsFromCollectionRequest** | [**RemoveItemsFromCollectionRequest**](RemoveItemsFromCollectionRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="removeRatings"></a>
# **removeRatings**
> removeRatings(traktApiVersion, traktApiKey, removeItemsFromCollectionRequest)

Remove ratings

#### &amp;#128274; OAuth Required  Remove ratings for one or more items.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;episodes&#x60; | array | Array of &#x60;episode&#x60; objects. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SyncApi apiInstance = new SyncApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    RemoveItemsFromCollectionRequest removeItemsFromCollectionRequest = new RemoveItemsFromCollectionRequest(); // RemoveItemsFromCollectionRequest | 
    try {
      apiInstance.removeRatings(traktApiVersion, traktApiKey, removeItemsFromCollectionRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncApi#removeRatings");
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
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **removeItemsFromCollectionRequest** | [**RemoveItemsFromCollectionRequest**](RemoveItemsFromCollectionRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="reorderPersonallyRecommendedItems"></a>
# **reorderPersonallyRecommendedItems**
> reorderPersonallyRecommendedItems(traktApiVersion, traktApiKey, reorderPersonallyRecommendedItemsRequest)

Reorder personally recommended items

#### &amp;#128274; OAuth Required  Reorder all items on a user&#39;s personal recommendations by sending the updated &#x60;rank&#x60; of list item ids. Use the [**_/sync/recommendations**](#reference/sync/get-personal-recommendations) method to get all list item ids.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SyncApi apiInstance = new SyncApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    ReorderPersonallyRecommendedItemsRequest reorderPersonallyRecommendedItemsRequest = new ReorderPersonallyRecommendedItemsRequest(); // ReorderPersonallyRecommendedItemsRequest | 
    try {
      apiInstance.reorderPersonallyRecommendedItems(traktApiVersion, traktApiKey, reorderPersonallyRecommendedItemsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncApi#reorderPersonallyRecommendedItems");
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
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **reorderPersonallyRecommendedItemsRequest** | [**ReorderPersonallyRecommendedItemsRequest**](ReorderPersonallyRecommendedItemsRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="reorderWatchlistItems"></a>
# **reorderWatchlistItems**
> reorderWatchlistItems(traktApiVersion, traktApiKey, reorderPersonallyRecommendedItemsRequest)

Reorder watchlist items

#### &amp;#128274; OAuth Required  Reorder all items on a user&#39;s watchlist by sending the updated &#x60;rank&#x60; of list item ids. Use the [**_/sync/watchlist**](#reference/sync/get-watchlist) method to get all list item ids.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SyncApi apiInstance = new SyncApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    ReorderPersonallyRecommendedItemsRequest reorderPersonallyRecommendedItemsRequest = new ReorderPersonallyRecommendedItemsRequest(); // ReorderPersonallyRecommendedItemsRequest | 
    try {
      apiInstance.reorderWatchlistItems(traktApiVersion, traktApiKey, reorderPersonallyRecommendedItemsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncApi#reorderWatchlistItems");
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
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **reorderPersonallyRecommendedItemsRequest** | [**ReorderPersonallyRecommendedItemsRequest**](ReorderPersonallyRecommendedItemsRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

