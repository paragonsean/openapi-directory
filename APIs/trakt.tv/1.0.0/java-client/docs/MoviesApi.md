# MoviesApi

All URIs are relative to *https://api.trakt.tv*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAMovie**](MoviesApi.md#getAMovie) | **GET** /movies/{id} | Get a movie |
| [**getAllMovieAliases**](MoviesApi.md#getAllMovieAliases) | **GET** /movies/{id}/aliases | Get all movie aliases |
| [**getAllMovieComments**](MoviesApi.md#getAllMovieComments) | **GET** /movies/{id}/comments/{sort} | Get all movie comments |
| [**getAllMovieReleases**](MoviesApi.md#getAllMovieReleases) | **GET** /movies/{id}/releases/{country} | Get all movie releases |
| [**getAllMovieTranslations**](MoviesApi.md#getAllMovieTranslations) | **GET** /movies/{id}/translations/{language} | Get all movie translations |
| [**getAllPeopleForAMovie**](MoviesApi.md#getAllPeopleForAMovie) | **GET** /movies/{id}/people | Get all people for a movie |
| [**getListsContainingThisMovie**](MoviesApi.md#getListsContainingThisMovie) | **GET** /movies/{id}/lists/{type}/{sort} | Get lists containing this movie |
| [**getMovieRatings**](MoviesApi.md#getMovieRatings) | **GET** /movies/{id}/ratings | Get movie ratings |
| [**getMovieStats**](MoviesApi.md#getMovieStats) | **GET** /movies/{id}/stats | Get movie stats |
| [**getMovieStudios**](MoviesApi.md#getMovieStudios) | **GET** /movies/{id}/studios | Get movie studios |
| [**getPopularMovies**](MoviesApi.md#getPopularMovies) | **GET** /movies/popular | Get popular movies |
| [**getRecentlyUpdatedMovieTraktIDs**](MoviesApi.md#getRecentlyUpdatedMovieTraktIDs) | **GET** /movies/updates/id/{start_date} | Get recently updated movie Trakt IDs |
| [**getRecentlyUpdatedMovies**](MoviesApi.md#getRecentlyUpdatedMovies) | **GET** /movies/updates/{start_date} | Get recently updated movies |
| [**getRelatedMovies**](MoviesApi.md#getRelatedMovies) | **GET** /movies/{id}/related | Get related movies |
| [**getTheMostAnticipatedMovies**](MoviesApi.md#getTheMostAnticipatedMovies) | **GET** /movies/anticipated | Get the most anticipated movies |
| [**getTheMostCollectedMovies**](MoviesApi.md#getTheMostCollectedMovies) | **GET** /movies/collected/{period} | Get the most Collected movies |
| [**getTheMostPlayedMovies**](MoviesApi.md#getTheMostPlayedMovies) | **GET** /movies/played/{period} | Get the most played movies |
| [**getTheMostRecommendedMovies**](MoviesApi.md#getTheMostRecommendedMovies) | **GET** /movies/recommended/{period} | Get the most recommended movies |
| [**getTheMostWatchedMovies**](MoviesApi.md#getTheMostWatchedMovies) | **GET** /movies/watched/{period} | Get the most watched movies |
| [**getTheWeekendBoxOffice**](MoviesApi.md#getTheWeekendBoxOffice) | **GET** /movies/boxoffice | Get the weekend box office |
| [**getTrendingMovies**](MoviesApi.md#getTrendingMovies) | **GET** /movies/trending | Get trending movies |
| [**getUsersWatchingRightNow**](MoviesApi.md#getUsersWatchingRightNow) | **GET** /movies/{id}/watching | Get users watching right now |


<a id="getAMovie"></a>
# **getAMovie**
> getAMovie(id, traktApiVersion, traktApiKey)

Get a movie

#### &amp;#10024; Extended Info  Returns a single movie&#39;s details.  **Note:** When getting &#x60;full&#x60; extended info, the &#x60;status&#x60; field can have a value of &#x60;released&#x60;, &#x60;in production&#x60;, &#x60;post production&#x60;, &#x60;planned&#x60;, &#x60;rumored&#x60;, or &#x60;canceled&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getAMovie(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#getAMovie");
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
| **200** | &#x60;&#x60;&#x60; /movies/tron-legacy-2010?extended&#x3D;full &#x60;&#x60;&#x60; |  -  |

<a id="getAllMovieAliases"></a>
# **getAllMovieAliases**
> getAllMovieAliases(id, traktApiVersion, traktApiKey)

Get all movie aliases

Returns all title aliases for a movie.  Includes country where name is different.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getAllMovieAliases(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#getAllMovieAliases");
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

<a id="getAllMovieComments"></a>
# **getAllMovieComments**
> getAllMovieComments(id, sort, traktApiVersion, traktApiKey)

Get all movie comments

#### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all top level comments for a movie. By default, the &#x60;newest&#x60; comments are returned first. Other sorting options include &#x60;oldest&#x60;, most &#x60;likes&#x60;, most &#x60;replies&#x60;, &#x60;highest&#x60; rated, &#x60;lowest&#x60; rated, and most &#x60;plays&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
    String sort = "newest"; // String | how to sort
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getAllMovieComments(id, sort, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#getAllMovieComments");
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

<a id="getAllMovieReleases"></a>
# **getAllMovieReleases**
> getAllMovieReleases(id, country, traktApiVersion, traktApiKey)

Get all movie releases

Returns all releases for a movie including country, certification, release date, release type, and note. The release type can be set to &#x60;unknown&#x60;, &#x60;premiere&#x60;, &#x60;limited&#x60;, &#x60;theatrical&#x60;, &#x60;digital&#x60;, &#x60;physical&#x60;, or &#x60;tv&#x60;. The &#x60;note&#x60; might have optional info such as the film festival name for a &#x60;premiere&#x60; release or Blu-ray specs for a &#x60;physical&#x60; release. We pull this info from [TMDB](https://developers.themoviedb.org/3/movies/get-movie-release-dates).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
    String country = "us"; // String | 2 character country code
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getAllMovieReleases(id, country, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#getAllMovieReleases");
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
| **country** | **String**| 2 character country code | |
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

<a id="getAllMovieTranslations"></a>
# **getAllMovieTranslations**
> getAllMovieTranslations(id, language, traktApiVersion, traktApiKey)

Get all movie translations

Returns all translations for a movie, including language and translated values for title, tagline and overview.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
    String language = "es"; // String | 2 character language code
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getAllMovieTranslations(id, language, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#getAllMovieTranslations");
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

<a id="getAllPeopleForAMovie"></a>
# **getAllPeopleForAMovie**
> getAllPeopleForAMovie(id, traktApiVersion, traktApiKey)

Get all people for a movie

#### &amp;#10024; Extended Info  Returns all &#x60;cast&#x60; and &#x60;crew&#x60; for a movie. Each &#x60;cast&#x60; member will have a &#x60;characters&#x60; array and a standard &#x60;person&#x60; object.  The &#x60;crew&#x60; object will be broken up by department into &#x60;production&#x60;, &#x60;art&#x60;, &#x60;crew&#x60;, &#x60;costume &amp; make-up&#x60;, &#x60;directing&#x60;, &#x60;writing&#x60;, &#x60;sound&#x60;, &#x60;camera&#x60;, &#x60;visual effects&#x60;, &#x60;lighting&#x60;, and &#x60;editing&#x60; (if there are people for those crew positions). Each of those members will have a &#x60;jobs&#x60; array and a standard &#x60;person&#x60; object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getAllPeopleForAMovie(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#getAllPeopleForAMovie");
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

<a id="getListsContainingThisMovie"></a>
# **getListsContainingThisMovie**
> getListsContainingThisMovie(id, type, sort, traktApiVersion, traktApiKey)

Get lists containing this movie

#### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all lists that contain this movie. By default, &#x60;personal&#x60; lists are returned sorted by the most &#x60;popular&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
    String type = "all"; // String | Filter for a specific list type
    String sort = "popular"; // String | How to sort
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getListsContainingThisMovie(id, type, sort, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#getListsContainingThisMovie");
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
| **type** | **String**| Filter for a specific list type | [enum: all, personal, official, watchlists, recommendations] |
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

<a id="getMovieRatings"></a>
# **getMovieRatings**
> getMovieRatings(id, traktApiVersion, traktApiKey)

Get movie ratings

Returns rating (between 0 and 10) and distribution for a movie.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getMovieRatings(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#getMovieRatings");
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

<a id="getMovieStats"></a>
# **getMovieStats**
> getMovieStats(id, traktApiVersion, traktApiKey)

Get movie stats

Returns lots of movie stats.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getMovieStats(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#getMovieStats");
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

<a id="getMovieStudios"></a>
# **getMovieStudios**
> getMovieStudios(id, traktApiVersion, traktApiKey)

Get movie studios

Returns all studios for a movie.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getMovieStudios(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#getMovieStudios");
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

<a id="getPopularMovies"></a>
# **getPopularMovies**
> getPopularMovies(traktApiVersion, traktApiKey)

Get popular movies

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most popular movies. Popularity is calculated using the rating percentage and the number of ratings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getPopularMovies(traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#getPopularMovies");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  |

<a id="getRecentlyUpdatedMovieTraktIDs"></a>
# **getRecentlyUpdatedMovieTraktIDs**
> getRecentlyUpdatedMovieTraktIDs(startDate, traktApiVersion, traktApiKey)

Get recently updated movie Trakt IDs

#### &amp;#128196; Pagination  Returns all movie Trakt IDs updated since the specified UTC date and time. We recommended storing the &#x60;X-Start-Date&#x60; header you can be efficient using this method moving forward. By default, &#x60;10&#x60; results are returned. You can send a &#x60;limit&#x60; to get up to &#x60;100&#x60; results per page.  **Important!** The &#x60;start_date&#x60; is only accurate to the hour, for caching purposes. Please drop the minutes and seconds from your timestamp to help optimize our cached data. For example, use &#x60;2021-07-17T12:00:00Z&#x60; and not &#x60;2021-07-17T12:23:34Z&#x60;.  **Note:** The &#x60;start_date&#x60; can only be a maximum of 30 days in the past.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String startDate = "2020-11-27T00:00:00Z"; // String | Updated since this date and time.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getRecentlyUpdatedMovieTraktIDs(startDate, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#getRecentlyUpdatedMovieTraktIDs");
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
| **startDate** | **String**| Updated since this date and time. | |
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
| **200** | OK |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  * X-Start-Date -  <br>  |

<a id="getRecentlyUpdatedMovies"></a>
# **getRecentlyUpdatedMovies**
> getRecentlyUpdatedMovies(startDate, traktApiVersion, traktApiKey)

Get recently updated movies

#### &amp;#128196; Pagination &amp;#10024; Extended Info  Returns all movies updated since the specified UTC date and time. We recommended storing the &#x60;X-Start-Date&#x60; header you can be efficient using this method moving forward. By default, &#x60;10&#x60; results are returned. You can send a &#x60;limit&#x60; to get up to &#x60;100&#x60; results per page.  **Important!** The &#x60;start_date&#x60; is only accurate to the hour, for caching purposes. Please drop the minutes and seconds from your timestamp to help optimize our cached data. For example, use &#x60;2021-07-17T12:00:00Z&#x60; and not &#x60;2021-07-17T12:23:34Z&#x60;.  **Note:** The &#x60;start_date&#x60; can only be a maximum of 30 days in the past.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String startDate = "2020-11-27T00:00:00Z"; // String | Updated since this date and time.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getRecentlyUpdatedMovies(startDate, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#getRecentlyUpdatedMovies");
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
| **startDate** | **String**| Updated since this date and time. | |
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
| **200** | OK |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  * X-Start-Date -  <br>  |

<a id="getRelatedMovies"></a>
# **getRelatedMovies**
> getRelatedMovies(id, traktApiVersion, traktApiKey)

Get related movies

#### &amp;#128196; Pagination &amp;#10024; Extended Info  Returns related and similar movies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getRelatedMovies(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#getRelatedMovies");
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

<a id="getTheMostAnticipatedMovies"></a>
# **getTheMostAnticipatedMovies**
> getTheMostAnticipatedMovies(traktApiVersion, traktApiKey)

Get the most anticipated movies

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most anticipated movies based on the number of lists a movie appears on.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getTheMostAnticipatedMovies(traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#getTheMostAnticipatedMovies");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  |

<a id="getTheMostCollectedMovies"></a>
# **getTheMostCollectedMovies**
> getTheMostCollectedMovies(period, traktApiVersion, traktApiKey)

Get the most Collected movies

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most collected (unique users) movies in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String period = "daily"; // String | Time period.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getTheMostCollectedMovies(period, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#getTheMostCollectedMovies");
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
| **period** | **String**| Time period. | [enum: daily, weekly, monthly, yearly, all] |
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

<a id="getTheMostPlayedMovies"></a>
# **getTheMostPlayedMovies**
> getTheMostPlayedMovies(period, traktApiVersion, traktApiKey)

Get the most played movies

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most played (a single user can watch multiple times) movies in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String period = "daily"; // String | Time period.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getTheMostPlayedMovies(period, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#getTheMostPlayedMovies");
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
| **period** | **String**| Time period. | [enum: daily, weekly, monthly, yearly, all] |
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

<a id="getTheMostRecommendedMovies"></a>
# **getTheMostRecommendedMovies**
> getTheMostRecommendedMovies(period, traktApiVersion, traktApiKey)

Get the most recommended movies

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most recommended movies in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String period = "daily"; // String | Time period.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getTheMostRecommendedMovies(period, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#getTheMostRecommendedMovies");
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
| **period** | **String**| Time period. | [enum: daily, weekly, monthly, yearly, all] |
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

<a id="getTheMostWatchedMovies"></a>
# **getTheMostWatchedMovies**
> getTheMostWatchedMovies(period, traktApiVersion, traktApiKey)

Get the most watched movies

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most watched (unique users) movies in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String period = "daily"; // String | Time period.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getTheMostWatchedMovies(period, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#getTheMostWatchedMovies");
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
| **period** | **String**| Time period. | [enum: daily, weekly, monthly, yearly, all] |
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

<a id="getTheWeekendBoxOffice"></a>
# **getTheWeekendBoxOffice**
> getTheWeekendBoxOffice(traktApiVersion, traktApiKey)

Get the weekend box office

#### &amp;#10024; Extended Info  Returns the top 10 grossing movies in the U.S. box office last weekend. Updated every Monday morning.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getTheWeekendBoxOffice(traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#getTheWeekendBoxOffice");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getTrendingMovies"></a>
# **getTrendingMovies**
> getTrendingMovies(traktApiVersion, traktApiKey)

Get trending movies

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns all movies being watched right now. Movies with the most users are returned first.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getTrendingMovies(traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#getTrendingMovies");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  * X-Trending-User-Count -  <br>  |

<a id="getUsersWatchingRightNow"></a>
# **getUsersWatchingRightNow**
> getUsersWatchingRightNow(id, traktApiVersion, traktApiKey)

Get users watching right now

#### &amp;#10024; Extended Info  Returns all users watching this movie right now.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoviesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    MoviesApi apiInstance = new MoviesApi(defaultClient);
    String id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getUsersWatchingRightNow(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoviesApi#getUsersWatchingRightNow");
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

