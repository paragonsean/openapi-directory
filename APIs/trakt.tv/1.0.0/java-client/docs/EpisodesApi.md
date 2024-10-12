# EpisodesApi

All URIs are relative to *https://api.trakt.tv*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getASingleEpisodeForAShow**](EpisodesApi.md#getASingleEpisodeForAShow) | **GET** /shows/{id}/seasons/{season}/episodes/{episode} | Get a single episode for a show |
| [**getAllEpisodeComments**](EpisodesApi.md#getAllEpisodeComments) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/comments/{sort} | Get all episode comments |
| [**getAllEpisodeTranslations**](EpisodesApi.md#getAllEpisodeTranslations) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/translations/{language} | Get all episode translations |
| [**getAllPeopleForAnEpisode**](EpisodesApi.md#getAllPeopleForAnEpisode) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/people | Get all people for an episode |
| [**getEpisodeRatings**](EpisodesApi.md#getEpisodeRatings) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/ratings | Get episode ratings |
| [**getEpisodeStats**](EpisodesApi.md#getEpisodeStats) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/stats | Get episode stats |
| [**getListsContainingThisEpisode**](EpisodesApi.md#getListsContainingThisEpisode) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/lists/{type}/{sort} | Get lists containing this episode |
| [**showsIdSeasonsSeasonEpisodesEpisodeWatchingGet**](EpisodesApi.md#showsIdSeasonsSeasonEpisodesEpisodeWatchingGet) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/watching | Get users watching right now |


<a id="getASingleEpisodeForAShow"></a>
# **getASingleEpisodeForAShow**
> getASingleEpisodeForAShow(id, season, episode, traktApiVersion, traktApiKey)

Get a single episode for a show

#### &amp;#10024; Extended Info  Returns a single episode&#39;s details. All date and times are in UTC and were calculated using the episode&#39;s &#x60;air_date&#x60; and show&#39;s &#x60;country&#x60; and &#x60;air_time&#x60;.  **Note:** If the &#x60;first_aired&#x60; is unknown, it will be set to &#x60;null&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EpisodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    EpisodesApi apiInstance = new EpisodesApi(defaultClient);
    String id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
    Integer season = 1; // Integer | season number
    Integer episode = 1; // Integer | episode number
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getASingleEpisodeForAShow(id, season, episode, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling EpisodesApi#getASingleEpisodeForAShow");
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
| **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | |
| **season** | **Integer**| season number | |
| **episode** | **Integer**| episode number | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | &#x60;&#x60;&#x60; /shows/game-of-thrones/seasons/1/episodes/1?extended&#x3D;full &#x60;&#x60;&#x60; |  -  |

<a id="getAllEpisodeComments"></a>
# **getAllEpisodeComments**
> getAllEpisodeComments(id, season, episode, sort, traktApiVersion, traktApiKey)

Get all episode comments

#### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all top level comments for an episode. By default, the &#x60;newest&#x60; comments are returned first. Other sorting options include &#x60;oldest&#x60;, most &#x60;likes&#x60;, most &#x60;replies&#x60;, &#x60;highest&#x60; rated, &#x60;lowest&#x60; rated, and most &#x60;plays&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EpisodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    EpisodesApi apiInstance = new EpisodesApi(defaultClient);
    String id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
    Integer season = 1; // Integer | season number
    Integer episode = 1; // Integer | episode number
    String sort = "newest"; // String | how to sort
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getAllEpisodeComments(id, season, episode, sort, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling EpisodesApi#getAllEpisodeComments");
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
| **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | |
| **season** | **Integer**| season number | |
| **episode** | **Integer**| episode number | |
| **sort** | **String**| how to sort | [enum: newest, oldest, likes, replies, highest, lowest, plays] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  |

<a id="getAllEpisodeTranslations"></a>
# **getAllEpisodeTranslations**
> getAllEpisodeTranslations(id, season, episode, language, traktApiVersion, traktApiKey)

Get all episode translations

Returns all translations for an episode, including language and translated values for title and overview.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EpisodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    EpisodesApi apiInstance = new EpisodesApi(defaultClient);
    String id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
    Integer season = 1; // Integer | season number
    Integer episode = 1; // Integer | episode number
    String language = "es"; // String | 2 character language code
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getAllEpisodeTranslations(id, season, episode, language, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling EpisodesApi#getAllEpisodeTranslations");
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
| **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | |
| **season** | **Integer**| season number | |
| **episode** | **Integer**| episode number | |
| **language** | **String**| 2 character language code | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getAllPeopleForAnEpisode"></a>
# **getAllPeopleForAnEpisode**
> getAllPeopleForAnEpisode(id, season, episode, traktApiVersion, traktApiKey)

Get all people for an episode

#### &amp;#10024; Extended Info  Returns all &#x60;cast&#x60; and &#x60;crew&#x60; for an episode. Each &#x60;cast&#x60; member will have a &#x60;characters&#x60; array and a standard &#x60;person&#x60; object.  The &#x60;crew&#x60; object will be broken up by department into &#x60;production&#x60;, &#x60;art&#x60;, &#x60;crew&#x60;, &#x60;costume &amp; make-up&#x60;, &#x60;directing&#x60;, &#x60;writing&#x60;, &#x60;sound&#x60;, &#x60;camera&#x60;, &#x60;visual effects&#x60;, &#x60;lighting&#x60;, and &#x60;editing&#x60; (if there are people for those crew positions). Each of those members will have a &#x60;jobs&#x60; array and a standard &#x60;person&#x60; object.  #### Guest Stars  If you add &#x60;?extended&#x3D;guest_stars&#x60; to the URL, it will return all guest stars that appeared in the episode.  **Note:** This returns a lot of data, so please only use this extended parameter if you actually need it!

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EpisodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    EpisodesApi apiInstance = new EpisodesApi(defaultClient);
    String id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
    Integer season = 1; // Integer | season number
    Integer episode = 1; // Integer | episode number
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getAllPeopleForAnEpisode(id, season, episode, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling EpisodesApi#getAllPeopleForAnEpisode");
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
| **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | |
| **season** | **Integer**| season number | |
| **episode** | **Integer**| episode number | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | &#x60;&#x60;&#x60; /shows/game-of-thrones/seasons/1/episodes/1/people?extended&#x3D;guest_stars &#x60;&#x60;&#x60; |  -  |

<a id="getEpisodeRatings"></a>
# **getEpisodeRatings**
> getEpisodeRatings(id, season, episode, traktApiVersion, traktApiKey)

Get episode ratings

Returns rating (between 0 and 10) and distribution for an episode.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EpisodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    EpisodesApi apiInstance = new EpisodesApi(defaultClient);
    String id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
    Integer season = 1; // Integer | season number
    Integer episode = 12; // Integer | episode number
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getEpisodeRatings(id, season, episode, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling EpisodesApi#getEpisodeRatings");
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
| **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | |
| **season** | **Integer**| season number | |
| **episode** | **Integer**| episode number | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getEpisodeStats"></a>
# **getEpisodeStats**
> getEpisodeStats(id, season, episode, traktApiVersion, traktApiKey)

Get episode stats

Returns lots of episode stats.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EpisodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    EpisodesApi apiInstance = new EpisodesApi(defaultClient);
    String id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
    Integer season = 1; // Integer | season number
    Integer episode = 1; // Integer | episode number
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getEpisodeStats(id, season, episode, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling EpisodesApi#getEpisodeStats");
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
| **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | |
| **season** | **Integer**| season number | |
| **episode** | **Integer**| episode number | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getListsContainingThisEpisode"></a>
# **getListsContainingThisEpisode**
> getListsContainingThisEpisode(id, season, episode, type, sort, traktApiVersion, traktApiKey)

Get lists containing this episode

#### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all lists that contain this episode. By default, &#x60;personal&#x60; lists are returned sorted by the most &#x60;popular&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EpisodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    EpisodesApi apiInstance = new EpisodesApi(defaultClient);
    String id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
    Integer season = 1; // Integer | season number
    Integer episode = 1; // Integer | episode number
    String type = "all"; // String | Filter for a specific list type
    String sort = "popular"; // String | How to sort
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getListsContainingThisEpisode(id, season, episode, type, sort, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling EpisodesApi#getListsContainingThisEpisode");
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
| **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | |
| **season** | **Integer**| season number | |
| **episode** | **Integer**| episode number | |
| **type** | **String**| Filter for a specific list type | [enum: all, personal, official, watchlists] |
| **sort** | **String**| How to sort | [enum: popular, likes, comments, items, added, updated] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  |

<a id="showsIdSeasonsSeasonEpisodesEpisodeWatchingGet"></a>
# **showsIdSeasonsSeasonEpisodesEpisodeWatchingGet**
> showsIdSeasonsSeasonEpisodesEpisodeWatchingGet(id, season, episode, traktApiVersion, traktApiKey)

Get users watching right now

#### &amp;#10024; Extended Info  Returns all users watching this episode right now.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EpisodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    EpisodesApi apiInstance = new EpisodesApi(defaultClient);
    String id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
    Integer season = 1; // Integer | season number
    Integer episode = 1; // Integer | episode number
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.showsIdSeasonsSeasonEpisodesEpisodeWatchingGet(id, season, episode, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling EpisodesApi#showsIdSeasonsSeasonEpisodesEpisodeWatchingGet");
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
| **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | |
| **season** | **Integer**| season number | |
| **episode** | **Integer**| episode number | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

